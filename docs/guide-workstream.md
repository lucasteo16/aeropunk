# Guide workstream

## Isolation

Branch: `guide/sandbox-handbook`.

Workspace: `/home/tsb/Projects/lucas/aeropunk-guide`.

Base: `grouped/chunky` at `4491dfe`.

Keep this workstream independent from Chunky testing, optimizer trials and Northstar work. Do not switch other worktrees or modify launcher instances. Future baseline changes require an explicit merge and inventory reconciliation; branch ancestry does not automatically synchronize content.

## Scope

Complete the full functional taxonomy and page plan before expanding guide prose. Treat Lucas's examples as suggestions, not a frozen category list. Map every selected project to a primary function, permit secondary activity links, and identify missing or unsupported content explicitly. All pages remain available from the start.

Research an extensible in-game presentation with item-free access, contextual actions and English and Chinese content. GuideME is the provisional recommendation, not an approved installed dependency. Default English with Simplified Chinese is an authoring starting point; Traditional Chinese can share page identifiers and be added independently.

Maintain a separate integration findings register. Notify Lucas about confirmed or credible gameplay problems, missing integration, redundant additions and proposed removals. Do not silently alter the pack. Separate upstream reports, release-supported mechanisms and actual gameplay tests. Northstar's renderer override remains on hold.

## Work products

- `guide-taxonomy.md` describes the complete activity and page plan.
- `guide-coverage.json` maps all selected metadata and deferred branch content.
- `guide-engine-audit.md` distinguishes built-in presentation features from custom bridge work and unknowns.
- `guide-integration-review.md` and `guide-integration-findings.json` track exact-version gameplay concerns and recommended actions.

## Sequence

Finish coverage and integration planning first. Review the engine audit and choose one representative vertical slice with Lucas. Tune its layout, access, localization and contextual actions. Only then expand approved page templates in batches.

Documentation work does not authorize installing guide dependencies, launching gameplay tests, rebuilding diagnostic packs or changing accepted mod selections. A later implementation checkpoint needs an explicit scope decision. Background research is session-bound; the dedicated worktree preserves completed files if a session ends.
