import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

ROOT = Path(__file__).resolve().parents[1]


def runner():
    spec = importlib.util.spec_from_file_location('aeropunk_test_server', ROOT / 'scripts/test_server.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExportTests(unittest.TestCase):
    def test_server_export_uses_default_cache_and_normal_cli(self):
        from unittest.mock import patch
        module = runner()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            (root / 'mods').mkdir()
            (root / 'pack.toml').write_text('[versions]\nminecraft="1.21.1"\nneoforge="21.1.255"\n')
            directory = root / 'build' / 'smoke-test'
            directory.mkdir(parents=True)
            def export(command, **kwargs):
                self.assertEqual(command[:3], ['packwiz', 'curseforge', 'export'])
                self.assertNotIn('--cache', command)
                self.assertNotIn('--output', command)
                self.assertIn('server', command)
                with zipfile.ZipFile(Path(kwargs['cwd']) / 'Native-0.1.0.zip', 'w') as out:
                    out.writestr('manifest.json', json.dumps({'minecraft': {'version': '1.21.1', 'modLoaders': [{'id': 'neoforge-21.1.255'}]}, 'files': []}))
                import subprocess
                return subprocess.CompletedProcess(command, 0, 'exported')
            with patch.object(module.subprocess, 'run', side_effect=export):
                result = module.build_server_export(root, directory)
            self.assertEqual(result['mod_count'], 0)


class StartupTests(unittest.TestCase):
    def test_ready_immediately_stops_and_cleans_up(self):
        module = runner()
        class Engine:
            def __init__(self): self.calls = []; self.running = True
            def up(self): self.calls.append('up')
            def state(self): return {'Running': self.running, 'ExitCode': 0}
            def logs(self): return 'Done (1s)! For help, type "help"'
            def rcon(self, command):
                self.calls.append(command); self.running = False
                return 'Stopping the server'
            def down(self): self.calls.append('down')
        engine = Engine()
        from unittest.mock import patch
        with patch.object(module.time, 'sleep', side_effect=AssertionError('Unexpected readiness wait')):
            result = module.smoke(engine, timeout=1)
        self.assertTrue(result['ready'])
        self.assertEqual(engine.calls, ['up', 'stop', 'down'])

    def test_early_exit_still_cleans_up(self):
        module = runner()
        class Engine:
            cleaned = False
            def up(self): pass
            def state(self): return {'Running': False, 'ExitCode': 1}
            def down(self): self.cleaned = True
        engine = Engine()
        with self.assertRaisesRegex(RuntimeError, 'before readiness'):
            module.smoke(engine, timeout=1)
        self.assertTrue(engine.cleaned)

    def test_unsupported_refs_and_unsafe_paths_fail_before_extraction(self):
        module = runner()
        for files, path, message in [([{'projectID': 1, 'fileID': 2}], 'overrides/mods/a.jar', 'CurseForge'),
                                     ([], 'overrides/../../escape', 'Unsafe')]:
            with self.subTest(path=path), tempfile.TemporaryDirectory(dir=ROOT) as tmp:
                directory = Path(tmp)
                archive = directory / 'export.zip'
                with zipfile.ZipFile(archive, 'w') as out:
                    out.writestr('manifest.json', json.dumps({'minecraft': {'version': '1.21.1', 'modLoaders': [{'id': 'neoforge-21.1.255', 'primary': True}]}, 'files': files}))
                    out.writestr(path, 'payload')
                with self.assertRaisesRegex(ValueError, message):
                    module.extract_server_export(archive, directory / 'runtime', {'minecraft': '1.21.1', 'neoforge': '21.1.255'})
                self.assertFalse((directory / 'runtime').exists())


class IncompleteExportTests(unittest.TestCase):
    def test_missing_server_artifact_is_rejected_before_runtime(self):
        module = runner()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            directory = Path(tmp)
            archive = directory / 'export.zip'
            with zipfile.ZipFile(archive, 'w') as out:
                out.writestr('manifest.json', json.dumps({'minecraft': {'version': '1.21.1', 'modLoaders': [{'id': 'neoforge-21.1.255'}]}, 'files': []}))
            with self.assertRaisesRegex(ValueError, 'server artifacts'):
                module.extract_server_export(archive, directory / 'runtime',
                                             {'minecraft': '1.21.1', 'neoforge': '21.1.255'},
                                             expected_mods={'required.jar'})
            self.assertFalse((directory / 'runtime').exists())


if __name__ == '__main__':
    unittest.main()
