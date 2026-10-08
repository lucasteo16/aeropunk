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
entries = entries + [dict(metadata_path='mods/guideme.pw.toml', name='GuideME', availability='baseline', category='Technical reference', topic='help.handbook')]
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
('utilities', 'Player utilities and quality of life', '实用工具与便利功能', 'minecraft:bed', 'Find everyday help with controls, interactions, sleep and recovery.', '寻找按键、交互、睡眠和死亡后恢复方面的日常帮助。'),
('visuals', 'Visuals and sound', '视觉与音效', 'minecraft:painting', 'Choose how the game looks and sounds on your machine.', '根据你的电脑和喜好选择画面与声音效果。'),
('technical', 'Technical reference', '技术参考', 'minecraft:redstone', 'Look up supporting libraries, optimization and administrator tools.', '查询支持库、性能优化和管理员工具。'),
]
category_by_name = {c[1]: c for c in categories}

raw_zh_titles = '''help.search|查找物品、配方与用途
help.inspect|查看方块与生物信息
help.controls|查找和修改按键
help.reference|查找已有演示与帮助界面
help.handbook|使用活动指南
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

# Drafts orient players toward items and existing help, rather than duplicating it.
drafts = {
'help.search': ('''Start with what you want to make or use. The item browser shows both recipes that produce an item and recipes that consume it.

## Find a smaller set of items

Search `@create` for Create or `@farmersdelight` for Farmer's Delight. These mod queries are useful when a broad word produces too many results. Names can change with the game language, so do not assume an English item name will always work in Chinese.

## Recipes and uses answer different questions

Recipes help when you want to obtain an item. Uses help when you already have an ingredient and want to know what it can become. Follow the browser's displayed controls; your bindings may differ from someone else's.

If a craft has several valid outputs, Polymorph provides a way to choose the intended result. Check the output before taking it.

## Existing demonstrations

For a Create machine, inspect its tooltip for the Ponder prompt. Use that demonstration for assembly and operation. This handbook tells you which machine to investigate, rather than repeating the demonstration.''', '''先从你想制作或使用的物品开始。物品浏览器既能查看产出这个物品的配方，也能查看消耗它的配方。

## 缩小搜索范围

搜索 `@create` 查看机械动力，搜索 `@farmersdelight` 查看农夫乐事。当一个词返回太多结果时，模组查询很有用。物品名称会随游戏语言改变，因此不要假定英文名称在中文界面中一定能搜到。

## 配方和用途回答不同的问题

想获得某个物品时查看配方。已经有一种材料，想知道能做什么时查看用途。按照浏览器显示的操作提示使用，你的按键可能与别人不同。

当一次合成存在多个有效产物时，Polymorph 可以帮助选择目标产物。取出物品之前先确认结果。

## 已有演示

查看机械动力机器的提示，寻找思索提示。组装和操作请使用已有演示。本指南帮助你决定该找哪台机器，不重复演示内容。'''),
'machines.ore-processing': ('''Create has several ways to process materials. Choose a machine by the recipe you need, rather than assuming a larger machine always gives more metal.

## Items to look for

<Row>
  <ItemImage id="create:millstone" />
  <ItemImage id="create:crushing_wheel" />
  <ItemImage id="create:encased_fan" />
</Row>

Look for the Millstone, Crushing Wheel and Encased Fan. The first two process materials mechanically; a fan can perform further processing with the appropriate setup. Their accepted ingredients and outputs differ, so inspect recipes before building.

## Follow one ingredient

Try raw iron. In the selected Create release, crushing it produces crushed raw iron, with a chance of an experience nugget. Washing the crushed material produces iron nuggets, with a chance of redstone. Check the recipe outputs and quantities in the item browser when comparing this route with smelting.

Search `@create`, inspect the machine's tooltip, and follow its Ponder prompt for the actual arrangement and power requirements.

## Move materials afterward

Belts, funnels and filters belong to [material routing](machines.logistics.md). Learn the processing recipe first, then choose how to deliver ingredients and collect outputs.''', '''机械动力提供多种原料加工方式。先根据配方选择机器，不要以为机器越大就一定能得到更多金属。

