"""Transport authoring contracts, including the defects found in final review."""
import hashlib
import json
from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
TOPICS = (
    'reference.vehicles', 'transport.local', 'transport.passenger',
    'transport.railway-builder', 'vehicles.water', 'vehicles.assembly',
    'vehicles.airships', 'vehicles.engines', 'vehicles.controls',
    'vehicles.radar', 'vehicles.weapons', 'space.vehicle-transfer',
    'space.life-support', 'space.navigation', 'travel.destinations',
)


class TransportFinalization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = json.loads((ROOT / 'docs/handbook-content.json').read_text())

    def test_every_topic_has_compact_bilingual_tutorials(self):
        for topic in TOPICS:
            for locale in ('en_us', 'zh_cn'):
                with self.subTest(topic=topic, locale=locale):
                    body = self.content[topic][locale]
                    self.assertTrue(body.startswith('## '))
                    first = body.splitlines()[2]
                    self.assertTrue(first.startswith('![YouTube](images/tutorial-video.png) '))
                    for row in body.splitlines():
                        if 'youtube.com/results?' not in row:
                            continue
                        self.assertRegex(row, r'^!\[(?:YouTube|Tutorial)\]\(images/tutorial-video.png\) ')
                        labels = re.findall(r'\[([^\]]+)\]\(https://www.youtube.com/results\?[^)]+\)', row)
                        self.assertEqual(labels, ['English', '中文'])
                        urls = re.findall(r'\]\((https://www.youtube.com/results\?[^)]+)\)', row)
                        self.assertEqual(len(urls), 2)
                        for url in urls:
                            self.assertFalse(any(c.isspace() or ord(c) > 127 for c in url))
                            self.assertTrue(parse_qs(urlparse(url).query).get('search_query', [''])[0].strip())

    def test_reference_grids_are_small_and_queries_native(self):
        for topic in TOPICS:
            for locale in ('en_us', 'zh_cn'):
                body = self.content[topic][locale]
                with self.subTest(topic=topic, locale=locale):
                    self.assertNotIn('</EmiSearch>', body)
                    for grid in re.findall(r'<ItemGrid>(.*?)</ItemGrid>', body, re.S):
                        self.assertLessEqual(len(re.findall(r'<ItemIcon\b', grid)), 6)

    def test_train_schedule_has_a_driver_and_real_conditions(self):
        english = self.content['transport.railway-builder']['en_us']
        chinese = self.content['transport.railway-builder']['zh_cn']
        self.assertIn('seated conductor', english)
        self.assertIn('wait condition', english)
        self.assertIn('乘务员', chinese)
        self.assertIn('等待条件', chinese)
        self.assertNotIn('one driver bogie per train', english)
        self.assertNotIn('will derail', english)
        self.assertNotIn('a train without one stops', english)

    def test_cannon_loading_and_propellant_are_not_conflated(self):
        english = self.content['vehicles.weapons']['en_us']
        self.assertNotIn('charge, projectile, close', english)
        self.assertNotIn('combined propellant and shot', english)
        self.assertIn('behind the projectile', english)
        self.assertIn('propellant, not a projectile', english)
        self.assertIn('barrel-side', english)
        self.assertNotIn('Big Cannons do not shove', english)

    def test_space_navigation_uses_real_transfer_coordinates(self):
        english = self.content['space.vehicle-transfer']['en_us']
        chinese = self.content['space.vehicle-transfer']['zh_cn']
        navigation = self.content['space.navigation']['en_us']
        self.assertIn('19,000', english)
        self.assertIn('19000', chinese.replace(',', ''))
        self.assertIn('20,000', english)
        self.assertNotIn('will fall faster', navigation)
        self.assertNotIn('Mars, gas giants, ice worlds', navigation)
        self.assertNotIn('long before crossing', navigation)
        self.assertIn('unsafe above height 5,000', navigation)
        self.assertIn('upper bound', navigation)
        self.assertNotIn('Cut thrust early and let gravity', english)
        self.assertNotIn('Keep the fuel tank higher', english)

    def test_oxygen_budget_matches_selected_bytecode_not_old_ponder(self):
        for topic in ('vehicles.water', 'space.life-support'):
            for locale in ('en_us', 'zh_cn'):
                body = self.content[topic][locale]
                self.assertNotIn('proportionally to', body)
                self.assertNotIn('按潜艇体积消耗氧气', body)
                self.assertNotIn('按舱室体积消耗氧气', body)
        self.assertIn('50 millibuckets', self.content['vehicles.water']['en_us'])

    def test_evidence_preserves_baseline_and_all_native_references(self):
        review = json.loads((ROOT / 'docs/transport-final-review.json').read_text())
        native = lambda body: sorted(set(re.findall(r'<(?:ItemIcon|ItemLink|ItemImage|Recipe)\b[^>]*\bid="([^"]+)"', body)))
        self.assertEqual(review['topics'], list(TOPICS))
        for topic in TOPICS:
            for locale in ('en_us', 'zh_cn'):
                body = self.content[topic][locale]
                record = review['topic_reviews'][topic][locale]
                self.assertEqual(hashlib.sha256(body.encode()).hexdigest(), record['body_sha256'])
                expected = set(record['baseline_native_ids'])
                for old, disposition in review['reference_corrections'].get(topic, {}).items():
                    if old in expected:
                        expected.remove(old)
                        if disposition['replacement']:
                            expected.add(disposition['replacement'])
                self.assertLessEqual(expected, set(native(body)))
                self.assertEqual(native(body), native(self.content[topic]['zh_cn' if locale == 'en_us' else 'en_us']))
        unrelated = {k: v for k, v in self.content.items() if k not in TOPICS}
        digest = hashlib.sha256(json.dumps(unrelated, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        self.assertEqual(digest, review['unrelated_source_sha256'])
        self.assertEqual(review['status'], 'ready-for-user-review')
        self.assertFalse(review['runtime_verified'])
        self.assertEqual(hashlib.sha256((ROOT / 'docs/handbook-content.json').read_bytes()).hexdigest(), review['source_file_sha256']['after'])

    def test_landing_order_matches_native_sidebar(self):
        import sys
        sys.path.insert(0, str(ROOT / 'scripts'))
        from handbook_navigation import CHILD_ORDER
        for locale in ('en_us', 'zh_cn'):
            links = re.findall(r'\]\(([^)]+)\.md\)', self.content['reference.vehicles'][locale])
            self.assertEqual(links, list(CHILD_ORDER['reference.vehicles']))

    def test_later_edits_cannot_hide_behind_historical_restoration(self):
        import copy
        from handbook_revision_contract import before_machines_finalization
        for topic in ('vehicles.water', 'space.navigation', 'food.utensils', 'machines.rotation'):
            changed = copy.deepcopy(self.content)
            changed[topic]['en_us'] += '\nUnreviewed change.'
            with self.assertRaises(AssertionError, msg=topic):
                before_machines_finalization(changed)

    def test_every_packaged_resource_has_current_reviewed_bytes(self):
        review = json.loads((ROOT / 'docs/transport-final-review.json').read_text())
        pack = ROOT / 'resourcepacks/astropunk-guide-preview'
        actual = {p.relative_to(pack).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in pack.rglob('*') if p.is_file()}
        self.assertEqual(actual, review['resource_sha256'])


if __name__ == '__main__':
    unittest.main()
