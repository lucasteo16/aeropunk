# Handbook access investigation

## Outcome

The live shortcut failure has no proven root cause yet. The installed helper already contains the previous direct-opening candidate, its event wiring is present, and the guide is registered. Replacing its opening endpoint again would repeat an unproven change.

Two narrower findings are established. The helper can silently omit its inventory button when there is no free rectangle large enough. Native watched-source loading was active in this run, and later navigation rebuilds show changes reached the engine. Neither finding establishes what Lucas saw when pressing a shortcut or watching a particular page.

Native colored text works in GuideME 21.1.19. This investigation executed both its parser and its actual Color compiler, including malformed negative controls. No new production helper source changes were made.

## Scope and artifacts

Read-only inspection used the dedicated profile at `/home/tsb/.local/share/ModrinthApp/profiles/astropunk-0.3.0-guide.light.1-modrinth`. Repository work used `/home/tsb/Projects/lucas/astropunk-guide`; the supplied path string also contained `test/guide`, which is not a directory here.

| Artifact | Verified SHA256 |
| --- | --- |
| Installed GuideME and compile dependency | `2ce254edb931c3c3cf81d69abaf8f4ce5b871bf85e64984f366bf044173bd66a` |
| Installed helper, repository packaged helper and rebuilt helper | `946027c72b8f99e6fb2e8c09d01b6d19e94254f4c4a3541f887721abd4910b8e` |

The selected engine is 21.1.19. Its release-matching source evidence is under `build/handbook-access/evidence/GuideME-52334ccacf15d763ffe318281d38dca8ec7aaeb8`. Binary checks used the actual archives, not only repository source. The helper targets NeoForge 21.1.255 and declares client-only dependencies.

Safe process metadata identified a Java process whose working directory is this profile, started at 11:39:25 on October 9, 2026. The installed helper modification time was 01:59:20 that day. Therefore a file replacement after this process started is not supported by these timestamps. This is not a readback of loaded class bytes. No complete process arguments, credentials or launcher settings were inspected.

## Shortcuts and registration

Saved options contain these exact identifiers:

```text
key_key.guideme.guide:key.keyboard.comma
key_key.astropunk_handbook_access.open:key.keyboard.f9
```

The comma rebinding belongs to native GuideME contextual help, not the whole-handbook opener. `OpenGuideHotkey` registers a graphical-interface-context binding. It watches item tooltips, resolves a page through `ItemIndex`, and requires holding the key for ten ticks. A plain press without an associated hovered item does not open the handbook home. Changing that binding cannot repair the helper's F9 action.

The installed helper's compiled `HandbookAccess` has the correct client `@Mod` identifier and a public constructor accepting `IEventBus`. The release-matching loader's `FMLModContainer.constructMod` accepts that injected parameter. This class registers listeners directly; it does not depend on an `EventBusSubscriber` annotation.

Compiled wiring contains all four listeners:

| Handler | Event bus and event |
| --- | --- |
| `registerKeys` | Injected mod bus, `RegisterKeyMappingsEvent` |
| `addInventoryButton` | NeoForge bus, `ScreenEvent.Init.Post` |
| `onClientTick` | NeoForge bus, `ClientTickEvent.Post` |
| `onInventoryKey` | NeoForge bus, `ScreenEvent.KeyPressed.Post` |

Lambda bootstrap descriptors retain the exact event types. The registration pattern matches GuideME's own release implementation. No missing subscriber or constructor registration was found.

The helper's world handler drains `consumeClick` and opens only when `Minecraft.screen` is null. Its separate screen handler accepts only survival and creative inventory screens, and runs after unhandled key input. Chat, pause, containers other than those inventories, a consumed earlier screen key, and other open screens are outside this path. An earlier screen handler consuming a key remains a possible conflict, not an observed cause.

The opener looks up `astropunk:handbook` and calls `GuideMEClient.openGuideAtPreviousPage(guide, guide.getStartPage())`. That direct endpoint is already present in the installed archive. It matches the client command endpoint; the prior common endpoint normally reaches the same endpoint through the client proxy. The latest log contains no `Failed to open guide.` exception. Absence of that exception does not prove the helper received F9.

