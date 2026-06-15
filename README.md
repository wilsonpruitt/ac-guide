# Guide to Annual Conference

A community-curated guide to the Río Texas Annual Conference: what each part of the
agenda means, what each body does, and how to take part. It sits *on top of* the
[Río Texas Atlas](https://riotexas.wrootlabs.com) (the numbers) and links down into it.

## Run

```bash
npm install
npm run dev          # http://localhost:4321
npm run seed:agencies  # regenerate src/content/agencies/*.yaml from the Standing Rules
```

## Layout

```
src/
  content.config.ts        # all collection schemas (the content model)
  content/
    agencies/   *.yaml      # Layer A  authoritative spine (generated; edit the seed)
    agenda/     *.md        # Layer B  evergreen explainers, per item of business
    process/    *.md        # Layer B  evergreen explainers, how the body works
    annotations/*.yaml      # Layer C  institutional knowledge, attached to the spine
    questions/  *.yaml      # Layer C  open questions, resolved in place
  data/motions.yaml         # parliamentary helper data
  pages/                    # minimal placeholder routes (design pass deferred)
scripts/seed_agencies.py    # single source of truth for the agency spine
```

See `HANDOFF.md` for what's done, what's next, and the open decisions.
The full rationale is in the design sketch (`AC-Guide-Design-Sketch.md`).
