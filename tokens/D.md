---
token: D
type: token
tier: free
nw_grade: A
nw_grade_worst: F
identity: verified_same
contracts:
  - { chain: ethereum, address: "0x33b481cbbf3c24f2b3184ee7cb02daad1c4f49a8" }
  - { chain: ethereum, address: "0xdac17f958d2ee523a2206206994597c13d831ec7" }
exchanges: [GN, WV, SU, YZ]
transfer: blocked
updated: 2026-10-07T03:55:02.925017Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# D · NW Grade **A**

Ethereum-network token; NW grade A liquidity; transfer is currently blocked (deposit/withdrawal frozen on at least one venue).

## Identity
- Contract: [[ethereum]] `0x33b481…49a8` (verified_same)
- Contract: [[ethereum]] `0xdac17f…1ec7` (verified_same)
- Listed on: GN, WV, SU, YZ

## Grade by exchange
- GN: B+
- WV: B
- SU: A
- YZ: F

## Deposit / Withdrawal
- GN: deposit ❌ / withdraw ❌
- WV: deposit ❌ / withdraw ✅
- SU: deposit ❌ / withdraw ✅
- VQ: deposit ❌ / withdraw ✅
- YZ: deposit ❌ / withdraw ✅
- VK: deposit ❌ / withdraw ✅

## Events
- 2026-10-05 · WV [[bep20]] withdraw → open · [[event/dw-resume]]
- 2026-10-02 · WV [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-09-30 · SU [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-09-30 · SU [[bsc]] withdraw → closed · [[event/dw-freeze]]
- 2026-09-28 · VK [[ethereum]] withdraw → open · [[event/dw-resume]]
- 2026-09-28 · WV [[bep20]] withdraw → closed · [[event/dw-freeze]]

## Transfer map
- GN: closed:bsc,ethereum
- WV: closed:bsc,bsc
- SU: closed:bsc
- VQ: closed:bsc,bsc,ethereum,ethereum
- YZ: closed:bsc,bsc,ethereum,ethereum
- VK: closed:bsc,ethereum
- Suspended now: GN
- Recently reopened (48h): WV

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Thusus shadow-fund track record
4 shadow trades · realized net **-1.77 USD** · win rate 25% (4 settled)

- 2026-08-03 · livescan · VK→YZ · -0.01 USD · _price_drift_
- 2026-07-28 · livescan · YZ→VK · +0.80 USD · _in_line_
- 2026-07-23 · livescan · YZ→VK · -1.22 USD · _depth_shrink_

_Paper / dry-run track record — trades are simulated with a 5-min simulated transfer window; no capital is deployed. See [[Thusus]]._

## Sources
contract verification sweep · NW grade · dep/wd status · listings · dep/wd events · Thusus track record
_Live from the NightWatch Knowledge Graph · 2026-10-07T03:55:02.925017Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/D.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Notes

