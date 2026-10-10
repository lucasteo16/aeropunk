"""Build the bilingual handbook skeleton from the reconciled coverage checklist."""
from pathlib import Path
from collections import defaultdict, Counter
import json
import tomllib
import argparse
import re
import html

parser = argparse.ArgumentParser()
parser.add_argument('--content-source', type=Path, help='Read a staged content source without modifying authoritative JSON')
args = parser.parse_args()

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
    if entry['topic'] == 'travel.moving-destinations':
        entry['topic'] = 'travel.destinations'
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
    # Exact verified audio providers and their Sable compatibility addons.
    if path in {'mods/cool-rain-reforged.pw.toml', 'mods/pf-neoforge.pw.toml', 'mods/sable-cool-rain.pw.toml', 'mods/presence-footsteps-x-sable.pw.toml'}:
        entry.update(category='Visuals and sound', topic='sounds.ambience')
    if path == 'mods/create-dragons-plus.pw.toml':
        entry.update(category='Technical reference', topic='technical.libraries')
placement_overrides = json.loads((ROOT / 'docs/handbook-placement-overrides.json').read_text())
assert set(placement_overrides) <= {entry['metadata_path'] for entry in entries}
for entry in entries:
    if placement := placement_overrides.get(entry['metadata_path']):
        # Classification changes do not override availability reconciled above.
        entry.update(category=placement['category'], topic=placement['topic'])
# Consolidate the former Sound article into the first-level Audio page.
for entry in entries:
    if entry['topic'] in {'sounds.ambience', 'audio.sound'}:
        entry['topic'] = 'reference.audio'
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

reference_sections = [('help.controls', 'Controls', '操作与按键', 'minecraft:lever', 'Bindings and interface settings', '按键绑定与界面设置'), ('help.search', 'Browse recipe', '浏览配方', 'minecraft:crafting_table', 'Ingredients, uses and recipe conflicts', '原料、用途与配方冲突'), ('adventure.bosses', 'Bosses', '首领', 'minecraft:dragon_head', 'Encounters, locations and access', '遭遇、位置与进入条件'), ('adventure.creatures', 'Creatures', '生物', 'minecraft:egg', 'Species, variants and habitats', '种类、变种与栖息地'), ('adventure.structures', 'Structures and dungeons', '结构与地牢', 'minecraft:stone_bricks', 'Locations, families and variants', '位置、类型与变体'), ('world.dimensions', 'Dimensions', '维度', 'minecraft:grass_block', 'Overworld, Nether and End', '主世界、下界与末地'), ('reference.equipment', 'Equipment', '装备', 'minecraft:iron_chestplate', 'Weapons, armor and accessories', '武器、护甲与饰品'), ('reference.skills', 'Spells and skills', '法术与技能', 'minecraft:enchanted_book', 'Combat styles, spells and skill systems', '战斗风格、法术与技能系统'), ('reference.food', 'Food and farming', '食物与农业', 'minecraft:apple', 'Ingredients, dishes and crops', '食材、料理与作物'), ('reference.building', 'Building', '建筑', 'minecraft:bricks', 'Materials, shapes and furniture', '材料、形状与家具'), ('reference.vehicles', 'Vehicles and travel', '载具与旅行', 'minecraft:minecart', 'Components, transport and destinations', '组件、交通与目的地'), ('reference.machines-storage', 'Machines and storage', '机器与储存', 'create:crushing_wheel', 'Machines, power, resources and containers', '机器、动力、资源与容器'), ('maps.personal', 'Maps', '地图', 'minecraft:map', 'World maps, waypoints and finders', '世界地图、路标与查找工具')]
reference_hubs = {'reference.equipment': ('Combat and character', ['equipment.weapons-armor', 'equipment.accessories', 'equipment.display']), 'reference.skills': ('Combat and character', ['combat.handling', 'combat.martial', 'combat.magic', 'combat.skills']), 'reference.food': ('Food and farming', ['food.utensils', 'food.hunger', 'food.nether', 'food.end', 'food.underground', 'food.encounters', 'food.machine-cooking', 'food.growing', 'food.fishing']), 'reference.building': ('Building and decoration', ['building.palette', 'building.factory', 'building.copycats', 'building.architecture', 'building.furniture', 'building.displays', 'building.placement', 'building.safety']), 'reference.vehicles': ('Vehicles and travel', ['vehicles.assembly', 'vehicles.airships', 'vehicles.engines', 'vehicles.controls', 'vehicles.radar', 'vehicles.weapons', 'vehicles.water', 'transport.passenger', 'transport.railway-builder', 'transport.local', 'travel.destinations', 'travel.moving-destinations']), 'reference.machines-storage': ('Automation and industry', ['storage.portable', 'storage.bulk', 'storage.handling', 'machines.ore-processing', 'machines.rotation', 'machines.logistics', 'machines.renewables', 'machines.enchanting', 'machines.trading', 'machines.miscellaneous', 'power.electricity', 'power.industry', 'power.burners', 'power.stored-rotation'])}

