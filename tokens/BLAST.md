---
token: BLAST
type: token
tier: free
nw_grade: A+
nw_grade_worst: B+
identity: verified_same
contracts:
  - { chain: blast, address: "0xb1a5700fa2358173fe465e6ea4ff52e36e88e2ad" }
exchanges: [bitget, bithumb, bybit, coinbase, gateio, kucoin, mexc, upbit]
korean_exchanges: [bithumb, upbit]
transfer: open
updated: 2026-07-22T03:52:36.793344Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# BLAST · NW Grade **A+**

Blast-network token; NW grade A+ liquidity; transfer is open on at least one venue.

## Identity
- Contract: [[blast]] `0xb1a570…e2ad` (verified_same)
- Listed on: [[bitget]], [[bithumb]], [[bybit]], [[coinbase]], [[gateio]], [[kucoin]], [[mexc]], [[upbit]]

## Grade by exchange
- [[bitget]]: B+
- [[bithumb]]: A+
- [[bybit]]: A+
- [[coinbase]]: B+
- [[gateio]]: A
- [[kucoin]]: B+
- [[mexc]]: B+
- [[upbit]]: A+

## Deposit / Withdrawal
- [[bitget]]: deposit ✅ / withdraw ✅
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[bybit]]: deposit ✅ / withdraw ✅
- [[coinbase]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[mexc]]: deposit ✅ / withdraw ✅
- [[upbit]]: deposit ✅ / withdraw ✅

## Events
- 2026-07-13 · [[upbit]] [[blastnet]] withdraw → open · [[event/dw-resume]]
- 2026-07-13 · [[upbit]] [[blastnet]] deposit → open · [[event/dw-resume]]
- 2026-07-12 · [[upbit]] [[blastnet]] withdraw → closed · [[event/dw-freeze]]
- 2026-07-12 · [[upbit]] [[blastnet]] deposit → closed · [[event/dw-freeze]]

## Transfer map
- [[bitget]]: open:blast
- [[bithumb]]: open:blast
- [[bybit]]: open:blast
- [[coinbase]]: open:blast
- [[gateio]]: open:blast,blasteth
- [[kucoin]]: open:blast
- [[mexc]]: open:blast
- [[upbit]]: open:blastnet

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Community intel
_Sourced contributions from the vault claim intake. [verified] passed review; [community-reported, unverified] are pending and NOT facts._

- [verified] **dw_change** · 2026-07-16 · [source](https://nightwatch-v1-api.onrender.com/kg/BLAST.md) · by thusus-vault-bot

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events)
_Live from the NightWatch Knowledge Graph · 2026-07-22T03:52:36.793344Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/BLAST.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

BLAST is the vault's canonical demonstration that [[nw-grade]] and [[transfer-feasibility]] are **different dimensions**. Its book is clean and deep — a straight grade A across venues — and its contract (`0xb1a5700f…88e2ad` on the Blast chain) is verified. Yet on 2026-07-13 [[upbit]] shut **both** deposits and withdrawals for the Blast network while [[bybit]] stayed fully open, turning any Korean-vs-global gap into a textbook [[mirage-arb]]. Upbit resumed a couple of days later, and `transfer` reads **open** again as of 2026-07-16. Full timeline: [[2026-07-13-blast-wallet-lockdown]].
