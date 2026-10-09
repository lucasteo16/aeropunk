"""Homepage-only presentation exception, not a rendered viewport test."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class HomeOpening(unittest.TestCase):
    def test_home_starts_with_ship_and_has_no_secondary_headings(self):
        for locale in ('', '_zh_cn'):
            page = (PAGES / locale / 'index.md').read_text()
            body = page.split('\n# Astropunk\n', 1)[1].strip()
            self.assertTrue(body.startswith('!['))
            self.assertIn('](images/home-merun173-airship.png)', body.splitlines()[0])
            self.assertIsNone(re.search(r'(?m)^#{2,6} ', body))
            self.assertEqual(len(re.findall(r'!\[[^\]]*\]\(', body)), 1)
            self.assertNotIn('<ItemImage ', body)
            self.assertNotIn('Your next project', body)
            self.assertNotIn('你的下一个项目', body)
            self.assertNotIn('](help.controls.md)', body)
            self.assertNotIn('## Related mods', body)
            self.assertLessEqual(len(body.split('\n\n')), 6)
        credits = (PAGES / 'help.credits.md').read_text()
        self.assertIn('Merun173', credits)
        self.assertIn('https://createmod.com/author/merun173', credits)
        english = (PAGES / 'index.md').read_text()
        self.assertLessEqual(len(english.split()), 230)


if __name__ == '__main__':
    unittest.main()
