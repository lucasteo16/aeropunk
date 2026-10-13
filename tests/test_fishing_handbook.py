"""Source-quality checks for the bilingual fishing handbook update."""
import json
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
UPDATED = {
    'adventure.aquatic', 'adventure.creatures', 'adventure.settlements',
    'adventure.structures', 'fishing.habitats', 'food.fishing', 'food.hunger',
    'food.seafood', 'help.inspect', 'help.reference', 'machines.ore-processing',
    'power.burners', 'reference.food', 'technical.bridges', 'technical.libraries',
    'vehicles.water', 'visuals.lighting', 'world.dimensions',
}
NEW = {'adventure.aquatic', 'fishing.habitats', 'food.seafood'}


class FishingHandbookTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        cls.original = json.loads(subprocess.check_output(
            ['git', 'show', 'dc1ad93:docs/handbook-content.json'], cwd=ROOT, text=True))
        cls.evidence = json.loads((ROOT / 'docs/fishing-handbook-evidence.json').read_text())
        cls.visual_scope = json.loads((ROOT / 'docs/handbook-visual-pass.json').read_text())
        cls.creature_pages = json.loads((ROOT / 'docs/handbook-creature-navigation.json').read_text())

    def test_unrelated_articles_unchanged(self):
        for topic, locales in self.original.items():
            if topic not in UPDATED | set(self.visual_scope['changed_topics']):
                self.assertEqual(locales, self.content[topic], topic)
        self.assertEqual(set(self.content) - set(self.original), NEW | set(self.creature_pages))

    def test_bilingual_native_reference_parity(self):
        for topic in UPDATED:
            locales = self.content[topic]
            self.assertEqual(set(locales), {'en_us', 'zh_cn'}, topic)
            for body in locales.values():
                self.assertTrue(body.startswith('## '), topic)
                self.assertNotRegex(body, '[\u2013\u2014;；]')
                self.assertNotRegex(body, r'\*\*[^\n]*\*\*:')
            pattern = r'<(?:ItemIcon|ItemLink|ItemImage|Recipe|KeyBind|EmiSearch)\b[^>]*>'
            self.assertEqual(sorted(re.findall(pattern, locales['en_us'])),
                             sorted(re.findall(pattern, locales['zh_cn'])), topic)
            links = r'\]\(([^)]+\.md)\)'
            self.assertEqual(sorted(re.findall(links, locales['en_us'])),
                             sorted(re.findall(links, locales['zh_cn'])), topic)

    def test_acquisition_boundaries_and_short_stacks(self):
        english = self.content['food.fishing']['en_us']
        self.assertIn('Required rod attachments', english)
        self.assertIn('key.starcatcher.minigame_hit', english)
        self.assertIn('Natural swimming creatures and rod catches use different rules', english)
        self.assertIn('Amethyst Hook', english)
        self.assertIn('Short Stacks', self.content['food.hunger']['en_us'])
        self.assertIn('never raises', self.content['food.hunger']['en_us'])
        for points, limit in self.evidence['artifact_evidence']['short-stacks.pw.toml']['examples'].items():
            self.assertIn(f'| {points} | {limit} |', self.content['food.hunger']['en_us'])
        self.assertIn('Bucket capture and creature harvesting differ from rod loot',
                      self.content['food.seafood']['en_us'])

    def test_species_catalog_and_actual_library_home(self):
        species = self.evidence['artifact_evidence']['hybrid-aquatic.pw.toml']['natural_spawn_species']
        self.assertEqual(len(species), 120)
        family_pages = self.visual_scope['aquatic_family_pages']
        row_count = sum(len(re.findall(r'^\| [^|]+ \| [^|]+ \|$',
                                      self.content[topic]['en_us'], re.M))
                        for topic in family_pages)
        self.assertEqual(row_count, len(species) + 2 * len(family_pages))
        placements = json.loads((ROOT / 'docs/handbook-placement-overrides.json').read_text())
        queries = json.loads((ROOT / 'docs/handbook-item-queries.json').read_text())
        self.assertEqual(placements['mods/strut-your-stuff.pw.toml']['topic'], 'technical.libraries')
        self.assertEqual(queries['mods/strut-your-stuff.pw.toml'], {'en_us': [], 'zh_cn': []})
        self.assertNotIn('Reliable Advancements', self.content['help.reference']['en_us'])
        self.assertIn('Better Advancements', self.content['help.reference']['en_us'])

    def test_selected_artifact_evidence(self):
        for entry in self.evidence['artifact_evidence'].values():
            self.assertTrue(entry['hash_matches'], entry['filename'])
        self.assertFalse(self.evidence['client_runtime_tested'])


if __name__ == '__main__':
    unittest.main()
