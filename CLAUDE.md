# Capital Sawmill website

Rebuild of capitalsawmill.com for Steven Daniels (Kevin's dad) — tree service + sawmill,
Nassau NY. Built July 2026.

## Structure

- `site/` — the deployed site (Cloudflare Pages output directory). Static HTML, no framework.
- `build.py` — generates every `site/**/index.html` from shared header/footer templates.
  **Edit build.py, not the generated HTML**, then run `python3 build.py` and commit both.
- `site/assets/css/main.css` — all styling. Brand: greens `#0e6b17`/`#063a00`/`#075818`,
  maroon `#780027`. Charred-wood dark bars use `tex/footer-bg.jpg` (fixed-attachment
  parallax on desktop, scroll on mobile). Live-edge plank H2s: `.plank-wrap`/`.plank`
  masked by `assets/img/plank-mask-a.svg` / `-b.svg`, maple texture `tex/h2-bg.jpg`,
  nail heads via ::before/::after.
- `site/assets/js/main.js` — parallax, plank tilt, Leaflet service-area map, form UX.

## Key decisions (from Kevin)

- Nav/header cloned exactly from the old Divi site, minus Landscaping, Blog, Gift Shop.
- 50/50 tree services + sawmill positioning; the differentiator is "we mill YOUR tree
  into lumber you keep" — pushed hard but without deterring single-service customers.
- Phone-first everywhere: (518) 479-0729, sticky mobile call bar. Steve answers his
  phone, not email.
- Header video (`assets/vid/header.mp4`, 960x404) shown at full aspect ratio, never cropped
  on desktop; on mobile the copy drops below the video instead of cropping it.
- Contact form posts to formsubmit.co → Steven@CapitalSawmill.com. NOTE: the first real
  submission triggers a FormSubmit activation email to Steve's inbox that he must click
  once; until then submissions don't deliver.

## Deploy

GitHub repo `foxhousemedia/capital-sawmill` → Cloudflare Pages (git-integrated,
build command: none, output dir: `site`). Push to `main` auto-deploys.

## Original site rip

The old site's full asset/content rip lives only in the July 2026 build session
(pages, Divi CSS, all images). Everything worth keeping was copied into `site/assets/`.
