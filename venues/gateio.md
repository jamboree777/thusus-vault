---
venue: gateio
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.2
maker_fee: null
premium_lean: neutral
bias_pct: -0.0945
geo: authenticated reachability verified per venue; not on the confirmed geo-block list
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Gate.io

A broad-listing global venue that appears constantly in NightWatch's token graph — it lists a long tail of small tokens, so many cross-exchange gaps have a Gate leg. It connects to hub routing through [[mexc]] on multi-chain tokens like [[BTR]].

## Fees

Spot **taker 0.2%** (from `/arb/fees`) — twice Binance's rate and a meaningful drag on thin edges. Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **neutral**, very slightly cheap (about **50.8% cheap**, `bias_pct −0.0945`). No strong directional habit — Gate is roughly a coin-flip on which side of the mid it sits.

## Traits we can state

- **Withdrawal fees are gas-denominated and can be brutal for thin tokens.** Gate charges withdrawal in units of the token's own gas/chain cost, so on a low-priced, thinly-liquid token the withdrawal fee can swallow a large fraction of a small transfer — a critical input to [[transfer-feasibility]] economics and [[executable-spread]] on any send-arb through Gate.
- **Gate does not expose L1 order-book sizes** in the way some venues do, which limits static-depth reads and makes [[orderbook-probing]] more necessary, not less, before sizing.
- On [[BTR]], Gate lists BSC and the Bitlayer chain and reaches other venues via the [[mexc]] hub; it was not the venue that froze (that was [[bitget]]).

_Only fields the API returns or the operating docs state are recorded here._
