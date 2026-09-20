# MODEL SNAPSHOT MIGRATION FRAMEWORK — 설계안 v2 (후보)

> 상태: **REVIEWED-DRAFT (미확정), 미구현.** v1(`DESIGN.md`) + Codex 적대 검토(`DESIGN-REVIEW-codex.md`) + Claude 독립 검증 반영. 승인 전까지 구현·migration 금지.
> 작성 2026-09-20. v1 대비 변경은 §CHANGELOG 참조.

## GOALS

1. pinned snapshot → upstream 전환 시 **위키 근거가 깨지는 지점**을 저장소 유형과 무관하게 같은 방식으로 판정한다.
2. 읽을 양을 줄이되, **축소는 우선순위 필터이지 무영향 증명이 아니다.** 해석되지 않은 참조가 남아 있으면 "영향 없음"으로 종결하지 않는다.
3. 판정·적용·검증의 각 단계가 기계 검증 가능한 산출물(manifest·CSV·hash)을 남긴다.
4. historical provenance 를 보존하고 current validation 을 검증 종류·범위와 함께 분리 기록한다.

## NON-GOALS

- 위키 서술 개선·참조 정규화(hygiene), upstream 코드 리뷰, 빌드·실행 검증, 부속 도구 내부 전수 분석(`CLAUDE.md` 범위 통제).
- 모든 저장소의 최신화. 전환은 근거 영향이 확인된 저장소만, 건별 승인.

## REPOSITORY CLASSIFICATION

| 유형 | 정의 | 해당(2026-09-20 기준일 명시) | 비교 방법 |
|---|---|---|---|
| A. 일반 git | full clone | 현재 없음 | `git diff old..new` |
| B. shallow git | `--depth 1` | BEHIND 13 + CURRENT 다수 | staging clone + baseline 커밋 추가 fetch → tree 비교 |
| C. 대형 차이 | 변경 파일·패치 규모 큼 | Delft3D(+1,771), hydromt(+29), asgs(+20) | tree 대 tree, 예산 승인 후 진행 |
| D. local patch | 추적 파일 로컬 수정 | FUNWAVE-GPU(3파일) | §LOCAL-PATCH |
| E. non-git/provenance 불완전 | commit 부재·로컬 확인 불가 | LISFLOOD-FP, SFINCS, XBeach | §NON-GIT |

유형은 중첩 가능. 저장소마다 `repo_id`(model+repo)와 **상태 기준일**(collected_at)을 기록한다. `manifest.csv` 의 pinned 와 `provenance-final.csv` 의 current 가 다를 수 있으므로(ADCIRC 전환 후 실제 발생) 입력 충돌 시 **실제 설치본 재조사가 우선**이다.

## INPUTS

v1 동일 + 각 입력에 `collected_at`·`source_method` 필수. 네트워크 수집은 Claude, 로컬 계산은 Codex(§ROLE). Codex 에는 **Claude 가 고정한 staging 트리·아카이브**를 넘긴다.

## REFERENCE GRAMMAR

**v1 의 "SWAN/SWASH file:line 0건" 전제는 오측정이었다.** 원인: 확장자 대안 순서에서 `f` 가 `ftn` 보다 앞서 `swanpre1.ftn:738` 이 `swanpre1.f`(줄 없음)로 매칭. 정정 실측(2026-09-20, 확장자 긴 것 우선):

| 모델 | file:line | 파일만 | bare | 모델 | file:line | 파일만 | bare |
|---|---:|---:|---:|---|---:|---:|---:|
| Delft3D | 1,568 | 1,121 | 806 | SWAN | **170** | 1,183 | 129 |
| ROMS | 1,196 | 1,227 | 388 | SWASH | **440** | 300 | 1,246 |
| XBeach | 620 | 484 | 247 | SFINCS | 89 | 333 | 890 |
| EFDC | 548 | 604 | 247 | LISFLOOD-FP | 275 | 274 | 322 |
| ADCIRC | 496 | 937 | 118 | FUNWAVE | 80 | 310 | 21 |
| CADMAS-SURF | 419 | 445 | 141 | Celeris | 243 | 516 | 248 |
| ShorelineS | 22 | 108 | 6 | **합계** | **6,166** | 7,842 | 4,809 |

