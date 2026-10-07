#!/usr/bin/env python3
"""Export the server pack and check disposable Docker startup and normal shutdown."""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import shutil
import time
import tomllib
import uuid
import zipfile


def new_run(root, label='smoke'):
    directory = root / 'build' / f'{label}-{time.strftime("%Y%m%d-%H%M%S")}-{uuid.uuid4().hex[:8]}'
    directory.mkdir(parents=True)
    return directory


def build_server_export(root, directory):
    # Packwiz owns archive generation. The existing Docker installer owns
    # downloads, server-side selection, override extraction and loader setup.
    archive = directory / 'server.mrpack'
    subprocess.run(['packwiz', 'modrinth', 'export', '--output', str(archive)],
                   cwd=root, check=True, timeout=300)
    with zipfile.ZipFile(archive) as exported:
        if exported.testzip():
            raise ValueError('Corrupt exported archive')
        index = json.loads(exported.read('modrinth.index.json'))
        versions = index['dependencies']
        expected = tomllib.loads((root / 'pack.toml').read_text())['versions']
        if versions != expected:
            raise ValueError(f'Export versions differ from pack.toml: {versions}')
        for item in exported.infolist():
            path = Path(item.filename)
            if (path.is_absolute() or '..' in path.parts or '\\' in item.filename
                    or (item.external_attr >> 16) & 0o170000 == 0o120000):
                raise ValueError(f'Unsafe archive path: {item.filename}')
    return {'versions': versions, 'format': 'modrinth', 'archive': str(archive),
            'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
            'installer': 'mc-image-helper install-modrinth-modpack'}


TRANSIENT_DIRECTORIES = {'world': 'smoke-world', 'config': 'config',
                         'defaultconfigs': 'defaultconfigs', 'logs': 'logs',
                         'crash-reports': 'crash-reports', 'mixin-output': '.mixin.out',
                         'generated-data-packs': 'dynamic-data-pack-cache',
                         'global-data-packs': 'moonlight-global-datapacks'}


def clean_runtime(root, runtime, diagnostics=None):
    from tasks import safe_path
    dumps = sorted(runtime.glob('streamsreflowing-stall-*.txt'))
    if dumps and diagnostics is not None:
        (diagnostics / 'startup-diagnostics.log').write_text('\n'.join(safe_path(root, p).read_text() for p in dumps))
    for path in dumps:
        safe_path(root, path).unlink()
    # Installed binaries and native installer metadata remain. Test state does not.
    for name in ('server.properties', 'eula.txt', 'ops.json', 'whitelist.json',
                 'banned-players.json', 'banned-ips.json', 'usercache.json',
                 'usernamecache.json', '.rcon-cli.env', '.rcon-cli.yaml'):
        safe_path(root, runtime / name).unlink(missing_ok=True)
    for name in TRANSIENT_DIRECTORIES.values():
        path = safe_path(root, runtime / name)
        if path.is_dir():
            shutil.rmtree(path)


def prepare_runtime(root, directory, fresh=False):
    from tasks import safe_path
    runtime = safe_path(root, directory / 'runtime' if fresh else root / 'build' / 'server-installation')
    runtime.mkdir(parents=True, exist_ok=True)
    clean_runtime(root, runtime)
    # The native helper skips existing filenames. Remove a mismatching artifact
    # before handing downloads to it, including same-filename version changes.
    with zipfile.ZipFile(directory / 'server.mrpack') as archive:
        index = json.loads(archive.read('modrinth.index.json'))
    reused = invalidated = 0
    for item in index['files']:
        path = safe_path(root, runtime / item['path'])
        if path.is_file():
            algorithm = 'sha512' if 'sha512' in item['hashes'] else 'sha1'
            with path.open('rb') as stream:
                actual_hash = hashlib.file_digest(stream, algorithm).hexdigest()
            if actual_hash != item['hashes'][algorithm]:
                path.unlink()
                invalidated += 1
            else:
                reused += 1
    for name in TRANSIENT_DIRECTORIES:
        (directory / name).mkdir()
    print(f'Installation: {runtime}; verified reusable files: {reused}; invalidated files: {invalidated}', flush=True)
    return runtime


