---
token: D
type: token
tier: free
nw_grade: B+
nw_grade_worst: F
identity: verified_same
contracts:
  - { chain: ethereum, address: "0x33b481cbbf3c24f2b3184ee7cb02daad1c4f49a8" }
  - { chain: ethereum, address: "0xdac17f958d2ee523a2206206994597c13d831ec7" }
exchanges: [binance, bitget, bithumb, kucoin, mexc]
korean_exchanges: [bithumb]
transfer: partial
updated: 2026-09-04T03:54:06.391557Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# D · NW Grade **B+**

Ethereum-network token; NW grade B+ liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[ethereum]] `0x33b481…49a8` (verified_same)
- Contract: [[ethereum]] `0xdac17f…1ec7` (verified_same)
- Listed on: [[binance]], [[bitget]], [[bithumb]], [[kucoin]], [[mexc]]

## Grade by exchange
- [[binance]]: B+
- [[bitget]]: B
- [[bithumb]]: B+
- [[kucoin]]: F
- [[mexc]]: F

## Deposit / Withdrawal
- [[binance]]: deposit ❌ / withdraw ❌
- [[bitget]]: deposit ❌ / withdraw ✅
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ❌ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[mexc]]: deposit ✅ / withdraw ✅

## Events
- 2026-09-02 · [[mexc]] [[bsc]] withdraw → closed · [[event/dw-freeze]]
- 2026-08-31 · [[mexc]] [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-08-29 · [[kucoin]] [[bsc]] withdraw → closed · [[event/dw-freeze]]
- 2026-08-29 · [[mexc]] [[bsc]] withdraw → closed · [[event/dw-freeze]]
- 2026-08-26 · [[kucoin]] [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-08-26 · [[kucoin]] [[bsc]] withdraw → closed · [[event/dw-freeze]]

## Transfer map
- [[binance]]: closed:bsc,ethereum
- [[bitget]]: closed:bsc,bsc
- [[bithumb]]: open:bsc
- [[gateio]]: closed:bsc,bsc,ethereum,ethereum
- [[kucoin]]: open:ethereum,ethereum | closed:bsc,bsc
- [[mexc]]: open:ethereum | closed:bsc
- Suspended now: [[binance]]

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
4 shadow trades · realized net **-1.77 USD** · win rate 25% (4 settled)

- 2026-08-03 · livescan · [[mexc]]→[[kucoin]] · -0.01 USD · _price_drift_
- 2026-07-28 · livescan · [[kucoin]]→[[mexc]] · +0.80 USD · _in_line_
- 2026-07-23 · livescan · [[kucoin]]→[[mexc]] · -1.22 USD · _depth_shrink_

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events) · nw_paper_trades + nw_woncarry_shadow (Thusus track record)
_Live from the NightWatch Knowledge Graph · 2026-09-04T03:54:06.391557Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/D.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

