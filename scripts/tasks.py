"""Small export and scoped filesystem maintenance tasks."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def safe_path(root, path):
    root = root.resolve()
    path = Path(path)
    if '..' in path.parts or not path.is_relative_to(root):
        raise ValueError(f'Unsafe path: {path}')
    for part in [path, *path.parents]:
        if part == root:
            break
        if part.is_symlink():
            raise ValueError(f'Symlink rejected: {part}')
    if path.is_dir():
        for child in path.rglob('*'):
            if child.is_symlink():
                raise ValueError(f'Symlink rejected: {child}')
    return path


def summary(paths):
    files = [item for path in paths for item in ([path] if path.is_file() else path.rglob('*')) if item.is_file()]
    return {'paths': len(paths), 'files': len(files), 'bytes': sum(item.stat().st_size for item in files)}


def clean(root):
    safe_path(root, root / 'build')
    paths = [p for p in (root / 'build').glob('*') if p.name.startswith(('smoke-', 'unit-', 'startup-'))]
    bytecode_dirs = list(root.rglob('__pycache__'))
    paths += bytecode_dirs
    paths += [p for p in root.rglob('*.pyc')
              if not any(p.is_relative_to(d) for d in bytecode_dirs)]
    for path in paths:
        safe_path(root, path)
    # Read only resource check. Never stop or remove a container from clean.
    for path in paths:
        if (path / 'compose.json').is_file():
            project = 'aeropunk-' + path.name.lower()
            active = subprocess.run(['docker', 'ps', '--all', '-q', '--filter', f'label=com.docker.compose.project={project}'], capture_output=True, text=True, check=True)
            networks = subprocess.run(['docker', 'network', 'ls', '-q', '--filter',
                                       f'label=com.docker.compose.project={project}'],
                                      capture_output=True, text=True, check=True)
            if active.stdout.strip() or networks.stdout.strip():
                raise ValueError(f'Docker resources use {path}; refusing cleanup')
    print('Cleanup before: ' + json.dumps(summary(paths)), flush=True)
    for path in paths:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    print('Cleanup after: ' + json.dumps(summary([p for p in paths if p.exists()])), flush=True)


def capture(root, directory, result):
    safe_path(root, directory)
    reports = safe_path(root, root / 'reports')
    reports.mkdir(exist_ok=True)
    (reports / 'server.log').write_text((directory / 'server.log').read_text() if (directory / 'server.log').exists() else '')
    (reports / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f'Reports: {reports / "result.json"}, {reports / "server.log"}', flush=True)
    if (directory / 'compose.json').exists():
        cleanup = directory / 'cleanup.json'
        if not cleanup.exists() or json.loads(cleanup.read_text()) != {'containers': [], 'networks': []}:
            print(f'Runtime retained: Docker cleanup unconfirmed: {directory}', flush=True)
            return
    print('Temporary cleanup before: ' + json.dumps(summary([directory])), flush=True)
    shutil.rmtree(directory)
    print('Temporary cleanup after: ' + json.dumps(summary([])), flush=True)


def native_export(root, directory, side):
    stage = directory / 'pack'
    stage.mkdir()
    for name in ('pack.toml', 'index.toml', '.packwizignore'):
        if (root / name).exists():
            shutil.copy2(root / name, stage / name)
    for name in ('mods', 'config'):
        if (root / name).exists():
            shutil.copytree(root / name, stage / name)
    subprocess.run(['packwiz', 'curseforge', 'export', '--side', side],
                   cwd=stage, check=True, timeout=180)
    archives = list(stage.glob('*.zip'))
    if len(archives) != 1:
        raise ValueError(f'Expected one native export archive, got {archives}')
    import zipfile
    archive = archives[0]
    with zipfile.ZipFile(archive) as exported:
        if exported.testzip():
            raise ValueError('Corrupt export archive')
        manifest = json.loads(exported.read('manifest.json'))
        if manifest.get('files'):
            raise ValueError('Unresolved CurseForge manifest references: export is not fully materialized')
    return archive


def export(root, side):
    from test_server import extract_server_export
    import tomllib
    dist = safe_path(root, root / 'dist')
    dist.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.export-', dir=dist) as tmp:
        directory = Path(tmp)
        archive = native_export(root, directory, side)
        if side == 'server':
            versions = tomllib.loads((root / 'pack.toml').read_text())['versions']
            metadata = [tomllib.loads(p.read_text()) for p in (root / 'mods').glob('*.pw.toml')]
            expected = {m['filename'] for m in metadata if m.get('side', 'both') != 'client'}
            extract_server_export(archive, directory / 'runtime', versions, expected)
        destination = safe_path(root, dist / side)
        destination.mkdir(exist_ok=True)
        target = safe_path(root, destination / archive.name)
        archive.replace(target)
        if side == 'server':
            legacy = safe_path(root, dist / 'aeropunk-server.zip')
            legacy.unlink(missing_ok=True)
        print(f'Validated export: {target} ({target.stat().st_size} bytes)', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task', choices=['export', 'export-client', 'clean'])
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.task == 'clean':
        clean(root)
    else:
        export(root, 'client' if args.task == 'export-client' else 'server')
