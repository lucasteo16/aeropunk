"""Review-feedback image coverage and unchanged prose checks."""
import hashlib
import json
from pathlib import Path
import re
import unittest
from handbook_revision_contract import before_development_update

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class HandbookImageFeedbackTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        cls.review = json.loads((ROOT / 'docs/handbook-image-feedback.json').read_text())
        cls.sources = json.loads((ROOT / 'docs/handbook-visual-sources.json').read_text())

    def test_every_requested_topic_and_appearance_page_has_images(self):
        required = {'travel.destinations', 'space.vehicle-transfer', 'vehicles.weapons',
                    'vehicles.radar', 'machines.enchanting', 'power.industry',
                    'power.burners', 'machines.rotation', 'combat.martial',
                    'adventure.aquatic', 'help.inspect', 'interactions.carry'}
        required.update(k for k in self.content if k.startswith('visuals.'))
        self.assertEqual(required, set(self.review['changed_topics']))
        for topic in required:
            for locale in ('en_us', 'zh_cn'):
                self.assertRegex(self.content[topic][locale], r'!\[[^\]]+\]\(images/[^)]+\)')
        for topic in self.content:
            english = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', self.content[topic]['en_us'])
            chinese = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', self.content[topic]['zh_cn'])
            self.assertEqual(english, chinese, topic)

    def test_only_documented_image_blocks_changed(self):
        restored = json.loads(json.dumps(before_development_update(self.content, include_mars_retirement=True)))
        for row in reversed(self.review['insertions']):
            body = restored[row['topic']][row['locale']]
            self.assertEqual(body.count(row['block']), 1, row['topic'])
            restored[row['topic']][row['locale']] = body.replace(row['block'], '', 1)
        self.assertEqual(set(restored), set(self.review['before_topic_sha256']))
        for topic, locales in restored.items():
            digest = hashlib.sha256(json.dumps(locales, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
            self.assertEqual(digest, self.review['before_topic_sha256'][topic], topic)

    def test_assets_and_honest_provenance(self):
        resources = {row['resource']: row for key, row in self.sources.items()
                     if key.startswith('handbook:feedback-')}
        self.assertEqual(set(resources), set(self.review['image_resources']))
        self.assertEqual(len(resources), 20)
        for resource, row in resources.items():
            data = (BASE / resource).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['resource_sha256'])
            self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
            self.assertEqual(resource, resource.lower())
            self.assertTrue(row['source_url'])
            self.assertTrue(row['publisher'])
            self.assertTrue(row['rights_note'])
            self.assertLessEqual(row['dimensions'][0], 1120)
            self.assertLessEqual(row['dimensions'][1], 800)
        supplied = resources['images/feedback-oil-extraction.png']
        self.assertEqual(supplied['kind'], 'user-supplied Reddit screenshot')
        self.assertEqual(supplied['license']['id'], 'unknown')
        self.assertIn('not provided', supplied['rights_note'])
        self.assertIn('crop', resources['images/feedback-earth-orbit.png'])


if __name__ == '__main__':
    unittest.main()