## 寻找这些物品

<Row>
  <ItemImage id="create:millstone" />
  <ItemImage id="create:crushing_wheel" />
  <ItemImage id="create:encased_fan" />
</Row>

寻找磨石、粉碎轮和鼓风机。前两者通过机械方式加工原料；鼓风机可以在合适的装置中进行进一步加工。它们接受的材料和产物不同，建造之前先查看配方。

## 顺着一种材料查看

先看粗铁。当前机械动力版本中，粉碎粗铁会产出粉碎铁矿石，并有概率获得经验颗粒。洗涤粉碎铁矿石会产出铁粒，并有概率获得红石。与熔炼比较时，请在物品浏览器中查看产物和数量。

搜索 `@create`，查看机器提示中的思索提示，使用已有演示了解实际排列方式和动力要求。英文检索参考：Millstone, Crushing Wheel, Encased Fan, Raw Iron。

## 再安排物品输送

传送带、漏斗和过滤器见[物品输送](machines.logistics.md)。先确定加工配方，再选择如何送入原料和收集产物。'''),
'food.utensils': ('''Farmer's Delight adds cooking tools, not just more food items. Start with the tool that matches the kind of recipe you want to make.

## Items to look for

<Row>
  <ItemImage id="farmersdelight:cooking_pot" />
  <ItemImage id="farmersdelight:cutting_board" />
  <ItemImage id="farmersdelight:skillet" />
  <ItemImage id="farmersdelight:stove" />
</Row>

Search `@farmersdelight` for the Cooking Pot, Cutting Board, Skillet and Stove. Look at a meal's recipe to identify the required tool; ordinary crafting, cutting and cooking are different operations.

The following is the registered crafting recipe for the Cooking Pot, not an example meal:

<Recipe id="farmersdelight:cooking_pot" fallbackText="Look up Cooking Pot in the item browser to see its crafting recipe." />

## Choose a meal

Find a dish you want to make, inspect its ingredients, and check its cooking method. A recipe may also need a serving container. Gather those requirements before building a larger kitchen.

For more variety, explore the [Nether](food.nether.md), [End](food.end.md) and [underground](food.underground.md) food pages. Machine kitchens have a separate [automation page](food.machine-cooking.md).''', '''农夫乐事不仅增加食物，还提供烹饪工具。先根据你想制作的配方选择工具。

## 寻找这些物品

<Row>
  <ItemImage id="farmersdelight:cooking_pot" />
  <ItemImage id="farmersdelight:cutting_board" />
  <ItemImage id="farmersdelight:skillet" />
  <ItemImage id="farmersdelight:stove" />
</Row>

搜索 `@farmersdelight`，寻找烹饪锅、砧板、煎锅和炉灶。查看一道食物的配方，确认需要哪种工具；普通合成、切割和烹饪是不同操作。英文名称参考：Cooking Pot, Cutting Board, Skillet, Stove。

下面是烹饪锅本身的合成配方，不是示例菜品：

<Recipe id="farmersdelight:cooking_pot" fallbackText="请在物品浏览器中查看烹饪锅的合成配方。" />

## 选择一道食物

找到想做的食物，查看食材和制作方法。有些配方还需要盛装容器。先准备这些要求，再考虑扩建厨房。

更多食材见[下界](food.nether.md)、[末地](food.end.md)和[地下](food.underground.md)食物页面。机器厨房另见[自动烹饪](food.machine-cooking.md)。'''),
'food.hunger': ('''Food choice affects both eating and packing for a trip. AppleSkin helps you compare hunger and saturation information instead of judging a meal only by its appearance.

## Compare foods before leaving

Hover food items and inspect the information AppleSkin provides. Hunger and saturation are different: two foods with similar hunger restoration need not keep you fed for the same length of time.

Short Stacks changes food stack sizes according to how filling the food is. Check the stack limit you actually see in this pack before planning how much food fits in your inventory.

