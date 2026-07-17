---
type: lesson
date: 2026-07-18
trigger: "capital-pressure never fired in the abundant-capital paper env → replaced the whole density staircase with a single adaptive-threshold hill-climb on trade count. Live logs showed the pressure ratio was either ≤1 for hours (idle $10k treasury) or, once the fund accounting drained, pinned at stage 6 / 0.8% blocking every entry — an erratic, capital-coupled signal that never expressed the simple intent 'if we're trading a lot, ask for more edge.'"
problem: "The prior design had two coupled dimensions (capital pressure + activity-count staircase), a 6-notch ladder, a size-reduction stage, and asymmetric hysteresis — a lot of moving parts whose headline signal (pressure = Σsize ÷ capital) does not work in a paper fund where capital is either abundant or mis-accounted. Robin: radically simpler. One lever."
change: "Rewrote nw_dynamic_sizing.py to a single per-engine ADAPTIVE NET THRESHOLD that hill-climbs on the engine's own ENTRY count. State persists in a new table nw_dyn_threshold_state(engine, threshold_pct, …); read at pass start. Every NW_DYN_WINDOW_MIN (60) min compare entries in the trailing window vs the prior equal-length window: count rose beyond ±NW_DYN_DEADBAND (1) → threshold += NW_DYN_STEP_PCT (0.05%); count fell → −= step; ~equal → hold. Bounded [engine_base_gate .. base + NW_DYN_MAX_LIFT (1.5%)], never below base (livescan 0.5, bigspike 3.0, woncarry 0.5, hedged 0.5). The effective entry net-gate = this one adaptive number. SIZE band stays fixed $40-300 — untouched. DELETED: capital-pressure, the fund fetch, activity notches, the size-reduction stage, per-point resolve, hysteresis. Every trade stamps assumptions.dyn = {threshold_pct, window_count, prev_window_count, direction, step, engine, base_gate, window_min, status}. Applied to all 4 engines, each with its own row + base floor."
expected_effect: "Self-limiting hurdle: more trades → the net gate creeps up 0.05%/hr until the trade count stops rising; fewer trades → it creeps back toward base. One number, one step, persisted across restarts. Also fixes the missing-stamp bug — assumptions.dyn is now populated on every new entry (verified on a fresh trade post-deploy) instead of silently null. 7-day review: did the hill-climb hold trade count near a stable band without starving good edges, and is the stamped threshold moving sensibly with activity?"
review_after: 2026-07-25
status: active
supersedes: "[[2026-07-18-dynamic-sizing]]"
---

# One number that creeps

The density staircase was elegant and wrong for this environment. Its headline
signal — *pressure = Σ(target size) ÷ available capital at a point* — assumes the
paper fund's capital figure is a faithful scarcity gauge. It isn't. In the
$10k-treasury shadow fund the ratio sat below 1 for hours (nothing escalated),
then, as the fund reconstruction drained, snapped to stage 6 (0.8% net) and
[blocked every entry](../lessons/PARAMS.md). The thing Robin actually wanted was
much smaller: **if the engine is booking a lot of trades, make it ask for more
edge; if it goes quiet, relax.** That is one lever, not a two-dimensional ladder.

## The class of mistake

Reaching for a rich control law (multi-stage, multi-signal, hysteretic) before a
one-parameter controller has been shown insufficient. Complexity you can't yet
justify is complexity you can't tune or trust. The generalised rule: **start the
controller at one input and one step; add dimensions only when the single lever
demonstrably fails.** A hill-climb on the directly-observed target (trade count)
beats a proxy (capital pressure) that needs a trustworthy denominator we don't have.

## The change

`nw_dynamic_sizing.resolve_threshold(conn, engine, base_gate, count_table, …)`:

- Persist one threshold per engine in `nw_dyn_threshold_state`; seed = base gate.
- Once per `NW_DYN_WINDOW_MIN` (60m): `trailing = entries in [now−W, now]`,
  `prior = entries in [now−2W, now−W]`.
  - `trailing − prior > DEADBAND` → threshold `+= STEP`
  - `prior − trailing > DEADBAND` → threshold `−= STEP`
  - else hold.
- Clamp to `[base_gate, base_gate + MAX_LIFT]`. STEP `0.05%`, MAX_LIFT `1.5%`,
  DEADBAND `1`.
- Effective entry net-gate = the adaptive threshold. Size band untouched ($40-300).
- Stamp `assumptions.dyn = {threshold_pct, window_count, prev_window_count,
  direction, step, engine, base_gate, window_min, status}` on every entry.

Fail-safe: any DB error returns the base gate (`status='error'`) so a hiccup never
blocks entries.

## The missing-stamp bug, closed

Before the rewrite, recent livescan rows carried `assumptions.dyn = null`. Root
cause was NOT a stamp bug — the stamp code was correct — but that the rows
predated the dyn deploy AND no entry had booked since (the pressure signal had
escalated to 0.8% and blocked everything). The simpler controller both (a) makes
the gate move on trade count instead of a stuck pressure ratio, and (b) stamps a
concrete `dyn` dict on every entry. Verified on a fresh trade after deploy.

_Related: [[2026-07-18-dynamic-sizing]] (superseded) · [[THUSUS_OPS_LOOP]] · [[repeat-haircut]] · [[uniform-size-band-diversification|2026-07-18-uniform-size-band-diversification]] · [[Thusus]]_
