"""Authored space content and authentic asset contracts, independent of generation."""
import hashlib
import json
from pathlib import Path
import re
import struct
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
TOPICS = ('world.dimensions', 'space.vehicle-transfer', 'space.life-support', 'space.navigation')
PROVIDERS = ('mods/create-cosmonatics.pw.toml', 'mods/cosmonautics-deep-air.pw.toml', 'mods/aeroengine-fuel-compat.pw.toml')


def load(name):
    return json.loads((ROOT / 'docs' / name).read_text())


class CosmonauticsSourceQuality(unittest.TestCase):
    def test_destinations_have_one_authored_home(self):
        source = load('handbook-content.json')
        self.assertNotIn('space.destinations', source)
        self.assertNotIn('space.destinations.md', json.dumps(source))
        for locale in ('en_us', 'zh_cn'):
            body = source['world.dimensions'][locale]
            for name in ('cosmo-moon-terrain', 'cosmo-deep-space'):
                self.assertIn('images/' + name + '.png', body)
            self.assertNotIn('20,000', body)
            self.assertNotIn('19,000', body)
            self.assertNotIn('universe_planets', body)
            self.assertNotRegex(body, r'planet records|行星数据|物理句柄')

    def test_reference_and_visual_parity(self):
        source = load('handbook-content.json')
        for topic in TOPICS:
            rows = source[topic]
            native = lambda body: re.findall(r'<(ItemIcon|ItemLink|Recipe|KeyBind)[^>]*id="([^"]+)"', body)
            images = lambda body: re.findall(r'!\[[^\]]*\]\(([^)]+)\)', body)
            links = lambda body: re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', body)
            self.assertEqual(native(rows['en_us']), native(rows['zh_cn']), topic)
            self.assertEqual(images(rows['en_us']), images(rows['zh_cn']), topic)
            self.assertEqual(links(rows['en_us']), links(rows['zh_cn']), topic)
            self.assertEqual(rows['en_us'].count('\n## '), rows['zh_cn'].count('\n## '), topic)

    def test_sections_prose_and_standalone_links(self):
        source = load('handbook-content.json')
        for topic in TOPICS + ('vehicles.engines', 'travel.destinations', 'food.fishing', 'power.industry', 'performance.baseline'):
            for body in source[topic].values():
                self.assertTrue(body.startswith('## '), topic)
                self.assertNotRegex(body, r'[;；—–]|\bWIP\b|not installed|selected release|prototype|artifact|未经测试|所选版本|已安装|未安装|审查|原型|物理句柄')
                for line in body.splitlines():
                    if re.search(r'(?<!!)\[[^\]]+\]\([^)]*\.md\)', line):
                        self.assertTrue(line.startswith('- ') or line.startswith('| '), (topic, line))

    def test_released_mechanics_and_survival_boundaries_remain_explicit(self):
        source = load('handbook-content.json')
        for locale in ('en_us', 'zh_cn'):
            flight = source['space.vehicle-transfer'][locale]
            for value in ('20,000', '19,000', '2,500', '1,000', '60', 'minecraft:lava_bucket'):
                self.assertIn(value, flight)
            self.assertNotIn('<Recipe id="rocketnautics:mechanical_crafting/rocket_thruster"', flight)
            life = source['space.life-support'][locale]
            for item in ('create:copper_diving_helmet', 'create:copper_backtank', 'rocketnautics:space_helmet', 'rocketnautics:copper_anchor_boots', 'cosmonauticsdeepair:gravity_generator'):
                self.assertIn('<ItemLink id="' + item + '"', life)
            self.assertNotIn('<Recipe id="rocketnautics:space_helmet"', life)
            self.assertIn('create_submarine:oxygene_diffuser', life)
            self.assertIn('<Recipe id="create_submarine:oxygen_diffuser"', life)
        self.assertIn('at least one room', source['space.life-support']['en_us'])
        self.assertIn('至少', source['space.life-support']['zh_cn'])
        self.assertIn('does not need a diffuser', source['space.life-support']['en_us'])
        self.assertIn('not the ship\'s steering', source['space.navigation']['en_us'])

    def test_provider_icons_are_real_publisher_assets(self):
        visuals = load('handbook-visual-sources.json')
        purposes = load('handbook-provider-purposes.json')
        descriptions = load('handbook-project-descriptions.json')
        queries = load('handbook-item-queries.json')
        for provider in PROVIDERS:
            row = visuals[provider]
            self.assertEqual(row['kind'], 'publisher icon')
            self.assertEqual(row['dimensions'], [96, 96])
            self.assertEqual(row['project_url'], descriptions[provider]['url'])
            self.assertIn(row['project_id'], row['source_url'])
            self.assertEqual(set(purposes[provider]), {'en_us', 'zh_cn'})
            self.assertEqual(queries[provider]['en_us'], queries[provider]['zh_cn'])

    def test_assets_have_provenance_hashes_lowercase_paths_and_decodable_pixels(self):
        visuals = load('handbook-visual-sources.json')
        rows = [visuals[key] for key in PROVIDERS]
        rows += [value for key, value in visuals.items() if key.startswith('handbook:cosmo-')]
        self.assertEqual(len(rows), 8)
        for row in rows:
            resource = row['resource']
            self.assertEqual(resource, resource.lower())
            data = (IMAGES / resource).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['resource_sha256'])
            self.assertRegex(row['original_sha256'], r'^[0-9a-f]{64}$')
            for key in ('source_url', 'project_url', 'publisher', 'license', 'rights'):
                self.assertTrue(row[key], (resource, key))
            self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
            offset, compressed, ended = 8, bytearray(), False
            while offset < len(data):
                size = struct.unpack('>I', data[offset:offset + 4])[0]
                tag = data[offset + 4:offset + 8]
                payload = data[offset + 8:offset + 8 + size]
                crc = struct.unpack('>I', data[offset + 8 + size:offset + 12 + size])[0]
                self.assertEqual(zlib.crc32(tag + payload) & 0xffffffff, crc)
                if tag == b'IHDR':
                    self.assertEqual(list(struct.unpack('>II', payload[:8])), row['dimensions'])
                if tag == b'IDAT':
                    compressed.extend(payload)
                if tag == b'IEND':
                    ended = True
                    break
                offset += size + 12
            self.assertTrue(ended)
            self.assertTrue(zlib.decompress(compressed))


if __name__ == '__main__':
    unittest.main()
