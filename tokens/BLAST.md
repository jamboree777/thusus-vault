---
token: BLAST
type: token
tier: free
nw_grade: A
nw_grade_worst: F
identity: verified_same
contracts:
  - { chain: blast, address: "0xb1a5700fa2358173fe465e6ea4ff52e36e88e2ad" }
exchanges: [WV, SU, QK, XD, VQ, YZ, VK, ZU]
transfer: partial
updated: 2026-10-09T03:53:38.406714Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# BLAST · NW Grade **A**

Blast-network token; NW grade A liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[blast]] `0xb1a570…e2ad` (verified_same)
- Listed on: WV, SU, QK, XD, VQ, YZ, VK, ZU

## Grade by exchange
- WV: C
- SU: A
- QK: C-
- XD: C-
- VQ: B+
- YZ: D-
- VK: B+
- ZU: A

## Deposit / Withdrawal
- WV: deposit ❌ / withdraw ✅
- SU: deposit ❌ / withdraw ✅
- QK: deposit ❌ / withdraw ✅
- XD: deposit ✅ / withdraw ✅
- VQ: deposit ✅ / withdraw ✅
- ST: deposit ✅ / withdraw ✅
- YZ: deposit ✅ / withdraw ✅
- VK: deposit ❌ / withdraw ✅
- ZU: deposit ❌ / withdraw ✅

## Events
- 2026-10-08 · YZ [[blast]] deposit → closed · [[event/dw-freeze]]
- 2026-10-07 · VQ [[blast]] deposit → closed · [[event/dw-freeze]]
- 2026-10-06 · QK [[blast]] deposit → closed · [[event/dw-freeze]]
- 2026-10-02 · ZU [[blastnet]] deposit → closed · [[event/dw-freeze]]
- 2026-10-02 · SU [[blast]] deposit → closed · [[event/dw-freeze]]
- 2026-10-02 · WV [[blast]] withdraw → open · [[event/dw-resume]]

## Transfer map
- WV: closed:blast,blast
- SU: closed:blast
- QK: closed:blast
- XD: open:blast
- VQ: open:blasteth | closed:blast
- ST: open:blast
- YZ: open:blast | closed:blast
- VK: closed:blast
- ZU: closed:blastnet

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Community intel
_Sourced contributions from the vault claim intake. [verified] passed review; [community-reported, unverified] are pending and NOT facts._

- [verified] **dw_change** · 2026-07-16 · [source](https://nightwatch-v1-api.onrender.com/kg/BLAST.md) · by thusus-vault-bot

## Sources
contract verification sweep · NW grade · dep/wd status · listings · dep/wd events
_Live from the NightWatch Knowledge Graph · 2026-10-09T03:53:38.406714Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/BLAST.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

BLAST is the vault's canonical demonstration that [[nw-grade]] and [[transfer-feasibility]] are **different dimensions**. Its book is clean and deep — a straight grade A across venues — and its contract (`0xb1a5700f…88e2ad` on the Blast chain) is verified. Yet on 2026-07-13 [[upbit]] shut **both** deposits and withdrawals for the Blast network while [[bybit]] stayed fully open, turning any Korean-vs-global gap into a textbook [[mirage-arb]]. Upbit resumed a couple of days later, and `transfer` reads **open** again as of 2026-07-16. Full timeline: [[2026-07-13-blast-wallet-lockdown]].
