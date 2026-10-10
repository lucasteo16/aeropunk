"""Food articles teach common tools once and leave repetitive recipes to the browser."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
ICONS = {
    'reference.food': 'minecraft:bread',
    'food.hunger': 'minecraft:apple',
    'food.utensils': 'farmersdelight:cooking_pot',
    'food.nether': 'minecraft:crimson_fungus',
    'food.end': 'minecraft:chorus_fruit',
    'food.underground': 'minecraft:brown_mushroom',
    'food.encounters': 'minecraft:rotten_flesh',
    'food.machine-cooking': 'minecraft:smoker',
    'food.growing': 'minecraft:wheat',
    'food.fishing': 'minecraft:cod',
}


class FoodConcision(unittest.TestCase):
    def test_every_food_topic_has_a_distinct_relevant_navigation_icon(self):
        self.assertEqual(len(set(ICONS.values())), len(ICONS))
        for locale in ('', '_zh_cn'):
            for topic, icon in ICONS.items():
                page = (PAGES / locale / (topic + '.md')).read_text()
                self.assertIn('  icon: ' + icon + '\n', page)

    def test_food_source_avoids_repetitive_recipe_transcriptions(self):
        source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        topics = {key for key in source if key.startswith('food.') or key == 'reference.food'}
        self.assertEqual(topics, set(ICONS))
        for topic in topics:
            for locale, body in source[topic].items():
                self.assertNotIn('another accepted', body, (topic, locale))
                self.assertNotIn('Yield ', body, (topic, locale))
                self.assertNotIn('Its recipe uses', body, (topic, locale))
                self.assertNotIn('This entry is a serving, container or specialized ingredient', body)
                self.assertLessEqual(len(re.findall(r'(?m)^\d+\. ', body)), 3, (topic, locale))
                prose = re.sub(r'<[^>]+>', '', body)
                prose = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', prose)
                if locale == 'en_us':
                    self.assertLessEqual(len(prose.split()), 450, topic)


if __name__ == '__main__':
    unittest.main()
