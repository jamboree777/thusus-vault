---
concept: quiet-size
type: concept
aliases: [quiet size, optimal size, footprint, non-impact size]
related: [executable-spread, orderbook-probing, nw-grade, five-min-settlement]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Quiet size — harvesting without moving either book

**Quiet size** is the largest position you can take on both legs of an arb *without moving either order book against yourself.* Trade smaller than quiet size and you leave money on the table; trade larger and your own flow eats the spread you came for. It is the size at which the harvest is invisible to the market you are harvesting.

## The footprint rule

NightWatch's working heuristic: each leg's fill should consume **no more than about 25% of the available depth** on that side. Cross that line and your buying visibly lifts the ask, your selling visibly presses the bid, and the executable spread ([[executable-spread]]) collapses under your own weight — the very gap you measured disappears as you take it.

Because an arb has two legs, quiet size is bounded by the **thinner** of the two books. The sell leg is almost always the binding one: buying is reversible (worst case you hold what you bought), but a sell leg with no depth turns an accumulated position into a *strand* — tokens you can only offload by crashing the price. So quiet size is set by confirmed sell-side absorption, never by the buy side.

## Why the visible book understates it

A static order-book snapshot both over- and under-states quiet size. It overstates it when the visible depth is spoof/layering that vanishes on approach. It **understates** it when a market-maker is penny-jumping and refilling — the book looks thin but heals every time it is hit, so true quiet size is far larger than the snapshot. You cannot tell which from a snapshot; you have to poke it. That is what [[orderbook-probing]] is for: quiet size is not read off the book, it is *measured* by probing how the book refills.

## Relationship to grade

[[nw-grade]] tells you a market is deep and tight in general; quiet size tells you how much *you specifically* can move through it *right now* without leaving a footprint. A grade-A market has a large quiet size; a grade-D market's quiet size may be a few hundred dollars. Sizing to quiet size — and re-probing as you scale — is how an arb stays profitable instead of paying its edge back as slippage.
