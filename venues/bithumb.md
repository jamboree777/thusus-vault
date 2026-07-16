---
venue: bithumb
type: venue
kind: cex
fiat: [KRW]
taker_fee: 0.04
maker_fee: null
premium_lean: neutral
bias_pct: null
geo: KRW venue; geo-blocked for non-Korean IPs (scanned from the Chuncheon box)
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Bithumb

Korea's second major exchange and a **KRW venue** — the other Korean side of the [[kimchi-premium]] / [[won-carry]] map, alongside [[upbit]].

## Fees

Spot **taker 0.04%** (from `/arb/fees`) — the **lowest taker fee of any venue** NightWatch scans. Maker not published (`null`).

## Habitual premium bias

Bithumb was **below the minimum-sample threshold** in the trailing-14-day market-wide premium run (the summary reported no stable market-level lean for it), so no `bias_pct` is recorded here rather than inventing one. As with [[upbit]], any Bithumb premium must be read basis-adjusted ([[stablecoin-basis]] → [[won-carry]]), never raw.

## Traits we can state

- **KRW settlement**, same as Upbit — a Bithumb leg is a cross-currency trade governed by [[kimchi-premium]] mechanics and a durable fiat-border gap.
- **Geo-fenced**: geo-blocked for non-Korean IPs, reached from the Korean (Chuncheon) box; carries travel-rule friction on cross-border transfers.
- Bithumb is the sole Korean listing for [[BTR]], and — per media reports on the [[2026-03-24-btr-crash]] — was named as the venue that absorbed a large reported supply dump during that crash `[media-reported, unverified]`.

_Only fields the API returns or the operating docs state are recorded here; where a field (bias) had no reliable value it is left null rather than guessed._
