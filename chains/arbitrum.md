---
chain: arbitrum
type: chain
layer: L2
role: low-fee Ethereum L2; cheap delivery network with small median withdrawal cost
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Arbitrum

Arbitrum is an Ethereum **L2** — it settles to Ethereum while executing cheaply off-chain, so transfers avoid the gas sensitivity of L1 [[ethereum]]. Like [[base]], that makes it a low-cost **delivery network** for cross-venue arb when both venues support the token on it.

## Role in transfer routes

The key property for arb delivery is the **small median withdrawal cost**: NightWatch's paper-engine cost tables put L2 withdrawal-fee medians in roughly the **$0.00–$0.64** band, low enough that the transfer fee rarely dominates the [[executable-spread]]. When a token is movable on Arbitrum with both channels open, the L2 route is generally preferred to the L1 one on cost.

## Caveat

Bridge and confirmation timing still register as latency in a [[transfer-feasibility]] assessment, and a token *listed* on Arbitrum at both venues must have both deposit and withdrawal channels *open* to be a real route. The cheap network reduces delivery cost, not the deposit-path requirement. See [[base]] for the sibling L2 and [[ethereum]] for the L1 that BTC-chain latency (30–60 min, excluded from the paper engine) sits well beyond.
