---
type: registry
date: 2026-07-16
author: thusus
status: active
source: nightwatch-kg
---

# PARAMS — Thusus engine tunables (single source of truth)

Every environment-tunable parameter across the three shadow engines
([[Thusus]]'s livescan, big-spike sniper, and [[won-carry]] shadow). **Current
value** is the value actually running on the Chuncheon worker; where the server
`.env` sets no override, current = code default. As of Cycle #3 (2026-07-18) the
server `.env` sets explicit overrides for the uniform size band + diversification
guards (`NW_PAPER_SIZE_MIN_USD=40`, `NW_PAPER_SIZE_MAX_USD=300`,
`NW_WONCARRY_MAX_USD=300`, `NW_WONCARRY_SIZE_GRID_MIN=40`,
`NW_DIV_MAX_PER_TOKEN_USD=300`, `NW_DIV_MAX_PER_PAIR=3`) — these match the new
code defaults, so current = default regardless. Bounds are
suggested guard-rails for the [[THUSUS_OPS_LOOP|ops loop]]'s Phase-2 auto-tuning,
not hard limits. A linked lesson means the value has an evidenced rationale on
file; `—` means it is a seed default not yet challenged by data.

> Attribution note: every engine stamps its active params into
> `nw_paper_trades.assumptions` (and the woncarry rows) per trade, so any
> historical trade is attributable to the exact param set that produced it.

## Cycle #1 changes (2026-07-16)

| Env | Before → After | Lesson |
|---|---|---|
| `NW_PAPER_MAX_SPREAD_PCT` | (new / off) → **3.0** | [[2026-07-16-spread-drift-cap]] |
| `NW_BIGSPIKE_MAX_SPREAD_PCT` | (new / off) → **10.0** | [[2026-07-16-spread-drift-cap]] (deviation) |
| `NW_BIGSPIKE_SIZE_FACTOR` | 1.0 → **0.5** | [[2026-07-16-bigspike-size-haircut]] |
| `NW_WC_CAND_LOG_SEC` | (new) → **300** | [[2026-07-16-woncarry-blind-instrumentation]] |
| narrative `capture` / `cost_drag` | (no env — logic) | [[2026-07-16-narrative-cost-drag]] |

## Cycle #2 changes (2026-07-17)

Won-carry EXIT POLICY v2 — the KRW pool must drain, not just accumulate. Out-legs
(KRW→abroad) exit through the most undervalued token on the Korean venue whenever
that is at least as cheap as repurchasing USDT; in-legs are capped; parked KRW is
force-exited past a dwell limit and marked to market so FX drift is separable.

| Env | Before → After | Lesson |
|---|---|---|
| `NW_WC_KRW_POOL_CAP_PCT` | (new) → **30** | [[2026-07-17-woncarry-exit-policy-v2]] |
| `NW_WC_EXIT_EDGE_MIN_PCT` | (new) → **0.0** | [[2026-07-17-woncarry-exit-policy-v2]] |
| `NW_WC_MAX_DWELL_H` | (new) → **72** | [[2026-07-17-woncarry-exit-policy-v2]] |
| `NW_WC_FORCED_EXIT_MAJORS` | (new) → **BTC,ETH,XRP,SOL** | [[2026-07-17-woncarry-exit-policy-v2]] |
| accounting `fx_pnl` / `carry_pnl` / `dwell_h` | (no env — logic) | [[2026-07-17-woncarry-exit-policy-v2]] |

## Cycle #3 changes (2026-07-18)

Uniform per-trade size band + diversification guards. ~$500 Korean entries were
exploding and the KRW pool overshot (30%→35.9%). Every engine now shares MIN **$40**
.. MAX **$300**, and concentration is bounded per-token and per-route so capital
spreads across many small positions (measured: big single trades erode their own
capture 8–22%). Applies to livescan, big-spike, and won-carry identically.

| Env | Before → After | Lesson |
|---|---|---|
| `NW_PAPER_SIZE_MIN_USD` | 20 → **40** | [[2026-07-18-uniform-size-band-diversification]] |
| `NW_PAPER_SIZE_MAX_USD` | 350 → **300** | [[2026-07-18-uniform-size-band-diversification]] |
| `NW_WONCARRY_MAX_USD` | 600 → **300** | [[2026-07-18-uniform-size-band-diversification]] |
| `NW_WONCARRY_SIZE_GRID_MIN` | 20 → **40** | [[2026-07-18-uniform-size-band-diversification]] |
| `NW_KIMCHI_ROUNDTURN_MAX_USD` (Render API) | 600 → **300** | [[2026-07-18-uniform-size-band-diversification]] |
| `NW_DIV_MAX_PER_TOKEN_USD` | (new) → **300** | [[2026-07-18-uniform-size-band-diversification]] |
| `NW_DIV_MAX_PER_PAIR` | (new) → **3** | [[2026-07-18-uniform-size-band-diversification]] |
| breadth reorder (round-robin by base) | (no env — logic) | [[2026-07-18-uniform-size-band-diversification]] |

## Cycle #4 changes (2026-07-18)

Per-chain settle delay. The paper engine settled EVERY chain at a flat +5min, so
slow chains (Ethereum mainnet, the #2 chain in the data) settled against a
too-early tick and booked optimistic P&L. Settle timing is now modelled per chain:
ETH mainnet **15min**, fast chains/L2s + TRON **5min** (unchanged), unknown chains
default 5min and are logged for classification. Acceptance window = delay + **3min**
buffer (fast 8min unchanged, ETH 18min). Forward-only — historical rows keep their
old +5min settlement. Shared by livescan + big-spike.

| Env | Before → After | Lesson |
|---|---|---|
| `NW_PAPER_SETTLE_DELAY_ETH_MIN` | (new) → **15** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_BUFFER_MIN` | (new) → **3** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_DELAY_MAP` | (new / off) → **JSON override** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_DELAY_MIN` | 5 (flat, all chains) → **5 (fast-chain default only)** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_MAX_MIN` | 8 (flat ceiling) → **legacy / superseded by buffer** | [[2026-07-18-per-chain-settle-delay]] |
| `chain_settle_delay()` per-chain map (logic) | (no env — logic) | [[2026-07-18-per-chain-settle-delay]] |

## Livescan + shared economics (`nw_paper_arb.py`)

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_PAPER_MIN_NET_PCT` | 0.5 | 0.5 | 0.3 – 1.5 | — | seed |
| `NW_PAPER_MAX_SPREAD_PCT` | 3.0 | 3.0 | 1.0 – 6.0 | [[2026-07-16-spread-drift-cap]] | 2026-07-16 |
| `NW_PAPER_REPEAT_HAIRCUT_PCT` | 0.15 | 0.15 | 0.05 – 0.5 | [[repeat-haircut]] | seed |
| `NW_PAPER_FOOTPRINT_MAX_PCT` | 25 | 25 | 10 – 40 | [[quiet-size]] | seed |
| `NW_PAPER_LEG_SLIP_CAP_PCT` | 0.75 | 0.75 | 0.3 – 1.5 | [[quiet-size]] | seed |
| `NW_PAPER_MAX_BUY_SLIP_PCT` | 3.0 | 3.0 | 1.5 – 5.0 | — | seed |
| `NW_PAPER_MARGIN_RETENTION` | 0.7 | 0.7 | 0.5 – 0.9 | [[quiet-size]] | seed |
| `NW_PAPER_SLIPPAGE_APPLY` | 0.9 | 0.9 | 0.7 – 1.0 | [[five-min-settlement]] | seed |
| `NW_PAPER_REBATE_SHARE` | 0.5 | 0.5 | 0.0 – 0.6 | [[executable-spread]] | seed |
| `NW_PAPER_DEFAULT_TAKER_PCT` | 0.2 | 0.2 | 0.05 – 0.3 | — | seed |
| `NW_PAPER_WD_FEE_FALLBACK_PCT` | 0.1 | 0.1 | 0.05 – 0.5 | [[transfer-feasibility]] | seed |
| `NW_PAPER_WD_FEE_FALLBACK_USD` | 0.10 | 0.10 | 0.05 – 1.0 | [[transfer-feasibility]] | seed |
| `NW_PAPER_SIZE_USD` | 200 | 200 | 50 – 350 | — | seed |
| `NW_PAPER_SIZE_MIN_USD` | 40 | 40 | 10 – 50 | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_PAPER_SIZE_MAX_USD` | 300 | 300 | 100 – 1000 | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_PAPER_SIZE_STEP_USD` | 10 | 10 | 5 – 50 | — | seed |
| `NW_DIV_MAX_PER_TOKEN_USD` (shared) | 300 | 300 | 100 – 1000 | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_DIV_MAX_PER_PAIR` (shared) | 3 | 3 | 1 – 10 | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_PAPER_COOLDOWN_MIN` | 15 | 15 | 5 – 60 | — | seed |
| `NW_PAPER_DAILY_BASE_CAP` | 6 | 6 | 2 – 20 | — | seed |
| `NW_PAPER_PREFILTER_SPREAD_PCT` | 0.0 | 0.0 | 0.0 – 1.0 | [[executable-spread]] | seed |
| `NW_PAPER_MAX_LIVE_SCANS` | 15 | 15 | 5 – 40 | — | seed |
| `NW_PAPER_SETTLE_DELAY_MIN` (fast-chain default) | 5 | 5 | 5 – 8 | [[2026-07-18-per-chain-settle-delay]] | 2026-07-18 |
| `NW_PAPER_SETTLE_DELAY_ETH_MIN` | 15 | 15 | 10 – 20 | [[2026-07-18-per-chain-settle-delay]] | 2026-07-18 |
| `NW_PAPER_SETTLE_BUFFER_MIN` | 3 | 3 | 2 – 6 | [[2026-07-18-per-chain-settle-delay]] | 2026-07-18 |
| `NW_PAPER_SETTLE_DELAY_MAP` (JSON) | — | — | full-map override | [[2026-07-18-per-chain-settle-delay]] | 2026-07-18 |
| `NW_PAPER_SETTLE_MAX_MIN` (legacy, superseded) | 8 | 8 | — | [[2026-07-18-per-chain-settle-delay]] | 2026-07-18 |
| `NW_PAPER_POLL_SEC` | 45 | 45 | 15 – 120 | — | seed |
| `NW_PAPER_BATCH_LIMIT` | 500 | 500 | 100 – 1000 | — | seed |
| `NW_PAPER_FRESH_MIN` | 10 | 10 | 5 – 30 | — | seed |
| `NW_PAPER_BOOK_DEPTH` | 50 | 50 | 20 – 100 | [[orderbook-probing]] | seed |
| `NW_PAPER_BOOK_TICKER_TOL_BPS` | 3.0 | 3.0 | 1 – 10 | [[orderbook-probing]] | seed |
| `NW_PAPER_CCXT_TIMEOUT_MS` | 9000 | 9000 | 3000 – 20000 | — | seed |
| `NW_PAPER_CURRENCIES_TTL_H` | 1 | 1 | 1 – 24 | — | seed |
| `NW_PAPER_TRANSFER_BLOCK_TTL_H` | 24 | 24 | 1 – 72 | [[transfer-feasibility]] | seed |
| `NW_PAPER_TRANSFER_UNKNOWN_TTL_H` | 1 | 1 | 1 – 24 | [[transfer-feasibility]] | seed |
| `NW_PAPER_DEBUG_REJECTS` | 1 | 1 | 0 / 1 | — | seed |
| `NW_TRANSFER_EXCLUDE_MAINNET_ONLY` | 1 | 1 | 0 / 1 | [[transfer-feasibility]] | seed |

## Big-spike sniper (`nw_bigarb_sniper.py`)

Reuses all shared economics constants above (fees, slippage, footprint, size
grid, repeat-haircut). Sniper-specific:

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_BIGSPIKE_MAX_SPREAD_PCT` | 10.0 | 10.0 | 3.0 – 15.0 | [[2026-07-16-spread-drift-cap]] | 2026-07-16 |
| `NW_BIGSPIKE_SIZE_FACTOR` | 0.5 | 0.5 | 0.3 – 1.0 | [[2026-07-16-bigspike-size-haircut]] | 2026-07-16 |
| `NW_SNIPER_POLL_SEC` | 20 | 20 | 10 – 60 | — | seed |
| `NW_SNIPER_COOLDOWN_MIN` | 10 | 10 | 5 – 30 | — | seed |
| `NW_SNIPER_MAX_LIVE_SCANS` | 24 | 24 | 8 – 48 | — | seed |
| `NW_SNIPER_TELEGRAM` | 0 | 0 | 0 / 1 | — | seed |

## Won-carry shadow (`nw_woncarry_shadow.py`)

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_WC_CAND_LOG_SEC` | 300 | 300 | 60 – 900 | [[2026-07-16-woncarry-blind-instrumentation]] | 2026-07-16 |
| `NW_WC_KRW_POOL_CAP_PCT` | 30 | 30 | 10 – 60 | [[2026-07-17-woncarry-exit-policy-v2]] | 2026-07-17 |
| `NW_WC_EXIT_EDGE_MIN_PCT` | 0.0 | 0.0 | −0.5 – 1.0 | [[2026-07-17-woncarry-exit-policy-v2]] | 2026-07-17 |
| `NW_WC_MAX_DWELL_H` | 72 | 72 | 24 – 168 | [[2026-07-17-woncarry-exit-policy-v2]] | 2026-07-17 |
| `NW_WC_FORCED_EXIT_MAJORS` | BTC,ETH,XRP,SOL | BTC,ETH,XRP,SOL | liquid majors | [[2026-07-17-woncarry-exit-policy-v2]] | 2026-07-17 |
| `NW_WONCARRY_MIN_NET_PCT` | 0.5 | 0.5 | 0.3 – 2.0 | [[executable-spread]] | seed |
| `NW_WONCARRY_MIN_NET_USD` | 6 | 6 | 2 – 20 | [[executable-spread]] | seed |
| `NW_WONCARRY_MAX_USD` | 300 | 300 | 100 – 2000 | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_WONCARRY_TRANSIT_MIN` | 5 | 5 | 5 (fixed rule) | [[five-min-settlement]] | seed |
| `NW_WONCARRY_MAX_ENTRIES_PER_PASS` | 2 | 2 | 1 – 5 | — | seed |
| `NW_WONCARRY_COOLDOWN_MIN` | 60 | 60 | 15 – 180 | — | seed |
| `NW_WONCARRY_MAX_PROBES` | 16 | 16 | 8 – 32 | [[orderbook-probing]] | seed |
| `NW_WONCARRY_REJECT_COOLDOWN_MIN` | 10 | 10 | 5 – 30 | [[orderbook-probing]] | seed |
| `NW_WONCARRY_EDGE_IMPROVE_PP` | 0.25 | 0.25 | 0.1 – 1.0 | [[executable-spread]] | seed |
| `NW_WONCARRY_SETTLE_PROBES` | 10 | 10 | 5 – 20 | — | seed |
| `NW_WONCARRY_SIZE_GRID_MIN` | 40 | 40 | 10 – 50 | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_WONCARRY_SIZE_GRID_STEP` | 50 | 50 | 20 – 100 | — | seed |
| `NW_WONCARRY_FUND_KRW_USD` | 3000 | 3000 | pool size | — | seed |
| `NW_WONCARRY_FUND_ABROAD_USD` | 7000 | 7000 | pool size | — | seed |
| `NW_WONCARRY_POLL_SEC` | 30 | 30 | 15 – 120 | — | seed |
| `NW_WONCARRY_API_TIMEOUT_SEC` | 20 | 20 | 5 – 60 | — | seed |
| `NW_PAPER_REPEAT_HAIRCUT_PCT` | 0.15 | 0.15 | 0.05 – 0.5 | [[repeat-haircut]] | seed (shared) |

_Related: [[THUSUS_OPS_LOOP]] · [[quiet-size]] · [[executable-spread]] · [[five-min-settlement]] · [[repeat-haircut]] · [[expectation-gap]] · [[2026-07-17-woncarry-exit-policy-v2]] · [[2026-07-18-uniform-size-band-diversification]] · [[2026-07-18-per-chain-settle-delay]] · [[won-carry]] · [[Thusus]]_
