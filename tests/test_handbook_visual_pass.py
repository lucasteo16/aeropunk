"""Verify the visual-first improvement without claiming in-game rendering."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import struct
import unittest
import zlib
from handbook_revision_contract import before_development_update

ROOT = Path(__file__).resolve().parents[1]
IMAGE_BASE = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
NATIVE = r'<(?:ItemIcon|ItemLink|ItemImage|Recipe|KeyBind|EmiSearch)\b[^>]*>'


def catalog_rows(body):
    rows = []
    for line in body.splitlines():
        if not line.startswith('| ') or line.startswith('| ---'):
            continue
        first = line.split('|')[1].strip()
        if first in {'Creature', 'Mod', '生物', '模组'}:
            continue
        rows.append(line)
    return rows


class HandbookVisualPassTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        cls.before = json.loads((ROOT / 'docs/handbook-before-visual-pass.json').read_text())
        cls.scope = json.loads((ROOT / 'docs/handbook-visual-pass.json').read_text())
        cls.visuals = json.loads((ROOT / 'docs/handbook-visual-sources.json').read_text())
        cls.navigation = json.loads((ROOT / 'docs/handbook-creature-navigation.json').read_text())

    def test_scope_and_untouched_articles(self):
        content = before_development_update(self.content, include_mars_retirement=True)
        actual = {topic for topic, locales in content.items()
                  if locales != self.before.get(topic)}
        self.assertEqual(actual, set(self.scope['changed_topics']))
        for topic, locales in self.before.items():
            if topic not in actual:
                self.assertEqual(locales, content[topic], topic)
        self.assertEqual(set(self.content) - set(self.before), set(self.navigation))

    def test_native_interactions_preserved(self):
        content = before_development_update(self.content)
        moved = {'adventure.creatures', 'adventure.aquatic'}
        for topic in set(self.before) - moved:
            for locale in ('en_us', 'zh_cn'):
                self.assertEqual(sorted(re.findall(NATIVE, self.before[topic][locale])),
                                 sorted(re.findall(NATIVE, content[topic][locale])),
                                 (topic, locale))

    def test_bilingual_images_links_and_references(self):
        for topic in self.scope['changed_topics']:
            locales = self.content[topic]
            self.assertEqual(set(locales), {'en_us', 'zh_cn'})
            for body in locales.values():
                self.assertTrue(body.startswith('## '), topic)
                self.assertNotRegex(body, '[\u2013\u2014;；]')
            for pattern in (NATIVE, r'!\[[^\]]*\]\(([^)]+)\)', r'\]\(([^)]+\.md)\)'):
                self.assertEqual(sorted(re.findall(pattern, locales['en_us'])),
                                 sorted(re.findall(pattern, locales['zh_cn'])), topic)

    def test_creature_catalogs_preserved_and_shortened(self):
        families = self.scope['aquatic_family_pages']
        for locale in ('en_us', 'zh_cn'):
            old = Counter(catalog_rows(self.before['adventure.aquatic'][locale]))
            rows = [row for topic in families for row in catalog_rows(self.content[topic][locale])]
            normalized = [row.replace('（Lionfish）', '').replace('（Snailfish）', '') for row in rows]
            self.assertEqual(Counter(normalized), old, locale)
            self.assertEqual(len(rows), self.scope['aquatic_species_rows'])
            for topic in families:
                self.assertLessEqual(len(catalog_rows(self.content[topic][locale])), 30, topic)
            original = Counter(catalog_rows(self.before['adventure.creatures'][locale]))
            split = Counter(catalog_rows(self.content['adventure.creatures'][locale]))
            for topic in self.navigation:
                if topic.startswith('creatures.'):
                    split.update(catalog_rows(self.content[topic][locale]))
            self.assertEqual(split, original, locale)
            self.assertLess(len(self.content['adventure.creatures'][locale]),
                            len(self.before['adventure.creatures'][locale]))
            self.assertLess(len(self.content['adventure.aquatic'][locale]),
                            len(self.before['adventure.aquatic'][locale]))

    def test_authentic_assets_and_png_integrity(self):
        added = {row['resource']: row for key, row in self.visuals.items()
                 if key.startswith('handbook:visual-')}
        self.assertEqual(set(added), set(self.scope['image_resources']))
        for resource, row in added.items():
            self.assertEqual(resource, resource.lower())
            self.assertTrue(row['source_url'].startswith('https://'))
            self.assertIn(row['kind'], {'publisher gallery', 'publisher main-description image'})
            self.assertTrue(row['publisher'])
            self.assertTrue(row['license'])
            data = (IMAGE_BASE / resource).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['resource_sha256'])
            self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
            offset = 8
            compressed = bytearray()
            header = None
            while offset < len(data):
                size = struct.unpack('>I', data[offset:offset + 4])[0]
                kind = data[offset + 4:offset + 8]
                payload = data[offset + 8:offset + 8 + size]
                checksum = struct.unpack('>I', data[offset + 8 + size:offset + 12 + size])[0]
                self.assertEqual(zlib.crc32(kind + payload) & 0xffffffff, checksum)
                if kind == b'IHDR':
                    header = struct.unpack('>IIBBBBB', payload)
                elif kind == b'IDAT':
                    compressed.extend(payload)
                offset += size + 12
            assert header is not None, 'Missing PNG header'
            width, height, depth, color, *_ = header
            self.assertEqual([width, height], row['dimensions'])
            self.assertLessEqual(width, 1120)
            self.assertLessEqual(height, 800)
            self.assertEqual((depth, color), (8, 2))
            self.assertEqual(len(zlib.decompress(compressed)), height * (width * 3 + 1))


if __name__ == '__main__':
    unittest.main()
