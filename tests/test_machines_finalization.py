"""Regressions for the scoped Machines review and historical restoration."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import unittest
import zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tests'))
from handbook_revision_contract import before_machines_finalization, topic_digest

class MachinesFinalization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current=json.loads((ROOT/'docs/handbook-content.json').read_text())
        cls.contract=json.loads((ROOT/'docs/machines-storage-revision-contract.json').read_text())

    def test_exact_source_contract_and_scope(self):
        self.assertEqual(topic_digest(self.current),self.contract['source_sha256']['after'])
        self.assertEqual(len(self.contract['topics']),15)
        self.assertEqual(len(before_machines_finalization(self.current)),len(self.current))

    def test_negative_controls_reject_changed_owned_and_unrelated_prose(self):
        for topic in ('machines.ore-processing','food.utensils','machines.rotation'):
            altered=copy.deepcopy(self.current)
            altered[topic]['en_us']+='\nUnapproved change.'
            with self.assertRaises(AssertionError):before_machines_finalization(altered)

    def test_negative_controls_reject_retired_resurrection_and_missing_topics(self):
        for mutate in (lambda c:c.update({'fishing.habitats':{'en_us':'retired','zh_cn':'retired'}}),lambda c:c.pop('machines.trading')):
            altered=copy.deepcopy(self.current);mutate(altered)
            with self.assertRaises(AssertionError):before_machines_finalization(altered)

    def test_processing_has_real_browser_action_not_broken_recipe_or_recipe_item(self):
        for locale, query in (('en_us', 'Wheat Flour'), ('zh_cn', '小麦面粉')):
            text=self.current['machines.ore-processing'][locale]
            self.assertIn(f'<EmiSearch query="{query}">',text)
            self.assertNotIn('<EmiSearch query="@create">Open Create recipes</EmiSearch>',text)
            self.assertNotIn('<Recipe id="create:milling/wheat"',text)
            self.assertNotIn('<ItemLink id="create:milling/wheat"',text)
            self.assertIn('two extra flour' if locale=='en_us' else '额外产出两份面粉',text)

    def test_workshop_has_exact_recipe_and_actual_drone_controls(self):
        searches = {
            'en_us': ('Phantom Membrane', 'Brown Mushroom Block', 'Red Mushroom Block'),
            'zh_cn': ('幻翼膜', '棕色蘑菇方块', '红色蘑菇方块'),
        }
        for locale, queries in searches.items():
            text=self.current['machines.miscellaneous'][locale]
            for token in ('stam1ocreatetweaks:blasting/blue_dye','create_sa:brass_drill_head','key.create_sa.increase_reach','key.create_sa.decrease_reach','minecraft:feather','minecraft:prismarine_shard'):
                self.assertIn(token,text)
            self.assertNotIn('<EmiSearch query="@minecraft">', text)
            for query in queries:
                self.assertIn(f'<EmiSearch query="{query}">', text)
            self.assertNotIn('selected procedure',text)
            self.assertNotIn('source excerpt',text)

    def test_progression_order_and_vent_illustration(self):
        sys.path.insert(0,str(ROOT/'scripts'))
        from handbook_navigation import CHILD_ORDER
        order=CHILD_ORDER['reference.machines-storage']
        self.assertLess(order.index('machines.rotation'),order.index('storage.bulk'))
        self.assertLess(order.index('machines.rotation'),order.index('machines.ore-processing'))
        for locale in ('en_us','zh_cn'):
            self.assertIn('images/molten-vent-dormant.png',self.current['machines.renewables'][locale])

    def test_independent_review_corrections_remain_closed(self):
        for locale in ('en_us', 'zh_cn'):
            industry = self.current['power.industry'][locale]
            self.assertIn('tfmg:empty_spool', industry)
            self.assertNotIn('tfmg:spool"', industry)
            self.assertNotIn('tfmg:engine_controller', industry)
            enchanting = self.current['machines.enchanting'][locale]
            self.assertIn('Place the second Mechanical Grindstone on top' if locale == 'en_us' else '上方放置第二个机械磨石', enchanting)
            self.assertIn('Hold the equipment type' if locale == 'en_us' else '手持要用作筛选依据的装备', enchanting)

    def test_final_handoff_records_bind_the_same_source_file(self):
        digest=hashlib.sha256((ROOT/'docs/handbook-content.json').read_bytes()).hexdigest()
        self.assertEqual(self.contract['source_file_sha256'],digest)
        records=(('final-review-closure.json','content_sha256'),
                 ('final-verification/chapter-report.json','final_content_sha256'),
                 ('final-package-report.json','content_sha256'))
        for filename,key in records:
            report=json.loads((ROOT/'build/machines-final'/filename).read_text())
            self.assertEqual(report[key],digest,filename)

    def test_review_archive_contains_exact_current_resource_bytes(self):
        record=json.loads((ROOT/'build/machines-final/final-package-report.json').read_text())
        path=Path(record['archive'])
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),record['sha256'])
        pack=ROOT/'resourcepacks/astropunk-guide-preview'
        resources={p.relative_to(pack).as_posix():p for p in pack.rglob('*') if p.is_file()}
        self.assertEqual(len(resources),record['resource_members_verified'])
        with zipfile.ZipFile(path) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()),set(resources)|{'MACHINES-STORAGE-REVIEW.txt'})
            for name,source in resources.items():
                self.assertEqual(archive.read(name),source.read_bytes(),name)

if __name__=='__main__':unittest.main()
