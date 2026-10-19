"""Focused source and comparison-overlay regressions, no game launch."""
from pathlib import Path
import json
import re
import runpy
import unittest
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
SOURCE = json.loads((ROOT / 'docs/handbook-content.json').read_text())
CLASSES = {key for key in SOURCE if key.startswith('class.')}
HUBS = {'reference.skills', 'reference.equipment', 'combat.handling', 'combat.martial',
        'combat.magic', 'combat.skills', 'combat.abilities', 'equipment.weapons-armor',
        'equipment.accessories', 'equipment.display'}
COMBAT = CLASSES | HUBS
NATIVE = re.compile(r'<(?:ItemLink|ItemIcon|ItemImage)\b[^>]*\bid="([^"]+)"')


class CombatReview(unittest.TestCase):
    def test_complete_bilingual_scope(self):
        self.assertEqual(len(CLASSES), 18)
        self.assertEqual(len(COMBAT), 28)
        for topic in COMBAT:
            self.assertEqual(set(SOURCE[topic]), {'en_us', 'zh_cn'})
            self.assertTrue(all(body.startswith('## ') for body in SOURCE[topic].values()))

    def test_language_independent_tutorial_choices(self):
        for topic in COMBAT:
            urls = []
            for locale, body in SOURCE[topic].items():
                found = re.findall(r'\[(English|中文)\]\((https://www.youtube.com/results\?[^)]+)\)', body)
                self.assertEqual([label for label, _ in found], ['English', '中文'], (topic, locale))
                self.assertEqual(body.count('![YouTube](images/tutorial-video.png)'), 1)
                page = PAGES / ('_zh_cn' if locale == 'zh_cn' else '') / (topic + '.md')
                rendered_body = page.read_text().split('---', 2)[2].strip().split('\n', 1)[1].strip()
                action_row, remaining = rendered_body.split('\n\n', 1)
                self.assertTrue(action_row.startswith('![YouTube](images/tutorial-video.png) '), (topic, locale))
                self.assertTrue(remaining.startswith('## '), (topic, locale))
                queries = [parse_qs(urlsplit(url).query)['search_query'][0] for _, url in found]
                self.assertTrue(all('1.21.1' in query for query in queries))
                self.assertNotEqual(queries[0], queries[1])
                urls.append(found)
            self.assertEqual(urls[0], urls[1], topic)

    def test_native_reference_locale_parity(self):
        for topic in COMBAT:
            values = SOURCE[topic]
            self.assertEqual(set(NATIVE.findall(values['en_us'])), set(NATIVE.findall(values['zh_cn'])), topic)
            for tag in ('Recipe', 'KeyBind'):
                pattern = r'<' + tag + r'\b[^>]*\bid="([^"]+)"'
                self.assertEqual(re.findall(pattern, values['en_us']), re.findall(pattern, values['zh_cn']), topic)

    def test_native_grids_have_only_item_children(self):
        for topic in COMBAT:
            for locale, body in SOURCE[topic].items():
                for grid in re.findall(r'<ItemGrid>(.*?)</ItemGrid>', body, re.S):
                    self.assertFalse(re.sub(r'<ItemIcon\s+id="[^"]+"\s*/>', '', grid).strip(), (topic, locale))

    def test_landing_links_all_classes_without_stacked_weapon_cells(self):
        for locale, body in SOURCE['reference.skills'].items():
            links = set(re.findall(r'\]\((class\.[^)]+)\.md\)', body))
            self.assertEqual(links, CLASSES, locale)
            # One identification grid is allowed: the binding table that opens the
            # first steps. Stacked weapon cells on the landing page are what this
            # test stops, so the rule stays strict rather than permissive.
            grids = re.findall(r'<ItemGrid>.*?</ItemGrid>', body, re.S)
            self.assertEqual(grids, ['<ItemGrid><ItemIcon id="spell_engine:spell_binding" /></ItemGrid>'], locale)
            self.assertNotIn('<EmiSearch', body)
            page = (PAGES / ('_zh_cn' if locale == 'zh_cn' else '') / 'reference.skills.md').read_text()
            self.assertNotIn('## Related mods', page)
            self.assertNotIn('## 相关模组', page)

    def test_binding_has_one_primary_item_association(self):
        for locale in ('', '_zh_cn'):
            pages = {p.name: p.read_text().split('---', 2)[1] for p in (PAGES / locale).glob('*.md')}
            for item in ('spell_engine:spell_binding', 'spell_engine:spell_book', 'spell_engine:spell_scroll'):
                homes = [name for name, front in pages.items() if '  - ' + item + '\n' in front]
                self.assertEqual(homes, ['combat.abilities.md'])

    def test_class_links_follow_canonical_binding_home(self):
        for topic in CLASSES:
            for locale, body in SOURCE[topic].items():
                self.assertIn('](combat.abilities.md)', body)
                self.assertNotIn('[Spell binding & resources](combat.magic.md)', body)
                self.assertNotIn('[法术绑定与资源](combat.magic.md)', body)

    def test_arsenal_catalog_has_no_duplicate_inventory_and_preserves_roles(self):
        for locale, body in SOURCE['equipment.weapons-armor'].items():
            heading = '## Arsenal weapons' if locale == 'en_us' else '## Arsenal 武器'
            section = body.split(heading, 1)[1].split('\n## ', 1)[0]
            assignments = {}
            rows = re.findall(r'^\| [^|]+ \| <ItemGrid>(.*?)</ItemGrid> \| ([^|]+) \|$', section, re.M)
            self.assertEqual(len(rows), 18, locale)
            for grid, role in rows:
                for item in NATIVE.findall(grid):
                    self.assertNotIn(item, assignments, (locale, item))
                    assignments[item] = role
            self.assertEqual(len(assignments), 44, locale)
            self.assertEqual(len(NATIVE.findall(section)), 44, locale)
            self.assertNotIn('<ItemLink', section)
            english = locale == 'en_us'
            arcane, fire, frost, healing = (
                ('Arcane power', 'Fire power', 'Frost power', 'Healing power') if english
                else ('奥术强度', '火焰强度', '冰霜强度', '治疗强度'))
            joiner = ' and ' if english else '与'
            damage = {
                '1': [arcane, frost], '2': [arcane, fire], '3': [arcane, fire],
                '4': [fire, frost], '5': [arcane, frost], '6': [arcane, frost],
                'sw': [arcane, fire, frost]}
            for item, role in assignments.items():
                suffix = item.rsplit('_', 1)[1]
                if item.startswith('arsenal:unique_staff_damage_'):
                    expected = joiner.join(damage[suffix])
                elif item.startswith('arsenal:unique_staff_heal_'):
                    expected = joiner.join([healing, arcane]) if suffix == '1' else healing
                elif item.startswith('arsenal:unique_shield_'):
                    expected = 'Armor toughness and Maximum health' if english else '护甲韧性与生命上限'
                elif item.startswith(('arsenal:unique_longbow_', 'arsenal:unique_heavy_crossbow_')):
                    expected = 'Ranged weapon' if english else '远程武器'
                else:
                    expected = 'Melee weapon or focus' if english else '近战武器或法器'
                self.assertEqual(role, expected, (locale, item))

    def test_arcane_scene_preserves_complete_example_loadout(self):
        scenes = []
        for locale, body in SOURCE['class.arcane'].items():
            scene = re.findall(r'<GameScene\b.*?</GameScene>', body, re.S)
            self.assertEqual(len(scene), 1, locale)
            self.assertIn('interactive={true}', scene[0])
            self.assertIn('<Entity id="minecraft:armor_stand"', scene[0])
            self.assertNotIn('<ImportStructure', scene[0])
            self.assertIn('ArmorItems:[{id:"wizards:wizard_robe_feet",count:1},'
                          '{id:"wizards:wizard_robe_legs",count:1},'
                          '{id:"wizards:wizard_robe_chest",count:1},'
                          '{id:"wizards:wizard_robe_head",count:1}]', scene[0])
            self.assertIn('HandItems:[{id:"wizards:wand_arcane",count:1},{}]', scene[0])
            self.assertLess(body.index('<GameScene'), body.index('images/visual-arcane-casting.png'))
            scenes.append(scene[0])
        self.assertEqual(scenes[0], scenes[1])

    def test_build_links_are_standalone_actions(self):
        for locale, body in SOURCE['reference.skills'].items():
            rows = [line for line in body.splitlines() if line.startswith('| <ItemImage ')]
            self.assertEqual(len(rows), 18, locale)
            self.assertTrue(all(('Start ' if locale == 'en_us' else '开始') in row for row in rows))

    def test_scroll_transfer_states_resource_consequences(self):
        english = SOURCE['combat.abilities']['en_us']
        chinese = SOURCE['combat.abilities']['zh_cn']
        self.assertIn('consumes the scroll and charges the displayed experience-level cost', english)
        self.assertIn('This transfer does not require lapis', english)
        self.assertIn('会消耗卷轴，并扣除界面显示的普通经验等级', chinese)
        self.assertIn('这种转移不需要青金石', chinese)

    def test_old_clone_remaps_only_navigation_and_internal_destinations(self):
        clone = runpy.run_path(str(ROOT / 'scripts/combat-comparison.py'))['clone_original']
        original = ('---\nnavigation:\n  title: "Combat"\n  position: 8\n'
                    '  icon: minecraft:iron_sword\nitem_ids:\n  - minecraft:book\n'
                    '---\n\n# Combat\n\n## Classes\n\n'
                    '[Archer](class.archer.md#starter) ![Art](images/archer.png)\n')
        result = clone(original, ['reference.skills.md', 'class.archer.md'], False)
        self.assertIn('title: "Combat (old)"', result)
        self.assertIn('position: 9', result)
        self.assertNotIn('item_ids:', result)
        self.assertIn('[Archer](combat-old.class.archer.md#starter)', result)
        self.assertIn('![Art](images/archer.png)', result)
        self.assertIn('  icon: minecraft:iron_sword', result)


if __name__ == '__main__':
    unittest.main()
