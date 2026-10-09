---
token: FOXY
type: token
tier: free
nw_grade: A-
nw_grade_worst: D+
identity: partial
contracts:
  - { chain: linea, address: "0x5fbdf89403270a1846f5ae7d113a989f850d1566" }
exchanges: [VQ, YZ]
transfer: partial
updated: 2026-10-09T03:57:32.862620Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# FOXY · NW Grade **A-**

Linea-network token; NW grade A- liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[linea]] `0x5fbdf8…1566` (partial)
- Listed on: VQ, YZ

## Grade by exchange
- VQ: A-
- YZ: D+

## Deposit / Withdrawal
- QK: deposit ❌ / withdraw ✅
- VQ: deposit ✅ / withdraw ✅
- YZ: deposit ❌ / withdraw ❌

## Events
- 2026-10-07 · QK [[linea]] withdraw → open · [[event/dw-resume]]
- 2026-10-06 · QK [[linea]] withdraw → closed · [[event/dw-freeze]]
- 2026-09-02 · YZ [[linea]] withdraw → closed · [[event/dw-freeze]]
- 2026-09-02 · YZ [[linea]] withdraw → open · [[event/dw-resume]]
- 2026-09-02 · YZ [[linea]] withdraw → closed · [[event/dw-freeze]]
- 2026-09-02 · YZ [[linea]] withdraw → open · [[event/dw-resume]]

## Transfer map
- QK: closed:linea
- VQ: open:linea,lineaeth
- YZ: closed:linea,linea
- Suspended now: YZ
- Recently reopened (48h): QK

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
3 shadow trades · realized net **+3.00 USD** · win rate 66.7% (3 settled)

- 2026-07-19 · livescan · VQ→YZ · -2.83 USD · _price_drift_
- 2026-07-15 · bigspike · VQ→YZ · +4.64 USD
- 2026-07-15 · bigspike · VQ→YZ · +1.19 USD

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
contract verification sweep · NW grade · dep/wd status · listings · dep/wd events · Thusus track record
_Live from the NightWatch Knowledge Graph · 2026-10-09T03:57:32.862620Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/FOXY.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

FOXY is the clean illustration of why [[nw-grade]] keeps `nw_grade_worst` alongside the badge: its best venue ([[gateio]]) is grade A while another market is grade F. The badge alone would flatter a token whose weakest book is barely tradeable. On the transfer side, NightWatch's wiki records a [[bybit]] Linea-network **deposit freeze on 2026-07-12** (Bybit withdrawal-only for FOXY thereafter) — a [[transfer-feasibility]] constraint. FOXY was also one of day one's [[expectation-gap|price-drift tails]], settling **−$14.93** in [[Thusus]]'s paper book ([[journal/2026-07-15]]).
