# Migration record

## Baseline and preservation

Redesign branch: `redesign-v2`, created from the fetched `origin/main` at
`6b03b54c84b533a2cda1becd3f0cb19833494b9a` on 12 October 2026.
The existing `redesign` branch was left intact. `main` was not modified.

All original HTML, CSS and README sources are preserved byte-for-byte in
`content/original/<original filename>.txt`, as well as in Git history.
`content/legacy-publications.md` contains all 14 original raw bibliography entries.
The supplied design specification is retained in `content/design-specification.md`.

## Audit and routes

| Original | Finding | Destination / remediation |
| --- | --- | --- |
| `index.html` | Long CV page; duplicate IDs; unmatched sections; missing education anchor; div menu | Research-first homepage, semantic HTML, six page navigation |
| `styles.css` | Conflicting content rules, fixed sidebar, invalid translateX | Shared `assets/css/site.css`; original CSS retained |
| `about.html` | Missing stylesheet; biography and memberships | New biography, CV sections, five degrees, appointments, teaching and awards |
| `education.html` | Missing stylesheet; conflicting dates | Styled landing with real link to `about.html#education` |
| `experience.html` | Truncated HTML; obsolete current-role wording | Styled landing with real link to `about.html#appointments` |
| `publications.html` | Missing stylesheet; incomplete/old list | Full 16-entry index, five categories, stable entry anchors |
| `O-index.htm`, `1-index.htm` | Older profiles and pending works; potential stale claims | Styled landing pages to home; full originals archived as `.txt` |
| `1-about.htm` | Alternate scaffold with missing CSS | Styled landing to About; full original archived as `.txt` |
| `1-style.css` | Alternate unused stylesheet | Retained unchanged; no current-page references |
| `README.md` | Outdated monograph status and addresses | Current preview, maintenance, QA and branch instructions |

Old homepage hashes `#01`–`#06` map to home, about, education, appointments,
publications and contact using `location.replace`; works on load and hash changes.
This enhancement requires JavaScript. Without JavaScript the complete normal
navigation remains visible and working. Legacy `.html` / `.htm` routes use real
links and canonical metadata, without script-only or automatic redirects.

## Content decisions

- Preserved the original 14 citations and added B01 (2025 monograph) and P01 (2025
  LiFE Suite paper). Category counts: 2 books, 5 articles, 1 chapter, 5 proceedings,
  3 reports. Full original editor list on P03 retained; reports remain reports.
- Primary Springer metadata corrects J02 author order: Ganesh Sinisetty precedes
  Karthick Narayanan; volume 46, issue 3, article 128. Original 1–12 pagination
  and conflicting historical author order remain in the original source archive.
- Verified J04 first author Ktien Hima and replaced the old PID link with the
  publisher's DOI. Verified direct ACL page and all 12 authors in published order.
- Five degrees preserved. PhD award year is 2021 and MA 2010–2012 per the supplied
  reconciliation. Thesis topics are descriptive, avoiding unverified formal titles.
- Six professional appointments, three early research appointments and three
  teaching records retained. Added the supplied CoDIN June 2026 role. Postdoc and
  other older appointment ranges use years where current-CV verification is absent;
  all original month detail remains archived for review.
- Retained academic memberships from the original biography; 2024 award preserved.
- Tholkudi and Suvadugal descriptions use conservative collaborative wording;
  no ownership, contract, funding, open-access or personally executed scanning claims.
- Prospective orthography programme and unpublished material are held from launch.
- Existing email retained. No guessed profiles, dummy CV, contact form or downloads.
- Per the user’s revised instruction, removed the Tamil quotation and the
  transliterated footer phrase from the public site. Original source copies remain archived.

## Image audit

Inspected `logo.png` (abstract ornament/waveform emblem), `image1.jpg` (monochrome
portrait), and `Slide1.JPG` (landscape slide with an older Krea postdoc identification).
No confirmed portrait identity, credits or licences accompany these files.
They remain unchanged at their original paths, but none is used in the redesign.
The new site uses text-led composition and has no external image or font dependency.

## QA and review limitations

[QA report](docs/qa/README.md) records static and navigation checks and outbound
link responses. Browser QA was waived by the user because this is a VS Code Codex
session with no connected browser. There are no screenshots or claimed browser
scores. Rendering and device font behaviour remain unverified.

[Editorial ledger](content/editorial-status.md) lists unresolved citation details,
exact historical dates, partner wording, publisher link status and held material.
These are review items; unresolved facts have not been invented.
No Pages configuration, deployment workflow, main commit or merge was changed.