**문법 규칙**
- 확장자 대안은 **긴 것 우선**(`ftn90|ftn|F90|for|f90|cpp|...`). 복수 범위(`file:1-3,5-7`), bracket 문법(`[file=... line=...]`), backtick 없는 표 셀 참조, en dash·`L` 접두를 모두 인식한다.
- **coverage ledger 필수**: 탐지된 모든 후보는 `resolved` / `unresolved` / `excluded(코드블록·frontmatter)` 중 하나로 귀속된다. 부분 파싱 성공을 처리 완료로 세지 않는다.
- frontmatter·코드블록은 **자동 수정 제외**지만 탐지·보고 대상이다(실제 근거가 그 안에 있는 사례 존재: `verification_method`, 인용 코드).

| 유형 | 자동 식별 | 해석 | confidence | 자동 수정 |
|---|---|---|---|---|
| `file:line` / `file:a-b` | 가능 | repo 내 유일 경로 | high | **조건부 허용** — §AUTOMATION BOUNDARY 조건 전부 충족 시 |
| bare `:line` | 탐지 가능 | 같은 **문장·표 셀** 우선 → 절 문맥 → 상위 명시 파일 | medium | 조건부(문장 내 파일 후보가 1개일 때만) |
| 파일만 | 가능 | 경로 해석 | high | rename·삭제 시 **수정 대상**(v1 의 "수정 불필요" 정정) |
| 심볼 | 가능 | old·new **양쪽** 검색 | medium | 금지(존재·소멸 보고) |
| 파일+심볼 | 가능 | 파일 내 심볼 위치 | medium | 동명 정의·호출·주석 구분 증거 있을 때만 |
| 산문 경로·요약 주장 | 부분 | 경로/주장 대상 | low | 금지(보고) |

**한 문장에 파일이 둘 이상이면 nearest-file 규칙을 쓰지 않는다**(예: SWASH 노트가 `SwashUBotFrict.ftn90:254` 와 `SwashBotFrict.ftn90:298` 을 한 문장에서 비교). 문장 단위로 후보를 모두 수집하고, 유일하지 않으면 AMBIGUOUS.

## CHANGE DETECTION PIPELINE

```
[0] snapshot manifest (repo_id, collected_at, 유형)
[1] 참조 인덱스 + coverage ledger (resolved / unresolved / excluded)
[2] 변경 파일 집합  ← tree 대 tree (old_path·new_path·mode·object type 포함)
[3] ∩ 위키 참조 파일 (old·new 경로 양쪽)
[4] 교집합 파일의 patch 확보
[5] ∩ 참조 지점(줄·심볼) + old→new 매핑 + 범위 내부 동일성
[6] 영향 분류 + decision_state
```

**[3] 종료 조건 정정(v1 C1)**: 교집합 0 은 "**해석된 직접 참조**의 교집합 0" 으로만 기록한다. `unresolved > 0`, 소멸 심볼 존재, 변경된 인터페이스·기본값을 다루는 요약 주장이 남아 있으면 전체 NO_ACTION 으로 종결하지 않고 `pending` 으로 둔다.

**[2] 규모별 방법**: 소규모 GitHub compare(파일 300 상한·`truncated` 확인 필수) / 그 외 staging tree 비교 / non-git 은 manifest 비교. patch 는 교집합 파일만 확보.

**예산**: 파일 수만으로 비용을 추정하지 않는다. `changed_files`, `changed_lines`, `patch_bytes`, `unresolved_refs`, `broad_refs` 4종을 산출해 **사용자 승인 후** [4] 진행(대형 저장소 필수).

## IMPACT CLASSIFICATION

3단계 유지 + 별도 축.

| 분류 | 기준 |
|---|---|
| UPDATE_REQUIRED | 노트 주장과 새 baseline 이 불일치. **hunk 겹침은 충분조건이지 필요조건이 아니다** — 인터페이스·기본값·상태 서술(예: "PR OPEN") 불일치 증거가 있으면 겹침 없이도 해당 |
| REVIEW_ONLY | 변경 파일 인용이나 의미 영향 미확인(broad span, 줄 이동, 심볼 존속) |
| NO_ACTION | 변경 근거와 교차하지 않음 |