# Keep stable landing identifiers. Equipment and full abilities are siblings under Combat.
reference_sections = [r for r in reference_sections if r[0] != 'reference.equipment']
reference_sections = [(topic, 'Combat' if topic == 'reference.skills' else english, '战斗' if topic == 'reference.skills' else chinese, 'minecraft:iron_sword' if topic == 'reference.skills' else icon, 'Equipment, classes, spells and character skills' if topic == 'reference.skills' else role, '装备、职业、法术与角色技能' if topic == 'reference.skills' else zh_role) for topic, english, chinese, icon, role, zh_role in reference_sections]
reference_hubs.pop('reference.equipment')
reference_hubs['reference.skills'][1].extend(['reference.equipment', 'combat.abilities', 'equipment.weapons-armor', 'equipment.accessories', 'equipment.display'])

short_reference_titles = {'adventure.structures': 'Structures', 'reference.skills': 'Combat', 'reference.food': 'Food & farming', 'reference.vehicles': 'Transport', 'reference.machines-storage': 'Machines & storage', 'help.controls': 'Controls'}
reference_sections = [(topic, short_reference_titles.get(topic, english), '交通' if topic == 'reference.vehicles' else chinese, icon, role, zh_role) for topic, english, chinese, icon, role, zh_role in reference_sections]
reference_icons = {topic: icon for topic, _, _, icon, *_ in reference_sections}
short_category_titles = {'automation': 'Automation', 'storage': 'Storage & logistics', 'food': 'Food & farming', 'building': 'Building', 'travel': 'Vehicles', 'combat': 'Combat & skills', 'exploration': 'Exploration', 'utilities': 'Utilities', 'visuals': 'Visuals & sound', 'technical': 'Technical'}

