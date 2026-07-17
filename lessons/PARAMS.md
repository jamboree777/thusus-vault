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
buffer (fast 8min unchanged, ETH 18min). Plus **exposure-time-adjusted sizing**:
ETH-mainnet routes are capped at **$150 max (half** of the $300 standard) because
they stay open ~3x longer — MIN stays $40, others keep $300. Forward-only —
historical rows keep their old +5min settlement. Shared by livescan + big-spike;
woncarry untouched.

| Env | Before → After | Lesson |
|---|---|---|
| `NW_PAPER_SETTLE_DELAY_ETH_MIN` | (new) → **15** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_BUFFER_MIN` | (new) → **3** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_ETH_MAX_SIZE_USD` | (new) → **150** (ETH-route MAX, half of $300) | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_DELAY_MAP` | (new / off) → **JSON override** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_DELAY_MIN` | 5 (flat, all chains) → **5 (fast-chain default only)** | [[2026-07-18-per-chain-settle-delay]] |
| `NW_PAPER_SETTLE_MAX_MIN` | 8 (flat ceiling) → **legacy / superseded by buffer** | [[2026-07-18-per-chain-settle-delay]] |
| `chain_settle_delay()` per-chain map (logic) | (no env — logic) | [[2026-07-18-per-chain-settle-delay]] |

## Cycle #5 changes (2026-07-18)

