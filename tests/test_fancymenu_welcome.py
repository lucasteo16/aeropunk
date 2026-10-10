from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FancyMenuWelcomeDefaults(unittest.TestCase):
    def test_fresh_instances_disable_welcome_dialog_and_editor_overlay(self):
        text = (ROOT / 'configureddefaults/config/fancymenu/options.txt').read_text()
        self.assertIn("##[tutorial]\nB:show_welcome_screen = 'false';", text)
        self.assertIn("##[customization]\nB:show_customization_overlay = 'false';", text)


if __name__ == '__main__':
    unittest.main()
