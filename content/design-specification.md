# R. Karthick Narayanan — Academic Website Redesign
## Design document, content master, and Codex implementation specification

**Version:** 1.0  
**Prepared:** 12 October 2026 (IST)  
**Current live website:** https://rkarthick-narayanan.github.io/rkn/  
**Source repository:** https://github.com/RKarthick-Narayanan/rkn  
**Implementation target:** new branch `redesign-v2`, branched from `main`  
**Status:** design and editorial specifications; **no repository changes authorised by this document alone**

> **Instruction to Codex:** Treat this document as the authoritative design and content brief, not as permission to invent biographical facts or publish unverified material. Work only on `redesign-v2`. Do not push to `main`, merge a pull request, or change the GitHub Pages publishing settings. Preserve the existing site and keep all available historical content recoverable. Build, test, document, and open a reviewable PR.

---

# Executive decision

Rebuild this as a **scholarly, editorial, responsive personal academic website**, not a chronological online CV and not a flashy agency portfolio. The site should present a coherent research identity at a glance and offer deeper, well-organised academic material for visitors who want it.

**Primary proposition:** *Language, multilingualism, and the social life of archives.* The academic work joins sociolinguistics, language documentation, digital archiving, and community-centred research practices in India. The homepage should make these connections intelligible; the research, projects, and publications pages should provide evidence.

**Chosen approach:** static HTML + modern CSS + only essential vanilla JavaScript, built and deployed through the existing GitHub Pages repository. Avoid adding a framework, build system, CSS framework, image carousel, animation package, or CMS without a demonstrated necessity.

**Four completed design tasks captured here:**

1. Critically evaluate the existing site — audit and remediation requirements (Part I).
2. Decide visual identity and academic presentation — complete design system (Part II).
3. Plan homepage, navigation, and content hierarchy — sitemap and page blueprints (Part III).
4. Rewrite and organise academic content — site-ready copy and content ledger (Part IV).

Part V contains the operational specification and acceptance criteria for Codex.

---

# Part I — Critical evaluation of the existing website

## I.1 Audit basis and confidence

Sources inspected: the public live home page on 12 October 2026; the current `main` repository tree and the contents of `index.html`, `styles.css`, `about.html`, `education.html`, `experience.html`, `publications.html`, `README.md`, `O-index.htm`, and `1-about.htm`. The repository had 14 root-level files and no structured subdirectories at inspection. The published home page contains the biography, educational history, work experience, bibliographic list, and contact details on one long page.

**Limits:** No actual desktop/mobile screenshots or browser-rendered visual measurements were captured. Layout criticisms below are grounded in source code and page structure, **not** claims from a visual screenshot comparison. Codex must perform actual browser QA as part of the implementation.

**Evidence URLs:**

- Live: https://rkarthick-narayanan.github.io/rkn/
- Repository: https://github.com/RKarthick-Narayanan/rkn/tree/main
- Active home: https://github.com/RKarthick-Narayanan/rkn/blob/main/index.html
- Active CSS: https://github.com/RKarthick-Narayanan/rkn/blob/main/styles.css
- Separate pages: `about.html`, `education.html`, `experience.html`, `publications.html`
- Older draft: `O-index.htm`; additional alternate files `1-index.htm`, `1-about.htm`, `1-style.css`

## I.2 Existing strengths — retain these

- A clear and recognisable scholarly identity: linguist and archivist working on lesser-known languages, especially Toda and Kota, multilingualism, and linguistic/cultural documentation.
- Substantial factual academic material: degrees, appointments, teaching, research experiences, publications, and reports.
- Accessible point of contact via an email link.
- The existing Tamil quotation attributed to Vaali and the expression **“Katravai Patravai”** give the site a distinctive linguistic/personal character. Preserve with accurate attribution and appropriate language tagging.
- The website already uses static files and GitHub Pages, an appropriate infrastructure for a small academic profile.
- Existing publications have several direct DOI/permalink links worth retaining.

## I.3 Major issues and what to change

| ID | Severity | Evidence / observation | Why it matters | Required action |
|---|---|---|---|---|
| A01 | High | `index.html` puts biography, degrees, experience and bibliography in one page | Visitors cannot distinguish a research overview from an exhaustive CV | Develop separate research, projects, publications, and about/CV pages |
| A02 | High | Navigation link `href="#03"` has no matching `id="03"` in `index.html` | Education navigation is broken | Replace all numeric anchor IDs with descriptive IDs; test every link |
| A03 | High | Duplicate nested `<section id="01">` and surplus `</section>` elements | Invalid/incoherent semantic structure | Rebuild valid semantic HTML, one `main`, one H1 per page |
| A04 | High | `styles.css` declares `.content` more than once, with conflicting margins/padding | Fragile, hard-to-maintain layout | Replace with one predictable CSS grid/container system |
| A05 | High | `transform: translateX;` is invalid CSS in `.timeline-entry.right` | Browser ignores the declaration; timeline may position unpredictably | Remove alternating timeline or fix it; preferred: use a straightforward chronological list |
| A06 | High | Fixed header and a 200px fixed left sidebar with hardcoded content offset | Compromises available reading width and adaptability | Use horizontal desktop navigation and a compact mobile menu |
| A07 | High | Hamburger is a clickable `<div onclick="toggleSidebar()">` | Not inherently keyboard-operable or properly announced to assistive tech | Use an actual `<button>`, `aria-expanded`, `aria-controls`, Escape and outside-click behaviour |
| A08 | High | `about.html`, `education.html`, `experience.html` and `publications.html` reference `style.css`, which does **not** exist in repository | Direct visits to these pages may be unstyled | Consolidate styling in `assets/css/site.css` and standardise page scaffolding |
| A09 | High | 2025 monograph missing; 2025 collaborative NLP publication missing | Academic record is materially outdated | Include verified newer publications prominently |
| A10 | High | Educational dates disagree between versions (PhD 2014–2019 vs historical 2014–2021; MA 2010–2012 vs 2010–2013) | Publishing an incorrect academic chronology harms credibility | Use the reconciled fact ledger below; flag items requiring confirmation |
| A11 | Medium | Biography is four long paragraphs before visitors encounter research output | Weak scanability and first-impression hierarchy | Short introductory thesis, featured publication, current work and four research themes |
| A12 | Medium | Publications grouped as “Journals Published in India/Abroad” | Geography is a weak discovery mechanism | Group by books, journal articles, chapters, proceedings, and reports; reverse chronology within categories |
| A13 | Medium | Plain `alt="Logo"` and no distinct image/credit system | Weak accessible alternatives and uncertain asset provenance | Meaningful `alt`, image provenance, and consent-led image use |
| A14 | Medium | Page title is `Karthick's Page`; SEO/social metadata are minimal | Search result lacks academic context | Unique titles, descriptions, canonical URLs, OpenGraph metadata and structured data only for verified facts |
| A15 | Medium | `README.md` is outdated, has errors and older contact addresses | Confusing maintainer documentation | Rewrite as installation/deployment/content-maintenance guide |
| A16 | Medium | Root contains old alternate files and images with opaque names | Risk of publishing orphaned or conflicting pages | Inspect references first; move unused legacy files to `legacy/` only if safe |
| A17 | Medium | Copyright text hardcodes 2024 | Site looks stale | Use current year, or an explicit dated range with responsible ownership wording |
| A18 | Medium | No clearly differentiated projects, archives, methods or outreach | Work outside conventional appointments is invisible | Add project archive with roles, collaborators and status, without overstating institutional ownership |

