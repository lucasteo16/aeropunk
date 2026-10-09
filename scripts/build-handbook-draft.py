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
# Inventory homes follow the mod's function, not whichever mechanic mentions it.
for entry in entries:
    path = entry['metadata_path']
    if entry['topic'] == 'food.machine-cooking':
        entry['category'] = 'Automation and industry'
    if entry['topic'].startswith('landscapes.'):
        entry['topic'] = 'world.dimensions'
    if path in {'mods/emi-enchanting.pw.toml', 'mods/emi-professions-(emip).pw.toml'}:
        entry.update(category='Player utilities and quality of life', topic='help.search')
    if path == 'mods/villager-names-serilum.pw.toml':
        entry.update(category='Player utilities and quality of life', topic='help.inspect')
    if path == 'mods/trade-refresh.pw.toml':
        entry.update(category='Player utilities and quality of life', topic='help.controls')
    if path in {'mods/easy-anvils.pw.toml', 'mods/create-stuff-additions.pw.toml', 'mods/create-stam1o-tweaks.pw.toml'}:
        entry['category'] = 'Player utilities and quality of life'
    if path == 'mods/create-dragons-plus.pw.toml':
        entry.update(category='Technical reference', topic='technical.libraries')
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

reference_sections = [('help.controls', 'Controls', '操作与按键', 'minecraft:lever', 'Bindings and interface settings', '按键绑定与界面设置'), ('help.search', 'Item recipe', '物品配方', 'minecraft:crafting_table', 'Ingredients, uses and recipe conflicts', '原料、用途与配方冲突'), ('adventure.bosses', 'Bosses', '首领', 'minecraft:dragon_head', 'Encounters, locations and access', '遭遇、位置与进入条件'), ('adventure.creatures', 'Creatures', '生物', 'minecraft:egg', 'Species, variants and habitats', '种类、变种与栖息地'), ('adventure.structures', 'Structures and dungeons', '结构与地牢', 'minecraft:stone_bricks', 'Locations, families and variants', '位置、类型与变体'), ('world.dimensions', 'Dimensions', '维度', 'minecraft:grass_block', 'Overworld, Nether and End', '主世界、下界与末地'), ('reference.equipment', 'Equipment', '装备', 'minecraft:iron_chestplate', 'Weapons, armor and accessories', '武器、护甲与饰品'), ('reference.skills', 'Spells and skills', '法术与技能', 'minecraft:enchanted_book', 'Combat styles, spells and skill systems', '战斗风格、法术与技能系统'), ('reference.food', 'Food and farming', '食物与农业', 'minecraft:apple', 'Ingredients, dishes and crops', '食材、料理与作物'), ('reference.building', 'Building', '建筑', 'minecraft:bricks', 'Materials, shapes and furniture', '材料、形状与家具'), ('reference.vehicles', 'Vehicles and travel', '载具与旅行', 'minecraft:minecart', 'Components, transport and destinations', '组件、交通与目的地'), ('reference.machines-storage', 'Machines and storage', '机器与储存', 'create:crushing_wheel', 'Machines, power, resources and containers', '机器、动力、资源与容器'), ('maps.personal', 'Maps', '地图', 'minecraft:map', 'World maps, waypoints and finders', '世界地图、路标与查找工具')]
reference_hubs = {'reference.equipment': ('Combat and character', ['equipment.weapons-armor', 'equipment.accessories', 'equipment.display']), 'reference.skills': ('Combat and character', ['combat.handling', 'combat.martial', 'combat.magic', 'combat.skills']), 'reference.food': ('Food and farming', ['food.hunger', 'food.utensils', 'food.nether', 'food.end', 'food.underground', 'food.encounters', 'food.machine-cooking', 'food.growing', 'food.fishing']), 'reference.building': ('Building and decoration', ['building.palette', 'building.factory', 'building.copycats', 'building.architecture', 'building.furniture', 'building.displays', 'building.placement', 'building.safety']), 'reference.vehicles': ('Vehicles and travel', ['vehicles.assembly', 'vehicles.airships', 'vehicles.engines', 'vehicles.controls', 'vehicles.radar', 'vehicles.weapons', 'vehicles.water', 'transport.passenger', 'transport.railway-builder', 'transport.local', 'travel.destinations', 'travel.moving-destinations']), 'reference.machines-storage': ('Automation and industry', ['storage.portable', 'storage.bulk', 'storage.handling', 'machines.ore-processing', 'machines.rotation', 'machines.logistics', 'machines.renewables', 'machines.enchanting', 'machines.trading', 'machines.miscellaneous', 'power.electricity', 'power.industry', 'power.burners', 'power.stored-rotation'])}

