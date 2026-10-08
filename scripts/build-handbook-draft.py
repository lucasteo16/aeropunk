"""Build the bilingual handbook skeleton from the reconciled coverage checklist."""
from pathlib import Path
from collections import defaultdict, Counter
import json
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / 'resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook'
coverage = json.loads((ROOT / 'docs/guide-coverage.json').read_text())
checklist = json.loads((ROOT / 'docs/guide-authoring-checklist.json').read_text())
entries = checklist['entries']
# Retain optional-edition references, but never describe absent heavy content as installed.
entries = [dict(e, availability='heavy') if e['availability'] == 'baseline' and not (ROOT / e['metadata_path']).is_file() else e for e in entries]
# GuideME was added after the original inventory snapshot.
entries = entries + [dict(metadata_path='mods/guideme.pw.toml', name='GuideME', availability='baseline', category='Technical reference', topic='help.handbook'), dict(metadata_path='mods/astropunk-handbook-access-1.0.0.jar', name='Astropunk Handbook Access', availability='baseline', category='Player utilities and quality of life', topic='help.controls')]
for entry in entries:
    if entry['topic'] == 'food.machine-cooking':
        entry['category'] = 'Automation and industry'
by_topic = defaultdict(list)
for entry in entries:
    by_topic[entry['topic']].append(entry)

categories = [
('automation', 'Automation and industry', '自动化与工业', 'create:crushing_wheel', 'Find machines for processing materials, making power and doing repetitive work.', '寻找加工原料、提供动力和代替重复劳动的机器。'),
('storage', 'Storage and logistics', '仓储与物流', 'minecraft:chest', 'Choose storage, then decide how items reach their destination.', '先选择储存方式，再决定物品如何到达目的地。'),
('food', 'Food and farming', '食物与农业', 'minecraft:wheat', 'Discover ingredients, cooking tools and reasons to vary your meals.', '了解食材、烹饪工具，以及丰富饮食的作用。'),
('building', 'Building and decoration', '建筑与装饰', 'minecraft:bricks', 'Find materials, shapes and tools for the build you have in mind.', '寻找适合你的建筑构想的材料、形状和工具。'),
('travel', 'Vehicles and travel', '载具与旅行', 'minecraft:minecart', 'Choose how to travel, from shared transport to a vehicle of your own.', '选择出行方式，可以乘坐公共交通，也可以建造自己的载具。'),
('combat', 'Combat and character', '战斗与角色', 'minecraft:iron_sword', 'Explore equipment, combat roles and character choices.', '了解装备、战斗风格和角色培养选择。'),
('exploration', 'Exploration and adventure', '探索与冒险', 'minecraft:compass', 'Find landscapes, settlements, dungeons and encounters worth a trip.', '寻找值得出发探索的地形、聚落、地牢和遭遇。'),
('utilities', 'Player utilities and quality of life', '实用工具与便利功能', 'minecraft:white_bed', 'Find everyday help with controls, interactions, sleep and recovery.', '寻找按键、交互、睡眠和死亡后恢复方面的日常帮助。'),
('visuals', 'Visuals and sound', '视觉与音效', 'minecraft:painting', 'Choose how the game looks and sounds on your machine.', '根据你的电脑和喜好选择画面与声音效果。'),
('technical', 'Technical reference', '技术参考', 'minecraft:redstone', 'Look up supporting libraries, optimization and administrator tools.', '查询支持库、性能优化和管理员工具。'),
]
category_by_name = {c[1]: c for c in categories}

