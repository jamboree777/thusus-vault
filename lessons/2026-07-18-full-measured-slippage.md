---
type: lesson
date: 2026-07-18
trigger: "Robin directive (paper fund honesty, 2026-07-18): apply measured slippage at 100%, not 90%, in ALL paper engines — including the hedge legs of the covered engine."
problem: "Every paper engine (livescan/big-spike, won-carry, hedged/covered-arb) discounted the raw book-walk slip it charged itself: only SLIPPAGE_APPLY (90%) of the measured slip was actually applied to each fill, on the theory that refills / hidden liquidity absorb the rest. That is an assumption, not a measurement — and it is the SAME assumption on every leg of every engine, including the hedge/margin-perp entry fill in the covered engine, which had never been separately re-examined. Charging less than the full measured slip flatters every engine's paper capture by construction."
change: "SLIPPAGE_APPLY (env NW_PAPER_SLIPPAGE_APPLY, defined once in nw_paper_arb.py) default changed 0.9 -> 1.0. All three engines share this single constant via the imported _apply_buy_slip / _apply_sell_slip helpers, so the change is uniform: livescan/big-spike buy+sell legs, won-carry buy+sell legs (incl. the v2 size-search grid, which reuses the SAME constant/functions — the '80% of the measured slip' language in its docstrings was stale prose describing the same SLIPPAGE_APPLY, not a second independent factor), and the hedged engine's buy leg AND hedge leg (margin short / perp short entry fill) via _apply_buy_slip / _apply_sell_slip on hedge_bids. Chuncheon .env now sets NW_PAPER_SLIPPAGE_APPLY=1.0 explicitly (defense-in-depth alongside the code default). Every engine's per-trade assumptions JSONB now also stamps slippage_apply (won-carry and hedged previously computed with the constant but never recorded it; livescan already did) so any row is attributable to which value was live at its entry."
expected_effect: "Fewer marginal entries clear the net gate (a wider effective slip cost eats into thin-margin trades first), and realized vs. expected capture on trades that DO enter becomes more honest — no more crediting 10% of measured slip back to the fund for free. Should show as a modest ENTRY RATE drop across all three engines with no change in win/loss classification logic, and (for engines whose fill quality was previously flattered) a downward shift in realized net% distribution toward the true economics."
review_after: 2026-07-25
status: active
supersedes: null
---

# Charge the fund the slip it actually measures — 100%, not 90%, on every leg

The paper engines never assumed we pay zero slippage — every fill walks the live order book and measures the real VWAP-vs-touch slip on both legs. But then each engine only **charged itself 90%** of that measured number (`SLIPPAGE_APPLY`), on the theory that refills and hidden liquidity absorb the rest. That is a *model*, and a generous one: it quietly gives the paper fund back a tenth of its own measured execution cost on every single fill, in every engine, forever. Robin's directive is blunt — stop doing that. Charge the full measured slip.

## The class of mistake

This is the mirror image of the [[per-chain-settle-delay]] and [[uniform-size-band-diversification]] lessons: a **flattering discount baked into the fill model itself**, applied uniformly everywhere without being re-examined per engine. It is easy to miss because it is not a bug — the 90% number was a deliberate, documented assumption — but "deliberate and documented" is not the same as "true," and every day it goes unchallenged it inflates every engine's paper capture by a small, compounding amount. The generalization: **any assumption that discounts a MEASURED cost back toward the fund's favor needs its own review date**, the same as a guard or a gate does.

## Where it lived — one constant, three engines

`SLIPPAGE_APPLY` is defined exactly once, in `svc/worker/nw_paper_arb.py` (`NW_PAPER_SLIPPAGE_APPLY` env, default was `0.9`), and consumed through two shared helpers:

- `_apply_buy_slip(touch, raw_vwap)` — effective buy price = `touch * (1 + SLIPPAGE_APPLY * raw_buy_slip)`
- `_apply_sell_slip(touch, raw_vwap)` — effective sell price = `touch * (1 - SLIPPAGE_APPLY * raw_sell_slip)`

