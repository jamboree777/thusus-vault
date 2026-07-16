---
concept: identity-verification
type: concept
aliases: [identity verification, contract identity, ticker collision, symbol collision]
related: [transfer-feasibility, mirage-arb, one-price]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Identity verification — is it even the same token?

Before any cross-exchange gap can be an opportunity, one question has to be answered: **are the two listings actually the same asset?** A shared ticker is not proof. NightWatch establishes identity from the **on-chain contract address checked against the project's official documentation** — never from the symbol alone.

## Symbol collisions (the trap)

Tickers are not unique. Two entirely different projects can ship the same three or four letters, and an "arb" between them is not an arb at all — it is two unrelated assets that happen to share a name. The [[BTR]] case is the textbook example: the BTR on our venues is the official **Bitlayer** token (verified against Bitlayer's own docs across BSC, Ethereum, and the Bitlayer chain), but there also exists an unrelated **Bitrue Coin (BTR)** on Ethereum at a different contract. Confuse the two and you would "arbitrage" a spread that cannot exist, because the coin you bought is not the coin the other venue lists.

So a collision is a **hard exclude**, not an opportunity. The frontmatter records the result as `identity: verified_same`, `unverified`, or `collision`.

## Same identity, different chains

The inverse also holds: the same token can have **different contract addresses on different chains** and still be one asset (a genuine multi-chain deployment). [[BTR]] is BSC `0xfed1…`, Ethereum `0x6c76…`, and Bitlayer `0x0e4c…` — three addresses, one Bitlayer token. Here identity is verified, and the open question shifts to *routing*: which chains actually connect the venues (see [[transfer-feasibility]]). Identity tells you it is the same coin; feasibility tells you whether the coin can move.

## The weekly sweep

Identity and its associated contracts are refreshed by a periodic (weekly) sweep against exchange contract data and on-chain checks, so a listing that quietly re-points to a different contract, or a new collision that appears, is caught rather than assumed stable. Identity is the *first* gate in the dossier — nothing downstream ([[transfer-feasibility]], grading, sizing) means anything until it passes.
