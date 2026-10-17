"""Small, source-level contracts for Astropunk's portable utility backpacks."""
import json
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'config/paxi/datapacks/astropunk-backpacks'
RECIPES = PACK / 'data/sophisticatedbackpacks/recipe'
MODULES = {
    'crafting_upgrade', 'stonecutter_upgrade', 'tool_swapper_upgrade',
    'refill_upgrade', 'feeding_upgrade', 'jukebox_upgrade',
    *(f'chipped/{name}_upgrade' for name in (
        'botanist_workbench', 'glassblower', 'carpenters_table', 'mason_table',
        'loom_table', 'alchemy_bench', 'tinkering_table')),
}
BACKPACKS = {'backpack', *(f'{tier}_backpack' for tier in (
    'copper', 'iron', 'gold', 'diamond', 'netherite'))}


class BackpackRecipesTest(unittest.TestCase):
    def test_only_approved_modules_are_obtainable_and_installable(self):
        common = tomllib.loads((ROOT / 'config/sophisticatedcore-common.toml').read_text())
        flags = dict(entry.rsplit('|', 1) for entry in common['common']['enabledItems'])
        self.assertEqual(flags.get('sophisticatedcore:ender_linker'), 'false',
                         'Remote linked storage bypasses the approved field-kit role')
        actual = {key.removeprefix('sophisticatedbackpacks:')
                  for key, value in flags.items()
                  if key.startswith('sophisticatedbackpacks:') and value == 'true'}
        self.assertEqual(actual, MODULES | BACKPACKS | {'upgrade_base'})
        server = tomllib.loads((ROOT / 'config/sophisticatedbackpacks-server.toml').read_text())['server']
        limits = dict(entry.rsplit('|', 1) for entry in server['maxUpgradesPerStorage'])
        for key, value in flags.items():
            item = key.removeprefix('sophisticatedbackpacks:')
            if key.startswith('sophisticatedbackpacks:') and value == 'false' and (
                    item.endswith('_upgrade') or item.startswith('stack_') and 'conversion' not in item):
                self.assertEqual(limits[item], '0', item)
        self.assertFalse(tomllib.loads((ROOT / 'config/sophisticatedbackpacks-common.toml').read_text())['common']['chestLootEnabled'])
        self.assertFalse(server['entityBackpackAdditions']['addLoot'])
        self.assertFalse(server['entityBackpackAdditions']['playJukebox'])
        self.assertEqual(server['entityBackpackAdditions']['entityLootTableList'], ['minecraft:player|null'])

    def test_nested_shulkers_and_backpacks_are_blocked(self):
        server = tomllib.loads((ROOT / 'config/sophisticatedbackpacks-server.toml').read_text())['server']
        self.assertTrue(server['containerItemsDisallowed'])
        self.assertFalse(server['canBePlacedInContainerItems'])
        self.assertTrue(server['nerfs']['onlyWornBackpackTriggersUpgrades'])
        blocked = set(server['disallowedItems'])
        self.assertTrue({f'sophisticatedbackpacks:{item}' for item in BACKPACKS} <= blocked)
        for tier in ('copper', 'iron', 'gold', 'diamond', 'netherite'):
            self.assertIn(f'reinfshulker:{tier}_shulker_box', blocked)
            for color in ('white', 'orange', 'magenta', 'light_blue', 'yellow', 'lime',
                          'pink', 'gray', 'light_gray', 'cyan', 'purple', 'blue',
                          'brown', 'green', 'red', 'black'):
                self.assertIn(f'reinfshulker:{color}_{tier}_shulker_box', blocked)

    def test_authoritative_tier_capacities_and_upgrade_slots(self):
        path = ROOT / 'config/sophisticatedbackpacks-server.toml'
        self.assertTrue(path.is_file(), 'Missing authoritative server balance')
        server = tomllib.loads(path.read_text())['server']
        tiers = ('leather', 'copper', 'iron', 'gold', 'diamond', 'netherite')
        for tier, slots, upgrades in zip(tiers, (9, 18, 27, 36, 45, 54),
                                         (1, 1, 2, 2, 3, 3)):
            with self.subTest(tier=tier):
                self.assertEqual(server[f'{tier}Backpack']['inventorySlotCount'], slots)
                self.assertEqual(server[f'{tier}Backpack']['upgradeSlotCount'], upgrades)

    def recipe(self, name):
        path = RECIPES / f'{name}.json'
        self.assertTrue(path.is_file(), f'Missing progression override: {name}')
        return json.loads(path.read_text())

    def test_module_base_requires_create_brass(self):
        base = self.recipe('upgrade_base')
        self.assertEqual(base['type'], 'minecraft:crafting_shaped')
        self.assertEqual(base['key']['I'], {'item': 'create:brass_ingot'})
        self.assertEqual(base['result'], {
            'count': 1, 'id': 'sophisticatedbackpacks:upgrade_base'})

    def test_upgrades_are_sequential_and_preserve_backpack_data(self):
        iron = self.recipe('iron_backpack')
        self.assertEqual(iron['type'], 'sophisticatedbackpacks:backpack_upgrade')
        self.assertEqual(iron['key']['B'], {
            'item': 'sophisticatedbackpacks:copper_backpack'})
        diamond = self.recipe('diamond_backpack')
        self.assertEqual(diamond['type'], 'sophisticatedbackpacks:backpack_upgrade')
        self.assertEqual(diamond['key']['B'], {
            'item': 'sophisticatedbackpacks:gold_backpack'})
        self.assertEqual(diamond['key']['S'], {'item': 'minecraft:shulker_shell'})
        for recipe in (iron, diamond):
            self.assertEqual(recipe['result']['count'], 1)
            self.assertIn({'type': 'sophisticatedcore:item_enabled',
                           'itemRegistryName': recipe['result']['id']},
                          recipe['neoforge:conditions'])


if __name__ == '__main__':
    unittest.main()