# Supplemental topics live in the same tree, not in competing mod catalogs.
reference_sections += [
    ('reference.utilities', 'Utilities', '实用工具', 'minecraft:lever', 'Inspection, interactions, sleep and recovery', '信息查看、交互、睡眠与恢复'),
    ('reference.appearance', 'Appearance', '外观', 'minecraft:painting', 'Camera, models, lighting and resource packs', '视角、模型、光照与资源包'),
    ('reference.audio', 'Audio', '音效', 'minecraft:note_block', 'Ambience, footsteps and weather sounds', '环境声、脚步声与天气音效'),
    ('reference.technical', 'Technical', '技术', 'minecraft:redstone', 'Libraries, performance and administration', '支持库、性能与管理'),
]
reference_hubs.update({
    'reference.utilities': ('Player utilities and quality of life', ['help.inspect', 'interactions.carry', 'adventure.recovery', 'adventure.sleep']),
    'reference.appearance': ('Visuals and sound', ['visuals.camera', 'visuals.models', 'visuals.weather', 'visuals.lighting', 'visuals.resource-packs', 'visuals.shader-packs', 'visuals.interface']),
    'reference.technical': ('Technical reference', ['help.handbook', 'help.reference', 'performance.baseline', 'performance.deferred', 'server.tools', 'server.deferred-pack-loading', 'technical.bridges', 'technical.space-bridge', 'technical.libraries']),
})
reference_hubs['reference.vehicles'] = (reference_hubs['reference.vehicles'][0], [topic for topic in reference_hubs['reference.vehicles'][1] if topic != 'travel.moving-destinations'])
reference_hubs['reference.vehicles'][1].extend(['space.destinations', 'space.vehicle-transfer'])
reference_icons.update({topic: icon for topic, _, _, icon, *_ in reference_sections})
# Explicit whole-tree icons: never inherit a parent's icon for a topic.
# Selected binary registration evidence and topic rationale are recorded in
# docs/final-review/navigation-icon-audit.json. Deferred topics use vanilla
# metaphors, not identifiers from mods that are absent from this pack.
reference_icons = {
    'index': 'minecraft:compass',
    'help.controls': 'minecraft:lever',
    'help.search': 'minecraft:crafting_table',
    'adventure.bosses': 'minecraft:dragon_head',
    'adventure.creatures': 'minecraft:egg',
    'adventure.structures': 'minecraft:stone_bricks',
    'world.dimensions': 'minecraft:grass_block',
    'reference.skills': 'minecraft:iron_sword',
    'reference.food': 'minecraft:bread',
    'reference.building': 'create:schematicannon',
    'reference.vehicles': 'minecraft:minecart',
    'reference.machines-storage': 'create:crushing_wheel',
    'maps.personal': 'minecraft:map',
    'reference.utilities': 'minecraft:chest',
    'reference.appearance': 'minecraft:painting',
    'reference.audio': 'minecraft:note_block',
    'reference.technical': 'minecraft:redstone',
    'reference.equipment': 'minecraft:iron_chestplate',
    'combat.abilities': 'minecraft:enchanted_book',
    'equipment.accessories': 'minecraft:emerald',
    'equipment.display': 'minecraft:potion',
    'combat.skills': 'minecraft:experience_bottle',
    'combat.magic': 'minecraft:blaze_rod',
    'combat.martial': 'minecraft:bow',
    'equipment.weapons-armor': 'minecraft:trident',
    'combat.handling': 'minecraft:feather',
    'food.hunger': 'minecraft:apple',
    'food.utensils': 'farmersdelight:cooking_pot',
    'food.nether': 'minecraft:crimson_fungus',
    'food.end': 'minecraft:chorus_fruit',
    'food.underground': 'minecraft:brown_mushroom',
    'food.encounters': 'minecraft:rotten_flesh',
    'food.machine-cooking': 'minecraft:smoker',
    'food.growing': 'minecraft:wheat',
    'food.fishing': 'minecraft:cod',
    'building.palette': 'chipped:mason_table',
    'building.factory': 'create:industrial_iron_block',
    'building.copycats': 'copycats:copycat_block',
    'building.architecture': 'minecraft:oak_stairs',
    'building.furniture': 'handcrafted:oak_chair',
    'building.displays': 'minecraft:item_frame',
    'building.placement': 'mechtrowel:mech_trowel',
    'building.safety': 'minecraft:torch',
    'storage.portable': 'minecraft:shulker_box',
    'storage.bulk': 'create:item_vault',
    'storage.handling': 'minecraft:bundle',
    'machines.ore-processing': 'create:millstone',
    'machines.rotation': 'create:cogwheel',
    'machines.logistics': 'create:brass_funnel',
    'machines.renewables': 'create:mechanical_drill',
    'machines.enchanting': 'minecraft:enchanting_table',
    'machines.trading': 'minecraft:emerald_block',
    'machines.miscellaneous': 'create:wrench',
    'power.electricity': 'minecraft:lightning_rod',
    'power.industry': 'minecraft:iron_ingot',
    'power.burners': 'minecraft:lava_bucket',
    'power.stored-rotation': 'create:flywheel',
    'vehicles.assembly': 'create:mechanical_bearing',
    'vehicles.airships': 'minecraft:elytra',
    'vehicles.engines': 'create:steam_engine',
    'vehicles.controls': 'create:controls',
    'vehicles.radar': 'minecraft:sculk_sensor',
    'vehicles.weapons': 'minecraft:dispenser',
    'vehicles.water': 'minecraft:oak_boat',
    'transport.passenger': 'minecraft:rail',
    'transport.railway-builder': 'create:track',
    'transport.local': 'minecraft:powered_rail',
    'travel.destinations': 'minecraft:ender_pearl',
    'travel.moving-destinations': 'minecraft:lodestone',
    'space.destinations': 'minecraft:end_stone',
    'space.vehicle-transfer': 'minecraft:end_portal_frame',
    'maps.shared': 'minecraft:cartography_table',
    'maps.find': 'minecraft:spyglass',
    'adventure.settlements': 'minecraft:bell',
    'adventure.loot': 'minecraft:gold_ingot',
    'help.inspect': 'minecraft:debug_stick',
    'help.reference': 'minecraft:book',
    'interactions.carry': 'minecraft:barrel',
    'adventure.recovery': 'minecraft:recovery_compass',
    'adventure.sleep': 'minecraft:white_bed',
    'visuals.camera': 'minecraft:ender_eye',
    'visuals.models': 'minecraft:armor_stand',
    'visuals.weather': 'minecraft:snowball',
    'visuals.lighting': 'minecraft:lantern',
    'visuals.resource-packs': 'minecraft:loom',
    'visuals.shader-packs': 'minecraft:prismarine_crystals',
    'visuals.interface': 'minecraft:oak_sign',
    'help.handbook': 'minecraft:writable_book',
    'help.credits': 'minecraft:written_book',
    'performance.baseline': 'minecraft:clock',
    'performance.deferred': 'minecraft:repeater',
    'server.tools': 'minecraft:command_block',
    'server.deferred-pack-loading': 'minecraft:hopper',
    'technical.bridges': 'minecraft:chain',
    'technical.space-bridge': 'minecraft:end_rod',
    'technical.libraries': 'minecraft:bookshelf',
}
reference_parents: dict[str, str | None] = {topic: None for topic, *_ in reference_sections}
for hub, (_, topics) in reference_hubs.items():
    for topic in topics:
        reference_parents[topic] = hub + '.md'