## Try a varied diet

Spice of Life Onion tracks dietary variety. Look for its Food Book to inspect your food history and the benefits configured for this pack. This draft does not prescribe a reward threshold or a fixed diet.

Start with [cooking tools](food.utensils.md), then choose meals you enjoy making. No food milestone unlocks another handbook page.''', '''选择食物也关系到出门时如何打包。AppleSkin 可以帮助比较饥饿值与饱和度，不必只看食物外观。

## 出发前比较食物

把鼠标移到食物上，查看 AppleSkin 提供的信息。饥饿值与饱和度不同；恢复饥饿值相近的食物，不一定能让你同样久不饿。

Short Stacks 会根据食物的饱腹能力调整堆叠数量。规划背包空间之前，先看这个整合包里实际显示的堆叠上限。

## 尝试多样化饮食

Spice of Life Onion 会记录饮食多样性。寻找它的 Food Book，查看吃过的食物和本整合包配置的收益。本草稿不指定奖励门槛，也不要求固定饮食路线。

先了解[烹饪工具](food.utensils.md)，再选择你喜欢制作的食物。任何食物里程碑都不会解锁或限制指南页面。'''),
'storage.portable': ('''Choose portable storage by how you want to handle its contents. Backpacks! provides dyeable, upgradeable backpacks. Reinforced Shulker Boxes provides another storage option, while Easy Shulker Boxes adds inventory interactions for shulker-box contents.

## Find your options

Search the item browser for backpack and shulker-box items. Inspect the specific upgrade recipes and tooltips before committing materials. This draft does not assume a universal capacity or identical controls across the different containers.

Use the displayed interaction prompts to learn how a container opens and how items move in or out. Try a small set of ordinary materials before relying on it during a long expedition.

## Keep other questions separate

Storage capacity is different from [carrying a placed block](interactions.carry.md). Workshop stockpiles have their own [bulk storage page](storage.bulk.md).''', '''根据你希望如何存取内容来选择便携储存。Backpacks! 提供可染色和升级的背包；Reinforced Shulker Boxes 提供强化潜影盒；Easy Shulker Boxes 增加在物品栏中操作潜影盒内容的方式。

## 找到可选物品

在物品浏览器中查找背包和潜影盒。投入材料之前，先查看具体升级配方和提示。本草稿不假定所有容器都有相同容量或操作方式。

按照实际提示了解如何打开容器和存取物品。长途探险前，先用少量普通材料试用。

## 区分其他需求

扩大携带容量与[搬运已放置的方块](interactions.carry.md)不同。工厂库存另见[大批原料储存](storage.bulk.md)。'''),
'travel.destinations': ('''Waystones and Tempad offer different approaches to teleportation. Waystones connects activated destinations; Tempad provides portable portal travel. NetherPortalFix addresses return destinations for Nether portals in multiplayer, rather than adding another destination network.

## Items to investigate

Look for Waystone and the available scroll items, then inspect Tempad's items and help. Read the current interface for activation, destination and cost requirements. Do not assume every travel system uses the same rules.

Create Waystones Recipes changes Waystones crafting to use Create ingredients. Use the recipes in this pack instead of a recipe copied from an unrelated installation.

## Fixed coordinates and moving vehicles

A saved location is not automatically a live destination aboard a moving ship. Vehicle-specific integration has a separate [moving destinations page](travel.moving-destinations.md). Its behavior still needs verification, so do not treat ordinary saved coordinates as a promise of safe ship arrival.''', '''Waystones 与 Tempad 提供不同的传送方式。Waystones 连接已激活的目的地；Tempad 提供便携传送门。NetherPortalFix 处理多人游戏中下界传送门的返回目的地问题，不是另一个目的地网络。

## 查找相关物品

寻找 Waystone 和可用的卷轴，再查看 Tempad 的物品与帮助。激活方式、目的地和费用以当前界面为准，不要假定不同传送系统使用同一套规则。

Create Waystones Recipes 会让 Waystones 合成使用机械动力材料。请查看本整合包里的配方，不要照搬其他整合包的配方。