class PhaseReport:
    def __init__(self):
        self.phases = []
        self.current = None
        self.started = None
        self.failure_phase = None

    def start(self, name):
        self.finish()
        self.current = {'name': name, 'status': 'running'}
        self.started = time.monotonic()
        self.phases.append(self.current)
        print(f'[{name}] START', flush=True)

    def finish(self):
        if self.current is not None and self.current['status'] == 'running':
            self.current['status'] = 'completed'
            self.current['elapsed_seconds'] = round(time.monotonic() - self.started, 3)
            print(f'[{self.current["name"]}] COMPLETE after {self.current["elapsed_seconds"]} seconds', flush=True)

    def fail(self, error):
        if self.current is not None:
            self.current['status'] = 'failed'
            self.current['elapsed_seconds'] = round(time.monotonic() - self.started, 3)
            self.current['error'] = f'{type(error).__name__}: {error}'
            if self.failure_phase is None:
                self.failure_phase = self.current['name']
            print(f'[{self.current["name"]}] FAILED after {self.current["elapsed_seconds"]} seconds: {error}', flush=True)


def smoke(engine, timeout=600, stop_timeout=60, report=None):
    started = time.monotonic()
    result = {'ready': False, 'commands': []}
    try:
        if report:
            report.start('downloads/install')
        engine.up()
        startup_phase = False
        while time.monotonic() - started < timeout:
            logs = engine.logs()
            if not startup_phase and ('ModLauncher' in logs or 'Done (' in logs):
                startup_phase = True
                if report:
                    report.start('startup')
            state = engine.state()
            if not state['Running']:
                raise RuntimeError(f'Server exited before readiness: {state}')
            if 'Done (' in logs and 'For help, type' in logs:
                result['ready'] = True
                break
            time.sleep(1)
        if not result['ready']:
            raise TimeoutError('Server readiness timeout')
        result['ready_seconds'] = round(time.monotonic() - started, 3)
        if report:
            report.start('shutdown')
        response = engine.rcon('stop')
        result['commands'].append({'command': 'stop', 'response': response})
        if 'Stopping the server' not in response:
            raise RuntimeError(f'Unconfirmed stop: {response}')
        stopping = time.monotonic()
        while engine.state()['Running']:
            if time.monotonic() - stopping >= stop_timeout:
                raise TimeoutError('Server shutdown timeout')
            time.sleep(1)
        result['exit_code'] = engine.state()['ExitCode']
        if result['exit_code'] != 0:
            raise RuntimeError(f'Unclean server exit: {result["exit_code"]}')
        result['total_seconds'] = round(time.monotonic() - started, 3)
        return result
    except (Exception, KeyboardInterrupt) as error:
        if report:
            report.fail(error)
        raise
    finally:
        if report:
            report.start('cleanup/report')
        try:
            engine.down()
        except (Exception, KeyboardInterrupt) as error:
            if report:
                report.fail(error)
            raise


SERVER_IMAGE = 'itzg/minecraft-server@sha256:63948ade43e562b9400db3bfe7367c04903d509d2c4167ace717a9a426156eb6'
def compose_definition(directory, versions, runtime=None):
    runtime = runtime or directory.parent / 'server-installation'
    return {'services': {'server': {
        'image': SERVER_IMAGE, 'restart': 'no', 'stop_grace_period': '60s',
        'mem_limit': '5g', 'cpus': 4,
        'environment': {
            'EULA': 'TRUE', 'TYPE': 'MODRINTH', 'VERSION': versions['minecraft'],
            'MODRINTH_MODPACK': '/export/server.mrpack',
            'MODRINTH_DEFAULT_EXCLUDE_INCLUDES': '',
            'FETCH_USE_HTTP2': 'false',
            'UID': str(os.getuid()), 'GID': str(os.getgid()),
            'MEMORY': '4G', 'INIT_MEMORY': '1G', 'ENABLE_RCON': 'true',
            'VIEW_DISTANCE': '4', 'SIMULATION_DISTANCE': '4',
            'MAX_PLAYERS': '1', 'LEVEL': 'smoke-world', 'LEVEL_SEED': '637921',
            'ONLINE_MODE': 'true',
        },
        'volumes': [
            {'type': 'bind', 'source': str(runtime), 'target': '/data'},
            {'type': 'bind', 'source': str(directory), 'target': '/export', 'read_only': True},
            *[{'type': 'bind', 'source': str(directory / source), 'target': '/data/' + target}
              for source, target in TRANSIENT_DIRECTORIES.items()],
        ],
    }}}


