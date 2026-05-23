# Qwen Domain Evaluation Set V1

Date: 2026-04-30

Purpose:
- create a small, repeatable benchmark for local Qwen improvements
- measure whether changes to prompt template, retrieval policy, or model routing actually improve answers
- prevent subjective drift like "feels better"

Use this set before and after each major change:
- system prompt/template change
- retrieval priority change
- new promoted knowledge added
- fast/quality routing change

## Scoring Frame

For each question, score 0-2 on each axis:
- correctness
- use of relevant evidence
- practical usefulness
- uncertainty handling

Suggested total per question:
- 0-8

Optional binary checks:
- did it answer the actual question?
- did it cite the right knowledge layer?
- did it avoid hallucinating unsupported parameter names?
- did it recommend a sane next action?

---

## EFDC Questions

### EFDC-01
Question:
In EFDC, if water level matches reasonably well but currents do not, what should be checked before bottom friction tuning?

What a good answer should contain:
- comparison basis
- geometry/bathymetry
- boundary/forcing
- wetting/drying
- friction later, not first

Primary target docs:
- `knowledge/methods/efdc-current-mismatch-diagnosis.md`
- `knowledge/methods/efdc-calibration-foundation.md`
- `knowledge/heuristics/efdc-check-comparison-basis-before-friction-tuning.md`

### EFDC-02
Question:
What is the practical calibration order for an EFDC tidal/coastal model when stage is acceptable but current timing and magnitude are wrong?

What a good answer should contain:
- ordered sequence
- fixed comparison frame
- boundary and wet/dry before heavy friction retuning
- experiment logging mindset

Primary target docs:
- `knowledge/playbooks/efdc-tidal-calibration-order.md`
- `knowledge/methods/efdc-calibration-foundation.md`

### EFDC-03
Question:
How should boundary-condition issues be separated from friction issues in EFDC calibration?

What a good answer should contain:
- open-boundary interpretation
- harmonic vs time-series forcing
- river/freshwater role
- wind/density forcing possibility
- friction only after forcing audit

Primary target docs:
- `knowledge/methods/efdc-boundary-condition-foundation.md`
- `knowledge/playbooks/efdc-boundary-forcing-checklist.md`

### EFDC-04
Question:
What do `ISDRY = 0`, `11`, and `99` mean in EFDC+, and why does this matter for shallow tidal systems?

What a good answer should contain:
- meaning of each mode
- face masking / rewetting distinction
- connectivity interpretation
- relevance to flats, shoals, harbor margins

Primary target docs:
- `knowledge/methods/efdc-wetting-drying-foundation.md`

### EFDC-05
Question:
When should wetting/drying be treated as a likely cause of current mismatch in EFDC?

What a good answer should contain:
- shallow-zone mismatch clues
- connectivity bias logic
- not confusing it with pure friction issue

Primary target docs:
- `knowledge/methods/efdc-wetting-drying-foundation.md`
- `knowledge/failure-patterns/efdc-wetdry-connectivity-bias.md`

---

## XBeach Questions

### XBEACH-01
Question:
What is the difference between `stationary`, `surfbeat`, and `nonh` modes in XBeach, and which one should usually be the first baseline for storm-impact work?

What a good answer should contain:
- mode distinction
- surfbeat as likely default first baseline
- higher cost / narrower need of nonh

Primary target docs:
- `knowledge/methods/xbeach.md`
- `knowledge/methods/xbeach-parameter-glossary-v1.md`

### XBEACH-02
Question:
Why must XBeach boundary setup be described together with `wavemodel` rather than separately?

What a good answer should contain:
- boundary logic depends on mode
- stationary vs surfbeat/nonh differences
- reproducibility requires both

Primary target docs:
- `knowledge/methods/xbeach-boundary-and-wave-setup.md`

### XBEACH-03
Question:
What are the main wave boundary families currently documented in the local XBeach setup?

What a good answer should contain:
- `wbctype = parametric`
- `wbctype = jonstable`
- `wbctype = swan`
- role of `bcfile`

Primary target docs:
- `knowledge/methods/xbeach-boundary-and-wave-setup.md`
- `knowledge/methods/xbeach-parameter-glossary-v1.md`

### XBEACH-04
Question:
Which XBeach parameters should always be logged in an early baseline experiment for wave/morphology interpretation?

What a good answer should contain:
- `wavemodel`
- `wbctype`
- `bcfile`
- `break`
- `bedfriction`
- `form`
- `morfac`
- `avalanching`
- `wetslp`, `dryslp`

Primary target docs:
- `knowledge/methods/xbeach-parameter-glossary-v1.md`

### XBEACH-05
Question:
What evidence shows that the locally rebuilt XBeach executable is actually runnable?

What a good answer should contain:
- example_1d smoke test
- exit code 0
- promoted executable path
- distinction between smoke test and scientific validation

Primary target docs:
- `experiments/2026/xbeach/2026-04-30-example-1d-smoke-test.md`

---

## Failure-Pattern / Cross-Workflow Questions

### FP-01
Question:
What is the ADCIRC `wide6` provenance-gap problem, and why is it a failure pattern rather than just missing documentation?

What a good answer should contain:
- retained artifact exists but reproducibility path unclear
- baseline credibility issue
- affects fair revalidation

Primary target docs:
- `knowledge/failure-patterns/adcirc-wide6-provenance-gap.md`
- `knowledge/playbooks/adcirc-wide6-reconstruction-checklist.md`

### FP-02
Question:
Why should baseline classification come before serious mesh-tool revalidation in ADCIRC?

What a good answer should contain:
- reproducible / partially reproducible / non-reproducible framing
- fairness of comparison
- avoid debating tool choice too early

Primary target docs:
- `knowledge/heuristics/adcirc-baseline-before-tool-revalidation.md`

### FP-03
Question:
How do you distinguish EFDC water-level-good/current-bad from EFDC wet/dry connectivity bias?

What a good answer should contain:
- broad mismatch pattern vs shallow-zone connectivity-specific pattern
- when wet/dry becomes the prime suspect
- overlap but not equivalence

Primary target docs:
- `knowledge/failure-patterns/efdc-water-level-good-current-bad.md`
- `knowledge/failure-patterns/efdc-wetdry-connectivity-bias.md`

### FP-04
Question:
What makes a good promoted knowledge note in this workspace, versus a raw source note or experiment card?

What a good answer should contain:
- distinction between raw source / experiment / heuristic / failure pattern / playbook
- durable reusable knowledge emphasis

Primary target docs:
- `README.md`
- `protocols/taxonomy.md`
- `templates/source-note.md`
- `templates/experiment-card.md`
- `templates/heuristic-note.md`
- `templates/failure-pattern.md`
- `templates/playbook.md`

### FP-05
Question:
Why is a small evaluation set necessary before changing retrieval rules for local Qwen?

What a good answer should contain:
- objective before/after measurement
- avoid intuition-only optimization
- use benchmark as compass for retrieval/template changes

Primary target docs:
- this file

---

## Suggested Evaluation Procedure

1. Run all 15 questions with the current setup.
2. Save raw answers.
3. Score each question 0-8.
4. Note recurring misses by category:
   - wrong retrieval
   - missing evidence
   - weak structure
   - unsupported parameter naming
   - poor next-action advice
5. Change exactly one thing at a time:
   - template
   - retrieval policy
   - routing
6. Re-run the same 15 questions.
7. Compare totals and failure categories.

## Next Planned Step

After freezing this eval set:
- define the answer template/system prompt
- then implement retrieval priority rules
