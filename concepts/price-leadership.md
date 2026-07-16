---
type: concept
name: price-leadership
aliases: [anchor venue, liquidity leadership, deviant reversion]
updated: 2026-07-16
author: thusus
source: robin-directive-2026-07-16
---

# Price Leadership — the anchor venue sets the price, deviants revert

Price discovery happens where liquidity is deep. The high-liquidity venue (the **anchor**)
determines the market price; a low-liquidity venue's price is largely an echo. When a small
venue's price deviates — a sudden volume burst, a local dump or spike — it is unlikely to move
the anchor. The anchor barely moves on small size, and the small venue soon **follows the
anchor back**.

Two structurally different cross-exchange trades follow from this:

- **Buy the deviant dip, sell at the anchor** — the small venue is quoting below the leader.
  The anchor's price is stable during a transfer window; the gap closes by the *deviant
  reverting upward*. Favorable class for a [[five-min-settlement]] model.
- **Sell into the deviant spike** — the small venue is quoting above the leader, and we sell
  into it after a transfer. The spike tends to collapse back toward the anchor *before*
  settlement. Unfavorable class: the edge you saw at entry is the very thing that mean-reverts
  against you. The Thusus book's worst early tails (FOXY −$14.93, settle price −8.4% in five
  minutes) belong to this class.

## How Thusus operationalizes it

Every trade's entry fingerprint records `anchor_leg` (which side held dominant depth) and
`deviation_pattern` (`buy_deviant_dip` / `sell_into_deviant_spike` / `balanced`). The
attribution ledger slices realized outcomes by this dimension; if the hypothesis holds in our
own data, `sell_into_deviant_spike` above a spread threshold becomes an entry guard — a
recorded lesson, not a hunch. See [[expectation-gap]], [[quiet-size]], [[nw-grade]].

Status: hypothesis under measurement (fingerprint coverage began 2026-07-16). This note will
be updated with the measured verdict — including if it turns out wrong.

_Paper/dry-run context; informational only._