## Inventory entry

GuideME's release source supplies contextual item help and a guide item, but no discovered native whole-book inventory button or recipe-browser toolbar button. The visible Astropunk entry is custom helper functionality.

The helper creates a translated 96 by 20 text button only on `InventoryScreen` and `CreativeModeInventoryScreen`. It reserves the inventory rectangle, creative tab padding and visible Minecraft widgets, then scans for free space. If placement returns empty, `Optional.ifPresent` does nothing. There is no fallback or warning.

A compiled probe using the actual `ButtonPlacement` class reproduced omission in a 344 by 194 logical viewport with a centered survival inventory. A 480 by 270 viewport produced a button. Saved graphical-interface scale is four, but actual window dimensions were not obtained. The compact example is a deterministic characterization of the implementation, not a measurement of Lucas's screen or proof of his missing-button cause.

`ScreenEvent.Init.addListener` is not inherently an invisible-input-only registration. The selected patched Minecraft `Screen.addEventWidget` adds a renderable listener to `renderables`, `children` and `narratables`. That mechanism was inspected in bytecode and is covered by the added wiring check.

Installed EMI is `emi-1.1.24+1.21.1+neoforge.jar`. Its public `EmiRegistry` exposes `addExclusionArea` and `addGenericExclusionArea`, which can keep the browser away from a custom inventory widget. The helper has no such integration and its placement only considers Minecraft widgets, not arbitrary browser panels. Browser overlap remains unverified.

The inspected `EmiRegistry` has recipe, stack, screen-bound, exclusion and related registration hooks, but no general custom toolbar-button registration hook. No native GuideME integration was found in the selected engine's class names or source. A recipe-browser entry would need a separately designed bridge; it should not be presented as a built-in toggle. The narrowest candidate visible entry is a compact inventory button with an explicit small-screen placement policy and an EMI exclusion area. That is a proposal, not an implemented fix.

## Refresh and caches

The latest profile log contains these positive observations:

| Time on October 9, 2026 | Observation |
| --- | --- |
| 11:40:58.983 | Resource manager reload included `file/astropunk-guide-preview` |
| 11:41:10.098 | Watcher started on the generated repository handbook folder |
| 11:42:33.655 | `Data driven guides: [astropunk:handbook]` |
| 11:42:33.659 | Loading 190 potential page files |
| 11:42:34.121 | Loaded 95 locale-selected pages from the watched source folder |
| 12:42:16.688 to 12:42:17.432 | Navigation rebuilds reported temporary unknown parents during a batch of edits |
| 14:44:03 and 14:46:40 | Page compiler warned about missing crossbow item identifiers |

The watcher path is `resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook` beneath the repository, not the copied profile resource pack. The profile preview directory is a normal directory, not a symbolic link. Watcher startup therefore proves explicit native source properties were effective; the helper's older symbolic-link-only `LiveEditing.configure` fallback was not needed in this run.

The 190 candidate files and 95 loaded pages are consistent with locale selection, not ninety-five rejected pages. Saved locale is `en_us`. The watcher strips translation prefixes and `MutableGuide.applyChanges` filters changes to the default and current language. A Chinese-only edit need not redraw an English page.

Released behavior was traced through `GuideBuilder`, `GuideSourceWatcher`, `GuideMEClient`, `MutableGuide` and `GuideScreen`:

1. Source properties are consumed when the guide is built.
2. The directory watcher parses Markdown changes and queues them.
3. The native client pre-tick calls `MutableGuide.tick`, which takes queued changes.
4. Changes update development pages, indices and navigation.
5. A matching currently displayed GuideScreen page is explicitly reloaded.
6. `getPage` compiles the current parsed page rather than reading a persistent compiled-page cache.

The navigation errors at 12:42 are evidence that watched changes reached navigation rebuilding after startup. They do not prove a later page remained current. A batch of writes can briefly make a child refer to a parent that has not arrived yet. No watcher failure or page-reload exception was found in the filtered log. No later full resource-manager reload line was found either, so the reported F3 and T attempt did not leave evidence of a completed second resource reload in this log.