## I.4 Editorial diagnosis

The site is academically substantive but currently answers **“what positions has this person held?”** better than **“what intellectual problems does this person work on, what has this work produced, and how can I engage with it?”** That ordering should be reversed. Readers should encounter the research proposition, evidence of scholarship, and selected work before any full chronology.

Do **not** reduce the site to marketing vocabulary such as “pioneering innovator,” “transformative leader,” “revolutionising indigenous technology,” or ungrounded impact metrics. Academic authority should emerge from precise descriptions, evidence, citations, and transparent collaborations.

## I.5 Factual discrepancies requiring disciplined handling

| Field | Conflicting material | Resolution for design stage | Publication rule |
|---|---|---|---|
| PhD | Current home and `education.html`: 2014–2019; older `O-index.htm`: 2014–2021 | Use **PhD in Linguistics, JNU; awarded 2021**, with 2014–2021 as candidature period only if necessary | Do not show 2019 as award year |
| MA | Home: 2010–2012; `education.html`: 2010–2013 | Use 2010–2012, consistent with past CV information | Confirm if a qualification transcript suggests otherwise |
| Postdoc end date | Site: March 2024; other profile records: January 2024 | Display **2022–2024** until end month reconciled | Do not invent a month |
| CoDIN role | Home: Executive Director; older pages may omit CoDIN | Use **Executive Director, Council for Diversity and Innovation (CoDIN)** | Current, institutionally grounded |
| UnReaL-TecE role | One page says August 2024–Present; home says August 2024–2026 | Use **Chief Community and Data Officer, 2024–2026** | Do not list as current without renewed confirmation |
| 2017 Toda book author credit | Several forms of collaborator name / title transliteration | Preserve existing bibliography provisionally; verify from title page/ISBN | Do not silently correct names |
| 2024 award | Home names SPARROW-R Thyagarajan Literary Award | Preserve if included; source indicates user-supplied academic identity | Do not invent awarding venue or speech |
| IGNCA/RIWATCH orthography programme | Planning, proposals, pilots and MoU discussions have evolved | Treat as **collaborative programme development** | No unverified claim of a signed contract, awarded grant, or completed pilot |

---

# Part II — Visual identity and academic presentation

## II.1 Positioning

**Brand archetype:** scholarly editorial. Visually akin to a carefully designed research publication: understated, patient, evidence-led, culturally attentive, and legible across devices. The site is personal, not a CoDIN institutional microsite; organisations are identified where relevant but should not overpower the scholar's name.

**Tone:** intellectually confident but not self-promotional; specific rather than grandiose; plain, precise English; no marketing jargon. Use third person for short formal biography, first person for reflective research introduction if needed, but do not switch grammatical person unpredictably within a page. In this document the main on-page copy adopts a generally **first-person research voice** with a **third-person formal biography**.

**Core themes:** languages in society; multilingual life and language vitality; linguistic and cultural documentation; community-centred archives and governance; orthography and language resources.

**Visual motif:** typography and disciplined whitespace. Optional small line/shape accent inspired by annotations, transcription or archival metadata; never use pseudo-Indigenous ornamentation or cultural symbols without context, permission and attribution.

## II.2 Colour tokens (locked)

| Token | HEX | Use |
|---|---|---|
| `--color-ink` | `#1F2F35` | Primary text/headings |
| `--color-page` | `#F7F6F2` | Background |
| `--color-surface` | `#FFFFFF` | Paper/card surface |
| `--color-accent` | `#24675D` | Interactive links/buttons, rules and accents |
| `--color-muted` | `#586B70` | Secondary labels and descriptive copy |
| `--color-line` | `#DFE3DF` | Dividers/borders |
| `--color-warm` | `#B18750` | Rare decorative accents only — **not** body text on white |
| `--color-focus` | `#1D5EAE` | Focus ring; use adequate contrast |

The principal text palette achieves strong contrast: `#1F2F35` on `#F7F6F2` ≈ 12.8:1; `#24675D` on white ≈ 6.6:1; `#586B70` on white ≈ 5.6:1. Warm gold on white is insufficient for ordinary text, so restrict its use to nonessential decoration.

No automatic dark-mode variant for v1. Respect device preferences for reduced motion and increased contrast. A coherent high-quality light theme is preferable to two inconsistent modes. If a dark mode is added in a later phase, it must be fully designed and tested, not merely colour-inverted.

## II.3 Typography

- **Display headings:** Georgia, `Iowan Old Style`, or available high-quality serif fallbacks. Avoid external paid fonts and remote dependencies. Example: `font-family: Georgia, 'Times New Roman', serif;`.
- **UI/body:** system sans stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', Arial, sans-serif`.
- **Tamil text:** dedicated fallback chain such as `'Noto Sans Tamil', 'Tamil Sangam MN', 'Latha', sans-serif`; use `<span lang="ta">…</span>` and test glyph rendering on Android, iOS and Windows.
- Body size: `clamp(1rem, 0.97rem + 0.14vw, 1.08rem)`, line-height 1.65–1.75.
- Desktop H1: `clamp(2.5rem, 5vw, 4.65rem)`, line-height 1.08–1.15.
- Page H1: `clamp(2.15rem, 4vw, 3.6rem)`; H2: `clamp(1.55rem, 2.6vw, 2.25rem)`.
- Navigation and labels: 0.875–0.95rem, with genuine text case rather than unnecessary all caps.
- Bibliographic entries: 1rem with generous line spacing and hanging-indent treatment only when readable on mobile.
- Do not use line-length-stretching justification. Never allow all-cap lengthy prose.

## II.4 Spatial system

- Main site max-width: **1120px** (`--container: 70rem`) including gutters.
- Reading text max-width: **68ch**, ideally 60–68 characters for prose; use full width for structured bibliography, tables and project cards where appropriate.
- Side gutters: `clamp(1rem, 4vw, 2.5rem)`.
- Vertical section separation: 64–104px desktop, 40–72px mobile.
- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64, 96px.
- Corner radius: 8px or 12px for lightweight cards; avoid fully rounded/pill shapes everywhere.
- Borders: 1px `var(--color-line)`; no deep shadows. Shadows only when they meaningfully clarify an elevated surface.
- Avoid fixed-width cards below 360px. Text must not overflow at 320px viewport width.

## II.5 Global components

