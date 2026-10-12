# R. Karthick Narayanan — academic website

A buildless, six-page academic website for GitHub Pages at
<https://rkarthick-narayanan.github.io/rkn/>. HTML, shared CSS, and a small vanilla
JavaScript file provide an editorial, responsive layout and accessible navigation.
No runtime dependencies, remote fonts, framework, or data collection.

## Preview

From the repository's parent directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/rkn/>. Serving the parent tests the project subpath.
The committed HTML is ready to serve directly; Python is only a local helper.

## Pages and source

- `index.html`: research identity, themes, featured book, selected work, biography.
- `research.html`: research questions, contexts, methods, related scholarship.
- `projects.html`: research, archives, and collaborative documentation.
- `publications.html`: all 16 publications, grouped by type.
- `about.html`: biography, five degrees, appointments, teaching, awards, memberships.
- `contact.html`: direct academic email.
- `assets/css/site.css`: locked palette, typography, layout, responsive/print styles.
- `assets/js/navigation.js`: progressively enhanced menu and old bookmark mapping.

For updates, edit `scripts/render.py` for shared structure and page-specific copy,
`content/publications.json` for citations, and the relevant copy in
`content/design-specification.md` for the sourced paragraphs. Then regenerate:

```sh
python3 scripts/render.py
python3 scripts/check-site.py
node --check assets/js/navigation.js
node scripts/check-navigation.cjs
```

These helpers use Python and Node standard libraries and are optional for hosting.
Regeneration updates the committed static pages; no client-side content injection.
`publications.json` is the sole maintained bibliography; citations and editorial
status are separate fields. Shared academic facts and page shell live in the renderer;
repeated biography copy comes from the supplied specification.

## Validation and review

See [QA report](docs/qa/README.md), [migration record](MIGRATION.md), and
[editorial checks](content/editorial-status.md). Static checks verify local links,
fragments, landmarks, titles, language, publication count, and palette contrast.
Navigation tests verify logic using a DOM stub; they are not a browser audit.

**Browser QA was explicitly waived by the user on 12 October 2026 in the VS Code
Codex session.** Screenshots, rendered responsiveness, real keyboard navigation,
and axe/Lighthouse audits have not been performed.

## Deployment

This branch is `redesign-v2`, based on `main` at
`6b03b54c84b533a2cda1becd3f0cb19833494b9a`. Assets and internal links are relative
and compatible with `/rkn/`. No GitHub Pages settings or workflows were changed.
Review the pull request before authorising any merge or deployment. This work does
not deploy the redesigned site.
