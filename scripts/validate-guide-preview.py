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
assert not (resource / "assets/astropunk/guideme_guides/handbook.json").exists(), "Native helper registration must not be overridden by a resource guide"
assert (root / "mods/astropunk-handbook-access-1.0.0.jar").exists()
pages = resource / "assets/astropunk/guides/astropunk/handbook"
expected = {p.name for p in pages.glob("*.md")}
assert {p.name for p in (pages / "_zh_cn").glob("*.md")} == expected
handbook = json.loads((root / 'docs/handbook-draft-manifest.json').read_text())
assert len(expected) == handbook['article_count'] + handbook['category_count'] + handbook['navigation_page_count'] + handbook['reference_directory_count'] + 1
paths = [e['metadata_path'] for e in handbook['content']]
assert len(paths) == len(set(paths)), 'Duplicate provider inventory'
homes = [path for article in handbook['pages'] for path in article['metadata_paths']]
assert sorted(homes) == sorted(paths), 'Missing or duplicate primary provider home'
for article in handbook['pages']:
    assert article['filename'] in expected
    for language in ('', '_zh_cn'):
        article_text = (pages / language / article['filename']).read_text()
        if not article['drafted']:
            assert 'WIP' in article_text
        for entry in handbook['content']:
            if entry['metadata_path'] in article['metadata_paths']:
                heading = '## 相关模组' if language else '## Related mods'
                assert heading in article_text, entry['metadata_path']
                footer = article_text.rsplit(heading, 1)[1]
                assert not re.search(r'^## ', footer, re.M), article['filename']
                label = entry['name'].replace('|', ',').replace('\n', ' ').replace('—', ', ').replace('–', ' to ').replace(';', ',').replace('；', '，')
                identity = '[' + label + '](' + entry['topic'] + '.md)'
                matching_rows = [line for line in footer.splitlines() if identity in line]
                assert len(matching_rows) == 1, entry['metadata_path']
                row = matching_rows[0]
                assert '![' in row or '<ItemImage ' in row, entry['metadata_path']
                availability = {
                    'baseline': '已安装基准版' if language else 'Baseline, installed',
                    'heavy': '重型版，当前未安装' if language else 'Heavy edition, not installed here',
                    'deferred': '暂缓，未安装' if language else 'Deferred, not installed',
                }[entry['availability']]
                assert availability in row, entry['metadata_path']
assert not (pages / "_zh_tw").exists()
links = 0
for p in pages.rglob("*.md"):
    text = p.read_text()
    assert text.startswith("---\n"), p
    for parent in re.findall(r'^  parent: (.+)$', text, re.MULTILINE):
        assert (p.parent / parent).is_file(), (p, parent)
    assert "\u2014" not in text and "\u2013" not in text, p
    assert 'minecraft:bed' not in text, p
    # Native ItemImage is allowed for decorative navigation and category labels.
    # Actual instructional items use ItemGrid with ItemIcon and native tooltips.
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
    assert 'quick-reference.md' in visited, language
    assert 'mod-catalogs.md' not in expected
    assert not list(locale_root.glob('category-*.md'))
    home_links = set(re.findall(r'\]\(([^)]+\.md)\)', (locale_root / 'index.md').read_text()))
    reference_links = set(re.findall(r'\]\(([^)]+\.md)\)', (locale_root / 'quick-reference.md').read_text()))
    assert home_links == {'quick-reference.md'}, language
    assert len(reference_links) == 16, language
    assert 'reference.equipment.md' not in reference_links
    assert not (resource / 'assets/astropunk/guideme_guides/handbook.json').exists(), 'Native query guide registration must not be overridden'
    for filename in ('reference.equipment.md', 'combat.abilities.md'):
        assert '  parent: reference.skills.md\n' in (locale_root / filename).read_text()
    for article in handbook['pages']:
        current = article['filename']
        seen = {current}
        depth = 0
        while parents := re.findall(r'^  parent: (.+)$', (locale_root / current).read_text(), re.M):
            assert len(parents) == 1, current
            current = parents[0]
            assert current not in seen, article['filename']
            seen.add(current)
            depth += 1
        assert current == 'quick-reference.md', article['filename']
        assert depth <= 2, article['filename']
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
