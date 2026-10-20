"""Regression checks for asset hints, deliberately not runtime registry tests."""
from collections import defaultdict
import importlib.util
import io
import json
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('item_asset_check', ROOT / 'scripts/check_item_existence.py')
assert SPEC is not None and SPEC.loader is not None
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def archive_bytes(members):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        for path, data in members.items():
            archive.writestr(path, data)
    return buffer.getvalue()


def scan(members):
    index = defaultdict(set)
    with zipfile.ZipFile(io.BytesIO(archive_bytes(members))) as archive:
        CHECK.harvest(archive, index)
    return index


class ItemAssetDiscovery(unittest.TestCase):
    def test_nested_item_path_is_not_flattened_or_changed_to_dots(self):
        index = scan({
            'assets/example/models/item/chipped/alchemy_upgrade.json': '{}',
            'assets/example/lang/en_us.json': json.dumps({
                'item.example.chipped.alchemy_upgrade': 'Alchemy Upgrade',
                'item.example.unregistered_item': 'Not registered',
            }),
        })
        self.assertEqual(index['example'], {'chipped/alchemy_upgrade'})
        self.assertNotIn('chipped.alchemy_upgrade', index['example'])
        self.assertNotIn('alchemy_upgrade', index['example'])
        self.assertNotIn('unregistered_item', index['example'])

    def test_blockstate_path_is_an_asset_hint(self):
        index = scan({'assets/example/blockstates/paired_connector.json': '{}'})
        self.assertEqual(index['example'], {'paired_connector'})

    def test_both_nested_jar_layouts_are_scanned(self):
        inner = archive_bytes({'assets/nested/models/item/tool.json': '{}'})
        for directory in ('jars', 'jarjar'):
            with self.subTest(directory=directory):
                index = scan({'META-INF/' + directory + '/nested.jar': inner})
                self.assertEqual(index['nested'], {'tool'})

    def test_translation_without_assets_supplies_no_registry_candidate(self):
        index = scan({'assets/example/lang/en_us.json': '{"item.example.fake": "Fake"}'})
        self.assertEqual(dict(index), {})


if __name__ == '__main__':
    unittest.main()