class DockerEngine:
    def __init__(self, directory):
        self.directory = directory
        self.project = 'aeropunk-' + directory.name.lower()
        self.prefix = ['docker', 'compose', '--project-name', self.project,
                       '-f', str(directory / 'compose.json')]
        self.container = None

    def command(self, *args, timeout=90, check=True):
        process = subprocess.run([*self.prefix, *args], text=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        with (self.directory / 'commands.log').open('a') as log:
            log.write(f'COMMAND {list(args)!r}\n{process.stdout}\n')
        if check:
            process.check_returncode()
        return process.stdout

    def up(self):
        self.command('up', '-d', timeout=180)
        self.container = self.command('ps', '--all', '-q', 'server').strip()
        if not self.container:
            raise RuntimeError('Compose did not create a server container')

    def state(self):
        process = subprocess.run(['docker', 'inspect', '--format', '{{json .State}}', self.container],
                                 text=True, capture_output=True, timeout=15, check=True)
        state = json.loads(process.stdout)
        (self.directory / 'container-state.json').write_text(json.dumps(state, indent=2) + '\n')
        return state

    def logs(self):
        logs = self.command('logs', '--no-color', '--timestamps', 'server', check=False)
        (self.directory / 'server.log').write_text(logs)
        return logs

    def rcon(self, command):
        return self.command('exec', '-T', 'server', 'rcon-cli', command, timeout=60)

    def down(self):
        # Preserve diagnostics before destroying the containers, including failed startup.
        try:
            self.logs()
        finally:
            self.command('down', '--remove-orphans', '--timeout', '60', timeout=120)
            remaining = self.command('ps', '--all', '-q').strip()
            networks = subprocess.run(['docker', 'network', 'ls', '--filter',
                                       f'label=com.docker.compose.project={self.project}', '-q'],
                                      text=True, capture_output=True, timeout=15, check=True).stdout.strip()
            cleanup = {'containers': remaining.splitlines(), 'networks': networks.splitlines()}
            (self.directory / 'cleanup.json').write_text(json.dumps(cleanup, indent=2) + '\n')
            if remaining or networks:
                raise RuntimeError('Compose cleanup left resources behind')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-only', action='store_true', help='Export without starting Docker')
    parser.add_argument('--fresh-install', action='store_true', help='Bypass the reusable installation for a clean-install check')
    parser.add_argument('--timeout', type=float, default=600, help='Readiness deadline in seconds')
    parser.add_argument('--stop-timeout', type=float, default=60, help='Normal shutdown deadline in seconds')
    args = parser.parse_args()
    if args.timeout <= 0 or args.stop_timeout <= 0:
        parser.error('Timeouts must be positive')
    root = Path(__file__).resolve().parents[1]
    from tasks import capture
    directory = new_run(root)
    result: dict = {'status': 'failed', 'run_directory': str(directory),
                    'image': SERVER_IMAGE, 'scope': 'startup-only'}
    exit_code = 1
    lock = runtime = None
    report = PhaseReport()
    report.start('preparation')
    try:
        if not args.build_only and not args.fresh_install:
            lock = (root / 'build' / '.server-installation.lock').open('a')
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError('Another test is using the reusable installation') from None
            containers = subprocess.run(['docker', 'ps', '--all', '-q'],
                                        capture_output=True, text=True, check=True, timeout=30).stdout.split()
            if containers:
                inspected = json.loads(subprocess.run(['docker', 'inspect', *containers],
                    capture_output=True, text=True, check=True, timeout=30).stdout)
                installation = (root / 'build' / 'server-installation').resolve()
                if any(source.is_relative_to(installation) or installation.is_relative_to(source)
                       for container in inspected for mount in container.get('Mounts', [])
                       if mount.get('Source')
                       for source in [Path(mount['Source']).resolve()]):
                    raise RuntimeError('A retained container still uses the installation; resolve its cleanup first')
        result['export'] = build_server_export(root, directory)
        if args.build_only:
            result['status'] = 'built'
        else:
            runtime = prepare_runtime(root, directory, args.fresh_install)
            result['installation'] = {'directory': str(runtime), 'mode': 'fresh' if args.fresh_install else 'reusable',
                                      'world': 'fresh'}
            definition = compose_definition(directory, result['export']['versions'], runtime)
            (directory / 'compose.json').write_text(json.dumps(definition, indent=2) + '\n')
            result['smoke'] = smoke(DockerEngine(directory), timeout=args.timeout,
                                    stop_timeout=args.stop_timeout, report=report)
            result['status'] = 'passed'
        exit_code = 0
    except (Exception, KeyboardInterrupt) as error:
        result['error'] = f'{type(error).__name__}: {error}'
        if report.failure_phase is None:
            report.fail(error)
    finally:
        cleanup = directory / 'cleanup.json'
        if runtime is not None and cleanup.exists() and json.loads(cleanup.read_text()) == {'containers': [], 'networks': []}:
            try:
                clean_runtime(root, runtime, directory)
            except Exception as error:
                report.fail(error)
                result['status'] = 'failed'
                result['error'] = f'{type(error).__name__}: {error}'
                exit_code = 1
        report.finish()
        result['phases'] = report.phases
        result['failure_phase'] = report.failure_phase
        try:
            capture(root, directory, result)
        finally:
            if lock is not None:
                lock.close()
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
