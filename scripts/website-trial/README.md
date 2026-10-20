# Disposable GuideME website trial

## Outcome

No website or completed game export was produced. Do not present this trial as a working browser guide. Work stopped within the requested investigation window. No preview server was started.

The isolated client remains Minecraft 1.21.1 with NeoForge 21.1.255 and GuideME 21.1.19. The website generator runs separately with Java 25 and genuine Minecraft 26.3 library dependencies. Those dependencies are not installed into, or launched as, a Minecraft instance.

## Scope

Only this feature worktree contains source changes. The source handbook is from the 0.16.4 repository, while the 326 copied mod archives come from the existing 0.17.0 instance, excluding its old handbook helper. The helper is compiled from repository sources. This is not an exact export of either release. No instance settings, credentials, worlds or account files were copied. The trial uses fresh default game configuration, not personal instance configuration. Only English export is currently wired. Chinese export and browser behavior remain unverified.

Everything generated is under `build/website-trial`, already ignored by the repository. The played instance is read-only input for mod archives. No commits, pushes, public hosting, Minecraft upgrades or pack release rebuilds were performed.

## Implementation

- `prepare.py` stages the existing helper source, the authored handbook resource pack and mod archive copies in an isolated Gradle project.
- `WebsiteExportBridge.java` calls the real `guideme.internal.siteexport.SiteExporter` from GuideME 21.1.19 after resources are ready. It does not reconstruct or invent exported game data.
- `build.gradle` defines the ModDevGradle client export run. It supplies the clean named Minecraft artifact required by Connector and disables the development run's automatic game-test discovery.
- `generate.py` invokes the official `guideme.web.WebSiteGenerator` from 26.3.4-alpha in a separate process. It refuses to proceed without a real exported `index.json`.
- `EmiSearchWebFallback.java` uses the official custom web renderer extension. Search queries are visible plain text labeled game-only, not pretend browser buttons. Its compilation succeeded with Eclipse Compiler 3.44.0 on Java 25, but rendering remains untested.

## Reproduction

Run from the repository root. These commands are machine-specific because they reuse existing development caches and Java installations.

```sh
python scripts/website-trial/prepare.py
JAVA_HOME=/home/tsb/Projects/lucas/astropunk-guide/build/handbook-access/toolchain/jdk-21.0.12.1+1 \
GRADLE_USER_HOME=/home/tsb/Projects/lucas/astropunk-guide/build/handbook-access/.gradle-user-home \
bash build/website-trial/gradlew -p build/website-trial runExportGuide --console=plain
# Only after a successful game export creates exported/en_us/index.json:
python scripts/website-trial/generate.py
```

The generator currently requires the previously downloaded official archive at `/home/tsb/.hermes/cache/scratch/guideme-website-research/26.3.4-alpha.jar`. It downloads official Minecraft generator dependencies into the ignored trial folder and verifies their published SHA-1 checksums. It downloads Eclipse Compiler there for compiling the fallback extension. It does not install system tools.

## Executed evidence

Logs remain under `build/website-trial`.

1. `export-run.log`: helper and export bridge compiled. Offline preparation failed because `neoforge-21.1.255-moddev-config.json` was not cached. Retrying without offline mode resolved this prerequisite.
2. `generator-run.log`: the official generator actually started under Java 25, then failed with `NoSuchFileException` for `exported/en_us/index.json`. This was not a successful generation. A fail-fast precondition now prevents that invalid sequence.
3. `export-run-online.log`: Connector failed with `Could not determine clean minecraft artifact path`. Its actual bytecode specifies the `connector.clean.path` development property. Supplying the existing named Minecraft artifact resolved this error.
4. `export-run-connector.log`: startup failed while the development run scanned game-test fixtures referencing absent `alabaster.hearthandharvest.common.block.entity.CaskBlockEntity`. The crash stack identifies `GameTestHooks.registerGametests`, not the exporter. Generated run arguments explicitly enabled `neoforge.enableGameTest`.
5. `export-run-no-gametests.log`: an initial attempt to clear the running-in-editor flag did not address the explicit game-test property. That temporary flag change was removed from the final source.
6. `export-run-final.log`: with `neoforge.enableGameTest` explicitly false, the client passed those startup blockers and reached resource model loading. The command exceeded its 210-second foreground bound and was terminated with exit 124. No Java export process remained afterward. The log includes repeated Puzzles Lib diagonal-block model errors, including an invalid boolean value for the wall-side property on `create:small_andesite_brick_wall` and `tfmg:purple_concrete_wall`. There is no `ASTROPUNK_WEBSITE_TRIAL` export-start marker and no exported `index.json`.

The remaining blocker is reaching a completed resource reload in this copied full-mod development runtime. This does not establish a hard incompatibility between old exported data and the new website generator, because no real export reached the generator. Investigate the recorded model-reload errors before another full run, or explicitly approve a smaller, honestly labeled runtime smoke test. Do not fabricate a replacement export.

## References

- Official two-step workflow: https://guideme.appliedenergistics.org/integration/website-export
- Official source: https://github.com/AppliedEnergistics/GuideME

The old release's export command is unfinished, but its exporter implementation exists. This bridge exercises that implementation without modifying the distributed mod archive or production helper source.