Both **livescan/big-spike** (buy leg + sell leg, at entry AND at settlement) and **won-carry** (`nw_woncarry_shadow.py`, buy leg + sell leg, both the entry grid-search and the settle path) call these same two functions directly — there is no separate constant to find or change. The **hedged/covered-arb engine** (`nw_hedged_shadow.py`) also imports the identical helpers: `_apply_buy_slip` on the cheap-venue buy leg and `_apply_sell_slip` on the RICH-venue hedge leg (margin short or perp short entry fill, `hedge_bids` walk) — meaning the hedge leg was ALSO only 90%-applied before this change, exactly like every other leg. Settlement in all three engines re-calls the same helpers against the live book at settle time.

One investigation resolved a possible second factor: won-carry's and livescan's v2 size-search docstrings describe "80% of the measured slip" applied during the size grid search. That is stale prose from an earlier default (`SLIPPAGE_APPLY` was 0.8 before it was 0.9), not a second, independent constant — the size search calls the exact same `_apply_buy_slip` / `_apply_sell_slip` functions reading the exact same module-global. Changing the one constant to 1.0 covers it; the comments have been corrected to say `SLIPPAGE_APPLY` generically instead of hardcoding a stale percentage, so this can't drift again.

## The fix

`SLIPPAGE_APPLY` default `0.9 -> 1.0` in `nw_paper_arb.py`, plus an explicit `NW_PAPER_SLIPPAGE_APPLY=1.0` in the Chuncheon `.env` for defense-in-depth clarity. Because the helpers are shared, this one change propagates to all three engines' buy legs, sell legs, AND the hedge leg — no per-engine duplication needed. Every entry's `assumptions` JSONB now stamps `slippage_apply` with the value that was live at that row's entry (won-carry and hedged previously computed WITH the constant but never recorded which value; that gap is now closed), so the audit trail can always distinguish a 0.9-era row from a 1.0-era row by inspecting its own stamp — not by inferring it from the deploy timestamp.

## The nuance: SLIPPAGE_APPLY is a live global, not a per-row frozen value

`_apply_buy_slip` / `_apply_sell_slip` read the CURRENT module-global `SLIPPAGE_APPLY` whenever they are called — at entry **and again at settlement**. A row's `assumptions.slippage_apply` stamp records what was live **at entry**, but the SETTLE-time fill math re-reads whatever is live **at settle time**. Concretely: any row that was still `status='pending'` at deploy — entered under the 0.9 model — will be **settled under the new 1.0 model** once its settle window arrives post-deploy, because the settle path calls the same shared helper against the same now-1.0 global. This is not a bug to special-case for a handful of straddling rows; it is a known, reported behavior. It means a small number of rows will show `assumptions.slippage_apply = 0.9` (their entry stamp) while their `settle_sell_slip_applied_pct` / realized economics were actually computed with `SLIPPAGE_APPLY=1.0` — i.e. they were entered expecting the discounted (favorable) fill model and got marked-to-market under the stricter one. Their realized P&L will look slightly worse than their `expected_net_usd` implied, for a reason that has nothing to do with market drift. Anyone doing expectation-gap analysis across the 2026-07-18 deploy boundary should filter these straddlers out or read them with this caveat.

## Forward-only

Robin was explicit: this is **forward-only**. No rows in `nw_paper_trades`, `nw_woncarry_shadow`, or `nw_hedged_shadow` were recomputed, re-scored, or purged. Every already-settled trade stays exactly as booked under the 0.9 model it was measured with. Only the running engines' entry/settle computation changes going forward, with the `slippage_apply` assumptions stamp as the dividing line — plus the one class of straddling pending-row exception described above.

## Review

By 2026-07-25: does the entry rate across all three engines show a modest drop (fewer marginal spreads clearing the stricter net gate)? Do new (`slippage_apply=1.0`) rows show realized net% closer to expected net% than the historical 0.9-era baseline (less of a flattering gap)? Are there any straddling pending rows from the deploy window, and did their realized P&L undershoot expectation for the reason documented above (not drift)?

_Related: [[five-min-settlement]] · [[per-chain-settle-delay]] · [[executable-spread]] · [[expectation-gap]] · [[quiet-size]] · [[THUSUS_OPS_LOOP]] · [[won-carry]] · [[Thusus]]_