short_reference_titles = {'adventure.structures': 'Structures', 'reference.skills': 'Spells & skills', 'reference.food': 'Food & farming', 'reference.vehicles': 'Vehicles', 'reference.machines-storage': 'Machines & storage', 'help.controls': 'Controls'}
reference_sections = [(topic, short_reference_titles.get(topic, english), chinese, icon, role, zh_role) for topic, english, chinese, icon, role, zh_role in reference_sections]
reference_icons = {topic: icon for topic, _, _, icon, *_ in reference_sections}
short_category_titles = {'automation': 'Automation', 'storage': 'Storage & logistics', 'food': 'Food & farming', 'building': 'Building', 'travel': 'Vehicles', 'combat': 'Combat & skills', 'exploration': 'Exploration', 'utilities': 'Utilities', 'visuals': 'Visuals & sound', 'technical': 'Technical'}

reference_parents = {topic: 'quick-reference.md' for topic, *_ in reference_sections}
for hub, (_, topics) in reference_hubs.items():
    for topic in topics:
        reference_parents[topic] = hub + '.md'
for topic in ('maps.shared', 'maps.find'):
    reference_parents[topic] = 'maps.personal.md'
for topic in ('adventure.settlements', 'adventure.loot'):
    reference_parents[topic] = 'adventure.structures.md'


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
page_defs = [p for p in coverage['pages'] if not p['page_id'].startswith('landscapes.') ] + [dict(page_id='help.handbook', title='Astropunk handbook', player_questions=[]), dict(page_id='world.dimensions', title='Dimensions', player_questions=[])]
page_defs += [dict(page_id=topic, title=english, player_questions=[]) for topic, english, *_ in reference_sections if topic in reference_hubs]
for topic, english, chinese_title, *_ in reference_sections:
    zh_titles[topic] = chinese_title
titles = {p['page_id']: p['title'] for p in page_defs}
titles.update({topic: english for topic, english, *_ in reference_sections})
titles.update({'help.search':'Item recipe', 'help.controls':'Controls', 'machines.ore-processing':'Ore processing', 'food.utensils':'Cooking tools', 'food.hunger':'Hunger and food variety', 'storage.portable':'Portable storage', 'travel.destinations':'Teleportation', 'building.copycats':'Copycat shapes', 'interactions.carry':'Carry On', 'visuals.lighting':'Lighting and distant terrain', 'combat.skills':'Character skills', 'maps.find':'Biome and structure finders', 'machines.rotation':'Rotational power', 'machines.renewables':'Renewable resources', 'machines.enchanting':'Automated enchanting', 'machines.trading':'Automated trading', 'machines.miscellaneous':'Workshop tools', 'power.electricity':'Electricity', 'power.industry':'Industrial materials and fuels', 'power.burners':'Liquid burner fuels', 'power.stored-rotation':'Rotational storage', 'food.machine-cooking':'Machine cooking'})
for topic, title in titles.items():
    for verb in ('Find ', 'Explore ', 'Choose ', 'Use ', 'Understand ', 'Read ', 'Look up ', 'Learn about '):
        if title.startswith(verb):
            title = title[len(verb):]
            break
    titles[topic] = title[:1].upper() + title[1:]

