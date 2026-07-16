---
venue: binance
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.1
maker_fee: null
premium_lean: rich
bias_pct: 0.0493
geo: authenticated endpoints geo-block the Korean (Chuncheon) IP (403); traded from Render Singapore
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Binance

The largest global venue by volume. In NightWatch's cross-exchange comparisons it is a reference book for [[one-price]] — deep, tight, and usually the venue others are measured against.

## Fees

Spot **taker 0.1%** (from `/arb/fees`). Maker fee is not published in that endpoint (`null` here); Binance runs the usual VIP-tier and maker-rebate schedule that lowers effective cost with volume.

## Habitual premium bias

Over the trailing 14 days Binance leans **rich**: it was on the rich side of the cross-exchange mid in about **64% of comparisons** (`bias_pct +0.0493`). It shows up on NightWatch's *sell-here* list — the venue you more often unload into than accumulate on. That makes Binance a natural **sell leg** paired against a habitually-cheap buy venue like [[coinbase]].

## Traits we can state

- Authenticated trading requires a non-Korean IP: NightWatch's Korean (Chuncheon) box is geo-blocked (403) on Binance's authenticated endpoints, so any live trading against Binance runs from Render Singapore. This is a hard operational constraint, not a preference.
- A global-to-global pair with Binance on one leg has **no Korean leg**, so it avoids travel-rule friction and can fully automate — unlike a [[kimchi-premium]] route.

_Only fields the API returns or the operating docs state are recorded here; anything else is left to the token dossiers and the live wiki._
