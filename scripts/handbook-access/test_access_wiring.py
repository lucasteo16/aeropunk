#!/usr/bin/env python3
"""Artifact wiring contracts, not gameplay reproduction.

Set ACCESS_HELPER_JAR to inspect a different archive. The negative control
compiles a helper with the inventory listener disconnected in build output.
It never changes main sources, the packaged helper or a launcher profile.
"""
from pathlib import Path
import os
import re
import subprocess
import sys
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent
JAVA = ROOT / 'toolchain/jdk-21.0.12.1+1/bin'
HELPER = Path(os.environ.get('ACCESS_HELPER_JAR', ROOT / 'build/libs/astropunk-handbook-access-1.0.0.jar'))


def bytecode(archive, name):
    return subprocess.check_output([str(JAVA / 'javap'), '-classpath', str(archive), '-p', '-c', '-v', name], text=True)


def method(code, name):
    start = re.search(r'^  (?:public|private).*\b' + re.escape(name) + r'\(', code, re.M)
    if start is None:
        raise AssertionError('Missing method ' + name)
    end = re.search(r'^  (?:public|private|static).*', code[start.end():], re.M)
    return code[start.start(): start.end() + end.start() if end else len(code)]


class AccessWiringTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code = bytecode(HELPER, 'dev.astropunk.handbook.HandbookAccess')

    def test_client_loader_entry_matches_manifest(self):
        self.assertIn('value="astropunk_handbook_access"', self.code)
        self.assertIn('dist=[Lnet/neoforged/api/distmarker/Dist;.CLIENT]', self.code)
        self.assertIn('public dev.astropunk.handbook.HandbookAccess(net.neoforged.bus.api.IEventBus)', self.code)
        with zipfile.ZipFile(HELPER) as archive:
            self.assertIn('modId="astropunk_handbook_access"', archive.read('META-INF/neoforge.mods.toml').decode())

    def test_constructor_connects_each_typed_event_to_correct_bus(self):
        constructor = method(self.code, 'dev.astropunk.handbook.HandbookAccess')
        # Key mappings use the injected mod bus. Guide registration is synchronous.
        # The four screen and tick listeners use NeoForge.EVENT_BUS.
        self.assertEqual(constructor.count('IEventBus.addListener:'), 5)
        self.assertNotIn('FMLClientSetupEvent', constructor)
        self.assertEqual(constructor.count('NeoForge.EVENT_BUS:'), 4)
        for name, event in [
            ('registerKeys', 'RegisterKeyMappingsEvent'),
            ('addInventoryButton', 'ScreenEvent$Init$Post'),
            ('onInventoryRender', 'ScreenEvent$Render$Pre'),
            ('onClientTick', 'ClientTickEvent$Post'),
            ('onInventoryKey', 'ScreenEvent$KeyPressed$Post'),
        ]:
            self.assertIn('HandbookAccess.' + name + ':(Lnet/neoforged/neoforge/client/event/' + event + ';)V', self.code)

    def test_guide_is_registered_before_initial_reload_can_start(self):
        constructor = method(self.code, 'dev.astropunk.handbook.HandbookAccess')
        self.assertIn('HandbookQueryGuide.register:', constructor)
        self.assertLess(constructor.index('HandbookQueryGuide.register:'), constructor.index('IEventBus.addListener:'))
        self.assertNotIn('FMLClientSetupEvent', constructor)

    def test_inventory_widget_is_added_as_renderable_listener(self):
        self.assertIn('ScreenEvent$Init$Post.addListener:', self.code)
        self.assertIn('Button$Builder.build:', self.code)
        inventory = method(self.code, 'addInventoryButton')
        self.assertIn('inventory/InventoryScreen', inventory)
        self.assertIn('inventory/CreativeModeInventoryScreen', inventory)
        placement = method(self.code, 'updateInventoryButton')
        self.assertIn('ButtonPlacement.findGuide:', placement)
        self.assertIn('EmiSearchPlacement.collect:', placement)
        self.assertLess(placement.index('ModList.isLoaded:'), placement.index('EmiSearchPlacement.collect:'))
        self.assertIn('updateInventoryButton:', method(self.code, 'onInventoryRender'))
        self.assertNotIn('ButtonPlacement.findInventory:', self.code)
        self.assertNotIn('dev/emi/emi/screen/EmiScreenManager', self.code)
        classpath = (ROOT / 'build/access-probe-classpath.txt').read_text()
        screen = bytecode(classpath, 'net.minecraft.client.gui.screens.Screen')
        callback = method(screen, 'addEventWidget')
        self.assertIn('Field renderables:', callback)
        self.assertIn('Field children:', callback)
        self.assertIn('Field narratables:', callback)

    def test_selected_emi_search_bounds_are_read_not_recreated(self):
        released = bytecode(ROOT / 'emi-1.1.24.jar', 'dev.emi.emi.screen.EmiScreenManager')
        self.assertIn('public static dev.emi.emi.screen.widget.EmiSearchWidget search;', released)
        layout = method(released, 'addWidgets')
        self.assertIn('EmiSearchWidget.x:I', layout)
        self.assertIn('EmiSearchWidget.y:I', layout)
        self.assertIn('EmiSearchWidget.setWidth:', layout)
        self.assertIn('EmiSearchWidget.setVisible:', layout)
        adapter = bytecode(HELPER, 'dev.astropunk.handbook.EmiSearchPlacement')
        self.assertIn('EmiScreenManager.search:', adapter)
        for name in ('getX', 'getY', 'getWidth', 'getHeight'):
            self.assertIn('AbstractWidget.' + name + ':', adapter)
        self.assertNotIn('EmiSearchWidget."<init>"', adapter)
        self.assertNotIn('EmiScreenManager.addWidgets:', adapter)
        self.assertNotIn('java/lang/reflect', adapter)
        api = bytecode(ROOT / 'emi-1.1.24.jar', 'dev.emi.emi.api.EmiApi')
        self.assertNotIn('getSearchBounds(', api)

    def test_shortcut_world_and_inventory_dispatch_are_present(self):
        tick = method(self.code, 'onClientTick')
        self.assertIn('KeyMapping.consumeClick:', tick)
        self.assertIn('Minecraft.screen:', tick)
        self.assertIn('openHandbook:', tick)
        key = method(self.code, 'onInventoryKey')
        self.assertIn('KeyMapping.isActiveAndMatches:', key)
        self.assertIn('openHandbook:', key)

    def test_compiled_shortcut_is_comma_and_registered_independently_of_button(self):
        constructor = method(self.code, 'dev.astropunk.handbook.HandbookAccess')
        self.assertRegex(constructor, r'bipush\s+44\b', 'Whole handbook default must be GLFW comma')
        self.assertNotRegex(constructor, r'bipush\s+46\b', 'Period belongs to shader toggle, not handbook')
        self.assertIn('KeyConflictContext.UNIVERSAL:', constructor)
        registration = method(self.code, 'registerKeys')
        self.assertIn('Field shortcut:', registration)
        self.assertIn('RegisterKeyMappingsEvent.register:', registration)
        self.assertNotIn('Field buttons:', registration)
        for name in ('onClientTick', 'onInventoryKey', 'openHandbook'):
            handler = method(self.code, name)
            self.assertNotIn('Button.visible:', handler)
            self.assertNotIn('Button.active:', handler)
            self.assertNotIn('Field buttons:', handler)
        inventory = method(self.code, 'onInventoryKey')
        self.assertIn('ScreenEvent$KeyPressed$Post.setCanceled:', inventory)
        self.assertIn('inventory/InventoryScreen', inventory)
        self.assertIn('inventory/CreativeModeInventoryScreen', inventory)

    def test_handbook_controls_have_distinct_localized_category_and_action(self):
        import json
        with zipfile.ZipFile(HELPER) as archive:
            for locale, word in [('en_us', 'Handbook'), ('zh_cn', '手册')]:
                strings = json.loads(archive.read(f'assets/astropunk_handbook_access/lang/{locale}.json'))
                for key in ('key.categories.astropunk_handbook_access', 'key.astropunk_handbook_access.open'):
                    self.assertIn(word, strings[key])
                    self.assertIn('Astropunk', strings[key])
                    self.assertIn(key, self.code)

    def test_native_guideme_key_is_contextual_item_help_not_whole_handbook(self):
        native = bytecode(ROOT / 'guideme-21.1.19.jar', 'guideme.internal.hotkey.OpenGuideHotkey')
        self.assertIn('key.guideme.guide', native)
        self.assertIn('key.guideme.category', native)
        self.assertIn('ItemStack', native)
        self.assertIn('PageAnchor', native)

    def test_selected_engine_polls_watcher_and_reloads_visible_page(self):
        engine = ROOT / 'guideme-21.1.19.jar'
        client = bytecode(engine, 'guideme.internal.GuideMEClient')
        mutable = bytecode(engine, 'guideme.internal.MutableGuide')
        self.assertIn('ClientTickEvent$Pre', client)
        self.assertTrue('guideme/internal/MutableGuide.tick:' in client, 'Selected client must tick MutableGuide')
        self.assertIn('GuideSourceWatcher.takeChanges:', method(mutable, 'tick'))
        self.assertIn('GuideScreen.reloadPage:', method(mutable, 'applyChanges'))
        self.assertIn('GuideSourceWatcher.loadAll:', method(mutable, 'setPages'))


