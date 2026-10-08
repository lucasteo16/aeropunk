# Guide preview testing

Version: `0.3.0-guide.preview.1`.

This preview is built in the separate `guide/sandbox-handbook` worktree. It does not modify stable main, the Chunky branch or existing launcher instances.

## Import and open

Import `dist/astropunk-0.3.0-guide.preview.1-modrinth.mrpack` into Modrinth App as a fresh instance. Launch it and enter a disposable world.

Open chat and type `/guidemec open astropunk:handbook`. This is GuideME's client command, which does not require a book or server operator permissions.

The guide resource pack is included, and its enabled selection is supplied through Configured Defaults. If the guide is absent, check that `astropunk-guide-preview` is enabled under Resource Packs, then retry the command.

## What to inspect

- Open Process ores from Activities and return using its page link.
- Inspect the real item icons and tooltips.
- Check the ordinary iron-ingot recipe display.
- Check the Create processing displays. Unsupported recipe types require custom renderers; fallback behavior needs client verification.
- Rotate the interactive machine-model scene and hover its outlines. This scene is illustrative, not a functioning factory.
- Switch the game language to Simplified Chinese, reopen the guide and check both pages.
- Search the Chinese guide for `Crushing Wheel`. English aliases are included in its translated article. This does not establish English search behavior in the separate item browser.

## Scope and verification

Included: activity introduction, ore-processing article, English and Simplified Chinese versions, item images, recipe capability checks and an annotated scene.

Not included yet: spatial category map, direct item-browser or Ponder buttons, cooking companion and complete pack coverage.

Export success and archive checks are packaging verification, not a client startup or rendered gameplay test. No existing player world is used for this preview.

## Released documentation

Command, registration, translation and tag syntax were checked against GuideME source commit `52334ccacf15d763ffe318281d38dca8ec7aaeb8`, corresponding to selected release 21.1.19.

https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/docs/docs/40-commands.md
