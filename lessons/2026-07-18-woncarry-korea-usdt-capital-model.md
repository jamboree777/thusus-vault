---
type: lesson
date: 2026-07-18
trigger: "Code audit + Robin's definitive correction (2026-07-18): the won-carry engine ran on an env-seeded krw_pool ($3,000) that represented KRW cash the fund does NOT hold at any Korean exchange (bithumb Fund Wallet showed $0). 'discount' trades assumed that phantom KRW as their capital source, so the derived pools and reported P&L were funded by capital that did not exist. Separately, _derive_fund_state summed the ENTIRE nw_woncarry_shadow table with no time/ruleset window and the table had no retention DELETE, so stale/old-ruleset rows permanently poisoned the pools."
problem: "Phantom capital source + unbounded ledger. (a) Korea working capital was never allocated — modeling it as a phantom KRW seed made discount trades non-real. (b) The fund-state derivation had no epoch window and no retention, so pre-ruleset rows corrupted the pools every pass."
change: "Korea working capital is now a REAL USDT balance PRE-POSITIONED at bithumb (held as USDT → no FX risk, converted to KRW only at trade time): NW_WC_BITHUMB_USDT_ALLOC=1500 (drawn from the $10k fund; replaces the phantom NW_WONCARRY_FUND_KRW_USD=3000, now defaulted to the alloc; NW_WONCARRY_FUND_ABROAD_USD 7000→8500 so total stays $10k). Discount is a real, single-transfer-leg, USDT-funded round-trip capped by the bithumb-USDT balance; when exhausted the engine logs capital_short (replenishment is a Quartermaster batch USDT top-up abroad→bithumb) instead of a per-trade bridge. The bithumb-USDT balance is surfaced in /arb/thusus/fund so the Fund Wallet shows bithumb holding USDT. Ledger honesty: NW_WC_LEDGER_SINCE (default = Thusus fund epoch 2026-07-15T07:09Z; set to the 2026-07-18 cutover on Chuncheon so pre-model rows do not poison the new pools) windows _derive_fund_state; NW_WC_RETENTION_DAYS=30 adds an hourly retention DELETE mirroring the candidates table."
expected_effect: "Reported woncarry pools reflect only real, allocated capital ($1,500 bithumb USDT + $8,500 offshore = $10k). Discount trades are executable and honestly funded (no phantom KRW); when Korea USDT runs out the engine emits capital_short so QM/Robin see Korea needs a top-up rather than silently trading against capital that isn't there. Stale/pre-epoch rows can no longer corrupt the derived pools."
review_after: 2026-07-25
status: active
supersedes: "[[2026-07-16-woncarry-blind-instrumentation]]"
---

# Won-carry Korea capital is pre-positioned USDT at bithumb, not phantom KRW

[[won-carry]] had a capital-source lie at its center. The engine seeded a `krw_pool` of $3,000 from an env var and let `discount` trades (buy cheap in Korea, ship the token out, sell abroad) draw on it as if the fund were holding ₩4.5M in cash at bithumb. It was not — the Fund Wallet showed **bithumb $0**, because Korea working capital was **never allocated**. Every discount trade booked against that phantom KRW was, in capital terms, not a real trade, and its P&L flowed into the reported book.

## The class of mistake

This is **phantom-capital accounting**: an engine that prices a trade's *edge* correctly but sources its *principal* from a balance that does not exist in the fund. The edge gate was never wrong — `entry_relative_edge_pct` / `expected_net_pct` already strip the [[stablecoin-basis]], so a token discounted *deeper* than the basis is a genuine edge. The bug was purely the capital model: where do the dollars come from?

## The fix — pre-positioned USDT at bithumb

Robin's definitive model: **Korea working capital is USDT pre-positioned at the Korean exchange, held as USDT** (a dollar balance → no FX risk), and **converted to KRW only at the instant of each trade** (seconds of KRW exposure; the basis cost at that instant is already inside `relative_edge`, so it is never double-counted). A discount round-turn is therefore a **single transfer leg**:

```
USDT @ bithumb  →(sell for KRW at execution)→  buy discounted token
                →(ship token abroad: 1 transfer, fee+time)→  sell offshore for USDT
```

Concretely: FIL at −2.29% against a −0.6% basis ≈ **+1.7% net**. A uniformly-discounted market (token ≈ basis) correctly nets ~0 and is skipped. The trade is capital-capped by the real bithumb-USDT balance (`NW_WC_BITHUMB_USDT_ALLOC`, default **$1,500**, drawn from the $10k fund; offshore pool holds the remaining **$8,500**). As tokens ship out and settle offshore the bithumb balance depletes — when it falls below the minimum size the engine logs **`capital_short`** rather than bridging fresh USDT per trade. Replenishment (batch USDT top-up abroad→bithumb on a cheap chain) is a **Quartermaster** job. Premium in-legs also replenish Korea, since their proceeds land there.

The ₩7.5M Robin is adding stays **separate** — it is locked short-side lending collateral, **not** won-carry working capital.

## Ledger honesty (retention + epoch)

Two structural holes let the pools drift regardless of the capital model. `_derive_fund_state` summed the **entire** `nw_woncarry_shadow` table with no time window, and only the candidates table had a retention DELETE. So a single stale or old-ruleset row poisoned the derived pools forever. The fix windows the derivation on **`NW_WC_LEDGER_SINCE`** (default = the Thusus fund epoch `2026-07-15T07:09Z`; advanced to the `2026-07-18` cutover on the live worker so pre-model rows are excluded from the new pools while staying in the table for research) and adds an hourly retention DELETE (**`NW_WC_RETENTION_DAYS`** = 30) mirroring the candidates cleanup. On cutover the pools re-derived cleanly to **$1,500 bithumb + $8,500 offshore = $10,000**, and discount entries immediately funded from the bithumb USDT (SKR, COOKIE, NCT, VVV at 0.53–0.84% net), draining $1,500→$1,210→$920→$630→$340 as expected.

## Why this replaces the interim framings

Two earlier framings of this same fix were wrong and are superseded: (1) marking discount **shadow-only / non-executable** (it *is* executable and real), and (2) modelling it as a **two-leg** USDT-abroad→Korea + token-Korea→abroad round-trip (the USDT is *already* at bithumb, so it is a **single** token-out leg with only seconds of FX exposure). The correct model is: pre-positioned USDT, single leg, FX-minimized, capital-capped, `capital_short` when exhausted.

_Related: [[won-carry]] · [[stablecoin-basis]] · [[executable-spread]] · [[quartermaster-wallet-type-pools]] · [[2026-07-17-woncarry-exit-policy-v2]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
