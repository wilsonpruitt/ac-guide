---
title: Making a motion
order: 20
summary: What to say when you want to speak, change, pause, or object — and whether it needs a second, is debatable, or takes two-thirds.
rulesRefs: ["19", "22"]
updated: 2026-01-01
---

The scariest moment for a new delegate is wanting to *do* something and not knowing how.
Conference business runs on a small set of motions, each with its own rules: does it need
a **second**, is it **debatable**, can it be **amended**, and what **vote** carries it.

The data for an interactive "what do you want to do?" helper lives in
`src/data/motions.yaml` (loaded as the `motions` collection). Building the helper UI is a
Phase-1 TODO — see HANDOFF.

Order of precedence matters: when one motion is pending, those that outrank it are in
order and those below it are not. Speeches are limited to three minutes (Rule 22), and the
order of authority is the Book of Discipline, then the Standing Rules, then special rules,
then Robert's Rules (Rule 19).
