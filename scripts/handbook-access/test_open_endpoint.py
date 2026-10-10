#!/usr/bin/env python3
"""Regression contract against the exact released command and helper bytecode.

No Minecraft process is started. This proves endpoint selection, not rendering.
"""
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parent
JAVAP = ROOT / 'toolchain/jdk-21.0.12.1+1/bin/javap'
RELEASED = ROOT / 'guideme-21.1.19.jar'
HELPER = ROOT / 'build/libs/astropunk-handbook-access-1.0.0.jar'
ENDPOINT = 'guideme/internal/GuideMEClient.openGuideAtPreviousPage:(Lguideme/Guide;Lnet/minecraft/resources/ResourceLocation;)Z'


def bytecode(jar, name):
    return subprocess.check_output([str(JAVAP), '-classpath', str(jar), '-p', '-c', name], text=True)


class OpenEndpointTest(unittest.TestCase):
    def test_helper_uses_same_local_endpoint_as_working_client_command(self):
        command = bytecode(RELEASED, 'guideme.internal.command.GuideClientCommand')
        helper = bytecode(HELPER, 'dev.astropunk.handbook.HandbookAccess')
        self.assertIn(ENDPOINT, command)
        self.assertTrue(ENDPOINT in helper, 'Shortcut must bypass the common proxy and match guidemec opening')
        self.assertNotIn('guideme/GuidesCommon.openGuide:', helper)
        self.assertIn('guideme/Guide.getStartPage:', helper)

    def test_released_common_endpoint_discards_proxy_failure(self):
        common = bytecode(RELEASED, 'guideme.GuidesCommon')
        self.assertIn('guideme/internal/GuideMEProxy.openGuide:', common)
        self.assertIn('pop', common)
        server = bytecode(RELEASED, 'guideme.internal.GuideMEServerProxy')
        self.assertIn('instanceof', server)
        self.assertIn('net/minecraft/server/level/ServerPlayer', server)
        self.assertIn('iconst_0', server)

    def test_released_client_proxy_already_supports_the_local_player(self):
        proxy = bytecode(RELEASED, 'guideme.internal.GuideMEClientProxy')
        self.assertIn('Field net/minecraft/client/Minecraft.player:', proxy)
        self.assertIn('if_acmpne', proxy)
        self.assertIn(ENDPOINT, proxy)
        client = bytecode(RELEASED, 'guideme.internal.GuideMEClient')
        self.assertIn('Field guideme/internal/GuideME.PROXY:', client)
        # Common opening is not inherently server-only. Its normal client proxy
        # already reaches this endpoint, so bytecode alone cannot prove why the
        # reported live shortcut failed.


if __name__ == '__main__':
    unittest.main(verbosity=2)
