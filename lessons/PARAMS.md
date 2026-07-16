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
`.env` sets no override, current = code default (as of 2026-07-16 the server
overrides *none* of these, so every engine runs on defaults). Bounds are
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
| `NW_PAPER_SIZE_MIN_USD` | 20 | 20 | 10 – 50 | [[quiet-size]] | seed |
| `NW_PAPER_SIZE_MAX_USD` | 350 | 350 | 100 – 1000 | [[quiet-size]] | seed |
| `NW_PAPER_SIZE_STEP_USD` | 10 | 10 | 5 – 50 | — | seed |
| `NW_PAPER_COOLDOWN_MIN` | 15 | 15 | 5 – 60 | — | seed |
| `NW_PAPER_DAILY_BASE_CAP` | 6 | 6 | 2 – 20 | — | seed |
| `NW_PAPER_PREFILTER_SPREAD_PCT` | 0.0 | 0.0 | 0.0 – 1.0 | [[executable-spread]] | seed |
| `NW_PAPER_MAX_LIVE_SCANS` | 15 | 15 | 5 – 40 | — | seed |
| `NW_PAPER_SETTLE_DELAY_MIN` | 5 | 5 | 5 (fixed rule) | [[five-min-settlement]] | seed |
| `NW_PAPER_SETTLE_MAX_MIN` | 8 | 8 | 6 – 15 | [[five-min-settlement]] | seed |
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
| `NW_WONCARRY_MIN_NET_PCT` | 0.5 | 0.5 | 0.3 – 2.0 | [[executable-spread]] | seed |
| `NW_WONCARRY_MIN_NET_USD` | 6 | 6 | 2 – 20 | [[executable-spread]] | seed |
| `NW_WONCARRY_MAX_USD` | 600 | 600 | 100 – 2000 | [[quiet-size]] | seed |
| `NW_WONCARRY_TRANSIT_MIN` | 5 | 5 | 5 (fixed rule) | [[five-min-settlement]] | seed |
| `NW_WONCARRY_MAX_ENTRIES_PER_PASS` | 2 | 2 | 1 – 5 | — | seed |
| `NW_WONCARRY_COOLDOWN_MIN` | 60 | 60 | 15 – 180 | — | seed |
| `NW_WONCARRY_MAX_PROBES` | 16 | 16 | 8 – 32 | [[orderbook-probing]] | seed |
| `NW_WONCARRY_REJECT_COOLDOWN_MIN` | 10 | 10 | 5 – 30 | [[orderbook-probing]] | seed |
| `NW_WONCARRY_EDGE_IMPROVE_PP` | 0.25 | 0.25 | 0.1 – 1.0 | [[executable-spread]] | seed |
| `NW_WONCARRY_SETTLE_PROBES` | 10 | 10 | 5 – 20 | — | seed |
| `NW_WONCARRY_SIZE_GRID_MIN` | 20 | 20 | 10 – 50 | [[quiet-size]] | seed |
| `NW_WONCARRY_SIZE_GRID_STEP` | 50 | 50 | 20 – 100 | — | seed |
| `NW_WONCARRY_FUND_KRW_USD` | 3000 | 3000 | pool size | — | seed |
| `NW_WONCARRY_FUND_ABROAD_USD` | 7000 | 7000 | pool size | — | seed |
| `NW_WONCARRY_POLL_SEC` | 30 | 30 | 15 – 120 | — | seed |
| `NW_WONCARRY_API_TIMEOUT_SEC` | 20 | 20 | 5 – 60 | — | seed |
| `NW_PAPER_REPEAT_HAIRCUT_PCT` | 0.15 | 0.15 | 0.05 – 0.5 | [[repeat-haircut]] | seed (shared) |

_Related: [[THUSUS_OPS_LOOP]] · [[quiet-size]] · [[executable-spread]] · [[five-min-settlement]] · [[repeat-haircut]] · [[expectation-gap]] · [[Thusus]]_
