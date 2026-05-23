# ADCIRC Plugin And MCP Watchlist

Date: 2026-04-12

## Current Decision

Do not install extra MCP servers or plugins yet.

## Why Not Yet

- the current bottleneck is not access to tools
- the current bottleneck is stabilizing ADCIRC vocabulary, baseline choice, and experiment discipline
- adding more surfaces now would increase coordination cost before enough content exists to justify them

## First Trigger Conditions

Install or configure something new only when one of these becomes true:

1. PDF ingestion becomes frequent enough that manual reading is slowing down source-note creation.
2. Vault browsing becomes the main way you consume this wiki and local note access is clumsy.
3. Relationships between sources, experiments, and heuristics become hard to navigate manually.
4. Repetitive source gathering turns into a real workflow burden.

## Likely Future Candidates

- `pdf` skill
  - use when local workshop decks, manuals, or reports become numerous

- Obsidian-related tooling
  - use when the wiki is primarily navigated as a vault rather than as a plain directory tree

- graph or memory tooling
  - use when the number of source notes and promoted patterns is large enough to justify relationship extraction

- browser automation or scraping support
  - use when repeated source collection from stable sites becomes routine

## ADCIRC-Specific Tooling To Consider Later

- `ADCIRCpy`
  - when setup automation becomes a bottleneck after baseline understanding is stable

- `ASGS`
  - when the workflow shifts from local understanding to repeated operational or forecast-style runs

## Approval Rule

Before adding a new MCP server or plugin, write down:
- current pain point
- expected time saved
- what new complexity it introduces
- what existing manual step it replaces