raw_zh_titles = '''help.search|查找物品、配方与用途
help.inspect|查看方块与生物信息
help.controls|查找和修改按键
help.reference|查找已有演示与帮助界面
help.handbook|Astropunk 手册
food.hunger|饥饿、饮食多样性与食物携带
food.utensils|用烹饪工具准备食物
food.nether|用下界食材烹饪
food.end|用末地食材烹饪
food.underground|用地下食材烹饪
food.encounters|用特殊遭遇获得的食材烹饪
food.machine-cooking|用机器制作食物
food.growing|种植与收获食材
food.fishing|钓鱼与水产食材
storage.portable|携带便携储存装备
storage.bulk|储存工厂的大批原料
storage.handling|整理、转移与丢弃物品
machines.ore-processing|加工矿石与原料
machines.rotation|为机器提供旋转动力
machines.logistics|输送、筛选与分配物品
machines.renewables|生产可再生原料
machines.enchanting|附魔、修理与查看装备
machines.trading|手动交易与自动交易
machines.miscellaneous|寻找其他工厂工具
power.electricity|发电、配电与用电
power.industry|工业材料与燃料系统
power.burners|提供液体燃烧燃料
power.stored-rotation|储存旋转动力
vehicles.assembly|组装和操作移动载具
vehicles.airships|建造与平衡飞行船
vehicles.engines|选择引擎与推进装置
vehicles.controls|控制与稳定载具
vehicles.radar|读取雷达信息
vehicles.weapons|安装和操作载具武器
vehicles.water|操作船只与潜艇
transport.passenger|乘坐列车出行
transport.railway-builder|建造列车、轨道与车站
transport.local|在基地内移动
travel.destinations|使用固定与便携传送点
travel.moving-destinations|前往移动建筑上的目的地
maps.personal|阅读地图与标记目的地
maps.shared|共享地图信息
maps.find|寻找生物群系与结构
adventure.loot|分享与查看探险战利品
adventure.recovery|死亡后取回物品
adventure.sleep|睡眠与时间安排
adventure.settlements|探索聚落与法术图书馆
adventure.structures|探索地牢与改造后的结构
adventure.creatures|认识野外生物
adventure.bosses|选择具有挑战性的遭遇
combat.handling|使用武器与闪避
combat.martial|选择近战与远程战斗风格
combat.magic|选择法术与支援风格
combat.skills|通过技能培养角色
equipment.weapons-armor|选择武器与护甲
equipment.accessories|使用饰品、遗物与饰品栏
equipment.display|阅读护甲与状态信息
building.palette|选择装饰材料
building.factory|装饰工厂与车站
building.copycats|使用模仿材料的建筑形状
building.architecture|建造桥梁、屋顶与围栏
building.furniture|布置住宅与公共空间
building.displays|制作展示、画作、标牌与雕像
building.placement|使用随机放置与蓝图工具
building.safety|查看照明与管理刷怪
interactions.carry|搬运方块与生物
visuals.camera|调整视角与窗口
visuals.models|调整模型与动画
visuals.weather|调整天气、粒子与过渡效果
visuals.lighting|选择光影、动态光源与远景
visuals.resource-packs|选择资源包外观
visuals.shader-packs|比较光影风格
sounds.ambience|调整声音与环境声学
visuals.interface|调整通知与信息界面
landscapes.overworld|探索主世界地形与河流
landscapes.nether|探索下界地形
landscapes.end|探索末地地形
space.destinations|了解规划中的太空目的地
space.vehicle-transfer|了解整台载具的跨维度移动
performance.baseline|了解当前性能优化系统
performance.deferred|了解暂缓加入的优化模组
server.tools|了解管理员与诊断工具
server.deferred-pack-loading|了解暂缓加入的内容加载工具
technical.bridges|查询移动建筑与视觉兼容组件
technical.space-bridge|查询暂缓加入的太空渲染组件
technical.libraries|查询支持库与框架'''
zh_titles: dict[str, str] = {line.split('|', 1)[0]: line.split('|', 1)[1] for line in raw_zh_titles.splitlines()}

# Authored articles are maintained separately from generated indexes.
written = json.loads((ROOT / 'docs/handbook-content.json').read_text())
descriptions = json.loads((ROOT / 'docs/handbook-project-descriptions.json').read_text())
zh_titles['world.dimensions'] = '维度目录'
page_defs = list(coverage['pages']) + [dict(page_id='help.handbook', title='Astropunk handbook', player_questions=[]), dict(page_id='world.dimensions', title='Dimensions', player_questions=[])]
titles = {p['page_id']: p['title'] for p in page_defs}
titles.update({'help.search':'Items and recipes', 'help.controls':'Controls and key bindings', 'machines.ore-processing':'Ore processing', 'food.utensils':'Cooking tools', 'food.hunger':'Hunger and food variety', 'storage.portable':'Portable storage', 'travel.destinations':'Teleportation', 'building.copycats':'Copycat shapes', 'interactions.carry':'Carry On', 'visuals.lighting':'Lighting and distant terrain', 'combat.skills':'Character skills', 'maps.find':'Biome and structure finders'})
for topic, title in titles.items():
    for verb in ('Find ', 'Explore ', 'Choose ', 'Use ', 'Understand ', 'Read ', 'Look up ', 'Learn about '):
        if title.startswith(verb):
            title = title[len(verb):]
            break
    titles[topic] = title[:1].upper() + title[1:]

