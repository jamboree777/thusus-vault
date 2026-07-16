---
concept: orderbook-probing
type: concept
aliases: [order-book probing, probe before trade, MM detection, spoof detection, hidden liquidity]
related: [quiet-size, executable-spread, repeat-haircut, five-min-settlement]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Order-book probing — poke it before you trade it

A static order book lies about how much you can trade. **Order-book probing** is the practice of sending small live orders and reading how the book *reacts* — because true fillable size, and whether a market is real or fake, can only be known by poking it and watching, never from a snapshot.

## Why the snapshot is a lie in both directions

When a market-maker is **penny-jumping** (sitting one tick inside the best ask for queue priority) or **quote-stepping** (the same on the bid), it keeps the visible book thin but **refills the instant it's hit**. The book looks shallow; the liquidity is deep. Conversely, a **spoofer** stacks large visible orders it never intends to fill and **cancels them as you approach** — the book looks deep; the liquidity is a phantom. A snapshot cannot distinguish these. Only the *reaction* to real flow can.

## How to read the reaction

Snapshot the top of book (L2) immediately before and after a small order, and diff the best-quote price, the refilled size, and the **refill latency** (how fast the best quote heals after a hit). Three signatures:

| Behavior on approach | Verdict | Action |
|---|---|---|
| Quote **fills and refills** when hit | real MM liquidity | size up into it |
| Quote **cancels / retreats** as you approach, never fills | spoof / layering | treat book as *visible* depth only |
| One-tick step, trivial size, no refill | dumb penny-stepper | minor edge; size = static book |

The datafied version measures **fill-through rate**, **refill latency**, and **cancel-on-approach ratio**. Real MMs fill; spoofers vanish.

## The asymmetry: sell leg gates

The two legs are not symmetric. **Buying is the safe side** — if a bot refills the ask you keep accumulating, and worst case you simply hold what you bought (reversible). **Selling is the gating side** — you must confirm a hidden *bid* will absorb your unwind *before* you accumulate, or the position becomes a strand (tokens you can only sell by crashing the price). So the protocol is **sell-first**: probe the bid you will later sell into, confirm absorption, and never accumulate more than the sell leg has *confirmed* it will take. This is where [[quiet-size]] actually comes from — it is measured by the probe, not read off the book.

## Pre-screening

Live probes cost something, so candidates are pre-ranked by high-frequency microstructure signals (quote flicker, cancel/replace rate, spread stability) to spend probes only on pairs where a bot is likely present. Probe orders are IOC (immediate-or-cancel) or tiny post-only limits, leaving no resting footprint. Only after both legs confirm hidden depth does execution size up to the probed depth — and it re-probes as it scales, because the sell-side refill capacity is the real, binding size limit (and it decays on re-entry — see [[repeat-haircut]]).
