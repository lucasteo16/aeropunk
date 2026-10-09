#!/usr/bin/env python3
"""Run selected-release structural compiler, preserving the registry boundary explicitly.

This does not launch Minecraft. A mapped vanilla 1.21.1 artifact supplies a real
vanilla registry for native slot creation. Mod item identifiers are normalized
in the parsed tree by the Java probe, never in player-facing source. KeyBind and
Recipe remain explicit untested client-runtime boundaries.
"""
from pathlib import Path
import argparse
import json
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[2]
ACCESS = ROOT / 'scripts/handbook-access'

def run(fragment=None, pages=None, authored_only=False, label='markup', include_orphans=False):
    output = ROOT / 'build/handbook-access/markup-probe' / label
    output.mkdir(parents=True, exist_ok=True)
    fixtures = output / 'pages'
    if fixtures.exists():
        shutil.rmtree(fixtures)
    fixtures.mkdir(exist_ok=True)
    source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
    overlay = json.loads(Path(fragment).read_text()) if fragment else {}
    if authored_only:
        for topic, locales in source.items():
            for locale, body in locales.items():
                target = fixtures / locale / (topic + '.md')
                target.parent.mkdir(exist_ok=True)
                target.write_text(overlay.get(topic, {}).get(locale, body))
    else:
        pages = Path(pages or ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook')
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        expected = {entry['filename'] for entry in manifest['pages']} | {'index.md', 'quick-reference.md'}
        selected = set()
        for page in pages.rglob('*.md'):
            relative = page.relative_to(pages)
            if not include_orphans and page.name not in expected:
                print(f'Excluded stale page outside manifest: {relative}')
                continue
            selected.add(('zh_cn' if '_zh_cn' in relative.parts else 'en_us', page.name))
            target = fixtures / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            body = page.read_text()
            topic, locale = page.stem, 'zh_cn' if '_zh_cn' in relative.parts else 'en_us'
            if topic in overlay and overlay[topic][locale] != source[topic][locale]:
                old = source[topic][locale]
                if body.count(old) != 1:
                    raise AssertionError(f'Cannot safely overlay {page}: authored body occurs {body.count(old)} times')
                body = body.replace(old, overlay[topic][locale], 1)
            target.write_text(body)
        if not include_orphans:
            assert selected == {(locale, name) for locale in ('en_us', 'zh_cn') for name in expected}, 'Manifest locale parity failed'
    count = len(list(fixtures.rglob('*.md')))
    cp = (ACCESS / 'build/access-probe-classpath.txt').read_text().strip().split(':')
    cache = ROOT / 'build/handbook-access/.gradle-user-home/caches/neoformruntime/intermediate_results'
    vanilla = list(cache.glob('rename_*_output.jar'))
    if len(vanilla) != 1:
        raise AssertionError('Expected one mapped vanilla artifact for the registry-only boundary')
    native_game = [p for p in cp if p.endswith('artifacts/neoforge-21.1.255.jar')]
    cp = [str(vanilla[0]) if p.endswith('artifacts/neoforge-21.1.255.jar') else p for p in cp]
    cp.append(str(ACCESS / 'build/libs/astropunk-handbook-access-1.0.0.jar'))
    cp.extend(native_game)  # Loader-only types, vanilla classes take precedence.
    cp.append(str(ACCESS / 'build/moddev/artifacts/neoforge-21.1.255-client-extra-aka-minecraft-resources.jar'))
    classes = output / 'classes'
    classes.mkdir(exist_ok=True)
    java = ACCESS / 'toolchain/jdk-21.0.12.1+1/bin'
    subprocess.run([str(java / 'javac'), '-proc:none', '-cp', ':'.join(cp), '-d', str(classes),
                    str(ACCESS / 'syntax-validation/VerifyNativeItemGrid.java')], check=True)
    result = subprocess.run([str(java / 'java'), '-cp', ':'.join([str(classes), *cp]),
                             'VerifyNativeItemGrid', str(fixtures), str(count)], capture_output=True, text=True)
    log = result.stdout + result.stderr
    (output / 'compiler.log').write_text(log)
    for line in log.splitlines():
        if any(token in line for token in ('SUMMARY', 'CONTROLS', 'BOUNDARIES', 'FAIL ', 'Exception', 'AssertionError')):
            print(line)
    print(f'Native compiler exit {result.returncode}, {count} pages, evidence {output / "compiler.log"}')
    return result.returncode

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fragment')
    parser.add_argument('--pages')
    parser.add_argument('--authored-only', action='store_true')
    parser.add_argument('--include-orphans', action='store_true')
    parser.add_argument('--label', default='markup')
    args = parser.parse_args()
    raise SystemExit(run(args.fragment, args.pages, args.authored_only, args.label, args.include_orphans))
