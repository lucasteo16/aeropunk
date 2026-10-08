Historical reference from the retired combined experiment. This does not describe the current edition or testing plan.

# Java 25 trial

Astropunk currently targets Minecraft 1.21.1 and NeoForge 21.1.255. Java 25 is an optional runtime trial, not the validated pack baseline.

## Saved launcher settings

The local Modrinth installation stores instance launch settings in its application SQLite database, in the `instance_launch_overrides` table. The `overrides` field contains the instance settings.

Read-only inspection confirmed these settings for Lucas's Aeropunk performance.4 test instance:

- `java_path` selects an installed Zulu Java 25 executable.
- `extra_launch_args` contains the single argument `-XX:+UseZGC`.

The absolute executable path is specific to that computer and is deliberately not copied into the repository. No launcher database, account information, instance identifiers or world data is distributed.

## Apply the trial

In Modrinth instance settings, enable Custom Java installation and browse to an installed 64-bit Java 25 executable. Enable Custom Java arguments and enter:

```text
-XX:+UseZGC
```

Preserve unrelated launch arguments. Remove competing collector selections and G1-specific tuning if present. Keep memory allocation under the player's control. Do not add `-XX:+ZGenerational` for Java 25.

To revert, disable the custom Java installation and custom Java arguments to restore launcher defaults, provided the global arguments do not also select this collector.

## Packaging limitation

The standard Modrinth pack format has no Java runtime selection or launch-argument field. These settings are launcher database state, not game configuration files. Placing a copy of the database record in pack overrides does not apply it on import.

This document preserves the trial settings in version control. It is excluded from game exports by the existing documentation exclusion. Current native exports do not automatically enable Java 25 or its collector. No custom launcher installer or database-writing mechanism has been added.

## Verification

The saved Java selection and argument were confirmed through a read-only database query. This does not establish that Minecraft has launched successfully with Java 25 or that performance has improved.

## References

- https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack
- https://openjdk.org/jeps/490