for topic in ('maps.shared', 'maps.find'):
    reference_parents[topic] = 'maps.personal.md'
for topic in ('adventure.settlements', 'adventure.loot'):
    reference_parents[topic] = 'adventure.structures.md'
reference_parents['help.credits'] = None


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
written = json.loads((args.content_source or ROOT / 'docs/handbook-content.json').read_text())
descriptions = json.loads((ROOT / 'docs/handbook-project-descriptions.json').read_text())
visual_sources = json.loads((ROOT / 'docs/handbook-visual-sources.json').read_text())
zh_titles['world.dimensions'] = '维度目录'
page_defs = [p for p in coverage['pages'] if not p['page_id'].startswith('landscapes.') and p['page_id'] not in {'sounds.ambience', 'audio.sound', 'travel.moving-destinations'} ] + [dict(page_id='help.handbook', title='Astropunk handbook', player_questions=[]), dict(page_id='world.dimensions', title='Dimensions', player_questions=[])]
page_defs += [dict(page_id='reference.equipment', title='Equipment', player_questions=[]), dict(page_id='combat.abilities', title='Spells & abilities', player_questions=[])]
page_defs += [dict(page_id='help.credits', title='Credits', player_questions=[])]
zh_titles['help.credits'] = '鸣谢'
zh_titles.update({'reference.equipment': '装备', 'combat.abilities': '法术与招式'})
page_defs += [dict(page_id=topic, title=english, player_questions=[]) for topic, english, *_ in reference_sections if topic in reference_hubs or topic == 'reference.audio']
for topic, english, chinese_title, *_ in reference_sections:
    zh_titles[topic] = chinese_title
titles = {p['page_id']: p['title'] for p in page_defs}
titles.update({topic: english for topic, english, *_ in reference_sections})
titles.update({'help.search':'Browse recipe', 'help.controls':'Controls', 'machines.ore-processing':'Ore processing', 'food.utensils':'Cooking tools', 'food.hunger':'Hunger and food variety', 'storage.portable':'Portable storage', 'travel.destinations':'Teleportation', 'building.copycats':'Copycat shapes', 'interactions.carry':'Carry On', 'visuals.lighting':'Lighting and distant terrain', 'combat.skills':'Character skills', 'maps.find':'Biome and structure finders', 'machines.rotation':'Rotational power', 'machines.renewables':'Renewable resources', 'machines.enchanting':'Automated enchanting', 'machines.trading':'Automated trading', 'machines.miscellaneous':'Workshop tools', 'power.electricity':'Electricity', 'power.industry':'Industrial materials and fuels', 'power.burners':'Liquid burner fuels', 'power.stored-rotation':'Rotational storage', 'food.machine-cooking':'Machine cooking'})
for topic, title in titles.items():
    for verb in ('Find ', 'Explore ', 'Choose ', 'Use ', 'Understand ', 'Read ', 'Look up ', 'Learn about '):
        if title.startswith(verb):
            title = title[len(verb):]
            break
    titles[topic] = title[:1].upper() + title[1:]

