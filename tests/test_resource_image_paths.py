from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'resourcepacks/astropunk-guide-preview/assets'


class ResourceImagePaths(unittest.TestCase):
    def test_image_files_use_valid_minecraft_resource_paths(self):
        invalid = [str(p.relative_to(ASSETS)) for p in ASSETS.rglob('*')
                   if p.is_file() and p.suffix.lower() in ('.png', '.jpg', '.jpeg')
                   and re.fullmatch(r'[a-z0-9_./-]+', str(p.relative_to(ASSETS))) is None]
        self.assertEqual(invalid, [])

    def test_markdown_images_resolve_to_valid_paths(self):
        for page in ASSETS.rglob('*.md'):
            for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', page.read_text()):
                if target.startswith(('https:', 'http:')):
                    continue
                self.assertRegex(target, r'^[a-z0-9_./-]+$')
                base = page.parent.parent if page.parent.name == '_zh_cn' else page.parent
                self.assertTrue((base / target).is_file(), (page, target))


if __name__ == '__main__':
    unittest.main()
