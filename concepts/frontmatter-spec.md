---
concept: frontmatter-spec
type: concept
aliases: [frontmatter contract, frontmatter keys, note schema]
related: [nw-grade, transfer-feasibility, identity-verification]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# Frontmatter Spec — the published contract

Every note in this vault opens with a YAML frontmatter block. Those keys are a **published contract**, not decoration: stable, typed, documented here, so that Obsidian Dataview / Bases queries work on a cloned vault and third-party AIs can parse the file tier without scraping. **The frontmatter spec is the API for the file tier.**

The token-note keys mirror the live wiki (`GET https://nightwatch-v1-api.onrender.com/kg/{TOKEN}.md`) exactly, so a note and its live page are the same shape.

## Auto-region markers

Machine-written content is fenced by HTML comments:

```markdown
<!-- nw:auto:begin -->
Everything here is rewritten by the nightly sync bot from the live database.
Do not hand-edit inside the markers — your edits will be overwritten.
<!-- nw:auto:end -->
```

Prose **outside** the markers is durable and survives every sync. Frontmatter itself, on token and journal notes, lives inside the auto region (it mirrors live fields). On concept / venue / chain / event notes the frontmatter is human/AI-authored and is not auto-synced.

## Key sets per note type

### `token` (mirrors the live wiki)

| Key | Type | Meaning |
|---|---|---|
| `token` | string | Base symbol, uppercase (e.g. `BLAST`) |
| `type` | `token` | Node type |
| `tier` | `free` \| `pro` | Disclosure ring of the fields shown |
| `nw_grade` | `A`–`F` | [[nw-grade]] — best liquidity grade across venues |
| `nw_grade_worst` | `A`–`F` | Worst grade across venues (risk context) |
| `identity` | `verified_same` \| `unverified` \| `collision` | [[identity-verification]] result |
| `contracts` | list of `{ chain, address }` | Verified on-chain contracts |
| `exchanges` | list | Venues that list the token |
| `korean_exchanges` | list | KRW venues (subset of `exchanges`) |
| `transfer` | `open` \| `partial` \| `blocked` | [[transfer-feasibility]] summary |
| `updated` | ISO-8601 | Last sync timestamp |
| `source` | `nightwatch-kg` | Provenance |

Example:

```yaml
token: BLAST
type: token
tier: free
nw_grade: A
nw_grade_worst: A
identity: verified_same
contracts:
  - { chain: blast, address: "0xb1a5700fa2358173fe465e6ea4ff52e36e88e2ad" }
exchanges: [bitget, bithumb, bybit, coinbase, gateio, kucoin, mexc, upbit]
korean_exchanges: [bithumb, upbit]
transfer: open
updated: 2026-07-16T00:30:58Z
source: nightwatch-kg
```

### `venue`

| Key | Type | Meaning |
|---|---|---|
| `venue` | string | Exchange id (lowercase) |
| `type` | `venue` | Node type |
| `kind` | `cex` | Exchange kind |
| `fiat` | list | Fiat/settlement currencies (e.g. `[USDT]`, `[KRW]`) |
| `taker_fee` | number | Spot taker %, from `/arb/fees` |
| `maker_fee` | number \| null | Spot maker % if known |
| `premium_lean` | `cheap` \| `rich` \| `neutral` | Habitual side, from `/arb/exchange_premium` |
| `bias_pct` | number | Signed premium bias % (negative = cheap) |
| `geo` | string | IP/geo constraints relevant to trading |

### `chain`

| Key | Type | Meaning |
|---|---|---|
| `chain` | string | Chain id |
| `type` | `chain` | Node type |
| `layer` | `L1` \| `L2` | Layer classification |
| `role` | string | Role in transfer routes |

### `event`

| Key | Type | Meaning |
|---|---|---|
| `title` | string | Event title |
| `type` | `event` | Node type |
| `date` | ISO date | When it happened |
| `tokens` | list | `[[wikilink]]` targets involved |
| `venues` | list | Venues involved |
| `status` | `resolved` \| `monitoring` \| `ongoing` | Current state |
| `verification` | `verified` \| `mixed` \| `media-reported` | Highest provenance grade in the note |

### `concept`

| Key | Type | Meaning |
|---|---|---|
| `concept` | string | Slug of the term |
| `type` | `concept` | Node type |
| `aliases` | list | Synonyms for search / linking |
| `related` | list | Sibling concepts |

### `journal`

| Key | Type | Meaning |
|---|---|---|
| `date` | ISO date | Trading day |
| `type` | `journal` | Node type |
| `author` | `thusus` | Always Thusus |
| `fund_epoch` | ISO datetime | Current fund reset epoch |
| `mode` | `paper` | Always paper in Phase 0 |
| `tags` | list | e.g. `[paper, dry-run]` |

### `claim`

See [[claims/TEMPLATE]]. Keys: `claim_type`, `token`, `source_url` (**mandatory**), `observed_at`, `contributor`, `status`, `type: claim`.

### `contributor`

| Key | Type | Meaning |
|---|---|---|
| `handle` | string | `@handle` |
| `type` | `contributor` | Node type |
| `joined` | ISO date | First verified claim date |
| `verified_claims` | number | Count of merged, verified claims |

## Shared conventions

- **`updated`** and **`author`** appear on every hand/AI-authored note. `author: thusus` marks AI-written notes; `author: "@handle"` marks contributor-written ones. The vault is transparently a human + AI corpus.
- Wikilinks (`[[target]]`) are used everywhere; every link resolves to a real note.
- Provenance grading in prose: plain text for anything verifiable in NightWatch data, and an explicit `[media-reported, unverified]` / `[community-reported]` tag for anything that is not. See [[claims/pending/README]].