별도 축: `decision_state` ∈ {auto_ok, needs_claude_review, **NEEDS_USER_DECISION**, user_hold}, 보조 열 `line_shift`·`evidence_width`·`content_identity`·`citation_snapshot`·`escalated_from`.
**사용자 보류는 validated 가 아니다.** REVIEW_ONLY 전 행에 최종 disposition 또는 보류 사유를 남긴다.

## AUTOMATION BOUNDARY

자동 줄 수정은 **다음을 모두 충족할 때만** 허용한다.
1. repo·snapshot·경로가 확정(동명 파일 다중 후보 아님).
2. 인용의 **현재 좌표 기준(citation_snapshot)** 이 old baseline 과 일치.
3. old→new 대응이 유일.
4. **인용 범위 전체의 내용이 동일**(양 끝만 일치로 불충분 — ADCIRC 실측: 범위형 77건 중 4건이 내부 변경, 그중 1건은 의미 수정이 필요했음). 범위가 넓어(> 60줄) 내부 변경이 있으면 REVIEW_ONLY 로 두고 보고.
5. 치환 범위가 승인된 범위 안.

다음이면 조사 결과까지만 만들고 **멈춘다(NEEDS_USER_DECISION)**: old 근거 관계 복원 실패 / non-git 범위 불명 / provenance 충돌 / AMBIGUOUS·unresolved 잔존 상태의 설치 / local patch 의미 미확인 / rename·split·merge 미확정 / 승인 범위 초과 / 예산 초과.

## NON-GIT FALLBACK

1. 현재 설치본 manifest 는 `observed_local_snapshot` 으로 기록한다(**historical 아님**).
2. upstream 배포본은 archive 출처·배포 식별자·hash·추출 규칙·최상위 폴더 구조를 함께 고정한다.
3. 두 manifest 의 **비교 범위가 동일한지** 먼저 확인한다(LISFLOOD-FP 3,170 vs 1,672 미해결 — 원인 미확인이므로 "부분 추출" 로 단정하지 않는다).
4. 노트가 그 copy 를 봤다는 근거가 없으면 historical 은 `unknown`/`conflicting` 으로 보존하고, **줄 수정·검증 승격·설치를 막는다**(보고는 가능).
5. 소스 내 버전 문자열은 보조 증거(LISFLOOD-FP 8.1.0 stale 헤더 선례).

## LOCAL-PATCH HANDLING

1. migration 전 `git diff HEAD` 패치 + 대상 파일 hash + **필요 자산 목록**(untracked·binary 포함 여부 결정)을 고정.
2. staging 에서 새 base 에 패치 적용 → **결과 트리 hash 생성·보존**. `git apply --check` 통과는 구문적 조건일 뿐이다.
3. 패치가 의존하는 호출 계약·자료형·빌드 조건이 upstream 에서 바뀌었는지 Claude 가 검토. 불확실하면 NEEDS_USER_DECISION(빌드·실행 검증이 필요하면 별도 범위로 요청).
4. 노트 재현 기록 = `BASE_SHA + LOCAL_PATCH(hash)`.

## PROVENANCE MODEL

| 축 | 의미 |
|---|---|
| `historical_source_provenance` | 작성·검증 당시 snapshot. **불변**. 불확실하면 unknown/conflicting 유지 |
| `current_validated_against` | 실제 재검증한 경우만 |
| `validation_kind` / `validated_on` / `validated_refs` | 검증 종류(mechanical·semantic)·일자·대상 참조. **삭제 금지** |
| `citation_snapshot` (참조 단위) | 그 인용의 줄 좌표가 어느 snapshot 기준인지 |
| `worktree_state`, `reproducibility` | v1 동일 |

`citation_snapshot` 은 **다음 migration 의 이중 이동을 막는 핵심 열**이다(이번 세션에서 갱신된 인용을 옛 좌표로 재매핑해 118건 오탐이 실제 발생). 노트 상태(SEMANTICALLY_UPDATED / LINE_REFERENCE_ONLY / REVIEWED_NO_CHANGE / NO_ACTION)는 유지하되 note 요약이 전체 검증을 뜻하지 않게 한다.

