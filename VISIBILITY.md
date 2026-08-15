# Visibility follow up (Phase 2 and 3)

Phase 1 (on repo SEO) is done in the repo. Use this checklist later.

## Hard style rule: no dashes as separators

* List bullets use `*` (not `-`)
* Resource lines use colon only: `* [Name](url): Description.`
* Never use Awesome style ` - ` between the link and the description
* Prefer words or `:` / `>` over em dashes in prose

(GitHub topic tags and the repo name still use hyphens because the platform requires them.)

## Phase 2: Awesome list readiness

Do **not** open a PR to [sindresorhus/awesome](https://github.com/sindresorhus/awesome) until all of these are true:

* [ ] Repo is at least **30 days** old (created 2026-08-09, eligible around 2026-09-08)
* [ ] Sustained maintenance commits (not a one shot dump)
* [ ] Run `npx awesome-lint` and fix findings that do **not** force dash separators (keep colon style)
* [ ] License is **CC0-1.0** only if you want official Awesome listing (current: MIT)
* [ ] `Contents` TOC stays shallow; contributing stays in `contributing.md` (not in TOC)

## Phase 3: External distribution

SEO alone will not beat 4k star competitors. Ship traffic:

* [ ] Twitter/X + LinkedIn launch post: roadmap + weekly verified links + repo URL
* [ ] One value post on Dev.to or r/learnmachinelearning (no spam; explain the path)
* [ ] Keep a pinned “Suggest a resource” issue open for engagement
* [ ] After some stars: ask related lists/directories for a link (backlinks help Google)
* [ ] Optional: GitHub Pages mirror of the README for an extra indexed URL

## Social preview (manual once)

GitHub does not expose a stable public API to set the repo Open Graph image.

1. Open: https://github.com/mohabdelkarim/awesome-ai-resources/settings
2. Scroll to **Social preview** then **Edit**
3. Upload [`assets/social-preview.png`](assets/social-preview.png) (1280×640; SVG source also in `assets/social-preview.svg`)
4. Save. Slack / X / LinkedIn shares will use this card instead of the generic GitHub preview.

## Already done (Phase 1)

* Topics (16), About description, homepage URL
* `contributing.md`, issue + PR templates
* Weekly CI uses `GITHUB_TOKEN`; commits attributed via `GIT_AUTHOR_NAME` / `GIT_AUTHOR_EMAIL`
* README differentiation blurb + Contents TOC fixes
* Author only Cursor rule under `.cursor/rules/`
* Colon style list entries; asterisk bullets (no dash separators)
