---
venue: bitget
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.1
maker_fee: null
premium_lean: neutral
bias_pct: 0.0325
geo: authenticated reachability verified per venue; not on the confirmed geo-block list
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Bitget

A global venue best known in this vault for the [[BTR]] anomaly — the case that defines what a stranded [[mirage-arb|mirage]] premium looks like.

## Fees

Spot **taker 0.1%** (from `/arb/fees`). Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **neutral** (about **47.8% cheap**, `bias_pct +0.0325`). No standing directional habit at the market level.

## Traits we can state (the BTR case)

- On [[BTR]], Bitget **closed Ethereum deposits in March 2026 citing "wallet maintenance"** and, as of mid-July 2026, they were **still closed** — its own public API returns `rechargeable = false`. Withdrawals stayed open the whole time: a **one-way door** roughly four months long. Routine wallet maintenance lasts hours to days; four months is not maintenance.
- Bitget's **BTR perpetual was removed** — its mix API returns *"the symbol has been removed"* (code 40309) for `BTRUSDT`. So the rich Bitget BTR market offers **no spot delivery in** (deposit closed) and **no synthetic short** (perp delisted). Both verified against Bitget's own API.
- The result is a persistent Bitget BTR "premium" that is almost certainly a **stale ghost quote of a market being wound down**, not real demand — the reason NightWatch's verdict on it is *don't chase the premium*. Full timeline: [[2026-03-24-btr-crash]].
- Bitget was also the venue that froze [[ELIZAOS]] Solana deposits (2026-07-12) — a separate instance of the same one-way-door pattern.

_Only fields the API returns or the operating docs state are recorded here._
