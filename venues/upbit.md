---
venue: upbit
type: venue
kind: cex
fiat: [KRW]
taker_fee: 0.05
maker_fee: null
premium_lean: neutral
bias_pct: 0.0858
geo: KRW venue; geo-blocked for non-Korean IPs (scanned from the Chuncheon box)
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Upbit

Korea's largest exchange and a **KRW venue** — it settles in won, not USDT, which makes it one side of every [[kimchi-premium]] and [[won-carry]] calculation.

## Fees

Spot **taker 0.05%** (from `/arb/fees`) — among the lowest anywhere, a feature of the Korean venues. Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **neutral** (about **48.5% cheap**, `bias_pct +0.0858`). But note: the raw won-vs-USDT comparison is contaminated by the [[stablecoin-basis]], so Upbit's *token* premium should always be read basis-adjusted ([[won-carry]]), not off the raw number.

## Traits we can state

- **KRW settlement.** Upbit prices in won; any arb involving Upbit is a cross-*currency* trade, not just cross-exchange, and inherits the [[kimchi-premium]] mechanics — the gap is durable because a fiat border sits in the middle.
- **Geo-fenced.** Upbit is geo-blocked for non-Korean IPs; NightWatch reaches it from the Korean (Chuncheon) box, which is *why* the same box is blocked (403) on the global venues' authenticated endpoints. The geo split is structural to how the whole system is wired.
- Any Korean leg carries **travel-rule** friction on cross-border transfers, part of why the kimchi gap persists.
- On [[BLAST]], Upbit **shut both deposits and withdrawals** for the Blast network on 2026-07-13 (`dep=false`, `wd=false`, weekly-sweep verified), briefly stranding an otherwise grade-A token, then resumed a couple of days later. See [[2026-07-13-blast-wallet-lockdown]].

_Only fields the API returns or the operating docs state are recorded here._
