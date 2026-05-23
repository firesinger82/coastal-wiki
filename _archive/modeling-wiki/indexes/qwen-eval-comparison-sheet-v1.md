# Qwen Eval Comparison Sheet V1

Date: 2026-04-30

Use this sheet after both runs are available.

Models to compare:
- fast:
- quality:

Eval source:
- `indexes/qwen-domain-eval-set-v1.md`

## Summary Table

| Section | Fast total | Quality total | Delta | Notes |
|---|---:|---:|---:|---|
| EFDC (5 q) |  |  |  |  |
| XBeach (5 q) |  |  |  |  |
| Failure / Cross (5 q) |  |  |  |  |
| Overall (15 q) |  |  |  |  |

## Question-by-Question Comparison

| ID | Fast | Quality | Delta | Main failure type |
|---|---:|---:|---:|---|
| EFDC-01 |  |  |  |  |
| EFDC-02 |  |  |  |  |
| EFDC-03 |  |  |  |  |
| EFDC-04 |  |  |  |  |
| EFDC-05 |  |  |  |  |
| XBEACH-01 |  |  |  |  |
| XBEACH-02 |  |  |  |  |
| XBEACH-03 |  |  |  |  |
| XBEACH-04 |  |  |  |  |
| XBEACH-05 |  |  |  |  |
| FP-01 |  |  |  |  |
| FP-02 |  |  |  |  |
| FP-03 |  |  |  |  |
| FP-04 |  |  |  |  |
| FP-05 |  |  |  |  |

## Failure-Type Legend

Use one or more of:
- retrieval-wrong-layer
- retrieval-missed-doc
- weak-structure
- weak-procedure-order
- weak-evidence
- hallucinated-term
- weak-uncertainty
- weak-next-action

## Weakness-Axis Rollup

### Fast model recurring misses
- 
- 
- 

### Quality model recurring misses
- 
- 
- 

### Shared misses
- 
- 
- 

## Decision Rules

1. If both fast and quality miss the same question type:
   - fix retrieval or source coverage first
2. If quality wins mainly on structure but not evidence:
   - freeze answer template next
3. If quality wins mainly on exact terminology:
   - push glossary/source-note retrieval earlier for those query classes
4. If fast is close to quality on some section:
   - keep fast for that section to save latency/cost

## Next Fix Queue

1. 
2. 
3. 
