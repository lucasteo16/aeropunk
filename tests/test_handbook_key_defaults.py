from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HandbookDefaults(unittest.TestCase):
    def test_requested_pack_keybindings_are_unique_and_exact(self):
        lines = (ROOT / 'configureddefaults/options.txt').read_text().splitlines()
        for identifier, value in {
            'key_key.astropunk_handbook_access.open': 'key.keyboard.period',
            'key_key.guideme.guide': 'key.keyboard.comma',
        }.items():
            matching = [line for line in lines if line.startswith(identifier + ':')]
            self.assertEqual(matching, [identifier + ':' + value])
        # The two requested edits must not silently rebind unrelated controls.
        self.assertIn('key_iris.keybind.toggleShaders:key.keyboard.period', lines)


if __name__ == '__main__':
    unittest.main()
