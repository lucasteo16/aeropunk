# Opening endpoint investigation

## Exact artifacts

Installed GuideME 21.1.19 and the compile dependency are byte-identical, SHA256 `2ce254edb931c3c3cf81d69abaf8f4ce5b871bf85e64984f366bf044173bd66a`.

The installed helper and the pre-change built helper were also byte-identical, SHA256 `e62c3f62963a3ebb475f3fd847df096aff20a21df6abc9ec33bba923d0f08ef8`.

Released source baseline is commit `52334ccacf15d763ffe318281d38dca8ec7aaeb8`. Implementations were corroborated with `javap -p -c` from the actual installed binary, not inferred from descriptors.

## Released behavior and limits of diagnosis

`GuidesCommon.openGuide(Player, ResourceLocation)` calls `GuideMEProxy.instance().openGuide(player, guideId, null)` and discards its boolean result. `GuideMEServerProxy` only opens for `ServerPlayer`; for a local client player it returns false without logging.

However, `GuideMEClient` installs `GuideMEClientProxy`. Both of that proxy's opening overloads compare the supplied player to `Minecraft.getInstance().player`. For the identical local player, the null-anchor path calls `GuideMEClient.openGuideAtPreviousPage(guide, guide.getStartPage())`.

Therefore the existing common endpoint is not intrinsically server-only. Its native client implementation already supports precisely the local player the helper supplies. The reviewed source and logs do not establish that the running proxy was wrong, or that the shortcut event was delivered. A server-proxy mismatch remains a possible conditional failure, not a proven live cause.

`GuideClientCommand` uses the direct `GuideMEClient.openGuideAtPreviousPage` call after guide lookup. That method reads `GlobalInMemoryHistory`, navigates to the previous page if present or the native start page otherwise, catches exceptions, logs them and returns a boolean.

The minimal change makes helper opening match the user-confirmed working client command exactly. It removes proxy selection as a dependency, but does not prove the reported live shortcut failure is resolved. The method is public within `guideme.internal` and is coupled to the pinned release.

## Read-only runtime evidence

The selected instance's latest log reports `Data driven guides: [astropunk:handbook]` at `09Oct2026 01:29:46.973`. No matching `Failed to open guide` line or helper warning or error was present when inspected. Saved options still recorded the helper shortcut as F9. This does not disprove an unsaved live comma rebinding.

Logs were filtered for handbook loading, opening errors and helper errors. Launcher arguments and credentials were not read or printed.

## Regression and verification

`test_open_endpoint.py` was run before the implementation change. Its direct endpoint contract failed against the old helper, while the released proxy behavior tests passed. `red-open-endpoint.log` retains the failure. This is an artifact endpoint regression, not a simulated gameplay reproduction.

`open-endpoint-build.log` records a clean successful Gradle build, all nine existing JUnit tests passing, all three released-bytecode regression tests passing, and artifact verification passing. Existing controls, client distribution, inventory widgets, contextual bindings, missing-guide policy and watched-source setup are unchanged.

No game was launched, no computer control was used, and no files in the running instance were changed. Runtime keyboard and button behavior remain unverified. Installing this changed compiled helper requires a client restart; resource reload cannot replace loaded Java classes.

The repository helper archive may be replaced separately within the authorized scope. The pack index was deliberately not updated; its archive checksum must be reconciled by the parent before packaging.
