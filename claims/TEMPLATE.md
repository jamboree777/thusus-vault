---
claim_type: dw_change      # dw_change | delist_notice | contract | team_event | liquidity | listing
token: BLAST               # base symbol, or a venue/chain id
source_url: https://       # MANDATORY — a claim with no source is auto-rejected
observed_at: 2026-07-16T09:00Z
contributor: "@handle"
status: pending            # pending → verified | community-reported | rejected (set by review, not you)
type: claim
---

# Claim — <one-line summary>

> Copy this file into `claims/pending/`, rename it descriptively
> (e.g. `2026-07-16-blast-upbit-deposit-reopened.md`), and fill it in.
> Open a pull request, or submit through the in-app form.

## What you observed

State the single factual change you are claiming, plainly. One claim per note.
Example: "Upbit reopened BLAST (Blast network) deposits at 2026-07-16 09:00 UTC."

## Source (mandatory)

Paste the exact URL in `source_url` above **and** quote the relevant line here.
No source, no claim — the deterministic gate auto-rejects a claim without a
reachable source. Prefer primary sources: the exchange's own notice/announcement
or coin API, an official project channel, or an on-chain transaction. Media
reports are accepted but will be tagged `[community-reported]`, not `[verified]`.

## Why it matters (optional)

If this unblocks a decision — a [[transfer-feasibility]] flip, an [[identity-verification]]
correction, a [[nw-grade]]-relevant liquidity change — say so. Price-impacting
claims are prioritized and bounty-priced by their gap value.

---

**What happens next:** your claim lands in `claims/pending/` and is **never rendered
as fact**. It passes a deterministic gate (source reachable? schema valid? does it
contradict the database?), then AI review (does the source actually say this?), then,
where possible, a machine probe (we hit the exchange API and *know*). Only then does
it merge as prose with a `[verified]` or `[community-reported]` tag. Facts change
only when NightWatch's own measurement confirms them. See [[claims/pending/README]].
