"""Refurbishment bar for chapters rebuilt under docs/handbook-refurbish-playbook.md.

These checks are deliberately strict. They fail a chapter that keeps a text only
section, an empty item grid, a malformed grid or a banned character.
"""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONTENT = json.loads((ROOT / 'docs/handbook-content.json').read_text())
SCOPE = json.loads((ROOT / 'docs/handbook-refurbish-scope.json').read_text())
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
VISUAL = re.compile(r'(!\[|<ItemGrid|<ItemImage|<GameScene|<Recipe|<BlockImage)', re.M)
GRID = re.compile(r'<ItemGrid>(.*?)</ItemGrid>', re.S)
ICON = re.compile(r'<ItemIcon id="([^"]+)" />')
NATIVE = re.compile(r'<(?:ItemIcon|ItemLink|ItemImage)\b[^>]*\bid="([^"]+)"')


def topics():
    for batch in SCOPE['batches'].values():
        yield from batch['topics']


class RefurbishedChapter(unittest.TestCase):
    def test_generated_tutorial_actions_precede_sections(self):
        selected = set(topics()) | {
            'reference.food', 'reference.machines-storage', 'reference.vehicles'
        }
        for topic in sorted(selected):
            for locale in ('en_us', 'zh_cn'):
                with self.subTest(topic=topic, locale=locale):
                    folder = PAGES / '_zh_cn' if locale == 'zh_cn' else PAGES
                    body = (folder / (topic + '.md')).read_text().split('---', 2)[2]
                    rows = [line for line in body.splitlines()
                            if line.startswith('![YouTube](images/tutorial-video.png) ')]
                    self.assertEqual(len(rows), 1, 'exactly one tutorial action row is required')
                    row = rows[0]
                    self.assertRegex(row, r'\[English\]\(https://www\.youtube\.com/results\?search_query=[^)]+\)')
                    self.assertRegex(row, r'\[中文\]\(https://www\.youtube\.com/results\?search_query=[^)]+\)')
                    title = re.search(r'(?m)^# .+$', body)
                    section = re.search(r'(?m)^## .+$', body)
                    self.assertIsNotNone(title)
                    self.assertIsNotNone(section)
                    assert title is not None and section is not None
                    between = body[title.end():section.start()].strip()
                    self.assertEqual(between, row, 'tutorial row belongs immediately below the title')

    def test_scope_topics_exist(self):
        for topic in topics():
            self.assertIn(topic, CONTENT)
            self.assertEqual(set(CONTENT[topic]), {'en_us', 'zh_cn'}, topic)

    def test_bodies_start_with_a_section(self):
        for topic in topics():
            for locale, body in CONTENT[topic].items():
                self.assertTrue(body.startswith('## '), (topic, locale))

    def test_no_text_only_section(self):
        for topic in topics():
            for locale, body in CONTENT[topic].items():
                parts = re.split(r'(?m)^(## .*)$', body)
                for index in range(1, len(parts), 2):
                    content = '\n'.join(line for line in parts[index + 1].splitlines()
                                        if not line.startswith('![YouTube]'))
                    if not content.strip():
                        continue
                    self.assertTrue(VISUAL.search(content), (topic, locale, parts[index]))

    def test_grids_are_well_formed(self):
        for topic in topics():
            for locale, body in CONTENT[topic].items():
                for grid in GRID.findall(body):
                    icons = ICON.findall(grid)
                    self.assertTrue(icons, (topic, locale, 'empty grid'))
                    self.assertFalse(re.sub(r'<ItemIcon id="[^"]+" />', '', grid).strip(),
                                     (topic, locale, 'non item children'))

    def test_no_banned_characters_in_prose(self):
        for topic in topics():
            for locale, body in CONTENT[topic].items():
                prose = re.sub(r'<[^>]+>', '', re.sub(r'https?://\S+', '', body))
                self.assertNotRegex(prose, '[\u2013\u2014;；]', (topic, locale))

    def test_bilingual_native_parity(self):
        for topic in topics():
            english = CONTENT[topic]['en_us']
            chinese = CONTENT[topic]['zh_cn']
            self.assertEqual(sorted(set(NATIVE.findall(english))),
                             sorted(set(NATIVE.findall(chinese))), topic)
            self.assertEqual(len(re.findall(r'<Recipe\b', english)),
                             len(re.findall(r'<Recipe\b', chinese)), topic)
            for component in ('Recipe', 'KeyBind', 'EmiSearch'):
                pattern = r'<' + component + r'\b[^>]*>'
                self.assertEqual(set(re.findall(pattern, english)),
                                 set(re.findall(pattern, chinese)), (topic, component))


if __name__ == '__main__':
    unittest.main()
