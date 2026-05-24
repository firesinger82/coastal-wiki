---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/09-support-and-faq.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# ADCIRC Support And FAQ

## Metadata

- date: 2026-04-12
- title: Questions and support plus FAQ
- source type: manual
- authors: ADCIRC development team and Jason Fleming
- year: active docs page plus FAQ last updated 2015-03-27
- link: https://adcirc.github.io/adcirc/questions_and_support/index.html ; https://adcirc.org/home/adcirc-faq/
- local path: not downloaded yet

## Why This Matters

This is the best source for practical failure signatures before we have our own local issue history.

## Core Claims

- the official support channels are the docs site, website, wiki, GitHub issues, FAQ, and the ADCIRC listserv
- the FAQ gives concrete advice for instability, `adcprep` file-handle limits, SWAN coupling file placement, prefix-directory failures, and warning elevation messages
- the listserv is still presented as the primary community support path

## Practical Value

- method details: exposes real setup and runtime problems users actually hit
- implementation detail: seeds the first local failure-pattern notes
- validation detail: shows what symptoms are worth watching in logs and screen output
- limitations: FAQ content is older and should be used with current docs and releases

## Relevance Tags

- solver: ADCIRC
- physics: troubleshooting
- numerics: stability triage
- diagnostics: warnings and runtime errors
- failure mode: instability

## Transferability

Very high. This should directly inform local `failure-pattern` and `playbook` notes.

## Extraction Targets

- first instability triage checklist
- first screen-warning glossary

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
