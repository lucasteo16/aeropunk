from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
ICONS = {
    'reference.skills': 'minecraft:iron_sword',
    'reference.equipment': 'minecraft:iron_chestplate',
    'combat.abilities': 'minecraft:enchanted_book',
    'equipment.accessories': 'minecraft:emerald',
    'equipment.display': 'minecraft:potion',
    'combat.skills': 'minecraft:experience_bottle',
    'combat.magic': 'minecraft:blaze_rod',
    'combat.martial': 'minecraft:bow',
    'equipment.weapons-armor': 'minecraft:trident',
    'combat.handling': 'minecraft:feather',
}


class CombatNavigationIcons(unittest.TestCase):
    def test_combat_topics_have_distinct_icons_in_both_languages(self):
        self.assertEqual(len(set(ICONS.values())), len(ICONS))
        for locale in ('', '_zh_cn'):
            for topic, icon in ICONS.items():
                page = (PAGES / locale / (topic + '.md')).read_text()
                self.assertIn('  icon: ' + icon + '\n', page)


if __name__ == '__main__':
    unittest.main()
