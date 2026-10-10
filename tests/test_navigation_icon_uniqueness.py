"""Whole-tree icon contract, including the introduction and both locales."""
import ast
from collections import Counter
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
import unittest

ROOT = Path(__file__).resolve().parents[1]
# A scratch generation may be checked without touching the watched resources.
PAGES = Path(os.environ.get('HANDBOOK_ICON_PAGES', str(ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook')))


def generator_definitions():
    """Evaluate definitions only, stopping before any generated-page writes."""
    source = ROOT / 'scripts/build-handbook-draft.py'
    tree = ast.parse(source.read_text())
    stop = next(i for i, node in enumerate(tree.body)
                if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == 'status' for t in node.targets))
    tree.body = tree.body[:stop]
    namespace: dict[str, Any] = {'__file__': str(source)}
    previous = sys.argv
    try:
        sys.argv = [str(source)]
        exec(compile(tree, str(source), 'exec'), namespace)
    finally:
        sys.argv = previous
    return namespace


class NavigationIconUniqueness(unittest.TestCase):
    def test_every_topic_has_an_explicit_globally_unique_icon(self):
        definitions = generator_definitions()
        topics = {p['page_id'] for p in definitions['page_defs']} | {'index'}
        icons = definitions['reference_icons']
        self.assertEqual(len(topics), 113)
        self.assertEqual(set(icons), topics)
        collisions = {icon: count for icon, count in Counter(icons.values()).items() if count > 1}
        self.assertEqual(collisions, {})
        for icon in icons.values():
            self.assertRegex(icon, r'^[a-z0-9_.-]+:[a-z0-9_./-]+$')

    def test_generated_locales_match_the_audited_complete_tree(self):
        audit = json.loads((ROOT / 'docs/final-review/navigation-icon-audit.json').read_text())
        expected = {entry['id']: entry for entry in audit['topics']}
        self.assertEqual(len(expected), 113)
        for locale in ('en_us', 'zh_cn'):
            folder = PAGES / ('_zh_cn' if locale == 'zh_cn' else '')
            files = {path.stem: path for path in folder.glob('*.md')}
            self.assertEqual(set(files), set(expected))
            observed = []
            for topic, path in files.items():
                front = path.read_text().split('---', 2)[1]
                icon = re.search(r'^  icon: (.+)$', front, re.M).group(1)
                parent = re.search(r'^  parent: (.+)$', front, re.M)
                title = json.loads(re.search(r'^  title: (.+)$', front, re.M).group(1))
                self.assertEqual(icon, expected[topic]['icon'], (locale, topic))
                self.assertEqual(parent.group(1) if parent else None, expected[topic]['parent'])
                self.assertEqual(title, expected[topic]['labels'][locale])
                observed.append(icon)
            self.assertEqual(len(set(observed)), 113)

    def test_credits_is_an_intro_child_with_a_unique_book_icon(self):
        definitions = generator_definitions()
        self.assertEqual(definitions['reference_parents']['help.credits'], 'index.md')
        self.assertEqual(definitions['titles']['help.credits'], 'Credits')
        self.assertEqual(definitions['zh_titles']['help.credits'], '鸣谢')
        self.assertEqual(definitions['reference_icons']['help.credits'], 'minecraft:written_book')
        topics = {page['page_id'] for page in definitions['page_defs']}
        self.assertEqual(len(topics - set(definitions['reference_hubs'])), 104)
        self.assertEqual(len(definitions['reference_sections']) + 1, 17)

    def test_audit_matches_every_explicit_icon_and_selected_artifact(self):
        definitions = generator_definitions()
        audit = json.loads((ROOT / 'docs/final-review/navigation-icon-audit.json').read_text())
        self.assertEqual({topic['id']: topic['icon'] for topic in audit['topics']}, definitions['reference_icons'])
        self.assertEqual(audit['counts']['total_locale_entries'], 226)
        for topic in audit['topics']:
            self.assertTrue(topic['rationale'])
            self.assertTrue(topic['provenance'])
            namespace = topic['icon'].split(':')[0]
            if topic['id'].startswith('class.'):
                self.assertTrue(topic['provenance']['original_native_reference_present'])
                self.assertTrue(topic['provenance']['class_reference_evidence'])
            elif namespace != 'minecraft':
                artifact = audit['selected_artifacts'][namespace]
                self.assertTrue(artifact['matches_selected_hash'])
                self.assertTrue(topic['provenance']['item_registration_calls'])
                self.assertTrue((ROOT / artifact['metadata_path']).is_file())

    def test_building_uses_registered_modded_representatives(self):
        icons = generator_definitions()['reference_icons']
        self.assertEqual(icons['building.palette'], 'chipped:mason_table')
        self.assertEqual(icons['building.copycats'], 'copycats:copycat_block')
        self.assertEqual(icons['building.furniture'], 'handcrafted:oak_chair')
        self.assertEqual(icons['building.placement'], 'mechtrowel:mech_trowel')


if __name__ == '__main__':
    unittest.main()
