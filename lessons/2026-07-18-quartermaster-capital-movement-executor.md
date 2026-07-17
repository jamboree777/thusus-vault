---
type: lesson
date: 2026-07-18
trigger: "Robin: without simulating capital logistics (moving USDT to replenish exchanges as trades drain them), the fund is incoherent and the site is just an arb-info provider, not a fund. Live evidence: /arb/thusus/fund showed treasury_remaining=$0, bithumb (Korea) drained to $0 (venue_net_flow −$4,757) with NO replenishment, while binance hoarded a $4,280 surplus (net_flow +$3,475). The Quartermaster was a PLANNER only (W-QM-1): it produced rebalance plans but never MOVED the paper capital."
problem: "A planner that never executes cannot make the fund coherent. Balances only ever moved via trades (buy drains a venue, sell credits another) and an automatic per-trade treasury topup; once the treasury hit $0 there was no mechanism to replenish a drained venue, so Korea's bithumb USDT allocation bled to zero and stayed there and the fund's distribution drifted into an incoherent state that no plan could fix. Net fund value did not reflect the cost of the capital logistics that a real fund must pay, so the shadow fund was indistinguishable from an arb-info feed."
change: "Quartermaster v0.3 (nw_quartermaster_v0.py) adds a capital-movement EXECUTOR (paper) + a new nw_qm_transfers table, and the /arb/thusus/fund reconstruction (stats.py) now replays those transfers. (1) nw_qm_transfers(id, ts, from_venue, to_venue, amount_usd, chain, fee_usd, method['transfer'|'arb'], reason, epoch), 30d retention — the record of ACTUAL paper capital moves. (2) run_executor: reads the current reconstructed balances, finds deficits (below working floor; SPECIAL-CASE bithumb Korea USDT below NW_WC_BITHUMB_USDT_ALLOC, replenished FIRST) and surpluses (above cap), then EXECUTES rebalances — PREFER arb-as-rebalance when a live counter-direction arb is aligned (source=cheap/buy, deficit=rich/sell; reuses the v0.1 arb index; method='arb', fee_usd NEGATIVE = net gain), ELSE a plain USDT transfer on the cheapest OPEN chain from the transfer map (method='transfer', real fee). Netting/min-size ($25) amortizes fixed fees; single-move cap $2,500, rolling-24h cap $6,000; batches at most once per NW_QM_EXEC_MIN=60m (cadence-gated on max(ts) in nw_qm_transfers so it decouples from the planner cadence). Honest: a deficit surplus (+ treasury) can't cover is logged capital_short — NO fabricated transfer. (3) Fund reconstruction interleaves nw_qm_transfers as a 3rd event kind (rank 2) in the chronological replay: a transfer at T moves amount from→to and charges fee out of the destination, clamped so no venue/treasury goes impossibly negative (short moves apply pro-rata). Invariant updated to treasury + Σbalances + in_flight == 10000 + realized − Σ(applied transfer fees). accounting gains quartermaster_logistics{} + net_fund_value_usd = gross capture − logistics; response gains recent_transfers[] (newest-first executed moves for the frontend log) + a dedicated /arb/thusus/transfers history endpoint. Timer 6h→hourly. Still SHADOW/PAPER — no keys, no execution."
expected_effect: "Drained venues actually replenish in the paper model and the fund stays coherent. First live executor pass moves capital from the binance surplus to the starved venues, Korea bithumb FIRST: binance→bithumb $1,500 (Korea USDT floor restored from $0), then the highest missed-opportunity floor deficit (bybit, 12 live opps in 24h) funded from remaining binance + bitget surplus (~$858), with bybit's remainder + gateio + mexc honestly logged capital_short (surplus exhausted — the fund is genuinely capital-constrained until Robin's ₩7.5M / more treasury lands). After replay, /arb/thusus/fund shows bithumb and bybit balances reflecting the transfers, invariant_ok=true (now netting the logistics fee), and net_fund_value_usd = capture − logistics. As the executor runs hourly, subsequent Korea trades draw from the rebalanced capital instead of the empty treasury, so required_capital (treasury topups) falls over time — logistics becomes the measurable second profit source. The caps (NW_QM_EXEC_MIN, single/daily) and MIN_TRANSFER are seed values to be tuned from the observed replenish cadence and fee drag."
review_after: 2026-07-25
status: active
supersedes: null
---

# Capital-movement executor — the plan finally moves the money

