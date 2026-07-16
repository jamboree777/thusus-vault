---
venue: coinbase
type: venue
kind: cex
fiat: [USD]
taker_fee: 0.6
maker_fee: null
premium_lean: cheap
bias_pct: -0.2295
geo: US-regulated venue
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Coinbase

The US-regulated venue, and the most *distinctive* venue in NightWatch's premium data — it is habitually and strongly on the cheap side.

## Fees

Spot **taker 0.6%** (from `/arb/fees`) — **by far the highest** of any venue NightWatch scans (six times Binance's 0.1%, twelve times Bithumb's 0.05%). This fee alone is often larger than a cross-exchange gap, so a Coinbase leg frequently fails the [[executable-spread]] test even when the mid gap looks generous. Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **cheap, and by a wide margin** — Coinbase was on the cheap side in about **88% of comparisons** (`bias_pct −0.2295`, the strongest lean of any venue). It tops the *buy-here* list. Structurally it is the archetypal **buy leg**: accumulate on Coinbase, sell into a rich venue like [[binance]] or [[okx]]. The catch is the 0.6% taker fee, which eats much of the cheapness — the habitual discount and the punishing fee partly cancel, and only pairs where the gap clears *both* are real.

## Traits we can state

- **Coinbase does not expose L1 order-book sizes** the way some venues do, so static-depth reads are limited and [[orderbook-probing]] is required before sizing a Coinbase leg.
- The 0.6% taker makes Coinbase a poor *frequent-turnover* venue; it is best used where its deep cheap-side discount is large enough to survive the fee.

_Only fields the API returns or the operating docs state are recorded here._
