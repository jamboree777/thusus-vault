---
type: lesson
date: 2026-07-18
trigger: "opportunity density > capital → per-venue adaptive sizing. Day-one shadow showed good opportunities concentrating on a few capital-consumption points (gateio/bithumb buys, the tiny KRW pool, the $75 gate-futures hedge pool) while the fund as a whole sat idle — a global average hid the local starvation the Quartermaster had already measured."
problem: "A single fund-wide size/threshold cannot express that capital is scarce at ONE venue and slack everywhere else. Deploying max size at the bare 0.5% floor on every candidate spends the scarcest capital on marginal edges; averaging pressure across all venues makes a real gateio/KRW bottleneck invisible. The fund needs to raise quality (and, only then, split smaller) exactly where opportunities out-number capital — and nowhere else."
change: "New shared layer nw_dynamic_sizing.py (NW_DYN_*). Per pass, per capital-consumption POINT (buy exchange for livescan/bigspike; KRW/abroad pool for woncarry; buy exchange AND hedge pool for hedged, taking the max), compute pressure = Σ(candidate target size at the point) ÷ available capital, then walk a 2-stage staircase: STAGE1 raises the net threshold 0.5→0.6→0.7→0.8%, and only once 0.8% is exhausted STAGE2 lowers max size $300→$270→$240→$210 (floor −30%, min $40 unchanged). Relaxation is the same ladder in reverse (restore size before dropping threshold); hysteresis is asymmetric — escalate fast to protect quality, relax one notch per pass behind a DOWN band. A slack point keeps base; only bottlenecked points tighten."
expected_effect: "Higher risk-adjusted return per unit of the SAME $10k fund: the scarcest capital is spent on 0.8% A-grade edges instead of 0.5% marginal ones, and only over-subscribed A-grade points diversify into smaller tickets. Each trade stamps assumptions.dyn (threshold, max, pressure, stage, point, cap_source) so 7-day attribution can test whether the density regime actually lifted Sharpe. At the STAGE2 floor with pressure still >1 the overflow is skipped and logged as capital_short — direct evidence for a fund-size / rotation-speed increase. First live passes: gate-futures pool ($75) and the KRW pool ($19) hit the floor immediately while the bybit hedge pool ($300, pressure 4) held at 0.8%/$300 — the per-venue differentiation the design is for."
review_after: 2026-07-25
status: superseded
supersedes: null
superseded_by: "[[2026-07-18-dynamic-sizing-simplified]]"
---

> **SUPERSEDED 2026-07-18** by [[2026-07-18-dynamic-sizing-simplified]]: the
> capital-pressure staircase never fired in the abundant-capital paper env and
> was replaced with a single adaptive-threshold hill-climb on trade count. The
> NW_DYN_T*/S*/UP/DOWN/step/size params below are RETIRED.

# The fund wasn't out of money — one venue was

Day one's shadow book had a shape the fund-wide numbers couldn't see. The $10k
treasury was mostly idle, yet the *good* opportunities kept landing on the same
few doors: a gateio or bithumb spot buy, the small parked [[won-carry|KRW pool]],
the $75 gate-futures hedge pool. Averaged across ten venues the fund looked
relaxed. At the door where the capital actually had to come from, it was starved
— the same local starvation the [[QUARTERMASTER|Quartermaster]] had already
measured when it found gateio chronically drained as the habitual cheap side.

Deploying the full size at the bare 0.5% net floor on every one of those
crowded-door candidates is the mistake. It spends the scarcest dollar on the
*marginal* edge. When opportunities out-number capital at a point, the fund
should first demand *better* edges there (raise the threshold), and only if
A-grade edges still overflow should it split into *smaller* tickets — never the
other way round, and never fund-wide.

## The class of mistake

A global average is the wrong denominator for a per-venue constraint. Capital is
consumed at a *point* — a buy exchange, a hedge pool, a currency pool — and each
point has its own supply. The generalised rule: **size and quality thresholds
must be set against the pressure at the specific point a trade will draw from,
not against the fund as a whole.** Quality first (threshold up), then diversity
(size down); tighten only the bottleneck, leave slack points on base.

## The change

`nw_dynamic_sizing.py` — one stateless helper `resolve_sizing(pressure)` plus a
cached fund fetch, shared by all four engines. Per pass, each engine computes
`pressure(point) = Σ(target size of this-pass candidates routed through the
point) ÷ available_capital(point)` and walks the 2-stage staircase:

- **STAGE 1 — threshold first**: 0.5 → 0.6 → 0.7 → 0.8% as pressure climbs.
- **STAGE 2 — size second** (only after 0.8% is exhausted): $300 → $270 → $240
  → $210 (−10% ×3, floor). Min $40 never moves.

Relaxation is the *reverse* ladder — size is restored to $300 before the
threshold drops back toward 0.5% — so quality is protected to the last. A
[[repeat-haircut]]-style hysteresis band (escalate above boundary·`NW_DYN_UP`,
relax below boundary·`NW_DYN_DOWN`) stops flapping; escalation is deliberately
fast (protect quality now), relaxation slow (one notch per pass).

Available capital is sourced honestly: spot venues use `balances[venue] +
treasury_remaining` from `/arb/thusus/fund` (the shared treasury *is* deployable
in the paper model, so early — treasury full — pressure is low and sizing is
base; as trades pile up and the treasury drains, the denominator shrinks and the
staircase climbs on its own). Hedge pools use the Quartermaster's own v0.2
reservations ($300 bybit UTA, $75 gate futures); [[won-carry]] uses its own
derived KRW/abroad pools. Each source is labelled in the trade's `assumptions.dyn`.

## Why per-point, not global (the evidence)

The very first live passes proved the point differentiates. On the hedged engine
one pass showed `perp:gate` (a $75 pool) pinned at the **0.8% / $210 floor** while
`perp:bybit` (a $300 pool) held at **0.8% / $300** — same pass, same candidates,
two different sizes because the pools are two different sizes. The KRW pool
($19 free) hit the floor while the abroad pool ($9,836) stayed on base and was
never even tightened. That is the whole design: **do not globally tighten.**

## Review

By 2026-07-25, with a week of `assumptions.dyn`-stamped settlements: slice
realized net and Sharpe by `stage` / `pressure` bucket. Did the escalated
(0.7–0.8%) regime actually deliver higher risk-adjusted return than the base
0.5% regime on the same venues? Are the `capital_short` counts concentrated
enough to justify a fund-size or rotation-speed increase, or are the boundaries
(`NW_DYN_T1..T3`, `S1..S3`) mistuned — escalating on noise, or never reaching
STAGE2 where it matters? Tune the boundaries or the hysteresis band from that,
not from intuition.

_Related: [[QUARTERMASTER]] · [[won-carry]] · [[quiet-size]] · [[executable-spread]] · [[repeat-haircut]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
