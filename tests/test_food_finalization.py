"""Final accepted Food chapter contract, separate from unfinished chapters."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import unittest
from handbook_revision_contract import before_food_finalization, before_machines_finalization

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
CONTENT = json.loads((ROOT / 'docs/handbook-content.json').read_text())
MANIFEST = json.loads((ROOT / 'docs/food-chapter-final-review.json').read_text())
TOPICS = MANIFEST['topics']
NAMED = {'food.underground', 'food.nether', 'food.encounters'}


class FoodFinalization(unittest.TestCase):
    def test_chapter_and_accepted_pages_preserved(self):
        self.assertEqual(len(TOPICS), 11)
        for topic, expected in MANIFEST['accepted_topic_hashes'].items():
            actual = hashlib.sha256(json.dumps(CONTENT[topic], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
            self.assertEqual(actual, expected, topic)

    def test_food_only_source_scope(self):
        before = json.loads(subprocess.check_output(['git', 'show', MANIFEST['development_base'] + ':docs/handbook-content.json'], cwd=ROOT, text=True))
        historical = before_machines_finalization(CONTENT)
        for topic, bodies in before.items():
            if topic not in set(TOPICS) | {'fishing.habitats', 'world.dimensions', 'adventure.aquatic'}:
                self.assertEqual(historical[topic], bodies, topic)

    def test_retirement_and_book_lookup(self):
        self.assertNotIn('fishing.habitats', CONTENT)
        for path in PAGES.rglob('*.md'):
            self.assertNotIn('fishing.habitats', path.read_text(), str(path))
        for language in ('en_us', 'zh_cn'):
            self.assertIn('starcatcher:', CONTENT['food.fishing'][language])

    def test_historical_restoration_rejects_any_unapproved_edit(self):
        before = json.loads(subprocess.check_output(['git', 'show', MANIFEST['development_base'] + ':docs/handbook-content.json'], cwd=ROOT, text=True))
        self.assertEqual(before_food_finalization(CONTENT), before)
        for topic in ('food.underground', 'food.fishing', 'vehicles.airships'):
            changed = json.loads(json.dumps(CONTENT))
            changed[topic]['en_us'] += '\nUnapproved text.\n'
            with self.assertRaises(AssertionError, msg=topic):
                before_food_finalization(changed)
        changed = dict(CONTENT, **{'fishing.habitats': before['fishing.habitats']})
        with self.assertRaises(AssertionError):
            before_food_finalization(changed)

    def test_generated_article_changes_are_food_and_retirement_links_only(self):
        revision_path = ROOT / 'docs/machines-storage-revision-contract.json'
        revision = json.loads(revision_path.read_text()) if revision_path.exists() else None
        if revision:
            before_machines_finalization(CONTENT)
            endpoint = revision['development_base']
            # Later owned pages have their own exact source contract. Every other
            # generated article must still match the historical Food endpoint.
            for page in PAGES.rglob('*.md'):
                transport_path = ROOT / 'docs/transport-final-review.json'
                transport = json.loads(transport_path.read_text()) if transport_path.exists() else None
                if transport and page.stem in transport['topics']:
                    resource = page.relative_to(ROOT / 'resourcepacks/astropunk-guide-preview').as_posix()
                    self.assertEqual(hashlib.sha256(page.read_bytes()).hexdigest(), transport['resource_sha256'][resource], resource)
                    continue  # Exact Transport resource bytes, never a topic exemption.
                if page.stem not in revision['topics']:
                    relative = page.relative_to(ROOT).as_posix()
                    expected = subprocess.check_output(['git', 'show', endpoint + ':' + relative], cwd=ROOT)
                    self.assertEqual(page.read_bytes(), expected, relative)
            changed = subprocess.check_output(['git', 'diff', '--name-only', MANIFEST['development_base'], endpoint, '--', str(PAGES)], cwd=ROOT, text=True).splitlines()
        else:
            changed = subprocess.check_output(['git', 'diff', '--name-only', MANIFEST['development_base'], '--', str(PAGES)], cwd=ROOT, text=True).splitlines()
        allowed = set(TOPICS) | {'fishing.habitats', 'world.dimensions', 'adventure.aquatic'}
        self.assertTrue(changed)
        for path in changed:
            if path.endswith('.md'):
                self.assertIn(Path(path).stem, allowed, path)

    def test_named_page_column_labels(self):
        for topic in NAMED:
            self.assertNotIn('Identify it', CONTENT[topic]['en_us'])
            self.assertIn('| View |', CONTENT[topic]['en_us'])
            self.assertIn('| 外观 |', CONTENT[topic]['zh_cn'])

    def test_tutorial_under_title_in_all_generated_food_pages(self):
        for topic in TOPICS:
            for locale in ('', '_zh_cn'):
                body = (PAGES / locale / (topic + '.md')).read_text()
                rows = re.findall(r'(?m)^!\[YouTube\].*$', body)
                self.assertEqual(len(rows), 1, (topic, locale))
                self.assertIn('[English]', rows[0])
                self.assertIn('[中文]', rows[0])
                first_section = re.search(r'(?m)^## ', body)
                self.assertIsNotNone(first_section)
                assert first_section is not None
                self.assertIn(rows[0], body[:first_section.start()])

    def test_native_reference_and_link_parity(self):
        pattern = r'<(ItemIcon|ItemLink|ItemImage|Recipe|KeyBind|EmiSearch)\b[^>]*\bid="([^"]+)"'
        for topic in TOPICS:
            en, zh = CONTENT[topic]['en_us'], CONTENT[topic]['zh_cn']
            self.assertEqual(set(re.findall(pattern, en)), set(re.findall(pattern, zh)), topic)
            interactions = r'<(?:Recipe|KeyBind|EmiSearch)\b[^>]*>'
            self.assertEqual(set(re.findall(interactions, en)), set(re.findall(interactions, zh)), topic)
            self.assertEqual(set(re.findall(r'\]\(([^)]+\.md)\)', en)), set(re.findall(r'\]\(([^)]+\.md)\)', zh)), topic)

    def test_canonical_compact_grids_and_section_visuals(self):
        for topic in TOPICS:
            for locale, body in CONTENT[topic].items():
                for grid in re.findall(r'<ItemGrid>(.*?)</ItemGrid>', body, re.S):
                    self.assertRegex(grid, r'^(?:<ItemIcon id="[^"]+" />)+$', (topic, locale))
                    self.assertLessEqual(grid.count('<ItemIcon '), 6, (topic, locale))
                for title, section in re.findall(r'(?ms)^## ([^\n]+)\n(.*?)(?=^## |\Z)', body):
                    section = re.sub(r'(?m)^!\[YouTube\].*$', '', section)
                    self.assertRegex(section, r'<(?:ItemGrid|Recipe|GameScene|ItemImage)\b|!\[', (topic, locale, title))

    def test_critical_interactions_and_exact_recipe_path(self):
        nether = CONTENT['food.nether']['en_us']
        self.assertIn('mynethersdelight:crafting/raw_stuffed_hoglin', nether)
        self.assertNotIn('<Recipe id="mynethersdelight:raw_stuffed_hoglin"', nether)
        self.assertIn('roast_stuffed_hoglin', nether)
        self.assertIn('bowls', nether)
        underground = CONTENT['food.underground']['en_us']
        self.assertNotIn('fifth slot', underground)
        self.assertNotIn('Bar made with gossypium', underground)
        self.assertIn('minersdelight:baked_tentacles', underground)
        self.assertIn('either a baked cave carrot or vegan patty', underground)
        self.assertIn('烤洞穴胡萝卜或素饼', CONTENT['food.underground']['zh_cn'])
        self.assertNotIn('pot recipes that do not use it', underground)
        for grid in re.findall(r'<ItemGrid>(.*?)</ItemGrid>', CONTENT['food.encounters']['en_us'], re.S):
            ids = set(re.findall(r'id="([^"]+)"', grid))
            self.assertFalse({'lendersdelight:raw_deepling_meat', 'lendersdelight:deepling_meat'} <= ids)


if __name__ == '__main__':
    unittest.main()