## 固定坐标与移动载具

保存一个位置，不代表它会自动跟随移动船只。载具相关兼容另见[移动目的地](travel.moving-destinations.md)。这部分行为仍需验证，普通保存坐标不能保证安全到达船上。'''),
'building.copycats': ('''Create: Copycats+ adds building shapes that can take the appearance of another material. Look here when a full block is too bulky for the detail you want to build.

## Choose a shape first

Search the item browser for Copycats+ and compare the available shapes. Inspect the item's recipe and tooltip to find out how it accepts a material. Supported shapes and interactions depend on the specific block; do not assume every material or interaction works identically.

Create's existing Ponder help can explain supported blocks. When a block has no demonstration, its tooltip and recipe are the first references to check.

## Appearance is not compatibility

A copied texture does not establish airtightness, collision behavior or moving-vehicle compatibility. Those properties need checks for the actual block, especially when building a submarine. The [water vehicles page](vehicles.water.md) will cover those checks.

For other materials and furniture, return to [Building and decoration](category-building.md).''', '''Create: Copycats+ 增加可以采用其他材料外观的建筑形状。当完整方块太厚、无法表现想要的细节时，可以从这里寻找合适的形状。

## 先选形状

在物品浏览器中查找 Copycats+，比较可用形状。查看配方和提示，了解该方块如何接受材料。支持的形状与交互取决于具体方块，不要假定所有材料与操作都相同。

已有的思索演示可以解释受支持的方块。没有演示时，先查看物品提示与配方。

## 外观不代表兼容性

复制了纹理，不代表具备相同的气密性、碰撞行为或移动载具兼容性。尤其建造潜艇时，需要检查实际方块。这些检查会写入[水上与水下载具](vehicles.water.md)页面。

其他材料与家具见[建筑与装饰](category-building.md)。'''),
'interactions.carry': ('''Carry On lets you pick up supported placed blocks and creatures. It is useful when rearranging a base without turning every move into a break-and-rebuild task.

## Find the interaction

Open Controls and find Carry On's bindings. Use the binding shown in your instance; do not assume a key from another player's setup. Try the interaction on a simple supported target before moving something valuable.

Compatibility and restrictions depend on the target. This draft does not claim that every container, machine or creature can be carried, or that carrying is safe aboard every moving vehicle.

## Carrying is not storage

This interaction moves a target. It does not replace a [backpack or portable container](storage.portable.md). Use those when your question is how to carry more inventory items.''', '''Carry On 可以搬起受支持的已放置方块和生物。调整基地布局时，不必把每次移动都变成拆除和重建。

## 找到交互方式

打开按键设置，查找 Carry On。使用你当前实例显示的按键，不要假定与其他玩家相同。移动贵重目标之前，先在简单且受支持的目标上试用。

兼容性与限制取决于目标。本草稿不保证所有容器、机器或生物都能搬起，也不保证在所有移动载具上都安全。

## 搬运不是储存

这个交互用于移动目标，不能替代[背包或便携容器](storage.portable.md)。如果你想携带更多物品栏中的物品，应选择储存装备。'''),
'visuals.lighting': ('''Choose visual effects according to your machine and preferences. These settings do not unlock gameplay or handbook content.

## Shaders

Iris loads shader packs. The pack includes several choices, listed on the [shader styles page](visuals.shader-packs.md). Enable one at a time and compare the same location before deciding whether its appearance is worth the performance cost.

## Distant terrain

Distant Horizons renders terrain beyond ordinary chunk rendering. It is off by default in this pack, but players can choose to enable it. Its resource cost and behavior with moving builds need separate testing; off by default is not a ban on using it.

## Dynamic lighting

Sodium Dynamic Lights and its moving-build lighting addon are optional heavy-edition features. They are not installed in this light guide preview. Their compatibility references remain listed for players comparing editions.