Ordinary Markdown edits belong to the watched-source path. Non-Markdown assets and guide registration use resource-loading paths. Resource reload cannot replace already loaded helper Java classes. Changes to authoritative content are also not watched until the generator updates the generated Markdown. These distinctions should remain explicit in authoring instructions.

## Native command and query colors

Supported native syntax is a `Color` component around ordinary text:

```md
Type <Color color="#123456">/guidemec astropunk:handbook open</Color>.
Search for <Color id="gold">@create</Color>.
```

These are styled examples to type, not clickable command or browser-search actions. No backticks are required. The executed compiler probe preserved the exact command and query text and did not introduce italics.

| Attribute | Selected-release behavior |
| --- | --- |
| `color` | Quoted string accepting six-digit `#RRGGBB`, eight-digit `#AARRGGBB`, or the exact string `transparent` |
| `id` | Quoted symbolic color identifier, built-in name or a custom resolvable resource identifier |

`ColorTagCompiler` reads only `id` and `color`. If `id` is present, it takes precedence, even when resolution fails; a simultaneous valid `color` does not rescue an unknown identifier. Other attributes do not provide styling. In particular, `style="color: red"` alone reports the missing supported attribute rather than applying that style.

Executed acceptance cases were `#123456`, `#80123456`, `transparent` and symbolic `gold`. Executed compiler rejections were `#abc`, named `color="red"`, an expression-valued color, a style-only attribute, an unknown symbolic identifier and an unknown identifier combined with a valid color.

Do not confuse this component with the internal `Colors.hexToRgb` utility. That utility accepts shorthand and follows trailing-alpha notation, while the actual `Color` attribute path uses `MdxAttrs.getColor`, which requires six or eight digits and reads alpha first. Parser acceptance alone cannot catch these semantic differences.

Custom named colors are supported by the data-driven guide definition's `custom_colors`, with `dark_mode` and `light_mode` fields. Adding those definitions changes registration resources, not just watched Markdown. Visual contrast and rendering in the full pack remain untested here.

## Verification and files

Repeat the investigation probes from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python scripts/handbook-access/verify_access.py
```

The command rebuilds the existing helper without installing it, reruns its nine existing JUnit tests, runs five artifact wiring checks and three endpoint checks, and executes the native color and button-placement probes. The final run succeeded. The rebuilt helper checksum remained identical to the installed archive.

A deliberately disconnected inventory listener was compiled into an isolated test archive. The constructor-wiring test failed with three registrations instead of four, then passed against the real helper. This demonstrates a red-capable wiring guard. It is not a failing reproduction of the user's shortcut symptom. No original production source was changed to make a test pass, and no runtime fix is claimed.

Added test support:

- `scripts/handbook-access/test_access_wiring.py`
- `scripts/handbook-access/verify_access.py`
- `scripts/handbook-access/access-probe.gradle`
- `scripts/handbook-access/syntax-validation/VerifyNativeColor.java`
- `scripts/handbook-access/syntax-validation/VerifyButtonVisibility.java`

Execution records are under `scripts/handbook-access/build/access-investigation`, including `full-verification.log`, `negative-wiring.log`, `wiring.log`, `native-color.log`, `button-visibility.log`, `loader-screen-signatures.log` and `screen-bytecode.log`. These are local build evidence rather than distributed resources.

## Remaining uncertainty

The available evidence cannot identify whether the failed F9 attempt reached the operating system, Minecraft, the world handler or an inventory handler. There is also no measured viewport, current screen class, widget list or exact page-edit timing from that attempt. Those are the missing observations, not another opening endpoint.

A later authorized manual check should pair the current screen and logical dimensions with one deliberate F9 press, and pair an edit of the displayed English generated page with its source path and visible result. If dimensions reproduce omission, the visibility regression can then assert a guaranteed entry and drive a targeted compact-button fix. If input reaches the helper but opening fails, instrument that boundary before changing the endpoint. Do not install a replacement based only on these artifact checks.

No game was launched, no computer control was used, no installed helper or profile file was written, and no world, options or launcher setting was changed.
