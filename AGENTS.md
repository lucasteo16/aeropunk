# Project rules

## Branch permission

Do not create a new Git branch without Lucas's explicit advance permission for that branch. This includes `git branch`, branch-creating checkout and switch commands, branch-creating worktree commands, remote branch creation and equivalent library calls. A request to update, synchronize, export or test does not grant this permission. Do not create trial or edition companion branches implicitly.

## Releases and editions

Use the seven existing active branches: `dev`, `main`, `main-heavy`, `main-light`, `admin/hosting`, `admin/hosting-light` and `admin/worldgen`. Integrate accepted shared changes on development, promote to Main, then synchronize the established downstream editions. Hosting Light inherits Hosting; world generation inherits development. Preserve edition-only additions, settings and Light's exact declared exclusions. Keep the display name exactly `Astropunk`, one agreed base release version and the established edition suffixes.

Use existing native build commands from each edition's own checkout. Hosting and Hosting Light are the primary requested Modrinth deliveries. Do not invent branches, overlay exporters or ignored source snapshots to generate an accepted edition. Source synchronization does not authorize pushing, live-server changes, installed-instance edits, launching tests or exporting unrequested editions.

Preserve unrelated work and credentials. Do not read or distribute private authentication settings. Keep configuration migrations and intentional tuning aligned with the accepted shared release. Verify indexes, edition membership, shared-source ancestry and exported contents. Report runtime acceptance separately from packaging checks.
