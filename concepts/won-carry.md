---
concept: won-carry
type: concept
aliases: [won carry, relative edge, basis-adjusted premium, kimchi remittance]
related: [kimchi-premium, stablecoin-basis, transfer-feasibility, executable-spread]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Won carry — the basis-adjusted Korean edge

**Won carry** is the actionable Korean edge on a token after you remove the stablecoin distortion from the raw premium:

```
relative_edge = kimchi_premium − stablecoin_basis
```

It is the number that answers "does routing value across the Korean border through *this token* beat just moving USDT?" — not the raw [[kimchi-premium]], which is contaminated by the [[stablecoin-basis]].

## The two directions

Won carry is directional, because crossing the border requires buying on one side and selling on the other, and slippage lands on whichever token you use as the vehicle:

- **Discount → KRW-round (bring value in):** when a token trades at a *discount* relative to its basis-adjusted fair value overseas, buy it overseas, deposit it to Korea, and complete a round by selling into won. You bring value in cheaply.
- **Premium → USD-round (send value out):** when a token trades at a *premium* in Korea relative to basis, buy it in Korea, withdraw it, and complete a round by selling overseas for USDT. You send value out at the rich Korean price.

Put simply: **send out via the max-discount / min-premium token; bring in via the max-premium token.** Because the premium oscillates, there is almost always a favorable direction, so a trader with capital on both sides *rotates* — in via a premium token, out via a discount token, repeat — and the rotation self-balances their cross-border position.

## Why it is size-dependent

The vehicle route pays buy-side and sell-side slippage on the token, so the edge decays with size. A realistic edge-vs-size curve looks like `$2k: +1.5% · $10k: +0.6% · $30k: −0.2%`. The USDT baseline has its own (smaller) slippage. So won carry is only meaningful as an **executable, size-aware** figure — the mid-price premium overstates it (see [[executable-spread]]).

## The gates never come off

Every won-carry vehicle still has to clear [[transfer-feasibility]]: same-token identity, chain open, **buy-side withdrawal open, sell-side deposit open**, and confirmed executable depth on both legs. A premium with a closed transfer path is a [[mirage-arb]], not carry. In NightWatch's day-one paper book, the won-carry strategy took **zero entries** — every candidate inside ±1.8% was filtered out by exactly these executable-pricing gates ([[journal/2026-07-15]]).
