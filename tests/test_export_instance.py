"""Materialization tests use only tiny private fixtures and a native cache."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/export_instance.py"


def digest(data, algorithm="sha256"):
    return hashlib.new(algorithm, data).hexdigest()


class InstanceExport(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.cache = self.root / "cache"
        self.cache.mkdir()
        self.output = self.root / "output"
        self.entries = []
        self.add_file("mods/helper.jar", b"custom helper")
        self.add_file("config/settings.toml", b"setting = true\n")
        self.seal()

    def add_file(self, name, data, metafile=False):
        path = self.source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        self.entries.append((name, digest(data), metafile))
        return path

    def seal(self):
        text = 'hash-format = "sha256"\n'
        for name, checksum, meta in self.entries:
            text += f'\n[[files]]\nfile = {json.dumps(name)}\nhash = "{checksum}"\n'
            if meta:
                text += 'metafile = true\n'
        (self.source / "index.toml").write_text(text)
        (self.source / "pack.toml").write_text(
            'name = "Fixture"\nversion = "fixture.1"\n[index]\nfile = "index.toml"\n'
            f'hash-format = "sha256"\nhash = "{digest(text.encode())}"\n'
            '[versions]\nminecraft = "1.21.1"\nneoforge = "21.1.255"\n')

    def export(self, **kwargs):
        self.assertTrue(SCRIPT.is_file(), "export_instance.py has not been implemented")
        spec = importlib.util.spec_from_file_location("export_instance", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.export(self.output, source=self.source, cache=self.cache, **kwargs)

    def artifact(self, side="both", filename="download.jar", algorithm="sha512"):
        data = b"tiny cached artifact"
        canonical = digest(data)
        path = self.cache / canonical[:2] / canonical[2:]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        (self.cache / "index.json").write_text(json.dumps({"Version": 2, "Hashes": {
            "sha256": [canonical], algorithm: [digest(data, algorithm)]}}))
        self.add_file("mods/download.pw.toml", (
            f'filename = {json.dumps(filename)}\nside = "{side}"\n[download]\n'
            f'hash-format = "{algorithm}"\nhash = "{digest(data, algorithm)}"\n').encode(), True)
        self.seal()
        return path

    def fails_cleanly(self, message, **kwargs):
        with self.assertRaisesRegex((ValueError, RuntimeError, OSError), message):
            self.export(**kwargs)
        self.assertFalse(self.output.exists())
        self.assertFalse(list(self.output.parent.glob(".instance-export-*")))

    def test_native_cache_artifact_copy(self):
        cached = self.artifact()
        self.export()
        target = self.output / "game/mods/download.jar"
        self.assertEqual(target.read_bytes(), cached.read_bytes())
        self.assertNotEqual(target.stat().st_ino, cached.stat().st_ino)
        self.assertFalse((self.output / "game/mods/download.pw.toml").exists())

    def test_sha1_cache_and_nested_filename(self):
        cached = self.artifact(filename="nested/download.jar", algorithm="sha1")
        self.export()
        self.assertEqual((self.output / "game/mods/nested/download.jar").read_bytes(), cached.read_bytes())

    def test_canonical_cache_checksum(self):
        cached = self.artifact()
        bad_name = "a" * 64
        moved = self.cache / bad_name[:2] / bad_name[2:]
        moved.parent.mkdir()
        cached.rename(moved)
        index_path = self.cache / "index.json"
        data = json.loads(index_path.read_text())
        data["Hashes"]["sha256"] = [bad_name]
        index_path.write_text(json.dumps(data))
        self.fails_cleanly("checksum mismatch")

    def test_cache_arrays_must_be_parallel(self):
        self.artifact()
        path = self.cache / "index.json"
        data = json.loads(path.read_text())
        data["Hashes"]["sha512"].append("bad")
        path.write_text(json.dumps(data))
        self.fails_cleanly("parallel")

    def test_menu_images_handbook_and_configurations_unchanged(self):
        self.add_file("config/fancymenu/assets/menu.png", b"image bytes")
        self.add_file("resourcepacks/handbook/assets/guide/book.md", b"handbook text")
        self.add_file("configureddefaults/options.txt", b"options")
        self.seal()
        self.export()
        for name, _, _ in self.entries:
            self.assertEqual((self.output / "game" / name).read_bytes(), (self.source / name).read_bytes())

    def test_default_dist_subtree_is_output_only(self):
        self.output = self.source / "dist/astropunk-fixture.1-instance"
        self.export()
        self.assertTrue((self.output / "game/mods/helper.jar").is_file())

    def test_staging_removed_on_copy_failure(self):
        from unittest.mock import patch
        with patch("shutil.copyfile", side_effect=OSError("disk failure")):
            self.fails_cleanly("disk failure")
        self.assertTrue((self.source / "mods/helper.jar").is_file())

    def test_cli_empty_template(self):
        import subprocess
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.output),
                                 "--source", str(self.source), "--cache", str(self.cache),
                                 "--template", ""], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.output / "instance-export.json").is_file())

    def test_unrelated_staging_directory_is_preserved(self):
        unrelated = self.root / ".instance-export-keep"
        unrelated.mkdir()
        marker = unrelated / "keep"
        marker.write_text("keep")
        (self.source / "mods/helper.jar").write_bytes(b"corrupt")
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            self.export()
        self.assertEqual(marker.read_text(), "keep")
        self.assertFalse(self.output.exists())

    def test_output_symlink_rejected(self):
        self.output.symlink_to(self.root / "missing")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.export()
        self.assertTrue(self.output.is_symlink())

    def test_cache_output_overlap(self):
        self.output = self.cache / "output"
        self.fails_cleanly("overlap")

    def test_publication_cannot_replace_newly_created_output(self):
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location("export_instance", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = module.publish

        def concurrent_output(stage, output):
            output.mkdir()
            (output / "keep").write_text("keep")
            return original(stage, output)
        with patch.object(module, "publish", side_effect=concurrent_output):
            with self.assertRaisesRegex(ValueError, "exists"):
                module.export(self.output, source=self.source, cache=self.cache)
        self.assertEqual((self.output / "keep").read_text(), "keep")
        self.assertFalse(list(self.root.glob(".instance-export-*")))

    def test_existing_empty_output_is_not_replaced(self):
        self.output.mkdir()
        with self.assertRaisesRegex(ValueError, "exists"):
            self.export()
        self.assertEqual(list(self.output.iterdir()), [])

    def test_server_excluded_without_cache(self):
        self.artifact(side="server")
        (self.cache / "index.json").unlink()
        result = self.export()
        self.assertFalse((self.output / "game/mods/download.jar").exists())
        self.assertEqual(result["counts"]["server_excluded"], 1)

    def test_missing_cache_mapping(self):
        self.artifact()
        (self.cache / "index.json").write_text('{"Version":2,"Hashes":{"sha256":[],"sha512":[]}}')
        self.fails_cleanly("Missing cached artifact")

    def test_missing_cache_bytes(self):
        self.artifact().unlink()
        self.fails_cleanly("Missing cached artifact")

    def test_cache_checksum(self):
        self.artifact().write_bytes(b"corrupt")
        self.fails_cleanly("checksum mismatch")

    def test_pack_index_checksum(self):
        with (self.source / "index.toml").open("a") as stream:
            stream.write("\n# changed\n")
        self.fails_cleanly("checksum mismatch")

    def test_indexed_metadata_checksum_even_server(self):
        self.artifact(side="server")
        with (self.source / "mods/download.pw.toml").open("a") as stream:
            stream.write("\n# changed\n")
        self.fails_cleanly("checksum mismatch")

    def test_indexed_ordinary_checksum(self):
        (self.source / "mods/helper.jar").write_bytes(b"corrupt")
        self.fails_cleanly("checksum mismatch")

    def test_unsafe_index_paths(self):
        for name in ("../outside", "/absolute", "mods/../bad", "mods\\bad", "C:bad", "mods//bad", "mods/./bad"):
            with self.subTest(name=name):
                self.entries.append((name, "0" * 64, False))
                self.seal()
                self.fails_cleanly("Unsafe")
                self.entries.pop()

    def test_unsafe_artifact_filename(self):
        self.artifact(filename="../escape.jar")
        self.fails_cleanly("Unsafe")

    def test_source_file_symlink(self):
        path = self.source / "mods/helper.jar"
        data = path.read_bytes()
        path.unlink()
        outside = self.root / "outside"
        outside.write_bytes(data)
        path.symlink_to(outside)
        self.fails_cleanly("[Ss]ymlink")

    def test_source_parent_symlink(self):
        (self.source / "mods").rename(self.root / "mods")
        (self.source / "mods").symlink_to(self.root / "mods", target_is_directory=True)
        self.fails_cleanly("[Ss]ymlink")

    def test_cache_symlink(self):
        path = self.artifact()
        outside = self.root / "outside"
        path.rename(outside)
        path.symlink_to(outside)
        self.fails_cleanly("[Ss]ymlink")

    def test_duplicate_output(self):
        self.artifact(filename="helper.jar")
        self.fails_cleanly("[Cc]ollision|[Dd]uplicate")

    def test_file_directory_collision(self):
        self.entries.append(("mods/helper.jar/nested", "0" * 64, False))
        self.seal()
        self.fails_cleanly("[Cc]ollision")

    def test_source_output_overlap(self):
        self.output = self.source / "export"
        self.fails_cleanly("overlap")

    def test_output_parent_symlink(self):
        linked = self.root / "linked"
        linked.symlink_to(self.root, target_is_directory=True)
        self.output = linked / "output"
        self.fails_cleanly("[Ss]ymlink")

    def test_existing_output_preserved(self):
        self.output.mkdir()
        marker = self.output / "keep"
        marker.write_text("keep")
        with self.assertRaisesRegex((ValueError, RuntimeError, OSError), "exist"):
            self.export()
        self.assertEqual(marker.read_text(), "keep")
        self.assertFalse(list(self.root.glob(".instance-export-*")))

    def template(self, **changes):
        path = self.root / "template"
        (path / "game/empty/nested").mkdir(parents=True)
        metadata = {"game_version": "1.21.1", "loader": "neoforge", "loader_version": "21.1.255"}
        metadata.update(changes)
        (path / "template.json").write_text(json.dumps(metadata))
        return path

    def test_template_empty_layout(self):
        self.export(template=self.template())
        self.assertTrue((self.output / "game/empty/nested").is_dir())
        self.assertFalse((self.output / "template.json").exists())

    def test_template_ancestor_file_collision(self):
        path = self.template()
        self.add_file("empty", b"collides with empty folder ancestor")
        self.seal()
        self.fails_cleanly("[Cc]ollision", template=path)

    def test_empty_template_string(self):
        self.export(template="")
        self.assertTrue((self.output / "game").is_dir())

    def test_template_mismatch(self):
        path = self.template(loader_version="21.1.254")
        self.fails_cleanly("[Tt]emplate.*match", template=path)

    def test_template_regular_file(self):
        path = self.template()
        (path / "game/options.txt").write_text("do not copy")
        self.fails_cleanly("[Tt]emplate.*file", template=path)

    def test_template_symlink(self):
        path = self.template()
        (path / "game/link").symlink_to(self.source)
        self.fails_cleanly("[Ss]ymlink", template=path)

    def test_template_output_overlap(self):
        path = self.template()
        self.output = path / "export"
        self.fails_cleanly("overlap", template=path)

    def test_ordinary_files_and_manifest_are_independent(self):
        self.export()
        manifest = json.loads((self.output / "instance-export.json").read_text())
        self.assertEqual(manifest["pack_version"], "fixture.1")
        self.assertEqual(manifest["requirements"], {"minecraft": "1.21.1", "loader": "neoforge", "loader_version": "21.1.255"})
        self.assertEqual(manifest["counts"]["files"], 2)
        for name, checksum, _ in self.entries:
            copy = self.output / "game" / name
            self.assertEqual(copy.read_bytes(), (self.source / name).read_bytes())
            self.assertNotEqual(copy.stat().st_ino, (self.source / name).stat().st_ino)
            self.assertEqual(manifest["files"]["game/" + name], checksum)


if __name__ == "__main__":
    unittest.main()
