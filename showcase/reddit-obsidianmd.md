# Draft — r/ObsidianMD post

> Maintainer note (not for posting): this is a DRAFT. Robin decides if/when it goes up. Tone is deliberately low-hype and Obsidian-native. Swap in a graph-view screenshot before posting.

## Suggested titles (pick one)

1. A live-updating market-intelligence vault your AI can actually read
2. I built an Obsidian vault that a bot writes into every night — and it stays readable
3. Show: a public vault where a sync bot and humans co-write the same notes (machine regions + prose regions)

## Body

I've been building something that turned out to be very Obsidian-shaped, and I think this sub is the right room for it.

It's a **public, cloneable Obsidian vault of cross-exchange token intelligence** — not the numbers (every crypto site has those), but the *meaning*: why a price gap exists, why a token's deposits froze, what actually happened during an incident. Plain markdown, typed frontmatter, `[[wikilinks]]`. You `git clone` it, **Open folder as vault**, and the graph view lights up: tokens ↔ exchanges ↔ chains ↔ concepts ↔ a daily journal.

What might be interesting to this community specifically:

- **A bot writes *into* the vault daily** (03:50 UTC) and it stays hand-editable. Each machine-written note has a marked region — `<!-- nw:auto:begin --> … <!-- nw:auto:end -->` — and the sync only ever rewrites *inside* the markers. Prose you or the AI author outside them survives forever. Same idea as Terraform/dbt generated-docs blocks, but for a knowledge vault. So it's a living dataset that never clobbers your writing.
- **Frontmatter is a published contract**, so Dataview/Bases queries work on a fresh clone — grade, transfer status, contracts, exchange list are all typed keys. The frontmatter spec *is* the API for the file tier.
- **Wikilink graph as the real index.** Concepts (our working vocabulary — "One Price", "mirage arb", "quiet size") are their own notes, and every token/event note links to them, so the graph is genuinely navigable rather than a hairball.
- **Human + AI co-authored, labelled as such.** Notes carry an author field (AI trader vs `@contributor`). The daily journal is written "by" the AI and honestly labelled PAPER / simulated — no fake track record.

Contribution is a PR loop: you drop a claim note (with a mandatory `source_url`) into `claims/pending/`, a GitHub Action schema-checks it, and it only becomes rendered "fact" after review — unverified claims never touch the frontmatter facts.

**Licensing / honesty:** the vault prose is **CC BY-NC-SA 4.0** (attribution "NightWatch / Thusus", forks stay open, no commercial redistribution). Facts aren't copyrightable; the compilation prose is. And the disclaimer up front: the trading journal is a **paper / dry-run book** — fills are simulated against real quotes, reported P&L is the engine's accounting, not realized money and not advice.

Repo: https://github.com/jamboree777/thusus-vault

Clone it, open it as a vault, poke the graph. Genuinely curious what PKM-native folks think of the machine-region-vs-prose-region pattern — it's the part I'm least sure generalizes.
