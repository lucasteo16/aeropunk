#!/usr/bin/env python3
"""Stage only repository content and read-only instance mod copies in ignored build output."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'build/website-trial'
HELPER = ROOT / 'scripts/handbook-access'
MODS = Path('/home/tsb/.local/share/ModrinthApp/profiles/astropunk-0.17.0-hosting-modrinth/mods')
OUT.mkdir(parents=True, exist_ok=True)
shutil.copy2(Path(__file__).with_name('build.gradle'), OUT / 'build.gradle')
for name in ('gradlew', 'gradle.properties', 'settings.gradle'):
    shutil.copy2(HELPER / name, OUT / name)
shutil.copytree(HELPER / 'gradle', OUT / 'gradle', dirs_exist_ok=True)
shutil.copytree(HELPER / 'src/main', OUT / 'src/main', dirs_exist_ok=True)
shutil.copy2(Path(__file__).with_name('WebsiteExportBridge.java'), OUT / 'src/main/java/dev/astropunk/handbook/WebsiteExportBridge.java')
run = OUT / 'run'
(run / 'mods').mkdir(parents=True, exist_ok=True)
selected = []
for source in sorted(MODS.glob('*.jar')):
    if source.name.startswith('astropunk-handbook-access-'):
        continue
    shutil.copy2(source, run / 'mods' / source.name)
    selected.append({'filename': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
for name in ('guideme-21.1.19.jar', 'emi-1.1.24+1.21.1+neoforge.jar'):
    shutil.copy2(MODS / name, OUT / name)
shutil.copytree(ROOT / 'resourcepacks/astropunk-guide-preview', run / 'resourcepacks/astropunk-guide-preview', dirs_exist_ok=True)
(run / 'options.txt').write_text('resourcePacks:["vanilla","mod_resources","file/astropunk-guide-preview"]\nlang:en_us\n')
(OUT / 'selected-mods.json').write_text(json.dumps(selected, indent=2) + '\n')
print(f'Staged {len(selected)} instance mod copies at {run}; no worlds or account data copied.')
