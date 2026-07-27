# AGENT.md

Guidance for AI coding agents working in this repo. Read this before editing anything.

## What this repo is

A single-page marketing site for Camm Plastering Contractors Ltd. There is no framework, no
package manager, no test suite and no CI. The whole site is one HTML file plus two vendored
runtime scripts.

## The golden rules

1. **`index.html` is generated. Never edit it.** Edit `Camm Plastering Website v2.dc.html`,
   then run `node build.mjs`, then commit both files.
2. **`support.js` and `image-slot.js` are vendored/generated. Never edit them.** `support.js`
   says so on line 1. If something in the runtime is wrong, work around it in the page source.
3. **`Camm Plastering Website.dc.html` (v1) is archived.** Don't update it to match v2 — it's
   kept as a record of the earlier direction.
4. **Don't invent business facts.** Phone numbers, the client list, the founding year,
   insurance cover and accreditations are real-world claims about a real company. If a value
   isn't already in the source, ask — don't fill it in plausibly.

## The `.dc.html` format

Not plain HTML. `support.js` (`dc-runtime`) parses and renders it client-side via React.

```
<x-dc>
  <helmet> ... </helmet>          <!-- hoisted into <head>: fonts, <style>, extra scripts -->
  ... markup ...
</x-dc>
<script type="text/x-dc" data-dc-script data-props="{...json...}">
  class Component extends DCLogic {
    state = { ... };
    renderVals() { return { /* everything {{ }} can reference */ }; }
  }
</script>
```

Template syntax:

| Syntax | Meaning |
| --- | --- |
| `{{ expr }}` | Interpolate a value from `renderVals()`. |
| `<sc-for list="{{ items }}" as="x" hint-placeholder-count="4">` | Loop. The hint is design-tool-only. |
| `<sc-if value="{{ cond }}" hint-placeholder-val="{{ true }}">` | Conditional block. |
| `style-hover="..."` | Hover styles, since everything is inline-styled. |
| `onClick="{{ handler }}"` / `onChange="{{ handler }}"` | Bind to a function from `renderVals()`. |
| `data-props` on the script tag | Declares externally-settable props, with defaults. |

Gotchas:

- All styling is **inline `style` attributes**. There is no stylesheet and no class system.
  Match that — don't introduce CSS classes or a framework. Shared rules, responsive overrides
  and resets go in the `<style>` block inside `<helmet>`; classes exist there purely as
  media-query and shared-rule hooks, never as a general styling system.
- The page is **`content-box`** — there is no `box-sizing` reset, and every dimension was
  tuned that way. Don't add a global `border-box` reset; it would shift the whole layout.
  Two consequences bite repeatedly: never put `width:100%` on a padded element, and give
  grid tracks `minmax(0,1fr)` rather than `1fr` wherever a track holds an `<image-slot>` or
  a form field, both of which impose an intrinsic minimum width that blows the track out.
- Headings are **Source Serif 4**, everything else **Archivo**; the bronze `#b0885a` /
  `#94703f` accent is reserved for hairlines, eyebrows and hover states.
- The runtime pulls React 18.3.1, ReactDOM and Babel Standalone from **unpkg with SRI
  hashes**. Anything that breaks those requests breaks the page. Don't add a CSP.
- Because it's client-rendered, **nothing is in the initial HTML**. Any change justified by
  SEO needs the page flattened to static HTML first — that's a bigger decision, raise it
  rather than half-doing it.

## `<image-slot>`

Image placeholders from `image-slot.js`, designed for the "omelette" design tool: the user
drags an image in and it persists to a sibling `.image-slots.state.json` sidecar. Outside
that tool the slots are read-only — but a `src="..."` attribute on the slot renders fine
anywhere, and that's how the four slots are currently filled.

Every slot needs a unique `id`. Above each one is an HTML comment with the photo brief that
was originally intended for it. To swap an image, save the file into `assets/` and update
the slot's `src`; don't try to pre-seed the sidecar.

The images in there now (`hero.jpg`, `svc-*.jpg`) and `camm-logo.png` are **generated
stand-ins** produced by `scraps/generate_svg_assets.js` and `scraps/convert_svg_to_png.js` —
flat vector illustrations, not photographs, and a redrawn wordmark rather than the company's
real logo (the original is kept at `assets/camm-logo.png.bak`). Treat them as placeholders.
Do not generate stand-ins for *third-party* client logos in the client row — those are other
companies' trademarks and the source explicitly rules that out.

## Content model

Everything list-shaped lives in `renderVals()` at the bottom of the v2 source, not in the
markup: `capabilities`, `sectors`, and `clientLogos`.

`clientLogos` holds only confirmed clients that have supplied an official brand file. It is
rendered as a static row, not a marquee — there are deliberately no "TBC" placeholders, since
placeholder tiles on a live site undercut the established-contractor positioning the copy is
doing. Add a client only when the real logo file exists in `assets/clients/`.

The company does **not** offer screeding, external wall insulation, or coving and mouldings.
These were removed in July 2026 at the client's instruction — don't reintroduce them.

The contact form has no backend. `sendEnquiry` builds a `mailto:` URL and sets
`window.location.href`. Don't add a form endpoint without asking — it changes where a real
business's leads go.

## Build and check

```bash
node build.mjs && python -m http.server 4173
```

`build.mjs` uses `replaceOnce()`, which throws if a pattern it expects doesn't match exactly
once. If the build fails after you edit the source, you changed something the build depends
on — fix the build script to match, don't loosen the check.

There are no tests. Verify by loading <http://localhost:4173>, confirming the page renders,
and checking the browser console is clean.

## Deployment

Pushing to `main` publishes to GitHub Pages from the repository root. There is no staging
environment, so anything merged is live immediately.
