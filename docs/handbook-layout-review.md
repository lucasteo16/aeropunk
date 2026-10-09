# Handbook layout review

## Reviewed scope

The current layout trial covers Astropunk, Dimensions, and Automation and industry, in English and Simplified Chinese. Other authored articles have not received a full visual redesign. Common heading placement, affected inventory membership, link targets and the Item recipe title have been corrected across generated pages where necessary.

## Layout decisions

- The first-level heading supplies the toolbar title. All body content begins beneath a second-level heading.
- Astropunk puts Quick reference above Mod catalogs. Both use the same two-column icon-and-link pattern, with fixed-size decorative inline item images rather than full-width item grids. Navigation icons have no item tooltip; actual instructional item slots keep their tooltips. The old three-link strip had no special factual status and has been removed. Native thematic breaks separate major sections and catalog groups.
- Dimensions contains Overworld, Nether and End sections with the installed terrain mods and concise purposes. The old landscape pages are consolidated rather than retained as extra clicks.
- Automation Mods comes before Mechanics. The mod tables use authentic publisher icons and concise functional summaries, divided into machines, power and production groups.
- Recipe-browser addons, villager naming, trade-screen shortcuts and manual anvil conveniences have player-utility inventory homes. Mechanics can still refer to a relevant utility without recategorizing it as an automation mod.
- The ore-processing redirect page is removed. The existing full article remains under Automation and industry.
- Sources, image checksums and publisher license metadata are recorded in handbook-visual-sources.json. The landscape photograph is a Tectonic publisher screenshot, not an Astropunk instance capture.

## Settled shared navigation

Quick reference and Mod catalogs are ordered sidebar roots, alongside Astropunk. Thirteen reference entries match the homepage directory. Six grouped directories organize Equipment, Spells and skills, Food and farming, Building, Vehicles and travel, and Machines and storage. Existing topic articles have one primary navigation parent and remain cross-linked from mod catalogs. Native navigation position fields establish ordering. All parent chains are acyclic and have no more than two category levels before an article.

Reference and Getting started share a topic, not separate trees. Short starting guidance belongs within the reference article; a substantial companion shares the same topic grouping. Directories are counted separately from the 84 content articles, so the structural additions do not inflate authored content totals. There are now 206 bilingual Markdown files, with 14 authored content articles, 70 unwritten content articles, six reference directories, ten area catalogs, two navigation roots, and the homepage in each locale.

The first detailed writing batch is proposed in handbook-first-writing-batch.md. No new detailed boss, creature or dungeon sections have been written in the structural pass. Background styling remains deferred.

## Content-index priority

The next authoring priority is to answer what exists in the installed game: actual bosses, mobs, structures and dungeon variants first, then other content families. A complete mod roster does not establish a complete wiki. Crafting tutorials are secondary to these catalogs. The content-index completeness audit is being performed separately and must not be described as a completed set of game-facing lists. Background styling was not changed; a Create-like appearance remains low priority.

## Earlier layout verification

Six layout regression tests failed before the changes and pass after them. The selected GuideME 21.1.19 parser accepts all 190 bilingual page files and five templates, and rejects the malformed negative control. Source checks verify locale parity, primary inventory coverage, link targets and homepage reachability.

A fresh native packwiz export contains the 210 exact resource files, including 18 image assets, and excludes authoring documents, scripts, tests and obsolete navigation pages. The dedicated instance's normal handbook resource folder matches those same 210 files. The previous snapshot and consolidated pages are preserved outside the repository under the project archive. No other resource packs, mods, player options or worlds were changed for the content update.

The running instance has both official source properties set. Its log records watching the repository source directory. Removed source pages generated the released watcher's fallback lookup errors; deletion is still queued, but packaged fallback pages can remain in the resource cache. The installed handbook snapshot has therefore also been reconciled. Lucas should perform one resource reload with F3 and T to clear old fallback navigation, then reopen the handbook. Ordinary subsequent page edits still use the native watcher.

Actual layout, tooltip behavior and refreshed navigation remain subject to Lucas's review. Do not infer rendered quality from parser success. The opening shortcut failure is being investigated separately; use the confirmed guide command until the corrected helper has been installed and tested after a user-controlled restart.
