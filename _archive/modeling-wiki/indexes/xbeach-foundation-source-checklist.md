# XBeach Foundation Source Checklist

Date: 2026-04-30

This checklist records the first locally confirmed XBeach source assets that can seed the XBeach lane in `modeling-wiki`.

## Current Local Source Root

Confirmed local source root:
- `/mnt/e/numerical_models/xbeach`

This means XBeach is no longer blocked by total source absence. The next task is controlled ingest, not discovery from zero.

## Confirmed High-Value Local Sources

### P1 — Core Manual Sources

1. XBeach manual (master)
- `/mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_master.pdf`
- `/mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_master.docx`
- why: primary source for solver identity, setup vocabulary, parameter names, outputs, and workflow conventions
- target ingest output:
  - source note
  - `knowledge/methods/xbeach-parameter-glossary-v1.md`
  - `knowledge/methods/xbeach-boundary-and-wave-setup.md`

2. XBeach manual (kingsday)
- `/mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_kingsday.pdf`
- `/mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_kingsday.docx`
- why: may preserve variant explanations, examples, or wording useful for parameter and workflow clarification
- target ingest output:
  - source note
  - comparison against master manual if terminology differs

3. Local markdown manual stub
- `/mnt/e/numerical_models/xbeach/XBEACH_MANUAL.md`
- why: quick-entry local note that may expose how the local environment currently frames XBeach usage
- target ingest output:
  - one source note
  - list of local assumptions or shortcuts worth preserving separately from official docs

### P1 — Setup / Build / Interface Sources

4. Linux cluster install tutorial
- `/mnt/e/numerical_models/xbeach/src/config/Tutorial_installing_XBeach_on_Linux_cluster.docx`
- why: useful if runtime/build issues become part of the lane
- target ingest output:
  - source note
  - optional future playbook if operational setup becomes a bottleneck

5. Decision tree document
- `/mnt/e/numerical_models/xbeach/src/doc/misc/DecisionTreeXBeach.docx`
- why: likely useful for solver mode or workflow branching decisions
- target ingest output:
  - source note
  - candidate heuristic or method note on choosing XBeach mode/case framing

### P2 — Code / Library / Test Sources

6. Main source tree
- `/mnt/e/numerical_models/xbeach/src/src/xbeach/`
- why: useful for exact parameter names, output artifacts, and implementation-backed terminology when manual wording is ambiguous
- target ingest output:
  - targeted code source note, not full raw-code digestion at once

7. XBeach library source tree
- `/mnt/e/numerical_models/xbeach/src/src/xbeachlibrary/`
- why: useful if API/library embedding becomes relevant later
- target ingest output:
  - deferred unless library mode becomes an active need

8. Local executable path
- `/mnt/e/numerical_models/xbeach/bin/xbeach_IFX.exe`
- why: confirms runnable local installation exists
- target ingest output:
  - local runtime note later, if experiments start

## Recommended First Ingest Order

1. `XBeach_manual_master.pdf`
2. `XBEACH_MANUAL.md`
3. `DecisionTreeXBeach.docx`
4. one carefully chosen code/source-tree note for exact parameter naming

## Expected First XBeach Foundation Outputs

After the first ingest round, create:
- `knowledge/methods/xbeach-parameter-glossary-v1.md`
- `knowledge/methods/xbeach-boundary-and-wave-setup.md`
- `knowledge/methods/xbeach-morphology-foundation.md`

## Not Yet Confirmed

Still not confirmed from current inspection:
- local XBeach case-study folders with trusted observations
- locally curated erosion validation examples
- local experiment records already captured in modeling-wiki style

## Working Rule

Do not start XBeach promoted knowledge from vague memory alone. Start from the confirmed local manual set above, then move to a first source note and one narrow baseline theme.
