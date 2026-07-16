---
concept: transfer-feasibility
type: concept
aliases: [transfer feasibility, deposit path, movability, transferability]
related: [mirage-arb, identity-verification, one-price, nw-grade]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Transfer feasibility — can the token actually move?

**Transfer feasibility** answers the question a price screen never asks: if I buy this token on venue A, can I actually *deliver* it to venue B to sell? Without a yes, a cross-exchange gap is a [[mirage-arb]] — real on screen, uncapturable in practice.

## The deposit-path principle

The thing that matters is **not** whether the two venues list "the same token" in the abstract. It is whether the specific coin you bought can be **deposited** at the venue where you want to sell it. That requires an open path:

```
withdrawal chain at venue A  ∩  deposit chain at venue B  ≠  ∅
```

— and both of those channels have to be *open*, not merely *listed*. A shared open network is the requirement. Contract identity alone ([[identity-verification]]) is necessary but not sufficient: two venues can list the genuinely-same token and still have no open path between them if the chains they support don't overlap, or if the one shared chain has deposits frozen on the receiving side.

## Hub routing (the 2-hop path)

Sometimes a *direct* path is blocked but a **hub venue** bridges it. [[mexc]], for instance, lists many tokens across several chains at once and can act as a bridge: A → MEXC on chain X, MEXC → B on chain Y. A pair that looks "blocked" directly may in fact be movable in two hops through the hub — an execution path others miss. So transfer feasibility is evaluated over direct *and* hub routes.

## The failure modes

- **Frozen deposit (one-way door):** the receiving venue has deposits closed on the only shared chain. You can buy the token; you cannot deliver it. [[BTR]] on [[bitget]] — deposits closed since March 2026 while withdrawals stayed open — is the archetype ([[2026-03-24-btr-crash]]).
- **Both sides frozen:** [[BLAST]] on [[upbit]], 2026-07-13 — deposits *and* withdrawals shut for the Blast network ([[2026-07-13-blast-wallet-lockdown]]).
- **No shared open network:** the venues simply don't overlap on any open chain, hub included.

## Authority and freshness

Current deposit/withdrawal status is read from each exchange's **own public coin API** — the authoritative source — not inferred. Status flips (froze, reopened) are logged over time so the *reopen* moment, the instant a stranded gap becomes real, is captured. Transfer feasibility is a live dimension, not a static fact: a path open this morning can be a one-way door by afternoon.
