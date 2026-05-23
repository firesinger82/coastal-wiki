# ADCIRC Research Bot Brief

Use this brief when asking an agent or bot to gather ADCIRC material.

## Current Phase

foundation

## Current Objective

Strengthen the ADCIRC foundation without drifting into premature experimentation or automation.

## Active Model

ADCIRC

## Required Output

For each source:
- title
- source type
- link
- why it matters
- 3 to 7 concrete facts
- experiment implications
- uncertainty notes

## Source Priorities

1. official docs
2. official website pages
3. official repositories
4. official examples and testsuite materials
5. FAQ and support materials

## Destination Rules

- raw artifact -> `raw/.../adcirc`
- source note draft -> `knowledge/methods/adcirc-sources/`
- new gap -> `context/active-questions.md`
- new ingestion target -> `context/ingest-queue.md`

## Constraints

- do not invent heuristics
- do not treat recommendations as facts
- do not propose custom meshes yet
- do not recommend tooling unless it clearly reduces a current bottleneck
