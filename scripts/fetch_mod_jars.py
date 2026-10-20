#!/usr/bin/env python3
"""Download the pack's mod jars into a local cache for offline ID checks.

The handbook must never name an item that the pack does not ship. Jars are not
kept in the packwiz repository, so this caches them under build/ for scanning.
Existing files are skipped, which makes the fetch resumable.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MODS = ROOT / 'mods'
CACHE = ROOT / 'build' / 'mod-cache'


def targets():
    for meta in sorted(MODS.glob('*.pw.toml')):
        text = meta.read_text()
        name = re.search(r'^filename = "([^"]+)"', text, re.M)
        url = re.search(r'^url = "([^"]+)"', text, re.M)
        if not name:
            continue
        if url:
            yield url.group(1), name.group(1)
            continue
        # CurseForge metadata entries carry no URL, but the CDN path is derivable
        # from the file id as the first four digits and the remainder.
        file_id = re.search(r'file-id = (\d+)', text)
        if file_id and 'metadata:curseforge' in text:
            value = file_id.group(1)
            yield ('https://mediafilez.forgecdn.net/files/%s/%s/%s'
                   % (value[:4], value[4:], name.group(1))), name.group(1)


def fetch(pair):
    url, name = pair
    destination = CACHE / name
    if destination.exists() and destination.stat().st_size > 0:
        return None
    temporary = destination.with_suffix(destination.suffix + '.part')
    try:
        with urllib.request.urlopen(url, timeout=120) as response:
            temporary.write_bytes(response.read())
        temporary.replace(destination)
        return None
    except Exception as error:  # noqa: BLE001 - report and continue
        temporary.unlink(missing_ok=True)
        return name + ': ' + str(error)


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    pairs = list(targets())
    with ThreadPoolExecutor(max_workers=8) as pool:
        failures = [line for line in pool.map(fetch, pairs) if line]
    print('cached', len(list(CACHE.glob('*.jar'))), 'of', len(pairs))
    for line in failures:
        print('FAIL', line)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
