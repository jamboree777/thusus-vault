---
type: lesson
date: 2026-07-16
trigger: "FOXY #7903 (bigspike_sniper_v1, gateio→kucoin, entry spread 0.955%, expected +$1.42 → realized −$14.93). The single largest drift tail of day one, on a spike name, at the full quiet size."
problem: "On volatile spike names a full quiet-size position carries asymmetric 5-minute reversal risk — sizing to the footprint cap maximises exposure exactly in the regime where drift tails live, so the position is largest precisely where the hold is most dangerous."
change: "NW_BIGSPIKE_SIZE_FACTOR: 1.0 (implicit) → 0.5 — halve the chosen quiet size on the sniper, respecting the SIZE_MIN_USD floor."
expected_effect: "Roughly halves the magnitude of sniper reversal tails (a repeat of FOXY would settle near −$7.5, not −$14.9) at the cost of ~half the upside on winners. n=4 too small to tune precisely, so a conservative 0.5."
review_after: 2026-07-23
status: active
supersedes: null
---

# The position was biggest where the hold was most dangerous

[[FOXY]] **#7903** was day one's worst single trade: the big-spike sniper entered a real **0.955%** gap expecting **+$1.42**, and the name drifted so hard over the [[five-min-settlement]] window that it settled at **−$14.93**. Note the spread — under one percent. This was not a wide-spread mispricing (that is a different lesson, the [[ROAM]]/[[ELIZAOS]] [[expectation-gap]] cap). This was a *tight* entry on a *volatile* name that simply moved.

The sniper had sized this position at its full [[quiet-size]] — the largest size that keeps footprint under the cap. That is optimal for a stable book. It is exactly wrong for a spike name: the whole reason a token is on the sniper's watchlist is that it makes large, fast moves, which is another way of saying its five-minute reversal variance is high. **We were putting on our biggest position precisely where the hold carried the most tail risk.**

## The class of mistake

Quiet-size answers "how much can I trade without moving the book?" It does *not* answer "how much *should* I trade given how violently this name reverses?" On the sniper's population — selected for volatility — those two questions have very different answers. The generalised rule: **on a strategy whose candidate-selection is conditioned on volatility, position size must be discounted against reversal variance, not just against footprint.** A haircut on the quiet size is the crude-but-honest version of that discount until we have enough settled tails to fit something better.

## The change

`NW_BIGSPIKE_SIZE_FACTOR = 0.5`: after the quiet-size search, halve the chosen size. It respects existing floor handling — if the halved size falls below `SIZE_MIN_USD`, the candidate is skipped with a logged reason rather than entered sub-minimum, and the halved size is re-run through the feasibility clear (a fixed withdrawal fee is a larger fraction of a smaller size, so a halved position can stop clearing the net gate; if so, we skip honestly rather than book a trade that no longer clears our own bar).

The evidence base is thin — **n = 4** sniper tails — which is *why* the factor is a blunt 0.5 and not a tuned number. This is a risk-reduction placeholder, explicitly provisional, to be replaced once enough sniper settlements accumulate to estimate reversal variance per volatility bucket.

## Review

By 2026-07-23: with more sniper settlements, is the realized-tail distribution actually ~halved, and did the reduced size cost more in forgone winner upside than it saved in tail losses? If winners dominate, raise the factor toward 0.7; if tails still dominate, the problem is entry selection, not size, and this lesson points to a watchlist-quality lesson next.

_Related: [[FOXY]] · [[quiet-size]] · [[five-min-settlement]] · [[expectation-gap]] · [[ROAM]] · [[ELIZAOS]] · [[Thusus]]_
