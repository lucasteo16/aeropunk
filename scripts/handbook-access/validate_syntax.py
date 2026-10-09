#!/usr/bin/env python3
"""Run released GuideME syntax validation without starting Minecraft."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
java = root / 'toolchain/jdk-21.0.12.1+1/bin'
classes = root / 'syntax-validation/classes'
classes.mkdir(parents=True, exist_ok=True)
jar = root / 'guideme-21.1.19.jar'
slf4j = next((root / '.gradle-user-home/caches/modules-2').rglob('slf4j-api-2.0.9.jar'))
subprocess.run([str(java / 'javac'), '-cp', str(jar), '-d', str(classes),
                str(root / 'syntax-validation/ValidateHandbookSyntax.java')], check=True)
pages = Path(sys.argv[1]) if len(sys.argv) > 1 else root.parent.parent / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
if len(sys.argv) > 2:
    expected = sys.argv[2]
else:
    import json
    manifest = json.loads((root.parent.parent / 'docs/handbook-draft-manifest.json').read_text())
    # English and Simplified Chinese each have the same authoritative page set.
    expected = str(2 * (manifest['article_count'] + manifest['category_count']
                       + manifest['navigation_page_count'] + manifest['reference_directory_count'] + 1))
subprocess.run([str(java / 'java'), '-cp', ':'.join(map(str, [jar, classes, slf4j])),
                'ValidateHandbookSyntax', str(pages), expected], check=True)