The Quartermaster's whole point is that **logistics is the fund's second profit source**. But W-QM-1 was a *planner*: every 6h it wrote a beautiful rebalance plan to `nw_qm_plans` and then did nothing. Meanwhile the live fund told the story of why that is not enough — treasury `$0`, **bithumb drained to `$0`** (Korea USDT net flow **−$4,757**), **binance hoarding `$4,280`** (net flow +$3,475). Trades move capital one way (a buy drains, a sell credits) and the only counter-force was an automatic per-trade treasury topup; once the treasury emptied, **nothing** put money back into Korea. That is the incoherence Robin flagged: a fund whose Korea leg bleeds out with no replenishment is not a fund, it is an arb-info feed with a wallet drawing.

## What the executor does

Each pass (hourly, but the executor itself batches at most once per `NW_QM_EXEC_MIN`=60m) `run_executor`:

1. Reads the **current reconstructed balances** (the same `/arb/thusus/fund` source — which now already includes prior transfers, so it never re-issues a filled deficit).
2. Builds **deficits** — Korea `bithumb` below `NW_WC_BITHUMB_USDT_ALLOC` (special-cased, **highest priority**), then stats-floor deficits ranked by **missed-opportunity value** (recent live opps × avg size) — and **surpluses** (venues above cap, largest hoarder first so fewer/larger moves amortize the fixed fee).
3. **Executes** each needed move: **prefer arb-as-rebalance** — if a live arb is aligned (source is its cheap/buy side, the deficit its rich/sell side) with real depth, it ships capital the needed way *and earns the spread* (`method='arb'`, `fee_usd` negative = the move made money); **else** a plain USDT transfer on the cheapest OPEN chain from the transfer map (`method='transfer'`, real fee). Respects single ($2,500) and rolling-24h ($6,000) caps and a $25 min.
4. Writes each executed move to **`nw_qm_transfers`**.
5. Is **honest**: a deficit that surplus (+ any real treasury) cannot cover is logged `capital_short` — never a fabricated transfer.

## The reconstruction replays the transfers — that is what makes it real

`/arb/thusus/fund` now interleaves `nw_qm_transfers` into its chronological replay as a third event kind. A transfer at time *T* moves `amount` from→to and charges its fee out of the destination, **clamped** so no venue or treasury can go impossibly negative (a short-funded move applies pro-rata). Because it is time-positioned, a transfer that replenishes bithumb at *T* means **subsequent Korea buys draw from that rebalanced capital instead of the (empty) treasury** — so `required_capital` (treasury topups) falls as the executor runs. The conservation invariant is updated to net the logistics term:

```
treasury + Σbalances + in_flight  ==  10000 + realized_net − Σ(applied transfer fees)
```

`arb`-method moves carry a *negative* fee, so they **raise** net fund value — logistics as the second profit source, in the arithmetic. The accounting block now carries `quartermaster_logistics{}` and **`net_fund_value_usd = gross capture − logistics cost`**, and the response exposes `recent_transfers[]` (newest-first, for the frontend transfer log) plus a dedicated `/arb/thusus/transfers` history read.

## First executed moves (concrete)

Against the live state (binance $4,280 surplus, bithumb $0, treasury $0), the first pass replenishes **Korea first**: `binance→bithumb $1,500`, then the highest-missed-value floor deficit `bybit` from the remaining binance + bitget surplus (~$858), with bybit's remainder, gateio and mexc logged `capital_short` because the surplus is genuinely exhausted (the fund is capital-constrained until more capital lands). That is the coherence fix made concrete: Korea no longer bleeds to zero with no replenishment.

## Still shadow

No keys, no execution — the executor writes a *paper* transfer log the reconstruction replays. The value is that the fund is now **coherent** (drained venues replenish), its net value reflects the **cost of moving capital**, and the transfer log is the honest, time-ordered record of what the Quartermaster actually did — not just its latest wish.

## Review

By 2026-07-25: is `NW_QM_EXEC_MIN`=60m the right cadence (does Korea re-drain faster than we replenish)? Are the caps ($2,500 single / $6,000 daily) and $25 min right against the observed replenish volume and fee drag? Did `net_fund_value_usd` stay coherent and did `required_capital` measurably fall as the executor kept Korea funded from surplus instead of treasury? How often did `capital_short` fire (a signal the fund needs more real capital, not a tuning knob)? Did any arb-as-rebalance actually fire (negative-fee move), proving logistics can be net-positive?

_Related: [[PARAMS]] · [[2026-07-18-quartermaster-wallet-type-pools]] · [[2026-07-18-woncarry-korea-usdt-capital-model]] · [[transfer-feasibility]] · [[won-carry]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
