---
token: GTC
type: token
tier: free
nw_grade: A+
nw_grade_worst: B
identity: collision
contracts:
  - { chain: ethereum, address: "0xde30da39c46104798bb5aa3fe8b9e0e1f348163f" }
exchanges: [binance, bithumb, coinbase, kucoin, mexc]
korean_exchanges: [bithumb]
transfer: partial
updated: 2026-09-04T03:56:10.992561Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# GTC · NW Grade **A+**

Ethereum-network token; NW grade A+ liquidity; transfer is partial (some venues frozen); **ticker collision** — same symbol maps to different contracts across exchanges.

## Identity
- Contract: [[ethereum]] `0xde30da…163f` (collision)
- Listed on: [[binance]], [[bithumb]], [[coinbase]], [[kucoin]], [[mexc]]

## Grade by exchange
- [[binance]]: A+
- [[bithumb]]: A
- [[coinbase]]: A+
- [[kucoin]]: B
- [[mexc]]: B+

## Deposit / Withdrawal
- [[binance]]: deposit ✅ / withdraw ✅
- [[bitget]]: deposit ❌ / withdraw ✅
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[coinbase]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ❌ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[lbank]]: deposit ❌ / withdraw ✅
- [[mexc]]: deposit ✅ / withdraw ✅
- [[upbit]]: deposit ✅ / withdraw ✅

## Related
[[collision]]

## Events
- 2026-08-26 · [[bitget]] [[ethereum]] deposit → closed · [[event/dw-freeze]]
- 2026-08-05 · [[lbank]] [[erc20]] deposit → closed · [[event/dw-freeze]]
- 2026-07-16 · [[binance]] [[ethereum]] withdraw → open · [[event/dw-resume]]
- 2026-07-16 · [[binance]] [[ethereum]] deposit → open · [[event/dw-resume]]
- 2026-07-16 · [[binance]] [[ethereum]] withdraw → closed · [[event/dw-freeze]]
- 2026-07-16 · [[binance]] [[ethereum]] deposit → closed · [[event/dw-freeze]]

## Transfer map
- [[binance]]: open:ethereum
- [[bitget]]: closed:ethereum,ethereum
- [[bithumb]]: open:ethereum
- [[coinbase]]: open:ethereum
- [[gateio]]: closed:bsc,ethereum
- [[kucoin]]: open:ethereum,ethereum
- [[lbank]]: closed:ethereum
- [[mexc]]: open:ethereum
- [[upbit]]: open:ethereum

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
2 shadow trades · realized net **+1.73 USD** · win rate 100% (2 settled)

- 2026-08-14 · woncarry · [[bithumb]]→[[binance]] · +1.15 USD · _held_
- 2026-08-13 · woncarry · [[bithumb]]→[[binance]] · +0.57 USD · _held_

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-09-04T03:56:10.992561Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/GTC.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