1. **Site header:** wordmark `R. Karthick Narayanan` (text-led), optional subtle monogram or verified asset. Six primary navigation links. Header may be sticky if unobtrusive, but not so tall that it obscures anchor targets.
2. **Mobile menu:** actual button with accessible label; expandable menu with correct state, focus management, Escape-to-close. No hover-only navigation.
3. **Hero:** eyebrow `Linguist · Digital Archivist`, strong academic name/headline, concise research statement, two text links: `Explore research` and `View publications`.
4. **Research theme module:** clean numbered/labelled entries or quiet cards, title plus concise description; no generic stock icons.
5. **Publication entry:** title, full collaborators, venue, year, type, available DOI/permalink, optionally short context; no invented downloads or citation metrics.
6. **Project article:** name, role, collaborating institution(s), date range, status, 75–130-word description, confirmed link, credits if imagery is used.
7. **Formal experience list:** reverse chronology, two-column date/detail arrangement desktop and single column mobile. No alternating centre-line timeline.
8. **Editorial pullquote:** Tamil quotation and author attribution, as a deliberate supporting element below the primary research introduction, not replacing it.
9. **Footer:** contact email, © current year, optional expression `Katravai Patravai`, links to verified academic profiles only.

## II.6 Imagery policy

The current repository has `logo.png`, `image1.jpg` and `Slide1.JPG`. Codex must inspect them before reuse and determine whether each image depicts the person, a logo, a slide, or something else. Do not assume image identity from filename alone. Prefer one properly credited, high-resolution profile photograph if rights and identity are clear; the layout must also work **without** any photograph. Do not invent a portrait or generate documentary imagery representing named communities. Any community images, performances or archival objects need permission, attribution and an appropriate caption. Never scrape a third-party photograph into the repo just for visual decoration.

## II.7 Responsive behaviour

| Viewport | Composition | Navigation | Special checks |
|---|---|---|---|
| 320–479px | Single column, full line-wrap, 16px minimum gutters | Collapsible accessible menu | Tamil text, long surnames, DOI links, no x-scroll |
| 480–767px | Single column; slightly larger type | Collapsible menu | Clear section gaps |
| 768–1023px | Wider single column or optional two-column project cards | Desktop menu only if labels fit | No squeezed navbar |
| ≥1024px | Editorial grid, max 1120px, with constrained text column | Full horizontal nav | Hero balance, generous empty space |

Use content-driven breakpoints where appropriate; 768 and 1024 are guideposts, not arbitrary requirements. Honour `prefers-reduced-motion: reduce`; do not use parallax, autoplay, rotating quotations or decorative scroll effects.

---

# Part III — Homepage, navigation and hierarchy

## III.1 Canonical sitemap and URLs

Use an uncomplicated multi-page static structure. Keep the published subpath `/rkn/` working. Prefer **relative asset and internal URLs**, not root-relative `/assets/...`, which break under a GitHub Pages project subpath.

| Nav label | URL | Page title | Role |
|---|---|---|---|
| Home | `index.html` | `R. Karthick Narayanan — Linguist & Digital Archivist` | Thesis + selected work |
| Research | `research.html` | `Research — R. Karthick Narayanan` | Questions, themes, methods and language contexts |
| Projects & Archives | `projects.html` | `Projects & Archives — R. Karthick Narayanan` | Evidence of documentation, archiving and collaboration |
| Publications | `publications.html` | `Publications — R. Karthick Narayanan` | Complete, accurate scholarship index |
| About / CV | `about.html` | `About & CV — R. Karthick Narayanan` | Bio, education, appointments, teaching, awards |
| Contact | `contact.html` | `Contact — R. Karthick Narayanan` | Email, selected verified links, collaboration invitation |

Use real HTML pages, rather than single-page numeric anchor navigation. Existing `education.html` and `experience.html` must **not** break after redesign: retain as lightweight redirect/landing pages to `about.html#education` and `about.html#appointments` using real links and optional meta refresh. Existing `#02`, `#04`, `#05`, and `#06` links should be handled where feasible via an explicit `legacy-anchor` mapping or documented change; do not add conflicting duplicate IDs. Do not assume search engines will interpret script-only redirects reliably.

## III.2 Homepage content order

**Above the fold (especially at 390px):** name, professional descriptor, 2–3 line statement, one primary navigation action. Avoid a portrait that pushes every meaningful word below the fold.

1. **Header:** name wordmark + responsive navigation.
2. **Hero:** `R. Karthick Narayanan`; descriptor `Linguist · Digital Archivist`; short research thesis (copy in Part IV); two links.
3. **Research at a glance:** four themes: Multilingualism & vitality; Documentation & verbal art; Digital archives & data stewardship; Orthographies & language resources.
4. **Featured scholarship:** 2025 monograph with verified publisher link, one-sentence contribution; optionally one selected journal article about SiDHELA and one collaborative 2025 LiFE Suite paper.
5. **Selected work:** 3 to 4 records, one per well-defined area, each linking to the projects page. Do not treat institutional partners as projects in their own right.
6. **Position / short biography:** current CoDIN role, JNU PhD, field contexts in Nilgiris and Himalayan regions.
7. **Tamil quotation:** preserved with Vaali attribution and source clarification if a full verse/rights question arises; it should be visually distinct and readable, never used as the sole headline.
8. **Contact invitation:** restrained closing sentence plus direct mail link.
9. **Footer.**

**Desktop composition in words:** two-column hero with text occupying about 7/12 of width and optional portrait/empty editorial whitespace in 5/12; below, a full-width thin divider; four research themes in a 2×2 or 4-column responsive pattern; featured monograph in a restrained wide module; selected project teasers; biography and quotation; footer. On mobile, all blocks stack in the same semantic order.

## III.3 Page-by-page blueprints

### Research (`research.html`)
- H1 `Research`.
- Lead paragraph stating the common intellectual problem.
- Four H2 sections, each with 100–160 words of thematic analysis and context, not marketing claims.
- `Languages and regions` side note: Toda, Kota, Rongpo/Rongpo-related research, Spiti, and North-East Indian language contexts where professionally applicable; distinguish deep sustained field research from projects/support roles.
- `Methods and commitments`: sociolinguistic fieldwork; linguistic documentation; phonetic/phonological analysis where applicable; digital preservation; community-centred participation and governance.
- Relevant publications appended under each theme with links to bibliography anchors.
- Do not claim the site hosts primary field recordings or unpublished community data.

### Projects & Archives (`projects.html`)
- H1 `Projects & Archives`.
- Explain roles precisely: authored research, archival practice, organisational project, collaborative programme, or project in development.
- Distinguish **Selected research and completed work**, **Current collaborations**, and **Initiatives in development**.
- Eligible records for launch: Toda–Kota research and 2025 monograph; SiDHELA contribution; Tholkudi digital archive work; Suvadugal documentation collaboration; LiFE Suite / BoLI collaboration. Orthography programme can be described conservatively but should be held from public launch unless final role/status is verified.
- Each record contains title, dates, one-line role, partners, outcome and source. Avoid claimed sample totals, budget values or dataset releases without direct source and permission.
- No scraped community images or culturally sensitive source files.

### Publications (`publications.html`)
- H1 `Publications`.
- Intro: peer-reviewed and scholarly work in sociolinguistics, language documentation, verbal art and archiving.
- Featured book (2025) at top, distinct from the full list.
- Sections: Books; Journal Articles; Book Chapters; Conference Papers/Proceedings; Research Reports and Archival Outputs.
- Reverse chronological inside each category. Include all **14 original entries** (1 book + 5 journal articles + 1 chapter + 4 proceedings + 3 reports), **plus** the 2025 monograph and verified 2025 LiFE paper. Codex must re-count from source and **not** drop any entry; the explicit ledger below is authoritative.
- Each entry: full author list, year, title, venue/publisher, volume/pages/ISBN/DOI when available; distinguish peer-reviewed papers, conference proceedings and commissioned reports.
- Add simple filters only if the total warrants it; category anchors are sufficient for v1.

