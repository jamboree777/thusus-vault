---
type: lesson
date: 2026-07-17
trigger: "Robin's directive (2026-07-17): won-carry accumulates KRW but never deliberately exits it. Parked KRW carries FX risk and misses global opportunities; the naive exit (repurchase USDT) pays the full stablecoin premium. Exit instead through the most undervalued token on the Korean venue whenever its edge covers costs."
problem: "KRW capital lock + USDT-premium exit cost class — the engine had in-legs (premium buys that accrue KRW) but no formalized out-leg. Capital that flowed into Korea to capture the basis had no disciplined way back out; repurchasing USDT to exit re-pays the stablecoin basis + fees, and idle KRW is unhedged FX exposure the accounting could not separate from carry P&L."
change: "Exit-policy v2 params: NW_WC_EXIT_EDGE_MIN_PCT=0.0 (KRW-funded discount out-legs execute when executable exit_edge ≥ this — the token need NOT be discounted, only relative-premium-below-basis; MIN_NET_PCT/MIN_NET_USD floors waived for exits); NW_WC_KRW_POOL_CAP_PCT=30 (premium in-legs blocked once KRW share of the fund exceeds this); NW_WC_MAX_DWELL_H=72 (KRW parked longer force-exits via the lowest-relative-premium liquid major NW_WC_FORCED_EXIT_MAJORS=BTC,ETH,XRP,SOL, even at negative edge, logged as forced_exit with cost paid); fx_pnl marks the KRW pool at current usdt_krw each pass so carry_pnl vs FX exposure are separable in the accounting output."
expected_effect: "Out-legs execute only when covered (exit_edge ≥ 0 ⇒ at least as cheap as repurchasing USDT); in-legs stop over-parking KRW above 30%; forced exits are bounded to the dwell window and to liquid majors; fx_pnl is separated from carry_pnl in every pass summary so FX drift never masquerades as carry alpha."
review_after: 2026-07-24
status: active
supersedes: null
---

# Won-carry must come out: exit through the cheapest token, not through USDT

[[won-carry]] had a front door and no back door. Premium in-legs buy a token abroad, transfer it, and sell it dear in Korea — the proceeds land as KRW and the [[won-carry|KRW pool]] grows. That is the *carry going in*. But capital that walks into Korea to harvest the [[stablecoin-basis]] has to walk back out eventually, and the engine never formalized that walk. Left alone, KRW just sits: an unhedged FX position that also can't chase a better opportunity anywhere else on earth.

The naive exit is to buy USDT back and withdraw it. But USDT in Korea trades at the very premium you came to capture — **repurchasing USDT to leave pays the basis a second time**, plus two sets of fees. Robin's insight, formalized here: don't leave through USDT. Leave through a *token*. Buy the most undervalued liquid token on the Korean venue, transfer it, sell it abroad for USDT. If that token's relative premium sits **below** the USDT basis, the token is a cheaper vehicle out of KRW than the stablecoin itself.

## The class of mistake

This is a **round-trip blindness**: an arbitrage engine that models entry economics in full but treats the exit as free or automatic. The cost of *un-parking* capital is a real, priced leg — and when the parking currency trades at a premium, the exit vehicle you pick is itself an arbitrage decision. The fix is to make the out-leg a first-class, gated trade with its own edge definition, not a residual.

## The exit edge

```
exit_edge_pct = stablecoin_basis_pct
                − exit_token_relative_premium_pct
                − exit_costs_pct        (trading both legs + transfer + probed slippage)
```

The key insight is that the exit token **need not be discounted** — it only needs a relative premium *below* the USDT basis. A genuinely discounted token (premium < 0) makes the exit a *second arbitrage* (a double win); a merely-cheaper-than-USDT token still saves the basis. These are exactly the `/arb/kimchi_roundturn` **discount-mode** candidates, because `mode='discount'` is defined as `token_premium < basis`.

Crucially, the engine already prices the KRW buy leg through the USDT/KRW *market* rate (`usdt_krw = official × (1 + basis/100)`), so the stablecoin basis is **credited on that leg**. That means for a KRW-funded discount trade the engine's **executable `net_pct` already equals the exit edge**. The out-leg gate is therefore simply `net_pct ≥ NW_WC_EXIT_EDGE_MIN_PCT` (default **0.0** ⇒ "exit whenever at least as cheap as repurchasing USDT"), with the standalone `MIN_NET_PCT`/`MIN_NET_USD` floors **waived** — a thin or zero-profit exit is still worth taking if it beats leaving through USDT. `bridge_in`-funded discounts (fresh capital, not a KRW drain) keep the standard profit gate; they are second-arbitrages, not exits.

## Pool breathing, not forced round trips

The KRW pool accumulates during wide-premium regimes (in-legs) and drains during narrow/reverse regimes (out-legs). Each leg fires **independently** once its own edge clears threshold — there is no forced per-trade round trip. Three guardrails keep the breathing bounded:

- **`NW_WC_KRW_POOL_CAP_PCT` = 30** — once KRW is more than 30% of the fund, premium in-legs are blocked. Stop pouring capital into Korea when it's already over-concentrated there; out-legs stay open so the pool can drain.
- **`NW_WC_MAX_DWELL_H` = 72** — if KRW has sat undrained past 72h, force an exit through the lowest-relative-premium liquid major (`BTC,ETH,XRP,SOL`), **even at a negative edge**. A bounded, known cost paid to unstick capital beats an unbounded FX hold. It is logged as `forced_exit` with the cost paid, so the concession is always visible.
- **`fx_pnl`** — the KRW pool is marked to market each pass at the current `usdt_krw`, against the USD-weighted rate at which the carry KRW was parked (`settle_usdt_krw`, stamped at each premium settlement). The pass summary now reports `carry_pnl` and `fx_pnl` separately, so a favorable FX drift can never be mistaken for carry alpha, nor an adverse one hidden inside it.

All shadow/paper — no real money moves. Every out-leg and forced exit stamps the active exit-policy params into `assumptions` JSONB (`leg=out`, `exit_edge_pct`, `exit_policy{...}`) so any row is attributable to the exact ruleset that produced it.

## Review

By 2026-07-24: does the shadow table show KRW-funded discount out-legs with `leg=out` and `exit_edge_pct ≥ 0`, and does the KRW pool actually breathe (accumulate under wide premium, drain under narrow) rather than ratchet up? Is `fx_pnl` non-trivial and cleanly separated from `carry_pnl` in the pass summaries? Have any `forced_exit` rows fired, and if so was the cost paid within reason? If out-legs never fire despite a healthy discount feed, the gate — not the market — needs another look.

_Related: [[won-carry]] · [[executable-spread]] · [[stablecoin-basis]] · [[kimchi-premium]] · [[quiet-size]] · [[five-min-settlement]] · [[2026-07-16-woncarry-blind-instrumentation]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
