---
chain: solana
type: chain
layer: L1
role: fast, low-cost L1; attractive delivery network when both venues support it
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Solana

Solana is a high-throughput L1 with low transfer cost and fast finality, which makes it an attractive **delivery network** for cross-venue arb when both venues support the token on it. Several tokens in this vault route across Solana connectivity — [[ROAM]]'s transfer map, for instance, maps primarily to Solana across its venues.

## Role in transfer routes

Solana's speed and low fee are exactly the properties an arb wants: a fast confirmation keeps the leg open for less time, so less [[executable-spread]] drifts away before the coin arrives, and a low withdrawal fee leaves more of the gap intact. When a token is movable on Solana and both channels are open, it is often the preferred route in a [[transfer-feasibility]] check.

## The usual caveat

Solana being *listed* at both venues is still not the same as *open* at both. Bitget's [[ELIZAOS]] freeze on 2026-07-12 was specifically a **Solana-deposit** closure — the same one-way-door pattern as [[BTR]], just on a different chain. A fast, cheap chain closes just as hard as a slow one; the deposit-path principle ([[transfer-feasibility]]) does not care how good the network is if the receiving side is shut. Congestion incidents, when they occur, also stall confirmations and should be treated as a temporary feasibility risk on the route.
