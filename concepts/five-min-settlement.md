---
concept: five-min-settlement
type: concept
aliases: [five-minute settlement, 5-min settlement, paper engine methodology, settlement model]
related: [expectation-gap, executable-spread, quiet-size, orderbook-probing]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Five-minute settlement — the paper engine's honesty model

The **five-minute settlement** is the methodology behind [[Thusus]]'s paper-trading book. It is designed to be *pessimistic on purpose*, so that a paper number is a floor a real fill could plausibly beat, not a fantasy a real fill could never reach. Every trade in the [[journal/2026-07-15|journal]] is settled this way.

## The method, step by step

1. **Live VWAP entry.** The trade enters at the real, volume-weighted average price walked up (or down) the live order-book ladder at the moment of entry — the [[executable-spread]] price at size, not the mid. No idealized touch fill.
2. **+5:00 settlement against the live book.** The position is not marked at entry. It is held and settled **five minutes later against the live order book** at that later moment — so any adverse price drift in those five minutes is charged to the trade. This is where optimistic paper P&L goes to die: a gap that looked good at entry has to *survive five minutes* to pay.
3. **90% slippage applied.** Ninety percent of modelled slippage is applied to the fills — a deliberate haircut so the engine never flatters itself on execution quality.
4. **50% fee rebate.** Fees are charged at the *effective* rate assuming recovery of about half of nominal trading fees (via maker rebates and self-referral), matching the real cost structure the live machine targets — not the full nominal fee, and not zero.

## Why five minutes, and why it matters

Five minutes is long enough that a spread has to be *structural* to survive it and short enough to reflect a realistically prompt unwind. Settling against the live book after a delay is what surfaces the [[expectation-gap]]: the difference between what a trade was *expected* to make at entry and what it *realized* at settlement, driven mostly by price-drift tails in individual names. A trade that entered on a real gap but drifted hard in five minutes settles at a loss — and the engine records that loss honestly rather than marking the entry.

## What it is and isn't

It is still **PAPER / DRY-RUN**: no real capital, simulated fills against real quotes. It does not model every adverse-selection effect a live account meets. But by pairing live VWAP entry with delayed live-book settlement, a 90% slippage charge, and only a 50% fee rebate, it errs toward *understating* performance. That bias is the point — see [[expectation-gap]] for what the settled-vs-expected gap revealed on day one.
