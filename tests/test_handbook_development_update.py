"""Selected development handbook scope, source preservation and player content."""
from collections import Counter
import copy
import json
from pathlib import Path
import re
import subprocess
import unittest
from handbook_revision_contract import before_development_update, before_food_finalization

ROOT = Path(__file__).resolve().parents[1]
TOPICS = {'vehicles.airships', 'visuals.camera', 'help.controls', 'server.tools',
          'performance.baseline', 'visuals.lighting', 'world.dimensions'}
KEYS = {'key.aero_cam_sync.toggle', 'key.aero_cam_sync.open_config',
        'key.aero_player_tilt.toggle', 'key.aero_player_tilt.open_config'}
NATIVE = r'<(?:ItemIcon|ItemLink|ItemImage|Recipe|KeyBind|EmiSearch)\b[^>]*>'


class DevelopmentHandbook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = before_food_finalization(json.loads((ROOT / 'docs/handbook-content.json').read_text()))
        cls.revision = json.loads((ROOT / 'docs/handbook-development-update.json').read_text())
        cls.before = json.loads(subprocess.check_output(['git', 'show',
            cls.revision['guide_parent_commit'] + ':docs/handbook-content.json'],
            cwd=ROOT, text=True))

    def test_exact_scope_and_all_unrelated_prose_preserved(self):
        self.assertEqual(set(self.revision['topic_sha256']), TOPICS)
        self.assertEqual(set(self.content), set(self.before))
        changed = {topic for topic in self.content if self.content[topic] != self.before[topic]}
        self.assertEqual(changed, TOPICS)
        self.assertEqual(before_development_update(self.content), self.before)

    def test_revision_guard_rejects_edits_even_inside_approved_topics(self):
        changed = copy.deepcopy(self.content)
        changed['vehicles.airships']['en_us'] += '\nUnapproved text.\n'
        with self.assertRaises(AssertionError):
            before_development_update(changed)

    def test_bilingual_links_native_references_and_player_style(self):
        for topic in TOPICS:
            locales = self.content[topic]
            for body in locales.values():
                self.assertTrue(body.startswith('## '))
                self.assertNotRegex(body, '[\u2013\u2014;；]')
                self.assertNotRegex(body, r'\*\*[^\n]*\*\*:')
                self.assertNotRegex(body, r'(?i)OpenCL|worldgen|trial|review|prototype')
            for pattern in (NATIVE, r'\]\(([^)]+\.md)\)'):
                self.assertEqual(sorted(re.findall(pattern, locales['en_us'])),
                                 sorted(re.findall(pattern, locales['zh_cn'])), topic)

    def test_existing_native_interactions_preserved_with_only_verified_keys_added(self):
        for topic in TOPICS:
            for locale in ('en_us', 'zh_cn'):
                old = Counter(re.findall(NATIVE, self.before[topic][locale]))
                new = Counter(re.findall(NATIVE, self.content[topic][locale]))
                extra = Counter({f'<KeyBind id="{key}" />': 1 for key in KEYS}) if topic == 'vehicles.airships' else Counter()
                self.assertEqual(new, old + extra, (topic, locale))
        for artifact in self.revision['orientation_artifacts']:
            self.assertTrue(artifact['hash_matches_selected'])
            self.assertTrue(artifact['key_registration_verified'])

    def test_dimension_labels_match_packaged_titles_and_no_mars_surface(self):
        for locale in ('en_us', 'zh_cn'):
            titles = json.loads((ROOT / 'config/paxi/resourcepacks/astropunk-space-titles/assets/travelerstitles/lang' / (locale + '.json')).read_text())
            body = self.content['world.dimensions'][locale]
            for label in titles.values():
                self.assertIn(label, body)
        self.assertIn('without landable surfaces', self.content['world.dimensions']['en_us'])
        self.assertFalse((ROOT / 'mods/create-cosmonautics-expansion.pw.toml').exists())

    def test_border_and_performance_information_has_practical_boundaries(self):
        body = self.content['server.tools']['en_us']
        for token in ('/dimworldborder minecraft:overworld get', '/dimworldborder rocketnautics:moon get',
                      'full width of 5000', 'restart', 'moving ship'):
            self.assertIn(token, body)
        self.assertNotIn('rocketnautics_addon:', body)
        self.assertIn('Fast Noise', self.content['performance.baseline']['en_us'])
        self.assertIn('without special launch arguments', self.content['performance.baseline']['en_us'])
        self.assertIn('Existing player settings are preserved', self.content['visuals.lighting']['en_us'])


if __name__ == '__main__':
    unittest.main()