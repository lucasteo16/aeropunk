#!/usr/bin/env python3
"""Apply a refurbishment worker fragment to the authoritative handbook content.

The fragment is normalised before it is written, so a worker that writes icon
tags without the canonical spacing, leaves an empty grid, or leaves a text only
section cannot silently reach the guide.

Usage: python scripts/apply_refurbish_fragment.py build/refurb-food/worker-a.json --batch food
"""
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'docs/handbook-content.json'
SCOPE = ROOT / 'docs/handbook-refurbish-scope.json'
GRID = re.compile(r'<ItemGrid>(.*?)</ItemGrid>', re.S)
ICON = re.compile(r'<ItemIcon\b[^>]*\bid="([^"]+)"[^>]*/>')
VISUAL = re.compile(r'(!\[|<ItemGrid|<ItemImage|<GameScene|<Recipe|<BlockImage|^\| --- \|)', re.M)
LINK_LIST = re.compile(r'^(Related topics|相关主题|相关页面)$')


def canonical(body):
    def grid(match):
        icons = ICON.findall(match.group(1))
        return '<ItemGrid>' + ''.join('<ItemIcon id="%s" />' % icon for icon in icons) + '</ItemGrid>'
    body = re.sub(GRID, grid, body)
    body = re.sub(ICON, lambda m: '<ItemIcon id="%s" />' % m.group(1), body)
    parts = re.split(r'(?m)^(## .*)$', body)
    out = [parts[0]]
    for index in range(1, len(parts), 2):
        heading, section = parts[index], parts[index + 1]
        if LINK_LIST.match(heading[3:].strip()):
            bullets = '\n'.join(line for line in section.splitlines() if line.startswith('- '))
            if bullets:
                out.append(out.pop().rstrip() + '\n\n' + bullets + '\n')
                continue
        out.append(heading)
        out.append(section)
    return re.sub(r'\n{3,}', '\n\n', ''.join(out))


def problems(topic, locale, body):
    found = []
    if not body.startswith('## '):
        found.append('body does not start with a section heading')
    for grid in GRID.findall(body):
        if not ICON.findall(grid):
            found.append('empty item grid')
        elif re.sub(r'<ItemIcon id="[^"]+" />', '', grid).strip():
            found.append('grid holds non item children')
    prose = re.sub(r'<[^>]+>', '', re.sub(r'https?://\S+', '', body))
    if re.search(r'[\u2013\u2014;；]', prose):
        found.append('banned character in prose')
    parts = re.split(r'(?m)^(## .*)$', body)
    for index in range(1, len(parts), 2):
        content = '\n'.join(line for line in parts[index + 1].splitlines()
                            if not line.startswith('![YouTube]'))
        if content.strip() and not VISUAL.search(content):
            found.append('text only section: ' + parts[index])
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fragment')
    parser.add_argument('--batch', required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    fragment = json.loads(Path(args.fragment).read_text())
    content = json.loads(CONTENT.read_text())
    failures = []
    cleaned = {}
    for topic, locales in fragment.items():
        if topic not in content:
            failures.append((topic, 'unknown topic'))
            continue
        cleaned[topic] = {}
        for locale, body in locales.items():
            fixed = canonical(body)
            cleaned[topic][locale] = fixed
            for problem in problems(topic, locale, fixed):
                failures.append((topic + ' ' + locale, problem))
    if failures:
        for topic, problem in failures:
            print('FAIL', topic, problem)
        print('refusing to write while problems remain')
        return 1
    if not args.dry_run:
        content.update(cleaned)
        CONTENT.write_text(json.dumps(content, indent=2, ensure_ascii=False) + '\n')
        scope = json.loads(SCOPE.read_text())
        batch = scope['batches'].setdefault(args.batch, {'branch': '', 'topics': []})
        batch['topics'] = sorted(set(batch['topics']) | set(cleaned))
        SCOPE.write_text(json.dumps(scope, indent=2, ensure_ascii=False) + '\n')
    print('applied', len(cleaned), 'topics to batch', args.batch)
    return 0


if __name__ == '__main__':
    sys.exit(main())
