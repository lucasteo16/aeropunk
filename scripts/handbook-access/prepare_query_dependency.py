#!/usr/bin/env python3
"""Fetch only the selected compile-only EMI release, verify packwiz SHA512."""
from pathlib import Path
import hashlib
import tomllib
import urllib.request

ROOT = Path(__file__).resolve().parent
metadata = tomllib.loads((ROOT.parents[1] / 'mods/emi.pw.toml').read_text())
assert metadata['filename'] == 'emi-1.1.24+1.21.1+neoforge.jar'
assert metadata['download']['hash-format'] == 'sha512'
target = ROOT / 'emi-1.1.24.jar'
if not target.exists() or hashlib.sha512(target.read_bytes()).hexdigest() != metadata['download']['hash']:
    data = urllib.request.urlopen(metadata['download']['url'], timeout=60).read()
    assert hashlib.sha512(data).hexdigest() == metadata['download']['hash'], 'Selected EMI checksum mismatch'
    target.write_bytes(data)
print('Selected compile-only EMI checksum verified.')
