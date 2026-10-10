from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class FocusedClassReferences(unittest.TestCase):
    def test_eighteen_focused_classes_preserve_nineteen_book_pools(self):
        definitions = json.loads((ROOT / 'docs/handbook-class-navigation.json').read_text())
        classes = {key: value for key, value in definitions.items() if key.startswith('class.')}
        self.assertEqual(len(classes), 18)
        pools = {pool for value in classes.values() for pool in value['evidence']['book_pools']}
        self.assertEqual(len(pools), 19)
        for locale in ('', '_zh_cn'):
            for key, definition in classes.items():
                page = (PAGES / locale / (key + '.md')).read_text()
                self.assertIn('  parent: ' + definition['parent'] + '.md\n', page)
                self.assertIn('<Recipe ', page)
                self.assertIn('spell_engine:spell_book', page)
                self.assertIn('key.puffish_skills.open', page)
            self.assertNotIn('<Recipe ', (PAGES / locale / 'equipment.weapons-armor.md').read_text())

    def test_moving_destinations_is_consolidated_and_support_is_clear(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            self.assertFalse((base / 'travel.moving-destinations.md').exists())
            for page in base.glob('*.md'):
                self.assertNotIn('](travel.moving-destinations.md)', page.read_text())
            self.assertIn('Waystones Sable', (base / 'travel.destinations.md').read_text())
            self.assertIn('Team Capes', (base / 'maps.shared.md').read_text())
            shader = (base / 'visuals.shader-packs.md').read_text()
            self.assertNotIn('## Initial state', shader)
            self.assertNotIn('## 初始状态', shader)
            workshop = (base / 'machines.miscellaneous.md').read_text()
            self.assertNotIn('## Getting started', workshop)
            self.assertNotIn('## 初次使用', workshop)


if __name__ == '__main__':
    unittest.main()