titles.update({'help.inspect': 'Block & mob info', 'help.reference': 'Mod documentation', 'help.handbook': 'Handbook', 'food.hunger': 'Hunger & variety', 'food.utensils': 'Cooking tools', 'food.nether': 'Nether food', 'food.end': 'End food', 'food.underground': 'Underground food', 'food.encounters': 'Encounter food', 'food.machine-cooking': 'Machine cooking', 'food.growing': 'Farming', 'food.fishing': 'Fishing', 'storage.portable': 'Portable storage', 'storage.bulk': 'Bulk storage', 'storage.handling': 'Inventory tools', 'machines.ore-processing': 'Ore processing', 'machines.rotation': 'Rotational power', 'machines.logistics': 'Item routing', 'machines.renewables': 'Renewable resources', 'machines.enchanting': 'Enchanting', 'machines.trading': 'Trading', 'machines.miscellaneous': 'Workshop tools', 'power.electricity': 'Electricity', 'power.industry': 'Materials & fuels', 'power.burners': 'Liquid fuels', 'power.stored-rotation': 'Stored rotation', 'vehicles.assembly': 'Vehicle assembly', 'vehicles.airships': 'Airships', 'vehicles.engines': 'Engines', 'vehicles.controls': 'Vehicle controls', 'vehicles.radar': 'Radar', 'vehicles.weapons': 'Mounted weapons', 'vehicles.water': 'Boats & submarines', 'transport.passenger': 'Train travel', 'transport.railway-builder': 'Railways', 'transport.local': 'Local transport', 'travel.destinations': 'Teleportation', 'travel.moving-destinations': 'Moving destinations', 'maps.shared': 'Shared maps', 'maps.find': 'Location finders', 'adventure.loot': 'Loot', 'adventure.recovery': 'Death & recovery', 'adventure.sleep': 'Sleep', 'adventure.settlements': 'Settlements', 'combat.handling': 'Weapons & dodging', 'combat.martial': 'Martial classes', 'combat.magic': 'Magic classes', 'combat.skills': 'Character skills', 'equipment.weapons-armor': 'Weapons & armor', 'equipment.accessories': 'Accessories', 'equipment.display': 'Armor & status', 'building.palette': 'Materials', 'building.factory': 'Factory decor', 'building.copycats': 'Copycat shapes', 'building.architecture': 'Architecture', 'building.furniture': 'Furniture', 'building.displays': 'Displays', 'building.placement': 'Placement tools', 'building.safety': 'Lighting & safety', 'interactions.carry': 'Carry On', 'visuals.camera': 'Camera', 'visuals.models': 'Models & animations', 'visuals.weather': 'Weather & particles', 'visuals.lighting': 'Lighting & distance', 'visuals.resource-packs': 'Resource packs', 'visuals.shader-packs': 'Shaders', 'sounds.ambience': 'Sound', 'visuals.interface': 'Interface', 'space.destinations': 'Space (not installed)', 'space.vehicle-transfer': 'Space transport', 'performance.baseline': 'Performance', 'performance.deferred': 'Deferred optimizers', 'server.tools': 'Server tools', 'server.deferred-pack-loading': 'Deferred loading', 'technical.bridges': 'Compatibility', 'technical.space-bridge': 'Space compatibility', 'technical.libraries': 'Libraries'})

zh_titles['help.search'] = '浏览配方'
titles['help.reference'] = 'Advancements'
zh_titles['help.reference'] = '进度'
reference_icons.pop('travel.moving-destinations', None)
class_navigation = json.loads((ROOT / 'docs/handbook-class-navigation.json').read_text())
for topic, definition in class_navigation.items():
    assert topic in written, topic
    if topic not in {page['page_id'] for page in page_defs}:
        page_defs.append(dict(page_id=topic, title=definition['title']['en_us'], player_questions=[]))
    titles[topic] = definition['title']['en_us']
    zh_titles[topic] = definition['title']['zh_cn']
    reference_parents[topic] = definition['parent'] + '.md'
    reference_icons[topic] = definition['icon']

