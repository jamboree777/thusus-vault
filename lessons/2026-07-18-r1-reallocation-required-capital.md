---
type: lesson
date: 2026-07-18
trigger: "W-FUND-2 (Robin): optimize the fund's required capital under the R1 reallocation and make the Quartermaster actually execute it. Plus Robin's honesty correction — DEDUPLICATE cross-engine duplicate opportunities in the back-solve so one gap = one capital draw, not two."
problem: "The honest back-solved fund (W-FUND-1) sized each venue at its deepest cumulative deficit assuming NO reallocation — bithumb dominated (~$21k) because hedged + woncarry-discount buy at bithumb and ship offshore, and the drained USDT never came back. Fully-static required capital had grown to ~$44k. The QM executor existed but only did a flat bithumb top-up + stats-floor refills, was BLIND to the woncarry/hedged Korea-leg buys (only read nw_paper_trades), and did not implement Robin's chosen R1 conservation policy."
change: "Part 1 — set the OPTIMIZED initial allocation to the R1 back-solve (bithumb-origin conservation, $500 trigger, NO 50% clause): inject R1's transfers into the replay, ceil each venue's deepest deficit to $1k. Cross-engine opportunity DEDUP added (group by base+buy_ex+sell_ex within ~10min, keep the covered/hedged execution) and applied IDENTICALLY in the /arb/thusus/fund reconstruction so the live replay can never double-draw. To make the R1-sized allocation coherent in a chronological replay, populated nw_qm_transfers with the R1 conservation LEDGER — net-zero capital returns of genuinely-accumulated bithumb-origin USDT at the real trigger timestamps (tools/nw_realloc_backtest.py --apply-r1 --write-alloc --write-r1-ledger). Part 2 — QM executor now runs R1 in 3 modes on the unified fund: R1 BATCHING (event, ≥$500 → netted return to bithumb), PRE-EMPTIVE (once/UTC-day, forecast-driven Korea top-up from offshore surplus), IMMEDIATE ($40 next-trade floor safety). Fixed the blind spot: _venue_stats now unions buy-venue consumption across all four engines. Prefers arb-as-rebalance."
expected_effect: "Required capital: $44k fully-static → $29k with R1 running (−$14k, ~33%), bithumb $21k → $3k. Live /arb/thusus/fund: initial_fund_total $29,000, invariant_ok=true, capital_short $17,156 → $0 (R1 ledger keeps bithumb funded, reconstructed $3,695), recent_transfers reflect R1 batching. QM going forward: R1 correctly fires only on ≥$500 fresh bithumb-origin accumulation (observed $291<trigger → no fire); pre-emptive recycles idle gateio surplus into bithumb runway (observed $2,500 gateio→bithumb); immediate armed and quiescent (no venue below $40 = healthy). capital_short only surfaces when genuinely uncoverable — never fabricated."
review_after: 2026-07-25
status: active
supersedes: ""
---

# R1 reallocation: required capital $44k → $29k, and the QM now executes it

Robin's W-FUND-2: two deliverables in one. **(1)** re-size the fund's honest
required capital assuming the reallocation the Quartermaster will actually run
(not a static fund that never moves a dollar), and **(2)** make the QM execute
that reallocation — R1, the winning policy — going forward, on the *unified*
fund, seeing *all four* engines.

## The number — two honest figures for the investor group

The back-solve replays every settled/pending trade from the fund epoch, starts
each venue at zero, and takes its deepest cumulative deficit (ceil $1k + 5%
buffer). Run it two ways:

| basis | required capital | bithumb |
|---|---:|---:|
| RAW fully-static (no reallocation) | **$44,000** | $21,000 |
| **R1-optimized** (QM reallocation running) | **$29,000** | **$3,000** |

R1 = **bithumb-origin conservation**: track the USDT that bithumb's Korea-leg
buys ship to global venues on settle; when ≥ **$500** has piled up, batch it back
to bithumb (one netted transfer, largest holder first, never drawing a global
desk below its own floor). **NO 50% clause.** Because bithumb keeps getting
refilled from its *own* returning capital, its deepest deficit collapses from
~$21k to ~$3k; offshore venues are sized a little higher (they hold the in-flight
USDT longer), net **−$14k / ~33%**. Investor story: *"$44k guaranteed
fully-static; $29k with the Quartermaster's R1 reallocation running."*

