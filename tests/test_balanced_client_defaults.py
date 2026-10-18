import json
from pathlib import Path
import subprocess
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'configureddefaults/config'


class BalancedClientDefaultsTests(unittest.TestCase):
    def test_only_approved_sound_physics_overrides(self):
        settings = dict(line.split('=', 1) for line in
                        (CONFIG / 'sound_physics_remastered/soundphysics.properties').read_text().splitlines()
                        if line and not line.startswith('#'))
        self.assertEqual(settings, {
            'environment_evaluation_ray_count': '24',
            'max_sound_processing_distance': '384.0',
        })
        self.assertGreaterEqual(int(settings['environment_evaluation_ray_count']), 8)
        self.assertLessEqual(int(settings['environment_evaluation_ray_count']), 64)
        self.assertFalse((CONFIG / 'sound_physics_remastered/sound_rates.properties').exists())

    def test_only_approved_json_overrides(self):
        self.assertEqual(json.loads((CONFIG / 'presencefootsteps/userconfig.json').read_text()),
                         {'maxSteppingEntities': 32})
        previous = json.loads(subprocess.check_output(
            ['git', 'show', 'e9125b5:config/entity_texture_features.json'], cwd=ROOT, text=True))
        previous['textureUpdateFrequency_V2'] = 'Average'
        self.assertEqual(json.loads((CONFIG / 'entity_texture_features.json').read_text()), previous)

    def test_no_competing_active_config_overrides(self):
        for path in ('sound_physics_remastered/soundphysics.properties',
                     'presencefootsteps/userconfig.json', 'entity_texture_features.json'):
            self.assertFalse((ROOT / 'config' / path).exists(), path)

    def test_all_affected_mods_and_compatibility_addons_remain_selected(self):
        light = tomllib.loads((ROOT / 'pack.toml').read_text())['version'].endswith('-light')
        for slug in ('sound-physics-remastered', 'cool-rain-reforged', 'sable-cool-rain',
                     'pf-neoforge', 'presence-footsteps-x-sable', 'entity-model-features',
                     'entitytexturefeatures', 'emf-compat-core', 'create-emf-compat-skyhook'):
            self.assertEqual((ROOT / 'mods' / (slug + '.pw.toml')).is_file(), not light, slug)


if __name__ == '__main__':
    unittest.main()
