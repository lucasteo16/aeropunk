#!/usr/bin/env python3
"""Emit structural content repairs as a fragment, without changing shared source."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]

def repair(topic, locale, body):
    if topic == 'combat.skills':
        # Inline MDX preserves whitespace as MdAstText, unlike block MDX.
        return re.sub(r'<ItemGrid>([^\n]*?)</ItemGrid>',
                      lambda m: '<ItemGrid>' + ''.join(re.findall(r'<ItemIcon\b[^>]*?/>', m[1])) + '</ItemGrid>', body)
    if topic != 'equipment.weapons-armor':
        return body
    header = '| Set | Pieces |' if locale == 'en_us' else '| 套装 | 部件 |'
    body = body.replace(header + '\n| --- | --- |\n', '')
    body = body.replace('Each row shows every piece of one supported set, ordered head, chest, legs and feet.',
                        'Each group shows every piece of one supported set, ordered head, chest, legs and feet.')
    body = body.replace('每行展示该套装的全部部件，依次为头部、胸部、腿部与脚部。',
                        '每组展示该套装的全部部件，依次为头部、胸部、腿部与脚部。')
    def group(match):
        label, contents = match.groups()
        icons = re.findall(r'<ItemIcon\b[^>]*?/>', contents)
        if len(icons) != 4:
            raise AssertionError('Armor group must preserve all four pieces')
        return label.strip() + '\n\n<ItemGrid>\n' + ''.join('  ' + icon + '\n' for icon in icons) + '</ItemGrid>\n'
    return re.sub(r'^\|\s*(<ItemLink\b[^>]*?/>)\s*\|\s*<ItemGrid>(.*?)</ItemGrid>\s*\|\s*$',
                  group, body, flags=re.M)

def fragment(source):
    return {topic: {locale: repair(topic, locale, body) for locale, body in source[topic].items()}
            for topic in ('combat.skills', 'equipment.weapons-armor')}

if __name__ == '__main__':
    source = json.loads((ROOT / 'docs/handbook-content.json').read_text())
    target = ROOT / 'docs/final-review/markup-content.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(fragment(source), ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {target}, two topics in both languages. Shared source unchanged.')
