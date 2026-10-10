"""Native processing and reversible fallback reconciliation regressions."""
from pathlib import Path
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'resourcepacks/astropunk-guide-preview'
REL = Path('assets/astropunk/guides/astropunk/handbook')

class ReleasedNavigation(unittest.TestCase):
    def test_released_navigation_bytecode_and_negative_fallback_controls(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/test-native-navigation.py')], check=True, capture_output=True, text=True)
        report = json.loads(result.stdout)
        self.assertEqual({row['locale'] for row in report['tests']}, {'en_us', '_zh_cn'})
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        for row in report['tests']:
            self.assertIn(f"{len(manifest['pages']) + 1} nodes, eighteen ordered roots, direct Audio article", row['output'])
            self.assertIn('obsolete Quick reference and Sound resurrection and repair controls', row['output'])
        self.assertFalse(report['rendered_verified'])

    def test_registration_does_not_reintroduce_catalog_or_unsupported_nodes(self):
        self.assertFalse((SOURCE / 'assets/astropunk/guideme_guides/handbook.json').exists())

    def test_reconciliation_archives_stale_fallback_and_verifies_registration(self):
        spec = importlib.util.spec_from_file_location('fallback', ROOT / 'scripts/reconcile-handbook-fallback.py')
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory(prefix='fallback-regression-', dir=os.environ.get('TMPDIR', '/home/tsb/.hermes/cache/scratch')) as temporary:
            base = Path(temporary)
            target = base / 'pack'
            shutil.copytree(SOURCE, target)
            stale = target / REL / 'category-automation.md'
            stale.write_text('---\nnavigation:\n  title: Old Automation\n---\n# Old\n')
            old_bytes = stale.read_bytes()
            registration = target / 'assets/astropunk/guideme_guides/handbook.json'
            registration.parent.mkdir(parents=True, exist_ok=True)
            registration.write_text('{"default_language":"en_us","navigation":[{"title":"Old catalog"}]}')
            report = module.reconcile(target, base / 'archive')
            self.assertFalse(stale.exists())
            archived = [x for x in report['archived_files'] if x['path'].endswith('category-automation.md')]
            self.assertEqual(len(archived), 1)
            self.assertEqual(Path(archived[0]['archive']).read_bytes(), old_bytes)
            self.assertFalse(registration.exists())
            self.assertTrue(any(x['path'].endswith('guideme_guides/handbook.json') for x in report['archived_files']))
            self.assertFalse(report['client_reload_verified'])
            second = module.reconcile(target, base / 'archive')
            self.assertEqual(second['changed_files'], 0)
            self.assertEqual(second['retired_pages'], [])

if __name__ == '__main__':
    unittest.main()
