---
chain: base
type: chain
layer: L2
role: low-fee Ethereum L2; cheap delivery network with small median withdrawal cost
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Base

Base is an Ethereum **L2** — it settles to Ethereum but executes cheaply off-chain, so transfers are far less gas-sensitive than L1 Ethereum. That makes it a low-cost **delivery network** when both venues support a token on Base.

## Role in transfer routes

The attraction of an L2 like Base for arb delivery is a **small median withdrawal cost**: NightWatch's paper-engine cost tables record L2 withdrawal-fee medians in roughly the **$0.00–$0.64** band — a rounding error next to a congested Ethereum L1 withdrawal, and small enough that it rarely dominates the [[executable-spread]]. Where a token is movable on Base and both channels are open, it is usually preferred over the L1 route for exactly this reason.

## Caveat

L2 confirmation and bridge timing still count as latency in a [[transfer-feasibility]] check, and — as always — a token *listed* on Base at both venues must have both deposit and withdrawal channels *open* for the route to be real. The low fee lowers the cost of delivery; it does not remove the deposit-path requirement. Compare [[arbitrum]], the other L2 in the same low-median band, and [[ethereum]] for the L1 contrast.
