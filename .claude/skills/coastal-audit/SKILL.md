---
name: coastal-audit
description: L4 자가 감사 루프 V0 — canonical(concepts/·models/) 단언에 출처가 있는지 AI가 감사. citation_status: verified 인데 미출처 단언이 있으면 "무결성 위반" 적발(CLAUDE.md 절대규칙 #1). report-only — canonical 절대 미수정, 사람이 게이트. 트리거: "audit", "L4 감사", "출처 감사", "citation 감사".
---

# coastal-audit

CLAUDE.md 절대규칙 #1(canonical 단언 = 출처 인용 필수)의 **자가 감사 루프**. 결정론적 pre-commit 검증(링크·경로·placeholder)이 못 잡는 의미 판단 — "이 문장이 출처 없는 단언인가" — 만 AI가 수행한다. 설계 근거: [plan.md "L4 자가 감사 루프 PoC 설계"](../../../plan.md).

배관은 스크립트, **판단만 AI**. 이 skill 은 정책을 바꾸지 않는다.

## 절대 금지

1. **canonical 파일(`concepts/`·`models/`·`textbook/`·`experience/`) 일절 수정 금지.** 산출물 = 리포트뿐. 출처 보강·citation_status 강등은 *사람*이 리포트를 보고 결정한다(report-only).
2. **citation_status 자동 변경 금지.** verified→강등, 빈→verified 승격 모두 제안만.
3. **committed 내용만 감사.** SSOT = HEAD blob(Phase 1 F3). selector 가 `dirty` 표시한 파일은 미커밋분이 아닌 *커밋된 버전*을 본다 — 리포트에 dirty 명시.
4. **오탐 억제 우선.** "verified가 거짓"은 무거운 지적 — Adversary 단계로 refute 실패한 것만 confirmed.

## 입력

- 없음(기본): 변경된 슬라이스 N=8 자동 선정
- `--n <N>`: 슬라이스 크기
- 명시 파일 path list: 그 파일만 감사

## 루프 (5단계)

### 1. Select (결정론적)

```
python3 tools/llm-wiki-audit/select_audit.py [--n 8]
```

`{slice:[{path,citation_status,blob_sha,dirty}], stats:{total_content,pending,slice,...}}` 반환. ledger(`_staging/audit/ledger.json`)의 blob_sha 와 다른 파일만 후보 — 변경분 점진 소진. verified 우선. `pending`==0 이면 "감사 최신, 새 변경 없음" 보고 후 종료.

### 2. Audit (AI — 핵심 단계)

slice 의 각 파일을 읽고(`wiki_read` 또는 Read), **각 단언(assertion)을 분류**:

- **sourced** — 출처 인용이 붙음: 소스코드 `file:line`, 메뉴얼 페이지, 논문 인용 `(저자 연도)`, 교과서 `(source_id, p.NN)`, repo-상대 `file:line`, `[[wikilink]]`로 canonical 근거 연결.
- **UNSOURCED** — canonical 본문의 *사실 단언*인데 위 어떤 출처도 없음. ← 적발 대상.
- **opinion** — 주관·메타·구조 설명(단언 아님). 무시.

단언 판정 가이드(경계):
- 표·코드블록·직접 인용문(`> "..."`)은 그 자체로 출처가 명시돼 있으면 sourced.
- "X는 Y이다"류 도메인 사실·수식·계수·임계값 = 단언. 출처 없으면 UNSOURCED.
- 해당 섹션이나 인접 문장, frontmatter `source_id`, 같은 파일 상단의 포괄 출처로 커버되면 sourced(섹션 단위 인용 허용 — CONVENTIONS §2).
- 파일에 실질 사실 단언이 없으면(순수 안내·TOC·링크 모음) `has_real_claims=false`.

### 3. Adversary (AI — 오탐 컷)

UNSOURCED 후보마다 **반대 입장에서 refute 시도**: "사실은 이 근처/섹션 헤더/frontmatter/인접 wikilink에 출처가 있지 않은가?" refute 성공하면 그 플래그 폐기. **refute 실패한 것만 confirmed unsourced.** 불확실하면 폐기(precision 우선).

### 4. Record (결정론적)

각 파일의 findings 를 JSON 으로 조립해 recorder 에 전달:

```
python3 tools/llm-wiki-audit/record_audit.py --in <findings.json>
```

findings 스키마 (파일당):
```json
{ "path": "...", "blob_sha": "<selector 값 그대로>", "citation_status": "verified",
  "dirty": false, "has_real_claims": true, "sourced": 12, "opinion": 1,
  "unsourced": [ {"line": 42, "text": "원문 문장", "reason": "출처 0",
                  "adversary": "refute 실패 → confirmed"} ] }
```

recorder 가 verdict 매트릭스를 *결정론적으로* 적용(아래) → `_staging/audit/L4-<date>.md` 리포트 + ledger 갱신. blob_sha 는 selector 가 준 값을 그대로 넣을 것(감사한 정확한 버전 고정).

**verdict 매트릭스**(현재 citation_status × 미출처 수):

| citation_status | 미출처 | verdict |
|---|---|---|
| verified | >0 | **INTEGRITY-VIOLATION** (강등 or 출처 보강) |
| verified | 0 | verified-confirmed |
| 빈/source-needed | 0 | promote-candidate (verified 후보) |
| 빈/source-needed | >0 | needs-work |
| 표준 외(reference·partial-verified 등) | — | status-nonstandard (정규화) |
| 실질 단언 없음 | — | scaffolding-exempt |

### 5. Human gate

리포트 경로 + verdict 집계를 사용자에게 출력. **무결성 위반(INTEGRITY-VIOLATION)이 있으면 그 목록을 우선 제시.** 사용자가 출처 보강/강등/승격을 결정 — skill 은 여기서 멈춘다.

ledger·리포트(`_staging/audit/`)는 검색 인덱스 denylist + tracked. 커밋은 사용자 몫(상태 영속·멀티머신 전파). 커밋 메시지 초안:
```
chore(audit): L4 자가 감사 <date> — N파일, 위반 K건

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

## V0 범위 한계 (의도된 축소)

- 대상 = `concepts/`·`models/` 본문만(rule #1 직격). `textbook/`·`experience/`는 V1+.
- 트리거 = 수동. cron/autonomous(V3)는 신뢰 축적 후.
- 산출 = 리포트만. 제안 diff(V1)·pre-commit 통합(V2) 미포함.
- 상태값 정규화(partial-verified 등)는 적발만 — 수정은 별도 결정론적 lint 후보.
