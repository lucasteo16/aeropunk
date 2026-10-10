# Navigation and content review

## Before repairs

The supplied screenshot shows ten retired catalog roots beside Quick reference. The current repository guide definition has only default_language and item_settings. It contains no explicit navigation registration. GuideME 21.1.19 DataDrivenGuide.CODEC accepts item_settings, default_language and custom_colors, not a navigation array. Adding or removing an invented array cannot repair this released engine.

The released behavior reproduces the symptom through fallback merging. The screenshot alone does not establish whether the running instance has stale packaged pages or stale watched state. MutableGuide.buildNavigation copies packaged pages and then applies developmentPages by page identifier. Deleting a watched source removes its override and exposes the packaged fallback again. NavigationTree.build registers every parsed page with navigation frontmatter. Therefore stale packaged category pages remain roots even when the watched folder and source-only filename checks are clean.

The homepage duplicates the entire Quick reference table. Equipment and Spells & skills form two separate reference roots. Building placement already shows the Mech Trowel but reduces it to one generic sentence and omits acquisition and useful modes.

## Historical reconciliation

Compared all ten English category pages at commit 8e2499a against current authoritative content. Their ninety distinct linked destinations all have current content sources. Historical page snapshots and per-category findings are archived before retirement. Category-automation is the only category with substantial retained authored mechanics, so its machine guidance is reconciled into Machines & storage rather than silently discarded. The other category bodies mainly repeat topic links, installation labels and publisher descriptions, which remain in the topic reference pages and primary provider footers.

## Repair scope

Keep Astropunk as a separate introduction and Quick reference as the only topic-tree root. Rename the stable reference.skills landing to Combat, move its full class and ability reference to combat.abilities, and place Equipment and abilities as siblings directly beneath Combat. Keep other combat and equipment articles at the same level to avoid a third category level. No redirect pages.

Maintain source ownership through a bilingual navigation-content fragment for parent integration. The generator never writes the authoritative content source. Archive retired generated pages and sanitized registration bytes before removal. A fallback repair command must be supplied an explicit normal resource-pack target, archives its retired pages and registration first, and verifies bytes after copying the current resources. No launcher, game, profile or world changes.

## Verification boundaries

Execute the released NavigationTree bytecode with lightweight Minecraft boundary stubs, testing packaged and watched merge semantics, stale fallback resurrection, source and repaired fallback roots, Combat sibling ownership, cycles and depth. This is a native navigation-processing check, not rendered proof. Syntax, source, resource parity and installed fallback checks remain separate.


## Released watcher and reload findings

Confirmed against selected 21.1.19 bytecode as well as matching release source. GuideSourceWatcher.Listener dispatches DELETE to pageDeleted. takeChanges emits a null newPage and MutableGuide.tick removes that page from developmentPages, then rebuilds navigation. Deletion therefore does not suppress a still-packaged page. For translated deletions, pageDeleted first attempts default-language fallback. Its sourceFolder.resolve(pageId.toString()) uses a namespace-qualified identifier as a filesystem path, which can fail and then queues deletion instead.

A second stale-state route exists even after disk fallback cleanup. MutableGuide.setPages clears queued watcher changes, then adds watcher.loadAll pages to developmentPages without clearing that map. If a pending DELETE is cleared during resource reload, the old development page remains in memory and can continue registering its root. A clean repository plus clean installed folder is therefore not proof that a currently open sidebar has refreshed. A user-controlled clean restart after fallback reconciliation is the reliable state reset. No Java helper workaround or persistent hidden legacy page was introduced.

The repository registration was archived and inspected. It contains no navigation list to remove, and the actual selected DataDrivenGuide codec has no such field. The reconciler replaces a target registration with the checked current registration after archiving the target, so unsupported legacy nodes cannot survive in a copied fallback definition. No installed resource-pack target was supplied to this subagent, so installed bytes and current-client state are not claimed.

## Executed checks

Generated 97 pages per language from a staged merged content file without touching authoritative handbook-content.json. The manifest accounts for all 320 provider paths, comprising 292 installed, 20 heavy-edition and 8 deferred entries. All ninety historical category destinations remain available. Both locale trees execute unchanged released NavigationTree bytecode and pass two-root ownership, complete native node reachability, depth, Combat siblings, watched-precedence and stale-fallback negative controls. Native navigation tests use stubbed Minecraft item and parsed-page boundaries, not a running registry.

The fallback reconciliation fixture archives a stale category and unsupported registration, removes the old page, copies current resource bytes, verifies every copied file and remains idempotent on a second pass. Source-only validation passes with 194 bilingual pages and 1746 links. The released Markdown parser accepts all 194 pages and rejects its malformed-tag control. Navigation, fallback, layout and unified-content tests pass. The existing authored-source preservation test requires parent integration of the fragments before the full test suite can pass, because the generated test pages currently use the staged content source.

## Parent integration

Merge navigation-content.json and building-content.json into handbook-content.json, archive and remove the orphan category-automation key, then run the normal generator. navigation-content.json keeps the historical automation purpose sections within Machines & storage. Source remains authoritative, with no fragment overlay or automatic source rewrite in the generator. The optional --content-source argument only permits isolated staging. Re-run source preservation after integrating any other agents' markup repairs. Use the explicit fallback reconciler only for the selected normal resource-pack folder. Current-client refresh and rendered layout remain unverified.
