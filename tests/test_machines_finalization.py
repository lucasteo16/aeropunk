"""Regressions for the scoped Machines review and historical restoration."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import subprocess
import unittest

from urllib.parse import urlsplit, parse_qs
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tests'))
from handbook_revision_contract import before_machines_finalization, before_transport_finalization, topic_digest

class MachinesFinalization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.live=json.loads((ROOT/'docs/handbook-content.json').read_text())
        cls.current=before_transport_finalization(cls.live)
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
            self.assertIn(f'<EmiSearch query="{query}" />',text)
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
            for token in ('create_sa:brass_drill_head','key.create_sa.increase_reach','key.create_sa.decrease_reach'):
                self.assertIn(token,text)
            processing=self.current['machines.ore-processing'][locale]
            for token in ('stam1ocreatetweaks:blasting/blue_dye','minecraft:feather','minecraft:prismarine_shard'):
                self.assertIn(token,processing)
                self.assertNotIn(token,text)
            self.assertNotIn('<EmiSearch query="@minecraft">', text)
            for query in queries:
                self.assertIn(f'<EmiSearch query="{query}" />', processing)
            self.assertNotIn('selected procedure',text)
            self.assertNotIn('source excerpt',text)

    def test_progression_order_and_vent_illustration(self):
        sys.path.insert(0,str(ROOT/'scripts'))
        from handbook_navigation import CHILD_ORDER
        order=CHILD_ORDER['reference.machines-storage']
        self.assertEqual(order[:3],('storage.portable','storage.handling','storage.bulk'))
        self.assertLess(order.index('machines.rotation'),order.index('machines.ore-processing'))
        for locale in ('en_us','zh_cn'):
            self.assertIn('images/molten-vent-dormant.png',self.current['machines.renewables'][locale])

    def test_tutorial_links_have_short_labels_and_safe_destinations(self):
        import re
        total=0
        for topic in self.contract['topics']:
            for locale,body in self.current[topic].items():
                for line in body.splitlines():
                    if 'youtube.com/results?' in line:
                        self.assertTrue(line.startswith(('![YouTube](images/tutorial-video.png) ',
                                                         '![Tutorial](images/tutorial-video.png) ')),(topic,locale))
                self.assertNotIn('</EmiSearch>',body,(topic,locale))
                for label,url in re.findall(r'\[([^\]]+)\]\((https://www\.youtube\.com/results\?[^)]+)\)',body):
                    self.assertIn(label,('English','中文'),(topic,locale,label))
                    self.assertTrue(url.isascii(),(topic,locale,url))
                    self.assertNotRegex(url,r'[\s()]')
                    query=parse_qs(urlsplit(url).query)
                    self.assertEqual(set(query),{'search_query'})
                    self.assertTrue(query['search_query'][0])
                    total+=1
        self.assertGreater(total,60)

    def test_landing_groups_match_the_native_sidebar(self):
        import re
        sys.path.insert(0,str(ROOT/'scripts'))
        from handbook_navigation import CHILD_ORDER
        expected=list(CHILD_ORDER['reference.machines-storage'])
        for locale in ('en_us','zh_cn'):
            landing=self.current['reference.machines-storage'][locale]
            directory=landing.split('## Machine systems' if locale=='en_us' else '## 机器系统')[0]
            observed=re.findall(r'\]\(([^)]+)\.md\)',directory)
            self.assertEqual(observed,expected,locale)
        for locale in ('en_us','zh_cn'):
            self.assertIn('blaze_burner',self.current['power.burners'][locale])
            self.assertNotIn('blasting/blue_dye',self.current['power.burners'][locale])

    def test_processing_provider_follows_its_moved_recipes(self):
        path='mods/create-stam1o-tweaks.pw.toml'
        manifest=json.loads((ROOT/'docs/handbook-draft-manifest.json').read_text())
        homes=[row['topic'] for row in manifest['pages'] if path in row['metadata_paths']]
        self.assertEqual(homes,['machines.ore-processing'])
        coverage=json.loads((ROOT/'docs/guide-coverage.json').read_text())
        row=next(row for row in coverage['inventory'] if row['metadata_path']==path)
        self.assertEqual(row['primary_home'],homes[0])
        self.assertEqual(row['primary_category'],'Automation and industry')

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
        transport=ROOT/'docs/transport-final-review.json'
        if transport.exists():
            revision=json.loads(transport.read_text())
            self.assertEqual(topic_digest(self.live),revision['source_sha256']['after'])
            source=subprocess.check_output(['git','show',revision['development_base']+':docs/handbook-content.json'],cwd=ROOT)
        else:
            source=(ROOT/'docs/handbook-content.json').read_bytes()
        digest=hashlib.sha256(source).hexdigest()
        self.assertEqual(self.contract['source_file_sha256'],digest)
        report=json.loads((ROOT/'docs/machines-storage-final-review.json').read_text())
        self.assertEqual(report['content_sha256'],digest)

    def test_generated_resources_match_the_reviewed_manifest(self):
        record=json.loads((ROOT/'docs/machines-storage-final-review.json').read_text())
        pack=ROOT/'resourcepacks/astropunk-guide-preview'
        resources={p.relative_to(pack).as_posix():p for p in pack.rglob('*') if p.is_file()}
        transport=ROOT/'docs/transport-final-review.json'
        changes={}
        if transport.exists():
            revision=json.loads(transport.read_text())
            self.assertEqual(set(resources),set(revision['resource_sha256']))
            changes=revision['resource_changes']
            for name,source in resources.items():
                self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),revision['resource_sha256'][name],name)
            for name in set(changes)&set(record['resource_sha256']):
                prior=subprocess.check_output(['git','show',revision['development_base']+':resourcepacks/astropunk-guide-preview/'+name],cwd=ROOT)
                self.assertEqual(hashlib.sha256(prior).hexdigest(),record['resource_sha256'][name],name)
            self.assertEqual(set(resources),set(record['resource_sha256'])|set(changes))
        else:
            self.assertEqual(set(resources),set(record['resource_sha256']))
        for name,source in resources.items():
            if name in changes:
                continue  # Exact Transport hashes and historical bytes checked above.
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),record['resource_sha256'][name],name)

if __name__=='__main__':unittest.main()
