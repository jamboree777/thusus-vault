---
claim_type: rumor
token: BLAST
source_url: i-heard-it-somewhere
observed_at: last tuesday
---

# Claim — DEMO INVALID (exercises the schema check)

This file is intentionally malformed to prove the **Validate claims** Action
fails a bad claim: `claim_type` is off-whitelist, `source_url` is not an
http(s) URL, `observed_at` is not ISO-8601, and `contributor` is missing.
It is fixed/removed in the same PR before merge.
