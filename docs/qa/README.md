# Validation report — 12 October 2026

## Completed

- `python3 scripts/check-site.py`: all 11 HTML/HTM pages, 152 local links and
  asset references, valid fragment targets, six destinations in every navigation,
  one H1/main/title per page, matching tag nesting, unique IDs, language and metadata.
- Complete 16-entry publication ledger: 2 books, 5 articles, 1 chapter,
  5 conference/workshop papers, 3 research reports. Original 14 entries archived.
- Independent colour contrast calculation: 5.18–13.85:1 for all normal text colours
  on page/white backgrounds; accent 6.12:1 on page and 6.62:1 on white. Warm gold
  is decoration only. Focus uses the specified blue ring.
- `node --check assets/js/navigation.js`: passed.
- `node scripts/check-navigation.cjs`: menu state, focus on open, Escape focus
  return, toggle, outside click, focus exit, link selection, viewport-change logic,
  current year and all six old numeric hashes passed using a DOM stub.
- Installed HTML5 parser (`html5lib`) reported no parsing errors for all 11 pages.
  This was an additional one-off check, not a hosting dependency.
- All 11 original source snapshots match the baseline Git blobs byte-for-byte.
- Deterministic renderer: a second render produces identical page bytes.
- `git diff --check`: passed.
- Outbound scholarly links checked: ACL, Springer DOI, DRDO DOI, Rokdung DOI,
  VitalSource and direct Cambridge Scholars product URL returned HTTP 200.
  Emerald DOI returned HTTP 403; retained as the original valid identifier for
  manual access checking. HTTP 200 does not establish rights or full-text access.

Machine-readable output: [static checks](static-checks.json) and
[outbound link responses](external-links.json).

## Browser QA explicitly skipped

No browser was connected to this VS Code Codex session. The user explicitly
requested skipping browser QA on 12 October 2026. Consequently:

- No screenshots were captured, including before/after screenshots.
- 320×800, 390×844, 768×1024, 1024×768 and 1440×900 rendered layouts are untested.
- No measured document scroll width or visual overlap test was performed.
- Real keyboard/touch interactions and screen-reader announcements are untested.
- No axe/Lighthouse browser audit was run; no score is claimed.

Source implements content-driven responsive grids, a 1120px desktop-navigation
breakpoint, minmax columns, word wrapping, 16px minimum gutters, reduced-motion and
increased-contrast preferences, and fully visible navigation when JS is disabled.
These source properties are not substitutes for rendered verification.

The Tamil quotation and transliterated footer phrase were subsequently removed
at the user’s request; this change was checked in generated HTML and source.

## Optional review walkthrough

Serve the parent folder with `python3 -m http.server 8000 --bind 127.0.0.1`.
Open `/rkn/` and check all six pages at the five target sizes. Confirm no horizontal
scrolling and no clipped publication names/email. Use Tab, Enter/Space, Escape and
an outside click to exercise the mobile menu. Check text at 200% zoom,
skip-link focus and JS-disabled navigation. Follow `education.html`,
`experience.html`, the three old HTM routes and `index.html#02`–`#06`.

Unresolved factual questions are listed in `content/editorial-status.md`; prospective
programme details remain held. No known critical source defect remains, but browser
behaviour is unverified by agreement.
