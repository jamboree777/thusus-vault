---
concept: mirage-arb
type: concept
aliases: [MIRAGE, mirage arb, mirage arbitrage, uncapturable spread]
related: [transfer-feasibility, one-price, executable-spread, nw-grade]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# MIRAGE arb — the gap you can see but cannot capture

A **MIRAGE arb** is a cross-exchange price gap that is completely real on the screen and completely uncapturable in practice, because you cannot move the token from where it is cheap to where it is dear. The spread exists; the trade does not. NightWatch calls it a mirage because it has every visual property of an opportunity and none of the substance.

The word is ours, and it names the single most common way a naive [[one-price]] gap fools a trader.

## Why the gap stays open

Arbitrage closes gaps by *delivery* — buy cheap here, ship the token there, sell dear. Remove delivery and the closing mechanism is gone, so the gap simply persists. Delivery is removed whenever [[transfer-feasibility]] fails:

- a venue has **frozen deposits** on the relevant chain (you can buy the token but not deliver it into the rich venue);
- the two venues **share no open network** and no hub bridges them;
- the rich-side book is a **stranded ghost quote** — technically there, economically dead (see [[2026-03-24-btr-crash]]).

In every case the price screen shows a fat spread and the arbitrageur who tries to take it discovers, only after buying, that the exit is walled off.

## The canonical example

[[BLAST]] on 2026-07-13: liquidity grade A, an open book on [[bybit]] (contract `0xb1a5700f…88e2ad`, verified), and simultaneously **both deposits and withdrawals blocked on [[upbit]]** for the Blast network (`dep=false`, `wd=false`, confirmed by our weekly sweep). Any KRW-vs-global gap on BLAST that day was a mirage: you could not deliver the token into or out of the Korean venue. See [[2026-07-13-blast-wallet-lockdown]].

The [[BTR]] premium on [[bitget]] ([[2026-03-24-btr-crash]]) is a second, uglier variety: not just transfer-blocked but a market being wound down, whose "premium" is a stale quote rather than demand.

## The lesson

The moat is not seeing the gap — a price feed sees the gap. The moat is knowing, before you commit capital, whether the gap is money or a mirage. That judgment is exactly what [[transfer-feasibility]] and [[nw-grade]] combine to give: liquidity *and* movability, read together. Either one alone will lie to you.
