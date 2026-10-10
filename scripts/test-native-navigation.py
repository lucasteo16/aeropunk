#!/usr/bin/env python3
"""Execute selected GuideME NavigationTree bytecode without launching Minecraft.

Only Minecraft item and resource boundaries, parsed input holders, Pair and logging
are stubbed. NavigationTree and NavigationNode come unchanged from the release jar.
Merge ordering matches verified MutableGuide.buildNavigation bytecode, not a claim
that a running client has consumed a resource reload.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ENGINE = Path(os.environ.get('GUIDEME_JAR', str(ROOT / 'scripts/handbook-access/guideme-21.1.19.jar')))
JAVA = Path(os.environ.get('JAVA_HOME', str(ROOT / 'scripts/handbook-access/toolchain/jdk-21.0.12.1+1'))) / 'bin'
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
STUBS = {
'net/minecraft/resources/ResourceLocation.java': '''package net.minecraft.resources; public record ResourceLocation(String id) { public String toString(){return id;} }''',
'net/minecraft/world/item/ItemStack.java': '''package net.minecraft.world.item; public class ItemStack {}''',
'guideme/compiler/ParsedGuidePage.java': '''package guideme.compiler; import net.minecraft.resources.ResourceLocation; public record ParsedGuidePage(ResourceLocation id, Frontmatter frontmatter) {public ResourceLocation getId(){return id;} public Frontmatter getFrontmatter(){return frontmatter;}}''',
'guideme/compiler/Frontmatter.java': '''package guideme.compiler; public record Frontmatter(FrontmatterNavigation navigationEntry) {}''',
'guideme/compiler/FrontmatterNavigation.java': '''package guideme.compiler; import net.minecraft.resources.ResourceLocation; public record FrontmatterNavigation(String title, ResourceLocation parent, int position) {}''',
'guideme/internal/util/NavigationUtil.java': '''package guideme.internal.util; import guideme.compiler.ParsedGuidePage; import net.minecraft.world.item.ItemStack; import java.util.function.Supplier; public class NavigationUtil { public record NavIcon(ItemStack icon, Supplier<ItemStack> iconFactory){} public static NavIcon createNavigationIcon(ParsedGuidePage p){return new NavIcon(null,null);} }''',
'org/apache/commons/lang3/tuple/Pair.java': '''package org.apache.commons.lang3.tuple; public record Pair<L,R>(L left,R right){public static <L,R> Pair<L,R> of(L l,R r){return new Pair<>(l,r);} public L getLeft(){return left;} public L getKey(){return left;} public R getRight(){return right;} }''',
'org/slf4j/Logger.java': '''package org.slf4j; public interface Logger {default void error(String s,Object a){System.err.println(s);} default void error(String s,Object a,Object b){System.err.println(s);} }''',
'org/slf4j/LoggerFactory.java': '''package org.slf4j; public class LoggerFactory {public static Logger getLogger(Class<?> c){return new Logger(){};}}''',
'NativeNavigationProbe.java': '''import java.nio.file.*; import java.util.*; import guideme.compiler.*; import guideme.navigation.*; import net.minecraft.resources.ResourceLocation;
public class NativeNavigationProbe {
 static ResourceLocation id(String s){return new ResourceLocation(s);}
 static Map<ResourceLocation,ParsedGuidePage> load(Path path)throws Exception {
  Map<ResourceLocation,ParsedGuidePage> result=new HashMap<>();
  for(String line:Files.readAllLines(path)){String[] x=line.split("\\t",-1); var p=new ParsedGuidePage(id(x[0]),new Frontmatter(new FrontmatterNavigation(x[1],x[2].isEmpty()?null:id(x[2]),Integer.parseInt(x[3]))));result.put(p.getId(),p);}return result;
 }
 static Set<String> roots(NavigationTree t){Set<String>s=new TreeSet<>();for(var n:t.getRootNodes())s.add(n.pageId().toString());return s;}
 static int walk(NavigationNode n,int depth,Set<String>seen){if(!seen.add(n.pageId().toString()))throw new AssertionError("Duplicate or cyclic node"); if(depth>2)throw new AssertionError("Unexpected fourth navigation level");int count=1; for(var c:n.children())count+=walk(c,depth+1,seen);return count;}
 public static void main(String[]args)throws Exception{
  var watched=load(Path.of(args[0]));var fallback=new HashMap<>(watched); var clean=NavigationTree.build(watched.values());
  if(!roots(clean).equals(Set.of("index.md","help.controls.md","help.search.md","adventure.bosses.md","adventure.creatures.md","adventure.structures.md","world.dimensions.md","reference.skills.md","reference.food.md","reference.building.md","reference.vehicles.md","reference.machines-storage.md","maps.personal.md","reference.utilities.md","reference.appearance.md","reference.audio.md","reference.technical.md","help.credits.md")))throw new AssertionError("Unexpected source roots "+roots(clean));
  var ordered=new ArrayList<String>();for(var n:clean.getRootNodes())ordered.add(n.pageId().toString());
  if(!ordered.equals(List.of("index.md","help.controls.md","help.search.md","adventure.bosses.md","adventure.creatures.md","adventure.structures.md","world.dimensions.md","reference.skills.md","reference.food.md","reference.building.md","reference.vehicles.md","reference.machines-storage.md","maps.personal.md","reference.utilities.md","reference.appearance.md","reference.audio.md","reference.technical.md","help.credits.md")))throw new AssertionError("Unexpected native root order "+ordered);
  var combat=clean.getNodeById(id("reference.skills.md"));var children=new HashSet<String>();for(var n:combat.children())children.add(n.pageId().toString());
  if(!children.containsAll(Set.of("reference.equipment.md","combat.abilities.md","equipment.weapons-armor.md","combat.magic.md")))throw new AssertionError("Combat siblings missing");
  if(clean.getNodeById(id("reference.equipment.md")).children().size()!=0)throw new AssertionError("Equipment inserted third level");
  int count=0;Set<String>seen=new HashSet<>();for(var n:clean.getRootNodes())count+=walk(n,0,seen);if(count!=watched.size())throw new AssertionError("Unreachable native pages");
  for(int i=0;i<10;i++){var p=new ParsedGuidePage(id("category-old-"+i+".md"),new Frontmatter(new FrontmatterNavigation("Old catalog "+i,null,0)));fallback.put(p.getId(),p);}
  // Released MutableGuide copies fallback and then putAll(developmentPages).
  var merged=new HashMap<>(fallback);merged.putAll(watched);
  if(roots(NavigationTree.build(merged.values())).size()!=28)throw new AssertionError("Negative stale fallback control failed");
  // Removing watched overrides does not tombstone the packaged resource.
  var oldId=id("category-old-0.md");var override=new ParsedGuidePage(oldId,new Frontmatter(new FrontmatterNavigation("Old",id("reference.utilities.md"),0)));watched.put(oldId,override);merged=new HashMap<>(fallback);merged.putAll(watched);
  if(roots(NavigationTree.build(merged.values())).size()!=27)throw new AssertionError("Watched precedence control failed");
  watched.remove(oldId);merged=new HashMap<>(fallback);merged.putAll(watched);
  if(roots(NavigationTree.build(merged.values())).size()!=28)throw new AssertionError("Deletion resurrection control failed");
  for(int i=0;i<10;i++)fallback.remove(id("category-old-"+i+".md"));merged=new HashMap<>(fallback);merged.putAll(watched);
  if(!roots(NavigationTree.build(merged.values())).equals(Set.of("index.md","help.controls.md","help.search.md","adventure.bosses.md","adventure.creatures.md","adventure.structures.md","world.dimensions.md","reference.skills.md","reference.food.md","reference.building.md","reference.vehicles.md","reference.machines-storage.md","maps.personal.md","reference.utilities.md","reference.appearance.md","reference.audio.md","reference.technical.md","help.credits.md")))throw new AssertionError("Fallback repair failed");
  var obsolete=new ParsedGuidePage(id("quick-reference.md"),new Frontmatter(new FrontmatterNavigation("Quick reference",null,0)));fallback.put(obsolete.getId(),obsolete);merged=new HashMap<>(fallback);merged.putAll(watched);
  if(!roots(NavigationTree.build(merged.values())).contains("quick-reference.md"))throw new AssertionError("Quick reference fallback resurrection control failed");
  fallback.remove(obsolete.getId());merged=new HashMap<>(fallback);merged.putAll(watched);
  if(!roots(NavigationTree.build(merged.values())).equals(Set.of("index.md","help.controls.md","help.search.md","adventure.bosses.md","adventure.creatures.md","adventure.structures.md","world.dimensions.md","reference.skills.md","reference.food.md","reference.building.md","reference.vehicles.md","reference.machines-storage.md","maps.personal.md","reference.utilities.md","reference.appearance.md","reference.audio.md","reference.technical.md","help.credits.md")))throw new AssertionError("Quick reference fallback reconciliation failed");
  if(!clean.getNodeById(id("reference.audio.md")).children().isEmpty())throw new AssertionError("Audio wrapper remains");
  var sound=new ParsedGuidePage(id("sounds.ambience.md"),new Frontmatter(new FrontmatterNavigation("Sound",id("reference.audio.md"),0)));fallback.put(sound.getId(),sound);merged=new HashMap<>(fallback);merged.putAll(watched);
  if(NavigationTree.build(merged.values()).getNodeById(id("reference.audio.md")).children().size()!=1)throw new AssertionError("Sound fallback resurrection control failed");
  fallback.remove(sound.getId());merged=new HashMap<>(fallback);merged.putAll(watched);
  if(!NavigationTree.build(merged.values()).getNodeById(id("reference.audio.md")).children().isEmpty())throw new AssertionError("Sound fallback reconciliation failed");
  System.out.println("PASS released NavigationTree, "+count+" nodes, eighteen ordered roots, direct Audio article, Combat siblings, depth, fallback merge, watched deletion, obsolete Quick reference and Sound resurrection and repair controls");
 }
}'''
}

def run():
    with tempfile.TemporaryDirectory(prefix='native-navigation-', dir=os.environ.get('TMPDIR', '/home/tsb/.hermes/cache/scratch')) as folder:
        base = Path(folder)
        sources = []
        for name, content in STUBS.items():
            path = base / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            sources.append(str(path))
        classes = base / 'classes'
        classes.mkdir()
        subprocess.run([str(JAVA / 'javac'), '-cp', str(ENGINE), '-d', str(classes), *sources], check=True)
        outputs = []
        for locale in ('', '_zh_cn'):
            rows = []
            for path in sorted((PAGES / locale).glob('*.md')):
                front = path.read_text().split('---', 2)[1]
                title = re.search(r'^  title: (.+)$', front, re.M)
                if not title:
                    continue
                parent = re.search(r'^  parent: (.+)$', front, re.M)
                position = re.search(r'^  position: (.+)$', front, re.M)
                rows.append('\t'.join((path.name, json.loads(title[1]), parent[1] if parent else '', position[1] if position else '0')))
            data = base / 'pages.tsv'
            data.write_text('\n'.join(rows) + '\n')
            result = subprocess.run([str(JAVA / 'java'), '-cp', str(classes) + ':' + str(ENGINE), 'NativeNavigationProbe', str(data)], check=True, capture_output=True, text=True)
            outputs.append({'locale': locale or 'en_us', 'output': result.stdout.strip()})
        with zipfile.ZipFile(ENGINE) as archive:
            digest = hashlib.sha256(archive.read('guideme/navigation/NavigationTree.class')).hexdigest()
        print(json.dumps({'engine': '21.1.19', 'navigation_class_sha256': digest, 'tests': outputs, 'minecraft_boundaries_stubbed': True, 'rendered_verified': False}, indent=2))

if __name__ == '__main__':
    run()
