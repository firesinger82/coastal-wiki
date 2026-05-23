# Research Ingest Protocol

The goal of ingest is not volume. The goal is useful foundation.

## What To Ingest First

1. Primary references for the solver or method actually in use.
2. Validation studies close to your geometry or forcing regime.
3. Code examples that expose implementation details.
4. Failure discussions, troubleshooting notes, or issue threads.

## What To Avoid Early

- generic survey material without operational detail
- marketing blog posts
- duplicate summaries of the same primary source
- AI-generated commentary without traceable evidence

## Ingest Procedure

1. Put the original artifact into the correct `raw/` subfolder.
2. Create one source note using `templates/source-note.md`.
3. Extract only the parts that can influence setup, diagnostics, or decisions.
4. Add candidate experiments to `context/ingest-queue.md` or `context/active-questions.md`.

## Minimum Useful Extraction

Every important source note should capture:
- assumptions
- parameter ranges
- numerical constraints
- validation strategy
- failure modes
- implementation details worth testing

## Exit Condition

A source is "ingested enough" when it can directly inform:
- one experiment setup
- one diagnostic check
- or one heuristic candidate