def clean(value):
    return value.replace('|', ',').replace('\n', ' ').replace('—', ', ').replace('–', ' to ').replace(';', ',').replace('；', '，')

provider_purposes = json.loads((ROOT / 'docs/handbook-provider-purposes.json').read_text())
item_queries = json.loads((ROOT / 'docs/handbook-item-queries.json').read_text())
assert set(provider_purposes) == {entry['metadata_path'] for entry in entries}
assert set(item_queries) == set(provider_purposes)

def description(entry, chinese):
    return clean(provider_purposes[entry['metadata_path']]['zh_cn' if chinese else 'en_us'])

def query_links(entry, chinese):
    queries = item_queries[entry['metadata_path']]['zh_cn' if chinese else 'en_us']
    if queries:
        return ' '.join('<EmiSearch query="' + html.escape(query, quote=True) + '" />' for query in queries)
    return '无独立物品查询' if chinese else 'No separate item search'

def decorate_queries(body, chinese):
    # Keep query entry points separate from prose, beside the first relevant section.
    seen = {html.unescape(query) for query in re.findall(r'<EmiSearch query="([^"]+)"', body)}
    blocks = re.split(r'(?m)(?=^#{2,3} )', body)
    for index, block in enumerate(blocks):
        if not block.startswith('##'):
            continue
        links = []
        for entry in entries:
            queries = item_queries[entry['metadata_path']]['zh_cn' if chinese else 'en_us']
            for query in queries:
                if query in seen:
                    continue
                namespace = query[1:] if query.startswith('@') else None
                native_reference = namespace and re.search(r'id="' + re.escape(namespace) + ':', block)
                name_reference = re.search(r'(?<![\w])' + re.escape(entry['name']) + r'(?![\w])', block, re.I)
                component_reference = not namespace and 'id="backpacks:' in block
                if native_reference or name_reference or component_reference:
                    links.append('<EmiSearch query="' + html.escape(query, quote=True) + '" />')
                    seen.add(query)
        if links:
            heading, _, rest = block.partition('\n')
            blocks[index] = heading + '\n\n' + ' '.join(links) + '\n\n' + rest.lstrip('\n')
    return ''.join(blocks)

def roster(members, chinese, linked=False):
    header = '| 模组或内容 | 用途 | 物品查询 |' if chinese else '| Mod or content | Purpose | Item search |'
    rows = [header, '| --- | --- | --- |']
    for entry in sorted(members, key=lambda e: e['name'].lower()):
        name = clean(entry['name'])
        if linked:
            name = '[' + name + '](' + entry['topic'] + '.md)'
        label = {
            'baseline': '',
            'heavy': '（仅重型版）' if chinese else '(heavy edition only)',
            'deferred': '（暂缓加入）' if chinese else '(deferred addition)',
        }[entry['availability']]
        visual = visual_sources.get(entry['metadata_path'])
        if visual and visual.get('kind') in {'publisher icon', 'bundled publisher icon'}:
            name = '![' + clean(entry['name']) + '](' + visual['resource'] + ') ' + name
        else:
            # Missing publisher artwork is represented by a functional topic icon,
            # never passed off as a logo supplied by that publisher.
            icon = category_by_name[entry['category']][3]
            name = '<ItemImage id="' + icon + '" /> ' + name
        rows.append('| ' + name + (' ' + label if label else '') + ' | ' + description(entry, chinese) + ' | ' + query_links(entry, chinese) + ' |')
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
    if filename != 'index.md' and not body.startswith('## '):
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
    'adventure.bosses': ['cataclysm:abyssal_sacrifice', 'cataclysm:altar_of_abyss', 'cataclysm:altar_of_fire', 'cataclysm:altar_of_void', 'cataclysm:burning_ashes', 'cataclysm:cursed_tombstone', 'cataclysm:door_of_seal', 'cataclysm:necklace_of_the_desert', 'cataclysm:strange_key'],
    'combat.magic': ['spell_engine:spell_binding', 'spell_engine:spell_book', 'spell_engine:spell_scroll'],
    'machines.ore-processing': ['create:millstone', 'create:crushing_wheel', 'create:encased_fan', 'create:crushed_raw_iron'],
    'food.utensils': ['farmersdelight:cooking_pot', 'farmersdelight:cutting_board', 'farmersdelight:skillet', 'farmersdelight:stove'],
}
for topic, definition in class_navigation.items():
    if 'item_ids' in definition:
        associations[topic] = definition['item_ids']
