---
type: lesson
date: 2026-07-19
trigger: "Pipeline unification went LIVE (triggers = livescan + woncarry only; hedge = step-3 attachment; hedged engine retired; woncarry private ledger retired -> book-gating; upbit activated with $2,000 seed). Robin ordered the definitive 2-Book capital back-solve on the clean single-ledger structure as the investor-negotiation candidate numbers."
problem: "Yesterday's korea number ($15k R1-optimized) was computed on a smaller history. Re-running on the full clean history returned KOREA $24k (+$2k upbit seed) -- capital went UP, which looks like a regression unless honestly explained."
change: "Ran tools/nw_realloc_backtest.py --apply-r1 --write-alloc --write-r1-ledger at the LIVE config ($500 trigger x 30m cadence, cap-exempt R1, cross-engine dedup, static global book). Re-seeded the upbit $2,000 forward-looking FLOOR after the solver run (no history -> solver deletes it). Stamped notes 'final-unified-backsolve 2026-07-19, provisional'. Fixed global capital_short $104.40 (livescan HOME binance buy breached the $1,000 line) by bumping global binance to $2,000. Full-row backups to Chuncheon audit_logs before every write."
expected_effect: "Live /arb/thusus/fund: TOTAL $37,000 (korea $26k + global $11k), both books invariant_ok, books_reconcile_ok, capital_short $0. Realized to date $441.02 -> implied realized ROI 1.19% on the back-solved initials."
review_after: 2026-07-25
status: active
supersedes: lessons/2026-07-18-r1-optimization-korea-capital.md
---

# Final unified back-solve: a static replay number GROWS with executed logistics

The definitive 2-Book back-solve on the unified single-ledger structure gives **$37,000 total**
(KOREA $24,000 R1-optimized + $2,000 upbit seed floor; GLOBAL $11,000 static). KOREA raw-static
(no R1) would be $48,000 — **R1 halves the korea requirement**.

## Why korea went UP ($15k -> $24k) — and why that is honest

Not a tool regression (same md5, same flags, same $500/30m config as 07-18). Two real causes:

1. **History tripled**: korea book 07-17 = 42 trades ($13.5k bithumb buys) -> 07-18 = **122
   trades ($32.4k)**. 164 trades, $47,070 settled volume.
2. **The live QM actually executed R1/pre-emptive return batches** (07-18 12:27-17:40 UTC,
   12 non-backfill transfers, gross **$18,408** global->bithumb). A zero-start replay must
   pre-fund each source venue for its executed outflows: gateio bottomed at exactly -$5,000
   (two executed $2,500 legs), kucoin -$5,053.89, and gateio/binance/bybit share the same
   low-water timestamp 15:41:42 (one netted batch). **The offshore korea lines are the paid
   invoices of executed capital logistics, not phantom deficits.** Meanwhile bithumb itself
   FELL 6,000 -> 5,000 — R1 pressing the drain down exactly as designed.

## The class of lesson

A **static back-solve is a replay-of-history number: it monotonically grows as executed
transfers accumulate**, because every executed outflow must be pre-funded at its source in the
replay. It is the honest "what did history cost" number, not the forward steady-state need.
Forward structure (label clearly when negotiating): peak concurrent open korea notional was
only **$2,320**; steady state = bithumb refill float ~$5k + ~$2.3k open + small venue floats,
with R1 recycling the rest. Present investors the replay-honest $37k WITH this structure
alongside — both without spin.

Also: forward-looking seed floors (upbit $2,000, no history) are invisible to a back-solver —
any rewrite of the book must re-assert them explicitly ([[quartermaster]], [[woncarry]]).

Verification: /arb/thusus/fund books.korea {26,000 / realized 328.57 / invariant_ok / short 0},
books.global {11,000 / 112.45 / invariant_ok / short 0}, books_reconcile_ok true. All numbers
**provisional until Robin finalizes**.
