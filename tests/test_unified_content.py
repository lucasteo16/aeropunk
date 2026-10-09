"""Acceptance checks for the unified gameplay-first content revision."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'

class UnifiedContent(unittest.TestCase):
    def test_class_choices_and_first_steps_are_in_combat_abilities(self):
        for locale in ('', '_zh_cn'):
            landing = (PAGES / locale / 'reference.skills.md').read_text()
            self.assertIn('](combat.abilities.md)', landing)
            text = (PAGES / locale / 'reference.skills.md').read_text()
            rows = [line for line in text.splitlines() if line.startswith('| ') and '<ItemIcon ' in line]
            self.assertEqual(len(rows), 19)
            self.assertIn('<Recipe id="spell_engine:spell_binding_table" />', text)
            self.assertIn('<KeyBind id="key.puffish_skills.open" />', text)

    def test_technical_content_has_no_placeholders_or_audio_rosters(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        for entry in manifest['content']:
            if entry['metadata_path'] in ('mods/cool-rain-reforged.pw.toml', 'mods/presence-footsteps.pw.toml', 'mods/sable-cool-rain.pw.toml', 'mods/presence-footsteps-x-sable.pw.toml'):
                self.assertEqual(entry['topic'], 'reference.audio')
        for locale in ('', '_zh_cn'):
            for topic in ('reference.technical', 'technical.libraries', 'technical.bridges', 'technical.space-bridge'):
                self.assertNotIn('WIP', (PAGES / locale / (topic + '.md')).read_text())

    def test_clean_visual_coverage_and_cooking_interface(self):
        for locale in ('', '_zh_cn'):
            bosses = (PAGES / locale / 'adventure.bosses.md').read_text().split('## Related mods')[0].split('## 相关模组')[0]
            self.assertEqual(len(re.findall(r'!\[[^\]]*\]\(images/[^)]+\)', bosses)), 17)
            utensils = (PAGES / locale / 'food.utensils.md').read_text()
            self.assertIn('images/nav-visual-farmers-delight-pot-interface.png', utensils)
            self.assertIn('images/nav-visual-farmers-delight-pot-campfire.png', utensils)

    def test_all_article_bodies_are_authored_without_placeholders(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertTrue(all(page['drafted'] for page in manifest['pages']))
        for locale in ('', '_zh_cn'):
            for page in manifest['pages']:
                self.assertNotIn('WIP', (PAGES / locale / page['filename']).read_text())

    def test_templates_do_not_restore_competing_provider_navigation(self):
        for template in (ROOT / 'docs/handbook-templates').glob('*.md'):
            text = template.read_text()
            self.assertNotIn('mod-catalogs.md', text)
            self.assertNotIn('<Color id="gold">', text)
            self.assertNotIn('Item recipe', text)

if __name__ == '__main__':
    unittest.main()
