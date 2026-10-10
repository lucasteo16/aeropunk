"""Source regressions for one unified, shallow handbook topic tree."""
from pathlib import Path
import json
import re
import unittest
from test_flat_sidebar import SECTIONS

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class NavigationSkeleton(unittest.TestCase):
    def test_reference_sections_have_one_primary_parent(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            self.assertFalse((base / 'quick-reference.md').exists())
            self.assertFalse((base / 'mod-catalogs.md').exists())
            self.assertEqual(list(base.glob('category-*.md')), [])
            for filename in ('adventure.bosses.md', 'adventure.creatures.md', 'adventure.structures.md', 'world.dimensions.md', 'reference.skills.md', 'reference.food.md', 'reference.building.md', 'reference.vehicles.md', 'reference.machines-storage.md', 'reference.utilities.md', 'reference.appearance.md', 'reference.audio.md', 'reference.technical.md'):
                self.assertNotIn('  parent:', (base / filename).read_text())

    def test_sidebar_is_acyclic_and_no_more_than_two_category_levels(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            for page in manifest['pages']:
                path = base / page['filename']
                seen = {path.name}
                current = path
                depth = 0
                while parent := re.search(r'^  parent: (.+)$', current.read_text(), re.M):
                    name = parent.group(1)
                    self.assertNotIn(name, seen)
                    seen.add(name)
                    current = base / name
                    self.assertTrue(current.is_file())
                    depth += 1
                self.assertIn(current.name, {topic + '.md' for topic in SECTIONS} | {'index.md'}, path.name)
                self.assertLessEqual(depth, 2, path.name)

    def test_home_and_sidebar_reference_directory_match(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            home = (base / 'index.md').read_text()
            refs = {topic + '.md' for topic in SECTIONS}
            self.assertEqual(set(re.findall(r'\]\(([^)]+\.md)\)', home)), {'help.credits.md'})
            self.assertNotIn('| Reference | Contents |', home)
            self.assertEqual(len(refs), 16)
            self.assertNotIn('reference.equipment.md', refs)
            for child in ('reference.equipment.md', 'combat.abilities.md'):
                self.assertIn('  parent: reference.skills.md\n', (base / child).read_text())
            for filename in refs:
                self.assertNotIn('  parent:', (base / filename).read_text())

    def test_provider_inventory_has_one_primary_home_and_honest_footer_rows(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        checklist = json.loads((ROOT / 'docs/guide-authoring-checklist.json').read_text())
        paths = [e['metadata_path'] for e in manifest['content']]
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(set(paths), {e['metadata_path'] for e in checklist['entries']} | {'mods/guideme.pw.toml', 'mods/astropunk-handbook-access-1.0.0.jar'})
        homes = [path for page in manifest['pages'] for path in page['metadata_paths']]
        self.assertCountEqual(paths, homes)
        for locale in ('', '_zh_cn'):
            heading = '## 相关模组' if locale else '## Related mods'
            for entry in manifest['content']:
                text = (PAGES / locale / (entry['topic'] + '.md')).read_text()
                self.assertIn(heading, text, entry['metadata_path'])
                footer = text.rsplit(heading, 1)[1]
                self.assertNotRegex(footer, r'^## ', entry['topic'])
                rows = [line for line in footer.splitlines() if '[' + entry['name'].replace('|', ',') + '](' + entry['topic'] + '.md)' in line]
                self.assertEqual(len(rows), 1, entry['metadata_path'])
                row = rows[0]
                self.assertTrue('![' in row or '<ItemImage ' in row, row)
                label = {'baseline': '', 'heavy': '（仅重型版）' if locale else '(heavy edition only)', 'deferred': '（暂缓加入）' if locale else '(deferred addition)'}[entry['availability']]
                self.assertIn(label, row, entry['metadata_path'])
                visuals = json.loads((ROOT / 'docs/handbook-visual-sources.json').read_text())
                visual = visuals.get(entry['metadata_path'])
                if visual and visual.get('kind') in ('publisher icon', 'bundled publisher icon'):
                    self.assertIn(visual['resource'], row)

    def test_hubs_end_with_related_providers_linked_to_detailed_topics(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'reference.machines-storage.md').read_text()
            heading = '## 相关模组' if locale else '## Related mods'
            self.assertIn(heading, text)
            footer = text.rsplit(heading, 1)[1]
            self.assertIn('Create', footer)
            self.assertIn('](machines.rotation.md)', footer)
            self.assertIn('](storage.portable.md)', footer)

    def test_display_renames_keep_topic_identifiers(self):
        for locale in ('', '_zh_cn'):
            for name, title in (('help.search.md', '浏览配方' if locale else 'Browse recipe'), ('reference.vehicles.md', '交通' if locale else 'Transport')):
                text = (PAGES / locale / name).read_text()
                self.assertIn('# ' + title + '\n', text)
                self.assertIn('  title: ' + json.dumps(title, ensure_ascii=False), text)
                self.assertNotIn('  parent:', text)

    def test_audio_compatibility_providers_have_audio_homes(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        by_path = {e['metadata_path']: e for e in manifest['content']}
        for path in ('mods/cool-rain-reforged.pw.toml', 'mods/pf-neoforge.pw.toml', 'mods/sable-cool-rain.pw.toml', 'mods/presence-footsteps-x-sable.pw.toml'):
            self.assertEqual(by_path[path]['topic'], 'reference.audio')
            self.assertEqual(by_path[path]['category'], 'Visuals and sound')
        for locale in ('', '_zh_cn'):
            self.assertFalse((PAGES / locale / 'sounds.ambience.md').exists())
            self.assertNotIn('  parent:', (PAGES / locale / 'reference.audio.md').read_text())

    def test_schema_counts_match_generated_files(self):
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertEqual(manifest['category_count'], 0)
        self.assertEqual(manifest['navigation_page_count'], 0)
        self.assertEqual(len(list(PAGES.glob('*.md'))), manifest['article_count'] + manifest['reference_directory_count'] + manifest['navigation_page_count'] + 1)


if __name__ == '__main__':
    unittest.main()