## LOCKING / APPLY PROCEDURE

A. INSTALL-STYLE, B. SCOPED EDIT — v1 동일. 추가:
- 적용 **직전** 승인 hash 재확인(source·note·patch). 검토 이후 바뀌었으면 중단.
- 실패 경로 명시: 중간 실패 시 relock → 중단 → 복구 조건·재개 조건 기록. 성공 경로에만 relock 을 두지 않는다.
- source·notes·provenance 의 이전/목표 상태를 함께 남기고, 커밋은 분리하되 **같은 run_id** 를 공유한다.

## CODEX / CLAUDE ROLE SPLIT

v1 동일. 명확화: 네트워크 수집은 Claude(샌드박스 차단 확인), Codex 는 Claude 가 고정한 로컬 트리·아카이브만 사용. Codex 의 영향 분류는 **초안**이며 Claude 재판정 전 완료로 세지 않는다(ADCIRC: Codex 21 변경단위 IMPACTING → Claude 최종 노트 2 UPDATE_REQUIRED; **단위가 다르므로 과잉 판정률로 환산하지 않는다**).

## OUTPUT SCHEMA

디렉터리 키: `_staging/<model>-<repo>-upstream-review-<run_id>/` (model+repo+run_id — 같은 날 복수 repo 처리 시 덮어쓰기 방지).

| 파일 | 추가/변경 |
|---|---|
| `snapshot.json` | + collected_at, source_method, target_sha/archive_id |
| `changed-files.csv` | + repo_id, old_path, new_path, object_type, mode |
| `REFERENCES.csv` | + repo_id, citation_snapshot, coverage(resolved/unresolved/excluded), ranges(복수 보존) |
| `impact.csv` | + decision_state, evidence_width, content_identity, rationale |
| `note-status.csv` | + validation_kind, validated_on, validated_refs, pending_reason |
| `manifest-{A,B,C,D}.csv`, `DECISIONS.md` | v1 동일 |

## FAILURE MODES

v1 1–11 유지 + 추가:
12. 미해석 참조를 남긴 채 NO_ACTION 종결 → coverage ledger 강제
13. 범위 내부 변경을 양 끝 동일로 통과 → 전체 범위 동일성 검사
14. rename/split/merge 미식별 → old·new 경로 양쪽 교집합, split/merge 는 pending
15. 새 manifest 를 historical 로 오인 → observed_local_snapshot 분리
16. patch 구문 통과·의미 충돌 → 적용 결과 hash + 인터페이스 검토
17. 같은 날 복수 repo 산출물 충돌 → run_id 키
18. 인용 좌표 기준 혼동으로 이중 이동 → citation_snapshot
19. 승인 hash 이후 바이트 변경 → 적용 직전 재확인
20. 부분 적용·재실행 상태 미표현 → 실패 경로 gate
21. 부분 문법 인식 성공 처리 → 문법별 탐지·해석 수 대조

## PARSER SELF-TEST / GRAMMAR REGRESSION GATE

**framework 실행 전 통과 필수.** 2026-09-20 ADCIRC 후속 정정에서 parser 결함(확장자 우선순위)이 migration 누락으로 이어진 사실이 확인됐다. parser 정확성은 impact filter 신뢰의 **선행 조건**이다.

### fixture (실제 coastal-wiki 사례 기반)

최소 포함 문법: `file.f` · `file.f90` · `file.ftn` · `file.ftn90` · `file.for` · `file.cpp` · `file:NN` · `file:NN-NN` · `file:NN,NN-NN`(복수 범위) · bare `:NN` · bare `:NN-NN` · en dash 범위 · `L` 접두(`file:L120`) · 괄호·링크·표 셀 안의 참조 · 상대경로(`../thirdparty/...`) · 동일 basename 다중 repo · symbol-only · file+symbol.

각 fixture 는 다음 expected 값을 고정한다: `reference_type`, `source_file`, `start_line`, `end_line`, `symbol`, `repo/model context`, `expected_parse_status`(parsed/ambiguous/unsupported).