Change one setting at a time when comparing performance. [Resource packs](visuals.resource-packs.md), animations and sound are separate choices, so you can adjust them without treating every visual feature as a single preset.''', '''根据电脑性能和个人喜好选择视觉效果。这些设置不会解锁玩法或指南内容。

## 光影

Iris 用于加载光影包。本整合包提供的选择见[光影风格](visuals.shader-packs.md)。一次启用一个，在相同地点比较，再决定画面效果是否值得相应性能开销。

## 远景

Distant Horizons 在普通区块渲染范围之外显示地形。本整合包默认关闭，但玩家可以自行启用。资源开销和移动建筑相关行为需要单独测试；默认关闭不代表禁止使用。

## 动态光源

Sodium Dynamic Lights 及其移动建筑光源扩展属于重型版可选功能，未安装在这一轻量指南预览中。兼容参考仍保留，方便比较版本。

比较性能时，一次只修改一个设置。[资源包](visuals.resource-packs.md)、动画和声音是独立选择，不必把所有视觉功能当作同一个预设。'''),
}

drafts.update({
'combat.skills': ('''Skill choices are one way to shape a character. This pack includes several related skill systems; do not assume they share one point pool or the same unlock rules.

## Find your skill interface

Open Controls and search for the skill-related actions. Inspect the interface you open, its node descriptions and its displayed requirements before spending points. This draft does not prescribe a build or promise that every choice can be refunded.

Skill Tree and the selected role expansions belong to the role and equipment choices described in [martial roles](combat.martial.md) and [magic roles](combat.magic.md). Pufferfish's Skills is also selected. Their exact configured trees and overlap still need a separate check.

## Choose by what you want to play

Start with an activity or weapon style you enjoy, then look for the matching equipment and skills. You can read every handbook page regardless of your character's level; actual gameplay requirements remain part of the game.''', '''技能选择可以帮助形成角色风格。本整合包包含几个相关技能系统，不要假定它们共用技能点，或使用相同的解锁规则。

## 找到技能界面

打开按键设置，搜索技能相关操作。花费技能点之前，先查看打开的界面、节点说明和显示的要求。本草稿不指定配点，也不保证所有选择都能退款。

Skill Tree 与所选角色扩展关联的职业和装备选择见[战斗风格](combat.martial.md)和[法术风格](combat.magic.md)。本整合包也选择了 Pufferfish's Skills。具体配置的技能树及重叠仍需要单独检查。

## 根据你想玩的内容选择

先决定喜欢的活动或武器风格，再寻找对应装备和技能。无论角色等级如何，所有指南页面都能阅读；实际玩法要求仍由游戏决定。'''),
'maps.find': ('''Finding a landscape and finding a structure are different questions. Nature's Compass helps locate biomes; Explorer's Compass helps locate structures.

## Choose the right finder

Look for Nature's Compass when your destination is a biome. Look for Explorer's Compass when you want a structure. Inspect the chosen item's recipe and interface before planning a trip.

A finder is not a promise that every target exists nearby. Available targets and search behavior depend on the actual world and settings. This draft does not prescribe a search radius or guarantee a dungeon result.

## Keep the destination

Use the [personal maps page](maps.personal.md) for recording places and the [shared maps page](maps.shared.md) for multiplayer map sharing. To decide what to look for, browse [settlements](adventure.settlements.md), [structures](adventure.structures.md) and [Overworld landscapes](landscapes.overworld.md).''', '''寻找地形和寻找结构是不同需求。Nature's Compass 用于寻找生物群系，Explorer's Compass 用于寻找结构。

## 选择合适的工具

目标是生物群系时，寻找 Nature's Compass。目标是结构时，寻找 Explorer's Compass。规划旅程之前，先查看所选工具的配方和界面。

工具不保证每个目标都存在于附近。可用目标和搜索行为取决于实际世界与设置。本草稿不指定搜索半径，也不保证一定找到地牢。

## 记录目的地

记录地点见[个人地图](maps.personal.md)，多人共享地图见[地图共享](maps.shared.md)。想决定找什么，可以先看[聚落](adventure.settlements.md)、[结构](adventure.structures.md)和[主世界地形](landscapes.overworld.md)。'''),
})

