---
token: HOLD
type: token
tier: free
nw_grade: A
nw_grade_worst: D
identity: verified_same
contracts:
  - { chain: zksync, address: "0xed4040fd47629e7c8fbb7da76bb50b3e7695f0f2" }
exchanges: [bitget, gateio, hyperliquid, kucoin]
transfer: partial
updated: 2026-09-02T03:56:55.503703Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# HOLD · NW Grade **A**

Zksync-network token; NW grade A liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[zksync]] `0xed4040…f0f2` (verified_same)
- Listed on: [[bitget]], [[gateio]], [[hyperliquid]], [[kucoin]]

## Grade by exchange
- [[bitget]]: A-
- [[gateio]]: D
- [[hyperliquid]]: D
- [[kucoin]]: A

## Deposit / Withdrawal
- [[bitget]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[mexc]]: deposit ❌ / withdraw ✅

## Events
- 2026-08-26 · [[kucoin]] [[zksync2]] withdraw → closed · [[event/dw-freeze]]
- 2026-08-26 · [[kucoin]] [[zksync2]] deposit → closed · [[event/dw-freeze]]
- 2026-08-26 · [[bitget]] [[zksync]] withdraw → closed · [[event/dw-freeze]]
- 2026-08-26 · [[bitget]] [[zksync]] deposit → closed · [[event/dw-freeze]]
- 2026-07-29 · [[mexc]] [[ton]] withdraw → open · [[event/dw-resume]]
- 2026-07-29 · [[mexc]] [[ton]] withdraw → closed · [[event/dw-freeze]]

## Transfer map
- [[bitget]]: open:bsc,bsc | closed:zksync,zksyncera
- [[gateio]]: open:ton,ton
- [[kucoin]]: open:bsc,bsc | closed:bera,bera,zks20,zksync2
- [[mexc]]: closed:ton

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
1 shadow trade · realized net **+0.93 USD** · win rate 100% (1 settled)

- 2026-09-01 · livescan · [[bitget]]→[[kucoin]] · +0.93 USD · _beat_

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-09-02T03:56:55.503703Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/HOLD.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

