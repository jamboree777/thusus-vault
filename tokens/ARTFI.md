---
token: ARTFI
type: token
tier: free
nw_grade: D+
nw_grade_worst: D+
identity: verified_same
contracts:
  - { chain: sui, address: "0x706fa7723231e13e8d37dad56da55c027f3163094aa31c867ca254ba0e0dc79f::artfi::artfi" }
exchanges: [gateio, kucoin]
transfer: partial
updated: 2026-07-16T04:31:45.014734Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# ARTFI · NW Grade **D+**

Sui-network token; NW grade D+ liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[sui]] `0x706fa7…rtfi` (verified_same)
- Listed on: [[gateio]], [[kucoin]]

## Grade by exchange
- [[gateio]]: D+
- [[kucoin]]: D+

## Deposit / Withdrawal
- [[bitget]]: deposit ❌ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[mexc]]: deposit ❌ / withdraw ✅

## Events
- 2026-07-12 · [[mexc]] [[sui]] deposit → closed · [[event/dw-freeze]]
- 2026-07-12 · [[bitget]] [[sui]] deposit → closed · [[event/dw-freeze]]
- 2026-07-12 · [[gateio]] [[suinew]] withdraw → closed · [[event/dw-freeze]]
- 2026-07-12 · [[gateio]] [[suinew]] deposit → closed · [[event/dw-freeze]]

## Transfer map
- [[bitget]]: closed:sui
- [[gateio]]: open:sui,sui | closed:suinew,suinew
- [[kucoin]]: open:sui
- [[mexc]]: closed:sui

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
2 shadow trades · realized net **-3.39 USD** · win rate 0% (2 settled)

- 2026-07-16 · livescan · [[kucoin]]→[[gateio]] · -0.01 USD · _cost_drag_
- 2026-07-15 · livescan · [[kucoin]]→[[gateio]] · -3.38 USD

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-07-16T04:31:45.014734Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/ARTFI.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