page_defs = list(coverage['pages']) + [dict(page_id='help.handbook', title='Use the activity handbook', player_questions=[])]
# Read existing generated pages before replacing them, retaining their committed history.
for p in PAGES.rglob('*.md'):
    p.read_text()

status = []
assigned_paths = []
for page in page_defs:
    topic = page['page_id']
    members = by_topic[topic]
    if members:
        counts = Counter(e['category'] for e in members)
        category_name = counts.most_common(1)[0][0]
        assert len(counts) == 1, (topic, counts)
    else:
        category_name = 'Food and farming' if topic.startswith('food.') else 'Technical reference'
    cat = category_by_name[category_name]
    filename = topic + '.md'
    title_en = page['title']
    title_zh = zh_titles[topic]
    is_draft = topic in drafts
    is_deferred = bool(members) and all(e['availability'] == 'deferred' for e in members)
    status.append(dict(topic=topic, category=category_name, filename=filename, drafted=is_draft, deferred=is_deferred, metadata_paths=[e['metadata_path'] for e in members]))
    for language in ('en_us', 'zh_cn'):
        chinese = language == 'zh_cn'
        title = title_zh if chinese else title_en
        nav_title = title if is_draft else title + ' (WIP)'
        body = drafts[topic][1 if chinese else 0] if is_draft else ('编写中（WIP）。本页预留给这个主题，玩法说明尚未编写或验证。' if chinese else 'Work in progress (WIP). This page reserves the topic; its instructions have not been written or verified.')
        if is_deferred:
            body += '\n\n' + ('规划内容，未安装在这一预览中。' if chinese else 'Planned content, not installed in this preview.')
        if topic == 'food.fishing':
            body += '\n\n' + ('尚未确认本整合包有独立的扩展钓鱼系统。先保留这个查找入口，不把它当作已安装功能。' if chinese else 'A dedicated expanded fishing system has not been established for this pack. This is a discovery placeholder, not an installed-feature claim.')
        roster = []
        for e in members:
            assert (ROOT / e['metadata_path']).is_file() or e['availability'] in ('deferred', 'heavy'), e
            label = ('（重型版可选内容，当前未安装）' if chinese else ' (optional heavy edition, not installed here)') if e['availability'] == 'heavy' else ('（规划，未安装）' if chinese else ' (planned, not installed)') if e['availability'] == 'deferred' else ''
            roster.append('- ' + e['name'] + label)
        if roster:
            body += '\n\n## ' + ('涉及的内容' if chinese else 'Included content') + '\n\n' + '\n'.join(roster)
            if not is_draft:
                body += '\n\n' + ('这些名称用于完整收录，不代表玩法说明已经完成。' if chinese else 'These names provide coverage, not completed instructions.')
        body += '\n\n[' + ('返回分类' if chinese else 'Back to category') + '](category-' + cat[0] + '.md)\n\n[' + ('返回活动指南' if chinese else 'Back to activities') + '](index.md)\n'
        text = '---\nnavigation:\n  title: ' + json.dumps(nav_title, ensure_ascii=False) + '\n  parent: category-' + cat[0] + '.md\n---\n\n# ' + title + '\n\n' + ('草稿，可供评阅。物品浏览器和思索的直接按钮尚未实现。\n\n' if chinese and is_draft else 'Draft for review. Direct item-browser and Ponder buttons are not implemented.\n\n' if is_draft else '') + body
        out = PAGES / ('_zh_cn' if chinese else '') / filename
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
    assigned_paths += [e['metadata_path'] for e in members]

