# Draft — Obsidian Forum, "Share & showcase"

> Maintainer note (not for posting): DRAFT for the official Obsidian forum (Share & showcase category). Longer + more architectural than the Reddit post. Robin decides if/when it posts. Attach the three screenshots named at the bottom.

## Title

A live-updating market-intelligence vault: a sync bot and humans co-write the same notes

## Body

I want to share a vault that pushes on an idea I haven't seen done publicly: **a vault that a bot keeps current every night, while humans and an AI keep writing prose into the same files — without either side overwriting the other.**

### The architecture: DB = measurements, vault = meaning

Behind this is a normal database that stores *measurements* — exchange grades, deposit/withdrawal states, contract addresses, simulated trades. That layer is canonical for numbers and it's always fresh.

The **vault is canonical for meaning** — the prose layer that explains the measurements. Two things share each token note:

- a **machine region**, wrapped in `<!-- nw:auto:begin --> … <!-- nw:auto:end -->`, that a nightly sync bot rewrites from the live data (frontmatter facts + a generated summary), and
- a **prose region** below it that only humans / the AI author ever touch.

The sync bot edits *only inside the markers*. Everything else is durable. This is what makes it a living dataset instead of either a stale dump or a fragile scrape. `tokens/BLAST.md` is the cleanest example — scroll past the `nw:auto` block and there's hand-written prose explaining why BLAST is the vault's demonstration that "grade" and "transfer feasibility" are different dimensions.

Frontmatter is a **published contract** (`concepts/frontmatter-spec.md`): stable, typed keys, so Dataview and Bases queries work on a fresh clone and any third-party tool can parse the files without scraping.

### The contribution loop

Outside contributors write via pull request:

1. **PR** — drop a claim note into `claims/pending/` with a mandatory `source_url` (no source → auto-rejected).
2. **Validation Action** — `.github/workflows/validate-claims.yml` runs `.github/scripts/validate_claims.py`, which schema-checks the frontmatter (claim type in whitelist, ISO timestamp, http(s) source) and posts a pass/fail summary on the PR.
3. **Verified** — a review confirms the source actually says it; where the claim is machine-checkable, we probe the exchange API and *know*. Only then does it merge as prose tagged `[verified]` vs `[community-reported]`, and only verified facts enter frontmatter.
4. **Contributor page** — a first verified claim auto-creates a contributor node under `entities/contributors/`, back-linked from every note it improved: portable, citable reputation (plus a Cherry reward — our first verified contributor was paid 10 Cherry).

Unverified claims never render as fact. The anti-poisoning stance is: provenance mandatory, no direct fact writes, machine confirmation preferred.

### Concrete files to look at (and good screenshots)

- **`tokens/BLAST.md`** — the machine-region / prose-region split in one file (screenshot the boundary).
- **`claims/pending/2026-07-16-blast-upbit-deposit-resumed.md`** — a real, source-cited claim in the pending queue.
- **`.github/scripts/validate_claims.py`** + **`.github/workflows/validate-claims.yml`** — the PR schema gate that makes the contribution loop trustworthy.

(Bonus for the graph-view screenshot: `concepts/mirage-arb.md` and `concepts/one-price.md` are hubs that most token/event notes link into.)

### Honesty + license

The trading journal (`journal/`) is a **paper / dry-run book** — simulated fills against real quotes, labelled PAPER everywhere; not a track record, not advice. Prose is **CC BY-NC-SA 4.0**, attribution "NightWatch / Thusus".

Repo: https://github.com/jamboree777/thusus-vault — grown from a 49-file seed to ~100 notes, updated nightly.

Happy to answer questions about the marker-region sync pattern; it's the reusable part.
