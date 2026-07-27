# Camm Plastering Contractors Ltd — website

Marketing site for **Camm Plastering Contractors Ltd**, a plastering, drylining and
rendering subcontractor established over 30 years, based in Worksop, covering South
Yorkshire, Derbyshire and Nottinghamshire.

**Live preview:** https://cammycodes.github.io/cammPlasteringWebsite/

> Work in progress — the layout and copy are close to final, but the imagery, the logo and
> the client list are still stand-ins. See [Outstanding items](#outstanding-items).

---

## What's in here

| Path | What it is |
| --- | --- |
| `Camm Plastering Website v2.dc.html` | **Current design.** The source of truth for the site. |
| `Camm Plastering Website.dc.html` | First iteration, kept for reference. Not deployed. |
| `index.html` | **Generated** by `build.mjs` from the v2 source. This is what GitHub Pages serves. |
| `build.mjs` | The generator. No dependencies. |
| `support.js` | `dc-runtime` — renders the `.dc.html` format in the browser. Generated file, do not edit. |
| `image-slot.js` | The `<image-slot>` custom element used for the photo placeholders. |
| `assets/` | Site images (currently just the logo). |
| `uploads/`, `scraps/` | Working files from the design process. Not used by the site. |

## Running it locally

Any static file server over the repo root works — the page fetches `support.js` and
`assets/` relative to itself, so opening `index.html` via `file://` will not work.

```bash
node build.mjs && python -m http.server 4173
```

Then open <http://localhost:4173>.

## How the page is built

The `.dc.html` files are **not** plain HTML. They use a small template format that
`support.js` renders client-side:

- Markup lives inside `<x-dc>`; `<helmet>` content is hoisted into `<head>`.
- `{{ expr }}` interpolates, `<sc-for list="{{ items }}" as="x">` loops, `<sc-if value="{{ cond }}">` branches.
- A `<script type="text/x-dc" data-dc-script>` block at the bottom defines
  `class Component extends DCLogic`, whose `renderVals()` returns everything the template
  can reference — the services, sectors and client lists, plus the contact-form state and
  handlers.

`support.js` injects React 18.3.1, ReactDOM and Babel Standalone from unpkg (with SRI
hashes) at runtime, so the page renders on any static host with no build step —
but it **does need those CDN requests to succeed**, and the content is client-rendered,
so search engines see an empty body on first paint.

`build.mjs` produces `index.html` from the v2 source with three changes:

1. Turns off the pink "TO CONFIRM" note bar (an internal review aid — its own copy says it
   shouldn't appear on the live site).
2. Adds a `<title>`, meta description and favicon, which the source doesn't have.
3. Adds a "generated, do not edit" banner.

**Edit the `.dc.html` source, never `index.html`.** Re-run `node build.mjs` and commit both.

## Deployment

GitHub Pages serves the repository root on the `main` branch. Pushing to `main` publishes.
`.nojekyll` is present so Pages copies files through untouched.

## Outstanding items

Carried over from the design notes in the source:

- **Imagery** — the hero and the three service rows currently show *generated flat vector
  illustrations* (`assets/hero.jpg`, `assets/svc-*.jpg`, built by `scraps/generate_svg_assets.js`),
  not photographs. The HTML comment above each `<image-slot>` holds the photo brief that was
  originally intended. Real site photography should replace these.
- **Logo** — `assets/camm-logo.png` is a redrawn wordmark generated from
  `scraps/generate_svg_assets.js`, not the company's actual logo file. **The original is
  preserved at `assets/camm-logo.png.bak`** — restore it with
  `cp assets/camm-logo.png.bak assets/camm-logo.png` if the real mark is wanted.
- **"5,000+ plots completed" is an assumption, not a supplied figure.** It was chosen to sit
  credibly against 30+ years of trading when the client asked for a larger number than the
  previous "500+", but nobody has confirmed it. **It is a public factual claim about a real
  business and needs signing off or replacing.**
- **Client logos** — the static client row shows only the two confirmed logos (Harron Homes,
  Avant Homes). The four "Client TBC" placeholder tiles were removed. To add a client, drop
  the official brand file (transparent PNG or SVG, landscape, ≥400px wide) into
  `assets/clients/` and add an entry to `clientLogos`. These must be the companies' real
  brand files — redrawn versions of someone else's trademark aren't usable.
- **Copy to confirm** — the insurance cover level (the compliance line currently says only
  "fully insured") and the full client list.
- **SEO** — client-side rendering means no server-rendered content. If organic search
  matters, the page should be flattened to static HTML.

## Business details

Camm Plastering Contractors Ltd · Registered in England & Wales, No. 14195073
6c Gander Lane, Barlborough, Chesterfield S43 4PZ · 01909 488694 · cammplastering@gmail.com
