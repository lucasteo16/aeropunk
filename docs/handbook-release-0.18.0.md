# Handbook refinement release 0.18.0

Combat, Food and farming, Machines and storage, and Transport are accepted for the same release. Development retains `0.18.0-dev`; stable and edition branches use `0.18.0` with their existing edition suffixes. Transport does not trigger another increment.

## Final corrections

Every tutorial action has the play image and compact English and Chinese labels. Recipe-browser actions use the actual short query. Transport catalogs keep bounded icon rows outside width-filling table cells, and its height charts have separate language assets.

Create mechanical crafting is described in text and linked to the item browser. Its unsupported handbook recipe diagrams were removed at Lucas's request. Internal Simulated paired-docking and merging-glue blocks are not item references: the guide shows the ordinary docking connector and uses a Slime Ball for merging.

The exact Transport source and resource closure is `transport-final-review.json`. Prior review evidence is preserved separately. Invalid historical references have explicit per-topic dispositions in `transport-reference-corrections.json`; arbitrary missing identities remain blocking. Parser and structural-fixture checks are not in-game rendering or registry certification.

## Integration scope

Approved flow: Transport into local development, development into main, main into Heavy, Light and hosting, and development into private world generation. Preserve edition-only additions and removals, including the deployed hosting recipe-browser additions and authentication. Do not flow hosting or world-generation additions upstream.

The handbook changes alter client assets and authoring evidence, not gameplay mods or server settings. Release synchronization and exports do not deploy to a server or update played clients. Remote publication is separate from local branch synchronization. The dirty historical branch checked out in the directory named astropunk-dev remains untouched.
