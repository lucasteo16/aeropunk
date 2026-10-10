"""Official registration tests never use personal installations or launch a game."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load_wrapper():
    path = SCRIPTS / "export_official_instance.py"
    assert path.is_file(), "Official export wrapper is not implemented"
    spec = importlib.util.spec_from_file_location("export_official_instance", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(SCRIPTS))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


class OfficialExport(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.source = self.home / "source"
        self.source.mkdir()
        self.cache = self.home / "cache"
        self.cache.mkdir()
        data = b"tiny cached mod"
        digest = hashlib.sha256(data).hexdigest()
        artifact = self.cache / digest[:2] / digest[2:]
        artifact.parent.mkdir()
        artifact.write_bytes(data)
        (self.cache / "index.json").write_text(json.dumps({"Version": 2, "Hashes": {"sha256": [digest]}}))
        metadata = f'filename = "tiny.jar"\n[download]\nhash-format = "sha256"\nhash = "{digest}"\n'
        (self.source / "tiny.pw.toml").write_text(metadata)
        index = ('hash-format = "sha256"\n[[files]]\nfile = "tiny.pw.toml"\nmetafile = true\n'
                 f'hash = "{hashlib.sha256(metadata.encode()).hexdigest()}"\n')
        (self.source / "index.toml").write_text(index)
        (self.source / "pack.toml").write_text('name = "Fixture"\nversion = "fixture.1"\n[index]\nfile = "index.toml"\n'
            f'hash-format = "sha256"\nhash = "{hashlib.sha256(index.encode()).hexdigest()}"\n'
            '[versions]\nminecraft = "1.21.1"\nneoforge = "21.1.255"\n')
        self.profiles = self.home / ".minecraft/launcher_profiles.json"
        self.profiles.parent.mkdir()
        self.original = {"profiles": {"vanilla": {"name": "Template", "type": "custom", "gameDir": "old", "javaArgs": "-Xmx3G", "javaDir": "saved-java"}},
                         "selectedProfile": "vanilla", "settings": {"keep": True}, "other": [1, "exact"]}
        self.original_bytes = (json.dumps(self.original, indent=3) + "\n").encode()
        self.profiles.write_bytes(self.original_bytes)
        self.runtime = self.home / ".minecraft/versions/neoforge-21.1.255/neoforge-21.1.255.json"
        self.runtime.parent.mkdir(parents=True)
        self.runtime.write_text(json.dumps({"id": "neoforge-21.1.255", "inheritsFrom": "1.21.1"}))
        self.output = self.home / "explicit"

    def run_export(self, output=None, **kwargs):
        module = load_wrapper()
        with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed"):
            result = module.export(output, source=self.source, cache=self.cache, **kwargs)
        return result

    def test_explicit_destination_registration_preserves_existing_fields_and_backup(self):
        result = self.run_export(self.output)
        saved = json.loads(self.profiles.read_text())
        registration = result["official_launcher"]
        profile = saved["profiles"].pop(registration["profile_id"])
        self.assertEqual(saved, self.original)
        self.assertEqual(profile["gameDir"], str(self.output / "game"))
        self.assertEqual(profile["lastVersionId"], "neoforge-21.1.255")
        self.assertEqual(profile["type"], "custom")
        self.assertIn("Astropunk Guide Test fixture.1", profile["name"])
        self.assertEqual(profile["created"], profile["lastUsed"])
        self.assertEqual(profile["javaArgs"], "-Xmx6G")
        self.assertNotIn("javaDir", profile)
        self.assertEqual(registration["profiles_path"], str(self.profiles))
        self.assertEqual(json.loads((self.output / "instance-export.json").read_text()), result)
        backups = list((self.home / "Projects/lucas/instance-templates/official-neoforge-1.21.1/backups").glob("*.json"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), self.original_bytes)
        self.assertEqual(backups[0].stat().st_mode & 0o777, 0o600)
        self.assertEqual(backups[0].parent.stat().st_mode & 0o777, 0o700)
        self.assertEqual((self.output / "game/tiny.jar").read_bytes(), b"tiny cached mod")


    def test_installed_manifest_must_be_an_object(self):
        self.runtime.write_text("[]")
        with self.assertRaisesRegex(ValueError, "runtime.*object"):
            self.run_export(self.output)
        self.assertFalse(self.output.exists())

    def test_unique_automatic_destinations(self):
        first = self.run_export()
        second = self.run_export("")
        saved = json.loads(self.profiles.read_text())["profiles"]
        paths = [Path(saved[result["official_launcher"]["profile_id"]]["gameDir"]).parent for result in (first, second)]
        self.assertNotEqual(paths[0], paths[1])
        for path in paths:
            self.assertEqual(path.parent, self.home / "Projects/lucas/instance-runs")
            self.assertTrue(path.name.startswith("astropunk-fixture.1-"))

    def test_missing_installed_runtime_refused_before_export(self):
        self.runtime.unlink()
        with self.assertRaisesRegex((ValueError, OSError), "installed|runtime"):
            self.run_export(self.output)
        self.assertFalse(self.output.exists())
        self.assertEqual(self.profiles.read_bytes(), self.original_bytes)

    def test_wrong_runtime_inheritance_or_identifier_refused(self):
        for metadata in ({"id": "neoforge-21.1.255", "inheritsFrom": "1.21"},
                         {"id": "wrong", "inheritsFrom": "1.21.1"}):
            with self.subTest(metadata=metadata):
                self.runtime.write_text(json.dumps(metadata))
                with self.assertRaisesRegex(ValueError, "runtime|inherit"):
                    self.run_export(self.output)
                self.assertFalse(self.output.exists())


    def make_template(self, **profile_fields):
        template = self.home / "Projects/lucas/instance-templates/official-neoforge-1.21.1"
        (template / "game/resourcepacks").mkdir(parents=True)
        (template / "template.json").write_text(json.dumps({"game_version": "1.21.1", "loader": "neoforge",
            "loader_version": "21.1.255", "launcher_profile": {"icon": "Grass", "type": "custom", **profile_fields}}))
        return template

    def test_saved_template_icon_and_empty_layout_only(self):
        template = self.make_template()
        original = (template / "template.json").read_bytes()
        result = self.run_export(self.output)
        profile = json.loads(self.profiles.read_text())["profiles"][result["official_launcher"]["profile_id"]]
        self.assertEqual(profile["icon"], "Grass")
        self.assertTrue((self.output / "game/resourcepacks").is_dir())
        self.assertEqual((template / "template.json").read_bytes(), original)

    def test_reject_stale_or_unsafe_template_fields(self):
        template = self.make_template()
        for fields in ({"gameDir": "stale"}, {"created": "stale"}, {"lastUsed": "stale"},
                       {"id": "stale"}, {"javaArgs": "-Xmx9G"}, {"javaDir": "stale"},
                       {"icon": "../unsafe"}, {"type": "release"}):
            with self.subTest(fields=fields):
                (template / "template.json").write_text(json.dumps({"game_version": "1.21.1", "loader": "neoforge",
                    "loader_version": "21.1.255", "launcher_profile": {"icon": "Grass", "type": "custom", **fields}}))
                with self.assertRaisesRegex(ValueError, "[Tt]emplate|icon"):
                    self.run_export(self.output, template=template)
                self.assertFalse(self.output.exists())

    def test_explicit_template_requirements_and_regular_files_rejected(self):
        template = self.make_template()
        metadata = json.loads((template / "template.json").read_text())
        metadata["game_version"] = "1.21"
        (template / "template.json").write_text(json.dumps(metadata))
        with self.assertRaisesRegex(ValueError, "[Tt]emplate.*match"):
            self.run_export(self.output, template=template)
        metadata["game_version"] = "1.21.1"
        (template / "template.json").write_text(json.dumps(metadata))
        (template / "game/options.txt").write_text("personal")
        with self.assertRaisesRegex(ValueError, "[Tt]emplate.*file"):
            self.run_export(self.output, template=template)
        self.assertFalse(self.output.exists())

    def test_process_detection_without_command_disclosure(self):
        module = load_wrapper()
        proc = self.home / "proc"
        process = proc / "123"
        process.mkdir(parents=True)
        for comm, args in (("minecraft-launc", b"launcher\0--token\0SECRET"),
                           ("java", b"java\0net.minecraft.client.main.Main\0--accessToken\0SECRET"),
                           ("java", b"java\0cpw.mods.bootstraplauncher.BootstrapLauncher\0neoforgeclient\0SECRET"),
                           ("java", b"java\0net.neoforged.fml.startup.Client\0SECRET")):
            with self.subTest(comm=comm, args=args):
                (process / "comm").write_text(comm + "\n")
                (process / "cmdline").write_bytes(args)
                with self.assertRaisesRegex(RuntimeError, "running") as error:
                    module.ensure_closed(proc)
                self.assertNotIn("SECRET", str(error.exception))
        (process / "comm").write_text("java\n")
        (process / "cmdline").write_bytes(b"java\0OtherApplication")
        module.ensure_closed(proc)

    def test_running_launcher_refuses_export(self):
        module = load_wrapper()
        with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed", side_effect=RuntimeError("Launcher running")):
            with self.assertRaisesRegex(RuntimeError, "running"):
                module.export(self.output, source=self.source, cache=self.cache)
        self.assertFalse(self.output.exists())
        self.assertEqual(self.profiles.read_bytes(), self.original_bytes)

    def test_concurrent_profile_edit_preserves_output_and_changed_profiles(self):
        module = load_wrapper()
        original_export = module.instance.export
        changed = b'{"profiles": {}, "concurrent": true}\n'
        def export_then_edit(*args, **kwargs):
            result = original_export(*args, **kwargs)
            self.profiles.write_bytes(changed)
            return result
        with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed"), patch.object(module.instance, "export", side_effect=export_then_edit):
            with self.assertRaisesRegex(RuntimeError, "concurrently.*Prepared game folder preserved"):
                module.export(self.output, source=self.source, cache=self.cache)
        self.assertEqual(self.profiles.read_bytes(), changed)
        self.assertTrue((self.output / "game/tiny.jar").is_file())
        self.assertNotIn("official_launcher", json.loads((self.output / "instance-export.json").read_text()))
        self.assertFalse(list(self.profiles.parent.glob(".official-profile-*")))

    def test_launcher_started_during_export_preserves_output(self):
        module = load_wrapper()
        with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed", side_effect=[None, RuntimeError("Minecraft running")]):
            with self.assertRaisesRegex(RuntimeError, "running.*preserved"):
                module.export(self.output, source=self.source, cache=self.cache)
        self.assertEqual(self.profiles.read_bytes(), self.original_bytes)
        self.assertTrue((self.output / "game/tiny.jar").is_file())

    def test_failed_atomic_replace_preserves_output(self):
        module = load_wrapper()
        with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed"), patch.object(module.os, "replace", side_effect=OSError("disk failure")):
            with self.assertRaisesRegex(RuntimeError, "disk failure.*preserved"):
                module.export(self.output, source=self.source, cache=self.cache)
        self.assertEqual(self.profiles.read_bytes(), self.original_bytes)
        self.assertTrue((self.output / "game/tiny.jar").is_file())

    def test_profile_readback_is_verified(self):
        module = load_wrapper()
        real_replace = module.os.replace
        def replace_then_change(source, target):
            real_replace(source, target)
            self.profiles.write_text(json.dumps(self.original))
        with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed"), patch.object(module.os, "replace", side_effect=replace_then_change):
            with self.assertRaisesRegex(RuntimeError, "readback.*preserved"):
                module.export(self.output, source=self.source, cache=self.cache)
        self.assertTrue((self.output / "game/tiny.jar").is_file())
        self.assertNotIn("official_launcher", json.loads((self.output / "instance-export.json").read_text()))


    def test_command_line_defaults_and_empty_output(self):
        import contextlib
        import io
        module = load_wrapper()
        for output_args in ([], ["", "--template", ""]):
            with self.subTest(output_args=output_args):
                arguments = ["export_official_instance.py", *output_args, "--source", str(self.source), "--cache", str(self.cache)]
                with patch.object(Path, "home", return_value=self.home), patch.object(module, "ensure_closed"), patch.object(sys, "argv", arguments), contextlib.redirect_stdout(io.StringIO()) as stdout:
                    module.main()
                self.assertIn("Registered", stdout.getvalue())
        self.assertEqual(len(json.loads(self.profiles.read_text())["profiles"]), 3)

    def test_missing_process_inspection_refused(self):
        module = load_wrapper()
        with self.assertRaisesRegex(RuntimeError, "inspection.*unavailable"):
            module.ensure_closed(self.home / "missing-proc")

    def test_existing_output_remains_untouched(self):
        self.output.mkdir()
        marker = self.output / "keep"
        marker.write_text("user data")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.run_export(self.output)
        self.assertEqual(marker.read_text(), "user data")
        self.assertEqual(self.profiles.read_bytes(), self.original_bytes)


if __name__ == "__main__":
    unittest.main()
