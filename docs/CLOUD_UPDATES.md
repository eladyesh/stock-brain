# Cloud update migration

The ChatGPT/Sites daily task was disabled at the owner's request on 2026-10-22.

The supported replacement is the standalone application described in [STANDALONE.md](STANDALONE.md). Render runs collection code; GitHub Actions backs up the four validated payloads to `automation/research-data`. No ChatGPT task or connected-app session is required at runtime.

Do not resume the retired task. Keep the legacy GitHub disclosure collector gated because its hosted runner encountered source-access failures. The new GitHub workflow reads the public app checkpoint and does not collect from SEC or issuer sites.
