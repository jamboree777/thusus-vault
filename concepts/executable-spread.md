---
concept: executable-spread
type: concept
aliases: [executable spread, touch-to-touch, VWAP spread, why mid lies]
related: [one-price, quiet-size, orderbook-probing, five-min-settlement, nw-grade]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Executable spread — what you can actually capture

The **executable spread** is the gap you can really trade: the distance between the price you would truly *pay* to buy one leg and the price you would truly *receive* to sell the other, at your intended size, after fees. It is measured **touch-to-touch** — buy-side VWAP up the ask ladder versus sell-side VWAP down the bid ladder — not mid-to-mid.

## Why mid edges lie

Almost every "arb spread" you see quoted is a **mid-price** spread: the midpoint of one book against the midpoint of the other. Mid is a fiction — nobody trades at mid. To buy you cross the spread up to the ask; to sell you cross down to the bid. So a mid-to-mid gap silently double-counts *both* venues' half-spreads as if they were profit. On thin books that alone can turn a "+0.8% opportunity" into a negative number before a single coin moves.

Then subtract, in order:

1. **Both venues' touch spreads** — you pay to cross each book (already captured by using VWAP, not mid).
2. **Depth / footprint** — you don't fill the whole size at the touch; you walk the ladder, and beyond [[quiet-size]] your own flow moves the price against you.
3. **Fees** — taker fees on both legs (see the per-venue notes; [[coinbase]] alone is 0.6% a side).
4. **Transfer cost** — withdrawal fee and time, if the strategy actually ships the token (see [[transfer-feasibility]]).

What survives all four subtractions is the executable spread. It is routinely a fraction of the headline mid gap, and often negative.

## Why NightWatch measures it this way

A mid-price screen is optimistic by construction, and optimism is exactly what strands a trader. NightWatch grades a candidate on the executable spread and sizes to [[quiet-size]], because that is the only number that survives contact with the order book. The [[five-min-settlement]] paper engine goes further and settles each trade against the *live* book five minutes later, so realized results reflect real touch-to-touch fills, not mid. The recurring lesson: **the mid edge is the advertisement; the executable spread is the invoice.**
