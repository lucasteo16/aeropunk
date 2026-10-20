# Machines and storage human review handoff

## Outcome

All fifteen chapter topics are included in English and Simplified Chinese. The new resource pack is `build/refurb-review/Astropunk-Handbook-Machines-Storage-Final-20261020-212043.zip`. It is a handbook resource pack, not a modpack installer. Human review is pending. No installation, game launch, merge, commit or push was performed.

## Cause and correction

A narrow Ore processing source edit was made after generation, verification and packaging. The source contract had also not been refreshed. The earlier status report incorrectly compared a canonical structured-content digest with a raw file-byte digest; these are different encodings, not inherently contradictory revisions.

Regeneration exposed the pending query update. Workshop tools still used a whole-Minecraft search rather than named outputs. It now has specific Phantom Membrane, Brown Mushroom Block and Red Mushroom Block searches, with Chinese equivalents. The bilingual verifier now recognizes exactly those reviewed localized query pairs and Wheat Flour, while retaining negative controls for incorrect queries and changed item identities.

Only four resource pages changed relative to the earlier archive. The other 718 resource files, including the four independently reviewed correction pages, remain byte-identical. The original independent closure and package report are preserved in `build/machines-final/recovery`. The follow-up parent review covers the precise query delta, not a claimed new independent review of the entire chapter.

## Revision binding

The contract distinguishes its canonical structured-content digest from its raw source-file digest. Closure, chapter verification and package reports bind the raw source-file digest `a0ac15a0b3e268388ba7269c274e9d723223f745afa8cabae927a9ee4c1df819`. The export checks both encodings and confirms all nonblank authored chapter lines are present in generated pages.

Two new regression checks first failed on the stale handoff. Both pass after rebuilding: exact source binding across records, and archive integrity plus exact readback of every current resource file.

## Executed verification

- Nine Machines finalization tests passed, including negative controls and the two new stale-handoff regressions.
- Ten Food finalization tests passed. Two historical Food assertions were made revision-aware rather than treating the later Machines chapter as an unauthorized Food edit. They validate the exact Machines source contract and still compare every unrelated generated article with the historical endpoint.
- All thirty localized chapter pages passed the selected GuideME syntax parser and structural component fixture.
- Twenty-seven referenced images decoded fully. Thirteen recipe references were checked against selected resources or previously inspected dynamic registration.
- Released navigation bytecode passed for both languages, with 130 nodes and eighteen ordered roots, including reorder and fallback negative controls.
- The native pack index was refreshed. Git whitespace checks passed.
- All 722 resource files were read back byte for byte from the new archive. Archive integrity passed.
- The full current source suite ran 221 tests: 199 passed, 21 failed and one errored. All 22 failing check identifiers also fail in an isolated development-base worktree using the same current tests and selected Java and GuideME paths. There are no newly failing check identifiers. The complete suite is not green. Existing failures include historical Combat, Food, space, icon-audit and provider expectations, and were not silently skipped or rewritten.

Detailed suite evidence is in `build/machines-final/recovery/current.log`, `baseline.log` and `comparison.json`. The baseline comparison uses actual Git worktrees, not a source archive lacking history. New chapter-specific assertions are expected to fail when applied to the older chapter.

## Review boundaries

The structural fixture substitutes vanilla item identities, skips recipe and keybinding runtime dispatch, strips scenes and has no image loader. It does not establish real mod registry availability or rendering. No running-game registry, scene, recipe-manager, interaction or gameplay acceptance is claimed.

Place the archive in the instance resourcepacks folder and enable it above older handbook previews. Disable the earlier checkpoint if it overrides this resource pack. Review Ore processing, Workshop tools, enchanting, industrial materials, vent presentation and navigation in both languages. The remaining work is human visual and interaction review, not another automatic writing pass.

## Method adjustment

This recovery reused the accepted chapter and reviewed only four changed generated pages instead of dispatching new writers or rewriting the chapter. The safeguard is a failing stale-handoff regression and exact resource readback. The previous three hash values were not valid evidence of three distinct revisions until their encodings were identified. Future handoffs record both hash encodings explicitly and preserve prior review evidence. No comparative speed improvement is claimed because earlier active-effort timing is unavailable.
