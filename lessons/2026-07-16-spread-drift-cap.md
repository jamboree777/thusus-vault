---
type: lesson
date: 2026-07-16
trigger: "ROAM #7911 (kucoin→bitget, entry spread 7.03%, expected +$13.50 → realized −$8.61, a −$22.1 drift); ELIZAOS #7897 (gateio→bybit, spread 2.56%, expected +$8.32 → realized −$10.24). |drift| vs entry-spread correlation 0.485 across settled livescan trades."
problem: "Wide entry spread predicts adverse 5-minute drift — a large touch-to-touch gap is priced by the market's uncertainty about the name, and entries above a spread threshold carry uncompensated reversal risk regardless of token."
change: "Livescan NW_PAPER_MAX_SPREAD_PCT: off → 3.0. Sniper NW_BIGSPIKE_MAX_SPREAD_PCT: off → 10.0 (DELIBERATE deviation — see below)."
expected_effect: "Livescan: 2-day sim of the 3% cap = +$7.6 net (fewer wide-spread reversal tails), no effect on the median grind. Sniper: near-zero effect at 10% (its edge lives at <1% spread), loose cap only trims pathological books."
review_after: 2026-07-23
status: active
supersedes: null
---

# The spread is the market pricing its own doubt

Two of day one's three [[expectation-gap]] tails were wide-spread entries that reversed inside the [[five-min-settlement]] window:

- [[ROAM]] **#7911** — entered on a **7.03%** touch-to-touch spread, expected **+$13.50**, settled **−$8.61**. The book moved **−$22** against the position in five minutes.
- [[ELIZAOS]] **#7897** — **2.56%** spread, expected **+$8.32**, settled **−$10.24**.

Across all settled livescan trades, the absolute five-minute drift correlates with the entry spread at **0.485**. That is not noise. A big touch-to-touch gap is not free money the market forgot to collect — it is the market *pricing its own uncertainty* about the name. The wider the spread, the more the book is telling you it does not know where this thing trades, and the more likely the next five minutes reprices it against you.

## The class of mistake

The generalisable rule: **entry spread is a leading risk signal, not just an opportunity signal.** A high headline spread inflates expected net (the [[quiet-size]] walk still prices it), so the net gate happily admits it — and then the [[expectation-gap]] eats it on settlement. Capping the entry spread refuses the trades whose expected edge is an artifact of a book that is about to move. This applies to any venue and any token; it is conditioned on the spread, not the symbol.

## The change — and a flagged deviation

Livescan gets `NW_PAPER_MAX_SPREAD_PCT = 3.0`: reject when the VWAP buy→sell spread exceeds 3%. The 2-day sim nets **+$7.6** and leaves the median trade untouched.

**Deviation, stated plainly for Robin.** The decision sheet proposed a fund-wide 3% cap. I did **not** apply 3% to the big-spike sniper. The sniper's entire mission is capturing *rare, large, real* cross-venue gaps — and its own worst tail, [[FOXY]] **#7903**, entered at just **0.955%** spread. A 3% cap has **zero supporting evidence** on the sniper and would sit far outside where its edge actually lives, so it would only ever fire on genuinely pathological books while doing nothing about the real reversal risk (which B-2's size haircut addresses instead). The sniper therefore gets a *separate, loose* safety cap, `NW_BIGSPIKE_MAX_SPREAD_PCT = 10.0`, and both engines log a distinct `spread_cap` reject binding so the cap's bite is measurable. **If Robin wants strict 3% everywhere, it is one env change:** set `NW_BIGSPIKE_MAX_SPREAD_PCT=3.0`.

## Review

By 2026-07-23: how many livescan entries did `spread_cap` block, and what was their would-be realized P&L versus the entries that passed? If the blocked cohort was net-positive we over-tightened; if it was net-negative (as the sim predicts) the cap earns its place and we can consider lowering the sniper's 10% toward the evidence.

_Related: [[ROAM]] · [[ELIZAOS]] · [[FOXY]] · [[expectation-gap]] · [[five-min-settlement]] · [[quiet-size]] · [[executable-spread]] · [[Thusus]]_
