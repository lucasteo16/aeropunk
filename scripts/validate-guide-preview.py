"""Validate guide source and native Modrinth export, without launching Minecraft."""
import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--source-only', action='store_true')
args = parser.parse_args()
import hashlib
import json
import re
import subprocess
import tomllib
import zipfile

root = Path(__file__).resolve().parents[1]
pack = tomllib.loads((root / "pack.toml").read_text())
resource = root / "resourcepacks/astropunk-guide-preview"
json.loads((resource / "pack.mcmeta").read_text())
definition = json.loads((resource / "assets/astropunk/guideme_guides/handbook.json").read_text())
assert definition["default_language"] == "en_us"
pages = resource / "assets/astropunk/guides/astropunk/handbook"
expected = {p.name for p in pages.glob("*.md")}
assert {p.name for p in (pages / "_zh_cn").glob("*.md")} == expected
handbook = json.loads((root / 'docs/handbook-draft-manifest.json').read_text())
assert len(expected) == handbook['article_count'] + handbook['category_count'] + handbook['navigation_page_count'] + handbook['reference_directory_count'] + 1
for article in handbook['pages']:
    assert article['filename'] in expected
    for language in ('', '_zh_cn'):
        article_text = (pages / language / article['filename']).read_text()
        if not article['drafted']:
            assert 'WIP' in article_text
        for entry in handbook['content']:
            if entry['metadata_path'] in article['metadata_paths']:
                assert entry['name'] in article_text
                if entry['availability'] in ('deferred', 'heavy'):
                    assert ('未安装' if language else 'not installed') in article_text
assert not (pages / "_zh_tw").exists()
links = 0
for p in pages.rglob("*.md"):
    text = p.read_text()
    assert text.startswith("---\n"), p
    for parent in re.findall(r'^  parent: (.+)$', text, re.MULTILINE):
        assert (p.parent / parent).is_file(), (p, parent)
    assert "\u2014" not in text and "\u2013" not in text, p
    assert 'minecraft:bed' not in text, p
    # Decorative home icons intentionally have no item tooltip; instructional slots still do.
    if p.name not in ('index.md', 'quick-reference.md', 'mod-catalogs.md'):
        assert '<ItemImage' not in text, p
    for phrase in ('Draft for review', 'Drafts to review', 'first preview', 'This draft', 'Back to activities', '草稿，可供评阅'):
        assert phrase not in text, (p, phrase)
    assert '`@' not in text, p
    for target in re.findall(r"\]\(([^)]+\.md)\)", text):
        assert (p.parent / target).is_file(), (p, target)
        links += 1
for language in ('', '_zh_cn'):
    locale_root = pages / language
    visited = set()
    pending = ['index.md']
    while pending:
        filename = pending.pop()
        if filename in visited:
            continue
        visited.add(filename)
        page_text = (locale_root / filename).read_text()
        pending.extend(re.findall(r'\]\(([^)]+\.md)\)', page_text))
        pending.extend(re.findall(r'^  parent: (.+)$', page_text, re.MULTILINE))
    assert {a['filename'] for a in handbook['pages']} <= visited, language
    assert {'quick-reference.md', 'mod-catalogs.md'} <= visited, language
    assert {f'category-{c}.md' for c in ('automation', 'storage', 'food', 'building', 'travel', 'combat', 'exploration', 'utilities', 'visuals', 'technical')} <= visited
options = (root / "configureddefaults/options.txt").read_text()
assert '"file/astropunk-guide-preview"' in options
if args.source_only:
    assert '# Astropunk\n' in (pages / 'index.md').read_text()
    assert 'item_ids:' in (pages / 'machines.ore-processing.md').read_text()
    print(json.dumps({'mode': 'source-only', 'pages': len(list(pages.rglob('*.md'))), 'article_count': handbook['article_count'], 'written_articles': handbook['draft_articles'], 'installed_content_count': handbook['installed_content_count'], 'links': links, 'client_runtime_tested': False}, indent=2))
    sys.exit(0)
export = root / "dist" / f"astropunk-{pack['version']}-modrinth.mrpack"
with zipfile.ZipFile(export) as archive:
    assert archive.testzip() is None
    helper = root / "mods/astropunk-handbook-access-1.0.0.jar"
    assert archive.read("overrides/mods/" + helper.name) == helper.read_bytes()
    names = set(archive.namelist())
    manifest = json.loads(archive.read("modrinth.index.json"))
    assert manifest["versionId"] == pack["version"]
    assert manifest["dependencies"]["minecraft"] == "1.21.1"
    assert manifest["dependencies"]["neoforge"] == "21.1.255"
    assert any(f["path"] == "mods/guideme-21.1.19.jar" for f in manifest["files"])
    checked = 0
    for p in resource.rglob("*"):
        if p.is_file():
            name = "overrides/" + p.relative_to(root).as_posix()
            assert archive.read(name) == p.read_bytes(), name
            checked += 1
    assert archive.read("overrides/configureddefaults/options.txt").decode() == options
    assert not any(n.startswith(("overrides/docs/", "overrides/scripts/", "overrides/build/", "overrides/dist/")) for n in names)
    base = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "34cb006", "mods"], cwd=root, text=True).splitlines()
    for name in base:
        previous = subprocess.check_output(["git", "show", f"34cb006:{name}"], cwd=root)
        assert (root / name).read_bytes() == previous, name
    additions = {p.relative_to(root).as_posix() for p in (root / "mods").glob("*.pw.toml")} - set(base)
    assert additions == {"mods/guideme.pw.toml"}, additions
print(json.dumps({"pages": len(list(pages.rglob('*.md'))), "draft_articles": handbook['draft_articles'], "article_count": handbook['article_count'], "installed_content_count": handbook['installed_content_count'], "links": links, "resource_files_verified": checked, "baseline_mod_files_unchanged": len(base), "additional_mods": sorted(additions), "archive": str(export), "sha256": hashlib.sha256(export.read_bytes()).hexdigest(), "client_runtime_tested": False}, indent=2))