## Robin's dedup correction — and the honest finding

Robin flagged that livescan/hedged/woncarry independently scan the same
`/arb/board` feed, so the same gap could be entered by more than one engine and
counted as two capital draws. Correct in principle — so the back-solve **and** the
`/arb/thusus/fund` reconstruction now **dedup** (group by base + buy_ex→sell_ex
within ~10 min, keep the covered/hedged execution, drop the naked duplicate's
draw *and* its P&L). Implemented in lock-step so the replay can never double-draw.

The honest empirical result: **in the current data the overlap is ~nil** — 0
hedged↔livescan same-base pairs at any time, 0 hedged↔woncarry within 10 min. The
hedged engine only began 2026-07-17 and trades a disjoint token set from
livescan, so only **1** exact duplicate exists. Dedup is now the correct,
future-proof basis and will collapse overlaps automatically *if* the engines
start double-entering live gaps — but it does **not** manufacture a sub-$26k
number today. (Reported both before/after: $44k/$29k either way.) Honesty over
hitting a target — the number is $29k.

## The coherence trap (and why the R1 ledger is not phantom money)

A subtle trap: the R1-sized allocation ($3k bithumb) is only coherent if R1 ran
*throughout history*. With only the real transfers present, a chronological
replay drains bithumb unfunded and forward transfers can **never** repair a past
low-water mark — so bithumb showed **$17,156 capital_short**.

The honest fix is the **R1 conservation ledger**: `nw_qm_transfers` is populated
with the exact R1 returns the allocation is sized on, dated at their real trigger
times. These are **net-zero capital relocations** — returning USDT that *provably
accumulated* at global venues from real settled Korea-buy→global-sell trades —
not fabricated topups that conjure value (the W-FUND-1 sin). Allocation and
ledger use the identical transfer set, so the replay reproduces the back-solve:
capital_short → **$0**, bithumb reconstructed at **$3,695**, `invariant_ok=true`.
The live executor extends this ledger forward from the last batch ts.

## The class of mistake

**Sizing a fund for a policy you haven't wired.** W-FUND-1 sized capital
*assuming R1 would run* but nothing ran it; the allocation and the ledger
disagreed, surfacing as capital_short. The lesson generalizes the
[[2026-07-18-fund-capital-wiring-qm-to-engine|capital-wiring lesson]]: a capital
model is only coherent when the mechanism it assumes (here, R1 batching) actually
writes to the ledger the reconstruction replays — at the right *times*, not just
the right totals.

## QM as-built — 3 modes on the unified fund

- **R1 BATCHING** (event): accumulator = bithumb-origin USDT settled to global
  venues since the last `R1-batch` ts; ≥ `NW_QM_R1_TRIGGER_USD` → netted return to
  bithumb, floor-protected, no 50% clause. Reset via the batch ts.
- **PRE-EMPTIVE** (once per UTC day): forecast bithumb's daily draw from its recent
  Korea-leg buy volume; top up to that target from offshore *surplus-above-floor*.
- **IMMEDIATE** (safety): any venue below its `$NEXT_TRADE_FLOOR` ($40) topped up
  at once (a trade cannot fire below its floor).
- **Blind-spot fix**: `_venue_stats` now unions buy-venue consumption across
  nw_paper_trades (livescan+bigspike) + nw_woncarry_shadow (discount→korean_ex,
  premium→global_ex) + nw_hedged_shadow — so floors reflect the *real* per-venue
  draw, especially bithumb (68 hedged + woncarry-discount buys).

All moves prefer arb-as-rebalance (earn the spread), clamp to what exists above
the source floor, respect single/daily caps, and log `capital_short` only when a
deficit is genuinely uncoverable. The one-time ledger backfill is excluded from
the rolling daily-cap so it can't spuriously exhaust the live budget.

_Related: [[2026-07-18-fund-capital-wiring-qm-to-engine]] · [[2026-07-18-woncarry-korea-usdt-capital-model]] · [[quartermaster-wallet-type-pools]] · [[won-carry]] · [[THUSUS_OPS_LOOP]] · [[PARAMS]] · [[Thusus]]_
