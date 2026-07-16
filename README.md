# Thusus Vault

**A live-updating, cross-exchange token-intelligence vault — written by [[Thusus]], NightWatch's market-intelligence AI trader, and verified contributors.**

Every crypto data site sells *numbers*. Almost nobody owns the *explanations* — why a price gap exists, why a token's deposits froze, what actually happened to [[BTR]] on [[2026-03-24-btr-crash|24 March 2026]], which venue habitually trades on the cheap side. That prose layer — the *meaning* on top of the measurements — is what this vault is.

One sentence: **the NightWatch database stays canonical for measurements; this vault is canonical for meaning.**

## What lives here

| Folder | Node type |
|---|---|
| `tokens/` | Per-token dossiers (identity, contracts, exchange list, grade, transfer status) |
| `venues/` | Exchange notes: fee tables, deposit/withdrawal traits, habitual premium bias |
| `chains/` | Chain notes: role in transfer routes, withdrawal cost/latency |
| `events/` | Incident timelines (crashes, wallet lockdowns, fund resets), every line graded |
| `concepts/` | NightWatch's working vocabulary — One Price, NW Grade, MIRAGE arb, quiet size |
| `journal/` | [[Thusus]]'s daily paper-trading book — real numbers, honestly labelled PAPER |
| `entities/contributors/` | Contributor pages, auto-created on first verified claim |
| `claims/pending/` | Community-submitted claims, **never rendered as fact** until verified |
| `MOC/` | Maps of Content — hand-curated entry points into the graph |

## How to open in Obsidian

1. `git clone` this repository.
2. In Obsidian, **Open folder as vault** → select the cloned directory.
3. Open **Graph view** — you'll see tokens ↔ venues ↔ concepts ↔ journal linked by `[[wikilinks]]`.
4. Frontmatter follows a published contract ([[frontmatter-spec]]), so Dataview / Bases queries work on your clone.

## How the auto-sync works

Token notes and journal notes are partly machine-written. Each carries a marked **auto-generated region**:

```markdown
<!-- nw:auto:begin -->
...frontmatter facts + live fields, rewritten by the sync bot...
<!-- nw:auto:end -->
```

A nightly bot on NightWatch's Chuncheon worker only ever rewrites content *inside* those markers, mirroring the live wiki. **Prose you or Thusus write outside the markers survives forever.** The sync never touches human/AI prose, and community claims never write to the fact layer.

The same data is served live, always fresh, from the API:

- Live wiki page for any token: `GET https://nightwatch-v1-api.onrender.com/kg/{TOKEN}.md` (e.g. [`/kg/BLAST.md`](https://nightwatch-v1-api.onrender.com/kg/BLAST.md))
- Frontend: <https://nightwatch-v1-frontend.onrender.com>

A cloned vault goes stale within a day; the live feed does not. Copying the vault is *distribution*, not loss — every note links back to the source.

## Clip into your own vault

Two [Obsidian Web Clipper](https://obsidian.md/help/web-clipper) templates live in [`clipper/`](clipper/) — importable `.json` in the extension's own format:

- **NightWatch Token** — one-click clip of any token page (`/token/*` or the live `/kg/*` wiki) into your own `tokens/` folder, with our frontmatter and a `[[Thusus]] · live:` link back to the fresh source.
- **NightWatch Claim** — turn any exchange notice or news page into a ready-to-submit claim in `claims/pending/`, with the `source_url` captured automatically.

Import steps and the schema reference are in [`clipper/README.md`](clipper/README.md).

## Contribution quickstart

1. Copy [[claims/TEMPLATE|the claim template]] into `claims/pending/`.
2. Fill in `claim_type`, `token`, `observed_at`, `contributor`, and — **mandatory** — a `source_url`. A claim with no source is auto-rejected.
3. Open a pull request (or use the in-app submission form).

Your claim lands in `claims/pending/` and is **never rendered as fact**. It passes a deterministic gate (source reachable? schema valid? contradicts the database?), then AI review (does the source actually say this?), then, where possible, a machine probe (we hit the exchange API and *know*). Only then does it merge as prose with a `[verified]` / `[community-reported]` tag. See [[claims/pending/README|the contribution guide]].

## Honest disclaimer

[[Thusus]] runs a **paper / dry-run** trading book. No real capital is deployed. Fills are simulated against real order-book quotes with a 5-minute settlement model ([[five-min-settlement]]); reported P&L is the engine's accounting, not a promise and not a track record of realized money. Nothing in this vault is financial advice. It is informational cross-exchange market intelligence. Do your own research; markets move; deposits freeze without notice.

## Share it

Community showcase drafts (Reddit / Obsidian forum / X) live in [`showcase/`](showcase/) — **maintainer notes only**, unpublished, kept in-repo for the vault's stewards to adapt and post at their discretion.

## License

Prose in this vault is [[LICENSE|CC BY-NC-SA 4.0]], attribution "NightWatch / Thusus". Factual data (contracts, fees, grades) is not subject to copyright; the prose compilation is. Commercial licensing available separately.
