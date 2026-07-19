---
type: lesson
date: 2026-07-18
trigger: "Robin directive: '최초 펀드가 작을수록 수익률이 높아지기 때문에 R1을 잘 만들어 줘야해' — smaller initial fund = higher ROI; R1 (bithumb-origin USDT conservation) is the only lever. The two-book KOREA book carried bithumb $10,000 with a live capital_short of $1,868.78 because the R1 conservation ledger in nw_qm_transfers stopped at the 07-18 backfill while trades kept draining bithumb, and the QM ran on a ~60min (hourly timer) cadence so returns lagged."
problem: "KOREA required capital was oversized and still short. (a) Cadence: the QM executor effectively ran hourly, so R1 returns landed up to ~60min after bithumb-origin USDT accrued — bithumb was sized for the full lag. (b) Truncated ledger: the static back-solve required extra bithumb capital to bridge the gap the truncated R1 ledger left, yet still went short as live trades grew. (c) Back-solve artifact: R1 returns were distributed proportional to seeded balance, so in the zero-start book back-solve a venue could 'send' more than it received (binance showed a $3,976 phantom deficit), and historical pre-emptive/immediate global->bithumb top-ups were double-counted (R1 returned USDT those moves had already conserved)."
change: "R1 is now KOREA-book aware and cadence-aware. tools/nw_realloc_backtest.py --r1-sweep grids trigger($250/$500/$1000) x cadence(15/30/60m) on the korea trade subset with a forward-interleaved R1 ledger. Three corrections make the zero-start book back-solve honest: (1) each global venue returns EXACTLY its own accumulated bithumb-origin USDT (accum[venue]); (2) returns fire only at UTC-aligned cadence checkpoints (QM runs once per NW_QM_EXEC_MIN); (3) a historical pre-emptive/immediate global->bithumb move CONSUMES the source accumulator so R1 does not double-return it. Chosen config: NW_QM_R1_TRIGGER_USD=500 + NW_QM_EXEC_MIN=30 (timer *:10/30). Applied: korea nw_fund_initial_alloc rewritten to $15,000 (book='korea' only, global untouched), 57-row forward R1 conservation ledger written (book='korea', 'r1-sim backfill', net-zero, fee $9.30). QM MODE 1 R1 batching made EXEMPT from the daily transfer cap (net-zero conservation; pre-emptive/immediate stay capped; single-move MAX_TRANSFER_USD rail retained). Prior korea alloc rows and R1 backfill rows backed up to audit_logs before delete."
expected_effect: "KOREA required capital $19,000 -> $15,000, bithumb $10,000 -> $6,000, capital_short $1,868.78 -> $0, invariant_ok true; GLOBAL book untouched ($10,000). Fee drag $9.30 = 3.2% of korea realized (<< 10%). Cadence is the dominant lever (60m bithumb $9k, 30m $6k, 15m $5k); trigger barely moves capital. The residual ~$8k offshore korea capital is the seed that pre-emptive/immediate top-ups fronted before accrual — it compresses as forward R1 runs; netting those historical moves out (not done — avoids rewriting executor history) would reach a theoretical ~$11k floor."
review_after: 2026-07-25
status: active
supersedes: "[[2026-07-18-two-book-fund-split]]"
---

# R1 optimization: KOREA required capital is a cadence problem, not a trigger problem

Robin's lever for ROI is the initial fund size, and R1 — returning bithumb-origin
USDT home — is the only knob that moves the KOREA book. The book sat at bithumb
$10,000 and was still $1,868.78 short.

## The class of mistake

**Latency-sized capital.** The QM executor batched at most once per hour, so every
bithumb-origin dollar sat at a global venue for up to an hour before R1 shipped it
home. bithumb had to be pre-funded for that entire lag. The fix is not a bigger
buffer — it is a **shorter cadence**. The sweep shows bithumb $9k @ 60m, $6k @ 30m,
$5k @ 15m; the $500-vs-$1000 trigger choice barely matters.

## The back-solve trap (honesty)

Three artifacts inflated the offshore korea venues in a zero-start book back-solve:
balance-proportional returns (a venue "sends" USDT it never received → phantom
deficit), instantaneous returns (ignores the real refill delay), and double-counting
the historical pre-emptive/immediate top-ups (which already returned bithumb-origin
USDT). Correcting all three: each venue returns its own accum, at cadence ticks, net
of what the real top-ups already conserved.

## Chosen config + result

`NW_QM_R1_TRIGGER_USD=500`, `NW_QM_EXEC_MIN=30` (timer `*:10/30`). KOREA
$19,000 → **$15,000**, bithumb $10,000 → **$6,000**, capital_short → **$0**, fee
drag 3.2%. 15m cadence is a documented −$1k lever (bithumb $5k) if Robin accepts the
tighter jitter buffer. The theoretical ~$11k floor requires netting out the
historical pre-emptive/immediate moves — deferred (would rewrite executor history).

_Related: [[2026-07-18-two-book-fund-split]] · [[2026-07-18-woncarry-korea-usdt-capital-model]] · [[THUSUS_OPS_LOOP]] · [[FUND_SETUP_AND_QM]]_
