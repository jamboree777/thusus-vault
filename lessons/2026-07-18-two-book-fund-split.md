---
type: lesson
date: 2026-07-18
trigger: "Robin (W-FUND-3): split the paper fund into TWO separate books — KOREA (any trade touching a Korean venue) vs GLOBAL — keeping capital+operation separate going forward. Plus: kill Big-Spike (unneeded watchlist trigger, merge its rows into livescan at display level), fix chain canonicalization in the transfer gate, and re-verdict the flagged legacy won-carry rows."
problem: "The fund was reconstructed as ONE flat book. But the KOREA flows (won-carry + hedged korea_discount, R1 bithumb-origin conservation circulates them) and the GLOBAL flows (livescan + hedged global_global) have opposite capital dynamics: floor/refill churn HELPS Korea (R1 recycles bithumb capital) but HURTS the global book ($14k churned vs $10k static, measured). One book hid this. Separately: the transfer gate matched shared chains on RAW chain strings, so venues spelling the same chain differently (ERC20 vs ethereum, gobob vs bob, merlin network vs merlin) were falsely rejected as no_common_network — which had also let some closed-route won-carry rows book phantom P&L."
change: "1) /arb/thusus/fund reconstructs TWO books with per-(book,venue) sub-balances (binance holds korea bithumb-origin USDT AND global USDT as separate lines; R1 transfers touch only korea sub-balances), per-book invariant + capital_short, plus top-level `books`+`combined` blocks; legacy fields = combined. nw_fund_initial_alloc + nw_qm_transfers gain a `book` column. 2) QM scoped: R1+pre-emptive+immediate-korea = korea (the only circulated book); global gets ONLY the $40 immediate emergency floor; MODE 4 working-floor global circulation OFF by default (NW_QM_GLOBAL_CIRCULATION_ENABLED), legacy working-floor rows backfilled book='retired' (not replayed). 3) evaluate_transfer_gate canonicalizes chains on BOTH sides via _canon_chain + a conservative gate alias table before matching; missing aliases (gobob->bob, merlin network->merlin, nearprotocol->near) added to the shared _CHAIN_ALIASES source of truth. 4) Big-Spike worker (nw-bigarb-sniper + watchlist) stopped+disabled on Chuncheon; its 9 rows keep their DB tag but merge into livescan at the API display layer. 5) Re-ran the won-carry resolver (canon-aware) on the 8 flagged rows: 6 still hard-fail (closed route) → phantom purge (backed up first), 2 (MERL, BOB) become PASS via aliases → kept."
expected_effect: "Live /arb/thusus/fund: books.korea invariant_ok=true capital_short=$0 ($16,000), books.global invariant_ok=true capital_short=$0 ($10,000), combined invariant_ok=true ($26,000). /arb/thusus/book: no 'bigspike' strategy anywhere (by_strategy/trades/days), engines.bigspike={retired:true}. Gate: livescan+hedged pass clean in journalctl after canon deploy; won-carry MERL/BOB now route (merlin/bob), 6 phantoms (BFC×3, G, PUMPBTC×2) removed. KOREA back-solve came out $16k not the provisional $9k (won-carry premium legs need working capital at global venues + R1 ledger only timestamped from 07-17 so bithumb drains to -$6.3k first) — honest number written; Robin may re-interleave R1 from epoch to shrink it toward $9k."
review_after: 2026-07-25
status: active
supersedes: ""
---

# Two-book fund split (Korea vs Global) + Big-Spike retirement + chain canonicalization

Robin's W-FUND-3, three moves in one honesty pass on the investor-facing paper fund.

## 1. Two books, opposite dynamics

- **KOREA book** — every trade touching bithumb/upbit on its buy OR sell leg:
  all won-carry + hedged `korea_discount`. R1 (bithumb-origin USDT conservation,
  $500 batch) recycles this book's capital → circulation HELPS it.
- **GLOBAL book** — livescan + retired-bigspike + hedged `global_global`. STATIC.
  Floor/refill churn HURTS it ($14k churned vs $10k static, measured), so the QM
  does **not** circulate it; only the $40 immediate next-trade emergency floor may
  act on a global venue.

Sub-balances are tracked **per (book, venue)** — binance holds korea-book
bithumb-origin USDT and global-book USDT as two separate lines, and R1 transfers
only ever touch korea sub-balances. Each book carries its own invariant
(`initial + realized − qm_fee == treasury + Σbal + in_flight + hedge`); combined =
the sum (legacy top-level fields stay = combined for the old UI).

## 2. The honest KOREA number is $16k, not the provisional $9k

| book | required | note |
|---|---:|---|
| KOREA | **$19,000** | bithumb 10k, gateio 3k, kucoin 2k, bybit 1k, binance 1k, okx 1k, hedge 1k |
| GLOBAL | **$10,000** | gateio 4k, bybit 2k, binance 1k, kucoin 1k, mexc 1k, hedge 1k — matches provisional exactly |

GLOBAL's honest back-solve == the provisional. KOREA did not, and it **drifts up
with live trading**: (a) won-carry **premium** legs buy at global venues
(gateio/okx/kucoin) and need korea-book working capital there, separate from
bithumb-origin; (b) the R1 conservation ledger is timestamped 07-17→07-18 only,
while trades start 07-15, so bithumb drains before R1 refills it; (c) KOREA is a
**fast-draining R1 book** — bithumb's deepest deficit grew ~$2k/hour under live
trading (06→08k in one hour). Sized bithumb $10k (deficit + headroom) → both
books capital_short $0, but a STATIC back-solve re-shorts as the fund grows. The
durable fix is periodic alloc refresh (`--write-alloc`) or a forward-R1 ledger
interleaved to now (`--write-r1-ledger`, which also shrinks bithumb toward the
~$3k R1 thesis). Robin's call.

## 3. Big-Spike retired + gate canonicalization + phantom purge

- **Big-Spike**: `nw-bigarb-sniper` + `nw-bigarb-watchlist` stopped+disabled on
  Chuncheon; 9 rows keep their DB engine tag, merge into `livescan` at display.
- **Gate**: canonicalize both sides before shared-chain matching. This is the
  same class of false-reject that let closed-route won-carry rows book phantom
  P&L. Fixed once, benefits livescan + hedged + won-carry resolver + fee matcher.
- **Won-carry re-verdict**: 8 flagged → 6 hard-fail (closed route even after
  canon) → **phantom purge** (full-row backup first, per purge discipline); 2
  (MERL→merlin, BOB→bob) route via the new aliases → **kept**.

## Discipline note

`nw_fund_initial_alloc` and `nw_qm_transfers` are the source of truth (PK on
`(venue, asset, book)` since a venue lives in both books). Every destructive step
(alloc rewrite, phantom delete) backed up first. New param
`NW_QM_GLOBAL_CIRCULATION_ENABLED` registered in PARAMS.

_Related: [[FUND_SETUP_AND_QM]] · [[2026-07-18-r1-reallocation-required-capital]] · [[2026-07-18-woncarry-per-trade-chain-resolution]] · [[2026-07-18-quartermaster-capital-movement-executor]] · [[won-carry]] · [[Thusus]]_
