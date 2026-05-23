# ADCIRC Foundation Research Spec

Date: 2026-04-12

## Objective

Build the ADCIRC foundation layer before accumulating new trial-and-error records.

The foundation phase should answer four questions:
- what is the authoritative current documentation path?
- what is the minimum file and parameter vocabulary we must standardize?
- what is the best first baseline example?
- which support and tooling channels matter later, but should not be added too early?

## Scope

This spec covers only the foundation phase for ADCIRC.

It does not yet cover:
- local installation
- first experiment execution
- postprocessing recipes
- validation against observations
- automation of repeated production runs

## Source Selection Rules

Prioritize:
- official ADCIRC docs
- official ADCIRC website pages
- official ADCIRC GitHub repositories
- direct example and testsuite material
- support/troubleshooting sources with concrete failure signatures

Deprioritize for now:
- generic blog posts
- third-party summaries without direct links to official sources
- advanced automation tooling that hides core model mechanics

## Current Source Set

Primary sources collected:
- docs hub: https://adcirc.github.io/adcirc/
- getting started: https://adcirc.github.io/adcirc/getting_started/index.html
- theory page: https://adcirc.github.io/adcirc/theory/index.html
- theory PDF: https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf
- input files: https://adcirc.github.io/adcirc/technical_reference/input_files/index.html
- parameter definitions: https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html
- examples index: https://adcirc.github.io/adcirc/user_guide/examples/index.html
- official example problems: https://adcirc.org/home/documentation/example-problems/
- support page: https://adcirc.github.io/adcirc/questions_and_support/index.html
- FAQ: https://adcirc.org/home/adcirc-faq/
- core repo: https://github.com/adcirc/adcirc
- releases: https://github.com/adcirc/adcirc/releases
- testsuite: https://github.com/adcirc/adcirc-testsuite
- tools page: https://adcirc.github.io/adcirc/tools/index.html
- ADCIRCpy: https://github.com/oceanmodeling/adcircpy
- ASGS operators guide: https://github-wiki-see.page/m/StormSurgeLive/asgs/wiki/ASGS-Operators-Guide

Detailed source notes live in:
- `knowledge/methods/adcirc-sources/`

Local clones now present:
- `raw/code/adcirc/adcirc`
- `raw/code/adcirc/adcirc-testsuite`

Current caveat:
- git metadata inspection from the sandbox is blocked by Git safe-directory ownership checks, but the cloned file trees are present and usable for read-only inspection

## Key Decisions Made

1. ADCIRC is the first active model.
2. Source-note creation is allowed before downloading local copies of every artifact.
3. The first baseline should come from official examples or the official testsuite, not from a custom mesh.
4. FAQ and support material should seed the first failure-pattern notes.
5. Tooling adoption is staged after baseline understanding, not before it.
6. The core repository and testsuite were cloned locally during the foundation phase.

## MCP And Plugin Policy

Current decision:
- no extra MCP or plugin is required for the foundation research phase

Reason:
- public web sources and the current workspace are sufficient to structure the foundation layer
- adding Obsidian, graph, or automation plugins now would increase surface area before the core ADCIRC vocabulary is stable

Potential later additions:
- PDF-oriented tooling if we start ingesting many local reports and papers
- Obsidian-related tooling if the wiki becomes human-browsed primarily through a vault
- Graph tooling when there are enough source notes, experiments, and promoted heuristics to justify relationship extraction
- ADCIRCpy installation when setup automation becomes the actual bottleneck

## Immediate Next Actions

1. Expand the parameter glossary into a first fort.15 setup checklist.
2. Extract the file anatomy of `adcirc/adcirc_quarterannular-2d-netcdf`.
3. Define the first minimum viable experiment using that baseline case.
4. Download or copy a small set of especially important source artifacts locally if offline use becomes necessary.

## Success Criteria For Foundation Exit

- source catalog exists
- source notes exist for the main official sources
- one baseline example is selected
- one first-pass parameter glossary is written
- local ADCIRC code and testsuite are present
- one minimum viable experiment is defined
