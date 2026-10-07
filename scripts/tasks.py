"""Scoped filesystem maintenance and disposable test reporting."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess


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
    diagnostics = directory / 'startup-diagnostics.log'
    (reports / 'startup-diagnostics.log').write_text(diagnostics.read_text() if diagnostics.exists() else '')
    (reports / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f'Reports: {reports / "result.json"}, {reports / "server.log"}, {reports / "startup-diagnostics.log"}', flush=True)
    if (directory / 'compose.json').exists():
        cleanup = directory / 'cleanup.json'
        if not cleanup.exists() or json.loads(cleanup.read_text()) != {'containers': [], 'networks': []}:
            print(f'Runtime retained: Docker cleanup unconfirmed: {directory}', flush=True)
            return
    print('Temporary cleanup before: ' + json.dumps(summary([directory])), flush=True)
    shutil.rmtree(directory)
    print('Temporary cleanup after: ' + json.dumps(summary([])), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task', choices=['clean'])
    parser.parse_args()
    clean(Path(__file__).resolve().parents[1])
