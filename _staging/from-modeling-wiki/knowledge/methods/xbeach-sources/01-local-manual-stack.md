# XBeach Local Manual Stack

## Metadata

- date: 2026-04-30
- title: XBeach local manual stack
- source type: manual
- authors: XBeach / Deltares documentation plus local practical note author(s)
- year: mixed; official docs are active and the local note targets XBeach v1.24 Halloween
- link: https://xbeach.readthedocs.io/en/latest/
- local path:
  - /mnt/e/numerical_models/xbeach/XBEACH_MANUAL.md
  - /mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_master.pdf
  - /mnt/e/numerical_models/xbeach/src/doc/manual/XBeach_manual_kingsday.pdf

## Why This Matters

This is the first confirmed XBeach foundation source set for the modeling wiki. It is enough to start stabilizing vocabulary, hydrodynamic mode selection, parameter naming, and the first boundary/morphology notes without waiting for new external search.

## Core Claims

- XBeach is an open-source hydrodynamic and morphodynamic model originally aimed at storm-scale sandy-coast response on kilometer-scale domains
- the model includes wave transformation, infragravity response, wave-driven setup and currents, overwash/inundation, and sediment-driven morphology change
- XBeach has three main hydrodynamic modes that matter immediately for setup decisions:
  - `wavemodel = stationary`
  - `wavemodel = surfbeat`
  - `wavemodel = nonh`
- local documentation already frames `surfbeat` as the recommended/default practical mode for many storm-impact applications
- morphology-relevant controls and bed-friction options are explicit enough in the local manual note to seed a first glossary

## Practical Value

- method details: gives a compact overview of XBeach physics, mode structure, grid logic, and major process groups
- implementation detail: confirms local executable/runtime existence and gives practical run setup framing through `params.txt`
- validation detail: states that the model has been validated against analytical, laboratory, and field cases using a standard parameter set
- limitations: the local note is practical and dense, but it should still be checked against the official manual pages when exact behavior or parameter nuance matters

## Relevance Tags

- solver: XBeach
- physics: coastal hydrodynamics and morphodynamics
- numerics: mode selection, staggered curvilinear grid, boundary/setup vocabulary
- diagnostics: baseline setup interpretation
- failure mode: none yet

## Transferability

This source set is broadly transferable to future XBeach work in this wiki, especially for:
- choosing the first hydrodynamic mode
- identifying early parameter buckets
- separating hydrodynamic validation from morphology validation
- understanding how local builds and official docs connect

## Extraction Targets

- parameter names and buckets for the first glossary
- boundary-condition and wave-setup concepts for the first methods note
- morphology-sensitive controls and validation vocabulary
- first heuristics on when to use `stationary`, `surfbeat`, or `nonh`

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
