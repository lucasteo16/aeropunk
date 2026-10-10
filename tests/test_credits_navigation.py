from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class CreditsNavigation(unittest.TestCase):
    def test_credits_is_last_root_in_both_languages(self):
        for folder in (BASE, BASE / '_zh_cn'):
            credits = (folder / 'help.credits.md').read_text().split('---', 2)[1]
            self.assertNotIn('  parent:', credits)
            match = re.search(r'position: (\d+)', credits)
            assert match is not None
            position = int(match.group(1))
            for file in folder.glob('*.md'):
                if file.name == 'help.credits.md':
                    continue
                front = file.read_text().split('---', 2)[1]
                if '  parent:' not in front:
                    match = re.search(r'position: (\d+)', front)
                    self.assertLess(int(match.group(1)) if match else 0, position)


if __name__ == '__main__':
    unittest.main()
