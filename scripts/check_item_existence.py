#!/usr/bin/env python3
"""Find handbook references without matching assets in the selected jar cache.

This is a discovery check, NOT proof of runtime item registration. Assets can
remain for disabled compatibility content, and blocks may have no item form.
Translation keys must never be converted into candidate registry identifiers.
Vanilla namespaces are skipped because the Minecraft jar is not cached here.

Prepare the cache first: python scripts/fetch_mod_jars.py
Run: python scripts/check_item_existence.py [topic ...]
"""
from pathlib import Path
import collections
import io
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'build' / 'mod-cache'
CONTENT = ROOT / 'docs' / 'handbook-content.json'
SCOPE = ROOT / 'docs' / 'handbook-refurbish-scope.json'
IDENT = re.compile(r'<(?:ItemIcon|ItemLink|ItemImage)\b[^>]*\bid="([^"]+)"')
MODEL = re.compile(r'assets/([^/]+)/(?:models/(?:item|block)|blockstates)/(.+)\.json$')
NESTED = re.compile(r'META-INF/(?:jars|jarjar)/.+\.jar$')
VANILLA = {'minecraft', 'forge', 'neoforge', 'c', 'tag'}


def harvest(archive, index, depth=0):
    for member in archive.namelist():
        found = MODEL.match(member)
        if found:
            namespace = found.group(1)
            # Preserve the entire relative path, including integration subfolders.
            # A model at chipped/alchemy_bench_upgrade is not chipped.alchemy_bench_upgrade.
            index[namespace].add(found.group(2))
        if NESTED.match(member) and depth < 2:
            try:
                inner = zipfile.ZipFile(io.BytesIO(archive.read(member)))
            except Exception:  # noqa: BLE001 - skip unreadable nested jar
                continue
            harvest(inner, index, depth + 1)
            inner.close()


def build_index():
    index = collections.defaultdict(set)
    for jar in sorted(CACHE.glob('*.jar')):
        try:
            archive = zipfile.ZipFile(jar)
        except Exception:  # noqa: BLE001 - skip unreadable jar
            continue
        harvest(archive, index)
        archive.close()
    return index


def main():
    if not CACHE.is_dir():
        print('no jar cache at', CACHE, 'run scripts/fetch_mod_jars.py first')
        return 2
    index = build_index()
    content = json.loads(CONTENT.read_text())
    selected = sys.argv[1:]
    if not selected:
        batches = json.loads(SCOPE.read_text())['batches']
        selected = [topic for batch in batches.values() for topic in batch['topics']]
    unknown = collections.defaultdict(set)
    checked = 0
    for topic in selected:
        for locale, body in content[topic].items():
            for identifier in IDENT.findall(body):
                namespace, _, name = identifier.partition(':')
                if namespace in VANILLA:
                    continue
                checked += 1
                if namespace not in index:
                    unknown[identifier + ' (' + locale + ')'].add('no cached asset namespace')
                elif name not in index[namespace]:
                    unknown[identifier + ' (' + locale + ')'].add('no exact matching asset path')
    print('asset discovery only:', checked, 'references across', len(selected), 'topics')
    print('Runtime item registration and conditional loading are NOT verified by this check.')
    for identifier, reasons in sorted(unknown.items()):
        print('NO_ASSET_EVIDENCE', identifier, ' '.join(sorted(reasons)))
    print('references without asset evidence:', len(unknown))
    return 1 if unknown else 0


if __name__ == '__main__':
    sys.exit(main())
