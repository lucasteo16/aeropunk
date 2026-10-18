import json
from pathlib import Path
import subprocess
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
REMOVED = {
    'mods/sound-physics-remastered.pw.toml',
    'mods/cool-rain-reforged.pw.toml',
    'mods/sable-cool-rain.pw.toml',
    'mods/pf-neoforge.pw.toml',
    'mods/presence-footsteps-x-sable.pw.toml',
    'mods/entity-model-features.pw.toml',
    'mods/entitytexturefeatures.pw.toml',
    'mods/create-emf-compat-skyhook.pw.toml',
    'mods/emf-compat-core.pw.toml',
}


class LightEditionTests(unittest.TestCase):
    def test_exact_main_baseline_minus_approved_client_mods(self):
        spec = json.loads((ROOT / 'docs/light-edition.json').read_text())
        self.assertEqual(set(spec['removed_metadata']), REMOVED)
        baseline = spec['baseline_commit']
        subprocess.run(['git', 'merge-base', '--is-ancestor', baseline, 'HEAD'],
                       cwd=ROOT, check=True)
        paths = subprocess.check_output(
            ['git', 'ls-tree', '-r', '--name-only', baseline,
             'mods', 'resourcepacks', 'shaderpacks'], cwd=ROOT, text=True).splitlines()
        expected = {path for path in paths if path.endswith('.pw.toml')}
        actual = {path.relative_to(ROOT).as_posix()
                  for folder in ('mods', 'resourcepacks', 'shaderpacks')
                  for path in (ROOT / folder).glob('*.pw.toml')}
        self.assertEqual(actual, expected - REMOVED)
        for path in actual:
            self.assertEqual((ROOT / path).read_bytes(), subprocess.check_output(
                ['git', 'show', baseline + ':' + path], cwd=ROOT), path)
        for path in REMOVED:
            original = tomllib.loads(subprocess.check_output(
                ['git', 'show', baseline + ':' + path], cwd=ROOT, text=True))
            self.assertEqual(original['side'], 'client', path)
        pack = tomllib.loads((ROOT / 'pack.toml').read_text())
        original_pack = tomllib.loads(subprocess.check_output(
            ['git', 'show', baseline + ':pack.toml'], cwd=ROOT, text=True))
        self.assertEqual(pack['name'], 'Astropunk')
        self.assertEqual(pack['versions'], original_pack['versions'])
        self.assertEqual(pack['version'], original_pack['version'] + '-light')

    def test_all_remaining_game_overrides_match_main_baseline(self):
        spec = json.loads((ROOT / 'docs/light-edition.json').read_text())
        baseline_index = tomllib.loads(subprocess.check_output(
            ['git', 'show', spec['baseline_commit'] + ':index.toml'],
            cwd=ROOT, text=True))
        index = tomllib.loads((ROOT / 'index.toml').read_text())
        old = {entry['file']: entry for entry in baseline_index['files']}
        new = {entry['file']: entry for entry in index['files']}
        self.assertEqual(set(new), set(old) - REMOVED)
        for path in new:
            self.assertEqual(new[path], old[path], path)


if __name__ == '__main__':
    unittest.main()
