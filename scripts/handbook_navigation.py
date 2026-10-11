"""Explicit semantic sibling order shared by authoring and released-engine probes."""
ROOT_ORDER = (
    'index', 'help.controls', 'help.search', 'reference.utilities', 'maps.personal',
    'world.dimensions', 'adventure.structures', 'adventure.creatures', 'adventure.bosses',
    'reference.skills', 'reference.food', 'reference.building', 'reference.machines-storage',
    'reference.vehicles', 'reference.appearance', 'reference.audio', 'reference.technical',
    'help.credits',
)
CHILD_ORDER = {
    'adventure.structures': ('adventure.settlements', 'adventure.loot'),
    'maps.personal': ('maps.find', 'maps.shared'),
    'reference.utilities': ('help.inspect', 'interactions.carry', 'adventure.sleep', 'adventure.recovery'),
    'reference.skills': ('combat.handling', 'reference.equipment', 'equipment.weapons-armor',
                         'equipment.accessories', 'equipment.display', 'combat.martial',
                         'combat.magic', 'combat.abilities', 'combat.skills'),
    'combat.martial': ('class.warrior', 'class.berserker', 'class.rogue', 'class.forcemaster',
                       'class.archer', 'class.deadeye', 'class.war-archer', 'class.tundra-hunter'),
    'combat.magic': ('class.arcane', 'class.fire', 'class.frost', 'class.aqua', 'class.terra',
                     'class.wind', 'class.priest', 'class.paladin', 'class.bard', 'class.witcher'),
    'reference.food': ('food.utensils', 'food.hunger', 'food.growing', 'food.fishing',
                       'food.underground', 'food.nether', 'food.end', 'food.encounters', 'food.machine-cooking'),
    'reference.building': ('building.palette', 'building.placement', 'building.architecture',
                           'building.copycats', 'building.furniture', 'building.displays',
                           'building.factory', 'building.safety'),
    'reference.machines-storage': ('storage.portable', 'storage.handling', 'storage.bulk',
                                   'machines.rotation', 'machines.ore-processing', 'machines.logistics',
                                   'machines.renewables', 'machines.miscellaneous', 'power.stored-rotation',
                                   'power.burners', 'power.industry', 'power.electricity',
                                   'machines.enchanting', 'machines.trading'),
    'reference.vehicles': ('transport.local', 'transport.passenger', 'transport.railway-builder',
                           'vehicles.water', 'vehicles.assembly', 'vehicles.controls', 'vehicles.engines',
                           'vehicles.airships', 'vehicles.radar', 'vehicles.weapons',
                           'space.vehicle-transfer', 'space.life-support', 'space.navigation', 'travel.destinations'),
    'reference.appearance': ('visuals.interface', 'visuals.camera', 'visuals.resource-packs',
                             'visuals.models', 'visuals.weather', 'visuals.lighting', 'visuals.shader-packs'),
    'reference.technical': ('help.handbook', 'help.reference', 'performance.baseline',
                            'server.tools', 'technical.bridges', 'technical.libraries'),
}


def navigation_metadata():
    """Assign every page an explicit position unique among its siblings."""
    result = {topic: {'parent': None, 'position': -100 if topic == 'index' else
                     10000 if topic == 'help.credits' else position - 1}
              for position, topic in enumerate(ROOT_ORDER)}
    for parent, children in CHILD_ORDER.items():
        assert parent in result, parent
        for position, topic in enumerate(children):
            assert topic not in result, ('Duplicate navigation home', topic)
            result[topic] = {'parent': parent + '.md', 'position': position}
    return result


def assert_semantic_navigation(actual):
    """Reject missing pages, extra pages, wrong parents, ties and shifted positions."""
    expected = navigation_metadata()
    assert set(actual) == set(expected), {'missing': sorted(set(expected) - set(actual)),
                                         'extra': sorted(set(actual) - set(expected))}
    for topic, definition in expected.items():
        assert actual[topic] == definition, (topic, actual[topic], definition)
    for parent, order in [(None, ROOT_ORDER), *[(p + '.md', c) for p, c in CHILD_ORDER.items()]]:
        siblings = [(row['position'], topic) for topic, row in actual.items() if row['parent'] == parent]
        assert len({position for position, _ in siblings}) == len(siblings), ('Position tie', parent)
        assert tuple(topic for _, topic in sorted(siblings)) == order, ('Semantic order', parent)
