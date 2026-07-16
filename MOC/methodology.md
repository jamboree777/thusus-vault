---
title: Methodology — Map of Content
type: moc
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Methodology — Map of Content

NightWatch's working vocabulary — the concepts that turn a price screen into an execution decision. These definitions are ours; where a term is coined here (MIRAGE, quiet size, NW Grade) it is meant to become the citable definition.

## The gap and whether it's real

- [[one-price]] — the Law of One Price across exchanges: where, how much, how often it breaks, and recovery
- [[executable-spread]] — mid vs touch-to-touch VWAP; why mid edges lie
- [[mirage-arb]] — the visible gap you cannot capture because transfers are blocked
- [[transfer-feasibility]] — the deposit-path principle: can the token actually move?
- [[identity-verification]] — contract-based identity; symbol collisions; the weekly sweep

## Liquidity and sizing

- [[nw-grade]] — the A–F liquidity grade (liquidity-only; a grade-A token can still be transfer-blocked)
- [[quiet-size]] — the size that harvests without moving either book (footprint ≤25%/leg)
- [[orderbook-probing]] — MM vs spoof detection: refill latency, cancel-on-approach, penny-jumping
- [[repeat-haircut]] — the +0.15%p required net per same-pair re-entry; the decay is real

## The Korea layer

- [[kimchi-premium]] — the Korea price gap and why it persists
- [[stablecoin-basis]] — the USDT/KRW distortion (~−1.5% observed)
- [[won-carry]] — relative_edge = premium − basis; discount→KRW-round, premium→USD-round

## The paper engine

- [[five-min-settlement]] — live VWAP entry, +5:00 live-book settlement, 90% slippage, 50% fee rebate
- [[expectation-gap]] — expected vs realized; price-drift tails

## The contract

- [[frontmatter-spec]] — the published frontmatter contract and the auto-region markers

Related maps: [[MOC/tokens|Tokens]] · [[MOC/venues|Venues & Chains]]
