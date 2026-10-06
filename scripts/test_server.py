#!/usr/bin/env python3
"""Export the server pack and check disposable Docker startup and normal shutdown."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
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
    (directory / 'runtime').mkdir()  # A fresh installation, never an existing world.
    return {'versions': versions, 'format': 'modrinth', 'archive': str(archive),
            'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
            'installer': 'mc-image-helper install-modrinth-modpack'}


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
def compose_definition(directory, versions):
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
            {'type': 'bind', 'source': str(directory / 'runtime'), 'target': '/data'},
            {'type': 'bind', 'source': str(directory), 'target': '/export', 'read_only': True},
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
    parser.add_argument('--timeout', type=float, default=600, help='Readiness deadline in seconds')
    parser.add_argument('--stop-timeout', type=float, default=60, help='Normal shutdown deadline in seconds')
    args = parser.parse_args()
    if args.timeout <= 0 or args.stop_timeout <= 0:
        parser.error('Timeouts must be positive')
    root = Path(__file__).resolve().parents[1]
    from tasks import capture
    directory = new_run(root)
    result = {'status': 'failed', 'run_directory': str(directory),
              'image': SERVER_IMAGE, 'scope': 'startup-only'}
    exit_code = 1
    report = PhaseReport()
    report.start('preparation')
    try:
        result['export'] = build_server_export(root, directory)
        if args.build_only:
            result['status'] = 'built'
        else:
            definition = compose_definition(directory, result['export']['versions'])
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
        report.finish()
        result['phases'] = report.phases
        result['failure_phase'] = report.failure_phase
        capture(root, directory, result)
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
