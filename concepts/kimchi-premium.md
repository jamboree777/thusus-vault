---
concept: kimchi-premium
type: concept
aliases: [kimchi premium, Korea premium, KRW premium]
related: [stablecoin-basis, won-carry, transfer-feasibility, one-price]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Kimchi premium — the Korea price gap

The **kimchi premium** is the persistent price difference between Korean crypto exchanges ([[upbit]], [[bithumb]]) and the rest of the world. A token frequently trades at a different price in Korean won than its global USDT price implies, and unlike a normal [[one-price]] gap this one does not close on its own — because a **fiat border** and capital-flow friction sit between the two markets.

## Why it persists

Ordinary arbitrage closes a gap by moving the asset. The kimchi gap resists that because moving value across the Korean border is slow, regulated (travel-rule reporting), and capacity-constrained. Global market-makers cannot freely flood won markets with cheap coin or drain expensive coin, so the premium (or discount) can sit for extended periods. It oscillates — sometimes Korea is dear, sometimes cheap — rather than converging to zero.

## The premium is not the edge

The naive read is "Korea trades 2% rich, so short Korea / long global." That is wrong twice over. First, the raw won-vs-USDT gap is contaminated by the [[stablecoin-basis]] — USDT itself trades off its official USD/KRW value on Korean venues, so part of what looks like a token premium is really a stablecoin artifact. The premium you can actually act on is [[won-carry|relative edge = premium − basis]]. Second, capturing it requires a **transfer vehicle**: you must cross the border via *some* token, and that token's own premium is the real P&L.

## Directional vehicle logic

Because value has to cross the border in a token, the vehicle choice *is* the strategy:

- **Korea → overseas** (moving value out): buy in Korea, withdraw, sell overseas. Send out via the **maximum-discount / minimum-premium** token — a discount token profits, a premium token loses.
- **Overseas → Korea** (moving value in): buy overseas, deposit, sell in Korea. Bring in via the **maximum-premium** token — a premium token sold high in Korea profits.

This is the [[won-carry]] mechanic in practice, and every vehicle candidate still has to clear [[transfer-feasibility]]: same-token identity, chain open, buy-side withdrawal open, sell-side deposit open, and a real executable size. The KRW venues are geo-fenced (see [[upbit]] / [[bithumb]]), which is part of why the gap is durable.
