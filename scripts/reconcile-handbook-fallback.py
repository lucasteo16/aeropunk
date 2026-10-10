#!/usr/bin/env python3
"""Reconcile an explicitly selected normal fallback resource-pack folder.

Only this handbook resource pack is changed. Archive every replaced or retired file
outside the resource pack before changing it. Never mutate a launcher profile,
Minecraft configuration, mod, world, or loaded Java class. A successful copy does
not prove a running client reloaded its resources.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'resourcepacks/astropunk-guide-preview'
REL = Path('assets/astropunk/guides/astropunk/handbook')
REGISTRATION = Path('assets/astropunk/guideme_guides/handbook.json')


def reconcile(target, archive):
    target = target.resolve()
    archive = archive.resolve()
    assert target != SOURCE.resolve(), 'Use the generator for the source pack'
    assert target.is_dir() and not target.is_symlink(), 'Target must be an existing normal folder'
    assert (target / 'pack.mcmeta').is_file(), 'Target must be the selected resource-pack root'
    assert not archive.is_relative_to(target), 'Archive must remain outside the distributed pack'
    definition = json.loads((SOURCE / REGISTRATION).read_text()) if (SOURCE / REGISTRATION).exists() else None
    if definition is not None:
        assert set(definition) <= {'default_language', 'item_settings', 'custom_colors'}
    archive.mkdir(parents=True, exist_ok=True)
    old_pages = {p.relative_to(target) for p in (target / REL).rglob('*.md')}
    wanted_pages = {p.relative_to(SOURCE) for p in (SOURCE / REL).rglob('*.md')}
    source_files = [p for p in SOURCE.rglob('*') if p.is_file()]
    changes = {p.relative_to(SOURCE) for p in source_files if not (target / p.relative_to(SOURCE)).is_file() or p.read_bytes() != (target / p.relative_to(SOURCE)).read_bytes()}
    obsolete = old_pages - wanted_pages
    if definition is None and (target / REGISTRATION).exists():
        obsolete.add(REGISTRATION)
    existing = sorted(p for p in changes | obsolete | {REGISTRATION} if (target / p).is_file())
    record = []
    for rel in existing:
        original = target / rel
        digest = hashlib.sha256(original.read_bytes()).hexdigest()
        saved = archive / digest / rel
        saved.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(original, saved)
        assert saved.read_bytes() == original.read_bytes(), rel
        record.append({'path': rel.as_posix(), 'sha256': digest, 'archive': str(saved)})
    for rel in obsolete:
        (target / rel).unlink()
    for source in source_files:
        rel = source.relative_to(SOURCE)
        if rel not in changes:
            continue
        destination = target / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(destination.name + '.tmp')
        shutil.copy2(source, temporary)
        temporary.replace(destination)
    for source in source_files:
        assert source.read_bytes() == (target / source.relative_to(SOURCE)).read_bytes(), source
    assert {p.relative_to(target) for p in (target / REL).rglob('*.md')} == wanted_pages
    if definition is None:
        assert not (target / REGISTRATION).exists(), 'Resource definitions would override native query extensions'
    else:
        assert json.loads((target / REGISTRATION).read_text()) == definition
    report = {'target': str(target), 'archived_files': record, 'retired_pages': sorted(p.as_posix() for p in obsolete), 'changed_files': len(changes), 'verified_resource_files': len(source_files), 'client_reload_verified': False}
    (archive / 'reconciliation.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('resource_pack', type=Path)
    parser.add_argument('--archive', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(reconcile(args.resource_pack, args.archive), indent=2))
