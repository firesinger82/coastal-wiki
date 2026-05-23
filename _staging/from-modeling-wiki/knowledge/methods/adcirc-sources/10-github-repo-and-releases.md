# ADCIRC GitHub Repo And Releases

## Metadata

- date: 2026-04-12
- title: GitHub repository and releases
- source type: code
- authors: ADCIRC development group
- year: active repository, latest release surfaced as 2025-11-20
- link: https://github.com/adcirc/adcirc ; https://github.com/adcirc/adcirc/releases
- local path: E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc

## Why This Matters

This is the best reality check for what codebase and version line are alive now.

## Core Claims

- the public repository is active and open source
- the repository states that documentation is being consolidated from the website and wiki into the docs site
- the latest surfaced release is `v56.2.1` on `2025-11-20`, described as a bug-fix release for certain MPI-library behavior
- the repository includes source, build files, docs, utilities, containers, and work directories

## Practical Value

- method details: anchors version awareness before any local build or run
- implementation detail: confirms where build logic and docs live
- validation detail: release notes can explain behavior changes or fixes
- limitations: release notes alone do not replace workflow docs or theory docs

## Relevance Tags

- solver: ADCIRC
- physics: none
- numerics: version awareness
- diagnostics: bug-fix context
- failure mode: version mismatch

## Transferability

High for future local installation, reproduction, and troubleshooting.

## Extraction Targets

- pin a preferred starting release when installation begins
- record version-sensitive behavior in future experiment cards
- inspect the local source tree for work, build, docs, and utility structure

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
