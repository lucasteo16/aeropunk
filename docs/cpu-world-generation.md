# Processor-side generation baseline

Release `0.14.0-dev` aligns the base Concurrent Chunk Management Engine with the administrator worldgen pack at `0.4.0-alpha.0.123+1.21.1` and adds Fast Noise `1.0.13+1.21.1+neoforge`.

No custom optimization settings or launch arguments are applied. Preserve the defaults. Fast Noise needs no graphics acceleration. The OpenCL addon, its bundled acceleration libraries and ScalableLux are absent from development. Existing unrelated libraries remain unchanged.

The administrator worldgen branch accepts this development update downstream and retains the OpenCL addon exclusively. Never merge the administrator branch back into development or stable branches.

## Verification

The native Modrinth export was installed using the existing disposable Docker server test. It reached readiness on a fresh temporary world, saved all dimensions and shut down with exit code zero. The installer replaced base engine build 122 with build 123, and discovered Fast Noise and DimWorldBorder. No error-level lines named the two processor optimization identifiers; other error-level messages remain in the wider pack, so startup is not an error-free-pack claim.

Evidence remains in ignored `reports/result.json` and `reports/server.log`. This test establishes installation, startup, initial world generation, saving and shutdown. It does not establish sustained pregeneration speed, client rendering, planetary terrain parity, ship behavior or independent border persistence.

Sources:

- https://modrinth.com/mod/c2me-neoforge
- https://modrinth.com/mod/zfastnoise
