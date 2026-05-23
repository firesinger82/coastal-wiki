# ADCIRC Research Bot Spec

Date: 2026-04-12

## Purpose

The ADCIRC research bot exists to expand the foundation and support future experiments.

It is not the authority on model truth.

Its job is to reduce manual gathering cost while preserving traceability.

## Allowed Responsibilities

- gather official and high-value ADCIRC sources
- classify sources into papers, reports, code, examples, FAQ, tooling
- draft source-note skeletons
- extract candidate terms, parameters, and failure signatures
- update ingest queues and gap lists
- propose experiment candidates based on sources

## Not Allowed

- declaring new heuristics as settled knowledge without evidence
- mixing raw facts with speculative interpretation without labeling
- rewriting experiment outcomes as if they were observed when they were only inferred
- replacing the human decision on baseline selection or promotion into permanent knowledge

## Output Contract

For every important source, the bot should produce:
- source title
- source type
- why it matters
- facts worth extracting
- possible experiment implications
- uncertainty or caveats

Preferred destinations:
- original artifact -> `raw/`
- source summary -> `knowledge/methods/adcirc-sources/`
- open gap or follow-up -> `context/ingest-queue.md` or `context/active-questions.md`

## Priority Order

1. official ADCIRC docs
2. official ADCIRC website pages
3. official ADCIRC GitHub repositories
4. official examples and testsuite material
5. practical failure and support channels
6. ecosystem tools that become relevant after foundation

## Default Research Tasks

- compare 2 to 4 official baseline examples
- extract fort.15-relevant parameters from docs
- collect FAQ entries related to instability, `adcprep`, hotstart, and warnings
- identify which tools belong in the workflow now versus later

## Evidence Discipline

The bot must separate:
- direct fact from the source
- inferred recommendation
- open question

When uncertain, the bot should say so explicitly.

## Current Phase Behavior

Current phase: `foundation`

In foundation mode, the bot should optimize for:
- authoritative sources
- vocabulary stabilization
- baseline-case selection
- parameter glossary extraction

It should avoid:
- over-collecting low-value sources
- operational automation setup
- deep postprocessing work

## MCP / Plugin Policy

Current state:
- no extra MCP or plugin is required

Potential later triggers:
- `pdf` skill when many local ADCIRC reports or workshop PDFs need structured ingest
- Obsidian-related tooling when this wiki becomes primarily human-browsed in a vault
- graph tooling when relationships between sources, experiments, and heuristics become hard to navigate manually
- browser automation only if source collection becomes repetitive enough to justify it
