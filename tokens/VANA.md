---
token: VANA
type: token
tier: free
nw_grade: null
identity: native
contracts:
  - { chain: ethereum, address: "0x7ff7fa94b8b66ef313f7970d4eebd2cb3103a2c0" }
exchanges: [binance, bitget, bithumb, bybit, gateio, kucoin, mexc, upbit]
korean_exchanges: [bithumb, upbit]
transfer: partial
updated: 2026-07-16T01:54:03.222685Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# VANA

Ethereum-network token; transfer is partial (some venues frozen).

## Identity
- Contract: [[ethereum]] `0x7ff7fa…a2c0` (native)
- Listed on: [[binance]], [[bitget]], [[bithumb]], [[bybit]], [[gateio]], [[kucoin]], [[mexc]], [[upbit]]

## Deposit / Withdrawal
- [[binance]]: deposit ❌ / withdraw ❌
- [[bitget]]: deposit ❌ / withdraw ❌
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[bybit]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ❌ / withdraw ❌
- [[mexc]]: deposit ✅ / withdraw ❌
- [[upbit]]: deposit ✅ / withdraw ✅

## Events
- 2026-07-15 · [[mexc]] [[vana]] withdraw → closed · [[event/dw-freeze]]
- 2026-07-15 · [[mexc]] [[vana]] withdraw → open · [[event/dw-resume]]
- 2026-07-15 · [[gateio]] [[vana]] withdraw → open · [[event/dw-resume]]
- 2026-07-14 · [[bybit]] [[vana]] withdraw → open · [[event/dw-resume]]
- 2026-07-14 · [[bybit]] [[vana]] deposit → open · [[event/dw-resume]]
- 2026-07-14 · [[mexc]] [[vana]] withdraw → closed · [[event/dw-freeze]]

## Transfer map
- [[binance]]: closed:vana
- [[bitget]]: closed:vana
- [[bithumb]]: open:coin
- [[bybit]]: open:vana
- [[gateio]]: open:vana,vana
- [[kucoin]]: closed:vana
- [[mexc]]: closed:vana
- [[upbit]]: open:vana
- Suspended now: [[binance]], [[bitget]], [[kucoin]]
- Recently reopened (48h): [[bybit]], [[gateio]], [[mexc]], [[upbit]]

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
6 shadow trades · realized net **+44.43 USD** · win rate 100% (6 settled)

- 2026-07-15 · livescan · [[gateio]]→[[bybit]] · +5.35 USD
- 2026-07-15 · livescan · [[gateio]]→[[bybit]] · +3.59 USD
- 2026-07-15 · livescan · [[gateio]]→[[bybit]] · +9.44 USD

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-07-16T01:54:03.222685Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/VANA.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

