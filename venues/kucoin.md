---
venue: kucoin
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.1
maker_fee: null
premium_lean: neutral
bias_pct: 0.1574
geo: authenticated reachability verified per venue; not on the confirmed geo-block list
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# KuCoin

A broad-listing global venue, frequently a leg on small- and mid-cap tokens. On multi-chain tokens like [[BTR]] it reaches other venues via the [[mexc]] hub.

## Fees

Spot **taker 0.1%** (from `/arb/fees`). Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **neutral** on frequency — it sat on the cheap side about **52.4%** of the time (appearing on the *buy-here* list), yet its average signed bias is the **most positive** of any venue (`bias_pct +0.1574`). The two are not contradictory: KuCoin is cheap slightly more *often*, but when it is rich it is rich by more, so the size-weighted bias tilts positive. It is a good illustration of why frequency and magnitude are reported as separate fields — read them together, not either alone.

## Traits we can state

- Appears on the buy-here list by frequency; treat the positive average bias as a caution that its rich excursions are large — size and probe accordingly ([[orderbook-probing]]).
- On [[BTR]] it lists the Bitlayer chain and connects through [[mexc]]; it was not a frozen venue in that incident.

_Only fields the API returns or the operating docs state are recorded here._
