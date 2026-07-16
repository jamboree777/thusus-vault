---
chain: ethereum
type: chain
layer: L1
role: canonical settlement L1; common shared network for cross-venue delivery, but gas-sensitive withdrawal cost
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Ethereum

Ethereum is the canonical L1 and the most common shared network on which a token can be delivered between venues. Many tokens in this vault are ERC-20s — [[BTR]] (Ethereum `0x6c76…`), [[ELIZAOS]] (`0xea17…`) — so Ethereum is frequently the chain a [[transfer-feasibility]] check hinges on.

## Role in transfer routes

When two venues both support a token on Ethereum *and* both channels are open, Ethereum is the delivery path. The catch is that it is often the chain a venue **freezes**: the [[BTR]] one-way door was specifically an *Ethereum-deposit* closure on [[bitget]] ([[2026-03-24-btr-crash]]). Ethereum being listed at both venues was necessary but not sufficient — the deposit side has to be open, which is the whole deposit-path principle.

## Withdrawal cost and latency

Ethereum withdrawal fees are **gas-denominated and can be significant**, especially when the network is congested, which weighs directly on the [[executable-spread]] of any send-arb that ships an ERC-20. This is why NightWatch prefers an inventory model (pre-positioned balances on both venues) over transfer-per-trade whenever the Ethereum leg is expensive.

## A note on transfer time (why BTC-chain is excluded)

Confirmation latency matters as much as fee. NightWatch's paper engine **excludes BTC-chain routes entirely** because their 30–60 minute transfer time is far too long to hold an arb leg open — the [[executable-spread]] would drift away before the coin arrives ([[expectation-gap]]). Ethereum L1 sits in a middle band: usually fast enough to consider, but slow and dear enough under congestion that L2s ([[base]], [[arbitrum]]) or an inventory model are preferred where available.