for cat in categories:
    articles = [s for s in status if s['category'] == cat[1]]
    for chinese in (False, True):
        title = cat[2] if chinese else cat[1]
        intro = cat[5] if chinese else cat[4]
        lines = []
        for s in articles:
            definition = next(p for p in page_defs if p['page_id'] == s['topic'])
            label = zh_titles[s['topic']] if chinese else definition['title']
            label += ('（草稿）' if chinese else ' (draft)') if s['drafted'] else ' (WIP)'
            lines.append('- [' + label + '](' + s['filename'] + ')')
        text = '---\nnavigation:\n  title: ' + json.dumps(title, ensure_ascii=False) + '\n  icon: ' + cat[3] + '\n---\n\n# ' + title + '\n\n<ItemImage id="' + cat[3] + '" />\n\n' + intro + '\n\n' + '\n'.join(lines) + '\n\n[' + ('返回活动指南' if chinese else 'Back to activities') + '](index.md)\n'
        (PAGES / ('_zh_cn' if chinese else '') / ('category-' + cat[0] + '.md')).write_text(text)

for chinese in (False, True):
    body = '---\nnavigation:\n  title: ' + ('活动指南' if chinese else 'Activities') + '\n---\n\n# ' + ('你想做什么？' if chinese else 'What would you like to do?') + '\n\n' + ('所有主题都可以直接阅读，没有任务、奖励或解锁要求。已编写的页面标为草稿，未完成页面标为 WIP。先选你感兴趣的活动。' if chinese else 'Every topic is open from the start. There are no quests, rewards or unlock requirements. Written samples are marked draft; unfinished pages are marked WIP. Choose the activity that interests you.') + '\n\n## ' + ('先看这些草稿' if chinese else 'Drafts to review') + '\n\n'
    for topic in drafts:
        page = next(p for p in page_defs if p['page_id'] == topic)
        body += '- [' + (zh_titles[topic] if chinese else page['title']) + '](' + topic + '.md)\n'
    body += '\n## ' + ('全部活动' if chinese else 'All activities') + '\n\n'
    for cat in categories:
        if cat[0] == 'technical':
            continue
        body += '<Row><ItemImage id="' + cat[3] + '" /></Row>\n\n### [' + (cat[2] if chinese else cat[1]) + '](category-' + cat[0] + '.md)\n\n' + (cat[5] if chinese else cat[4]) + '\n\n'
    body += '## ' + ('参考资料' if chinese else 'Reference') + '\n\n[' + ('技术参考' if chinese else 'Technical reference') + '](category-technical.md)\n\n' + ('这一版采用默认排版。空间地图式首页和直接打开其他界面的按钮仍在规划中。' if chinese else 'This draft uses the ordinary layout. The spatial homepage and direct external-screen buttons remain planned.') + '\n'
    (PAGES / ('_zh_cn' if chinese else '') / 'index.md').write_text(body)

# Keep the original preview URL as a compatibility landing page, not another canonical article.
for chinese in (False, True):
    text = '---\n{}\n---\n\n# ' + ('矿石加工' if chinese else 'Process ores') + '\n\n[' + ('打开矿石加工草稿' if chinese else 'Open the ore-processing draft') + '](machines.ore-processing.md)\n'
    (PAGES / ('_zh_cn' if chinese else '') / 'ore-processing.md').write_text(text)

actual = {p.relative_to(ROOT).as_posix() for folder in ('mods', 'resourcepacks', 'shaderpacks') for p in (ROOT / folder).glob('*.pw.toml')}
assert len(assigned_paths) == len(set(assigned_paths)), 'Duplicate primary coverage'
covered = {e['metadata_path'] for e in entries if e['availability'] == 'baseline'}
assert actual == covered, {'missing': sorted(actual - covered), 'unexpected': sorted(covered - actual)}
assert set(assigned_paths) == {e['metadata_path'] for e in entries}
manifest = {'draft_articles': sum(s['drafted'] for s in status), 'article_count': len(status), 'category_count': len(categories), 'installed_content_count': len(actual), 'heavy_content_count': sum(e['availability'] == 'heavy' for e in entries), 'baseline_commit': '34cb006', 'deferred_content_count': sum(e['availability'] == 'deferred' for e in entries), 'pages': status, 'content': entries}
(ROOT / 'docs/handbook-draft-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in manifest.items() if k not in ('pages', 'content')}, indent=2))
