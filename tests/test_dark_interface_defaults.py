import json
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DarkInterfaceDefaults(unittest.TestCase):
    def test_dark_pack_is_client_only_enabled_and_explicitly_accepted(self):
        metadata = tomllib.loads((ROOT / 'resourcepacks/mandalas-gui-dark-mode.pw.toml').read_text())
        options = dict(line.split(':', 1) for line in (ROOT / 'configureddefaults/options.txt').read_text().splitlines() if ':' in line)
        pack = 'file/' + metadata['filename']
        self.assertEqual(metadata['side'], 'client')
        self.assertIn(pack, json.loads(options['resourcePacks']))
        self.assertIn(pack, json.loads(options['incompatibleResourcePacks']))
        index = tomllib.loads((ROOT / 'index.toml').read_text())
        self.assertTrue(any(entry['file'] == 'resourcepacks/mandalas-gui-dark-mode.pw.toml' for entry in index['files']))


if __name__ == '__main__':
    unittest.main()
