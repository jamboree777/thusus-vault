---
token: BTR
type: token
tier: free
nw_grade: A+
nw_grade_worst: B
identity: verified_same
contracts:
  - { chain: ethereum, address: "0x6c76de483f1752ac8473e2b4983a873991e70da7" }
exchanges: [bitget, bithumb, gateio, kucoin, mexc]
korean_exchanges: [bithumb]
transfer: partial
updated: 2026-07-16T04:31:56.016969Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# BTR · NW Grade **A+**

Ethereum-network token; NW grade A+ liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[ethereum]] `0x6c76de…0da7` (verified_same)
- Listed on: [[bitget]], [[bithumb]], [[gateio]], [[kucoin]], [[mexc]]

## Grade by exchange
- [[bitget]]: B+
- [[bithumb]]: A+
- [[gateio]]: B
- [[kucoin]]: A
- [[mexc]]: B

## Deposit / Withdrawal
- [[bitget]]: deposit ❌ / withdraw ✅
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[mexc]]: deposit ✅ / withdraw ✅

## Events
- 2026-07-12 · [[bitget]] [[erc20]] deposit → closed · [[event/dw-freeze]]

## Transfer map
- [[bitget]]: closed:ethereum
- [[bithumb]]: open:coin
- [[gateio]]: open:bsc,bsc,btrbtc,btrbtc
- [[kucoin]]: open:bitlayer
- [[mexc]]: open:bitlayer,bsc,ethereum

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Sources
nw_contract_verify sweep · scan_aggregate (NW grade) · nw_exchange_contracts (dep/wd) · tokens (listings) · nw_dw_status_log (events)
_Live from the NightWatch Knowledge Graph · 2026-07-16T04:31:56.016969Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/BTR.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

BTR is the flagship [[mirage-arb]] case. It is a genuine multi-chain [[identity-verification|verified]] Bitlayer token (BSC `0xfed1…`, Ethereum `0x6c76…`, Bitlayer `0x0e4c…`), not to be confused with the unrelated Bitrue Coin that shares the ticker. It trades cheaper on [[mexc]] / [[gateio]] than on [[bitget]], but the Bitget premium is uncapturable: Bitget's Ethereum deposit has been closed since March 2026 and its BTR perpetual was removed, so there is no way to deliver in and no way to short synthetically. The premium is most likely a stranded ghost quote. Verdict: don't chase it. Full dossier: [[2026-03-24-btr-crash]].
