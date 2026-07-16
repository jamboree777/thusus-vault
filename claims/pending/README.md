---
title: Contribution guide — pending claims
type: doc
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Pending claims — how to contribute

This folder holds **community-submitted claims that have not yet been verified.** Nothing here is rendered as fact anywhere in the vault, the live wiki, or the API until it clears verification. That is the anti-poisoning design: **claims can never write directly to the fact layer.**

## How to submit

1. Copy [[claims/TEMPLATE]] into this folder and rename it descriptively (e.g. `2026-07-16-btr-bitget-deposit-reopened.md`).
2. Fill in the frontmatter. **`source_url` is mandatory** — a claim with no reachable source is auto-rejected before any human or AI looks at it.
3. Set `observed_at` (when the change happened, UTC) and `contributor` (`@handle`).
4. Open a pull request into this folder, or use the in-app submission form.

## The verification pipeline

```
claim → deterministic gate  (source reachable? schema valid? contradicts the DB?)
      → AI review           (does the source actually say this?)
      → measurement probe    (where possible: we hit the exchange API and KNOW)
      → merge with provenance tag  [verified] / [community-reported]
```

Most claims here are **machine-checkable**, which is NightWatch's unfair advantage: a claim like "deposits reopened" is not taken on trust — we query the exchange's own API and confirm it. Verified claims merge as prose with a `[verified]` tag and may trigger a database-side verification task. Claims we cannot machine-confirm but which have a credible source merge in a visually distinct block tagged `[community-reported]`, excluded from frontmatter facts and from Pro API fields.

## Provenance grading (the hard rule)

Every factual line in this vault is graded. Plain prose is for things verifiable in NightWatch's own data or docs. Anything from the press or an unconfirmed source carries an explicit inline tag — `[media-reported, unverified]` or `[community-reported]` — and never enters the fact frontmatter. See the [[2026-03-24-btr-crash]] note for the canonical worked example of `[verified]` versus `[media-reported, unverified]` grading.

## What you earn

- **Cherry** per verified claim, bounty-priced by the gap's value.
- **Reputation with a URL** — a verified contributor gets an `entities/contributors/@handle` page, a citable node backlinked from every note they improved.
- **Earned access** — verified contributors can unlock deeper (Ring-1) fields instead of paying.

Contributor pages are created automatically on your first verified claim.
