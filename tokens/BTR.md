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
exchanges: [WV, SU, VQ, YZ, VK]
transfer: partial
updated: 2026-10-07T03:53:37.713378Z
source: nightwatch-kg
---

<!-- nw:auto:begin -->
# BTR · NW Grade **A+**

Bitlayer/ethereum-network token; NW grade A+ liquidity; transfer is partial (some venues frozen).

## Identity
- Contract: [[bitlayer]] `0x0e4cf4…20bf` (partial)
- Contract: [[ethereum]] `0x6c76de…0da7` (partial)
- Listed on: WV, SU, VQ, YZ, VK

## Grade by exchange
- WV: B+
- SU: A+
- VQ: B
- YZ: A+
- VK: A

## Deposit / Withdrawal
- WV: deposit ❌ / withdraw ✅
- SU: deposit ✅ / withdraw ✅
- VQ: deposit ✅ / withdraw ✅
- YZ: deposit ✅ / withdraw ✅
- VK: deposit ✅ / withdraw ✅
- CJ: deposit ✅ / withdraw ✅

## Events
- 2026-10-05 · VK [[bsc]] withdraw → open · [[event/dw-resume]]
- 2026-10-05 · WV [[erc20]] withdraw → open · [[event/dw-resume]]
- 2026-10-02 · WV [[ethereum]] withdraw → open · [[event/dw-resume]]
- 2026-10-01 · VK [[bsc]] deposit → open · [[event/dw-resume]]
- 2026-09-30 · SU [[ethereum]] withdraw → open · [[event/dw-resume]]
- 2026-09-30 · SU [[ethereum]] deposit → open · [[event/dw-resume]]

## Transfer map
- WV: closed:ethereum,ethereum
- SU: open:ethereum
- VQ: open:bsc,bsc,btrbtc,btrbtc
- YZ: open:bitlayer,bitlayer
- VK: open:bsc,ethereum | closed:bitlayer,none
- CJ: open:bsc
- Recently reopened (48h): WV, VK

## Backers & Project
_Not yet in the KG. Contribute verified backers/team/official links → see /kg (contribution). Convention: `[[backer/<name>]]`._

## Deep intelligence 🔒
Live microstructure & MM detection, on-chain flows, real-time arbitrage (One Price), grade-change alerts, and bulk access require an API key.
→ send header `X-NW-User-Key` (get one at /docs/api). Free tier is rate-limited and ~60s delayed. See /llms.txt.

## Sources
contract verification sweep · NW grade · dep/wd status · listings · dep/wd events
_Live from the NightWatch Knowledge Graph · 2026-10-07T03:53:37.713378Z_

---
_Clone the full vault: https://github.com/jamboree777/thusus-vault_

_Machine region — rewritten by the sync bot from the live wiki (`https://nightwatch-v1-api.onrender.com/kg/BTR.md`). Do not hand-edit inside these markers._
<!-- nw:auto:end -->

## Prose (durable)

BTR is the flagship [[mirage-arb]] case. It is a genuine multi-chain [[identity-verification|verified]] Bitlayer token (BSC `0xfed1…`, Ethereum `0x6c76…`, Bitlayer `0x0e4c…`), not to be confused with the unrelated Bitrue Coin that shares the ticker. It trades cheaper on [[mexc]] / [[gateio]] than on [[bitget]], but the Bitget premium is uncapturable: Bitget's Ethereum deposit has been closed since March 2026 and its BTR perpetual was removed, so there is no way to deliver in and no way to short synthetically. The premium is most likely a stranded ghost quote. Verdict: don't chase it. Full dossier: [[2026-03-24-btr-crash]].
