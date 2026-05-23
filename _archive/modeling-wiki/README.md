# Modeling Wiki

This workspace is for building durable know-how from numerical modeling work.

The priority is not to collect papers. The priority is to preserve:
- what failed
- under which conditions it failed
- what changed
- what improved
- what can be reused later

## Structure

- `raw/`: original source materials only
- `experiments/`: run-by-run records of trial and error
- `knowledge/`: promoted lessons that survived repeated use
- `context/`: current focus, open questions, and working state
- `protocols/`: operational rules for ingest, experiments, and promotion
- `indexes/`: lightweight maps of what exists and what is missing
- `templates/`: note templates for consistent capture
- `graphify-out/`: generated graph artifacts

## Core Rules

1. Do not mix raw source material with AI-generated summaries.
2. Do not write a heuristic unless it is backed by at least one experiment.
3. Every experiment record must include conditions, symptoms, actions, and outcome.
4. Treat "negative results" as first-class assets.
5. Promote stable patterns from `experiments/` into `knowledge/`.

## Recommended Workflow

1. Read `protocols/taxonomy.md`.
2. Add items to `context/ingest-queue.md`.
3. Ingest a source into `raw/`.
4. Create a source note from `templates/source-note.md`.
5. Define a small experiment using `protocols/experiment-protocol.md`.
6. Run an experiment and record it from `templates/experiment-card.md`.
7. When the same pattern repeats, promote it into:
   - `knowledge/failure-patterns/`
   - `knowledge/heuristics/`
   - `knowledge/playbooks/`
8. Periodically update `context/CONTEXT.md` and `context/active-questions.md`.

## Naming Conventions

- Experiment files: `YYYY-MM-DD-short-title.md`
- Source notes: `YYYY-MM-DD-source-title.md`
- Heuristics: `topic-short-rule.md`
- Failure patterns: `symptom-cause-pattern.md`
- Playbooks: `task-or-problem-type.md`

## Suggested First Steps

1. Lock the taxonomy and operating rules in `protocols/`.
2. Pick one modeling theme and add 3 to 5 foundational sources into `raw/`.
3. Write one source note per important source.
4. Define one minimum viable experiment and run it under the new structure.
5. Run `graphify` only after there is enough real material to connect.
