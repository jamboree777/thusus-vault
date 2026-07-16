# Web Clipper templates

Two importable [Obsidian Web Clipper](https://obsidian.md/help/web-clipper) templates that pull NightWatch intelligence straight into **your own** vault — with our frontmatter contract and a source URL captured by construction.

Web Clipper is a free browser extension (Chrome, Firefox, Safari, Edge, Brave, Arc). These templates are plain `.json` in the extension's own export format (`schemaVersion 0.1.0`) — nothing NightWatch-specific to install.

## What each template does

| File | Use it on | Result |
|---|---|---|
| [`nightwatch-token-clip.json`](nightwatch-token-clip.json) | A NightWatch token page — `nightwatch-v1-frontend.onrender.com/token/*` or the live wiki `nightwatch-v1-api.onrender.com/kg/*` | New note in **`tokens/`** named after the page. Frontmatter `type: token`, `source: <url>`, `clipped: <date>`, `tags: nightwatch`. Body is the clipped content, footed with `[[Thusus]] · live: <url>` so the note always links back to the fresh source. Triggers auto-select this template on those two URL prefixes. |
| [`nightwatch-claim-capture.json`](nightwatch-claim-capture.json) | Any exchange notice / announcement / news page you want to report as a claim | New **ready-to-submit claim** in **`claims/pending/`**, dated filename. Frontmatter matches [`claims/TEMPLATE.md`](../claims/TEMPLATE.md) exactly (`claim_type`, `token`, `source_url`, `observed_at`, `contributor`, `status: pending`, `type: claim`). **`source_url` is auto-filled from the page URL** — provenance is captured by construction, so a claim can never lose its source. Body pre-fills the "What you observed" / "Source" sections with your selected excerpt quoted. |

The claim template deliberately leaves `claim_type`, `token`, and `contributor` as `REPLACE-ME` placeholders — you fill those three, then open a PR. The repo's schema-check Action ([`.github/scripts/validate_claims.py`](../.github/scripts/validate_claims.py)) will flag them until they are real, which is intentional: it stops a half-filled claim from merging.

**Tip:** highlight just the relevant sentence(s) on the page before clipping. `{{content}}` captures your selection when there is one, so the claim body becomes exactly the quoted notice rather than the whole page.

## How to import

1. Install the Web Clipper extension and open its **Settings** (the gear icon in the extension popup, or right-click the toolbar icon → Options).
2. Go to the **Templates** section in the left sidebar.
3. Click the **⋯ / more** menu next to *Templates* (or the import icon) and choose **Import**.
4. Select one of the `.json` files from this folder. Repeat for the second.
5. Set the extension's **Vault** (in *General* settings) to the folder where you cloned `thusus-vault` (or any vault of your own).
6. Done. Open a NightWatch token page and the **NightWatch Token** template is picked automatically by its URL triggers; on any other page choose **NightWatch Claim** from the template dropdown in the clipper popup.

Export/round-trip: the same **Templates → ⋯ → Export** action writes a template back out in this exact format, so you can tweak and re-share.

## Schema reference

Authored against the Obsidian Web Clipper template format, **`schemaVersion` `0.1.0`** — the format documented at [obsidian.md/help/web-clipper/templates](https://obsidian.md/help/web-clipper/templates) and used by the official community templates at [github.com/kepano/clipper-templates](https://github.com/kepano/clipper-templates). Fields used: `schemaVersion`, `name`, `behavior` (`create`), `noteNameFormat`, `path`, `noteContentFormat`, `properties[]` (`name` / `value` / `type` where type ∈ `text`, `multitext`, `date`), and `triggers[]` (URL-prefix match). Variables used: `{{title}}`, `{{url}}`, `{{content}}`, `{{date}}` (with the `date:"YYYY-MM-DD"` filter) — see [obsidian.md/help/web-clipper/variables](https://obsidian.md/help/web-clipper/variables).
