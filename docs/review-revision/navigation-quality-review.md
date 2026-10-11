# Navigation quality review

## Scope and ownership

Reviewed the authoring standard, generator, every native root and every child list. The shared order is explicit in scripts/handbook_navigation.py and mirrored in coverage. The generator, source validator and released-engine probe reject missing pages, extra pages, wrong parents and position ties. Every page retains a meaningful globally unique icon and identical structural metadata in English and Simplified Chinese. The tree has 111 pages, eighteen roots and at most two ancestors. No wrapper hierarchy was added.

This worker did not generate pages, change authored bodies or provider artwork, export a pack, change a version, commit, launch Minecraft or modify a live installation.

## Root order

Astropunk, Controls, Browse recipe, Utilities, Maps, Dimensions, Structures, Creatures, Bosses, Combat, Food & farming, Building, Machines & storage, Transport, Appearance, Audio, Technical, Credits.

Access and everyday help come first. Maps starts exploration, followed by destinations, places, ordinary encounters and bosses. Combat follows encounters. Food, building and machines cover home and workshop activities before complex transport. Appearance and audio stay together, supporting technical information follows, and Credits remains last. The sequence is navigation, not a progression requirement.

## Child ordering rationale

- Structures puts settlements before loot. Maps puts finding locations before sharing them.
- Utilities starts with inspection and carrying, then routine sleep and death recovery.
- Combat starts with handling and equipment, then weapon, accessory and status references, class choices, abilities and character development. Equipment and abilities remain direct children.
- Martial classes group melee roles before ranged roles. Warrior introduces melee, Archer introduces ranged, and their specialist choices follow. Magic groups ordinary wizard schools, elemental extensions, then support and hybrid roles. These are functional groups, not claims about class difficulty.
- Food retains Cooking tools first and Hunger & variety second. Farming and fishing precede underground, Nether, End and encounter ingredients. Machine cooking comes last.
- Building starts with materials and placement tools, then architecture, copycat shapes, furniture, displays and factory decoration. Lighting and safety closes the list.
- Machines & storage starts with portable storage, inventory handling and bulk storage. Rotation precedes processing, routing, renewable production and workshop tools. Stored rotation, fuel and industrial systems lead to electricity. Specialized enchanting and trading automation closes the list.
- Transport follows land, sea, sky, space and teleportation. Local transport and riding trains precede railway construction. Boats follow. Assembly, controls and engines precede airships, radar and mounted weapons. Orbital flight, life support and space navigation are consecutive after sky topics and before Teleportation.
- Appearance starts with interface and camera choices, then resource packs, models, weather, lighting and shaders. Technical starts with handbook help and advancements, then performance, server tools, compatibility and libraries.

Every sibling has its own integer position. Native alphabetical tie-breaking is no longer part of the design. Generated directory rows use the same order. Existing authored catalog bodies belong to the content worker and are not automatically rewritten.

## Dimensions and current main

Space destinations no longer has a sidebar page. Dimensions owns the combined destination catalog and the primary Create Cosmonautics provider link. Orbital flight, life support and navigation remain Transport mechanics. The generator archives obsolete destination resources on its next run. The released probe includes a stale packaged destination resurrection and repair control.

Coverage and manifest generation now use f5c24f3. Selected provider metadata is reconciled to that main revision. Paxi is a baseline server-tools provider, with its exact selected download metadata and world-border data-pack paths recorded. Baseline verification compares all selected mod, resource-pack and shader-pack metadata bytes and all world-border files with main. Archive validation also checks the packaged world-border files. The local handbook helper is guide-owned and is not treated as an unchanged external provider artifact.

## Verification

Executed without generating pages:

```text
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p test_navigation_ordering.py -v
PYTHONDONTWRITEBYTECODE=1 python scripts/test-native-navigation.py --metadata-only
git diff --check
```

All eight semantic-ordering tests pass. Two additional source regressions pass: bilingual native-reference parity across the four retained space-related articles, and conservation of the former destination catalog's native references inside Dimensions. Their exact invocation was:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tests python -m unittest test_cosmonautics_handbook.CosmonauticsHandbook.test_four_pages_have_identical_native_references_in_both_locales test_cosmonautics_handbook.CosmonauticsHandbook.test_destinations_are_folded_into_dimensions_without_losing_native_items -v
```

The selected GuideME 21.1.19 NavigationTree processes 111 nodes and eighteen ordered roots in each language. It verifies every sibling list, depth and reachability, rejects a deliberate native transport reorder, and retains the fallback merge, watched deletion, obsolete Quick reference, Sound and Space destinations resurrection and repair controls. Five source mutations test rejection of ties, reorders, wrong parents, extra pages and missing pages. Main metadata and world-border byte parity pass. This does not verify rendering, live item registration or a running client's sidebar.

## Parent handoff

1. Coordinate Paxi provider entries with the content worker. Its metadata now has a primary home, but handbook-provider-purposes.json and handbook-item-queries.json need matching Paxi entries before normal generation. Add translated purposes and an empty independent-item query list. Project descriptions are also missing Paxi. The navigation worker deliberately did not edit those owned sources.
2. Confirm the content worker folded the destination body into Dimensions and updated authored directory links and topic lists. Existing provider queries, item grids and unrelated prose must survive.
3. Generate once after both workers finish, then run the complete test suite, source validator and normal native navigation probe against generated resources. Generated-dependent tests were updated but not run against stale pages. The flat-sidebar test now verifies existing generated pages rather than triggering another generation.
4. Coordinate authoring-standard edits centrally. Its old root sequence and suggestion that Credits is a child are stale. Replace them with this order, keep Credits last, and preserve the current comma whole-handbook shortcut, unbound contextual help and eight-pixel inventory-button gap. This worker did not edit the standard.

Suggested post-generation checks, without exporting or launching anything:

```text
PYTHONDONTWRITEBYTECODE=1 python scripts/build-handbook-draft.py
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
PYTHONDONTWRITEBYTECODE=1 python scripts/validate-guide-preview.py --source-only
PYTHONDONTWRITEBYTECODE=1 python scripts/test-native-navigation.py
git diff --check
```
