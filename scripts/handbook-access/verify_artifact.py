#!/usr/bin/env python3
"""Inspect the real built archive and exact released dependency signatures."""
import re
import hashlib
import json
from pathlib import Path
import subprocess
import tomllib
import xml.etree.ElementTree as ET
import zipfile

root = Path(__file__).resolve().parent
jar = root / 'build/libs/astropunk-handbook-access-1.0.0.jar'
java_home = root / 'toolchain/jdk-21.0.12.1+1'

def javap(archive, *arguments):
    return subprocess.check_output([str(java_home / 'bin/javap'), '-classpath', str(archive), *arguments], text=True)

released = javap(root / 'guideme-21.1.19.jar', '-public', '-s', 'guideme.internal.GuideMEClient', 'guideme.Guides')
assert '(Lguideme/Guide;Lnet/minecraft/resources/ResourceLocation;)Z' in released
assert '(Lnet/minecraft/resources/ResourceLocation;)Lguideme/Guide;' in released
with zipfile.ZipFile(jar) as archive:
    names = archive.namelist()
    assert not any(name.startswith('guideme/') or 'guideme_guides/' in name or name.endswith('.md') for name in names)
    metadata = tomllib.loads(archive.read('META-INF/neoforge.mods.toml').decode())
    assert metadata['mods'][0]['modId'] == 'astropunk_handbook_access'
    dependencies = {entry['modId']: entry for entry in metadata['dependencies']['astropunk_handbook_access']}
    assert dependencies['guideme']['versionRange'] == '[21.1.19]'
    assert all(entry['side'] == 'CLIENT' for entry in dependencies.values())
    locales = [json.loads(archive.read(f'assets/astropunk_handbook_access/lang/{locale}.json')) for locale in ('en_us', 'zh_cn')]
    assert locales[0].keys() == locales[1].keys()
    assert all(all(value.strip() for value in locale.values()) for locale in locales)
    for name in names:
        if name.endswith('.class'):
            contents = archive.read(name)
            if b'GuideBuilder' in contents:
                assert name == 'dev/astropunk/handbook/HandbookQueryGuide.class', name
            for banned in (b'PacketDistributor', b'RegisterPayloadHandlersEvent', b'DeferredRegister', b'java/lang/reflect', b'sendCommand'):
                assert banned not in contents, (name, banned)

client = javap(jar, '-p', '-c', '-v', 'dev.astropunk.handbook.HandbookAccess')
assert 'dist=[Lnet/neoforged/api/distmarker/Dist;.CLIENT]' in client
assert 'guideme/internal/GuideMEClient.openGuideAtPreviousPage:(Lguideme/Guide;Lnet/minecraft/resources/ResourceLocation;)Z' in client
assert 'guideme/Guide.getStartPage:' in client
assert 'guideme/GuidesCommon.openGuide:' not in client
assert 'guideme/Guides.getById:' in client
assert 'astropunk' in client and 'handbook' in client
assert re.search(r'bipush\s+44', client), 'The compiled default must be GLFW comma'
assert 'com/mojang/blaze3d/platform/InputConstants.UNKNOWN' not in client
configure_position = client.index('LiveEditing.configure:')
listeners_position = client.index('IEventBus.addListener:')
assert configure_position < listeners_position

reports = [ET.parse(path).getroot() for path in (root / 'build/test-results/test').glob('TEST-*.xml')]
total = sum(int(report.attrib['tests']) for report in reports)
assert total == 15, total
assert any(case.attrib.get('name') == 'compactViewportKeepsAnInventoryEntry()'
           for report in reports for case in report.findall('testcase')), 'Compact inventory regression did not run'
assert sum(int(report.attrib['failures']) + int(report.attrib['errors']) for report in reports) == 0
print(f'Archive verified: {jar}')
print(f'Archive size: {jar.stat().st_size} bytes')
print(f'Archive SHA256: {hashlib.sha256(jar.read_bytes()).hexdigest()}')
print(f'JUnit: {total} tests, zero failures, zero errors')
print('Verified client distribution annotation, local public GuideME calls, comma default, locale parity, dependency metadata and public native query-guide registration and absence of bundled engine, reflection or packet registration.')
print('\nExact released public signatures:\n' + released)
