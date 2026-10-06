---
token: BTR
type: token
tier: free
nw_grade: A+
nw_grade_worst: B
identity: partial
contracts:
  - { chain: bitlayer, address: "0x0e4cf4affdb72b39ea91fa726d291781cbd020bf" }
  - { chain: ethereum, address: "0x6c76de483f1752ac8473e2b4983a873991e70da7" }
exchanges: [bitget, bithumb, gateio, kucoin, mexc]
transfer: partial
updated: 2026-10-06T03:53:27.288105Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# BTR · NW Grade **A+**

Bitlayer/ethereum-network token; NW grade A+ liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[bitlayer]] `0x0e4cf4…20bf` (partial)
- Contract: [[ethereum]] `0x6c76de…0da7` (partial)
- Listed on: [[bitget]], [[bithumb]], [[gateio]], [[kucoin]], [[mexc]]

## Grade by exchange
- [[bitget]]: B+
- [[bithumb]]: A+
- [[gateio]]: B
- [[kucoin]]: A+
- [[mexc]]: A

## Deposit / Withdrawal
- [[bitget]]: deposit ❌ / withdraw ✅
- [[bithumb]]: deposit ✅ / withdraw ✅
- [[gateio]]: deposit ✅ / withdraw ✅
- [[kucoin]]: deposit ✅ / withdraw ✅
- [[mexc]]: deposit ✅ / withdraw ✅
- [[toobit]]: deposit ✅ / withdraw ✅

## Events
- 2026-10-05 · [[mexc]] [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-10-05 · [[bitget]] [[erc20]] withdraw → open · [[event/dw-resume]]
- 2026-10-02 · [[bitget]] [[ethereum]] withdraw → open · [[event/dw-resume]]
- 2026-10-01 · [[mexc]] [[bsc]] deposit → open · [[event/dw-resume]]
- 2026-09-30 · [[bithumb]] [[ethereum]] withdraw → open · [[event/dw-resume]]
- 2026-09-30 · [[bithumb]] [[ethereum]] deposit → open · [[event/dw-resume]]

## Transfer map
- [[bitget]]: closed:ethereum,ethereum
- [[bithumb]]: open:ethereum
- [[gateio]]: open:bsc,bsc,btrbtc,btrbtc
- [[kucoin]]: open:bitlayer,bitlayer
- [[mexc]]: open:bsc,ethereum | closed:bitlayer,none
- [[toobit]]: open:bsc
- Recently reopened (48h): [[bitget]], [[mexc]]

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Sources
contract verification sweep · NW grade · dep/wd status · listings · dep/wd events
_Live from the NightWatch Knowledge Graph · 2026-10-06T03:53:27.288105Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/BTR.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

BTR is the flagship [[mirage-arb]] case. It is a genuine multi-chain [[identity-verification|verified]] Bitlayer token (BSC `0xfed1…`, Ethereum `0x6c76…`, Bitlayer `0x0e4c…`), not to be confused with the unrelated Bitrue Coin that shares the ticker. It trades cheaper on [[mexc]] / [[gateio]] than on [[bitget]], but the Bitget premium is uncapturable: Bitget's Ethereum deposit has been closed since March 2026 and its BTR perpetual was removed, so there is no way to deliver in and no way to short synthetically. The premium is most likely a stranded ghost quote. Verdict: don't chase it. Full dossier: [[2026-03-24-btr-crash]].
