"""Retain a bounded number of complete, versioned Astropunk distributions."""
import argparse
import json
from pathlib import Path
import re
import shutil
import tomllib
import zipfile


ARTIFACT = re.compile(
    r'^astropunk-(?P<version>\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?)'
    r'-(?:live-client|live-server|modrinth|curseforge|server|standalone)(?:\.mrpack|\.zip)?$'
)


def version_key(version):
    base, _, suffix = version.partition('-')
    return (*map(int, base.split('.')), suffix)


def verify_export(path, expected):
    """Check completed native archives before allowing retention to run."""
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError('Archive integrity check failed')
        if 'modrinth.index.json' in archive.namelist():
            manifest = json.loads(archive.read('modrinth.index.json'))
            name, version = manifest['name'], manifest['versionId']
        elif 'manifest.json' in archive.namelist():
            manifest = json.loads(archive.read('manifest.json'))
            name, version = manifest['name'], manifest['version']
        else:
            raise ValueError('No native pack manifest in export')
        if name != 'Astropunk' or version != expected:
            raise ValueError(f'Unexpected pack identity: {name!r}, {version!r}')


def candidates(root, keep):
    if keep < 1:
        raise ValueError('At least one release must be retained')
    root = Path(root).resolve()
    directory = root / 'dist'
    if directory.is_symlink():
        raise ValueError('Distribution directory cannot be a symbolic link')
    pack = tomllib.loads((root / 'pack.toml').read_text())
    if pack['name'] != 'Astropunk':
        raise ValueError('Pack name must be Astropunk')
    groups = {}
    for path in directory.iterdir() if directory.exists() else []:
        match = ARTIFACT.fullmatch(path.name)
        if match:
            if path.is_symlink():
                raise ValueError(f'Symbolic link rejected: {path}')
            if path.is_dir() and not path.name.endswith('-live-server'):
                raise ValueError(f'Unexpected artifact directory: {path}')
            groups.setdefault(match['version'], []).append(path)
    current = pack['version']
    if current not in groups:
        raise ValueError('Current release must exist before old releases can be removed')
    versions = sorted(groups, key=version_key, reverse=True)
    if versions[0] != current:
        raise ValueError('A newer or different edition exists; inspect it before pruning')
    return [path for version in versions[keep:] for path in groups[version]]


def prune(root, keep=2, apply=False):
    paths = candidates(root, keep)
    # Preflight the entire selection before deleting anything.
    for path in paths:
        if path.is_dir() and any(child.is_symlink() for child in path.rglob('*')):
            raise ValueError(f'Symbolic link inside artifact rejected: {path}')
    for path in paths:
        print(('Removing ' if apply else 'Would remove ') + str(path), flush=True)
        if apply:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    return paths


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--keep', type=int, default=2)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--after-export', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.after_export:
        path = args.after_export.resolve()
        # Custom export destinations do not authorize cleaning the standard dist.
        if path.parent != root / 'dist':
            print('Custom output: standard distribution retention skipped')
            raise SystemExit(0)
        expected = tomllib.loads((root / 'pack.toml').read_text())['version']
        verify_export(path, expected)
    prune(root, args.keep, args.apply)
