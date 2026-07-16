---
venue: bybit
type: venue
kind: cex
fiat: [USDT]
taker_fee: 0.1
maker_fee: null
premium_lean: neutral
bias_pct: 0.008
geo: authenticated endpoints geo-block the Korean (Chuncheon) IP (403); traded from Render Singapore
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Bybit

A major global venue with strong derivatives and a deep spot book on liquid names. It carries the verified [[BLAST]] listing that sits at the center of the [[2026-07-13-blast-wallet-lockdown]] case.

## Fees

Spot **taker 0.1%** (from `/arb/fees`). Maker not published (`null`).

## Habitual premium bias

Trailing 14 days: **neutral**, essentially balanced (about **46% cheap / 54% rich**, `bias_pct +0.008` — the smallest bias of any venue). Bybit appears on the *sell-here* list by a slim margin. In practice it is close to unbiased and is chosen as a leg on the merits of the specific pair, not a standing habit.

## Traits we can state

- On [[BLAST]], Bybit kept **both deposits and withdrawals open** (contract `0xb1a5700f…88e2ad`, verified) exactly when [[upbit]] shut both — making the Bybit ↔ Upbit BLAST gap a textbook [[mirage-arb]]: real on screen, dead on delivery. See [[2026-07-13-blast-wallet-lockdown]].
- On [[FOXY]] (Linea), Bybit was withdrawal-only after a 2026-07-12 deposit freeze — another case where "listed" ≠ "movable" ([[transfer-feasibility]]).
- Authenticated trading requires a non-Korean IP: the Korean (Chuncheon) box is geo-blocked (403), so live Bybit trading runs from Render Singapore.

_Only fields the API returns or the operating docs state are recorded here._
