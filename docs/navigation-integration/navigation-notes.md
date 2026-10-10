# Unified handbook navigation

## Result

The home and sidebar now expose one topic tree. Quick reference retains its existing primary topics, followed by Utilities, Appearance, Audio and Technical. Mod catalogs and all ten duplicate category catalogs have left the active generated source. No redirect pages replace them.

Every retained article has one primary navigation parent and reaches Quick reference in at most two parent steps. Detailed gameplay content stays on individual topics. Related provider lists appear after the authored body, beneath a separator and the final Related mods section. Topic hubs summarize their child providers and link each provider to its primary detailed topic. These secondary rows do not count as another inventory home.

## Mapping

- `help.search` keeps its identifier and now displays Browse recipe, or 浏览配方.
- `reference.vehicles` keeps its identifier and now displays Transport, or 交通.
- Equipment, Spells and skills, Food and farming, Building, Transport, and Machines and storage retain their established child articles.
- Maps retains Shared maps and Location finders. Structures retains Settlements and Loot.
- Utilities owns Block and mob information, Existing help, Carry On, Death and recovery, and Sleep.
- Appearance owns Camera, Models and animations, Weather and particles, Lighting and distance, Resource packs, Shaders, and Interface.
- Audio owns `sounds.ambience`.
- Technical owns Handbook, Performance, Deferred optimizers, Server tools, Deferred loading, Compatibility, Space compatibility, and Libraries.
- The two existing space destination and transfer articles now live beneath Transport. Their heavy or deferred availability remains explicit.

The generator still uses functional category metadata for fallback icons and inventory classification. That metadata no longer generates a competing category tree.

## Inventory and availability

The authoring checklist has 318 entries. The generator adds the existing GuideME selection and handbook access helper, yielding 320 unique provider paths. Current generation reconciles 292 installed baseline paths, 20 heavy-edition paths and 8 deferred paths. These totals describe file presence and inventory, not gameplay verification.

The manifest preserves one primary topic assignment per provider. Every primary topic has its provider rows at the bottom. Each row has an existing publisher icon when supplied, otherwise a functional topic icon, a linked provider name, a status and the available publisher summary. Chinese provider tables label the English publisher summaries explicitly. Missing publisher summaries remain limited rather than being replaced with invented feature descriptions.

## Audio overrides and integration boundary

The generator's entry-normalization loop explicitly assigns these exact paths to `sounds.ambience` and the Visuals and sound inventory category:

- `mods/cool-rain-reforged.pw.toml`
- `mods/pf-neoforge.pw.toml`
- `mods/sable-cool-rain.pw.toml`
- `mods/presence-footsteps-x-sable.pw.toml`

The latter two were previously under `technical.bridges`. Their selected metadata names and stored publisher descriptions identify rain-sound and footstep compatibility functions. Sable: Cool Rain names rain sounds on Sable structures, Create copycats and other modded blocks. Presence Footsteps x Sable names its compatibility with Sable and Create Aeronautics.

Further technical placement changes should extend this same normalization loop before `by_topic` is built. Keep one primary topic per exact metadata path. Do not add another navigation root. The parent owns those placement decisions, the authored technical and class fragments, pink typed input, the authoring standard, and final authoring-source merging. This change does not write `docs/handbook-content.json`.

After merging those fragments, regenerate the handbook and repeat the checks below. Authored hub bodies remain authoritative. Supplemental hubs without an authored body receive real child-topic directories with honest completion labels. Unwritten articles retain their Work in progress marker.

## Removed generated files and recovery

Both locales retired `mod-catalogs.md` and these category pages:

- `category-automation.md`
- `category-storage.md`
- `category-food.md`
- `category-building.md`
- `category-travel.md`
- `category-combat.md`
- `category-exploration.md`
- `category-utilities.md`
- `category-visuals.md`
- `category-technical.md`

The generator moved 22 original files to `/home/tsb/Projects/lucas/.archive/astropunk-guide/unified-navigation`, outside the authoring repository and distributed source. Chinese copies remain in `_zh_cn`. Archive filenames retain the original stem and a content-hash suffix. All archived bytes were compared with repository HEAD and matched. Repeated generation does not create another archive unless obsolete files reappear.

For recovery, copy an archived file back to its original locale and filename, then restore the matching older generator and navigation contract from Git. Running the new generator will retire those old files again. The parent must reconcile embedded fallback resources and pack synchronization before distribution. This task does not update exports, the pack index or a running instance.

## Verification

The navigation regressions first failed on the old competing roots and parent chains, then passed with the unified tree. Separate failing checks covered missing provider footers, missing hub provider rows, display renames and audio compatibility placement before their implementation.

Source validation no longer searches obsolete category catalogs for provider identity. It checks primary topic footer identity, visuals and honest status, unique inventory assignment, locale parity, real links, home reachability, acyclic parents and the two-level limit. The released parser wrapper now derives its default expected page total from the manifest instead of retaining the obsolete fixed total of 198.

Run these commands from the repository:

```sh
python scripts/build-handbook-draft.py
python -m unittest discover -s tests -p test_handbook_navigation.py -v
python -m unittest discover -s tests -p test_handbook_review_layout.py -v
python -m unittest discover -s tests -p test_quick_reference_visuals.py -v
python scripts/validate-guide-preview.py --source-only
python scripts/handbook-access/validate_syntax.py
git diff --check
```

Verified before final fragment merging: 23 handbook tests pass, source validation passes for 192 localized pages and 1674 links, and GuideME 21.1.19 accepts all 192 pages with zero parse failures. Its malformed native-tag negative control is rejected. The parser emits the existing missing-logger-provider warning but completes successfully.

No client rendering, gameplay, helper behavior or live refresh is claimed. No game was launched, and this task did not change mods, options, helper code, worlds, exports or Hermes profiles. Parent-owned source edits visible during generation were consumed, not edited by this task.


## Final integration

Classification overrides are authoritative in `docs/handbook-placement-overrides.json`, and affect category and topic only. Current installation status still comes from the reconciled pack inventory. All 84 content articles now have bilingual bodies, with no work-in-progress markers. Both languages contain 192 physical pages in total.

Integrated class choices, technical content, clean boss and cooking images, suitable native recipe displays and compact location text. Typed commands and queries are pink. Templates match the single topic tree. The old catalog resources were backed up and retired from the normal installed fallback pack, and exact resource readback and export parity passed. Mods, helper installation, configurations, keybindings and worlds were not changed.

Parser, source, navigation, visual and package checks are recorded in `integration-verification.json`. No game rendering or gameplay validation was performed. Image reuse permissions remain uncertain for third-party sources, the package is a local review artifact, not a public publication.
