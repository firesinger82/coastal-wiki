# Ingest Queue

Track which sources should be ingested next.

## Priority Queue

- priority: P1
  item: XBeach official manual set and local manual notes
  source type: manual / official docs / local note
  why now: XBeach foundation is currently blocked by source ingest, not by structure design
  target folder: raw/reports/xbeach
  expected output: source notes plus `knowledge/methods/xbeach-parameter-glossary-v1.md` and `knowledge/methods/xbeach-boundary-and-wave-setup.md`
  candidate paths:
    - /mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_master.pdf
    - /mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_kingsday.pdf
    - /mnt/e/numerical_models/xbeach/XBEACH_MANUAL.md

- priority: P1
  item: XBeach decision and mode-selection material
  source type: report / misc doc
  why now: needed before choosing the first XBeach baseline theme and validation framing
  target folder: raw/reports/xbeach
  expected output: 1 source note and candidate heuristics for when and how to use XBeach modes
  candidate paths:
    - /mnt/e/numerical_models/xbeach/src/doc/misc/DecisionTreeXBeach.docx

- priority: P2
  item: XBeach source-tree note for exact parameter names and output artifacts
  source type: code
  why now: useful after the first manual note to resolve exact terminology and file naming
  target folder: raw/code/xbeach
  expected output: 1 focused source note, not a full-code sweep
  candidate paths:
    - /mnt/e/numerical_models/xbeach/src/src/xbeach/
    - /mnt/e/numerical_models/xbeach/src/src/xbeachlibrary/

- priority: P1
  item: ADCIRC preprocessing docs for mesh tools, fort.14, bathymetry, boundaries, and forcing
  source type: manual / official docs
  why now: preprocessing is the actual first bottleneck before project-specific experiments
  target folder: raw/reports/adcirc
  expected output: source notes plus method notes for mesh-tool choice, bathymetry path, and forcing path

- priority: P1
  item: ADCIRC core documentation and user-facing reference material
  source type: manual / official docs
  why now: needed to anchor terminology, inputs, outputs, and baseline workflow
  target folder: raw/reports/adcirc
  expected output: 1 source note plus a list of key setup terms and file artifacts

- priority: P1
  item: ADCIRC governing equations and numerical formulation references
  source type: paper
  why now: needed to understand what should count as a numerical issue versus a setup issue
  target folder: raw/papers/adcirc
  expected output: 1 to 2 source notes with assumptions, stability-relevant details, and diagnostics

- priority: P1
  item: ADCIRC validation or benchmark examples close to intended use
  source type: report / example
  why now: needed to avoid building experiment logic without a reference behavior
  target folder: raw/examples/adcirc
  expected output: 1 source note and a list of candidate baseline cases

- priority: P2
  item: ADCIRC example input files and public example repositories
  source type: code / example
  why now: needed to map theory into runnable setup artifacts
  target folder: raw/code/adcirc
  expected output: 1 source note and a checklist of reusable config pieces

- priority: P2
  item: ADCIRC troubleshooting material, issue threads, and failure discussions
  source type: report / forum / issue
  why now: needed to seed future failure-pattern notes with realistic symptoms
  target folder: raw/reports/adcirc
  expected output: 1 source note with recurring failure signatures and likely checks

## Done Recently

- item: ADCIRC selected as the first active model
  date: 2026-04-12
  linked source note: none

- item: ADCIRC foundation source sweep completed across docs, repo, examples, support, and tooling
  date: 2026-04-12
  linked source note: knowledge/methods/adcirc-sources

- item: storm-surge topic foundation started
  date: 2026-04-12
  linked source note: knowledge/methods/adcirc-storm-surge-foundation.md

- item: local JMA-MSM plus NWS13 workflow captured as the dominant storm-surge path
  date: 2026-04-12
  linked source note: knowledge/methods/adcirc-jma-msm-nws13-foundation.md

- item: ADCIRC preprocessing foundation notes started for mesh, bathymetry, and forcing
  date: 2026-04-12
  linked source note: knowledge/methods/adcirc-preprocessing-foundation.md
