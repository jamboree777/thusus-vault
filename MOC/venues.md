---
title: Venues & Chains — Map of Content
type: moc
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Venues & Chains — Map of Content

Reusable notes that explain most anomalies across every token: exchange fee/habit/reliability traits, and the chains that carry transfers between them. Fees are from `/arb/fees`; premium leans from `/arb/exchange_premium?days=14`.

## Global venues (USDT)

| Venue | Taker | Habitual lean |
|---|---|---|
| [[binance]] | 0.1% | rich (~64%) — a sell leg |
| [[okx]] | 0.1% | rich (~61%) — a sell leg |
| [[coinbase]] | 0.6% | cheap (~88%) — a buy leg, but the fee bites |
| [[mexc]] | 0.05% | neutral — the transfer hub |
| [[gateio]] | 0.2% | neutral — gas-denominated withdrawals |
| [[kucoin]] | 0.1% | neutral (cheap by frequency, positive avg bias) |
| [[bybit]] | 0.1% | neutral — near-unbiased |
| [[bitget]] | 0.1% | neutral — the BTR one-way door |

## Korean venues (KRW)

| Venue | Taker | Note |
|---|---|---|
| [[upbit]] | 0.05% | KRW; geo-fenced; [[kimchi-premium]] side |
| [[bithumb]] | 0.04% | KRW; lowest fee; [[kimchi-premium]] side |

The KRW venues sit behind a fiat border and are geo-blocked for non-Korean IPs — read their premiums basis-adjusted ([[stablecoin-basis]] → [[won-carry]]), never raw.

## Chains (transfer networks)

- [[ethereum]] — canonical L1; gas-sensitive withdrawals; the chain Bitget froze on [[BTR]]
- [[bsc]] — cheap high-throughput L1; common delivery network
- [[solana]] — fast, low-cost L1; ROAM/ELIZAOS routing
- [[base]] — Ethereum L2; low median withdrawal cost (~$0.00–0.64)
- [[arbitrum]] — Ethereum L2; low median withdrawal cost (~$0.00–0.64)

BTC-chain routes are excluded from the paper engine (30–60 min transfer time — too slow to hold an arb leg). Every route still obeys [[transfer-feasibility]]: listed ≠ open.

Related maps: [[MOC/tokens|Tokens]] · [[MOC/methodology|Methodology]]
