# Parent research for the next correction batch

## Sources actually read

- https://raw.githubusercontent.com/PssbleTrngle/SliceAndDice/main/neoforge/1.21.x/README.md
  Web extraction cut this README midway through Automatic Cutting. Parent opened the raw document in the browser and read Automatic Cutting, Automatic Cooking and Sprinkler in full. This is current 1.21.x branch guidance, not a selected-tag guarantee. Slicer takes its tool by right-click, default allowed tools are knives and axes. Pot recipes become heated mixing recipes. Sprinklers are supplied through pipes; water applies wetness, fertilizer applies bone meal, potions affect entities, lava damages. No basis for asserting the sprinkler itself needs rotational power. Selected jar is sliceanddice-4.3.4-neoforge.jar and must settle numeric details/overrides.
- https://www.curseforge.com/minecraft/mc-mods/miners-delight-plus
  Publisher page read through the 1.20+ feature descriptions and beginning of older 1.19 section. 1.20+ says copper pot makes cup portions, half-size portions consumed twice as fast; Gossypium blooms on wild cave carrots and makes string. Knife-related animal drops are described. Old 1.19-specific probabilities and cup effects must not be copied to current selected NeoForge version without checking.
- https://modrinth.com/mod/miners-delight
  Publisher page extraction confirms the same 1.20+ copper-pot overview but truncates midway through the feature paragraph. Not a complete-source read.
- https://github.com/SammySemicolon/MinersDelight
  Repository identity/source link read, no substantial gameplay text extracted.
- https://github.com/Creators-of-Create/Create/wiki/Waterwheel
  Official historical wiki read. Its old recipe, flow-dependent speed and sixteen stress units per revolution per minute do NOT describe the selected Create 6.0.10 release. This is an example of why official documentation still needs a version check.

No video watched or transcript read in this research pass. Search results from generic recipe sites were discovery only and were not used as mechanics evidence.

## Rotation defect independently confirmed for the following chapter batch

Current machines.rotation presents configuration coefficients as total stress capacity, reporting water wheel 32 and large wheel 128. Exact selected Create 6.0.10 bytecode was inspected and saved under build/correction-round2:

- KineticNetwork.getStressMultiplierForSpeed returns absolute speed.
- Network capacity and stress multiply their base coefficients by this speed multiplier.
- WaterWheelBlockEntity.getGeneratedSpeed clamps flow score, multiplies by eight and divides by getSize.
- LargeWaterWheelBlockEntity.getSize returns two.
- With running flow and the configured 32/128 coefficients, small wheel output is 256 at eight revolutions per minute, large wheel output is 512 at four. Parent computed these with Python, not a guessed wiki value.

The existing handbook sentence claiming every speed increase doubles machine cost is also wrong: the selected multiplier is absolute speed, not an exponential step. Windmill and engine coefficients must likewise not be called fixed total output. Need actual ready-to-run first drive, Ponder entry and meaningful measurements when this topic is rewritten.

## Parent next-topic review

Parent read machines.rotation, storage.handling, storage.bulk and machines.logistics in full. Existing defects include explanatory relationships encoded as item strips; generic inventory filler; a prose-only trash section; no exact item-filter operation; vague vault-join success checks; no exact belt installation or arm configuration; and unsupported generalizations such as every delivery failure being funnel direction. Those need gameplay documentation and selected versions, not another coefficient-only audit. Twenty-seven further topic bodies after the current five-food batch are indexed in build/correction-round2/remaining-chapter-triage.json. That file is mechanical triage, not acceptance.
