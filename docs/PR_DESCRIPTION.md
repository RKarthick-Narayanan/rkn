Rebuild the academic profile as six static pages with a research-first scholarly
layout, consistent typography, responsive grids, and shared navigation. Preserve
all 14 original publications and add the 2025 monograph and LiFE Suite paper,
with the complete education, appointment, teaching and award record accessible.

- Branch `redesign-v2` starts from `main` at `6b03b54`.
- All original sources are archived byte-for-byte; old HTML/HTM routes remain
  useful, and old numeric home bookmarks have an explicit compatibility mapping.
- Static HTML, CSS and minimal vanilla JS; no runtime dependencies or framework.
- Publisher-verified book/ACL links and corrected Springer author metadata.
- Semantic landmarks, skip links, progressive enhancement, menu state/focus
  handling, and reduced-motion/increased-contrast support.

## Validation

Passed checks for all 11 pages, 152 local links/assets and fragment references,
16 publication entries, HTML5 parsing, JS syntax and menu/bookmark logic, palette
contrast (5.18–13.85:1), deterministic generation, source preservation and
`git diff --check`. Six scholarly destinations returned HTTP 200. The inherited
Emerald DOI returned HTTP 403 to automated requests and needs manual access review.

**Browser QA was explicitly waived by the user in the VS Code Codex session.**
No screenshots, measured viewport overflow checks, live keyboard/screen-reader
verification or axe/Lighthouse audit are claimed.
The five requested viewport sizes and review steps are documented in
`docs/qa/README.md`. No screenshot placeholders are supplied.

## Editorial review

See `content/editorial-status.md` for the complete READY/CHECK/HOLD ledger. Review
2017 book title-page attribution; older proceedings/report details and author
order; formal thesis titles; exact appointment months; membership status; and
Tholkudi/Suvadugal role and partner wording. Historical citation details are
preserved where uncertain; new project language is conservative. Prospective
orthography programme details, sensitive or unpublished records, unverified
profiles and CV downloads remain held. The Tamil quotation and transliterated
footer phrase are omitted at the user’s request.

## Local preview

From the repository parent, run `python3 -m http.server 8000 --bind 127.0.0.1`
and open `http://127.0.0.1:8000/rkn/`. No build step is needed. Optional source
maintenance: `python3 scripts/render.py`, `python3 scripts/check-site.py` and
`node scripts/check-navigation.cjs`.

`main`, the earlier `redesign` branch, GitHub Pages settings and the live site are
unchanged. This PR does not merge or deploy the redesign.
