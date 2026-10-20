"""Regressions for the screenshots in the first Transport feedback round."""
import json
from pathlib import Path
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]


class TransportFeedback(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content=json.loads((ROOT/'docs/handbook-content.json').read_text())
        cls.review=json.loads((ROOT/'docs/transport-final-review.json').read_text())

    def test_no_expanding_item_grids_inside_transport_tables(self):
        for topic in self.review['topics']:
            for locale,body in self.content[topic].items():
                for line in body.splitlines():
                    if line.startswith('|'):
                        self.assertNotIn('<ItemGrid>',line,(topic,locale))

    def test_bad_item_references_are_replaced_not_redistributed(self):
        for topic in self.review['topics']:
            for locale,body in self.content[topic].items():
                for invalid in ('create_submarine:rudder','rocketnautics:fluid_hose','aeronautics:levitite_blend"'):
                    self.assertNotIn(invalid,body,(topic,locale))
        for locale in ('en_us','zh_cn'):
            self.assertIn('create_high_seas:rudder',self.content['vehicles.water'][locale])
            self.assertIn('aeronautics:levitite_blend_bucket',self.content['vehicles.airships'][locale])
            self.assertNotIn('minecraft:obsidian',self.content['travel.destinations'][locale])

    def test_height_image_is_localized_and_old_combined_image_not_used(self):
        for locale in ('en_us','zh_cn'):
            body=self.content['space.vehicle-transfer'][locale]
            self.assertIn('transport-space-transfer-'+locale+'.png',body)
            self.assertNotIn('(images/transport-space-transfer.png)',body)

    def test_waystone_mechanical_recipes_are_shown(self):
        for locale in ('en_us','zh_cn'):
            body=self.content['travel.destinations'][locale]
            self.assertIn('create:mechanical_crafter',body)
            self.assertIn('waystones:warp_stone',body)
            self.assertIn('waystones:waystone',body)
            self.assertNotIn('<ItemImage ',body)
            self.assertNotIn('<Recipe id="waystones:waystone"',body)

    def test_unsupported_mechanical_recipes_are_explained_in_text(self):
        for locale in ('en_us','zh_cn'):
            body=self.content['travel.destinations'][locale]
            self.assertIn('cannot be displayed in this handbook' if locale=='en_us' else '不支持显示这些动力合成配方',body)
            self.assertNotIn('| 1 | 2 | 3 | 4 | 5 |',body)

    def test_internal_simulated_blocks_are_not_item_references(self):
        for locale in ('en_us','zh_cn'):
            body=self.content['vehicles.assembly'][locale]
            self.assertNotIn('simulated:paired_docking_connector',body)
            self.assertNotIn('simulated:merging_glue',body)
            self.assertIn('simulated:docking_connector',body)
            self.assertIn('minecraft:slime_ball',body)


if __name__=='__main__':unittest.main()
