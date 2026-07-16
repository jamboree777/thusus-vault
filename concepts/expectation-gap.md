---
concept: expectation-gap
type: concept
aliases: [expectation gap, expected vs realized, price-drift tails]
related: [five-min-settlement, executable-spread, quiet-size, repeat-haircut]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Expectation gap — expected versus realized

The **expectation gap** is the distance between what a set of trades was *expected* to make at entry and what it *actually realized* at settlement. It is the single most honest number a paper book produces, because it measures how much of the theoretical edge survives contact with a real, moving market.

## Where it comes from

At entry, each trade has an *expected* profit: the [[executable-spread]] at size, net of fees, that the gap implies. At settlement — five minutes later against the live book ([[five-min-settlement]]) — the trade has a *realized* profit, which reflects whatever the price actually did in between. Summed across a day, expected P&L and realized P&L diverge. That divergence is the expectation gap.

## Day-one shape: fat, one-sided tails

On [[Thusus]]'s first paper day ([[journal/2026-07-15]]), the gap was large: **expected ≈ $100.96, realized ≈ $30.20** — the book kept only about 30% of its theoretical edge. Crucially, the shortfall was **not** spread evenly. It was concentrated in a handful of **price-drift tails**: individual names that drifted hard against the position in the five-minute hold and settled at outsized losses —

- [[FOXY]] −$14.93
- [[ELIZAOS]] −$10.24
- [[ROAM]] −$8.61

Those three names alone account for the bulk of the gap between expected and realized. The *median* trade behaved roughly as expected; a few tail events did the damage. This is the characteristic signature: expected P&L is an average over well-behaved trades, and realized P&L is that average minus a few brutal drifts.

## Why it matters

The expectation gap is a design input, not just a scoreboard. It says: the edge is real (realized was solidly positive, +$30.20 on an 80.8% win rate) but **thinner than the mid-price screen advertises**, and the thinning is driven by drift tails you cannot see at entry. The operational responses follow directly — tighter [[executable-spread]] gates so marginal candidates that can't absorb a drift never enter, smaller [[quiet-size]] on names with drift history, and the [[repeat-haircut]] to stop re-entering a decaying pair. Watch the gap over time: if it narrows as the gates tighten, the machine is learning; if it stays wide, the edge is more advertisement than substance.
