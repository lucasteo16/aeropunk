"""Regression coverage for scoped distribution retention."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

SPEC = importlib.util.spec_from_file_location('retention', Path(__file__).resolve().parents[1] / 'scripts/retain_releases.py')
assert SPEC is not None and SPEC.loader is not None
retention = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(retention)


class ReleaseRetentionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'dist').mkdir()
        (self.root / 'pack.toml').write_text('name = "Astropunk"\nversion = "0.15.3"\n')

    def artifact(self, version, role='modrinth.mrpack'):
        path = self.root / 'dist' / f'astropunk-{version}-{role}'
        path.write_text('fixture')
        return path

    def test_two_versions_retained_as_complete_groups(self):
        oldest = self.artifact('0.9.0')
        self.artifact('0.15.1')
        current = self.artifact('0.15.3')
        sibling = self.artifact('0.15.3', 'server.zip')
        self.assertEqual(retention.prune(self.root, 2, True), [oldest])
        self.assertFalse(oldest.exists())
        self.assertTrue(current.exists() and sibling.exists())

    def test_dry_run_preserves_old_releases(self):
        old = self.artifact('0.15.1')
        self.artifact('0.15.3')
        retention.prune(self.root, 1)
        self.assertTrue(old.exists())

    def test_unknown_files_preserved(self):
        unknown = self.root / 'dist' / 'personal-world.zip'
        unknown.write_text('protected')
        self.artifact('0.15.3')
        retention.prune(self.root, 1, True)
        self.assertTrue(unknown.exists())

    def test_missing_current_release_refuses_deletion(self):
        old = self.artifact('0.15.1')
        with self.assertRaises(ValueError):
            retention.prune(self.root, 1, True)
        self.assertTrue(old.exists())

    def test_future_release_refuses_deletion(self):
        self.artifact('0.15.3')
        self.artifact('0.16.0')
        with self.assertRaises(ValueError):
            retention.prune(self.root, 1, True)

    def test_symbolic_links_refuse_deletion(self):
        self.artifact('0.15.3')
        target = self.root / 'protected'
        target.write_text('protected')
        (self.root / 'dist/astropunk-0.15.1-server.zip').symlink_to(target)
        with self.assertRaises(ValueError):
            retention.prune(self.root, 1, True)
        self.assertEqual(target.read_text(), 'protected')

    def test_export_identity_and_integrity(self):
        archive = self.root / 'dist/current.mrpack'
        with zipfile.ZipFile(archive, 'w') as out:
            out.writestr('modrinth.index.json', json.dumps({'name': 'Astropunk', 'versionId': '0.15.3'}))
        retention.verify_export(archive, '0.15.3')
        with self.assertRaises(ValueError):
            retention.verify_export(archive, '0.15.2')

    def test_negative_retention_refuses_deletion(self):
        self.artifact('0.15.3')
        with self.assertRaises(ValueError):
            retention.prune(self.root, 0, True)

    def test_unrecognized_subdirectory_not_removed(self):
        unrelated = self.root / 'dist/notes'
        unrelated.mkdir()
        self.artifact('0.15.3')
        retention.prune(self.root, 1, True)
        self.assertTrue(unrelated.is_dir())

    def test_packed_file_disguised_as_directory_is_rejected(self):
        self.artifact('0.15.3')
        bad = self.root / 'dist/astropunk-0.15.1-server.zip'
        bad.mkdir()
        with self.assertRaises(ValueError):
            retention.prune(self.root, 1, True)
