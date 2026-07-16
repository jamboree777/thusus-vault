---
concept: stablecoin-basis
type: concept
aliases: [stablecoin basis, USDT basis, USDT/KRW basis]
related: [kimchi-premium, won-carry, one-price]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Stablecoin basis — the USDT/KRW distortion

The **stablecoin basis** is the gap between what USDT costs in Korean won on a Korean exchange and what the *official* USD/KRW exchange rate says a dollar should cost. USDT is supposed to be a dollar, so on a frictionless market USDT/KRW would equal USD/KRW. It does not. On Korean venues USDT has traded roughly **−1.5% off** the official rate (an observed figure — it moves with flows and is not a constant).

## Why it exists

The same border friction that creates the [[kimchi-premium]] creates the basis: getting dollars in and out of the Korean banking-and-crypto system is regulated and capacity-limited, so the *stablecoin itself* drifts from parity. The basis is the kimchi premium of the dollar, measured in the dollar's own stand-in.

## Why it matters — it contaminates the premium

This is the reason a raw kimchi number is misleading. When you compare a token's won price to its global USDT price, you are unknowingly comparing through USDT — and USDT is itself off-parity by the basis. So a chunk of what looks like a **token** premium is actually the **stablecoin** basis leaking in.

To read the true, actionable Korean edge on a token you have to subtract the basis out:

```
relative_edge = token_premium − stablecoin_basis
```

That corrected number is [[won-carry]]. A token showing "+1% in Korea" against a −1.5% USDT basis is genuinely richer than it looks in won terms; a token showing "+1%" against a +1.5% basis is not really rich at all once you net the dollar's own distortion. Never trade the raw premium — trade the basis-adjusted one.

## Practical use

The basis also defines the **baseline route** for a remitter: the plain way to move value across the border is to buy or sell USDT and pay the basis. Any token vehicle only wins if it beats that USDT baseline after both legs' slippage — which is exactly the comparison the [[won-carry]] optimizer makes.
