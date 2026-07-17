---
type: lesson
date: 2026-07-18
trigger: "flat +5min settle overstated ETH-route P&L (Robin: '이더리움은 입금에 최소 5분 걸리는데' — ETH deposit takes AT LEAST 5min, so the full withdraw->confirm->credit transfer is well over 5min, realistically 10-20min). The paper engine settled EVERY chain at a flat +5:00, so slow-chain rows were marked against a too-early tick."
problem: "The settle-timing model ignored per-chain transfer latency. Settling an Ethereum-mainnet route against the +5min book let it absorb LESS spread decay than the coins really experience in transit, so slow-chain realized P&L looked more profitable than reality. Ethereum is the #2 chain in the data (~10 trades), so the bug materially inflated ETH-route capture."
change: "Per-chain settle delay model in nw_paper_arb.py (shared by big-spike): new chain_settle_delay(route_chain) -> minutes. ETH mainnet 15min (NW_PAPER_SETTLE_DELAY_ETH_MIN=15, a defensible 10-20min midpoint, NOT instant); fast chains/L2s + TRON keep 5min (NW_PAPER_SETTLE_DELAY_MIN=5); unknown chains default 5 and are LOGGED once for classification. Acceptance window = delay + NW_PAPER_SETTLE_BUFFER_MIN (3), so fast=8min (unchanged) and ETH=18min. Whole map overridable via NW_PAPER_SETTLE_DELAY_MAP (JSON). Per-row settle timing + the pending-settle loop + the dynamic sleep all use the row's chain delay; big-spike inherits it via import. PLUS exposure-time-adjusted sizing: ETH-mainnet routes capped at $150 max (half) via NW_PAPER_SETTLE_ETH_MAX_SIZE_USD=150 — clamped in the size search keyed on the same ETH classifier (MIN stays $40; if the clamp leaves no feasible size >= $40 the trade is skipped honestly). Applies to livescan AND big-spike; woncarry untouched. FORWARD-ONLY: already-settled historical rows are untouched."
expected_effect: "ETH-route rows now settle against the +15min tick, absorbing more spread decay -> realized P&L drops to honest levels and more ETH routes fail the net gate. ETH-route position risk halved to match ~3x settle window (max $150 vs $300). Fast-chain behaviour is identical to before (5min/8min window, $300 max). Capture ratio BY CHAIN becomes comparable, which is the calibration signal for tuning these initial-estimate delays with real transfer-latency data."
review_after: 2026-07-25
status: active
supersedes: null
---

# Slow chains don't settle in five minutes — settle each chain on its own clock

The paper engine's honesty rests on the [[five-min-settlement]]: a trade is not marked at entry, it is held and settled against the *live* book some minutes later, so any adverse drift in transit is charged to it. But "some minutes" was hard-coded to **five, for every chain**. That is a lie for slow chains.

Robin flagged it plainly: **이더리움은 입금에 최소 5분 걸리는데** — the Ethereum *deposit* alone takes at least five minutes, which means the full flow (withdrawal review → broadcast → ~12-32 block confirmations → destination crediting) is realistically **10-20 minutes**. Settling an ETH route at +5:00 marks it against a book that, in reality, the coins have not yet reached. The trade skips most of its own transit window, absorbs less spread decay than it truly would, and books a P&L that is optimistic by construction. Ethereum is the **#2 chain in our data** (~10 trades), so this quietly inflated a whole segment of the book.

## The class of mistake

This is a **uniform-latency assumption over a non-uniform process**. Transfer time is a physical property of the chain — a Base or Solana credit lands in a minute or two, an Ethereum-mainnet credit takes an order of magnitude longer — and any settlement model that collapses that distribution to a single constant will systematically flatter the slow tail and (in principle) penalize the fast one. The [[five-min-settlement]] was right that settlement must be *delayed against the live book*; it was wrong to think one delay fits every route.

## The fix: a per-chain settle clock

`chain_settle_delay(route_chain)` returns the delay in minutes:

- **Ethereum mainnet: 15 min** (`NW_PAPER_SETTLE_DELAY_ETH_MIN`, default 15) — a defensible midpoint of the real 10-20 min flow. Explicitly **not instant**, and explicitly an **initial estimate** to be calibrated once we have real latency data.
- **Fast chains: 5 min** (`NW_PAPER_SETTLE_DELAY_MIN`, unchanged) — L2s (Base, Arbitrum, Optimism, opBNB), fast L1s (BSC, Polygon, Solana, Avalanche, Sui), and **TRON** (fast ~1-3 min, kept at 5).
- **Unknown chain → 5 min default, logged once** so it can be classified and folded into the map.

The acceptance window follows the delay: `SETTLE_MAX(chain) = delay + NW_PAPER_SETTLE_BUFFER_MIN` (buffer default 3). So an ETH row settles against the first live tick at/after **+15min** (up to +18); a BSC row at/after **+5min** (up to +8), exactly as before. The pending-settle loop pulls due rows at the *smallest* delay and then skips any row not yet due for *its own* chain, so slow-chain rows are never marked `no_data` before their longer window elapses. The whole map is overridable in one shot via `NW_PAPER_SETTLE_DELAY_MAP` (JSON `{chain: minutes}`), with the ETH knob as the dedicated lever. Big-spike (`nw_bigarb_sniper.py`) imports the shared timing, so its scoped settle inherits the same per-chain clock.

BTC mainnet stays *excluded* from candidacy entirely (30-60 min transit is fundamentally incompatible with a minute-scale settle model) — this change is about the chains we *do* trade whose latency we were mis-modelling.

## Longer window, smaller position — halve ETH size

Correcting the *clock* is necessary but not sufficient: a route that is open ~3x longer is also exposed to spread-decay risk ~3x longer, so leaving its size unchanged just books the honest-but-larger loss. Robin's paired directive is to **shrink the position to match the window**. For ETH-mainnet routes the per-trade **MAX size is halved to $150** (vs the standard $300); MIN stays $40 for every chain. `NW_PAPER_SETTLE_ETH_MAX_SIZE_USD` (default 150) is clamped into the size search via `chain_size_max(route_chain)`, keyed on the *same* ETH classifier that drives the delay — the exact mechanism the diversification per-token cap already uses to **shrink** the search ceiling, not to skip. If after clamping no feasible size ≥ $40 remains, the trade is skipped honestly. This applies to **livescan and big-spike** (the big-spike `SIZE_FACTOR=0.5` haircut then shrinks further on top); **won-carry is untouched**. The natural generalization is "MAX scales inversely with settle delay" — but Robin pinned ETH to exactly **$150 (half)**, so the ETH value is set explicitly rather than derived.

## Forward-only — past ETH P&L was optimistic

This is a **forward-only** correction. Already-settled historical rows are **not** re-marked; they remain in the book at their old +5min settlement. So the honest caveat stands: **historical ETH-route realized P&L was optimistic**, and pre-2026-07-18 ETH capture ratios should be read as an upper bound, not a track record.

## Review

By 2026-07-25: do ETH-route rows in `nw_paper_trades` show `assumptions.settle_delay_min = 15` and settle lags near +15min (not +5), and is their realized capture ratio now visibly *lower* than the pre-change ETH rows? Do more ETH routes fail the net gate? The real deliverable is the **follow-up**: segment capture ratio **by chain** so these initial-estimate delays (15 for ETH, 5 for fast) can be calibrated against measured transfer latency instead of a defensible guess.

_Related: [[five-min-settlement]] · [[expectation-gap]] · [[transfer-feasibility]] · [[executable-spread]] · [[quiet-size]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
