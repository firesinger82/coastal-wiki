# Qwen Retrieval Policy V1

Date: 2026-04-30

Purpose:
- define the first retrieval policy for local Qwen over the modeling wiki and attached RAG systems
- make retrieval changes measurable against `indexes/qwen-domain-eval-set-v1.md`
- prefer domain-appropriate document types rather than flat semantic similarity alone

Scope:
- EFDC
- XBeach
- failure-pattern / workflow questions
- this is a policy note, not yet an implementation-specific code file

## Core Principle

Do not retrieve all document types equally.

The same keyword can appear in:
- raw/manual sources
- source notes
- method notes
- failure patterns
- heuristics
- playbooks
- experiment cards

These layers answer different question types. Retrieval quality improves when question type determines document priority.

## Retrieval Pipeline

Use this sequence.

### Step 1. Classify The Question

Assign one primary class:
- definition / glossary
- method / setup
- diagnosis / troubleshooting
- operating procedure
- baseline selection
- evidence / validation
- source lookup

Optional secondary labels:
- model: EFDC / XBeach / ADCIRC
- domain: hydrodynamics / morphodynamics / wet-dry / forcing / boundaries / calibration

### Step 2. Select Candidate Document Layers

Do not hit every layer with equal weight.
Pick the document classes that should dominate first.

### Step 3. Retrieve Within The Chosen Layers

Use filters or ordering by document type first, then semantic relevance.
If raw manuals are queried, prefer them as supporting evidence after curated notes unless the question explicitly asks for original wording.

### Step 4. Compose The Answer

Answer should reflect the dominant layer:
- glossary → precise definitions and key terms
- methods → conceptual setup guidance
- heuristics → short strong rule plus scope
- failure patterns → symptom, likely cause, quick triage
- playbooks → ordered actions
- experiments → concrete evidence and limits

## Document-Type Priority Rules

### 1. Definition / Glossary Questions

Examples:
- "ISDRY 99가 뭐야?"
- "XBeach에서 wbctype가 뭐야?"
- "morfac 의미가 뭐지?"

Priority:
1. glossary / methods with parameter sections
2. source notes with exact terminology
3. raw manuals
4. experiments only if needed for examples

Default target docs:
- EFDC: `efdc-parameter-glossary-v1.md`, `efdc-wetting-drying-foundation.md`
- XBeach: `xbeach-parameter-glossary-v1.md`, `xbeach-boundary-and-wave-setup.md`

### 2. Method / Setup Questions

Examples:
- "XBeach boundary를 어떻게 잡아?"
- "EFDC calibration 순서는?"
- "storm baseline 어떻게 세워?"

Priority:
1. methods
2. playbooks
3. heuristics
4. source notes
5. raw manuals

Default target docs:
- EFDC method stack
- XBeach boundary/morphology/baseline notes

### 3. Diagnosis / Troubleshooting Questions

Examples:
- "수위는 맞는데 유속이 안 맞음"
- "XBeach morphology 결과가 믿을 만한가?"
- "wet/dry가 문제인지 어떻게 알아?"

Priority:
1. failure patterns
2. heuristics
3. playbooks
4. methods
5. experiments
6. raw manuals last

Reason:
- troubleshooting quality depends on distilled pattern recognition, not raw documentation volume

### 4. Operating Procedure Questions

Examples:
- "무슨 순서로 점검해?"
- "경계조건부터 뭘 확인해?"
- "첫 baseline은 어떻게 잡아?"

Priority:
1. playbooks
2. heuristics
3. methods
4. experiments
5. raw manuals

### 5. Baseline Selection Questions

Examples:
- "XBeach baseline으로 뭘 써?"
- "DELILAH vs Holland Coast 차이?"
- "example_1d는 뭘 위한 거야?"

Priority:
1. baseline-selection note
2. reference notes
3. smoke-test or experiment notes
4. methods
5. raw manuals

### 6. Evidence / Validation Questions

Examples:
- "이게 실제로 돌았나?"
- "근거가 뭐야?"
- "현장 데이터 비교용 사례가 있나?"

Priority:
1. experiment cards
2. source/reference notes
3. methods
4. raw manuals

### 7. Source Lookup Questions

Examples:
- "매뉴얼에 뭐라고 되어 있어?"
- "원문 기준으로 찾아줘"
- "공식 문서 근거로 설명해줘"

Priority:
1. source notes
2. raw manuals / RAG source
3. methods as supporting context only

## Model-Specific Rules

### EFDC

If query mentions any of:
- current mismatch
- friction
- wet/dry
- boundary forcing
- ISDRY

Bias toward:
1. EFDC failure patterns
2. EFDC heuristics
3. EFDC playbooks
4. EFDC methods
5. EFDC manual RAG

If query asks exact manual meaning or control names:
- move EFDC manual RAG earlier
- still keep curated note if it prevents misinterpretation

### XBeach

If query mentions any of:
- wavemodel
- wbctype
- surfbeat
- nonh
- jonswap
- swan

Bias toward:
1. `xbeach-boundary-and-wave-setup.md`
2. `xbeach-parameter-glossary-v1.md`
3. DELILAH reference note
4. local/official manual source notes

If query mentions any of:
- morphology
- erosion
- dune
- profile
- morfac
- avalanching
- wetslp/dryslp

Bias toward:
1. `xbeach-morphology-foundation.md`
2. XBeach heuristic
3. XBeach failure pattern
4. Holland Coast reference note
5. glossary
6. raw/manual notes

If query asks about baseline choice:
1. `xbeach-first-baseline-case-selection.md`
2. DELILAH / Holland Coast notes
3. smoke-test experiment

## Attached RAG Usage Rules

### EFDC Manual RAG

Use EFDC manual RAG earlier when:
- exact control names are requested
- the user asks for official wording
- the curated notes explicitly say exact names remain uncertain

Do not use EFDC manual RAG as the first answer source when:
- the question is clearly diagnostic or procedural
- the workspace already has a distilled heuristic, failure pattern, or playbook for that issue

### XBeach Local Manuals / Source

Use source/manual notes earlier when:
- exact parameter names or example structure are requested
- code-path questions refer to `boundaryconditions.F90` behavior
- the question asks about documented examples or modes

## Retrieval Result Size Rules

Default top-k by question class:
- glossary: 2-4 docs
- methods/setup: 3-5 docs
- diagnosis: 3-4 docs, strongly typed
- procedure: 2-3 docs
- evidence/validation: 2-4 docs

Prefer fewer, better-typed documents over a large mixed set.

## Failure Modes Of Retrieval

Watch for these signs that retrieval policy is wrong:
- answers quote raw manuals but miss the existing heuristic or playbook
- exact parameter-name questions produce vague workflow advice
- troubleshooting answers rely on methods only and ignore failure patterns
- morphology questions pull smoke-test notes too early
- XBeach and EFDC documents cross-contaminate because the model label was not enforced

## Evaluation Rule

Any retrieval-policy change should be tested against:
- `indexes/qwen-domain-eval-set-v1.md`

Change one thing at a time:
1. freeze current score
2. modify retrieval priority
3. rerun the same eval set
4. compare total score and failure categories

## Immediate Next Implementation Step

After this policy note:
1. freeze answer template / system prompt
2. implement question classification labels
3. implement document-type filters or ranking boosts
4. evaluate against the 15-question set
