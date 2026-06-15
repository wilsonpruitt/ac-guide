# HANDOFF — Guide to Annual Conference

For Claude Code. Read alongside the design sketch (`AC-Guide-Design-Sketch.md`), which
carries the full rationale; this file is the build state.

## The model in one breath

Three content layers, kept structurally distinct so each is maintained differently and a
reader can always tell official from community:

- **Layer A — authoritative spine** (`agencies`): conference bodies, from the Standing
  Rules. Generated, not freely edited. Source of truth: `scripts/seed_agencies.py`.
- **Layer B — evergreen explainers** (`agenda`, `process`): written once, lightly
  maintained. *No per-year figures* live here — that's the fix for "the PDF goes stale."
- **Layer C — community knowledge** (`annotations`, `questions`): attached to a spine
  element by `target.ref` (slug, optionally `slug#anchor`). Attributed and dated.

Plus `motions`: the three parliamentary tables flattened for an interactive helper.

## What's seeded

- All collection **schemas** in `src/content.config.ts`.
- **15 agency files** covering the Uniting Table, the four Vision Teams (with sub-bodies),
  the Administrative Agencies, and the Administrative Review Committee — each with BOD
  refs and membership sizes from the rules.
- **Agenda explainers**: Standing Rules, Nominations, Finance (Finance ported as the
  evergreen reference page, figures stripped to per-year markers).
- **Process explainers**: resolutions & deadlines (incl. this year's agency vs. non-agency
  change), making a motion, consent agendas, conference membership.
- **Layer C examples** drawn from the Advocates thread: Rachel's line-F/line-H note
  (annotation on `finance#district-funding`) and Joe's compliance question. These are the
  proof that the join works — the finance page and `/questions` render them.
- **18 motions** in `src/data/motions.yaml`.
- Minimal runnable **routes**: home, agencies (index + detail), agenda (index + detail),
  questions index.

## What's next (Phase 1 finish, then 2–3)

1. **Per-year instances.** The biggest TODO. Add a `years` collection (or a loader) that
   pulls current-year figures from the journal / Atlas and renders into the
   `<!-- per-year instance -->` markers on agenda pages. This is what keeps the guide from
   being re-authored annually.
2. **Parliamentary helper UI.** Build the "what do you want to do?" component over
   `motions` (filter by intent → show say / second / debatable / amendable / vote), plus a
   precedence view using `rank`. Reuse the Wroot Labs motion-tracker schema if it fits.
3. **`process` routes.** Add `/process/[...slug].astro` (mirror the agenda detail page);
   wire the Layer C join for `target.type === 'process'`.
4. **More agenda/agency explainers.** Fill out the remaining recurring items.
5. **Frontend design pass.** Styling here is a deliberate placeholder
   (`public/styles/base.css`); the one idea worth keeping is that spine vs. community
   content look different. Do the real design pass with the frontend-design approach.
6. **Contribution workflow (Phase 3).** The open governance fork — open-publish vs.
   review-queue — is unresolved and gates auth + stack. See design sketch §7/§10. Until
   decided, Layer C files are added by hand to the repo.

## Conventions & notes

- **Slugs** are filenames without extension (the content-layer `id`). Annotation/question
  `target.ref` must match a spine slug, optionally `slug#anchor`; markdown headings get
  GitHub-style anchor ids (e.g. `## District funding` → `district-funding`).
- **Board of Ordained Ministry** is nested under Developing Leaders as a sub-body. It's a
  body delegates seek directly — consider promoting it to its own `type: board` file
  (`parent: developing-leaders`) for findability.
- **Attribution** in the seed uses first names from the thread; swap for handles or real
  names before publishing.
- Targeted Astro **5.x** (content layer / `glob` + `file` loaders, top-level `render()`).
