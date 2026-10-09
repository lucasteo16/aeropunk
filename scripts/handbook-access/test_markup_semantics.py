#!/usr/bin/env python3
"""Regression tests at the selected-release compiler seam, not parser-only checks.
Run: python -m unittest discover -s scripts/handbook-access -p test_markup_semantics.py -v
"""
from pathlib import Path
import collections
import importlib.util
import json
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
ACCESS = ROOT / 'scripts/handbook-access'
FRAGMENT = ROOT / 'docs/final-review/markup-content.json'

class MarkupSemanticRegression(unittest.TestCase):
    def test_original_inline_grid_reaches_the_reported_native_error(self):
        result = subprocess.run([sys.executable, str(ACCESS / 'verify_markup.py'), '--label', 'test-red-fixture',
                                 '--pages', str(ACCESS / 'markup-fixtures'), '--include-orphans'],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        log = (ROOT / 'build/handbook-access/markup-probe/test-red-fixture/compiler.log').read_text()
        self.assertIn('CONTROLS passed', log)
        self.assertIn('SUMMARY pages 1 failing_pages 1', log)
        self.assertIn('Unsupported child-element in ItemGrid text (3:60)', log)
        errors = [line for line in log.splitlines() if 'COMPILER_ERROR ' in line]
        self.assertEqual(len(errors), 7)
        self.assertTrue(all('Unsupported child-element in ItemGrid text' in line for line in errors))

    def test_repaired_book_preserves_slots_and_tooltip_labels(self):
        result = subprocess.run([sys.executable, str(ACCESS / 'verify_markup.py'), '--fragment', str(FRAGMENT),
                                 '--label', 'test-green-book'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        log = (ROOT / 'build/handbook-access/markup-probe/test-green-book/compiler.log').read_text()
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        expected_pages = 2 * len({row['filename'] for row in manifest['pages']} | {'index.md'})
        self.assertIn(f'SUMMARY pages {expected_pages} failing_pages 0', log)
        self.assertRegex(log, r'grids [1-9][0-9]* slots [1-9][0-9]* tooltip_labels [1-9][0-9]*')
        self.assertIn('Recipe and KeyBind not compiled', log)
        self.assertNotIn('COMPILER_ERROR ', log)

    def test_fragment_preserves_every_native_reference_in_both_languages(self):
        current = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        source = json.loads((ACCESS / 'markup-fixtures/baseline-content.json').read_text())
        fragment = json.loads(FRAGMENT.read_text())
        self.assertEqual(set(fragment), {'combat.skills', 'equipment.weapons-armor'})
        spec = importlib.util.spec_from_file_location('repair_markup_fragment', ACCESS / 'repair_markup_fragment.py')
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(fragment, module.fragment(source))
        for topic in fragment:
            self.assertEqual(current[topic], fragment[topic])
        pattern = r'<(ItemIcon|ItemLink|ItemImage|Recipe|KeyBind)\b[^>]*?/>'
        for topic, locales in fragment.items():
            self.assertEqual(set(locales), {'en_us', 'zh_cn'})
            for locale, body in locales.items():
                self.assertEqual(re.findall(pattern, body), re.findall(pattern, source[topic][locale]))
                references = lambda text: re.findall(r'<(?:ItemIcon|ItemLink|ItemImage|Recipe|KeyBind)\b[^>]*?/>', text)
                self.assertEqual(references(body), references(source[topic][locale]))
                self.assertNotRegex(body, r'[;；]')
                if topic == 'equipment.weapons-armor':
                    self.assertNotRegex(body, r'^\|.*<ItemGrid>', 'Armor grids must stay outside tables')
                    groups = re.findall(r'(<ItemLink\b[^>]*?/>)\n\n<ItemGrid>\n(.*?)</ItemGrid>', body, re.S)
                    armor = [(label, re.findall(r'<ItemIcon\b[^>]*?/>', content)) for label, content in groups if len(re.findall(r'<ItemIcon\b[^>]*?/>', content)) == 4]
                    self.assertEqual(len(armor), 90)
                else:
                    self.assertEqual(len(re.findall(r'<ItemGrid><ItemIcon\b[^>]*?/></ItemGrid>', body)), 45)
        # Already compact reference tables are valid controls, not needless repair targets.
        self.assertNotIn('reference.skills', fragment)

if __name__ == '__main__':
    unittest.main()
