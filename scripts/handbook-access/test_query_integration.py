#!/usr/bin/env python3
"""Selected public descriptors, compiled endpoint and native extension execution.

The compiler probe uses one test-only audio boundary rather than initializing
GuideMEClient's entire loader-dependent static initializer. No window is opened.
"""
from pathlib import Path
import subprocess
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent
JAVA = ROOT / 'toolchain/jdk-21.0.12.1+1/bin'
OUTPUT = ROOT / 'build/query-integration'


def bytecode(archive, *classes):
    return subprocess.check_output([str(JAVA / 'javap'), '-classpath', str(archive), '-p', '-c', '-s', '-v', *classes], text=True)


class QueryIntegrationTest(unittest.TestCase):
    def test_compiled_native_extension_exists(self):
        self.assertTrue((ROOT / 'build/classes/java/main/dev/astropunk/handbook/EmiSearchTagCompiler.class').is_file(), 'Missing compiled native query extension')

    def test_released_public_endpoints_and_screen_before_search(self):
        released = bytecode(ROOT / 'emi-1.1.24.jar', 'dev.emi.emi.api.EmiApi')
        self.assertIn('public static void setSearchText(java.lang.String);', released)
        setter = released.split('public static void setSearchText(java.lang.String);')[1].split('public static boolean isSearchFocused')[0]
        self.assertNotIn('Minecraft.setScreen', setter, 'Reassess need for custom screen if selected setter opens one')
        present = bytecode(ROOT / 'build/classes/java/main', 'dev.astropunk.handbook.EmiQueryClient$Present')
        self.assertLess(present.index('Minecraft.setScreen:'), present.index('EmiApi.setSearchText:'))
        close = bytecode(ROOT / 'build/classes/java/main', 'dev.astropunk.handbook.EmiQueryClient$QueryInventoryScreen')
        self.assertIn('extends net.minecraft.client.gui.screens.inventory.AbstractContainerScreen<net.minecraft.world.inventory.InventoryMenu>', close)
        self.assertIn('public void onClose();', close)
        self.assertIn('returnScreen:Lnet/minecraft/client/gui/screens/Screen;', close)
        self.assertIn('Minecraft.setScreen:', close)
        outer = bytecode(ROOT / 'build/classes/java/main', 'dev.astropunk.handbook.EmiQueryClient')
        self.assertLess(outer.index('ModList.isLoaded:'), outer.index('EmiQueryClient$Present.open:'))
        self.assertNotIn('dev/emi/emi/api/EmiApi', outer)

    def test_actual_compiler_registration_with_optional_emi_absent(self):
        OUTPUT.mkdir(parents=True, exist_ok=True)
        classes = OUTPUT / 'classes'
        audio = OUTPUT / 'audio-boundary'
        classes.mkdir(exist_ok=True)
        audio.mkdir(exist_ok=True)
        cp = (ROOT / 'build/access-probe-classpath.txt').read_text() + ':' + str(ROOT / 'build/classes/java/main')
        for target, source in [(audio, 'query-validation/audio-boundary/guideme/internal/GuideMEClient.java'),
                               (classes, 'query-validation/VerifyEmiSearch.java')]:
            subprocess.run([str(JAVA / 'javac'), '-proc:none', '-cp', cp, '-d', str(target), str(ROOT / source)], check=True)
        for mode in ('present', 'absent'):
            runtime = cp if mode == 'present' else ':'.join(p for p in cp.split(':') if Path(p).name != 'emi-1.1.24.jar')
            command = [str(JAVA / 'java'), '-cp', str(audio) + ':' + str(classes) + ':' + runtime, 'dev.astropunk.handbook.VerifyEmiSearch']
            result = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (OUTPUT / ('native-' + mode + '.log')).write_text(result.stdout)
            print(result.stdout)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn('PASS same-id data-driven override negative control and restoration', result.stdout)

    def test_selected_mod_search_bakes_display_name_and_namespace(self):
        released = bytecode(ROOT / 'emi-1.1.24.jar', 'dev.emi.emi.search.EmiSearch')
        bake = released.split('public static void bake();')[1].split('public static void update();')[0]
        # Exact released bytecode adds both names to the SAME mods suffix index.
        start = bake.index('EmiStack.getId:')
        section = bake[start:bake.index('EmiStack.getItemStack:', start)]
        self.assertIn('EmiUtil.getModName:', section)
        self.assertEqual(section.count('ResourceLocation.getNamespace:'), 2)
        self.assertEqual(section.count('SuffixArray.add:'), 3)  # display name, namespace, item path in names index
        mod = bytecode(ROOT / 'emi-1.1.24.jar', 'dev.emi.emi.search.ModQuery')
        self.assertIn('EmiSearch.mods:', mod)
        self.assertIn('SuffixArray.search:', mod)
        OUTPUT.mkdir(parents=True, exist_ok=True)
        (OUTPUT / 'selected-mod-search-bytecode.log').write_text(released + '\n' + mod)
        cp = (ROOT / 'build/access-probe-classpath.txt').read_text()
        classes = OUTPUT / 'mod-query-classes'
        classes.mkdir(exist_ok=True)
        subprocess.run([str(JAVA / 'javac'), '-proc:none', '-cp', cp, '-d', str(classes), str(ROOT / 'query-validation/VerifyEmiModQuery.java')], check=True)
        boundary = OUTPUT / 'index-boundary'
        boundary.mkdir(exist_ok=True)
        subprocess.run([str(JAVA / 'javac'), '-proc:none', '-cp', cp, '-d', str(boundary), str(ROOT / 'query-validation/index-boundary/dev/emi/emi/search/EmiSearch.java')], check=True)
        result = subprocess.run([str(JAVA / 'java'), '-cp', str(boundary) + ':' + str(classes) + ':' + cp, 'dev.astropunk.handbook.VerifyEmiModQuery'], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (OUTPUT / 'native-mod-query.log').write_text(result.stdout)
        self.assertEqual(result.returncode, 0, result.stdout)
        print(result.stdout)

    def test_registration_is_wired_and_test_boundary_not_shipped(self):
        jar = ROOT / 'build/libs/astropunk-handbook-access-1.0.0.jar'
        client = bytecode(jar, 'dev.astropunk.handbook.HandbookAccess')
        self.assertIn('FMLClientSetupEvent', client)
        self.assertIn('HandbookQueryGuide.register:', client)
        self.assertIn('FMLClientSetupEvent.enqueueWork:', client)
        released = bytecode(ROOT / 'guideme-21.1.19.jar', 'guideme.GuideBuilder', 'guideme.document.flow.LytFlowLink')
        self.assertIn('public <T extends guideme.extensions.Extension> guideme.GuideBuilder extension', released)
        self.assertIn('public void setClickCallback(java.util.function.Consumer<guideme.ui.GuideUiHost>);', released)
        with zipfile.ZipFile(jar) as archive:
            self.assertFalse(any(n.startswith(('guideme/', 'dev/emi/')) for n in archive.namelist()))


if __name__ == '__main__':
    unittest.main()
