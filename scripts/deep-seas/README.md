# Deep Seas local build

- Upstream: https://github.com/MaxCreateMC/Create-Deep-Seas
- Exact commit: `020c4fc6612051a76220ab003e2b41ae965a1edb`
- Local artifact: `mods/create_submarine-3.4.6-astropunk.1.jar`
- Internal mod version: `3.4.6`
- SHA-256: `fe9f90e5e8480e5951f62339f2f252bc060dce67998290aa90ba42f6ab36e6e6`

Apply `upstream.patch` to that commit in a separate clone, using a detached checkout, not a new branch. The patch contains the one-line pressure-scan repair and a build-only substitution for the author's hardcoded Windows deployment directory. It does not alter shader code or build dependencies.

With a Java 21 development kit selected through JAVA_HOME, build with:

```sh
bash ./gradlew jar --no-daemon --console=plain -Dorg.gradle.java.installations.paths="$JAVA_HOME"
```

The native build produces `build/libs/create_submarine-3.4.6.jar`. Rename a copy to the local artifact filename above. Never use the build's development client task as a substitute for the pack's official-launcher test. Do not invoke the author's auto-copy task or copy to a played instance.

The already tested artifact is tracked so normal pack exports and fresh source clones do not require a local compiler or an unavailable download URL. Rebuilds can have a different checksum because the upstream build embeds a build timestamp; validate the exact source, patch, mod metadata, dependencies and test evidence before replacing the approved artifact. A matching internal version alone does not identify our patched build.

This derivative retains the upstream All Rights Reserved license. Do not publish or upload it without reviewing permission. Keep the custom artifact and patch local until such publication is authorized. Retire the local replacement only after a corrected published release has been evaluated, avoiding duplicate Deep Seas archives.