titles.update({'help.inspect': 'Block & mob info', 'help.reference': 'Existing help', 'help.handbook': 'Handbook', 'food.hunger': 'Hunger & variety', 'food.utensils': 'Cooking tools', 'food.nether': 'Nether food', 'food.end': 'End food', 'food.underground': 'Underground food', 'food.encounters': 'Encounter food', 'food.machine-cooking': 'Machine cooking', 'food.growing': 'Farming', 'food.fishing': 'Fishing', 'storage.portable': 'Portable storage', 'storage.bulk': 'Bulk storage', 'storage.handling': 'Inventory tools', 'machines.ore-processing': 'Ore processing', 'machines.rotation': 'Rotational power', 'machines.logistics': 'Item routing', 'machines.renewables': 'Renewable resources', 'machines.enchanting': 'Enchanting', 'machines.trading': 'Trading', 'machines.miscellaneous': 'Workshop tools', 'power.electricity': 'Electricity', 'power.industry': 'Materials & fuels', 'power.burners': 'Liquid fuels', 'power.stored-rotation': 'Stored rotation', 'vehicles.assembly': 'Vehicle assembly', 'vehicles.airships': 'Airships', 'vehicles.engines': 'Engines', 'vehicles.controls': 'Vehicle controls', 'vehicles.radar': 'Radar', 'vehicles.weapons': 'Mounted weapons', 'vehicles.water': 'Boats & submarines', 'transport.passenger': 'Train travel', 'transport.railway-builder': 'Railways', 'transport.local': 'Local transport', 'travel.destinations': 'Teleportation', 'travel.moving-destinations': 'Moving destinations', 'maps.shared': 'Shared maps', 'maps.find': 'Location finders', 'adventure.loot': 'Loot', 'adventure.recovery': 'Death & recovery', 'adventure.sleep': 'Sleep', 'adventure.settlements': 'Settlements', 'combat.handling': 'Weapons & dodging', 'combat.martial': 'Martial classes', 'combat.magic': 'Magic classes', 'combat.skills': 'Character skills', 'equipment.weapons-armor': 'Weapons & armor', 'equipment.accessories': 'Accessories', 'equipment.display': 'Armor & status', 'building.palette': 'Materials', 'building.factory': 'Factory decor', 'building.copycats': 'Copycat shapes', 'building.architecture': 'Architecture', 'building.furniture': 'Furniture', 'building.displays': 'Displays', 'building.placement': 'Placement tools', 'building.safety': 'Lighting & safety', 'interactions.carry': 'Carry On', 'visuals.camera': 'Camera', 'visuals.models': 'Models & animations', 'visuals.weather': 'Weather & particles', 'visuals.lighting': 'Lighting & distance', 'visuals.resource-packs': 'Resource packs', 'visuals.shader-packs': 'Shaders', 'sounds.ambience': 'Sound', 'visuals.interface': 'Interface', 'space.destinations': 'Space (not installed)', 'space.vehicle-transfer': 'Space transport', 'performance.baseline': 'Performance', 'performance.deferred': 'Deferred optimizers', 'server.tools': 'Server tools', 'server.deferred-pack-loading': 'Deferred loading', 'technical.bridges': 'Compatibility', 'technical.space-bridge': 'Space compatibility', 'technical.libraries': 'Libraries'})

zh_titles['help.search'] = '物品配方'

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

