# Archived automation tests

The twelve original tests are preserved unchanged for reference, not maintained as an executable suite. Their imports assume the old tests directory and several assert wrapper behavior intentionally removed. The unit recipe has been removed. Pack exports are now packwiz commands, not custom Python export processing.

| Original test | Original purpose | Verdict |
| --- | --- | --- |
| test_preserves_cache_dist_and_unknown_build_content | Restrict cleanup to disposable outputs and bytecode. | Archive test, retain scoped cleanup guards in runtime. |
| test_rejects_symlinks_and_traversal_before_deletion | Reject unsafe filesystem cleanup targets. | Archive test, retain safe_path guards in runtime. |
| test_unconfirmed_docker_cleanup_preserves_runtime_and_reports | Keep runtime until Docker resource cleanup is confirmed. | Archive test, retain capture cleanup gate. |
| test_reports_captured_before_temporary_removal | Save latest evidence before removing runtime files. | Archive test, retain report-before-cleanup ordering. |
| test_client_export_uses_default_cache | Check wrapper invokes native export without a cache override. | Archive as obsolete wrapper test. Direct recipes use the default cache. |
| test_export_replaces_latest_atomically_without_archiving | Check custom staging, atomic replacement and preservation of other releases. | Archive as obsolete. Packwiz now owns output writes, with no wrapper atomicity promise. |
| test_failed_export_preserves_latest | Ensure staged wrapper failure preserves an older distribution. | Archive as obsolete wrapper guarantee. Native packwiz owns failure behavior. |
| test_server_export_uses_default_cache_and_normal_cli | Check mocked server export command and extracted archive. | Archive as obsolete mocked export. A real archive installation is exercised instead. |
| test_ready_immediately_stops_and_cleans_up | Require stop at readiness without an observation delay. | Archive test, retain immediate normal stop in smoke. |
| test_early_exit_still_cleans_up | Clean resources after a pre-readiness failure. | Archive test, retain finally cleanup and early-exit failure. |
| test_unsupported_refs_and_unsafe_paths_fail_before_extraction | Reject CurseForge references and unsafe override paths. | Archive. Reference rejection was wrong; retain a read-only unsafe-path check, and delegate extraction to the installer. |
| test_missing_server_artifact_is_rejected_before_runtime | Compare all physical archive jars against selected metadata. | Archive as invalid for reference-based exports. Existing installer resolves archive references and verifies downloads; startup remains decisive. |

Runtime checks retained include fresh installation, archive integrity and safe paths, exported loader versions, bounded readiness, normal stop confirmation and zero exit status, report capture, and confirmed container and network cleanup before disposable removal. No custom all-physical-jar inventory is retained.
