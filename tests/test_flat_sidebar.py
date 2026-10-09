"""Generated navigation regressions for native first-level handbook sections."""
from pathlib import Path
import json
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
SECTIONS = ('help.controls', 'help.search', 'adventure.bosses', 'adventure.creatures', 'adventure.structures', 'world.dimensions', 'reference.skills', 'reference.food', 'reference.building', 'reference.vehicles', 'reference.machines-storage', 'maps.personal', 'reference.utilities', 'reference.appearance', 'reference.audio', 'reference.technical')

class FlatSidebar(unittest.TestCase):
    def test_generated_sections_are_exact_native_roots(self):
        subprocess.run([sys.executable, str(ROOT / 'scripts/build-handbook-draft.py')], check=True, capture_output=True)
        for locale in ('', '_zh_cn'):
            base = PAGES / locale
            roots = {path.name for path in base.glob('*.md') if not re.search(r'^  parent:', path.read_text(), re.M)}
            self.assertEqual(roots, {'index.md'} | {topic + '.md' for topic in SECTIONS})
            self.assertFalse((base / 'quick-reference.md').exists())
            for position, topic in enumerate(SECTIONS):
                self.assertIn(f'  position: {position}\n', (base / (topic + '.md')).read_text())
            for path in base.glob('*.md'):
                self.assertNotIn('quick-reference.md', path.read_text())
            home = (base / 'index.md').read_text()
            self.assertEqual(re.findall(r'\]\(([^)]+\.md)\)', home), ['help.credits.md'])
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        self.assertEqual(manifest['navigation_page_count'], 0)
        self.assertEqual(manifest['root_page_count'], 17)

class ConsolidatedAudio(unittest.TestCase):
    def test_audio_is_complete_single_article_with_eight_providers(self):
        source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
        original = source.get('sounds.ambience', source.get('reference.audio'))
        manifest = json.loads((ROOT / 'docs/handbook-draft-manifest.json').read_text())
        audio = next(row for row in manifest['pages'] if row['filename'] == 'reference.audio.md')
        self.assertEqual(audio['page_type'], 'article')
        self.assertEqual(len(audio['metadata_paths']), 8)
        for locale, language in (('', 'en_us'), ('_zh_cn', 'zh_cn')):
            base = PAGES / locale
            text = (base / 'reference.audio.md').read_text()
            self.assertIn(original[language].strip(), text)
            self.assertIn('](vehicles.assembly.md)', text)
            self.assertEqual(text.count('## 相关模组' if locale else '## Related mods'), 1)
            self.assertNotIn('  parent:', text)
            for obsolete in ('sounds.ambience.md', 'audio.sound.md'):
                self.assertFalse((base / obsolete).exists())

if __name__ == '__main__':
    unittest.main()
