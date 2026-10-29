# Shared recipe-browser additions

These general recipe-browser features belong to the shared pack, not exclusively to Hosting. They were originally delivered in the targeted 0.17.0 hosting update and are now included in the working definitions for development, Main and the active downstream and update editions.

| Component | Selected version | Pack side |
|---|---|---|
| EMI Recipe Sharing | 1.0.4 | Client and server |
| WorldGen | 1.4.5 | Client and server |
| Moderately Enough Effect Descriptions | 8.1.0 | Client and server |
| EMIffect | 2.1.6 | Client only |

EMIffect is the existing hosting display companion for the additional effect descriptions. Keep it client-only; adding description data without an effect viewer would not provide the intended client feature. The pack already includes EMI and Just Enough Items. WorldGen is the selected world-generation information viewer; do not add EMI Ores as a duplicate replacement.

Exact selections, download hashes, side flags and provider tracking match the existing hosting definitions. The correction does not update their versions, change gameplay configurations or promote the separate global-update payload into stable branches. All existing pack versions remain unchanged by explicit request.

EasyAuth, authentication settings and the hosted-server address remain hosting-specific. Other hosting additions have not been moved by this narrowly scoped correction.

Provider relationships and checksum-verified native metadata were inspected. The selected EMI and NeoForge versions satisfy the declared minimums. Historical hosting server startup evidence and its known limitations are recorded in the hosting branch's `docs/emi-hosting-update.md`: some effect-source recipes depend on an unavailable serializer, and WorldGen data coverage and live recipe-sharing behavior are not fully established. This tracking correction does not claim to resolve those limitations or establish new gameplay acceptance.

No server upload folder, installed client, running server, launcher profile, remote branch or Git history is changed by this source correction. The source edits remain uncommitted until a commit and normal-merge checkpoint is authorized. Do not infer shared Git ancestry from matching working-tree definitions alone.
