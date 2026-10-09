"""Check the shared reference and mod navigation skeleton without rendering."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class NavigationSkeleton(unittest.TestCase):
    def test_reference_sections_have_one_primary_parent(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            for filename in ('quick-reference.md', 'mod-catalogs.md'):
                self.assertTrue((base / filename).is_file())
            for filename in ('adventure.bosses.md', 'adventure.creatures.md', 'adventure.structures.md', 'world.dimensions.md', 'reference.equipment.md', 'reference.skills.md', 'reference.food.md', 'reference.building.md', 'reference.vehicles.md', 'reference.machines-storage.md'):
                self.assertIn('  parent: quick-reference.md\n', (base / filename).read_text())
            for path in base.glob('category-*.md'):
                self.assertIn('  parent: mod-catalogs.md\n', path.read_text())

    def test_sidebar_is_acyclic_and_no_more_than_two_category_levels(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            for path in base.glob('*.md'):
                seen = {path.name}
                current = path
                depth = 0
                while parent := re.search(r'^  parent: (.+)$', current.read_text(), re.M):
                    name = parent.group(1)
                    self.assertNotIn(name, seen)
                    seen.add(name)
                    current = base / name
                    self.assertTrue(current.is_file())
                    depth += 1
                self.assertLessEqual(depth, 2, path.name)

    def test_home_and_sidebar_reference_directory_match(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            home = (base / 'index.md').read_text().split('\n***\n', 1)[0]
            directory = (base / 'quick-reference.md').read_text()
            refs = set(re.findall(r'\]\(([^)]+\.md)\)', directory))
            self.assertEqual(set(re.findall(r'\]\(([^)]+\.md)\)', home)), refs)
            self.assertGreaterEqual(len(refs), 12)

    def test_schema_counts_match_generated_files(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertEqual(len(list(PAGES.glob('*.md'))), manifest['article_count'] + manifest['category_count'] + manifest['navigation_page_count'] + manifest['reference_directory_count'] + 1)


if __name__ == '__main__':
    unittest.main()
