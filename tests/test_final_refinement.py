from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class FinalRefinement(unittest.TestCase):
    def test_shared_edition_docs_do_not_claim_local_install_state(self):
        for locale in ('', '_zh_cn'):
            for path in (PAGES / locale).glob('*.md'):
                text = path.read_text()
                for unwanted in ('Baseline, installed', 'not installed here', 'Not installed here', '已安装基准版', '当前未安装', 'provider project artwork, not a structure screenshot'):
                    self.assertNotIn(unwanted, text, path)
            all_text = '\n'.join(p.read_text() for p in (PAGES / locale).glob('*.md'))
            self.assertIn('（仅重型版）' if locale else '(heavy edition only)', all_text)

    def test_food_priority_and_documentation_home(self):
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            self.assertIn('  position: 0\n', (base / 'food.utensils.md').read_text())
            self.assertIn('  position: 1\n', (base / 'food.hunger.md').read_text())
            self.assertIn('  parent: reference.technical.md\n', (base / 'help.reference.md').read_text())

    def test_unavailable_enchanting_items_are_not_referenced(self):
        for locale in ('', '_zh_cn'):
            text = (PAGES / locale / 'machines.enchanting.md').read_text()
            for item in ('blaze_composer', 'brass_bookshelf', 'infuser', 'affix_augmenter', 'gem_cutter'):
                self.assertNotRegex(text, r'id="create_enchantment_industry:' + item + '"')


if __name__ == '__main__':
    unittest.main()
