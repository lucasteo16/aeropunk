"""Final player-review acceptance checks, separate from game rendering."""
from pathlib import Path
import json
import re
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'

class FinalReview(unittest.TestCase):
    def test_pack_intro_is_not_another_reference_directory(self):
        for locale in ('', '_zh_cn'):
            home = (PAGES / locale / 'index.md').read_text()
            self.assertEqual(set(re.findall(r'\]\(([^)]+\.md)\)', home)), {'help.credits.md'})
            self.assertNotIn('| Reference | Contents |', home)
            self.assertFalse((PAGES / locale / 'quick-reference.md').exists())

    def test_every_provider_has_translated_purpose_and_an_honest_query_cell(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        purposes = json.loads((ROOT / 'docs/handbook-provider-purposes.json').read_text())
        queries = json.loads((ROOT / 'docs/handbook-item-queries.json').read_text())
        self.assertEqual(set(purposes), {entry['metadata_path'] for entry in manifest['content']})
        self.assertEqual(set(queries), set(purposes))
        for entry in manifest['content']:
            for language, locale in (('en_us', ''), ('zh_cn', '_zh_cn')):
                text = (PAGES / locale / (entry['topic'] + '.md')).read_text()
                self.assertIn(purposes[entry['metadata_path']][language], text)
                self.assertNotIn('英文官方简介', text)
                for query in queries[entry['metadata_path']][language]:
                    self.assertIn('<EmiSearch query="' + query + '" />', text)
        self.assertNotIn('@create_abyss', json.dumps(queries))
        self.assertEqual(queries['mods/vanilla-backpacks.pw.toml'], {'en_us': ['backpack'], 'zh_cn': ['背包']})

    def test_classes_and_building_tools_are_not_buried_in_provider_lists(self):
        for locale in ('', '_zh_cn'):
            combat = (PAGES / locale / 'reference.skills.md').read_text()
            rows = [line for line in combat.splitlines() if line.startswith('| ') and '<ItemIcon ' in line]
            self.assertEqual(len(rows), 19)
            self.assertIn('<Recipe id="spell_engine:spell_binding_table" />', combat)
            building = (PAGES / locale / 'reference.building.md').read_text()
            self.assertIn('<ItemLink id="mechtrowel:mech_trowel" />', building)
            placement = (PAGES / locale / 'building.placement.md').read_text()
            self.assertIn('<Recipe id="mechtrowel:mech_trowel" />', placement)

    def test_full_width_and_query_registration_are_distribution_defaults(self):
        settings = tomllib.loads((ROOT / 'configureddefaults/config/guideme.toml').read_text())
        self.assertTrue(settings['gui']['fullWidthLayout'])
        self.assertFalse((ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guideme_guides/handbook.json').exists())

if __name__ == '__main__':
    unittest.main()
