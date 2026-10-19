#!/usr/bin/env python3
"""Build a disposable native Combat comparison pack from a frozen baseline."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import struct
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'resourcepacks/astropunk-guide-preview'
REL = Path('assets/astropunk/guides/astropunk/handbook')
PAGES = PACK / REL
WORK = ROOT / 'build/combat-review'
SNAPSHOT = WORK / 'baseline'
MANIFEST = SNAPSHOT / 'manifest.json'
LOCALES = ('', '_zh_cn')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def icon():
    """Original decorative play glyph, not an instructional illustration."""
    width, height = 64, 48
    rows = bytearray()
    for y in range(height):
        rows.append(0)
        for x in range(width):
            red = 3 <= x < 61 and 4 <= y < 44
            triangle = 25 <= x <= 43 and abs(y - 24) <= (43 - x) * 0.65
            rows.extend((255, 255, 255, 255) if triangle else
                        (210, 36, 44, 255) if red else (0, 0, 0, 0))
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(bytes(rows))) + chunk(b'IEND', b'')
    target = PAGES / 'images/tutorial-video.png'
    target.write_bytes(png)
    print(json.dumps({'icon': str(target), 'sha256': digest(png), 'dimensions': [width, height]}))


def tree():
    parents = {}
    for page in PAGES.glob('*.md'):
        match = re.search(r'^  parent: (.+)$', page.read_text(), re.M)
        parents[page.name] = match.group(1).strip('"') if match else None
    selected = {'reference.skills.md'}
    while True:
        expanded = selected | {name for name, parent in parents.items() if parent in selected}
        if expanded == selected:
            return sorted(selected)
        selected = expanded


def snapshot():
    if MANIFEST.exists():
        raise SystemExit('Baseline already exists. Refusing to replace the comparison original.')
    names = tree()
    records = {}
    for locale in LOCALES:
        for name in names:
            relative = Path(locale) / name
            data = (PAGES / relative).read_bytes()
            destination = SNAPSHOT / 'pages' / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            records[relative.as_posix()] = digest(data)
    content = ROOT / 'docs/handbook-content.json'
    shutil.copy2(content, SNAPSHOT / 'handbook-content.json')
    all_pages = {p.relative_to(PAGES).as_posix(): digest(p.read_bytes())
                 for p in PAGES.rglob('*.md')}
    manifest = {'topics': names, 'original_pages': records,
                'all_pages': all_pages, 'content_hash': digest(content.read_bytes())}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'topics': len(names), 'localized_pages': len(records),
                      'baseline': str(SNAPSHOT)}, indent=2))


def clone_original(text, names, chinese):
    front, body = text.split('---', 2)[1:]
    # Only current pages own contextual item associations. Duplicate ownership is ambiguous.
    front = re.sub(r'^item_ids:\n(?:  - .*\n)*', '', front, flags=re.M)
    is_root = not re.search(r'^  parent:', front, re.M)
    for name in names:
        text_name = 'combat-old.' + name
        front = re.sub(r'(?m)^(  parent: )' + re.escape(name) + r'$',
                       lambda match: match.group(1) + text_name, front)
        body = re.sub(r'(?<=\()' + re.escape(name) + r'(?=[#)])', text_name, body)
    if is_root:
        label = '战斗（旧版）' if chinese else 'Combat (old)'
        front = re.sub(r'^  title: .*$', '  title: ' + json.dumps(label, ensure_ascii=False),
                       front, flags=re.M)
        front = re.sub(r'^  position: .*$', '  position: 9', front, flags=re.M)
        body = re.sub(r'^# .*$', '# ' + label, body, count=1, flags=re.M)
    return '---' + front + '---' + body


def build():
    manifest = json.loads(MANIFEST.read_text())
    names = manifest['topics']
    output = WORK / 'Astropunk-Combat-Comparison'
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    shutil.copy2(PACK / 'pack.mcmeta', output / 'pack.mcmeta')
    # This is an overlay for the existing handbook, not an older replacement
    # for every unrelated page or a second copy of all publisher artwork.
    for locale in LOCALES:
        target = output / REL / locale
        target.mkdir(parents=True, exist_ok=True)
        for page in (PAGES / locale).glob('*.md'):
            text = page.read_text()
            front = text.split('---', 2)[1]
            position = re.search(r'^  position: (-?\d+)$', front, re.M)
            shifted_root = (not re.search(r'^  parent:', front, re.M) and position
                            and 9 <= int(position.group(1)) < 10000)
            if page.name in names or shifted_root:
                shutil.copy2(page, target / page.name)
    image = output / REL / 'images/tutorial-video.png'
    image.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PAGES / 'images/tutorial-video.png', image)
    meta = json.loads((output / 'pack.mcmeta').read_text())
    meta['pack']['description'] = 'Astropunk: Combat and Combat (old) comparison'
    (output / 'pack.mcmeta').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    for locale in LOCALES:
        target = output / REL / locale
        for name in names:
            relative = Path(locale) / name
            original = (SNAPSHOT / 'pages' / relative).read_bytes()
            assert digest(original) == manifest['original_pages'][relative.as_posix()]
            clone = clone_original(original.decode(), names, bool(locale))
            (target / ('combat-old.' + name)).write_text(clone)
        # Make room for the temporary root directly below Combat, only in this pack.
        for page in target.glob('*.md'):
            if page.name.startswith('combat-old.'):
                continue
            text = page.read_text()
            front = text.split('---', 2)[1]
            if re.search(r'^  parent:', front, re.M):
                continue
            position = re.search(r'^  position: (-?\d+)$', front, re.M)
            if position and 9 <= int(position.group(1)) < 10000:
                text = re.sub(r'(?m)^(  position: )(-?\d+)$',
                              lambda m: m.group(1) + str(int(m.group(2)) + 1), text, count=1)
                page.write_text(text)
    archive = WORK / 'Astropunk-Combat-Comparison.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for file in sorted(output.rglob('*')):
            if file.is_file():
                z.write(file, file.relative_to(output).as_posix())
    report = verify(output, archive, manifest)
    (WORK / 'comparison-verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


def verify(output, archive, manifest):
    pages = output / REL
    names = manifest['topics']
    old_count = 0
    checked_links = 0
    for locale in LOCALES:
        folder = pages / locale
        for name in names:
            old = folder / ('combat-old.' + name)
            expected = clone_original((SNAPSHOT / 'pages' / locale / name).read_text(), names, bool(locale))
            assert old.read_text() == expected, old
            assert not re.search(r'^item_ids:', expected, re.M), old
            old_count += 1
        for page in folder.glob('*.md'):
            text = page.read_text()
            parent = re.search(r'^  parent: (.+)$', text, re.M)
            if parent:
                parent_name = parent.group(1).strip('"')
                assert ((folder / parent_name).exists() or (PAGES / locale / parent_name).exists()), (page, parent_name)
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in link or link.startswith('#'):
                    continue
                path = link.split('#', 1)[0]
                if not path:
                    continue
                target = page.parent / path
                fallback = PAGES / locale / path
                shared = PAGES / path
                assert target.exists() or fallback.exists() or shared.exists(), (page, link)
                checked_links += 1
        merged = {p.name: p.read_text() for p in (PAGES / locale).glob('*.md')}
        merged.update({p.name: p.read_text() for p in folder.glob('*.md')})
        groups = {}
        for name, text in merged.items():
            front = text.split('---', 2)[1]
            parent = re.search(r'^  parent: (.+)$', front, re.M)
            parent = parent.group(1) if parent else None
            position_match = re.search(r'^  position: (-?\d+)$', front, re.M)
            assert position_match is not None, name
            position = int(position_match.group(1))
            groups.setdefault(parent, []).append((position, name))
            seen = {name}
            while parent:
                assert parent not in seen and parent in merged, (name, parent)
                seen.add(parent)
                assert len(seen) <= 3, (name, 'excessive navigation depth')
                match = re.search(r'^  parent: (.+)$', merged[parent], re.M)
                parent = match.group(1) if match else None
        for parent, siblings in groups.items():
            assert len({p for p, _ in siblings}) == len(siblings), ('duplicate position', parent)
        roots = [name for _, name in sorted(groups[None])]
        assert roots[roots.index('reference.skills.md') + 1] == 'combat-old.reference.skills.md'
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for file in output.rglob('*'):
            if file.is_file():
                assert z.read(file.relative_to(output).as_posix()) == file.read_bytes()
    return {'topics_per_tree': len(names), 'old_localized_pages': old_count,
            'new_localized_pages': len(names) * len(LOCALES),
            'checked_local_links': checked_links, 'old_preserved_except_navigation_and_associations': True,
            'archive_bytes_verified': True, 'requires_base_handbook': True, 'archive': str(archive),
            'pack_folder': str(output), 'rendered_review': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('snapshot', 'build', 'icon'))
    args = parser.parse_args()
    {'snapshot': snapshot, 'build': build, 'icon': icon}[args.action]()
