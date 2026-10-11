"""Selected Cosmonautics handbook integration regressions."""
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class CosmonauticsHandbook(unittest.TestCase):
    def test_authoritative_inventory_matches_generated_provider_coverage(self):
        coverage = json.loads((ROOT / 'docs/guide-coverage.json').read_text())
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertEqual({row['metadata_path']: row['availability'] for row in coverage['inventory']}, {row['metadata_path']: row['availability'] for row in manifest['content']})
        self.assertEqual(coverage['verification']['baseline_total'], manifest['installed_content_count'])
        self.assertEqual(coverage['verification']['union_metadata_total'], len(manifest['content']))

    def test_five_pages_have_identical_native_references_in_both_locales(self):
        source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        for topic in ('world.dimensions', 'space.destinations', 'space.vehicle-transfer', 'space.life-support', 'space.navigation'):
            references = lambda body: set(re.findall(r'<(?:ItemIcon|ItemLink|Recipe|KeyBind)[^>]*?id="([^"]+)"', body))
            self.assertEqual(references(source[topic]['en_us']), references(source[topic]['zh_cn']), topic)

    def test_orbital_article_names_fuel_without_unsupported_recipe_renderer(self):
        source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        for locale in ('en_us', 'zh_cn'):
            text = source['space.vehicle-transfer'][locale]
            self.assertIn('<ItemLink id="minecraft:lava_bucket" />', text)
            self.assertNotIn('<Recipe id="rocketnautics:mechanical_crafting/rocket_thruster" />', text)
            self.assertIn('19,000', text)

    def test_life_support_identifies_all_three_providers(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'space.life-support.md').read_text()
            footer = text.rsplit('## 相关模组' if locale else '## Related mods', 1)[1]
            for name, query in [('Create Cosmonautics', '@rocketnautics'), ('Create Deep Seas', '@create_submarine'), ('Cosmonautics: Deep Air', '@cosmonauticsdeepair')]:
                self.assertIn('[' + name + '](', footer)
                self.assertIn('<EmiSearch query="' + query + '" />', footer)

    def test_complete_bilingual_space_topics_use_native_references(self):
        content = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        expected = {
            'space.vehicle-transfer': 'rocketnautics:rocket_thruster',
            'space.life-support': 'rocketnautics:space_helmet',
            'space.navigation': 'rocketnautics:hologram_block',
        }
        for topic, item in expected.items():
            self.assertIn(topic, content)
            for locale in ('en_us', 'zh_cn'):
                text = content[topic][locale]
                self.assertIn('<ItemLink id="' + item + '" />', text)
                self.assertNotRegex(text, r'not been tested|selected release|installed|未经测试|所选版本|已安装|[;；—–]')

    def test_space_topics_have_one_primary_item_destination(self):
        for locale in ('', '_zh_cn'):
            for topic, item in [('space.vehicle-transfer', 'rocketnautics:rocket_thruster'), ('space.life-support', 'cosmonauticsdeepair:gravity_generator'), ('space.navigation', 'rocketnautics:hologram_block')]:
                text = (PAGES / locale / (topic + '.md')).read_text()
                self.assertIn('  parent: reference.vehicles.md', text)
                self.assertIn('  - ' + item, text.split('---', 2)[1])

    def test_retired_providers_and_deferred_articles_are_absent(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertFalse(any('northstar' in row['metadata_path'] for row in manifest['content']))
        self.assertEqual(manifest['deferred_content_count'], 0)
        for locale in ('', '_zh_cn'):
            for page in (PAGES / locale).glob('*.md'):
                self.assertNotRegex(page.read_text(), r'Northstar|Work in progress|\bWIP\b|not installed|未安装')


if __name__ == '__main__':
    unittest.main()
