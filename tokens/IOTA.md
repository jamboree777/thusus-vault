---
token: IOTA
type: token
tier: free
nw_grade: A+
nw_grade_worst: B+
identity: partial
contracts:
  - { chain: iota, address: "0x2::iota::iota" }
exchanges: [binance, bithumb, gateio, kucoin, mexc, okx, upbit]
korean_exchanges: [bithumb, upbit]
transfer: partial
updated: 2026-08-31T03:57:42.190399Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# IOTA · NW Grade **A+**

Iota-network token; NW grade A+ liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[iota]] `0x2::iot…iota` (partial)
- Listed on: [[binance]], [[bithumb]], [[gateio]], [[kucoin]], [[mexc]], [[okx]], [[upbit]]

## Grade by exchange
- [[binance]]: A+
- [[bithumb]]: A
- [[gateio]]: A
- [[kucoin]]: A
- [[mexc]]: B+
- [[okx]]: A+
- [[upbit]]: A+

## Deposit / Withdrawal
- [[binance]]: deposit ✅ / withdraw ✅
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[htx]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ❌ / withdraw ✅
- [[lbank]]: deposit ❌ / withdraw ✅
- [[mexc]]: deposit ✅ / withdraw ✅
- [[okx]]: deposit ✅ / withdraw ✅
- [[upbit]]: deposit ✅ / withdraw ✅

## Events
- 2026-08-31 · [[kucoin]] [[iota]] deposit → closed · [[event/dw-freeze]]
- 2026-08-30 · [[binance]] [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-08-30 · [[binance]] [[bsc]] withdraw → closed · [[event/dw-freeze]]
- 2026-08-29 · [[kucoin]] [[iotamainnet]] deposit → closed · [[event/dw-freeze]]
- 2026-08-27 · [[binance]] [[iota]] withdraw → open · [[event/dw-resume]]
- 2026-08-27 · [[binance]] [[iota]] deposit → open · [[event/dw-resume]]

## Transfer map
- [[binance]]: open:bsc,iota
- [[bithumb]]: open:iota
- [[gateio]]: open:bsc,bsc,iota,iota
- [[htx]]: open:iota2
- [[kucoin]]: closed:iota,iotamainnet
- [[lbank]]: closed:bep20(bsc)
- [[mexc]]: open:bsc
- [[okx]]: open:iota stardust
- [[upbit]]: open:iota
- Recently reopened (48h): [[binance]]

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
1 shadow trade · realized net **+0.87 USD** · win rate 100% (1 settled)

- 2026-08-21 · woncarry · [[bithumb]]→[[binance]] · +0.87 USD · _held_

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-08-31T03:57:42.190399Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/IOTA.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