written['world.dimensions'] = {
'en_us': '''| Dimension | Catalog |
| --- | --- |
| Overworld | [Landscapes and rivers](landscapes.overworld.md) |
| Nether | [Nether landscapes](landscapes.nether.md) |
| End | [End landscapes](landscapes.end.md) |

<ItemGrid>
  <ItemIcon id="minecraft:grass_block" />
  <ItemIcon id="minecraft:netherrack" />
  <ItemIcon id="minecraft:end_stone" />
</ItemGrid>

The light edition uses the three vanilla dimensions. Space content is not installed. [Space reference](space.destinations.md) lists that separate content.''',
'zh_cn': '''| 维度 | 目录 |
| --- | --- |
| 主世界 | [地形与河流](landscapes.overworld.md) |
| 下界 | [下界地形](landscapes.nether.md) |
| 末地 | [末地地形](landscapes.end.md) |

<ItemGrid>
  <ItemIcon id="minecraft:grass_block" />
  <ItemIcon id="minecraft:netherrack" />
  <ItemIcon id="minecraft:end_stone" />
</ItemGrid>

轻量版使用三个原版维度，当前未安装太空内容。相关独立内容见[太空参考](space.destinations.md)。'''
}

def clean(value):
    return value.replace('|', ',').replace('\n', ' ').replace('—', ', ').replace('–', ' to ')

def description(entry, chinese):
    data = descriptions.get(entry['metadata_path'])
    if data:
        return clean(data['description'])
    if entry['name'] == 'Astropunk Handbook Access':
        return '物品栏手册按钮与可配置快捷键。' if chinese else 'Inventory handbook button and configurable opening shortcut.'
    if entry['name'] == 'Short Stacks':
        return '食物堆叠上限随饱腹能力变化。' if chinese else 'Food stack limits vary with filling power.'
    return '当前未安装。' if chinese else 'Not installed here.'

def roster(members, chinese, linked=False):
    header = '| 模组或内容 | 官方简介 |' if chinese else '| Mod or content | Publisher description |'
    rows = [header, '| --- | --- |']
    for entry in sorted(members, key=lambda e: e['name'].lower()):
        name = clean(entry['name'])
        if linked:
            name = '[' + name + '](' + entry['topic'] + '.md)'
        label = ''
        if entry['availability'] == 'heavy':
            label = '（重型版，当前未安装）' if chinese else ' (heavy edition, not installed here)'
        elif entry['availability'] == 'deferred':
            label = '（未安装）' if chinese else ' (not installed)'
        rows.append('| ' + name + label + ' | ' + description(entry, chinese) + ' |')
    return '\n'.join(rows)

def write_page(filename, title, body, chinese, parent=None, icon=None, associations=None):
    front = '---\nnavigation:\n  title: ' + json.dumps(title, ensure_ascii=False) + '\n'
    if parent:
        front += '  parent: ' + parent + '\n'
    if icon:
        front += '  icon: ' + icon + '\n'
    if associations:
        front += 'item_ids:\n' + ''.join('  - ' + item + '\n' for item in associations)
    text = front + '---\n\n# ' + title + '\n\n' + body.strip() + '\n'
    out = PAGES / ('_zh_cn' if chinese else '') / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)

status = []
assigned_paths = []
associations = {
    'machines.ore-processing': ['create:millstone', 'create:crushing_wheel', 'create:encased_fan', 'create:crushed_raw_iron'],
    'food.utensils': ['farmersdelight:cooking_pot', 'farmersdelight:cutting_board', 'farmersdelight:skillet', 'farmersdelight:stove'],
}
for page in page_defs:
    topic = page['page_id']
    members = by_topic[topic]
    counts = Counter(e['category'] for e in members)
    category_name = counts.most_common(1)[0][0] if members else 'Exploration and adventure' if topic == 'world.dimensions' else 'Food and farming' if topic.startswith('food.') else 'Technical reference'
    assert len(counts) <= 1, (topic, counts)
    cat = category_by_name[category_name]
    authored = topic in written
    deferred = bool(members) and all(e['availability'] == 'deferred' for e in members)
    status.append(dict(topic=topic, category=category_name, filename=topic+'.md', drafted=authored, deferred=deferred, metadata_paths=[e['metadata_path'] for e in members]))
    for chinese in (False, True):
        title = zh_titles[topic] if chinese else titles[topic]
        body = written[topic]['zh_cn' if chinese else 'en_us'] if authored else '编写中（WIP）。' if chinese else 'Work in progress (WIP).'
        if members:
            body += '\n\n## ' + ('相关模组' if chinese else 'Related mods') + '\n\n' + roster(members, chinese)
        # The toolbar already provides history navigation. Avoid duplicate footer links.
        write_page(topic+'.md', title, body, chinese, 'category-'+cat[0]+'.md', associations=associations.get(topic))
    assigned_paths += [e['metadata_path'] for e in members]