def write_page(filename, title, body, chinese, parent=None, icon=None, associations=None, position=0):
    front = '---\nnavigation:\n  title: ' + json.dumps(title, ensure_ascii=False) + '\n'
    front += '  position: ' + str(position) + '\n'
    if parent:
        front += '  parent: ' + parent + '\n'
    if icon:
        front += '  icon: ' + icon + '\n'
    if associations:
        front += 'item_ids:\n' + ''.join('  - ' + item + '\n' for item in associations)
    body = body.strip()
    if not body.startswith('## '):
        body = '## ' + ('概览' if chinese else 'Overview') + '\n\n' + body
    text = front + '---\n\n# ' + title + '\n\n' + body + '\n'
    out = PAGES / ('_zh_cn' if chinese else '') / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    # Avoid unnecessary reloads and never let the watcher read a half-written page.
    if not out.exists() or out.read_text() != text:
        temporary = out.with_suffix('.md.tmp')
        temporary.write_text(text)
        temporary.replace(out)

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
    # A mechanic can reference utility mods without giving them an automation inventory home.
    if topic in reference_hubs:
        category_name = reference_hubs[topic][0]
    cat = category_by_name[category_name]
    authored = topic in written or topic in reference_hubs
    deferred = bool(members) and all(e['availability'] == 'deferred' for e in members)
    status.append(dict(topic=topic, category=category_name, filename=topic+'.md', drafted=authored, page_type='directory' if topic in reference_hubs else 'article', deferred=deferred, metadata_paths=[e['metadata_path'] for e in members]))
    for chinese in (False, True):
        title = zh_titles[topic] if chinese else titles[topic]
        body = written[topic]['zh_cn' if chinese else 'en_us'] if topic in written else '编写中（WIP）。' if chinese else 'Work in progress (WIP).'
        if topic in reference_hubs and topic not in written:
            body = '## ' + ('内容目录' if chinese else 'Contents') + '\n\n'
            body += '| 主题 | 状态 |\n| --- | --- |\n' if chinese else '| Topic | Status |\n| --- | --- |\n'
            for child in reference_hubs[topic][1]:
                label = zh_titles[child] if chinese else titles[child]
                state = ('参考' if chinese else 'Reference') if child in written else 'WIP'
                body += '| [' + label + '](' + child + '.md) | ' + state + ' |\n'
        if members and topic != 'world.dimensions' and topic not in reference_parents:
            body += '\n\n## ' + ('相关模组' if chinese else 'Related mods') + '\n\n' + roster(members, chinese)
        # The toolbar already provides history navigation. Avoid duplicate footer links.
        write_page(topic+'.md', title, body, chinese, reference_parents.get(topic, 'category-'+cat[0]+'.md'), icon=reference_icons.get(topic, reference_icons.get(reference_parents.get(topic, '').removesuffix('.md'), cat[3])), associations=associations.get(topic), position=next((i for i, ref in enumerate(reference_sections) if ref[0] == topic), 0))
    assigned_paths += [e['metadata_path'] for e in members]

for cat in categories:
    articles = [s for s in status if s['category'] == cat[1]]
    installed = [e for e in entries if e['category'] == cat[1] and e['availability'] == 'baseline']
    optional = [e for e in entries if e['category'] == cat[1] and e['availability'] != 'baseline']
    for chinese in (False, True):
        title = cat[2] if chinese else short_category_titles[cat[0]]
        body = '## ' + ('主题目录' if chinese else 'Contents') + '\n\n'
        body += '| 主题 | 状态 |\n| --- | --- |\n' if chinese else '| Topic | Status |\n| --- | --- |\n'
        for article in articles:
            label = zh_titles[article['topic']] if chinese else titles[article['topic']]
            state = ('参考' if chinese else 'Reference') if article['drafted'] else 'WIP'
            body += '| [' + label + '](' + article['filename'] + ') | ' + state + ' |\n'
        body += '\n## ' + ({'automation':'自动化模组','storage':'仓储模组','food':'食物与农业模组','building':'建筑模组','travel':'载具与旅行模组','combat':'战斗与角色模组','exploration':'探索模组','utilities':'实用工具模组','visuals':'视觉与音效模组','technical':'技术组件'}[cat[0]] if chinese else {'automation':'Automation Mods','storage':'Storage Mods','food':'Food and Farming Mods','building':'Building Mods','travel':'Vehicle and Travel Mods','combat':'Combat and Character Mods','exploration':'Exploration Mods','utilities':'Player Utility Mods','visuals':'Visual and Sound Mods','technical':'Technical Components'}[cat[0]]) + '\n\n' + roster(installed, chinese, linked=True)
        if optional:
            body += '\n\n## ' + ('其他版本与未安装内容' if chinese else 'Other editions and uninstalled content') + '\n\n' + roster(optional, chinese, linked=True)
        if cat[0] == 'automation':
            body = written['category-automation']['zh_cn' if chinese else 'en_us'] + '\n\n***\n\n' + body.split('\n## ', 1)[0].replace('## 主题目录', '## 机制指南').replace('## Contents', '## Mechanics')
        else:
            contents, mod_tables = body.split('\n## ', 1)
            body = '## ' + mod_tables + '\n\n***\n\n' + contents.replace('## Contents', '## Topics').replace('## 主题目录', '## 主题')
        write_page('category-'+cat[0]+'.md', title, body, chinese, parent='mod-catalogs.md', icon=cat[3], position=categories.index(cat))

