"""Semantic navigation contract, exercised without generating handbook pages."""
from pathlib import Path
import copy
import json
import subprocess
import sys
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from handbook_navigation import CHILD_ORDER, ROOT_ORDER, navigation_metadata, assert_semantic_navigation


class SemanticOrdering(unittest.TestCase):
    def test_root_order_groups_access_exploration_gameplay_and_preferences(self):
        self.assertEqual(ROOT_ORDER, ('index', 'help.controls', 'help.search', 'reference.utilities',
            'maps.personal', 'world.dimensions', 'adventure.structures', 'adventure.creatures',
            'adventure.bosses', 'reference.skills', 'reference.food', 'reference.building',
            'reference.machines-storage', 'reference.vehicles', 'reference.appearance',
            'reference.audio', 'reference.technical', 'help.credits'))

    def test_transport_land_sea_sky_space_then_teleportation(self):
        self.assertEqual(CHILD_ORDER['reference.vehicles'], ('transport.local', 'transport.passenger',
            'transport.railway-builder', 'vehicles.water', 'vehicles.assembly', 'vehicles.controls',
            'vehicles.engines', 'vehicles.airships', 'vehicles.radar', 'vehicles.weapons',
            'space.vehicle-transfer', 'space.life-support', 'space.navigation', 'travel.destinations'))

    def test_every_child_list_has_practical_entry_points_and_functional_groups(self):
        expected = {
            'adventure.structures': ('adventure.settlements', 'adventure.loot'),
            'adventure.creatures': ('creatures.wilderness', 'creatures.friends', 'adventure.aquatic',
                'creatures.creepers', 'creatures.endermen', 'creatures.variants', 'creatures.guards',
                'creatures.cataclysm', 'creatures.illagers', 'creatures.summons'),
            'adventure.aquatic': ('aquatic.freshwater', 'aquatic.marine', 'aquatic.deepwater',
                'aquatic.sharks', 'aquatic.jellyfish', 'aquatic.cephalopods', 'aquatic.seafloor',
                'aquatic.mammals'),
            'maps.personal': ('maps.find', 'maps.shared'),
            'reference.utilities': ('help.inspect', 'interactions.carry', 'adventure.sleep', 'adventure.recovery'),
            'reference.skills': ('combat.handling', 'reference.equipment', 'equipment.weapons-armor',
                'equipment.accessories', 'equipment.display', 'combat.martial', 'combat.magic', 'combat.abilities', 'combat.skills'),
            'combat.martial': ('class.warrior', 'class.berserker', 'class.rogue', 'class.forcemaster',
                'class.archer', 'class.deadeye', 'class.war-archer', 'class.tundra-hunter'),
            'combat.magic': ('class.arcane', 'class.fire', 'class.frost', 'class.aqua', 'class.terra',
                'class.wind', 'class.priest', 'class.paladin', 'class.bard', 'class.witcher'),
            'reference.food': ('food.utensils', 'food.hunger', 'food.growing', 'food.fishing',
                'food.seafood', 'food.underground', 'food.nether', 'food.end',
                'food.encounters', 'food.machine-cooking'),
            'reference.building': ('building.palette', 'building.placement', 'building.architecture',
                'building.copycats', 'building.furniture', 'building.displays', 'building.factory', 'building.safety'),
            'reference.machines-storage': ('storage.portable', 'storage.handling', 'storage.bulk',
                'machines.rotation', 'machines.ore-processing', 'machines.logistics', 'machines.renewables',
                'machines.miscellaneous', 'power.stored-rotation', 'power.burners', 'power.industry',
                'power.electricity', 'machines.enchanting', 'machines.trading'),
            'reference.appearance': ('visuals.interface', 'visuals.camera', 'visuals.resource-packs',
                'visuals.models', 'visuals.weather', 'visuals.lighting', 'visuals.shader-packs'),
            'reference.technical': ('help.handbook', 'help.reference', 'performance.baseline',
                'server.tools', 'technical.bridges', 'technical.libraries'),
        }
        self.assertEqual(set(CHILD_ORDER), set(expected) | {'reference.vehicles'})
        for parent, children in expected.items():
            self.assertEqual(CHILD_ORDER[parent], children, parent)

    def test_generator_definitions_cover_all_pages_and_preserve_unique_icons(self):
        definitions = json.loads(subprocess.check_output([sys.executable,
            str(ROOT / 'scripts/build-handbook-draft.py'), '--check-navigation'], text=True))
        self.assertEqual(len(definitions), 130)
        self.assertNotIn('fishing.habitats', definitions)
        assert_semantic_navigation({k: {field: row[field] for field in ('parent', 'position')}
                                   for k, row in definitions.items()})
        self.assertEqual(len({row['icon'] for row in definitions.values()}), len(definitions))
        for row in definitions.values():
            self.assertTrue(row['title'])
            self.assertTrue(row['title_zh_cn'])

    def test_coverage_has_exact_sibling_order_and_no_retired_destination(self):
        coverage = json.loads((ROOT / 'docs/guide-coverage.json').read_text())
        self.assertEqual(coverage['navigation']['roots'], list(ROOT_ORDER))
        self.assertEqual(coverage['navigation']['sibling_order'],
                         {'roots': list(ROOT_ORDER), **{k: list(v) for k, v in CHILD_ORDER.items()}})
        self.assertNotIn('space.destinations', {p['page_id'] for p in coverage['pages']})
        self.assertNotIn('space.destinations', coverage['navigation']['topic_parents'])
        self.assertNotIn('fishing.habitats', {p['page_id'] for p in coverage['pages']})
        self.assertNotIn('fishing.habitats', coverage['navigation']['topic_parents'])
        for path, topic in [('mods/create-cosmonatics.pw.toml', 'world.dimensions'),
                            ('mods/paxi.pw.toml', 'server.tools')]:
            row = next(e for e in coverage['inventory'] if e['metadata_path'] == path)
            self.assertEqual(row['primary_home'], topic)
            checklist = json.loads((ROOT / 'docs/guide-authoring-checklist.json').read_text())
            self.assertEqual(next(e for e in checklist['entries'] if e['metadata_path'] == path)['topic'], topic)

    def test_negative_controls_reject_ties_reorders_wrong_parents_and_extra_pages(self):
        mutations = [lambda n: n['transport.passenger'].update(position=0),
                     lambda n: n['transport.passenger'].update(position=99),
                     lambda n: n['space.navigation'].update(parent='world.dimensions.md'),
                     lambda n: n.update({'space.destinations': {'parent': 'reference.vehicles.md', 'position': 20}}),
                     lambda n: n.pop('class.warrior')]
        for mutate in mutations:
            actual = copy.deepcopy(navigation_metadata())
            mutate(actual)
            with self.assertRaises(AssertionError):
                assert_semantic_navigation(actual)

    def test_declared_development_metadata_and_world_border_remain_byte_identical(self):
        coverage = json.loads((ROOT / 'docs/guide-coverage.json').read_text())
        baseline_commit = coverage['baseline_commit']
        paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', baseline_commit,
            'mods', 'resourcepacks', 'shaderpacks', 'config/paxi'], cwd=ROOT, text=True).splitlines()
        paths = [p for p in paths if p.endswith('.pw.toml') or p.startswith('config/paxi/')]
        baseline_metadata = {p for p in paths if p.endswith('.pw.toml')}
        pack = tomllib.loads((ROOT / 'pack.toml').read_text())
        heavy_metadata = set()
        self.assertEqual(pack['name'], 'Astropunk')
        if pack['version'].endswith('-h'):
            original_heavy = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only',
                '3366e71', 'mods', 'resourcepacks', 'shaderpacks'], cwd=ROOT, text=True).splitlines()
            original_shared = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only',
                'f5c24f3', 'mods', 'resourcepacks', 'shaderpacks'], cwd=ROOT, text=True).splitlines()
            # Retired shared providers are not Heavy additions to preserve.
            heavy_metadata = {p for p in original_heavy if p.endswith('.pw.toml')} - set(original_shared)
            self.assertEqual(len(heavy_metadata), 18)
        actual = {p.relative_to(ROOT).as_posix() for folder in ('mods', 'resourcepacks', 'shaderpacks')
                  for p in (ROOT / folder).glob('*.pw.toml')}
        edition_metadata = set()
        if pack['version'].endswith('-worldgen'):
            edition_metadata = {'mods/c2me-ocl.pw.toml'}
        elif pack['version'].endswith('-hosting'):
            edition_metadata = {'mods/easyauth.pw.toml'}
        self.assertEqual(actual, baseline_metadata | heavy_metadata | edition_metadata)
        for path in paths:
            self.assertEqual((ROOT / path).read_bytes(), subprocess.check_output(
                ['git', 'show', baseline_commit + ':' + path], cwd=ROOT), path)
        for path in heavy_metadata:
            self.assertEqual((ROOT / path).read_bytes(), subprocess.check_output(
                ['git', 'show', '3366e71:' + path], cwd=ROOT), path)
        coverage = json.loads((ROOT / 'docs/guide-coverage.json').read_text())
        self.assertEqual(coverage['baseline_commit'], baseline_commit)
        baseline = [e for e in coverage['inventory'] if e['availability'] == 'baseline']
        self.assertEqual(len(baseline), coverage['verification']['baseline_total'])
        self.assertEqual(len(coverage['inventory']), coverage['verification']['union_metadata_total'])
        for entry in baseline:
            if entry['metadata_path'].endswith('.pw.toml'):
                selected = tomllib.loads((ROOT / entry['metadata_path']).read_text())
                self.assertEqual(entry['selected_download'], selected['download'])
                # Retain the original provenance of unchanged selections, but
                # verify that its source really contains the selected bytes.
                self.assertEqual((ROOT / entry['metadata_path']).read_bytes(),
                    subprocess.check_output(['git', 'show', entry['source_commit'] + ':' +
                                             entry['metadata_path']], cwd=ROOT))

    def test_released_native_tree_all_orders_and_negative_controls_without_generation(self):
        report = json.loads(subprocess.check_output([sys.executable,
            str(ROOT / 'scripts/test-native-navigation.py'), '--metadata-only'], text=True))
        self.assertEqual(report['mode'], 'metadata-only')
        self.assertEqual({row['locale'] for row in report['tests']}, {'en_us', '_zh_cn'})
        for row in report['tests']:
            self.assertIn('130 nodes, eighteen ordered roots', row['output'])
            self.assertIn('all sibling orders and semantic reorder negative control', row['output'])
            self.assertIn('Space destinations resurrection and repair controls', row['output'])
            self.assertIn('obsolete Quick reference and Sound resurrection and repair controls', row['output'])
        self.assertFalse(report['rendered_verified'])


if __name__ == '__main__':
    unittest.main()