for page in page_defs:
    topic = page['page_id']
    members = by_topic[topic]
    counts = Counter(e['category'] for e in members)
    category_name = counts.most_common(1)[0][0] if members else 'Exploration and adventure' if topic == 'world.dimensions' else 'Food and farming' if topic.startswith('food.') else 'Technical reference'
    # A mechanic can reference utility mods without giving them an automation inventory home.
    if topic in reference_hubs:
        category_name = reference_hubs[topic][0]
    elif topic in {'reference.equipment', 'combat.abilities'}:
        category_name = 'Combat and character'
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
        # A directory summarizes providers from its descendant topic pages.
        # This does not create a second inventory assignment or duplicate articles.
        related = [e for e in entries if e['topic'] == topic or reference_parents[e['topic']] == topic + '.md']
        # Search lessons already explain example queries, they are not mod catalog sections.
        if topic not in {'help.controls', 'help.search'}:
            body = decorate_queries(body, chinese)
        if related:
            body += '\n\n***\n\n## ' + ('相关模组' if chinese else 'Related mods') + '\n\n' + roster(related, chinese, linked=True)
        # The toolbar already provides history navigation. Avoid duplicate footer links.
        write_page(topic+'.md', title, body, chinese, reference_parents[topic], icon=reference_icons.get(topic, reference_icons.get((reference_parents.get(topic) or '').removesuffix('.md'), cat[3])), associations=associations.get(topic), position=10000 if topic == 'help.credits' else next((i for i, ref in enumerate(reference_sections) if ref[0] == topic), next((i for i, child in enumerate(reference_hubs['reference.food'][1]) if child == topic), 0)))
    assigned_paths += [e['metadata_path'] for e in members]

# Retire generated navigation reversibly, outside the authoring repository.
# Repeated builds do not create further archives unless obsolete files reappear.
archive_root = ROOT.parent / '.archive' / 'handbook-sidebar-flat'
for chinese in (False, True):
    locale = '_zh_cn' if chinese else ''
    base = PAGES / locale
    obsolete = sorted(base.glob('category-*.md')) + [base / name for name in ('mod-catalogs.md', 'quick-reference.md', 'sounds.ambience.md', 'audio.sound.md', 'travel.moving-destinations.md')]
    for old in obsolete:
        if old.is_file():
            import hashlib
            digest = hashlib.sha256(old.read_bytes()).hexdigest()[:12]
            destination = archive_root / locale / (old.stem + '-' + digest + '.md')
            destination.parent.mkdir(parents=True, exist_ok=True)
            old.replace(destination)
    home = written.get('index')
    assert home, 'The bilingual Astropunk introduction must be present in the authored content source'
    write_page('index.md', 'Astropunk', home['zh_cn' if chinese else 'en_us'], chinese, icon='minecraft:compass', position=-100)

actual = {p.relative_to(ROOT).as_posix() for folder in ('mods', 'resourcepacks', 'shaderpacks') for p in (ROOT / folder).glob('*.pw.toml')} | {'mods/astropunk-handbook-access-1.0.0.jar'}
assert len(assigned_paths) == len(set(assigned_paths)), 'Duplicate primary coverage'
covered = {e['metadata_path'] for e in entries if e['availability'] == 'baseline'}
assert actual == covered, {'missing': sorted(actual - covered), 'unexpected': sorted(covered - actual)}
assert set(assigned_paths) == {e['metadata_path'] for e in entries}
manifest = {'draft_articles': sum(s['drafted'] and s['page_type'] == 'article' for s in status), 'article_count': sum(s['page_type'] == 'article' for s in status), 'category_count': 0, 'navigation_page_count': 0, 'root_page_count': len(reference_sections) + 1, 'reference_section_count': len(reference_sections), 'reference_directory_count': len(reference_hubs), 'installed_content_count': len(actual), 'heavy_content_count': sum(e['availability'] == 'heavy' for e in entries), 'baseline_commit': '77b4453', 'deferred_content_count': sum(e['availability'] == 'deferred' for e in entries), 'pages': status, 'content': entries}
(ROOT / 'docs/handbook-draft-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in manifest.items() if k not in ('pages','content')}, indent=2))
