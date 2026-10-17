# Mars addon retirement

Release `0.15.0-dev` removes Create Cosmonautics Expansion 1.0.0 at Lucas's request after he reported severe lag in its Mars dimension. This is a content-selection decision, not proof of a measured root cause or a general judgment of the implementation.

Base Cosmonautics, the Moon, Deep Space, Deep Air and Deep Seas remain unchanged. Base Cosmonautics still contains a visible Mars celestial record without a linked surface dimension. Removing the addon does not remove that background body. The bilingual handbook now distinguishes this from a landable destination. Mars travel titles and the obsolete border-command example are retired; all seven lunar biome titles remain.

## Existing-world warning

Do not apply this to the only copy of a world. Move players, inventories, ships and valuable addon blocks out of the Mars dimension first. The addon registers blocks, items and biome definitions, so removal can lose content or prevent an existing save from loading. A populated-world removal and recovery test has not been performed. Keep the old pack export with its matching world backup for rollback. Existing played saves and launcher installations were not modified.

## Verification

Native packwiz removal completed. A disposable server test using the exported artifact reached readiness on a fresh temporary world, saved its dimensions and shut down with exit code zero. Installed mod inventory and export verification must exclude the retired artifact while retaining the base space mods. Fresh-world startup does not establish compatibility with an old Mars-populated save or prove the reported lag is fixed.

The handbook was regenerated against current development inventory. This also reconciled missing inventory entries for the recently approved dimension-border, processor-generation and ship-orientation additions, without adding more mods or changing their settings. Retired image provenance and historical release evidence are preserved.

The full inherited source suite was exercised and is not green: multiple historical inventory, visual snapshot, navigation and food checks fail, and native navigation probes lack their local prerequisites. An archived pre-removal source snapshot also fails many of these checks, but differing local fixtures prevent claiming identical results. Do not describe this change as a passing full-suite result. Focused Mars-removal and space-content checks are run separately; failures outside this scope are not repaired as part of a mod removal.

Evidence: ignored `reports/result.json`, `reports/server.log`, `build-mars-removal-tests.log` and `build-mars-baseline-tests.log`.
