---
title: BLAST wallet lockdown on Upbit — grade A yet transfer-blocked
type: event
date: 2026-07-13
tokens: [BLAST]
venues: [upbit, bybit]
status: resolved
verification: verified
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# 2026-07-13 — BLAST wallet lockdown on Upbit

The canonical example of the [[nw-grade]] trap and the [[mirage-arb]] pattern in one clean case: a token that is liquidity **grade A** and yet, for a window, **completely transfer-blocked** on one venue. Everything here is verified against NightWatch's own weekly sweep and the exchanges' coin APIs.

## What happened (verified)

- **[[BLAST]] carries NW Grade A** (`nw_grade: A`, `nw_grade_worst: A`) — a clean, deep, liquid book. Verified contract on the Blast network: `0xb1a5700fa2358173fe465e6ea4ff52e36e88e2ad` (`identity: verified_same`).
- On **[[upbit]]**, both **deposits and withdrawals were blocked** for the Blast (blastnet) network on 2026-07-13 — `dep=false`, `wd=false`, confirmed by NightWatch's weekly sweep. Both doors shut, not one.
- On **[[bybit]]**, the **same token was fully open** — both deposits and withdrawals available, same verified contract `0xb1a5700f…88e2ad`.

## Why it is the canonical case

Read the two facts together. Liquidity was excellent (grade A). Transferability, on the Korean side, was zero. Any Upbit ↔ Bybit price gap on BLAST during the lockdown was a **pure [[mirage-arb]]** — you could see it, you could not deliver into or out of Upbit to capture it. The book was worth trading *if you could get to it*, and you could not.

This is exactly why NightWatch keeps [[nw-grade]] (a **liquidity-only** measure) and [[transfer-feasibility]] as **separate dimensions**. Grade A said "the market is good." Transfer said "you cannot move the coin." Either number alone would have lied; only together do they tell you the gap is a mirage.

## Resolution

The lockdown was short. NightWatch's live wiki records that Upbit **briefly suspended** Blast-network deposits and withdrawals and **resumed operations about two days later** (the [[BLAST]] note now shows `transfer: open` again as of 2026-07-16). The event is `resolved` — but the window it opened is the clearest teaching case in the vault for grade-versus-transferability. The reopen is precisely the kind of state-flip NightWatch logs, because the instant a stranded gap becomes real is the instant it is worth acting on. See [[BLAST]], [[upbit]], [[bybit]].
