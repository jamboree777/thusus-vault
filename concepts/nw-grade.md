---
concept: nw-grade
type: concept
aliases: [NW Grade, liquidity grade, grade]
related: [executable-spread, quiet-size, one-price, transfer-feasibility]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# NW Grade — the A–F liquidity grade

**NW Grade is NightWatch's single-letter liquidity grade** — **A** (deepest, tightest, most liquid) down to **F** (worst) — computed per token from its spread, depth, and 24-hour volume, and stored per `(exchange, symbol)`. It is the same grade the Crisis Bulletin shows and the same grade the board warnings fire on. One canonical grade, surfaced everywhere as a badge.

## How it aggregates

A base symbol has one grade per venue it lists on. The badge you see is the **best** grade across those venues — a token needs only one genuinely good market to be usable. Alongside it we keep `nw_grade_worst`, the **worst** venue's grade, for risk context: how bad the weakest market is. Letters rank `A=5 > B=4 > C=3 > D=2 > F=1` to pick best and worst. A venue with no stored grade is skipped; a base with no graded venue at all returns null.

For example [[FOXY]] carries `nw_grade: A` but `nw_grade_worst: F` — one venue's market is excellent, another's is barely tradeable. The badge alone would flatter it.

## The one thing NW Grade does *not* tell you

**NW Grade is liquidity-only.** It measures how deep and tight a market is — nothing else. In particular it says nothing about whether you can *move* the token.

This is the trap worth internalizing: **a token can be grade A and still be transfer-blocked.** [[BLAST]] is the canonical case — a clean grade A, an excellent book on [[bybit]], and yet on [[upbit]] both deposits and withdrawals were shut ([[2026-07-13-blast-wallet-lockdown]]). The liquidity was real; the [[transfer-feasibility|transferability]] was not. Grade A tells you the book is worth trading *if you can get to it*. Whether you can get to it is a different dimension entirely — see [[mirage-arb]].

## Why it is cheap and canonical

The grade is served on-read from data already in the database — zero live exchange fetches, pure reads plus arithmetic, cached. There is exactly one grade; nothing recomputes or reinvents it. That discipline (born of a past out-of-memory incident) is why the grade is trustworthy as a stable key: it is the same number everywhere it appears.
