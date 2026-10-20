#!/usr/bin/env python3
"""Run official website generator in an isolated Java 25 process, never a game launch."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import os
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'build/website-trial'
DEPS = OUT / 'generator-dependencies'
JAVA = Path('/home/tsb/.local/share/ModrinthApp/meta/java_versions/zulu25.36.205-ca-jre25.0.4.1-linux_x64/bin/java')
GENERATOR = Path('/home/tsb/.hermes/cache/scratch/guideme-website-research/26.3.4-alpha.jar')
DEPS.mkdir(parents=True, exist_ok=True)
assert (OUT / 'exported/en_us/index.json').is_file(), 'Run the game export first; no real exported index exists yet.'

def fetch(entry):
    target = DEPS / entry.get('path', 'minecraft-26.3-client.jar')
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or hashlib.sha1(target.read_bytes()).hexdigest() != entry['sha1']:
        target.write_bytes(urllib.request.urlopen(entry['url'], timeout=60).read())
    assert hashlib.sha1(target.read_bytes()).hexdigest() == entry['sha1'], target
    return str(target)

manifest = json.load(urllib.request.urlopen('https://piston-meta.mojang.com/mc/game/version_manifest_v2.json'))
version = next(x for x in manifest['versions'] if x['id'] == '26.3')
metadata = json.load(urllib.request.urlopen(version['url']))
(DEPS / 'version.json').write_text(json.dumps(metadata, indent=2))
artifacts = [metadata['downloads']['client']]
artifacts.extend(lib['downloads']['artifact'] for lib in metadata['libraries'] if 'artifact' in lib.get('downloads', {}))
with ThreadPoolExecutor(max_workers=8) as pool:
    jars = list(pool.map(fetch, artifacts))
ecj = DEPS / 'ecj-3.44.0.jar'
if not ecj.exists():
    ecj.write_bytes(urllib.request.urlopen('https://repo.maven.apache.org/maven2/org/eclipse/jdt/ecj/3.44.0/ecj-3.44.0.jar').read())
classes = OUT / 'web-extension-classes'
classes.mkdir(exist_ok=True)
subprocess.run([str(JAVA), '-jar', str(ecj), '-25', '-proc:none', '-cp', str(GENERATOR), '-d', str(classes),
                str(Path(__file__).with_name('EmiSearchWebFallback.java'))], check=True)
service = classes / 'META-INF/services/guideme.web.CustomElementWebRenderer'
service.parent.mkdir(parents=True, exist_ok=True)
service.write_text('dev.astropunk.website.EmiSearchWebFallback\n')
command = [str(JAVA), '-cp', os.pathsep.join([str(classes), str(GENERATOR), *jars]), 'guideme.web.WebSiteGenerator',
           '--data', str(OUT / 'exported/en_us'), '--output', str(OUT / 'website/en_us'), '--title', 'Astropunk Handbook trial']
print(' '.join(command), flush=True)
raise SystemExit(subprocess.call(command))
