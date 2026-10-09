"""Review-contract checks for compact, illustrated reference pages."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'

class ReferenceVisuals(unittest.TestCase):
    def test_sidebar_labels_are_short_and_icons_complete(self):
        for locale in ('', '_zh_cn'):
            for p in (PAGES / locale).glob('*.md'):
                front = p.read_text().split('\n---\n', 1)[0]
                if p.name != 'index.md':
                    self.assertRegex(front, r'\n  icon: [a-z_]+:[a-z0-9_]+')
                if not locale:
                    match = re.search(r'^  title: (.+)$', front, re.M)
                    assert match is not None, p.name
                    title = json.loads(match.group(1))
                    self.assertLessEqual(len(title), 24, p.name)
        self.assertIn('Spells & skills', (PAGES / 'reference.skills.md').read_text())
        self.assertIn('Machines & storage', (PAGES / 'reference.machines-storage.md').read_text())

    def test_controls_separates_every_major_section(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'help.controls.md').read_text()
            headings = len(re.findall(r'^## ', text, re.M))
            self.assertEqual(text.count('\n***\n'), headings - 1)
            self.assertNotIn('Related mods', text)
            self.assertNotIn('相关模组', text)
            self.assertIn('key.astropunk_handbook_access.open', text)

    def test_dimensions_uses_real_screenshots_and_accurate_abyss_status(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'world.dimensions.md').read_text()
            for image in ('parent-incendium-terrain.png', 'parent-nullscape-terrain.png'):
                self.assertIn(image, text)
            self.assertNotIn('publisher screenshot', text.lower())
            self.assertNotIn('模组发布者截图', text)
            self.assertNotIn('<ItemGrid>', text)
        text = (PAGES / 'world.dimensions.md').read_text()
        self.assertIn('Abyss', text)
        self.assertIn('disables that dimension outside development', text)

    def test_recipe_reference_illustrates_interface_and_tree(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'help.search.md').read_text()
            self.assertIn('parent-emi-recipes.png', text)
            self.assertIn('parent-emi-tree.png', text)
            self.assertNotIn('Publisher description', text)

    def test_entire_reference_tree_has_authored_content(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        authored = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        by_filename = {p['filename']: p for p in manifest['pages']}
        for filename, page in by_filename.items():
            text = (PAGES / filename).read_text()
            current = text
            belongs = False
            while parent := re.search(r'^  parent: (.+)$', current, re.M):
                name = parent.group(1)
                if name == 'quick-reference.md':
                    belongs = True
                    break
                current = (PAGES / name).read_text()
            if belongs:
                self.assertIn(page['topic'], authored)
                for locale in ('', '_zh_cn'):
                    body = (PAGES / locale / filename).read_text()
                    self.assertNotIn('Work in progress', body)
                    self.assertNotIn('WIP', body)
                    if not locale:
                        for heading in re.findall(r'^#{2,3} (.+)$', body, re.M):
                            self.assertLessEqual(len(heading), 24, (filename, heading))
                    self.assertTrue(any(token in body for token in ('<ItemGrid', '<ItemImage', '<Recipe', '![', '| ')), filename)

    def test_review_removes_movement_and_corrects_access_claims(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'help.controls.md').read_text()
            self.assertNotIn('## Movement', text)
            self.assertNotIn('## 移动', text)
            self.assertNotIn('The inventory also has a Handbook button.', text)
            self.assertNotIn('物品栏也有手册按钮。', text)

    def test_catalog_entries_all_have_visuals(self):
        for locale in ('', '_zh_cn'):
            for page in (PAGES / locale).glob('category-*.md'):
                text = page.read_text()
                for row in text.splitlines():
                    if row.startswith('| ') and ('Publisher description' in text or '官方简介' in text):
                        if re.search(r'\]\([a-z][a-z0-9.-]+\.md\)', row) and not row.endswith('| Reference |') and not row.endswith('| 参考 |') and not row.endswith('| WIP |'):
                            self.assertTrue('![' in row or '<ItemImage ' in row, (page.name, row))

    def test_review_navigation_and_punctuation(self):
        authored = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        for topic, locales in authored.items():
            for locale, body in locales.items():
                self.assertNotIn(';', body, (topic, locale))
                self.assertNotIn('；', body, (topic, locale))
                for line in body.splitlines():
                    if re.search(r'(?<!!)\[[^\]]+\]\([^)]*\.md\)', line):
                        self.assertTrue(line.startswith(('- ', '| ')), (topic, locale, line))
        for locale in ('', '_zh_cn'):
            controls = (PAGES / locale / 'help.controls.md').read_text()
            recipe = (PAGES / locale / 'help.search.md').read_text()
            self.assertIn('<Color id="gold">/guidemec astropunk:handbook open</Color>', controls)
            self.assertIn('<Color id="gold">@create</Color>', recipe)
            equipment = (PAGES / locale / 'equipment.weapons-armor.md').read_text()
            for unavailable in ('ruby_rapid_crossbow', 'ruby_heavy_crossbow', 'ruby_spear'):
                self.assertNotIn('archers:' + unavailable, equipment)

    def test_local_images_exist(self):
        for p in PAGES.rglob('*.md'):
            for image in re.findall(r'!\[[^\]]*\]\((images/[^)]+)\)', p.read_text()):
                target = PAGES / image
                self.assertTrue(target.is_file(), (p.name, image))
                self.assertEqual(target.read_bytes()[:8], b'\x89PNG\r\n\x1a\n')

if __name__ == '__main__':
    unittest.main()
