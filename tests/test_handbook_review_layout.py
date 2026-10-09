"""Regression checks for the first reviewed handbook layout, not rendering tests."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


def body(path):
    text = path.read_text()
    return text.split('\n---\n', 1)[1].split('\n', 3)[-1].strip()


class ReviewedLayout(unittest.TestCase):
    def test_home_has_two_named_sections_and_visual_reference_rows(self):
        for language in ('', '_zh_cn'):
            text = (PAGES / language / 'index.md').read_text()
            content = text.split('\n# Astropunk\n', 1)[1].strip()
            self.assertTrue(content.startswith('## '))
            self.assertIn('Item recipe' if not language else '物品配方', text)
            self.assertEqual(len(re.findall(r'^## ', content, re.M)), 2)
            self.assertGreaterEqual(text.count('<ItemImage '), 6)
            self.assertNotIn('<ItemGrid>', text)
            reference = 'Quick reference' if not language else '快速参考'
            catalog = 'Mod catalogs' if not language else '模组目录'
            self.assertLess(text.index('## ' + reference), text.index('## ' + catalog))
            self.assertIn('\n***\n', text)
            self.assertNotIn(' · ', text)

    def test_dimensions_is_one_real_catalog(self):
        for language in ('', '_zh_cn'):
            text = (PAGES / language / 'world.dimensions.md').read_text()
            self.assertNotIn('landscapes.', text)
            for name in ('Tectonic', 'Terralith', 'Streams Reflowing', 'Incendium Biomes Only', 'Nullscape'):
                self.assertIn(name, text)
            for title in (('Overworld', 'Nether', 'End') if not language else ('主世界', '下界', '末地')):
                self.assertIn('## ' + title, text)

    def test_automation_is_role_based_not_intent_based(self):
        text = (PAGES / 'category-automation.md').read_text()
        self.assertIn('## Automation Mods', text)
        self.assertLess(text.index('## Automation Mods'), text.index('## Mechanics'))
        for name in ('Villager Names', 'EMI Enchanting', 'EMI professions', 'Easy Anvils', 'Trade Refresh'):
            self.assertNotIn(name, text)
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        for entry in manifest['content']:
            if entry['name'] in ('Villager Names', 'EMI Enchanting', 'Easy Anvils', 'Trade Refresh') or entry['name'].startswith('EMI professions'):
                self.assertEqual(entry['category'], 'Player utilities and quality of life')

    def test_no_redirect_only_navigation_pages(self):
        for locale in ('', '_zh_cn'):
            for name in ('ore-processing.md', 'landscapes.overworld.md', 'landscapes.nether.md', 'landscapes.end.md'):
                self.assertFalse((PAGES / locale / name).exists(), name)

    def test_images_are_local_real_assets(self):
        count = 0
        for name in ('world.dimensions.md', 'category-automation.md'):
            text = (PAGES / name).read_text()
            for target in re.findall(r'!\[[^\]]*\]\((images/[^)]+)\)', text):
                image = PAGES / target
                self.assertTrue(image.is_file(), target)
                self.assertEqual(image.read_bytes()[:8], b'\x89PNG\r\n\x1a\n')
                count += 1
        self.assertGreaterEqual(count, 3)

    def test_all_pages_and_templates_start_with_a_section(self):
        for base in (PAGES, ROOT / 'docs/handbook-templates'):
            for path in base.rglob('*.md'):
                text = path.read_text().split('\n---\n', 1)[1].strip()
                lines = text.splitlines()
                self.assertTrue(lines[0].startswith('# '), path)
                rest = '\n'.join(lines[1:]).strip()
                self.assertTrue(rest.startswith('## '), path)


if __name__ == '__main__':
    unittest.main()