Hedged-Arb ("Covered Arb", strategy #4) shadow engine — `nw_hedged_shadow.py`.
Hedges the transit window at the RICH venue (margin short / perp short, chosen per
trade by min incremental cost) so the ~61% edge decay livescan suffers is locked
out at t=0. Records the A/B (hedged vs unhedged capture). Margin incremental cost =
borrow interest ONLY (the spot sell fee is not incremental); gate borrow APR is
LIVE, other venues assumed. Perp cost = 2× taker + funding (sign-aware, per-contract
interval); perp contracts are quantized → coverage can be <100% and a perp under 70%
coverage loses to margin. Capital model shadow-only (does not move the $10k pools).

**Net-gate fix (2026-07-18, same cycle):** the entry gate admitted trivial-NET
trades. `NW_HEDGE_MIN_EDGE_PCT` is the GROSS edge — after cover cost (~0.1%) +
taker fees on all legs (~0.2%) + basis, a 0.5% gross trade nets only ~0.1–0.2%
(XCN net 0.09%, ARX 0.22%), not worth the 4-leg + margin-call-tail + exit risk.
Gross `MIN_EDGE_PCT` is now a cheap PREFILTER only; the SOLE BINDING gate is
expected NET% `NW_HEDGE_MIN_NET_PCT` (gross − cover cost − all taker fees −
wd/basis, the SAME net `_entry_economics_for_size` computes and the settle
realizes). **No absolute-$ floor** (Robin: "the $1 minimum is not important") —
a small-size trade clearing 0.5% net still qualifies (diversification intent).
The pre-fix sub-0.5%-net rows were **retroactively purged** from `nw_hedged_shadow`
(shadow table only). Per-pass log reports `net_gate: pass/drop`.

| Env | Before → After | Lesson |
|---|---|---|
| `NW_HEDGE_MIN_EDGE_PCT` | (new) → **0.5** (now GROSS PREFILTER only, not binding) | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_HEDGE_MIN_NET_PCT` | (new) → **0.5** (SOLE binding gate; net% only, no $ floor) | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_HEDGE_MIN_COVER_PCT` | (new) → **70** | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_HEDGE_MARGIN_PREF_PCT` | (new) → **0.10** | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_HEDGE_BORROW_APR_MAJOR` / `_ALT` | (new) → **5.0 / 20.0** | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_HEDGE_ETH_MAX_USD` | (new) → **300** (full band; hedge neutralises exposure-time) | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_HEDGE_PERP_VENUES` | (new) → **gate,bybit,binance** (never mexc/bitget) | [[2026-07-18-hedged-arb-instrument-selection]] |
| `NW_CA_MAX_HOLD_H` (E5 timestop) | (new) → **24** | [[2026-07-18-hedged-arb-instrument-selection]] |
| live gate borrow rate + perp quantization (logic) | (no env — logic) | [[2026-07-18-hedged-arb-instrument-selection]] |

## Cycle #6 changes (2026-07-18)

Quartermaster v0.2 — wallet-type capital pools for strategy #4 (Covered Arb). The
paper-fund Planner shadow (`nw_quartermaster_v0.py`) now separates transferable
working capital from **locked** hedge capital and plans how each hedge pool is
seated. Hedge reservations are subtracted from a venue's available working capital
at the venue where the money is actually drawn (no double counting); the Korean
lending collateral is EXTERNAL money, tracked separately and never carved from the
$10k fund. All new envs' defaults equal the front-plan targets, so current =
default (server `.env` sets no override).

| Env | Before → After | Lesson |
|---|---|---|
| `NW_QM_HEDGE_HUB_VENUE` | (new) → **bybit** | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_HEDGE_HUB_USD` | (new) → **300** (UTA unified: margin-short collateral + perp margin) | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_HEDGE_AUX_VENUE` | (new) → **gateio** | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_HEDGE_AUX_USD` | (new) → **75** (futures float; internal spot→futures wallet_move) | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_HEDGE_AUX_FALLBACK_VENUE` | (new) → **binance** (aux perp fallback if gate unverified) | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_LENDING_COLLATERAL_KRW` | (new) → **7500000** (bithumb, EXTERNAL, funded=false) | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_LENDING_COLLATERAL_VENUE` | (new) → **bithumb** | [[2026-07-18-quartermaster-wallet-type-pools]] |
| `NW_QM_UTA_VENUES` | (new) → **bybit,okx** (unified acct → no wallet move) | [[2026-07-18-quartermaster-wallet-type-pools]] |
| reservations[]/wallet_moves[]/verification{} + route_verified per move (logic) | (no env) | [[2026-07-18-quartermaster-wallet-type-pools]] |


## Cycle #7 changes (2026-07-18)

| Env | Before → After | Lesson |
|---|---|---|
| `NW_DYN_*` (16 params) | (new / off) → **on, defaults** | [[2026-07-18-dynamic-sizing]] |

## Quartermaster (`nw_quartermaster_v0.py`)

Paper-fund rebalance Planner shadow (W-QM-1/v0.2). No real money, no keys — produces
a plan persisted to `nw_qm_plans`, surfaced via the `/arb/thusus/fund` quartermaster
block. New envs' current values equal code defaults (server `.env` sets no override).

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_QM_HEDGE_HUB_VENUE` | bybit | bybit | UTA venue | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_HEDGE_HUB_USD` | 300 | 300 | 100 – 800 | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_HEDGE_AUX_VENUE` | gateio | gateio | classic-acct futures venue | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_HEDGE_AUX_USD` | 75 | 75 | 50 – 200 | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_HEDGE_AUX_FALLBACK_VENUE` | binance | binance | verified futures venue | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_LENDING_COLLATERAL_KRW` | 7500000 | 7500000 | external deposit | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_LENDING_COLLATERAL_VENUE` | bithumb | bithumb | KR lending venue | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_FUNDING_SOURCE_VENUE` | — | — (auto: largest WC venue) | pin or auto | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_UTA_VENUES` | bybit,okx | bybit,okx | unified-acct venues | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_FX_USDKRW_FALLBACK` | 1380 | 1380 | fx fallback | [[2026-07-18-quartermaster-wallet-type-pools]] | 2026-07-18 |
| `NW_QM_FLOOR_MULT` | 2.0 | 2.0 | 1.0 – 4.0 | — | seed |
| `NW_QM_CAP_MULT` | 3.0 | 3.0 | 2.0 – 5.0 | — | seed |
| `NW_QM_LOOKBACK_DAYS` | 7 | 7 | 3 – 30 | — | seed |
| `NW_QM_MIN_FLOOR_USD` | 50 | 50 | 20 – 200 | — | seed |
| `NW_QM_MIN_ARB_EXEC_USDT` | 10 | 10 | 5 – 50 | — | seed |
| `NW_QM_TREASURY_MIN_USD` | 1.0 | 1.0 | 1 – 100 | — | seed |
| `NW_QM_RETENTION_DAYS` | 30 | 30 | 7 – 90 | — | seed |

## Hedged-Arb / Covered Arb (`nw_hedged_shadow.py`)

Shadow-only (does not move the $10k fund). Reuses the shared VWAP/slippage/rebate
economics + the per-chain settle clock (`chain_settle_delay`) from `nw_paper_arb.py`.

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_HEDGE_MIN_EDGE_PCT` (gross PREFILTER only) | 0.5 | 0.5 | 0.2 – 1.0 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_MIN_NET_PCT` (SOLE binding gate) | 0.5 | 0.5 | 0.3 – 1.5 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_MIN_COVER_PCT` | 70 | 70 | 50 – 95 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_MARGIN_PREF_PCT` | 0.10 | 0.10 | 0.0 – 0.3 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_BORROW_APR_MAJOR` | 5.0 | 5.0 | 1 – 10 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_BORROW_APR_ALT` | 20.0 | 20.0 | 10 – 200 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_BORROW_FEE_PCT` | 0.0 | 0.0 | 0 – 0.2 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_PERP_TAKER_PCT` | 0.05 | 0.05 | 0.02 – 0.1 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_FUNDING_INTERVAL_H` (fallback) | 8 | 8 | 1 – 8 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_SIZE_MIN` / `_MAX` / `_STEP` | 40 / 300 / 50 | same | band | [[2026-07-18-uniform-size-band-diversification]] | 2026-07-18 |
| `NW_HEDGE_ETH_MAX_USD` | 300 | 300 | 150 – 300 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_MAX_ENTRIES_PER_PASS` | 4 | 4 | 1 – 10 | — | seed |
| `NW_HEDGE_COOLDOWN_MIN` | 30 | 30 | 10 – 120 | — | seed |
| `NW_HEDGE_MAX_PROBES` | 24 | 24 | 8 – 48 | [[orderbook-probing]] | seed |
| `NW_HEDGE_INSTRUMENT_CACHE_H` | 1 | 1 | 1 – 24 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_PERP_VENUES` | gate,bybit,binance | same | never mexc/bitget | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_MARGIN_VENUES` | binance,gate,kucoin,okx,bybit,htx | same | ex-bitget/mexc | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_CA_MARGIN_HEADROOM_PCT` | 30 | 30 | 10 – 50 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_CA_MAX_HOLD_H` (E5) | 24 | 24 | 12 – 72 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_CA_COST_ABORT_PCT` (E2) | 50 | 50 | 20 – 80 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |
| `NW_HEDGE_MONITOR_PROBES` | 6 | 6 | 2 – 16 | [[2026-07-18-hedged-arb-instrument-selection]] | 2026-07-18 |

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
| `NW_PAPER_WD_FEE_FALLBACK_PCT` | REMOVED | — | — | [[transfer-feasibility]] | 2026-07-18 (audit #3: %-of-size understated fee → removed) |
| `NW_PAPER_WD_FEE_FALLBACK_USD` | 1.0 | 1.0 | 0.5 – 30 | [[transfer-feasibility]] | 2026-07-18 (audit #3: unknown wd-fee = conservative FLAT USD, not %-of-size) |
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
| `NW_PAPER_SETTLE_ETH_MAX_SIZE_USD` (ETH-route MAX) | 150 | 150 | 100 – 300 | [[2026-07-18-per-chain-settle-delay]] | 2026-07-18 |
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

## Dynamic sizing (`nw_dynamic_sizing.py`) — new guards (audit #9)

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_DYN_FUND_FAIL_TTL_SEC` | 10 | 10 | 5 – 30 | audit #9 (fund-blip: cache failures briefly, not 60s) | 2026-07-18 |
| `NW_DYN_NOFUND_CAP_USD` | 40 (=MIN_SIZE) | MIN_SIZE_USD | 40 – 300 | audit #9 (no-fund: conservative TIGHTENED floor, not $300 headroom) | 2026-07-18 |

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
| `NW_WC_BITHUMB_USDT_ALLOC` | 1500 | 1500 | 1000 – 2000 | [[2026-07-18-woncarry-korea-usdt-capital-model]] | 2026-07-18 |
| `NW_WONCARRY_FUND_KRW_USD` | 1500 | =BITHUMB_ALLOC | pool size | [[2026-07-18-woncarry-korea-usdt-capital-model]] | 2026-07-18 |
| `NW_WONCARRY_FUND_ABROAD_USD` | 8500 | 8500 | pool size | [[2026-07-18-woncarry-korea-usdt-capital-model]] | 2026-07-18 |
| `NW_WC_LEDGER_SINCE` | 2026-07-17T20:29:00Z | 2026-07-15T07:09:00Z | fund epoch / cutover | [[2026-07-18-woncarry-korea-usdt-capital-model]] | 2026-07-18 |
| `NW_WC_RETENTION_DAYS` | 30 | 30 | 14 – 90 | [[2026-07-18-woncarry-korea-usdt-capital-model]] | 2026-07-18 |
| `NW_WONCARRY_POLL_SEC` | 30 | 30 | 15 – 120 | — | seed |
| `NW_WONCARRY_API_TIMEOUT_SEC` | 20 | 20 | 5 – 60 | — | seed |
| `NW_PAPER_REPEAT_HAIRCUT_PCT` | 0.15 | 0.15 | 0.05 – 0.5 | [[repeat-haircut]] | seed (shared) |

## Dynamic sizing — density-adaptive layer (`nw_dynamic_sizing.py`, shared)

Opportunity-density-adaptive threshold/size, computed per capital-consumption
POINT (buy exchange, or KRW/abroad/hedge pool) every pass — see
[[2026-07-18-dynamic-sizing]] and docs/pm/DYNAMIC_SIZING.md. `pressure(point) =
Σ(candidate target size at the point) ÷ available capital`; a 2-stage staircase
raises the net threshold first (0.5→0.8%), then lowers max size ($300→$210). Only
bottlenecked points tighten; slack points stay on base. Every trade stamps
`assumptions.dyn` (threshold, max, pressure, stage, point, cap_source).

| Env | Current | Default | Bounds (suggested) | Lesson | Last changed |
|---|---|---|---|---|---|
| `NW_DYN_ENABLED` | 1 | 1 | 0 / 1 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_T1` | 1.0 | 1.0 | 1.0 – 2.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_T2` | 2.0 | 2.0 | 1.5 – 4.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_T3` | 3.0 | 3.0 | 2.0 – 6.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_S1` | 4.0 | 4.0 | 3.0 – 8.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_S2` | 6.0 | 6.0 | 4.0 – 12.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_S3` | 8.0 | 8.0 | 5.0 – 16.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_UP` | 1.1 | 1.1 | 1.0 – 1.5 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_DOWN` | 0.9 | 0.9 | 0.5 – 1.0 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_THRESH_STEP_PCT` | 0.1 | 0.1 | 0.05 – 0.2 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_THRESH_CAP_PCT` | 0.8 | 0.8 | 0.6 – 1.5 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_SIZE_STEP_FRAC` | 0.10 | 0.10 | 0.05 – 0.25 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_SIZE_FLOOR_FRAC` | 0.70 | 0.70 | 0.5 – 0.9 | [[2026-07-18-dynamic-sizing]] | 2026-07-18 |
| `NW_DYN_MAX_SIZE_USD` | 300 | 300 | module base (engines pass own) | [[quiet-size]] | 2026-07-18 |
| `NW_DYN_MIN_SIZE_USD` | 40 | 40 | 10 – 50 | [[quiet-size]] | 2026-07-18 |
| `NW_DYN_FUND_TTL_SEC` | 60 | 60 | 30 – 300 | — | 2026-07-18 |

Hedge-pool capital reuses the Quartermaster reservations (`NW_QM_HEDGE_HUB_USD`
= $300 bybit UTA, `NW_QM_HEDGE_AUX_USD` = $75 gate futures) as each pool's
denominator, so the engine (spend-thrift now) and the Quartermaster (refill over
6h) cooperate on the SAME per-point pressure signal.

_Related: [[THUSUS_OPS_LOOP]] · [[quiet-size]] · [[executable-spread]] · [[five-min-settlement]] · [[repeat-haircut]] · [[expectation-gap]] · [[2026-07-17-woncarry-exit-policy-v2]] · [[2026-07-18-uniform-size-band-diversification]] · [[2026-07-18-per-chain-settle-delay]] · [[won-carry]] · [[Thusus]]_
