#!/usr/bin/env python3
"""Audit one handbook chapter for the refurbishment bar.

Reports text-only sections, style violations, visual density and repeated grids.
Exits nonzero when a blocking problem exists, so a batch cannot be called done
while one remains.

Usage: python scripts/audit_handbook_chapter.py reference.food.md
"""
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
CONTENT = ROOT / 'docs/handbook-content.json'
VISUAL = re.compile(r'(!\[|<ItemGrid|<ItemImage|<GameScene|<Recipe|<BlockImage)', re.M)
BANNED = re.compile(r'[\u2013\u2014]')
SECTION = re.compile(r'(?m)^(## .*)$')


def chapter_pages(root_page):
    parent, title = {}, {}
    for page in PAGES.glob('*.md'):
        text = page.read_text()
        match = re.search(r'^  parent: (.+)$', text, re.M)
        parent[page.name] = match.group(1).strip('"') if match else None
        heading = re.search(r'^  title: (.+)$', text, re.M)
        title[page.name] = json.loads(heading.group(1)) if heading else page.name

    def root_of(name):
        seen = set()
        while parent.get(name) and name not in seen:
            seen.add(name)
            name = parent[name]
        return name

    return sorted(n for n in parent if root_of(n) == root_page), title


def audit(topic):
    body = json.loads(CONTENT.read_text()).get(topic, {}).get('en_us', '')
    if not body:
        return {'topic': topic, 'missing': True, 'blocking': ['missing authored body']}
    sections = SECTION.split(body)
    problems, text_only, empty = [], [], []
    for index in range(1, len(sections), 2):
        heading = sections[index][3:].strip()
        content = '\n'.join(line for line in sections[index + 1].splitlines()
                            if not line.startswith('![YouTube]'))
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        if lines and all(re.fullmatch(r'- \[.*\]\(.*\)', line) for line in lines):
            continue  # category index navigation, not authored prose
        if not content.strip():
            empty.append(heading)
        elif not VISUAL.search(content):
            text_only.append(heading)
    for match in re.finditer(r'<ItemGrid>(.*?)</ItemGrid>', body, re.S):
        inner = re.sub(r'<ItemIcon id="[^"]+" />', '', match.group(1))
        if inner.strip():
            problems.append('grid contains non item children')
    prose = re.sub(r'<[^>]+>', '', re.sub(r'https?://\S+', '', body))
    for match in BANNED.finditer(prose):
        problems.append('banned dash at character ' + str(match.start()))
    if ';' in prose or '；' in prose:
        problems.append('semicolon in prose')
    visuals = len(VISUAL.findall(body))
    return {
        'topic': topic,
        'characters': len(body),
        'visuals': visuals,
        'density': round(visuals * 1000 / max(len(body), 1), 1),
        'text_only_sections': text_only,
        'empty_sections': empty,
        'problems': problems,
        'blocking': text_only + problems + empty,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('chapter')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    topics, title = chapter_pages(args.chapter)
    topics = [t[:-3] if t.endswith('.md') else t for t in topics]
    rows = [audit(t) for t in topics]
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        print(f"{'page':26s} {'chars':>6s} {'visuals':>7s} {'density':>7s}  blocking")
        for row in rows:
            problems = ','.join(row.get('blocking', []))
            print(f"{title.get(row['topic'] + '.md', row['topic'])[:26]:26s} {row.get('characters', 0):6d} "
                  f"{row.get('visuals', 0):7d} {row.get('density', 0):7.1f}  {problems[:60]}")
    blocked = [row for row in rows if row.get('blocking')]
    print(f"\nchapter {args.chapter}: {len(rows)} pages, {len(blocked)} blocking")
    return 1 if blocked else 0


if __name__ == '__main__':
    sys.exit(main())
