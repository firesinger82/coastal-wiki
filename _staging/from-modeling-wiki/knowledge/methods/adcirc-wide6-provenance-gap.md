# ADCIRC wide6 Provenance Gap

Date: 2026-04-13

Purpose:
- state the real risk in the current `wide6` branch
- distinguish mesh quality questions from provenance and reproducibility questions

## Core Problem

The main problem with `wide6` is not:
- that the retained `fort.14` is obviously broken

The main problem is:
- `wide6` was improved through many iterative edits, manual interventions, and agent-assisted corrections
- the full sequence is not frozen
- therefore the branch is not currently reproducible

## Why This Matters

If the generation history is not reproducible:
- we cannot tell which intervention actually improved the mesh
- we cannot fairly compare `oceanmesh`, `OCSMesh`, or any other tool against `wide6`
- we cannot safely modify `wide6` because we do not know which steps are essential
- we risk copying accidental artifacts instead of real improvements

## Current Interpretation Of `wide6`

Right now `wide6` should be treated as:
- a retained artifact with some strong evidence
- a candidate reference
- a partially explainable result

It should **not** be treated as:
- a replayable workflow
- a clean baseline recipe
- a trustworthy gold standard

## What Is Missing

The missing asset is not another mesh.

The missing asset is:
- a reconstruction of the generation history

That reconstruction needs to answer:
- which files were source inputs
- which files were intermediate edits
- which scripts were actually used
- which GUI/manual steps were essential
- which edits were one-off experiments and later abandoned
- which final artifacts correspond to the accepted branch

## Working Rule

Until the provenance gap is reduced:
- do not optimize `wide6` further
- do not ask Python tools to match `wide6` exactly
- do not interpret every retained script as part of the final pipeline

## Immediate Goal

The immediate goal is:
- build a `wide6 replay candidate` document

That document should contain only:
- confirmed inputs
- confirmed scripts
- confirmed manual steps
- unresolved steps marked explicitly as unknown

## Decision

For now the highest-value task is:
- provenance reconstruction before further mesh improvement