def negative_control():
    directory = ROOT / 'build/access-wiring-negative'
    directory.mkdir(parents=True, exist_ok=True)
    source = (ROOT / 'src/main/java/dev/astropunk/handbook/HandbookAccess.java').read_text()
    original = '        NeoForge.EVENT_BUS.addListener(this::addInventoryButton);'
    assert source.count(original) == 1
    probe = directory / 'HandbookAccess.java'
    probe.write_text(source.replace(original, '        // Negative control: inventory event intentionally disconnected.'))
    classpath = (ROOT / 'build/access-probe-classpath.txt').read_text()
    classpath += ':' + str(ROOT / 'build/classes/java/main')
    subprocess.run([str(JAVA / 'javac'), '-proc:none', '-cp', classpath, '-d', str(directory), str(probe)], check=True)
    jar = directory / 'disconnected-helper.jar'
    name = 'dev/astropunk/handbook/HandbookAccess.class'
    with zipfile.ZipFile(HELPER) as old, zipfile.ZipFile(jar, 'w') as new:
        for entry in old.infolist():
            new.writestr(entry, (directory / name).read_bytes() if entry.filename == name else old.read(entry.filename))
    env = dict(os.environ, ACCESS_HELPER_JAR=str(jar))
    result = subprocess.run([sys.executable, __file__, 'AccessWiringTest.test_constructor_connects_each_typed_event_to_correct_bus'], env=env, text=True, capture_output=True)
    print(result.stdout + result.stderr)
    assert result.returncode != 0 and '4 != 5' in result.stderr, 'Expected disconnected-listener assertion to fail'
    print('Negative control rejected disconnected inventory listener.')


if __name__ == '__main__':
    if '--negative-control' in sys.argv:
        negative_control()
    else:
        unittest.main(verbosity=2)
