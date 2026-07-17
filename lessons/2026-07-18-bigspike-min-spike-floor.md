---
type: lesson
date: 2026-07-18
trigger: "bigspike degenerated into a livescan clone — no minimum-spike gate; it entered at the same 0.5% net gate as livescan (imports MIN_NET_PCT) with only a loose MAX spread cap (10%) and no MINIMUM, so it fired on small gaps instead of rare large dislocations."
problem: "Strategy-identity collapse — an engine whose defining purpose (patiently watch, enter ONLY on rare LARGE cross-venue dislocations) was never actually implemented, so it produced the same trades as livescan and added no distinct edge."
change: "New env NW_BIGSPIKE_MIN_NET_PCT=3.0. bigspike's effective net gate is now max(NW_BIGSPIKE_MIN_NET_PCT, MIN_NET_PCT+repeat_haircut, dynamic_threshold) — it enters ONLY when expected NET ≥ 3% (dynamic sizing may raise it further under pressure, never lower it below 3%). Distinct 'below_min_spike' reject outcome + per-pass skipped_min_spike counter (logged in the [sniper pass] line + heartbeat). Everything else unchanged: watchlist source, 10% MAX spread cap, 0.5 size factor, dynamic sizing, per-chain settle, corrected flat-USD wd-fee. Retroactive: TODAY's (UTC-day) bigspike log recomputed at the 3% floor — 5 of 6 removed (entered 1.3–2.65% net, i.e. livescan-clone gaps), 1 survivor ≥3%."
expected_effect: "bigspike becomes genuinely distinct: rare, large, high-conviction entries. Most passes now enter nothing (correct — big spikes are rare); the skipped_min_spike counter makes the selectivity visible. Kept trades are only the ≥3% dislocations."
review_after: 2026-07-25
status: active
supersedes: null
---

# Big-spike must be a SNIPER, not a livescan clone

[[big-spike]] was supposed to be the patient sniper: sit on a watchlist, ignore the constant 0.5% noise livescan harvests, and fire only when a token dislocates *hard* across venues. In practice it imported `MIN_NET_PCT` and gated at the exact same 0.5% net as livescan, guarded only by a deliberately-loose 10% MAX spread cap and no MINIMUM. So it entered the same small gaps livescan did — a **clone with a different name**.

## The class of mistake

This is **strategy-identity collapse**: two engines that are supposed to occupy different points on the edge/frequency curve converge because the distinguishing gate was never coded. The fix is a single, explicit floor that encodes the strategy's identity.

## The floor

```
effective_net_gate = max(NW_BIGSPIKE_MIN_NET_PCT,           # 3.0% — the identity floor
                         MIN_NET_PCT + repeat_haircut,       # per-name haircut
                         dynamic_threshold)                  # density-adaptive raise
```

The floor only ever *raises* the bar (via `max`), so dynamic sizing and repeat-haircut can make bigspike even more selective under pressure but can never drop it below 3%. A sub-3% candidate is rejected with a distinct `below_min_spike` outcome and counted in `skipped_min_spike`, so a glance at any pass line shows how many watchlist names were turned away for not being a real spike.

## Retroactive honesty (today only)

Under Robin's corrected-log rule, TODAY's (current UTC-day) log is re-judged by the *corrected* algorithms — including this new 3% floor — not the rules that were live when each trade booked. bigspike's today rows recomputed at 3%: **5 of 6 removed** (GAIA 1.65%, XPRT 2.22%, VENOM 1.30%, PTB 2.65%, LAB 1.88% — all livescan-clone gaps), one survivor clearing 3%. The kept log now honestly reflects what the sniper *should* have taken.

_Related: [[big-spike]] · [[2026-07-18-uniform-size-band-diversification]] · [[executable-spread]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
