---
claim_type: dw_change
token: BLAST
source_url: https://nightwatch-v1-api.onrender.com/kg/BLAST.md
observed_at: 2026-07-16T10:55Z
contributor: "thusus-vault-bot"
status: pending
type: claim
---

# Claim — Upbit resumed BLAST (Blast network) deposits

## What you observed

Upbit resumed BLAST (Blast network) **deposits**; the transfer door on
[[BLAST]] at [[upbit]] is open again. This is a single [[transfer-feasibility]]
state change: deposits moved from blocked back to open.

## Source (mandatory)

`source_url` above points to the live NightWatch Knowledge Graph note for BLAST,
which currently reports `transfer: open`. Quoted line from the note:

> transfer: open

This is a machine-checkable claim: NightWatch reads exchange deposit/withdrawal
state directly, so the note reflects the resumed-deposit condition and the claim
can merge as `[verified]` once review confirms it.

## Why it matters

This flips [[transfer-feasibility]] on [[BLAST]] at [[upbit]] from blocked back
to open, closing the [[mirage-arb]] window described in
[[events/2026-07-13-blast-wallet-lockdown]]. A stranded gap becoming real is the
instant it is worth acting on.

---

**What happens next:** this claim lands in `claims/pending/` and is never
rendered as fact until it clears the deterministic gate → AI review → machine
probe. See [[claims/pending/README]].
