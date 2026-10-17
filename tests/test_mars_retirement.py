"""Mars addon retirement preserves base space content and lunar titles."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RETIRED = 'mods/create-cosmonautics-expansion.pw.toml'


class MarsRetirement(unittest.TestCase):
    def test_only_expansion_is_retired_from_space_selection(self):
        self.assertFalse((ROOT / RETIRED).exists())
        for name in ('create-cosmonatics', 'cosmonautics-deep-air', 'create-deep-seas'):
            self.assertTrue((ROOT / 'mods' / (name + '.pw.toml')).is_file())

    def test_active_inventory_and_player_guidance_exclude_expansion(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertNotIn(RETIRED, {e['metadata_path'] for e in manifest['content']})
        source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        self.assertNotIn('## Mars', source['world.dimensions']['en_us'])
        self.assertNotIn('## 火星', source['world.dimensions']['zh_cn'])
        self.assertNotIn('rocketnautics_addon', json.dumps(source))
        self.assertIn('Mars, the gas giant and ice world', source['world.dimensions']['en_us'])

    def test_lunar_titles_remain_complete_in_both_languages(self):
        folder = ROOT / 'config/paxi/resourcepacks/astropunk-space-titles/assets/travelerstitles/lang'
        en = json.loads((folder / 'en_us.json').read_text())
        zh = json.loads((folder / 'zh_cn.json').read_text())
        self.assertEqual(set(en), set(zh))
        self.assertEqual(len(en), 9)
        self.assertEqual(en['travelerstitles.rocketnautics.moon'], 'Luna')
        self.assertFalse(any('rocketnautics_addon' in key for key in en))

    def test_generated_pages_have_no_retired_provider_or_destination(self):
        folder = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
        for path in folder.rglob('*.md'):
            text = path.read_text()
            self.assertNotIn('rocketnautics_addon', text, str(path))
            self.assertNotIn('Create Cosmonautics Expansion', text, str(path))
