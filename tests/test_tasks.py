import importlib.util
from pathlib import Path
import tempfile
import sys
import types
import unittest

ROOT = Path(__file__).resolve().parents[1]
def tasks():
    spec = importlib.util.spec_from_file_location('tasks', ROOT / 'scripts/tasks.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class CleanupTests(unittest.TestCase):
    def test_preserves_cache_dist_and_unknown_build_content(self):
        module = tasks()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            for name in ['build/packwiz-cache/a', 'build/verified-mods/a.jar', 'build/smoke-old/result.json', 'build/user-work/a', 'dist/a.zip', 'cache/tool/__pycache__/a.pyc']:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('data')
            module.clean(root)
            self.assertTrue((root / 'build/packwiz-cache/a').exists())
            self.assertTrue((root / 'build/verified-mods/a.jar').exists())
            self.assertTrue((root / 'dist/a.zip').exists())
            self.assertFalse((root / 'cache/tool/__pycache__').exists())
            self.assertTrue((root / 'build/user-work/a').exists())
            self.assertFalse((root / 'build/smoke-old').exists())

    def test_rejects_symlinks_and_traversal_before_deletion(self):
        module = tasks()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            (root / 'build').mkdir()
            (root / 'build/smoke-old').symlink_to(root / 'dist')
            with self.assertRaises(ValueError): module.clean(root)
            with self.assertRaises(ValueError): module.safe_path(root, root / 'build/../dist')

    def test_unconfirmed_docker_cleanup_preserves_runtime_and_reports(self):
        module = tasks()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            run = root / 'build/smoke-test'
            run.mkdir(parents=True)
            (run / 'compose.json').write_text('{}')
            (run / 'server.log').write_text('startup failure')
            module.capture(root, run, {'status': 'failed'})
            self.assertTrue(run.exists())
            self.assertEqual((root / 'reports/server.log').read_text(), 'startup failure')
            (run / 'cleanup.json').write_text('{"containers": [], "networks": []}')
            module.capture(root, run, {'status': 'failed'})
            self.assertFalse(run.exists())

    def test_reports_captured_before_temporary_removal(self):
        module = tasks()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            run = root / 'build/smoke-test'
            run.mkdir(parents=True)
            (run / 'server.log').write_text('final logs')
            module.capture(root, run, {'status': 'failed'})
            self.assertFalse(run.exists())
            self.assertEqual((root / 'reports/server.log').read_text(), 'final logs')
            self.assertIn('failed', (root / 'reports/result.json').read_text())
            self.assertEqual({p.name for p in (root / 'reports').iterdir()}, {'result.json', 'server.log'})

class DistributionTests(unittest.TestCase):
    def test_client_export_uses_default_cache(self):
        self.check_export(check_command=True)

    def test_export_replaces_latest_atomically_without_archiving(self):
        self.check_export(check_command=False)

    def check_export(self, check_command):
        import json
        import subprocess
        import zipfile
        from unittest.mock import patch
        module = tasks()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            for name in ['dist/client/Native-0.1.0.zip', 'dist/aeropunk-server.zip',
                         'dist/client/Native-older.zip', 'dist/other.zip', 'build/old.zip', 'exports/old.mrpack']:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'previous')
            def export(command, **kwargs):
                if check_command:
                    self.assertEqual(command[:3], ['packwiz', 'curseforge', 'export'])
                    self.assertNotIn('--cache', command)
                    self.assertNotIn('--output', command)
                self.assertEqual((root / 'dist/client/Native-0.1.0.zip').read_bytes(), b'previous')
                with zipfile.ZipFile(Path(kwargs['cwd']) / 'Native-0.1.0.zip', 'w') as out:
                    out.writestr('manifest.json', json.dumps({}))
                return subprocess.CompletedProcess(command, 0)
            with patch.dict(sys.modules, {'test_server': types.SimpleNamespace(extract_server_export=None)}), patch.object(module.subprocess, 'run', side_effect=export):
                module.export(root, 'client')
            self.assertFalse((root / '.archive').exists())
            for name in ['dist/aeropunk-server.zip', 'dist/client/Native-older.zip', 'dist/other.zip', 'build/old.zip', 'exports/old.mrpack']:
                self.assertEqual((root / name).read_bytes(), b'previous')
            self.assertFalse(list((root / 'dist').glob('.export-*')))

    def test_failed_export_preserves_latest(self):
        import subprocess
        from unittest.mock import patch
        module = tasks()
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            root = Path(tmp)
            (root / 'dist/client').mkdir(parents=True)
            target = root / 'dist/client/Native-0.1.0.zip'
            target.write_bytes(b'previous')
            with patch.dict(sys.modules, {'test_server': types.SimpleNamespace(extract_server_export=None)}), patch.object(module.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'packwiz')):
                with self.assertRaises(subprocess.CalledProcessError):
                    module.export(root, 'client')
            self.assertEqual(target.read_bytes(), b'previous')
            self.assertFalse(list((root / 'dist').glob('.export-*')))

if __name__ == '__main__': unittest.main()