### About & CV (`about.html`)
- H1 `About`.
- Formal third-person profile (Part IV).
- Research trajectory (Nilgiris, Himalayas, university/archival experience); avoid assuming every project is personally led.
- Education (five degrees) with JNU dissertation/thesis titles only where verified.
- Appointments in reverse chronology; teaching separate from appointments if needed.
- 2024 SPARROW-R Thyagarajan Literary Award, with concise verified wording.
- Downloadable CV link **only if a verified, current PDF is provided**. Otherwise omit the button; never link a dummy CV.
- Historical positions remain accessible without dominating home.

### Contact (`contact.html`)
- Direct link `mailto:karthick.narayanan@outlook.in` (existing site's public address).
- Short invitation for academic correspondence or appropriate collaborations.
- Optional public verified Google Scholar, ORCID, CoDIN, GitHub links; never guess URLs.
- No contact form collecting data unless actively requested, since email is sufficient.

## III.4 Content rules

- **One source of truth** for repeated biography facts and publication metadata (a small `data/publications.json` or a maintained Markdown data document is fine; choose the lightest solution). Codex should not introduce a JavaScript application just to load static text.
- Use IDs such as `#multilingualism`, `#digital-archives`, `#books`, `#education`, not `#01`.
- Make the global header/footer consistent on every page; for a static site, a modest amount of duplicated markup is acceptable, but extract it only if a simple mechanism can be supported on GitHub Pages without fragile client-side injection.
- All named affiliations and partner logos should reflect actual roles and permissions.
- Keep the academic biography distinct from the institutional marketing profile of CoDIN.
- No metrics such as “X endangered languages saved,” “thousands of lives impacted,” or data-scale claims without defensible evidence.

---

# Part IV — Edited and reorganised academic content

> **Editorial status key**  
> **READY** — copy grounded in published site, GitHub source, supplied professional history or independently verified scholarly metadata.  
> **CHECK** — credible working copy but factual dates/role names, links, or attribution need final checking before publication.  
> **HOLD** — do not automatically publish; pending confirmation of programme or permission.  
> The status flags belong in the working content ledger, **not** on the public website.

## IV.1 Identity and homepage — READY

### Name / descriptor

**R. Karthick Narayanan**  
**Linguist · Digital Archivist**

### Hero headline

**Languages in society. Knowledge in context. Archives for the future.**

### Hero introduction

> I work at the intersection of sociolinguistics, language documentation, and digital archiving. My research examines multilingual life, language vitality, and the social conditions in which languages are maintained, marginalised, or displaced. Alongside field-based research, I work on community-centred approaches to documenting and stewarding linguistic and cultural knowledge.

### Hero links

- `Explore my research` → `research.html`
- `Browse publications` → `publications.html`

### Short formal identification

> R. Karthick Narayanan is a linguist and digital archivist and serves as Executive Director of the Council for Diversity and Innovation (CoDIN). He holds a PhD in Linguistics from Jawaharlal Nehru University. His research draws particularly on work with Toda and Kota communities in the Nilgiris and on documentation and archival initiatives in other regions of India.

### Home research teasers (READY)

**Multilingualism and language vitality**  
How multilingual communities organise language use, negotiate social change, and sustain linguistic practices under unequal conditions.

**Documentation and verbal art**  
Recording and studying spoken language, oral traditions, and other forms of linguistic and cultural expression with attention to their social context.

**Digital archives and data stewardship**  
Designing and evaluating archives as sites of preservation, access, responsibility, and participation rather than as neutral storage systems.

**Orthographies and language resources**  
Exploring how community participation, linguistic analysis, and digital tools can support language resources and writing-system choices.

### Featured publication (READY)

**Multilinguality, Vitality, and Endangerment: Insights from the Lived Experiences of Multilingual India**  
R. Karthick Narayanan · Cambridge Scholars Publishing · 2025  
Print ISBN 978-1-0364-5464-7 · eBook ISBN 978-1-0364-5465-4

> Drawing on Toda and Kota experiences in the Nilgiris, this book questions approaches to language endangerment that overlook everyday multilingualism and the structural conditions shaping language choice.

**Source:** https://archive.cambridgescholars.com/product-category/social-sciences/language-and-linguistics/page/2/?orderby=date (publisher catalogue); https://www.vitalsource.com/in/products/multilinguality-vitality-and-endangerment-r-karthick-narayanan-v9781036454654 (ISBN metadata). Codex should seek a **direct permanent publisher product URL** and use it if verified; a category listing is not a substitute for a stable book-specific link.

### Optional cultural quotation — READY / ATTRIBUTION CHECK

> “ஏன் என்ற கேள்வி இங்கு கேட்காமல் வாழ்க்கை இல்லை...”  
> — Vaali (வாலி)

The source website contains a longer two-line Tamil quotation. For the redesign, retain the existing wording and attribution only after confirming the exact excerpt and any relevant permissions. Tag Tamil text `lang="ta"`. Codex must not extend it or add other lyrics. `Katravai Patravai` may appear discreetly in the footer.

## IV.2 About page — READY, subject to items in factual ledger

### Full professional biography

> R. Karthick Narayanan is a linguist and digital archivist whose research explores multilingualism, language vitality, and the documentation and stewardship of linguistic and cultural knowledge. His work is grounded in the view that languages must be understood through their speakers' social worlds and the historical, institutional, and political conditions that shape language use.
>
> He earned his PhD in Linguistics from Jawaharlal Nehru University in 2021. His doctoral research examined language maintenance among the Toda and Kota communities of the Nilgiris, with particular attention to multilingual practices and language shift. This research informed his 2025 monograph, *Multilinguality, Vitality, and Endangerment: Insights from the Lived Experiences of Multilingual India* (Cambridge Scholars Publishing).
>
> His academic and professional experience spans language documentation, sociolinguistic fieldwork, linguistic description, digital language archives, teaching, and community-centred research initiatives. His work has engaged with Toda oral literature, documentation in Himalayan regions, archival infrastructures, and collaborative approaches to language technologies and resources.
>
> He serves as Executive Director of the Council for Diversity and Innovation (CoDIN). Previously, he held a postdoctoral fellowship at the Moturi Satyanarayana Centre for Advanced Study in the Humanities and Social Sciences at Krea University and worked on linguistic and archival projects with research institutions including Sikkim University and the Central Institute of Indian Languages. In 2024 he received the SPARROW-R Thyagarajan Literary Award in recognition of his work on Toda verbal art.

**Copy edit safeguards:** Do not state that the monograph was the doctoral dissertation verbatim. Do not assert that all co-authored projects were led solely by the site owner. Avoid the phrase “saving endangered languages.”

### Educational history (READY / date reconciliation)

- **PhD, Linguistics**, Jawaharlal Nehru University, New Delhi; **awarded 2021**. Dissertation research: language maintenance among Toda and Kota in the Nilgiris. Historical title on `education.html`: *Maintenance of Minority Languages of Nilgiri District, Tamil Nadu: A Case Study of Toda and Kota* (**CHECK formal title before printing it as a thesis title**). Supervisors: Anvita Abbi and Ayesha Kidwai (previous academic profile).
- **MPhil, Linguistics**, Jawaharlal Nehru University, New Delhi; **2012–2014**. Dissertation: *Assessing Vitality of Languages Spoken by Less than 10,000 Speakers in India* (**CHECK capitalisation and exact title**).
- **MA, Linguistics**, Jawaharlal Nehru University, New Delhi; **2010–2012**. Dissertation research on Shekhawati phonetics and phonology (**CHECK exact official title**).
- **BEd, English Language Teaching**, Tamil Nadu Teacher Education University; **2009–2010**.
- **BA, English**, Loyola College, Chennai / University of Madras; **2006–2009**.

### Selected professional appointments (READY / exact ending months CHECK)

- **Executive Director**, Council for Diversity and Innovation (CoDIN), **June 2026–present**.
- **Chief Community and Data Officer**, UnReaL-TecE LLP, **2024–2026**.
- **Post-Doctoral Fellow**, Moturi Satyanarayana Centre for Advanced Study in the Humanities and Social Sciences, Krea University, **2022–2024**.
- **Senior Resource Person**, Orthography Development for Languages of North-East India, Central Institute of Indian Languages, **2021–2022**.
- **Teaching Faculty**, Department of Linguistics, Central University of Karnataka, **2021**.
- **Research Associate and Digital Archivist**, Centre for Endangered Languages, Sikkim University, **2019–2020**.

### Early research and teaching (READY / original dates where relevant)

- **Junior Resource Person**, Scheme for Protection and Preservation of Endangered Languages, Central Institute of Indian Languages, **2014**.
- **Research Assistant**, Toda Oral Literature Project, Sahitya Akademi, **2015–2016**.
- **Junior Resource Person**, Rongpo and Spiti-related language documentation, **2016** (retain precise project agency/institution after checking original appointment).
- **Course Teacher**, Introduction to Phonetics, Jawaharlal Nehru University, **2015**.
- **Field Methods and Data Digitisation Tutor**, Jawaharlal Nehru University, **2015 and 2016**.

The original site has more precise start/end months. Retain them only when internally consistent with a current CV; do not invent months for newer appointments.

## IV.3 Research page — READY

### Page lead

> My research asks how multilingualism shapes language vitality, how social institutions influence language maintenance and shift, and how the documentation and archiving of language can be made accountable to the people whose knowledge is represented. These questions connect my research in the Nilgiris with work on verbal art, linguistic resources, and digital infrastructures elsewhere in India.

### R1. Multilingualism, vitality, and endangerment

> The study of language endangerment often begins by counting speakers or examining intergenerational transmission. These measures matter, but they do not by themselves explain the place of a language in a multilingual society. My work investigates how people distribute language use across social relationships, institutions, and practices; how language choices are shaped by unequal access to resources and recognition; and how communities sustain multilingual repertoires. My research with Toda and Kota speakers in the Nilgiris offers a context for questioning simplified associations between multilingualism and language decline. This line of research is developed in my 2025 monograph.

**Related work:** 2025 monograph; 2019 methodological review; 2022 chapter on gender differences and language shift.

### R2. Documentation, description, and verbal art

> Linguistic documentation involves more than accumulating recordings or transcriptions. It requires attention to genres, performance settings, interactions, and the knowledge relationships within which language is used. My work has included documentation and study of Toda oral literature and participation in descriptive and documentary initiatives in Himalayan language contexts. I am particularly interested in approaches that allow linguistic materials to remain intelligible and useful in their social and cultural settings, including through careful metadata, annotation, attribution, and access arrangements.

**Related work:** 2017 Toda oral-literature volume (with Vasamalli); Rongpo reports; Toda acoustic research.

### R3. Digital archiving and community-centred stewardship

> A language archive is not only a technical repository. Decisions about what is collected, how material is described, who may access it, and how it may be reused are also social and ethical decisions. My work in digital archiving has included SiDHELA and subsequent archival collaborations. I am interested in participatory archives, the relationship between preservation and community authority, and governance arrangements that account for the responsibilities attached to linguistic and cultural data. Digital tools should support careful stewardship rather than obscure the relationships through which data are created.

**Related work:** 2020 SiDHELA article; 2022 collaboratory-model article; Tholkudi archival work (**CHECK scope**).

### R4. Orthography, resources, and language technology

> Orthography development and the creation of digital language resources raise questions that are simultaneously linguistic, educational, social, and technological. Script and spelling choices require attention to sound systems, learnability, existing practices, community preferences, and available technologies. My work and collaborations in this area connect linguistic analysis with documentation workflows and language-data infrastructures. I am especially interested in the conditions under which communities can make informed choices about the creation, use, and governance of their language resources.

**Related work:** prior CIIL orthography role; collaborative LiFE Suite paper (2025); programme development in North-East India (**HOLD current programme details unless confirmed**).

### Methods / cross-cutting practices (short list)

Sociolinguistic and ethnographic fieldwork; language documentation; verbal-art analysis; linguistic annotation; archival design and metadata; collaborative digital resources; participation, attribution and culturally appropriate access.

## IV.4 Projects & Archives — copy and publication state

The project page should **not** suggest that every initiative belongs to, is funded by, or was founded by the site owner. Each article must say what the owner did and what collaborators did. Suggested text:

### P1. Toda and Kota: multilingualism and language vitality — READY

**Type:** Research programme / doctoral and subsequent scholarship  
**Period:** Long-term field research; monograph published 2025  
**Role:** Researcher and author  
**Context:** Nilgiris, Tamil Nadu

> Research on language maintenance and multilingual practices among Toda and Kota communities in the Nilgiris. This work investigates language choice and change in relation to social life and structural inequalities. It forms the empirical foundation of the 2025 monograph *Multilinguality, Vitality, and Endangerment*.

**Link:** verified publisher/book page when available. **Image:** optional, subject to permission.

### P2. SiDHELA: endangered-language archiving — READY / exact project role CHECK

**Type:** Digital language archive  
**Period:** Linked to Sikkim University appointment, 2019–2020  
**Role:** Research associate and digital archivist; co-authored subsequent scholarly analysis  
**Collaborators:** Centre for Endangered Languages, Sikkim University

> Work on documenting and organising language collections within the Sikkim–Darjeeling Himalayas Endangered Language Archive (SiDHELA). The experience informed published research on the development of language archives in India and collaborative approaches to their creation.

**Link:** link to an archive URL **only after checking that it still resolves and that the specific collection is appropriate for linking**.

### P3. Tholkudi digital archive — READY / scope CHECK

**Type:** Digital heritage and archival infrastructure  
**Period:** 2025–2026  
**Role:** Archival planning / digital repository collaboration (**CHECK contractually accurate designation**)  
**Collaborators:** The project owners and implementing organisations should be named exactly as contractually permitted.

> Contribution to the organisation, digitisation, description and long-term accessibility of linguistic and cultural heritage collections through a digital repository. This work concerns the practical relationship between archival metadata, preservation infrastructure and responsible access.

Do not claim personal ownership of the Tholkudi archive or that all materials are open access. Use `https://tholkudi.in/` only after verifying public availability and intended access.

### P4. Suvadugal: performing-arts documentation — READY / partnership wording CHECK

**Type:** Collaborative documentation and digital-heritage initiative  
**Period:** 2026  
**Role:** Research/curatorial and documentation collaboration through CoDIN with Alternative Media Centre  
**Collaborators:** Alternative Media Centre and participating artists, practitioners and organisations

> Suvadugal brings together documentation of performing-arts practices, artists, instruments, and associated material culture. Recent work has included the documentation and 3D scanning of Silambam objects and a curated exhibition on Silambam material traditions. The initiative connects field documentation with questions of interpretation, attribution, digital representation and the continuity of artistic knowledge.

Do **not** say the site owner personally performed 3D scanning. Distinguish scanning teams, organisers, and community practitioners in extended project detail. Do not publish images or 3D models without clearance.

### P5. Collaborative language technology and LiFE Suite — READY / role CHECK

**Type:** Collaborative publication and resource development  
**Period:** 2025 onward (only show an ongoing range if continuing role is established)  
**Role:** Co-author / collaborator  
**Collaborators:** Research and technology co-authors as in the 2025 paper

> Collaboration on approaches connecting community-based linguistic data collection with annotation, dataset preparation and language-technology workflows. The 2025 paper *Field to Model: Pairing Community Data Collection with Scalable NLP through the LiFE Suite* describes a pipeline spanning field collection, data processing and model development.

**Link:** verified ACL Anthology paper landing page. Do not imply that the site's owner independently designed or maintains every component of the LiFE Suite.

### P6. Community-led orthography work in North-East India — HOLD

**Type:** Collaborative programme development / prospective implementation  
**Period:** 2026  
**Role:** Research design, training, and methods collaboration (subject to final confirmation)  
**Collaborators discussed:** IGNCA, RIWATCH/RCML, CoDIN and technical partners

> Collaborative work exploring informed, community-led choices in orthography development. The approach considers linguistic representation, learnability, community preferences, education, and digital usability, with documentation and consultation as part of the process.

**Hold from launch** unless the parties authorise a public project description and the final project status, scope, contract arrangements, role and partner attribution are confirmed. This is deliberately **not** described as an awarded or completed project.

### Other work for later editorial consideration — HOLD

Toda micro-courses and other proposed training certificates; BoLINet dataset-scale assertions; unpublished working papers; future IGNCA project targets; archive inventories and community knowledge-holder lists. Do not automatically publish operational plans, budgets, unpublished datasets, sensitive records, or collaborator names from private work discussions.

## IV.5 Publications — migration-complete master ledger

**Rules:** Preserve *all* bibliography entries from the current homepage, correct known omissions, do not turn conference proceedings into peer-reviewed journal publications, and do not fabricate missing DOIs, publisher URLs or PDFs. The following is edited for clarity while keeping original bibliographic substance. Copy the raw original citations into `content/legacy-publications.md` or an equivalent audit record for comparison.

### Books

**B01 — 2025 — READY**  
Narayanan, R. Karthick. *Multilinguality, Vitality, and Endangerment: Insights from the Lived Experiences of Multilingual India*. Cambridge Scholars Publishing, 2025. ISBN (hardback): 978-1-0364-5464-7; ISBN (eBook): 978-1-0364-5465-4.  
Source: https://www.vitalsource.com/in/products/multilinguality-vitality-and-endangerment-r-karthick-narayanan-v9781036454654 and publisher catalogue.

**B02 — 2017 — CHECK exact title-page author spelling/transliteration**  
Narayanan, R. Karthick, and Vasamalli K. *Maarum Ulagil Maraiyaa Oligal Thodar Vaimozhi Ilakkiyathin Oru Thoguppu* [English rendering: *Enduring Voices in the Changing Times: A Collection of Toda Oral Literature*]. Sahitya Akademi, New Delhi, 2017. ISBN 978-81-260-5344-5.  
Source: current `index.html`. Retain original title and attribution until title-page verified.

### Journal articles

**J01 — 2022 — READY**  
Narayanan, R. Karthick, and Meiraba Takhellambam. “A Collaboratory Model for Creation of Digital Language Archives in India.” *The Electronic Library* 40, no. 5 (2022): 594–606. https://doi.org/10.1108/EL-02-2022-0030.

**J02 — 2021 — CHECK author-list parsing**  
Shankar Narayanan, Aravind Illa, Nayan Anand, R. Karthick Narayanan, Ganesh Sinisetty, and Prasanta Kumar Ghosh. “An Acoustic Investigation on the Effect of Speaking Rate on Vowel Space and Coarticulation in Toda VCV Sequences.” *Sadhana* 46 (2021). https://doi.org/10.1007/s12046-021-01639-8.  
The current source has inconsistent comma/author delimiters. Verify with publisher DOI before finalising full author names and article number.

**J03 — 2020 — READY**  
Narayanan, R. Karthick. “Made in India: SiDHELA, India’s First Endangered Language Archive.” *DESIDOC Journal of Library and Information Technology* 40, no. 5 (2020): 292–299. https://doi.org/10.14429/djlit.40.05.16349.

**J04 — 2020 — CHECK first author/full official spelling**  
Hima, Ktien, and R. Karthick Narayanan. “Rokdung (Sikkim, India) Language Contexts.” *Language Documentation and Description* 19 (2020): 66–78. http://www.elpublishing.org/PID/209.  
Preserve exact published author order/spelling from journal, not guess from the current site's punctuation.

**J05 — 2019 — READY**  
Narayanan, R. Karthick. “Assessing Language Endangerment: A Methodological Review.” *Language in India* 19, no. 7 (2019): 128–145.

### Book chapter

**C01 — 2022 — READY / CHECK title punctuation**  
Narayanan, R. Karthick. “Tradition vs Aspiration: Gender Differences and Language Shift.” In *Linguistic Diversity in South and Southeast Asia*, edited by Anvita Abbi and Kapila Vatsyayan, 203–216. Primus Books, 2022. ISBN 978-93-91144-18-0.

### Conference proceedings / workshop papers

**P01 — 2025 — READY**  
Narayanan, R. Karthick, Siddharth Singh, Saurabh Singh, Aryan Mathur, Ritesh Kumar, Shyam Ratan, Bornini Lahiri, Benu Pareek, Neerav Mathur, Amalesh Gope, Meiraba Takhellambam, and Yogesh Dawer. “Field to Model: Pairing Community Data Collection with Scalable NLP through the LiFE Suite.” In *Proceedings of the Fourth Workshop on NLP Applications to Field Linguistics*, 76–84. Association for Computational Linguistics, 2025.  
Source: ACL Anthology workshop proceedings and https://unreal-tece.co.in/announcements. **Codex: resolve direct ACL paper page; preserve official author order.**

**P02 — 2024 — CHECK proceedings title/details**  
Narayanan, R. Karthick. “Orality and Language Vitality.” In *Endangered Languages and Oral Traditions: FEL XXVIII*, 58–63, 2024.  
Use existing source and confirm official proceedings bibliographic form before posting an external link.

**P03 — 2022 — CHECK editor and proceedings details**  
Narayanan, R. Karthick. “Traditional Religious-Cultural Practices & Reversing Language Shift among the Todas of Nilgiri.” In *Community Ownership of Language Education for Endangered Language Revitalisation*, 1–11, 2022.  
Source lists a longer editor set; restore exactly after checking the published proceedings, rather than truncate a reference deceptively.

**P04 — 2021 — CHECK publication status and pages**  
Narayanan, R. Karthick, and Meiraba Takhellambam. “Emerging Role of Libraries in Language Archiving in India: A Case Study of SiDHELA.” In *Proceedings of the International Workshop on Digital Language Archives: LangArc 2021*, edited by Oksana L. Zavalina and Shobhana L. Chelliah, 5–7, 2021.

**P05 — 2019 — CHECK official proceedings metadata**  
Shankar Narayanan, Aravind Illa, Nayan Anand, R. Karthick Narayanan, Ganesh Sinisetty, and Prasanta Kumar Ghosh. “An Acoustic-Articulatory Database of VCV Sequences and Words in Toda at Different Speaking Rates.” In *Proceedings of the 22nd Conference of the Oriental COCOSDA*, 1–6, 2019.

### Reports and archival outputs

**R01 — 2016 — CHECK full authors/institutional naming**  
Kidwai, A., B. Tinkari, M. Takhellambam, O. Bhalla, R. Karthick Narayanan, S. Metha, and V. Sharma. *Rongpo Sketch Grammar*. Research report, Scheme for Protection and Preservation of Endangered Languages, Central Institute of Indian Languages, Mysuru, 2016.

**R02 — 2016 — CHECK full authors/institutional naming**  
Kidwai, A., B. Tinkari, M. Takhellambam, O. Bhalla, R. Karthick Narayanan, S. Metha, and V. Sharma. *Rongpo Dictionary*. Research report, Scheme for Protection and Preservation of Endangered Languages, Central Institute of Indian Languages, Mysuru, 2016.

**R03 — 2016 — CHECK full authors/institutional naming**  
Kidwai, A., B. Tinkari, R. Karthick Narayanan, and S. Metha. *Rongpo Narrations, Songs and Stories*. Research report, Scheme for Protection and Preservation of Endangered Languages, Central Institute of Indian Languages, Mysuru, 2016.

**Total master entries:** 2 books + 5 journal articles + 1 chapter + 5 workshop/conference entries + 3 reports = **16 entries**. Existing home contains **14 entries** (1 + 5 + 1 + 4 + 3); two additions are the 2025 monograph and 2025 LiFE Suite publication. Do not accidentally omit either original material or confirmed new works.

### Additional publication reconciliation — HOLD

Older `O-index.htm` mentions works “in preparation,” including other chapters/articles, and the README says a monograph was still being prepared. Do not label any such work published without external verification or an updated publication list. Old profile mentions invited talks and grants; migrate to an optional **Talks & service** section only after verifying relevance and chronology. Do not import an old “in preparation” label as if it describes the present.

## IV.6 Contact — READY

**Heading:** Contact  
**Body:**

> For academic correspondence, research discussions, or enquiries about potential collaborations, please get in touch by email.

**Primary contact:** [karthick.narayanan@outlook.in](mailto:karthick.narayanan@outlook.in)

**Optional links:** CoDIN organisational site, Google Scholar profile, GitHub profile and ORCID, **only where the exact URLs are verified**. No dummy anchors.

## IV.7 SEO and social snippets — READY

- **Home title:** `R. Karthick Narayanan | Linguist & Digital Archivist`
- **Home meta description:** `Research in multilingualism, language vitality, documentation and community-centred digital archiving by linguist R. Karthick Narayanan.`
- **Research title:** `Research | R. Karthick Narayanan`
- **Research description:** `Research on multilingualism, language endangerment, verbal art, digital archiving and community-centred language resources.`
- **Projects title:** `Projects & Archives | R. Karthick Narayanan`
- **Publications title:** `Publications | R. Karthick Narayanan`
- **About title:** `About & CV | R. Karthick Narayanan`
- **Contact title:** `Contact | R. Karthick Narayanan`

Canonical home URL: `https://rkarthick-narayanan.github.io/rkn/`. For subpages, use fully qualified URLs at the same `/rkn/` base. Add OpenGraph title/description and a preview image **only if an owned image is available**. JSON-LD `Person` may include name, description, education, and published `sameAs` links only when verified; do not manufacture profile identifiers.

---

# Part V — Codex implementation instructions

## V.1 Repository operations / safety

1. Read this file and the source tree before writing code.
2. Checkout `main` and confirm it is the starting point; create `redesign-v2` from the latest intended baseline. Check for an existing branch with that name before creating it (do not overwrite existing work).
3. Commit all redesign work only on the new branch. Do not change GitHub Pages deployment configuration or `main`.
4. Keep originals retrievable via Git history, and if moving legacy files, document the mapping in `MIGRATION.md`.
5. Make one or more focused commits; provide a PR with before/after screenshots (if browser is available), a changeset summary, known review items, and link-check/testing results.
6. Do not claim that the new design has been deployed until the user has actually approved a merge and GitHub Pages has successfully published.

## V.2 Suggested structure (adapt if a simpler static structure works better)

```text
rkn/
├── index.html
├── research.html
├── projects.html
├── publications.html
├── about.html
├── contact.html
├── education.html           # legacy compatibility landing/redirect
├── experience.html          # legacy compatibility landing/redirect
├── assets/
│   ├── css/
│   │   └── site.css
│   ├── js/
│   │   └── navigation.js    # only if truly needed
│   └── images/
│       └── [verified and licensed assets only]
├── content/
│   ├── editorial-status.md # internal READY/CHECK/HOLD ledger
│   └── legacy-publications.md
├── README.md
└── MIGRATION.md
```

Do not copy old broken standalone pages verbatim, do not leave multiple stylesheets competing, and do not include dead template links.

## V.3 Build requirements

- Semantic HTML5 with correct heading hierarchy and landmark regions; one H1 per page.
- No inline onclick attributes; menu script should only handle the navigation state.
- Primary navigation supports keyboard, touch, and mouse; `aria-current="page"` on active link.
- Accessible focus-visible style; skip-to-content link; meaningful image alt text; language tagging for Tamil; no emoji-only controls.
- Validate HTML structure (or run equivalent automated markup checks).
- CSS variables for design tokens; consolidated layout rules; `box-sizing: border-box` globally.
- URLs work both locally and on GitHub Pages under `/rkn/`. Prefer `href="research.html"`, `href="assets/css/site.css"`, etc.
- Mark external links as such in accessible context if needed; no `target="_blank"` requirement by default.
- No third-party analytics, cookies, marketing widgets or external scripts by default.
- No inaccessible interactive controls; no content loaded exclusively by JavaScript; website remains readable if JS is disabled (except mobile navigation which should have a sensible fallback).
- Support full Tamil glyph rendering, smart quotes, DOI strings, book titles, and long hyphenated academic terms without horizontal overflow.
- Update README with pages, content maintenance steps, staging/PR process and how to preview locally.
- All externally linked DOIs/URLs in publication records must be valid URLs; do not fabricate a DOI if none exists.

## V.4 Build order (explicit)

**Phase 1 — Stabilisation**
- Inspect and inventory original pages, image usage and references.
- Fix malformed markup and unused/orphaned references as part of the new pages.
- Establish site shell, navigation and CSS tokens.

**Phase 2 — Design implementation**
- Build mobile-first header, footer, hero, section components, publications list and project cards.
- Implement responsive breakpoints and a readable editorial grid.

**Phase 3 — Content migration**
- Migrate all 14 original publication entries and add the 2 verified 2025 entries.
- Use the site-ready text in Part IV; respect READY/CHECK/HOLD tags.
- Write project records precisely, distinguishing personal research from collaboration or institutional ownership.
- Retain education and appointment history and existing contact email; reconcile date contradictions rather than silently overwriting.

**Phase 4 — Quality assurance**
- Test desktop/tablet/mobile layouts, accessibility, internal link integrity, static deployment base paths and source metadata.
- Record screenshots and issues in the PR; fix observed defects.
- Inspect all academic claims against their recorded sources; list unresolved CHECK/HOLD items prominently for human review.

## V.5 Acceptance tests — these determine completion

### Layout and browser

- Capture and inspect at least **320×800, 390×844, 768×1024, 1024×768, and 1440×900** (or closest available representative sizes), using browser rendering if available.
- No document-level horizontal scrolling at 320, 390, 768, 1024 or 1440 widths.
- Text does not overlap navigation, fixed/sticky header or footer.
- Menu opens/closes on click and keyboard, Escape closes, state is conveyed to screen readers, focus order is logical.
- Tamil quotation does not become tofu/unrendered glyphs; Tamil letterforms remain legible and correctly grouped.
- Publication titles wrap without breaking card boundaries.

### Functional/accessibility

- All six primary navigation destinations exist and work.
- Legacy `education.html` and `experience.html` have working routes to new about-page sections.
- Homepage has a skip link, correct H1, distinct landmarks and visible keyboard focus.
- Colour contrast meets WCAG AA for normal text; avoid using warm gold as light-background text.
- No broken local assets or invalid nested HTML.
- Check with a browser-based audit (e.g., Lighthouse/axe if available), document results and fix actionable issues; do not invent an audit score.

### Editorial completeness

- The complete **16-entry publication ledger** is represented; older 14 entries are preserved, two confirmed 2025 works added.
- 2025 monograph is featured above the fold or in the first major homepage content segment and appears in Books.
- Current professional identification and doctoral award year are represented accurately.
- Unverified projects are held back or conservatively described, not promoted as funded or completed.
- No invented institutional partnerships, metrics, dates, roles, external profiles or rights to recordings/images.
- READY/CHECK/HOLD editorial statuses are tracked in repository documentation but not exposed as arbitrary public badges.

### Delivery

- Changes exist **only** on `redesign-v2` (or a safely named substitute if that branch already exists).
- A PR against `main` contains summary, screenshots, local preview instructions, test results and unresolved factual checks.
- `main` and the live site have not been altered.
- User approval is required before any merge or deployment change.

## V.6 Final PR checklist / definition of done

- [ ] Existing page/content audit completed and listed in `MIGRATION.md`.
- [ ] New navigation and all six pages complete.
- [ ] Mobile and desktop screenshots captured from actual render.
- [ ] Header/menu keyboard navigation tested.
- [ ] Tamil text and metadata tested.
- [ ] All 16 known publications migrated; no fake links.
- [ ] Existing education/work/teaching materials preserved.
- [ ] Newer project text uses accurate roles and partner attribution.
- [ ] Unresolved dates, names, project statuses and optional social URLs documented.
- [ ] No invalid CSS declaration, duplicate section ID or missing CSS file.
- [ ] No horizontal scroll, broken relative links or missing images.
- [ ] README, MIGRATION and PR review instructions complete.
- [ ] No commit/merge into `main`.

---

# Part VI — Source register and editorial trail

**S01 — Existing published website and original publication list:**  
https://rkarthick-narayanan.github.io/rkn/

**S02 — GitHub repository, `main` (HTML/CSS/README/legacy source):**  
https://github.com/RKarthick-Narayanan/rkn/tree/main

**S03 — 2025 book, publisher catalogue:**  
https://archive.cambridgescholars.com/product-category/social-sciences/language-and-linguistics/page/2/?orderby=date

**S04 — 2025 book ISBN and title:**  
https://www.vitalsource.com/in/products/multilinguality-vitality-and-endangerment-r-karthick-narayanan-v9781036454654

**S05 — 2025 LiFE Suite academic paper (ACL Anthology author/index):**  
https://aclanthology.org/people/bornini-lahiri/unverified/  
Full proceedings: https://aclanthology.org/2025.fieldmatters-1.pdf

**S06 — LiFE Suite paper bibliographic details from collaborating organisation:**  
https://unreal-tece.co.in/announcements

**S07 — Direct DOI records inherited from current website:**  
https://doi.org/10.1108/EL-02-2022-0030  
https://doi.org/10.14429/djlit.40.05.16349  
https://doi.org/10.1007/s12046-021-01639-8

**S08 — Historical identity, roles, research, and project briefs:** prior professional information supplied in conversation and earlier CV/project discussions. These are treated as *user-provided working records* rather than public scholarly citations. For conflicting facts, rely on the most recent authoritative CV or documentation, and preserve the ambiguity in the CHECK ledger.

## Editorial decisions made and not made

**Made:** 6-page architecture; horizontal navigation; static technology; restrained colour palette; typography; responsive thresholds; research-first content; full bibliography categories; proposed ready copy; staging-branch workflow.

**Not made:** no claim that the user personally owns archives or community datasets; no publication of sensitive oral histories; no guessed portrait, logo licence, ORCID, Scholar URL, project budget, impact number or signed grant; no assumption that older fellowship or employer dates are correct where inconsistent; no live deployment.

---

# Copy-ready Codex handoff prompt

> You are redesigning a scholarly personal website at `RKarthick-Narayanan/rkn` on GitHub Pages. Read the entire `RKN_Website_Redesign_Design_and_Codex_Handoff.md` specification before editing code. Work on a new branch `redesign-v2` from `main`; if already present, do not overwrite it and choose a safe branch variant. Implement the six-page static site, scholarly editorial design system, ready-to-publish copy, content hierarchy, comprehensive 16-entry publication ledger, responsive and accessible navigation, legacy link compatibility, and editorial fact-check ledger as specified. Preserve the existing public site and all academic data. Do not publish HOLD material as completed work or fabricate names, dates, metrics, DOIs, photographs, links, partnerships or project status. Use HTML/CSS/only minimal JS. Keep all paths compatible with GitHub Pages `/rkn/`. Verify desktop/mobile layouts with real screenshots, run link and accessibility checks, update README and MIGRATION, and create a PR against `main` containing tests and screenshots. Do not merge or deploy to `main`. Explicitly list any unresolved CHECK/HOLD factual questions in your PR rather than guessing.