for chinese in (False, True):
    body = '## ' + ('模组目录' if chinese else 'Mod catalogs') + '\n\n'
    body += '| 领域 | 内容 |\n| --- | --- |\n' if chinese else '| Area | Contents |\n| --- | --- |\n'
    brief_en = {'automation':'Machines, power and processing', 'storage':'Containers and material routing', 'food':'Ingredients, kitchens and crops', 'building':'Materials, shapes and furniture', 'travel':'Ships, trains and teleportation', 'combat':'Equipment, skills and spells', 'exploration':'Dimensions, landscapes and encounters', 'utilities':'Controls and everyday interactions', 'visuals':'Appearance, shaders and audio', 'technical':'Libraries, performance and administration'}
    brief_zh = {'automation':'机器、动力与加工', 'storage':'容器与物品输送', 'food':'食材、厨房与作物', 'building':'材料、形状与家具', 'travel':'船只、列车与传送', 'combat':'装备、技能与法术', 'exploration':'维度、地形与遭遇', 'utilities':'按键与日常交互', 'visuals':'外观、光影与声音', 'technical':'支持库、性能与管理'}
    for cat in categories:
        slot = '<ItemImage id="' + cat[3] + '" />'
        body += '| ' + slot + ' [' + (cat[2] if chinese else short_category_titles[cat[0]]) + '](category-' + cat[0] + '.md) | ' + (brief_zh if chinese else brief_en)[cat[0]] + ' |\n'
    catalogs_body = body
    body = '## ' + ('快速参考' if chinese else 'Quick reference') + '\n\n'
    body += '| 参考 | 内容 |\n| --- | --- |\n' if chinese else '| Reference | Contents |\n| --- | --- |\n'
    reference = reference_sections
    for topic, english, chinese_name, icon, english_role, chinese_role in reference:
        slot = '<ItemImage id="' + icon + '" />'
        body += '| ' + slot + ' [' + (chinese_name if chinese else english) + '](' + topic + '.md) | ' + (chinese_role if chinese else english_role) + ' |\n'
    write_page('quick-reference.md', '快速参考' if chinese else 'Quick reference', body, chinese, icon='minecraft:book', position=0)
    write_page('mod-catalogs.md', '模组目录' if chinese else 'Mod catalogs', catalogs_body, chinese, icon='minecraft:bookshelf', position=1)
    body += '\n***\n\n' + catalogs_body
    write_page('index.md', 'Astropunk', body, chinese, position=-100)

actual = {p.relative_to(ROOT).as_posix() for folder in ('mods', 'resourcepacks', 'shaderpacks') for p in (ROOT / folder).glob('*.pw.toml')} | {'mods/astropunk-handbook-access-1.0.0.jar'}
assert len(assigned_paths) == len(set(assigned_paths)), 'Duplicate primary coverage'
covered = {e['metadata_path'] for e in entries if e['availability'] == 'baseline'}
assert actual == covered, {'missing': sorted(actual - covered), 'unexpected': sorted(covered - actual)}
assert set(assigned_paths) == {e['metadata_path'] for e in entries}
manifest = {'draft_articles': sum(s['drafted'] and s['page_type'] == 'article' for s in status), 'article_count': sum(s['page_type'] == 'article' for s in status), 'category_count': len(categories), 'navigation_page_count': 2, 'reference_section_count': len(reference_sections), 'reference_directory_count': len(reference_hubs), 'installed_content_count': len(actual), 'heavy_content_count': sum(e['availability'] == 'heavy' for e in entries), 'baseline_commit': '34cb006', 'deferred_content_count': sum(e['availability'] == 'deferred' for e in entries), 'pages': status, 'content': entries}
(ROOT / 'docs/handbook-draft-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in manifest.items() if k not in ('pages','content')}, indent=2))
