"""Player-facing query placement, independent of client screen rendering."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'


class QueryPresentation(unittest.TestCase):
    def test_templates_do_not_restore_removed_query_labels_or_wrapper(self):
        for path in sorted((ROOT / 'docs/handbook-templates').glob('*.md')):
            text = path.read_text()
            self.assertNotIn('quick-reference.md', text, path.name)
            self.assertNotIn('Browse items:', text, path.name)
            self.assertNotIn('浏览物品:', text, path.name)

    def test_section_queries_are_unlabeled_lines_directly_below_headings(self):
        bad = []
        query_sections = 0
        for path in sorted(PAGES.rglob('*.md')):
            text = path.read_text()
            for match in re.finditer(r'(?m)^#{2,3} [^\n]+\n\n([^\n]+)', text):
                line = match.group(1)
                if '<EmiSearch ' not in line or line.startswith('|'):
                    continue
                query_sections += 1
                if not re.fullmatch(r'<EmiSearch query="[^"]+" />(?: <EmiSearch query="[^"]+" />)*', line):
                    bad.append(str(path.relative_to(PAGES)) + ': ' + line)
            if 'Browse items:' in text or '浏览物品:' in text:
                bad.append(str(path.relative_to(PAGES)) + ': prefixed query remains')
        self.assertGreater(query_sections, 0)
        self.assertEqual(bad[:5], [], f'{len(bad)} query presentation violations')


if __name__ == '__main__':
    unittest.main()
