---
venue: okx
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.1
maker_fee: null
premium_lean: rich
bias_pct: 0.1125
geo: authenticated endpoints geo-block the Korean (Chuncheon) IP (403); traded from Render Singapore
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# OKX

A major global venue. In NightWatch's premium data it is one of the two clearest *rich-side* venues, alongside [[binance]].

## Fees

Spot **taker 0.1%** (from `/arb/fees`). Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **rich**. OKX sat on the rich side in about **61% of comparisons** (`bias_pct +0.1125`) and appears on NightWatch's *sell-here* list. Like Binance, it is a natural **sell leg** — the venue you more often offload into than accumulate on — pairing well against a habitually-cheap buy venue such as [[coinbase]] or [[mexc]].

## Traits we can state

- Rich-side habit by frequency; useful as the offload leg in a [[one-price]] pair, subject to [[transfer-feasibility]] on the specific token.
- Authenticated trading requires a non-Korean IP: the Korean (Chuncheon) box is geo-blocked (403), so live OKX trading runs from Render Singapore.

_Only fields the API returns or the operating docs state are recorded here._
