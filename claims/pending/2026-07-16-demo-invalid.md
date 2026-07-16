---
claim_type: dw_change
token: BLAST
source_url: https://upbit.com/service_center/notice?id=4321
observed_at: 2026-07-16T09:00Z
contributor: "@demo_researcher"
status: pending
type: claim
---

# Claim — DEMO (now valid, proves the check passes)

This file was intentionally malformed in the first commit of this PR to prove
the **Validate claims** Action fails a bad claim. It is now corrected to a valid
claim to prove the check passes, and is removed in the next commit so
`claims/pending/` stays clean on merge.

## Source

`source_url` above points to Upbit's own notice that BLAST (blastnet) deposits
reopened at 2026-07-16 09:00 UTC.