for cat in categories:
    articles = [s for s in status if s['category'] == cat[1]]
    installed = [e for e in entries if e['category'] == cat[1] and e['availability'] == 'baseline']
    optional = [e for e in entries if e['category'] == cat[1] and e['availability'] != 'baseline']
    for chinese in (False, True):
        title = cat[2] if chinese else cat[1]
        body = '## ' + ('主题目录' if chinese else 'Contents') + '\n\n'
        body += '| 主题 | 状态 |\n| --- | --- |\n' if chinese else '| Topic | Status |\n| --- | --- |\n'
        for article in articles:
            label = zh_titles[article['topic']] if chinese else titles[article['topic']]
            state = ('参考' if chinese else 'Reference') if article['drafted'] else 'WIP'
            body += '| [' + label + '](' + article['filename'] + ') | ' + state + ' |\n'
        body += '\n## ' + ('已安装模组与内容' if chinese else 'Installed mods and content') + '\n\n' + roster(installed, chinese, linked=True)
        if optional:
            body += '\n\n## ' + ('其他版本与未安装内容' if chinese else 'Other editions and uninstalled content') + '\n\n' + roster(optional, chinese, linked=True)
        write_page('category-'+cat[0]+'.md', title, body, chinese, icon=cat[3])

for chinese in (False, True):
    body = ('模组、世界与玩法的参考手册。按领域浏览内容，或查找具体机制。' if chinese else 'A reference to the mods, worlds and mechanics in Astropunk.') + '\n\n'
    body += ('[操作与按键](help.controls.md) · [物品与配方](help.search.md) · [维度目录](world.dimensions.md)' if chinese else '[Controls](help.controls.md) · [Items and recipes](help.search.md) · [Dimensions](world.dimensions.md)') + '\n\n## ' + ('内容目录' if chinese else 'Catalogs') + '\n\n'
    body += '| 领域 | 内容 |\n| --- | --- |\n' if chinese else '| Area | Contents |\n| --- | --- |\n'
    brief_en = {'automation':'Machines, power and processing', 'storage':'Containers and material routing', 'food':'Ingredients, kitchens and crops', 'building':'Materials, shapes and furniture', 'travel':'Ships, trains and teleportation', 'combat':'Equipment, skills and spells', 'exploration':'Dimensions, landscapes and encounters', 'utilities':'Controls and everyday interactions', 'visuals':'Appearance, shaders and audio', 'technical':'Libraries, performance and administration'}
    brief_zh = {'automation':'机器、动力与加工', 'storage':'容器与物品输送', 'food':'食材、厨房与作物', 'building':'材料、形状与家具', 'travel':'船只、列车与传送', 'combat':'装备、技能与法术', 'exploration':'维度、地形与遭遇', 'utilities':'按键与日常交互', 'visuals':'外观、光影与声音', 'technical':'支持库、性能与管理'}
    for cat in categories:
        body += '| [' + (cat[2] if chinese else cat[1]) + '](category-' + cat[0] + '.md) | ' + (brief_zh if chinese else brief_en)[cat[0]] + ' |\n'
    write_page('index.md', 'Astropunk', body, chinese)
    write_page('ore-processing.md', '矿石加工' if chinese else 'Ore processing', '[矿石加工](machines.ore-processing.md)' if chinese else '[Ore processing](machines.ore-processing.md)', chinese)

actual = {p.relative_to(ROOT).as_posix() for folder in ('mods', 'resourcepacks', 'shaderpacks') for p in (ROOT / folder).glob('*.pw.toml')} | {'mods/astropunk-handbook-access-1.0.0.jar'}
assert len(assigned_paths) == len(set(assigned_paths)), 'Duplicate primary coverage'
covered = {e['metadata_path'] for e in entries if e['availability'] == 'baseline'}
assert actual == covered, {'missing': sorted(actual - covered), 'unexpected': sorted(covered - actual)}
assert set(assigned_paths) == {e['metadata_path'] for e in entries}
manifest = {'draft_articles': sum(s['drafted'] for s in status), 'article_count': len(status), 'category_count': len(categories), 'installed_content_count': len(actual), 'heavy_content_count': sum(e['availability'] == 'heavy' for e in entries), 'baseline_commit': '34cb006', 'deferred_content_count': sum(e['availability'] == 'deferred' for e in entries), 'pages': status, 'content': entries}
(ROOT / 'docs/handbook-draft-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in manifest.items() if k not in ('pages','content')}, indent=2))