**확장자 매칭은 longest-match 를 명시 규칙으로 구현한다** — 정규식 대안 순서의 우연에 맡기지 않는다. 우선순위: `.ftn90 > .ftn > .for > .cpp > .f90 > .f`(그 외 확장자도 길이 내림차순).

### 회귀 테스트가 검증하는 것

1. fixture 전부 탐지 2. source filename 손실 없음 3. line/range 정확성 4. **확장자 절단 없음** 5. en dash·복수 범위 누락 없음 6. bare 를 file-qualified 로 오인하지 않음 7. 동일 basename 을 임의 resolution 하지 않음(AMBIGUOUS 유지).

### 필수 회귀 fixture (이번 사례)

| fixture | 출처 | expected |
|---|---|---|
| `SwanReadADCGrid.ftn90:44-153` | `adcirc-swan-coupling.md:26`(정정 전) | 확장자 `.ftn90` 보존, 범위 내부 변경 감지, **자동 line-only 금지**, semantic review required |
| `SwanReadADCGrid.ftn90:44-103` | 〃 `:83`(정정 전) | 동일 |
| `nodalattr.F:636-686` | `adcirc-nodal-attributes.md:21`(정정 전) | **range-interior-change fixture** — 양 끝 동일하지만 내부에 `swan_local_control` 추가 → semantic review 로 승격 |

### range 규칙 (재확인)

범위형 인용은 양 끝점만 검사하지 않는다. **changed hunk 와 citation interval 의 실제 교집합**을 검사하고, 범위 내부에 변경 hunk 가 하나라도 들어오면 자동 `LINE_REFERENCE_ONLY` 로 처리하지 않고 semantic review gate 로 올린다.

### coverage ledger (모델별 필수 집계)

`총 참조 수 / parsed / resolved / ambiguous / unsupported / broad citation / symbol-only / bare`.
**교집합이 0 이어도 unresolved·unsupported 가 남아 있으면 "영향 없음" 으로 종료하지 않는다.**

### gate 판정

- 전부 통과해야 migration 시작. 하나라도 실패하면 **`PARSER_GATE_FAILED`** 상태로 종료하고 migration 을 시작하지 않는다.
- parser 수정 후에는 **전체 fixture 를 다시 실행**한다(부분 재실행 금지).

### UNRESOLVED_SOURCE_REFERENCE (2026-09-20 신설)

위키가 인용한 source file 을 **현재 snapshot 에서 찾을 수 없는** 참조. 자동 `NO_ACTION` 금지 — 별도 unresolved ledger 에 남기고 다음 중 하나로 해소한다:
⑴ old snapshot 에만 존재 ⑵ 다른 repository/배포본 ⑶ stale reference ⑷ typo/path drift.
EFDC 사전 스캔 실측: 89건(참조 2,317 중). 저장소별 이 수치를 ledger 에 기록한다.

### NEW FILE RULE (보완)

신규 파일이 위키에서 **직접 인용되지 않아도**, 변경된 기존 파일에서 로직이 신규 파일로 **이동·분리**됐는지 확인한다. `new file + 관련 기존 파일 변경` 이면 semantic-review candidate 로 올린다.
**regression case**: EFDC v12.5 의 `EFDC/Transport/caltran_quickest.f90`(+503, 신규) · `EFDC/Transport/mod_quickest.f90`(+115, 신규) ↔ `EFDC/Transport/calconc.f90`(+59/−42, 기존·노트 인용 있음).

## ACCEPTANCE CRITERIA

v1 1–8 + 추가:
9. coverage ledger 완결(탐지 = resolved + unresolved + excluded), 알려진 실제 인용 예가 탐지에 포함됨.
10. REVIEW_ONLY 전 행에 disposition 또는 보류 사유. unresolved·AMBIGUOUS 잔존 시 완료 판정 금지(보류 결정은 명시적으로).
11. 자동 수정 건은 전부 §AUTOMATION BOUNDARY 5조건 충족 기록.
12. `validate-all` 통과·broken reference 0 은 **필요조건일 뿐** 완료 근거가 아니다.
13. `UNRESOLVED_SOURCE_REFERENCE` 전건이 ledger 에 분류되어 있고 자동 NO_ACTION 으로 처리되지 않음.
14. **PARSER GATE 통과**(§PARSER SELF-TEST) — 실패 시 `PARSER_GATE_FAILED` 로 종료, migration 미착수.

