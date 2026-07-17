---
type: lesson
date: 2026-07-18
trigger: "Robin flagged (2026-07-18): the won-carry engine booked trades — especially bithumb — WITHOUT resolving or recording WHICH transfer chain the token moves on. A chainless trade cannot be executed: unknown route, unknown withdrawal fee, unknown per-chain deposit/withdraw status. Meanwhile the data had arrived — the auth-wallet collector now writes 512 real per-network rows for bithumb (ethereum, solana, base, bsc, arbitrum, kaia, tron, ...) into nw_exchange_contracts — but the engine never picked a specific chain per trade nor stored one (SELECT route_chain errored; the column did not exist)."
problem: "Chainless bookings. The engine priced an edge and booked a round-turn without committing to a specific, open, shared transfer chain — so a booked trade was not actually executable and its withdrawal fee was a size-fraction estimate, not a real per-chain fee."
change: "Resolve a SPECIFIC transfer chain per trade at entry by intersecting the buy-venue's OPEN (wd_enabled) chains with the sell-venue's OPEN (dep_enabled) chains for that base, canonicalized with the same _canon_chain the roundturn resolver uses, and picking the cheapest open shared chain — REUSING the existing _open_shared_chains / _token_wd_fee_pct resolver (svc/worker/nw_woncarry_shadow.py:1405 / :1541); the resolved chain also drives the real per-chain wd-fee. If no open shared chain resolves → REJECT (log 'no_resolvable_chain'), no booking (both the main entry loop and the forced-exit path). Record the chain: idempotent route_chain TEXT column on nw_woncarry_shadow, populated on every entry + stamped into assumptions.route_chain. Prefer real per-chain rows over the coexisting 'coin' sentinel: drop the coin sentinel from a venue's set when it also has real chains (bithumb writes both 500 coin sentinels + 512 real rows), so real chains win and a fake coin<->coin match can never book. Display: /thusus shows 'via {chain}' on the woncarry trade row and in the expanded TimelineStrip; null route_chain (old rows) shows nothing. API: /arb/thusus/book passes route_chain through (column-guarded)."
expected_effect: "No more chainless woncarry bookings — every new entry carries a concrete open shared transfer chain (recorded + displayed). Some bithumb trades correctly drop as 'no_resolvable_chain' until their chains line up on both venues (honest). Withdrawal fees are priced on the actual resolved chain, tightening the fee model. Robin can SEE the chain each trade uses in the trade log."
review_after: 2026-07-25
status: active
supersedes: null
---

# Won-carry resolves, records and shows the transfer chain per trade

[[won-carry]] had a physical-execution hole: it booked a round-turn without ever committing to **which chain the token crosses on**. The edge math was fine, but a booked trade with no chain is not executable — you cannot know the route, the withdrawal fee, or whether deposits/withdrawals are even open on the leg that matters. This was most visible on **bithumb**, whose per-network deposit/withdraw data had only recently landed: the auth-wallet collector now writes **512 real per-network rows** for bithumb into `nw_exchange_contracts` (ethereum, solana, base, bsc, arbitrum, kaia, tron, ...). The engine simply never used them to pick a chain, and had nowhere to store one — `nw_woncarry_shadow` had no `route_chain` column.

## The class of mistake

**Booking a physical operation without resolving its physical route.** An arbitrage engine can compute a correct *edge* and still book an *unexecutable* trade if it doesn't bind the trade to a concrete transfer path (chain + open dep/wd + real fee). The fix is not token-specific — it is a per-trade route-resolution gate that applies to every won-carry entry on every venue pair.

## The fix — reuse the roundturn resolver, reject when no chain

The roundturn feasibility resolver (`stats.py` `_arb_transfer_feasibility` / `_chain_routes`) already knew how to intersect a Korean venue's chains with a global venue's chains. The won-carry worker already had the matching primitive — `_open_shared_chains` (nw_woncarry_shadow.py:1405) — which returns the OPEN shared chains (wd_enabled on the sender, dep_enabled on the receiver), canonicalized via the same `_canon_chain`, cheapest wd_fee first, BTC-mainnet excluded. `_token_wd_fee_pct` (:1541) already returned the chosen chain and priced the real per-chain fee. The gap was purely that the chosen chain was **thrown away**, and an empty resolution still booked.

So: at entry, take the resolver's chosen chain. If it is empty (no open shared chain, or the route could not be priced) → **reject and log `no_resolvable_chain`**; never book. Otherwise record it in the new **`route_chain`** column and stamp `assumptions.route_chain`, and use that chain for the real withdrawal fee. Same guard added to the forced-exit path.

Verified live on Chuncheon against the real feed + DB: BTT/NFT → **tron**, DEXE/SXT/SPACE → **ethereum**, 0G → **0g**, HOLO → **solana** — all 40 live candidates resolved a real chain (not the `coin` sentinel). The reject path fired honestly too: `BTC bithumb→binance` and `A bithumb→binance` returned `route_closed`/empty (no open shared chain), and a real pass logged `[enter] ARX no_resolvable_chain (kucoin→upbit) — not booking`.

## Prefer real chains over the `coin` sentinel

Bithumb's public assetsstatus gives a coin-wide flag, so the collector writes a `coin` sentinel row **in addition to** the 512 real per-network rows — they coexist per currency. The resolver now drops the `coin` sentinel from any venue's set when that venue also has real chains, so the real per-chain dep/wd/wd_fee data is used and a fake `coin↔coin` match can never produce a chainless booking. A currency whose *only* row is `coin` still expands onto the counterparty's real chains (unchanged).

## What Robin sees

The `/thusus` trade log now shows **"via tron" / "via bsc"** on the woncarry trade row (Route column) and in the expanded TimelineStrip detail. Old rows (route_chain NULL) show nothing — never fabricated. `/arb/thusus/book` carries `route_chain` on every woncarry trade (column-guarded, null on pre-2026-07-18 rows).

_Related: [[won-carry]] · [[2026-07-18-woncarry-korea-usdt-capital-model]] · [[2026-07-17-woncarry-exit-policy-v2]] · [[2026-07-18-per-chain-settle-delay]] · [[executable-spread]] · [[THUSUS_OPS_LOOP]] · [[Thusus]]_
