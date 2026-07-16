---
token: FOXY
type: token
tier: free
nw_grade: A
nw_grade_worst: F
identity: verified_same
contracts:
  - { chain: linea, address: "0x5fbdf89403270a1846f5ae7d113a989f850d1566" }
exchanges: [gateio, kucoin]
transfer: partial
updated: 2026-07-16T01:19:25.089063Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# FOXY · NW Grade **A**

Linea-network token; NW grade A liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[linea]] `0x5fbdf8…1566` (verified_same)
- Listed on: [[gateio]], [[kucoin]]

## Grade by exchange
- [[gateio]]: A
- [[kucoin]]: F

## Deposit / Withdrawal
- [[bybit]]: deposit ❌ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅

## Events
- 2026-07-12 · [[bybit]] [[linea]] deposit → closed · [[event/dw-freeze]]

## Transfer map
- [[bybit]]: closed:linea
- [[gateio]]: open:linea,lineaeth
- [[kucoin]]: open:linea

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
4 shadow trades · realized net **-8.00 USD** · win rate 75% (4 settled)

- 2026-07-15 · bigspike · [[gateio]]→[[kucoin]] · -14.93 USD
- 2026-07-15 · livescan · [[gateio]]→[[kucoin]] · +1.10 USD
- 2026-07-15 · bigspike · [[gateio]]→[[kucoin]] · +4.64 USD

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-07-16T01:19:25.089063Z_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/FOXY.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

FOXY is the clean illustration of why [[nw-grade]] keeps `nw_grade_worst` alongside the badge: its best venue ([[gateio]]) is grade A while another market is grade F. The badge alone would flatter a token whose weakest book is barely tradeable. On the transfer side, NightWatch's wiki records a [[bybit]] Linea-network **deposit freeze on 2026-07-12** (Bybit withdrawal-only for FOXY thereafter) — a [[transfer-feasibility]] constraint. FOXY was also one of day one's [[expectation-gap|price-drift tails]], settling **−$14.93** in [[Thusus]]'s paper book ([[journal/2026-07-15]]).
