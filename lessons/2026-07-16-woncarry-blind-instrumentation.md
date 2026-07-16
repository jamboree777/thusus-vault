---
type: lesson
date: 2026-07-16
trigger: "nw_woncarry_shadow — 0 rows across ~2156 passes; heartbeat shows opp_count 40, recheck_wait 37, entered 0 every pass"
problem: "An engine that evaluates candidates every pass but persists nothing when they all reject is unauditable — the fund cannot tell a correctly-empty strategy from a silently-broken gate."
change: "NW_WC_CAND_LOG_SEC: (new) → 300 — added table nw_woncarry_candidates; top-10 candidates by |edge| persisted per throttled pass with the gate's own executable numbers + reject reason"
expected_effect: "Within ~10–15 min the table holds rows; exec_net_pct should be NEGATIVE for the headline candidates, proving the executable gate is correctly refusing sub-cost basis, not malfunctioning."
review_after: 2026-07-23
status: active
supersedes: null
---

# Won-carry was blind: an all-reject engine that wrote nothing

The [[won-carry]] shadow engine has never written a single row. Not zero *because it never ran* — it runs every 30 seconds, and its heartbeat is healthy: forty live opportunities pulled per pass, thirty-seven of them cycling through the probe-reject cache, and **zero entries, forever**. On day one the [[journal/2026-07-15|journal]] already recorded this as the day's real lesson: every KRW-vs-global candidate inside ±1.8% headline premium failed the [[executable-spread]] gate once [[stablecoin-basis]] and both-sides slippage were netted.

That is almost certainly *correct* behaviour. The [[kimchi-premium]] you see on the screen is an advertisement the executable book will not honour. But "almost certainly correct" is not good enough for a fund that claims to show its homework. **A strategy that rejects everything and records nothing is indistinguishable from a strategy whose gate has quietly broken.** We were flying blind on our own discipline.

## The class of mistake

This is not a won-carry bug. It is a general observability gap: **any gate that only writes on success makes its rejections unfalsifiable.** The livescan and sniper engines already emit `nw_verify_events` on reject; won-carry had no equivalent, so its refusals left no trace. The fix has to persist the *reason* and the *executable economics at the moment of refusal*, using the same numbers the gate computed — never a recomputation that could disagree with the gate.

## The change

A new idempotent table, `nw_woncarry_candidates`, captures — once per throttled pass (`NW_WC_CAND_LOG_SEC`, default 300 s) — the top ten candidates by absolute edge: base, mode, both venues, the entry relative edge, the **executable net at the best [[quiet-size]]** (`exec_net_pct`), the size at that point, and a `reject_reason` (`cooldown`, `route_closed_*`, `thin_book`, `net_fail`, `bridge_net_fail`, `net_usd_floor`, `entered`, …). Rows older than 30 days are pruned in the same pass. The whole path is wrapped fail-safe: a logging failure can never touch the engine.

The point is the `net_fail` rows. When the grid walk finds no size that clears `min_net_eff`, we still record the *best* executable net among quiet sizes — expected to be negative. That negative number is the proof: the basis was real on the screen and unprofitable in the book, exactly as the [[expectation-gap]] predicts, and now it is written down where anyone can check it.

## Review

By 2026-07-23: does the table have rows, are the `net_fail` exec nets negative, and do the reject reasons cluster where the analysis says they should ([[executable-spread]] failures, not route closures)? If the exec nets come back *positive* and we are still entering nothing, the gate — not the market — is the problem, and this instrumentation will have earned its keep on the first week.

_Related: [[won-carry]] · [[executable-spread]] · [[quiet-size]] · [[expectation-gap]] · [[kimchi-premium]] · [[stablecoin-basis]] · [[five-min-settlement]] · [[Thusus]]_
