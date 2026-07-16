#!/usr/bin/env python3
"""validate_claims.py — schema gate for community claim PRs.

Given a list of changed claim files (paths under ``claims/pending/``), validate
each one against the published claim contract (see ``claims/TEMPLATE.md`` and
``concepts/frontmatter-spec.md``):

  - the file opens with a YAML frontmatter block that parses;
  - required keys are present and well-formed:
      claim_type   one of the whitelist below
      token        non-empty (base symbol, or a venue/chain id)
      source_url   an http/https URL (no source, no claim)
      observed_at  an ISO-8601-ish timestamp
      contributor  non-empty handle

On any failure the script writes a readable per-file report to the GitHub Step
Summary and exits non-zero, so the check fails. On success it writes an
"awaiting review" summary and exits zero.

Deterministic and dependency-light: uses PyYAML when available, otherwise a
minimal flat-frontmatter parser (claim frontmatter is flat key/value). Only the
default ``GITHUB_TOKEN`` is ever needed by the calling workflow — this script
touches no network and no secrets.
"""

from __future__ import annotations

import os
import re
import sys

CLAIM_TYPES = {
    "dw_change",
    "delist_notice",
    "contract",
    "team_event",
    "liquidity",
    "listing",
}

REQUIRED_KEYS = ["claim_type", "token", "source_url", "observed_at", "contributor"]

# Lenient ISO-8601: date, optionally with T + HH:MM(:SS)? and a Z or +HH:MM zone.
# Accepts the template's `2026-07-16T09:00Z` as well as full timestamps.
_ISO_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}"
    r"([T ]\d{2}:\d{2}(:\d{2}(\.\d+)?)?"
    r"(Z|[+-]\d{2}:?\d{2})?)?$"
)

_FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


def split_frontmatter(text: str):
    """Return (frontmatter_text, body) or (None, text) if no frontmatter block."""
    m = _FM_RE.match(text or "")
    if not m:
        return None, text or ""
    return m.group(1), text[m.end():]


def _strip_scalar(v: str):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    # drop inline comments on unquoted scalars ("dw_change   # note")
    return v


def parse_frontmatter(fm_text: str):
    """Parse a frontmatter block into a flat dict of str->str.

    Uses PyYAML when importable; otherwise a minimal `key: value` parser that
    covers the flat claim schema. Returns (data, error_or_None).
    """
    if fm_text is None:
        return None, "no YAML frontmatter block found (file must start with '---')"
    try:
        import yaml  # type: ignore
    except Exception:
        yaml = None

    if yaml is not None:
        try:
            data = yaml.safe_load(fm_text)
        except Exception as exc:  # noqa: BLE001
            return None, f"YAML frontmatter did not parse: {exc}"
        if data is None:
            return {}, None
        if not isinstance(data, dict):
            return None, "YAML frontmatter is not a key/value mapping"
        return {str(k): data[k] for k in data}, None

    # Fallback: minimal flat parser.
    data: dict = {}
    for raw in fm_text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None, f"frontmatter line is not 'key: value': {raw!r}"
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        # strip trailing inline comment for unquoted values
        if val and val[0] not in "\"'" and " #" in val:
            val = val.split(" #", 1)[0].strip()
        data[key] = _strip_scalar(val)
    return data, None


def validate_file(path: str):
    """Return a list of human-readable error strings (empty == valid)."""
    errors: list[str] = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except Exception as exc:  # noqa: BLE001
        return [f"could not read file: {exc}"]

    fm_text, _ = split_frontmatter(text)
    data, perr = parse_frontmatter(fm_text)
    if perr:
        return [perr]

    def _val(key):
        v = data.get(key)
        if isinstance(v, str):
            return _strip_scalar(v)
        return v

    # required-key presence
    for key in REQUIRED_KEYS:
        v = _val(key)
        if v is None or (isinstance(v, str) and not v.strip()):
            errors.append(f"missing or empty required key `{key}`")

    # claim_type whitelist
    ct = _val("claim_type")
    if isinstance(ct, str) and ct.strip() and ct.strip() not in CLAIM_TYPES:
        errors.append(
            f"`claim_type` is `{ct.strip()}` — must be one of: "
            + ", ".join(sorted(CLAIM_TYPES))
        )

    # source_url must be http/https
    su = _val("source_url")
    if isinstance(su, str) and su.strip():
        if not re.match(r"^https?://\S+$", su.strip()):
            errors.append(
                "`source_url` must be a reachable http(s) URL "
                "(no source, no claim)"
            )

    # observed_at ISO-ish
    oa = _val("observed_at")
    if oa is not None and str(oa).strip():
        if not _ISO_RE.match(str(oa).strip()):
            errors.append(
                f"`observed_at` is `{oa}` — must be an ISO-8601 timestamp "
                "(e.g. 2026-07-16T09:00Z)"
            )

    return errors


def _write_summary(lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    body = "\n".join(lines) + "\n"
    if path:
        try:
            with open(path, "a", encoding="utf-8") as fh:
                fh.write(body)
        except Exception:  # noqa: BLE001
            pass
    # also echo to stdout for the raw log (encode-safe on non-UTF8 consoles)
    try:
        sys.stdout.write(body)
    except UnicodeEncodeError:
        enc = sys.stdout.encoding or "ascii"
        sys.stdout.write(body.encode(enc, "replace").decode(enc, "replace"))


def main(argv):
    # The workflow scopes the diff to `claims/pending/**.md`; here we only guard
    # against the folder README and non-markdown (e.g. the .md.txt example).
    files = [
        f for f in argv
        if f.endswith(".md")
        and os.path.basename(f).lower() != "readme.md"
    ]

    if not files:
        _write_summary([
            "## Claim schema check",
            "",
            "No pending claim files changed in this PR — nothing to validate.",
        ])
        return 0

    all_errors: dict = {}
    for f in sorted(set(files)):
        if not os.path.exists(f):
            # deleted in the PR (e.g. an invalid file removed) — ignore
            continue
        errs = validate_file(f)
        if errs:
            all_errors[f] = errs

    if all_errors:
        lines = ["## Claim schema check — FAILED", ""]
        lines.append(
            "One or more claims do not satisfy the claim contract "
            "(see `claims/TEMPLATE.md`). Fix the items below and push again.\n"
        )
        for f, errs in all_errors.items():
            lines.append(f"### `{f}`")
            for e in errs:
                lines.append(f"- {e}")
            lines.append("")
        _write_summary(lines)
        return 1

    lines = ["## Claim schema check — schema OK", ""]
    lines.append(
        "All changed claims parse and carry the required keys "
        "(`claim_type`, `token`, `source_url`, `observed_at`, `contributor`).\n"
    )
    lines.append("Validated files:")
    for f in sorted(set(files)):
        if os.path.exists(f):
            lines.append(f"- `{f}`")
    lines.append("")
    lines.append(
        "**Schema OK — awaiting review.** A maintainer / AI review will confirm "
        "the source actually says this before it merges as fact. Verified claims "
        "earn Cherry — see the repo README and `claims/pending/README.md`."
    )
    _write_summary(lines)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
