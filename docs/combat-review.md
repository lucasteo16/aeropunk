# Combat comparison review

## Scope

The revision covers 28 topics in English and Simplified Chinese, including 18 class articles. Work is isolated on `feature/combat-guide-review`, based on development commit `9fed11b0bfe78b784c848fce1e9e70283f91b2ea`. Development, stable branches, worlds and installed instances are unchanged.

The 56 original localized pages were frozen before editing. Their hashes match the Combat pages in the selected Astropunk 0.17.0 installation. The comparison preserves those pages under Combat (old), with only navigation labels, parent references, internal Combat links and contextual item associations adjusted for coexistence.

## Changes

- Combat opens with linked class comparisons, short first steps and relevant reference destinations instead of repeated starter-weapon cells and a descendant-wide mod roster.
- Shared binding and casting instructions live in Spells and abilities. Magic classes covers weapon spells and rune resources. Character skills owns point budgets, paths and resets.
- Class armor catalogs use a visible chest-piece reference with four corresponding native item slots. Weapon catalogs group only matching families and roles.
- Shared equipment and accessory catalogs consolidate repeated attribute descriptions without dropping item identities. Arsenal's duplicated 44-item grid and 44-row table are replaced by 14 named families with 18 exact-role groups, preserving mixed-school staff and shield exceptions. Runes have separate workstation, storage and casting-resource groups.
- Every revised page offers English and Chinese YouTube searches beside one decorative play icon. Searches use contextual terms and Minecraft 1.21.1. They do not guarantee the language or accuracy of search results.
- Existing instructional images and recipes remain. No decorative scene was added merely to increase the visual count.

## Comparison pack

Second pass: six further topics were rewritten for playable guidance and presentation.

| Topic | Second-pass change |
| --- | --- |
| Combat | Class rows are standalone Start build links with compact decorative icons. |
| Arcane Wizard | Equipped armor-stand scene for an example starter outfit, plus four readiness checkpoints and a three-row weapon table. |
| Spells and abilities | Scroll use, scroll transfer including the consumed-scroll and experience cost, and a symptom table for abilities that fail. |
| Magic classes | Rune crafting in hand, altar batching, pouch loading and equipment, failure checks, and optional supply goals. |
| Character skills | How to choose a class root and weapon branch, how modifiers apply, and how resetting works. |
| Weapons and armor | Armory sets, Arsenal families and Cataclysm groups as compact tables with grouped items. |

Tutorial searches now sit immediately below the page title on every Combat page, placed by the generator from the authored single action row.

The generated file is `build/combat-review/Astropunk-Combat-Comparison.zip`.

1. Put the archive in the selected instance's resourcepacks folder.
2. Enable it above the existing Astropunk handbook resource pack. Keep that original pack enabled because it supplies the unchanged pages and shared images.
3. After resource loading completes, open the guide and compare Combat with the adjacent Combat (old) root. Both include their full subtrees.
4. Disable the comparison pack to restore the installed handbook. No mod replacement or player-setting change is required.

The overlay contains the revised and original Combat trees, the play icon, and navigation-position overrides for the following roots. It does not replace the entire handbook or register a competing guide. Old pages do not own contextual item associations, so item-based help continues to use the revised articles. Their explicit internal article links remain within the old tree.

## Verification

Nine focused source tests passed, including a regression that checks every Arsenal item occurs once and retains its exact role in both languages. The released GuideME 21.1.19 parser accepted all 126 pages in the final overlay. The selected release's structural compiler checked 112 localized old and new Combat pages, including 820 item grids and 2,786 slots, with zero failing pages. That probe normalizes item identifiers to vanilla stone and substitutes runtime-dependent recipes and key labels. It verifies component structure, not mod registry presence, recipe rendering or gameplay.

Native navigation checks passed for the revised source guide. Overlay checks establish unique sibling positions, acyclic parent links, maximum depth, adjacent Combat roots, original-page preservation and exact archive bytes. All 19 configured book pools and 118 ability rows per language remain. No authored topic outside Combat changed.

The first generation exposed an existing inventory omission for the already selected Just Enough Items mod. Its checklist entry, bilingual provider purpose and empty item-query record were added so generation can complete. This changes its generated Browse recipe footer, not the authored article or mod selection. The comparison overlay does not include that unrelated footer change.

Computer control and game launches were not used. Final in-game appearance, tooltip behavior and external-link opening still require player inspection.

## Reproduction and evidence

The parent integrates topic-keyed worker fragments into `docs/handbook-content.json`. Generated native pages remain owned by `scripts/build-handbook-draft.py`.

```sh
python scripts/build-handbook-draft.py
python scripts/combat-comparison.py build
python -m unittest discover -s tests -p test_combat_comparison.py -v
python -m unittest discover -s tests -p test_handbook_navigation.py -v
```

The comparison builder uses the frozen baseline in `build/combat-review/baseline`. Do not replace that baseline with revised pages. The original source remains recoverable from the development commit named above.

Per-page review evidence, independent review findings, focused test output, parser and structural compiler logs, and archive verification are under `build/combat-review`. `final-verification.json` records the final archive checksum and preservation counts. No full test suite, modpack export, release-version change, commit or push was performed.

The 64 by 48 pixel tutorial play glyph is original decorative artwork generated by the `icon` action of `scripts/combat-comparison.py`. It is not an official publisher logo or an instructional illustration.

## Verification gaps found after delivery

The first handoff claimed preserved references, but that check only compared against intermediate snapshots taken during this review, never against the branch base. Rechecked against `9fed11b`, the Combat landing page had genuinely lost the Spell Binding Table item, its recipe and two labelled reference bullets. Those are restored.

Six topics no longer reference individual items they referenced at the branch base. Each removal is recorded with a reason in `docs/handbook-combat-review-scope.json` under `accepted_reference_removals`. The shared binding procedure moved to Spells and abilities, and the path tables stopped repeating the same item as both an icon and a label.

The visual-pass snapshot test also compares against a snapshot older than this branch. It failed at the branch base before any Combat work for `storage.portable`, which this review never edited. That topic is recorded under `known_pre_existing_drift` so the check stays meaningful for everything else.

The preservation test now fails if any item reference disappears without a recorded reason.

## Third pass

Every class article now carries optional readiness guidance, concrete what-to-look-for text about the attribute, weapon family and armour set the class actually uses, and a compact weapon table instead of stacked heading and grid blocks. Five classes show an example outfit in a native equipped armor stand scene: Arcane, Fire, Rogue, Priest and Witcher. Each is labelled an example starter outfit, not an official default.

Combat controls and Martial classes gained the same treatment, including the verified roll behaviour from the Combat Roll publisher page: rolls follow movement, cost exhaustion, are blocked while using an item, jumping or swimming, and run without invulnerability frames by default here. Accessories and Equipment gained a short when-to-invest table.

Generation, the four source suites, the released parser over all 126 comparison pages, and the structural compiler over 112 localised pages all pass. Five scenes are present in the pack. In-game rendering, camera framing and table widths still need player inspection.