## PILOT ROLLOUT ORDER

**commit 수로 난이도를 판단하지 않는다.** 착수 전 ⑴ 변경 파일 ⑵ 인용 교집합 ⑶ 줄 이동 수 ⑷ 의미 변경 후보 ⑸ broad·unresolved 수를 먼저 뽑아 시험 범위를 확인한다.

| 순서 | 대상 | 선정 근거 |
|---|---|---|
| **2차(조건부)** | **EFDC/EFDCPlus_Stable** | +1 커밋, file:line 548·bare 247. **단, 사전 스캔에서 교집합·줄 이동·broad 비율이 충분히 나오지 않으면 대상 교체** |
| 2차 대안 | ROMS/roms(+6, file:line 1,196) 또는 Celeris(+10) | 교집합이 확보되는 쪽 |
| 3차 | **SWASH 또는 SWAN** | bare 1,246 / file:line 440(SWASH), 문법·문맥 해석 회로 검증. *SWASH 는 현재 CURRENT 이므로 파서 검증 전용* |
| 4차 | asgs·hydromt·잔여 소규모 | |
| 5차 | Delft3D | 대형 tree·예산 승인 회로 |
| 별도 | non-git 3, FUNWAVE-GPU | 전용 회로 |

## CHANGELOG (v1 → v2)

| Codex 권고 | 판정 | 반영 |
|---|---|---|
| R1 인용 집계·coverage | **채택(검증됨)** | 실측 오류 정정(SWAN 170·SWASH 440), 긴 확장자 우선, coverage ledger |
| R2 교집합=우선순위 필터 | **채택** | 종료 조건 정정, unresolved pending, hunk 겹침은 충분조건 |
| R3 자동 수정 증거 조건 | **채택(검증됨)** | 범위 전체 동일성(실측 4/77 내부 변경), 문장 단위 다중 후보 |
| R4 rename/경로 | 채택 | old/new path·mode, 파일만 인용도 수정 대상 |
| R5 non-git observed/historical | 채택 | 분리 + 적용 차단 조건 |
| R6 local patch 결과 검증 | 채택 | 적용 결과 hash + 인터페이스 검토 + 자산 목록 |
| R7 검증 종류·좌표 기준 | **채택(중요)** | validation_kind 복원, citation_snapshot 신설 |
| R8 산출물 키·바이트 결속 | 채택 | run_id, 승인 hash 재확인 |
| R9 unresolved·보류 | 채택 | acceptance 10 |
| R10 실패·복구 gate | 채택 | 실패 경로 relock·재개 |
| R11 파일럿 선정 기준 | 채택 | EFDC 조건부 + 사전 스캔 |
| N1 단위 혼동 | 채택 | 역할 절에서 단위 명시 |
| N2 기준일 | 채택 | collected_at |
| N3 네트워크 책임 | 채택 | 역할 절 명확화 |
| N4 예산 지표 | 채택 | 4종 지표 |
| F4 vendor/submodule 전수 | **부분 채택** | 인용된 범위·모델 인터페이스까지만. 부속 도구 내부 전수 분석은 `CLAUDE.md` 범위 통제에 따라 제외 |
| M3 간접 영향 | **부분 채택** | 노트가 주장한 입력·호출·설정 관계까지만 확인, 불확실하면 pending. 일반 의존성 분석 아님 |

## 미해결 — ADCIRC 파일럿 잔여 (v2 적용 대상 아님, 별도 보고)

v1 파서 결함(확장자 순서)으로 ADCIRC 파일럿이 놓친 참조가 **2건** 확인됐다(둘 다 `models/ADCIRC/source-analysis/adcirc-swan-coupling.md`).
- 26행 `thirdparty/swan/SwanReadADCGrid.ftn90:44-153` → 새 baseline 기준 `44-158`
- 83행 `SwanReadADCGrid.ftn90:44-103` → `44-108`
같은 파일 참조 11건은 줄 이동이 없어 영향 없음. 처리 여부는 사용자 결정(작은 후속 수정 또는 backlog 편입).
