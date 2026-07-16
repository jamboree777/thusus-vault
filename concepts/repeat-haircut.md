---
concept: repeat-haircut
type: concept
aliases: [repeat haircut, re-entry decay, same-pair decay]
related: [quiet-size, executable-spread, orderbook-probing, expectation-gap]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Repeat haircut — the decay of re-entering the same pair

The **repeat haircut** is the extra net edge NightWatch requires before re-entering the *same* pair on the *same* day: about **+0.15 percentage points** of additional required net per re-entry. Each time you go back to the same well, the bar goes up — because the decay is real.

## Why re-entry decays

The first time you harvest a gap, you take the easiest liquidity: the fresh mispricing, the market-maker refill that hasn't yet learned you're there. The second and third times, several things have quietly worsened:

- **You have moved the book.** Your earlier fills consumed the best depth; the remaining liquidity beyond [[quiet-size]] is worse-priced.
- **The counterparty adapts.** A refilling market-maker that got picked off once widens, pulls, or steps less generously the next time — the refill you probed ([[orderbook-probing]]) is not a constant.
- **The signal ages.** A gap that was worth taking at 9:00 is often partly closed by 9:30; re-entering chases a thinner remainder.

So the same nominal spread is worth less on the second pass than the first, and worth less again on the third. Treating every re-entry as if it were the first is how a profitable pair turns into a slow bleed.

## The rule

NightWatch bumps the required net [[executable-spread]] by ~0.15%p for each additional entry on the same pair within a day. A pair has to clear a *higher* bar to justify going back, which naturally rations re-entries to the cases where the edge genuinely refreshed rather than merely reappeared on the screen. It is a small number deliberately — enough to price in the decay, not so large that it forbids legitimately re-opened gaps (a genuine reopen after a [[transfer-feasibility|transfer]] flip resets the clock). The haircut is a discipline against the most seductive mistake in arb: assuming the well is as deep the fifth time as the first.
