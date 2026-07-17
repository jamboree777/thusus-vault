---
type: lesson
date: 2026-07-18
trigger: "~$500 Korean entries exploding + KRW pool overshoot: the won-carry KRW pool ran to 35.9% of the fund against a 30% cap, driven partly by oversized single entries (Korea's per-entry cap was $600 vs the global $350). Big trades were measured eroding their own capture 8–22% via footprint."
problem: "Oversized single entries + single-name/route concentration erode a stable realized return. Korea sized entries almost 2x the global standard, so capital rushed into the KRW pool in big chunks and overshot its cap; and any one token or one (buy_ex,sell_ex) route could absorb an outsized share of the fund, so realized return depended on a few large, high-footprint positions instead of many small ones."
change: "Uniform per-trade band across ALL engines (livescan, big-spike, won-carry): MIN $40, MAX $300 (NW_PAPER_SIZE_MIN_USD 20→40, NW_PAPER_SIZE_MAX_USD 350→300; NW_WONCARRY_MAX_USD 600→300, NW_WONCARRY_SIZE_GRID_MIN 20→40; Render API NW_KIMCHI_ROUNDTURN_MAX_USD 600→300; big-spike inherits the band via shared import and still applies SIZE_FACTOR=0.5 on top). Plus env-tunable diversification guards: NW_DIV_MAX_PER_TOKEN_USD=300 (total open exposure on one base across venues; extra entries shrink to headroom or skip) and NW_DIV_MAX_PER_PAIR=3 (max concurrent open positions on one (buy_ex,sell_ex) route), applied to all three engines, plus a deterministic breadth reorder (round-robin by base) so a limited scan/probe budget spreads across many names instead of stacking one."
expected_effect: "KRW inflow throttled to the global standard (no more ~$500 Korean chunks), so the KRW pool stops overshooting its 30% cap from oversized entries. Realized capture stabilises via breadth — no single name holds more than $300 open and no route holds more than 3 concurrent positions, so big-footprint single trades (the 8–22% self-erosion tail) are reduced and returns rest on many small positions. The guards matter more as parallel real-time scans surface MORE opportunities."
review_after: 2026-07-24
status: active
supersedes: null
---

# One small band for everyone: uniform sizing + spread over concentration

Two failures showed up together. First, **Korea was sized bigger than everywhere else** — the won-carry per-entry cap was `$600` while the global livescan standard was `$350` — so capital walked into the KRW pool in large chunks and the pool overshot its 30% cap to **35.9%**. Second, even at the global cap, the engines had no ceiling on *how much of the fund one name or one route could hold*: a single token or a single `(buy_ex, sell_ex)` pair could accumulate an outsized share, so realized return leaned on a few large positions rather than many small ones.

Both are the same class of mistake: **concentration masquerading as opportunity**. A large trade looks efficient (fewer fills, less overhead) but its own footprint moves the book — measured here eroding capture **8–22%** — and a fund whose P&L rides on a handful of big positions has a noisier realized return than one spread across many small ones.

## The fix: one band, then bound concentration

**Uniform band — MIN `$40`, MAX `$300`, every engine identical.** No engine may push a single entry above `$300` or below `$40`. Korea is no longer special: its per-entry cap drops from `$600` to `$300` (parity with — actually tighter than — the old global `$350`, which itself drops to `$300`). Big-spike inherits the band through the shared import and still halves on top via `SIZE_FACTOR=0.5`. The `/arb/kimchi_roundturn` reference cap on the Render API is moved to `$300` by env override so the API's advertised size matches what the engine will actually take.

**Diversification guards (env-tunable), layered around entry selection — never a rewrite of the sizing search:**

- **`NW_DIV_MAX_PER_TOKEN_USD` = 300** — total *open* (pending) exposure on one base, summed across venues, may not exceed this. An already-held token's next entry is **shrunk to the remaining headroom** (folded into the size ceiling) rather than stacked at full size; if the headroom is below the `$40` floor the candidate is skipped. Default `300` = exactly one max entry, so a token at full size takes nothing more until it settles.
- **`NW_DIV_MAX_PER_PAIR` = 3** — at most three concurrent open positions on the same `(buy_ex, sell_ex)` route, so one route cannot monopolise the fund.
- **Breadth reorder** (no env — logic) — after the usual priority sort, candidates are round-robined by base so the *first* occurrence of each name is processed before any *second* occurrence. A limited live-scan / probe budget therefore spreads across many opportunities instead of stacking into the highest-spread name repeatedly.

The exposure snapshot is taken once per pass *after* settlement (so freshly-settled positions free their headroom) and incremented in-memory on each entry, so within-pass entries respect the caps too. Every skip is logged (`div_token` / `div_pair`) and surfaced in each engine's heartbeat.

## Why breadth, not size

Robin's framing: arbitrage should **spread across many small positions rather than concentrate** — more stable realized returns. The measurement backs it: a big trade's own footprint eats 8–22% of the very edge it was chasing, and that erosion is worst exactly on the thin books where a large take moves both sides. Small, many, spread beats few, large, deep. This matters *more* over time, not less: as parallel real-time scans surface a wider opportunity set, the caps are what keep the fund from dumping the new capacity into the same few names.

## Review

By 2026-07-24: does the won-carry KRW pool stop overshooting 30% from oversized entries (entries capped at ≤`$300`, no `$500`+ chunks)? Do the shadow tables show `div_token` / `div_pair` skips firing on already-held names/routes, and is open exposure per base actually bounded near `$300`? Is realized capture steadier (fewer large high-footprint tails) across livescan and won-carry? If the guards never fire despite a busy feed, the caps — or the breadth reorder — need another look; if they fire constantly and starve entries, the caps are too tight for the current opportunity set.

_Related: [[quiet-size]] · [[executable-spread]] · [[won-carry]] · [[five-min-settlement]] · [[2026-07-16-bigspike-size-haircut]] · [[2026-07-17-woncarry-exit-policy-v2]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
