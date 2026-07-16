---
chain: bsc
type: chain
layer: L1
role: low-cost high-throughput L1; common cheap delivery network across global venues
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# BSC (BNB Smart Chain)

BSC is a low-cost, high-throughput L1 that is widely supported across the global venues NightWatch scans, which makes it a frequent and inexpensive **delivery network** for cross-venue transfers. Tokens in this vault deploy here routinely — [[BTR]] on BSC (`0xfed1…`), [[ROAM]] on BSC (`0x3fef…`).

## Role in transfer routes

Because BSC withdrawal costs are low and confirmation is fast, a BSC leg preserves more of the [[executable-spread]] than a congested Ethereum leg. When a token is movable on BSC and both venues have the channel open, it is often the economical route in a [[transfer-feasibility]] check. On multi-chain tokens, BSC is one of the chains a hub like [[mexc]] bridges — part of how a "directly blocked" pair can still move in two hops.

## Caveat

The same discipline applies as everywhere: listed on BSC at both venues is necessary but not sufficient — both deposit and withdrawal channels for that specific chain must be open. Cheapness of the network never substitutes for an open deposit path ([[transfer-feasibility]]).
