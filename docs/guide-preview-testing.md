# Handbook testing

Version: `0.3.0-guide.light.2`. Based on light main at `34cb006`, maintained on `test/guide`.

## Existing authoring instance

The dedicated light guide instance has the compiled access helper and a normal resource-pack folder installed. Its former symbolic link was rejected by Minecraft and has been archived. Other instances and worlds are untouched.

In this instance's launcher settings, append the two official GuideME Java arguments from guide-live-preview-java-arguments.txt without removing existing arguments. Computer use is currently prohibited, so Lucas performs this launcher setting change. Start the same instance, enable Astropunk Handbook under Resource Packs, and apply the selection. Minecraft previously removed it when rejecting the symbolic link.

Use the inventory Handbook button or F9. Configure Open Astropunk Handbook in Options, Controls and Key Binds. GuideME's native source setting points directly to the repository Markdown folder, which the engine watches for ordinary page changes. The installed normal copy provides registration and packaged fallback resources. Helper code changes still require a restart; registration and resource-pack asset changes may require a resource reload.

The normal folder and its 200 files have been checked. Java arguments, guide loading and live refresh still need verification after Lucas completes the launcher setting.

## Fresh package

The native export is `dist/astropunk-0.3.0-guide.light.2-modrinth.mrpack`. Fresh imports receive the same helper and handbook pages, but automatic source watching is limited to symbolic authoring resources. Ordinary distributed directories do not enable authoring mode.

The fallback command confirmed by Lucas is `/guidemec astropunk:handbook open`. If the handbook is missing, check that its resource pack is enabled.

## Runtime checks

- Open from survival and creative inventory. Confirm the button does not overlap other controls or the recipe browser.
- Open with F9 in the world and inventory. Rebind it and confirm the replacement works. Confirm text-entry screens remain unaffected.
- Return from the handbook and check the preceding interface remains usable.
- Change a page while reading it after the initial restart. Confirm the native watcher refreshes its content.
- Check the Astropunk catalog, mod tables, item tooltips, controls labels and recipes in English and Simplified Chinese.
- Check ore-processing icons and outputs against the actual item browser. The Millstone crafting recipe uses the native renderer; milling, crushing and washing comparisons use verified recipe data because this release has no Create processing renderer.

## Verified and remaining

The helper rebuilt from retained source with nine passing tests. Artifact inspection confirmed client distribution, exact released public opening methods, the F9 default, both locales and absence of a bundled engine or competing guide registration. The installed helper matches the built and packaged bytes.

The released Markdown parser accepted all 198 handbook pages and rejected its malformed-tag negative control. Source checks cover locale parity, links, complete installed-content coverage, unchanged baseline mod metadata and player-facing wording. Native archive checks compare resource bytes and the bundled helper.

No game was launched or closed for these checks. Rendered button placement, shortcut behavior, multiplayer and native live refreshing remain runtime-untested. Chinese navigation and authored articles are translated; exhaustive publisher-description tables still contain English source summaries.
