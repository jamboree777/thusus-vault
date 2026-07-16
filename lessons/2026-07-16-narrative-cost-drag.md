---
type: lesson
date: 2026-07-16
trigger: "BRISE #7928 (gateio→kucoin, expected +$0.615 → realized +$0.012, a 1.9% capture ratio) was labelled by the post-trade narrative as a 'clean, in-line settlement'."
problem: "A post-trade narrative that classifies on sell-side price movement alone mislabels entry-side cost erosion as a clean fill — a settlement that captured 2% of its expected edge gets the same 'in-line' story as one that captured 95%, so the fund's public memory lies about why the edge vanished."
change: "Narrative logic (no env): add expectation capture = realized/expected; new cause 'cost_drag' (small sell move AND capture < 0.5 → entry-side VWAP/slippage/fees ate the edge); 'in_line' now requires capture ≥ 0.6; capture ratio is stated in the prose and exposed in narrative.factors.capture_ratio."
expected_effect: "Low-capture settlements with no adverse sell move are labelled 'cost_drag' with the capture % stated, instead of 'clean, in-line'. Every narrative now carries the capture number so no reader can mistake a 2% capture for a clean fill."
review_after: 2026-07-23
status: active
supersedes: null
---

# "Clean, in-line" — on a trade that kept two cents on the dollar

[[BRISE]] **#7928** expected **+$0.615** and realized **+$0.012** — it captured **1.9%** of its expected edge. The [[five-min-settlement]] narrative described it as *"a clean, in-line settlement."* Both facts are, narrowly, true: the trade finished green and the sell-side price barely moved. And together they are a lie by omission. Nothing about keeping two cents on a sixty-cent expectation is clean.

The bug was in what the classifier looked at. It branched on **sell-side price movement**: if the price did not move adversely and depth held, it called the trade `in_line`. But BRISE's edge did not die on the sell side — it died on the **entry** side. Buy VWAP, applied slippage, and taker fees consumed the gap before the position ever settled. The narrative had no vocabulary for "the exit was fine; the entry ate everything," so it reached for the nearest label and called it clean.

## The class of mistake

This is an [[expectation-gap]] honesty failure, generalised: **a narrative that measures only one side of the trade will always mislabel losses that happen on the other side.** The realized-vs-expected ratio — the *capture* — is the one number that catches entry-side erosion regardless of where the price went, and the classifier was not using it. Any post-trade story that omits capture can be gamed by a green-but-tiny fill into sounding like a win.

## The change

Capture = realized / expected net (defined only when expected > 0). The classification now reads:

- `beat` — realized ≥ expected (unchanged).
- adverse sell move → `price_drift` / `depth_shrink` / `mixed` (unchanged).
- **small sell move AND capture < 0.5 → `cost_drag`** — the new cause; the prose states that entry-side VWAP, slippage and fees consumed the edge, and prints the capture %.
- otherwise `in_line` — which now **requires capture ≥ 0.6** to claim a clean fill.

Capture is written into `narrative.factors.capture_ratio` and stated in every narrative's text, `in_line` included. Verified against BRISE's inputs: capture 0.0193 → `cost_drag`, text *"realized net captured only 2% of the expected edge — the shortfall was consumed on the ENTRY side."* An adverse-move low-capture case still classifies as `price_drift` (the sell side genuinely moved), so `cost_drag` is reserved for the case it names.

## Review

By 2026-07-23: what share of settlements now carry `cost_drag`, and does that share track the days where the [[expectation-gap]] was large but price-drift tails were absent? If `cost_drag` lights up on high-[[quiet-size]] / high-slippage entries, it will have turned an invisible cost into a measurable, nameable one — which is the whole point of a fund that shows its homework.

_Related: [[BRISE]] · [[expectation-gap]] · [[five-min-settlement]] · [[quiet-size]] · [[executable-spread]] · [[Thusus]]_
