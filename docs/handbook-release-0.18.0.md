# Handbook refinement release 0.18.0

The development version is `0.18.0-dev`. Combat, Food and farming, Machines and storage, and the forthcoming Transport finalization share this version. Do not increment it again merely for the remaining Transport chapter.

## Acceptance

- Combat: accepted and already integrated.
- Food and farming: accepted and already integrated.
- Machines and storage: accepted subject to the final tutorial-icon and compact-query corrections, now applied in both languages.
- Transport: the remaining chapter to finalize. Existing content is retained, not newly accepted by this merge.

## Final presentation corrections

Every chapter tutorial row now includes the existing play image, including section-specific searches. There remains exactly one primary tutorial row beneath each page title. Contextual rows stay beside their sections rather than being hoisted into the header.

Processing searches use the standard self-closing query component. The visible pink text is the actual query, such as Wheat Flour, not an instructional sentence. Instructions remain ordinary prose. The query strings themselves are unchanged.

The scoped final review, source digest, native parser and structural-fixture results, and resource hashes are recorded in `docs/machines-storage-final-review.json`. Focused chapter, historical Food-preservation and navigation checks were used. Earlier unrelated complete-suite failures were not silently treated as resolved, and a full suite or game launch was not repeated for these presentation changes.

The merge targets the actual local `dev` branch. The separately checked-out, dirty `fix/refurbishment-combat-standard` branch in the directory named astropunk-dev is preserved. No stable branch, played instance, world or remote branch is changed by this local integration.
