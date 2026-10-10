# Astropunk main menu

## Scope

This feature customizes only `net.minecraft.client.gui.screens.TitleScreen`. The ship screenshot remains separate from the transparent Astropunk title. A static translucent black image overlay reduces background brightness by about 38 percent; native controls render above it. The title is centered at the top, 280 by 52 logical pixels, with a 30 pixel top offset. The old Minecraft logo and splash are hidden. Minecraft branding and copyright remain visible.

Singleplayer, Multiplayer, Realms, Options, Quit, language, accessibility and mod-provided controls retain their original widgets, placement, actions, keyboard navigation and translated labels. English and Simplified Chinese therefore use the existing Minecraft and mod translations, rather than fixed English replacement buttons. No new action scripts, music, browser content, downloads at menu time, GUI scale, keybinding changes, world changes or window overrides are configured.

This is a statically validated implementation awaiting an authorized fresh-client visual and interaction check. No game, desktop automation, launcher import or live installation was used.

## Exact additions

All three entries were added through native packwiz commands with explicit project and version identifiers. All are client-side pack entries, with no update holds.

| Metadata | Canonical name | Selected release | Modrinth project | Modrinth version | Purpose |
| --- | --- | --- | --- | --- | --- |
| `mods/fancymenu.pw.toml` | FancyMenu | 3.9.14 for NeoForge 1.21.1 | Wq5SjeWM | P9dDosz2 | Main-menu layout and image loading |
| `mods/konkrete.pw.toml` | Konkrete | 1.9.9 for NeoForge 1.21 | J81TRJWm | stJDU839 | Required FancyMenu utility and configuration library |
| `mods/melody.pw.toml` | Melody | 1.0.10 for NeoForge 1.21 | CVT4pFB2 | efcdRVZP | Required FancyMenu audio library, although this menu adds no audio |

Selected FancyMenu archive declarations require Konkrete at least 1.9.4, Melody at least 1.0.6, NeoForge at least 21.1.47 and Minecraft at least 1.21.1. Both library archives require NeoForge at least 21.0.20-beta and Minecraft at least 1.21. No additional mandatory external mods were declared. The pack's Minecraft 1.21.1 and NeoForge 21.1.255 satisfy these lower bounds. Declared compatibility is not full-pack runtime clearance.

Packwiz did not recognize FancyMenu's `client_only_server_optional` provider environment or Melody's `unknown` environment and initially marked both as shared. The three new entries were narrowly corrected to `side = "client"`; Konkrete is client-used here, not intrinsically incapable of server use. No baseline provider metadata was changed.

## Loader semantics

- `config/fancymenu/customizablemenus.txt` enables customization for the title-screen class only.
- `config/fancymenu/customization/astropunk-title.txt` is a native `fancymenu_layout` PropertyContainer file. FancyMenu loads layout files from this directory. The `layout-meta` identifier targets the same title-screen class.
- One `menu_background` uses the released `image` builder and `image_path`. The screenshot preserves its aspect ratio. FancyMenu 3.9.14 keeps only the first background per registered builder in a layout, so the shade is an ordinary image element, not a second image background.
- `source` and `image_path` use the released `[source:local]` prefix. The leading slash resolves relative to the game directory, not the operating-system root.
- The shade uses the released `%guiwidth%` and `%guiheight%` aliases, which enable element stretching. The top-centered title uses a sticky anchor. Both image elements render behind native widgets, in shade-then-title order.
- Only `minecraft_logo_widget` and `minecraft_splash_widget` receive hidden-widget overrides. Functional buttons are not replaced or targeted.
- `configureddefaults/config/fancymenu/options.txt` supplies only the FancyMenu editor-toolbar preference. Konkrete's native parser consumes `##[customization]` and `B:show_customization_overlay = 'false';`. The existing Configured Defaults mechanism copies this ordinary file only when absent, preserving an established FancyMenu options file. It does not merge individual entries into existing files. Players retain the library's remaining defaults, including normal menu music and automatic GUI scale.
- `.packwizignore` includes a narrow exception for that nested options template, because its broad `options.txt` rule would otherwise omit it.

## Assets and attribution

`config/fancymenu/assets/astropunk-title-transparent.png` is byte-identical to the reusable approved title at `/home/tsb/Hermes/research/astropunk-branding/astropunk-title-transparent.png`. It is 2162 by 405 pixels with real transparent and opaque pixels, and 167 distinct alpha levels. The lettering reads ASTROPUNK.

`config/fancymenu/assets/home-merun173-airship.png` is byte-identical to the handbook's existing `images/home-merun173-airship.png`, 1600 by 900 pixels. The screenshot is not regenerated or retouched. The shade is a separate one-pixel RGBA PNG, black with alpha 96 out of 255.

The ship build and image are attributed to Merun173 at https://createmod.com/author/merun173. Attribution does not establish redistribution rights; those rights have not been independently established. Resolve permission before public distribution.

## Verification

Executed against the actual selected FancyMenu 3.9.14 and Konkrete 1.9.9 binaries:

- Native PropertyContainer parsing of both shipped files.
- Serialization round trip.
- A malformed negative control rejected for missing type. Its expected error log is part of the test.
- Main-menu-only screen targeting, one background, two image elements, local asset existence and functional-widget preservation checks.
- Native Konkrete parsing of the hidden-editor-toolbar preference.

Result: `PASS released FancyMenu 3.9.14 parser, round trip, negative control, menu scope, local assets and Konkrete 1.9.9 options parser`.

Separately verified publisher SHA512 checksums for all three downloaded artifacts and inspected their `META-INF/neoforge.mods.toml`. Compared all 285 baseline provider metadata files against a pre-addition snapshot: all remained byte-identical, with exactly the three expected metadata additions. The handbook helper archive is owned by the concurrent parent task and is excluded from that baseline-provider comparison. Both source artwork copies are byte-identical; decoded title alpha bytes prove actual transparency.

The permanent probe is `tests/main-menu/MainMenuParserProbe.java`. With a Java 21 or later development kit and a classpath containing the exact FancyMenu and Konkrete archives, Log4j API and implementation, and Commons IO, run from the repository root:

```sh
java -cp "$MENU_PROBE_CLASSPATH" tests/main-menu/MainMenuParserProbe.java "$PWD"
```

The libraries are test prerequisites, not extra pack entries. Full layout deserialization, GPU texture loading, resizing, actual button navigation and the complete pack's startup have not been executed. Visual validation must still check the supported window sizes and both locales.

The parent owns final inventory reconciliation, native packwiz refresh, versioning, export, commit and push. No shared index refresh was run after handoff ownership was clarified; the final menu asset and side changes require that refresh before distribution. No export or commit was made.

## References

- https://modrinth.com/mod/fancymenu/version/P9dDosz2
- https://modrinth.com/mod/konkrete/version/stJDU839
- https://modrinth.com/mod/melody/version/efcdRVZP
- https://docs.fancymenu.net/docs/en-US/data-storage-locations
- https://docs.fancymenu.net/docs/en-US/resources
- https://docs.fancymenu.net/docs/en-US/vanilla-elements
- https://docs.fancymenu.net/docs/en-US/menu-backgrounds

Configuration field names and behavior were checked against the exact released deserializers, not inferred from editor screenshots or an unrelated modpack.
