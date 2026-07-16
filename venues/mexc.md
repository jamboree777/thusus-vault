---
venue: mexc
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.05
maker_fee: null
premium_lean: neutral
bias_pct: -0.0938
geo: authenticated endpoints geo-block the Korean (Chuncheon) IP (403); traded from Render Singapore
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# MEXC

The **hub venue** of NightWatch's transfer graph. MEXC lists an unusually broad set of tokens across an unusually broad set of chains, which makes it the bridge that connects otherwise-disconnected venues.

## Fees

Spot **taker 0.05%** (from `/arb/fees`) — among the lowest of any venue NightWatch scans, second only to the Korean venues. That low fee is part of why MEXC is attractive as an intermediate leg. Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **neutral**, slightly cheap (about **52.4% cheap**, `bias_pct −0.0938`). It appears on the *buy-here* list — marginally more often the cheap side than the rich side.

## Traits we can state

- **Broad multi-chain currency API.** MEXC exposes many chains per token, which is exactly what lets it act as a **2-hop hub** for [[transfer-feasibility]]: a pair that is blocked directly can often move A → MEXC on one chain, MEXC → B on another. On [[BTR]] it lists all three official chains (BSC, Ethereum, Bitlayer) and is *the* reason gateio/kucoin BTR remains movable among themselves ([[2026-03-24-btr-crash]]).
- Authenticated trading requires a non-Korean IP: the Korean (Chuncheon) box is geo-blocked (403), so live MEXC trading runs from Render Singapore.

_Only fields the API returns or the operating docs state are recorded here._
