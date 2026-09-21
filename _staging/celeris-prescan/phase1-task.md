# CODEX TASK — Celeris Phase 1 의미 검토 (13건 + 추가 조사 2)

```
OBJECTIVE
  Celeris pinned f6fd78b → upstream ebca435 변경이 위키 주장의 의미를 바꾸는지
  후보 13건을 판정하고 추가 조사 2건에 답한다. 위키는 수정하지 않는다.

SCOPE
  읽기: ~/coastal-wiki/models/Celeris (노트·raw 소스, 읽기 전용),
        ~/.cache/coastal-snapshots/celeris-upstream (새 스냅샷 git repo),
        ~/coastal-wiki/_staging/celeris-prescan/
  쓰기: ~/coastal-wiki/_staging/celeris-prescan/ 하위만
  금지: models/ 수정, 위키 본문 수정, chmod/sudo, 범위 밖 조사

STOP CONDITION
  13건 + 추가 조사 2건이 끝나면 종료. 근거가 소스에서 확인되지 않으면
  UNRESOLVED 로 표시하고 추측하지 않는다.

DELIVERABLE
  phase1-codex.csv — id, note, note_line, wiki_claim, old_evidence, new_evidence,
    semantic_meaning_changed, proposed_classification, reason_type, confidence, exact_evidence
  phase1-codex.md  — 요약, 추가 조사 답, UNRESOLVED 목록
```

## 입력

`phase1-candidates.csv` 13행. 노트 원문·신구 좌표·교차 hunk 원문 포함.
`REANCHOR(a-b)` 는 끝점이 변경 블록 안이라 기계 매핑 실패 — 새 좌표를 직접 찾아라.

## 변경의 성격

10커밋 / 371파일(신규 343 / 수정 28). 신규 대부분은 `CelerisAgent/`·`benchmarks/nthmp/` 자산.

| 커밋 | 내용 |
|---|---|
| afc1fe7 | **Spherical NLSW Solver** + Japan 2011 예제 (신규 `shaders/Pass3_NLSW_Spherical.wgsl` +267) |
| bb99fee · c4be488 | **Grid nesting** (신규 `js/Handler_ExtractNestedBoundaryTimeSeries.js` +109, `shaders/ExtractNestedBoundaryTimeSeries.wgsl` +53), multiple nested grids |
| 0ee5174 | CelerisAgent 신규 서브시스템 (신규 `js/agent_controls.js` +949) |
| ff0d046 | spherical grid 용 time series plot |
| ebca435 | time series write 버그 수정 |
| c20e659 · 77373fe | NTHMP 벤치마크 run·report |

소스 diff 규모: `js/main.js` **+3,429**, `shaders/BoundaryPass.wgsl` 136,
`js/constants_load_calc.js` 198, `js/Wave_Generator.js` 78, `js/Handler_BoundaryPass.js` 100.

## 판정 기준

UPDATE_REQUIRED / REVIEW_ONLY / NO_ACTION. UPDATE_REQUIRED 에는 `reason_type` 필수
(`SEMANTIC_CHANGE` / `BEHAVIOR_CHANGE` / `INTERFACE_CHANGE` / `SYMBOL_RENAME_ONLY` / `BUGFIX_AFFECTING_DOC`).

**hunk 겹침은 충분조건이 아니다.** `js/main.js` 가 파일의 절반 가까이 바뀌었으므로
broad 인용(`1893-2174`, `341-456` 등)은 대부분 겹친다. 그 범위가 뒷받침하던 주장이
무엇인지 보고 판정하라 — 코드가 바뀌었다는 사실만으로 UPDATE_REQUIRED 로 올리지 마라.

## 추가 조사 (필수)

**A. NEW FILE RULE.** 신규 `shaders/Pass3_NLSW_Spherical.wgsl`, `js/Handler_ExtractNestedBoundaryTimeSeries.js`,
`shaders/ExtractNestedBoundaryTimeSeries.wgsl`, `js/agent_controls.js` 가
기존 파일에서 **로직이 분리·이동**된 것인지, 아니면 순수 신규 기능인지 확인하라.
기존 파일이 위키에 인용돼 있으면 그 인용의 주장이 영향받는지 함께 보라.

**B. 파이프라인 구조 변경.** `models/Celeris/source-analysis/celeris-pipeline-graph.md` 와
`celeris-source-map.md` 는 렌더/계산 pass 순서와 `main.js` 구조를 서술한다.
grid nesting 과 spherical solver 추가로 **pass 구성이나 dispatch 순서**가 바뀌었는지
확인하고, 바뀌었으면 어느 서술이 어긋나는지 지목하라. 노트 전체를 읽고 판단하라.

## 반환하지 말 것

위키 문장 수정안, 좌표 일괄 치환, 13건 밖 임의 후보 추가(발견 시 md 에 별도 보고만).
