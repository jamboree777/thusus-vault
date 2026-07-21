---
type: lesson
date: 2026-07-21
trigger: "Worker task: build a tech-company knowledge graph (semis + AI complex), make entity names clickable in Haru's Read, and publish Haru's Read No1 (the Kimi-shock editorial)."
problem: "Haru's Read talks about SK Hynix, TSMC, ASML, Moonshot/Kimi etc. as flat prose. Readers had no way to see WHO these companies are or HOW they connect (who supplies whom, who competes, who owns whom) — and a KG of relations is only trustworthy if every edge is sourced. An unsourced 'ASML supplies TSMC' is indistinguishable from a hallucination."
change: "1) New nw_kg_entities (16 nodes: Samsung, SK Hynix, Micron, Kioxia, SanDisk, TSMC, ASML, Arm, NVIDIA, AMD, Intel, SoftBank, OpenAI, Anthropic, Moonshot, Zhipu) + nw_kg_relations (29 typed edges: supplies/customer_of/competes/owns_stake/invested_in/licenses). HONESTY INVARIANT enforced in schema AND seed: source_url is NOT NULL + a CHECK on non-empty + the seed refuses to insert any edge with an empty URL. Every one of the 29 edges was web-researched and carries a real source_url + as_of. 2) API /kg/entity/{slug} (entity + joined relations + live px via the RWA lane when rwa_base is set) and /kg/entities?known_names=1 (alias index for the linker). 3) Frontend shared _kg/EntityLink: longest-match, word-boundary linker + night popover (price, top-4 cited relations w/ src links). Wired into Observatory Haru's Read + /industries/semiconductors board names. 4) Haru's Read No1 (Kimi-shock editorial) published idempotently into nw_liam_briefs (2026-07-21, editorial=true)."
expected_effect: "Live: /kg/entity/sk-hynix returns 5 cited edges + SKHX px; nw_kg_relations has 0 rows with empty source_url (verified). Observatory items[0] = the No1 editorial; SK Hynix/TSMC/Moonshot in the prose are clickable -> cited popover. RULE for all future KG growth: a new edge without a source_url + as_of does not get added — an uncited edge is a fabricated edge. Any Claw/agent contributing KG edges must cite."
review_after: 2026-07-28
status: active
supersedes: ""
---

# Tech knowledge graph born — the cited-edges rule

First tech-company knowledge graph for NightWatch. The load-bearing decision is
not the schema — it is the **honesty invariant**: every relation carries a
`source_url` + `as_of`, enforced at three layers (DB NOT NULL, DB CHECK
non-empty, seed-time refusal). An uncited edge is a fabricated edge.

## What shipped
- **16 entities / 29 cited edges.** EUV (ASML -> TSMC/Samsung/SK Hynix/Intel/Micron),
  HBM (SK Hynix/Samsung/Micron -> NVIDIA), foundry (TSMC -> NVIDIA/AMD), Arm IP
  licensing, SoftBank owns Arm + funds OpenAI, SK Hynix ~14% of Kioxia, NVIDIA's
  $5B Intel stake, the memory competition triangle, and the AI-lab rivalry axis
  (Moonshot/Kimi vs OpenAI/Anthropic/Zhipu) that the No1 editorial rests on.
- **Clickable Haru's Read.** Company names in the brief open a night popover with
  live price (if tradable) and the top-4 cited relations; private names (Moonshot,
  Zhipu) read "private — not yet tradable".

## The rule to keep
Future KG edges — whether hand-added or contributed by a Claw/agent — MUST carry a
real source_url + as_of or they do not get inserted. The seed (`nw_kg_seed.py`)
already refuses uncited edges; keep that gate. Review 2026-07-28.
