# MODEL SNAPSHOT MIGRATION FRAMEWORK — v2.0

> 상태: **FINAL.** 파일럿 4건으로 검증됨 (전부 2026-09-20 종료) —
> ADCIRC(`6037225`→`e8b62a70`), EFDC/EFDCPlus_Stable(`3ed76b6`→`3b382fd`), SWAN(`5544152`→`43e9bbb`),
> ROMS/roms(`32c79b7`→`57aecf5`, Unit A/B 분리 적용).
> v1(`DESIGN-v1-superseded.md`) + Codex 적대 검토(`DESIGN-REVIEW-codex.md`) + Claude 독립 검증 +
> 네 파일럿 실측 반영. 변경 이력은 §CHANGELOG.
>
> 파일럿이 드러낸 것은 **설계 결함이 아니라 구현·운영의 누락**이었고 그 교정이 v2.0 에 들어갔다 —
> EFDC 에서 §UNCITED PROSE SWEEP·§EXCLUDED REFERENCE LEDGER(failure mode 22–25),
> SWAN 에서 파서 문맥 오탐과 §CROSS-MODEL RESOLUTION(failure mode 26–28),
> ROMS 에서 이중 배치 귀속·모양 기반 억제 금지·`AHEAD_OF_SNAPSHOT`(failure mode 29–31).
>
> 구현·게이트: `refparser.py` + `test_refparser.py`(문법), `resolver.py` + `test_resolver.py`(귀속),
> 좌표 맵 예시 `_staging/efdc-migration/build-inputs.py` · `_staging/swan-prescan/build-phase2.py`.
> **두 게이트를 모두 통과해야 migration 을 시작한다.**

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
4. **인용 범위 전체의 내용이 동일**(양 끝만 일치로 불충분 — ADCIRC 실측: 범위형 77건 중 4건이 내부 변경, 그중 1건은 의미 수정이 필요했음).
   내부가 바뀐 참조는 범위 폭이 아니라 **그 주장이 이미 판정됐는지**로 가른다.
   | 조건 | 처리 |
   |---|---|
   | 해당 `note:line` 이 이번 run 의 semantic review 에서 REVIEW_ONLY·UPDATE_REQUIRED 로 판정됨 | 좌표 치환 허용. 변경 hunk 를 이미 대조했으므로 "주장 불변" 이 확정된 상태다 |
   | 판정 이력 없음 | **NEEDS_CLAUDE_REVIEW** 로 승격. 내부 변경을 직접 읽고 판정한 뒤에만 치환 |

   EFDC 실측: MOVED 152건 중 31건이 내부 변경 — 30건은 판정 완료(REVIEW_ONLY 26 / UPDATE_REQUIRED 2 / 혼재 2), 1건(`concepts/sst/06-model-application.md:75` ← `input.f90` C14)은 승격 후 직접 확인(read 목록 동일, 진단 `write` 순서만 이동)하여 해소.
   **내부 변경은 좌표 치환의 게이트일 뿐, 문장 수정 사유가 아니다.**
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

**노트가 pinned 보다 앞설 수 있다** (2026-09-20, ROMS 파일럿). `citation_snapshot` 은 지금까지
"인용 좌표가 옛 snapshot 기준"인 경우만 상정했으나, 반대 방향이 실제로 나왔다 —
`roms_4dvar.md` 가 upstream PR 첨부 PDF 를 근거로 **pinned 에 없는 기능**(`MULTI_SCALE_B`,
`multiscale_*` 7파일)을 서술했다. 해당 참조 28건이 "미해소"로 잡히지만 원인은 stale 이 아니라 **선행 서술**이다.

| 상태 | 의미 | 처리 |
|---|---|---|
| `AHEAD_OF_SNAPSHOT` | 인용 대상이 pinned 에 없고 upstream 에만 존재 | migration 전에는 검증 불가. **UNRESOLVED 와 구분해 기록**하고 자동 NO_ACTION 금지 |
| — | migration 후 | 해당 노트는 좌표 정비가 아니라 **내용 정정 단위**로 분리한다(ROMS Unit B 선례) |

선행 서술 노트는 근거가 PDF·PR 설명이라 **추론이 섞인다.** ROMS 실측: merge 후 대조하니
존재하지 않는 파일명 2개, 단위 오기(km↔m), 드라이버 호환 과잉 단정이 확인됐다.
따라서 이런 노트는 migration 직후 **전체 재대조** 대상이며, 좌표만 맞추고 끝내지 않는다.

`citation_snapshot` 은 **다음 migration 의 이중 이동을 막는 핵심 열**이다(이번 세션에서 갱신된 인용을 옛 좌표로 재매핑해 118건 오탐이 실제 발생). 노트 상태(SEMANTICALLY_UPDATED / LINE_REFERENCE_ONLY / REVIEWED_NO_CHANGE / NO_ACTION)는 유지하되 note 요약이 전체 검증을 뜻하지 않게 한다.

## LOCKING / APPLY PROCEDURE

A. INSTALL-STYLE, B. SCOPED EDIT — v1 동일. 추가:
- 적용 **직전** 승인 hash 재확인(source·note·patch). 검토 이후 바뀌었으면 중단.
- 실패 경로 명시: 중간 실패 시 relock → 중단 → 복구 조건·재개 조건 기록. 성공 경로에만 relock 을 두지 않는다.
- source·notes·provenance 의 이전/목표 상태를 함께 남기고, 커밋은 분리하되 **같은 run_id** 를 공유한다.
- **snapshot 교체와 노트 반영은 같은 게이트에서 수행한다.** 갱신된 좌표는 새 snapshot 기준이므로
  둘을 분리하면 그 사이에 인용이 로컬 소스와 어긋나는 구간이 생긴다. 승인 전 단계의 노트 수정은
  잠긴 트리에 직접 쓰지 말고 `wiki-candidate/` 사본과 통합 diff 로 만든다(ADCIRC·EFDC 공통).
- 잠금 확인은 §FAILURE MODES 25 에 따라 **일반 사용자 권한**으로 한다.
- LFS 를 쓰는 저장소는 교체 전후의 **포인터/실파일 상태가 같은지** 확인한다.
  EFDC 실측: `redist/` 37개가 양쪽 모두 포인터여서 손실 없음.

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

EFDC 파일럿 추가(22–25). 넷 다 설계가 아니라 **구현·운영**이 어긋난 사례다.

22. **인용 없는 산문이 교집합 후보에서 빠져 낡은 채 남음** → §UNCITED PROSE SWEEP.
    실측: IINTPG 산문 7곳 중 후보에 있던 것 0곳.
23. **제외 영역(코드블록·frontmatter) 참조가 snapshot 교체 후 조용히 어긋남** → §EXCLUDED REFERENCE LEDGER.
    실측: 9건.
24. **분류 산출물의 컬럼 의미가 배치마다 달라 조인이 깨짐** → 분류 CSV 는 `note_path`(repo 상대)·`note_line`(정수)
    두 열을 **정규화 스키마로 고정**한다. 사람이 읽는 섹션 경로는 별도 열에 둔다.
    실측: 한 배치만 3번째 열이 `"… / claim L104"` 형태여서 17행의 줄번호가 통째로 잘못 들어갔고,
    "미분류 9건" 오탐으로 이어졌다. 조인 결과 건수를 **입력 건수와 대조**해야 잡힌다.
26. **basename 단독 매칭으로 참조를 다른 모델에 귀속** → §CROSS-MODEL RESOLUTION.
    실측: Delft3D 가 번들한 SWAN 사본으로 6건 오귀속 위험, ADCIRC `wind.F` 41건 동명 충돌.
27. **생성 파일 인용을 미해결로 분류** → `switch.pl` 전처리 매핑. 실측 SWAN 8건 + 확장자불일치 1건.
28. **롤백 자산(`.old-<sha>`)이 색인을 오염** → 색인 제외 규칙. 미적용 시 전 파일이 AMBIGUOUS.

ROMS 파일럿 추가(29–31).

29. **이중 배치 소스를 임의 귀속** → 노트 선언 `component:` 근거, 없으면 AMBIGUOUS 유지.
    실측: `ana_*.h` 41쌍이 배포본/템플릿으로 내용이 다름, 78건 충돌.
30. **모양 기반 오탐 억제가 실재 참조를 죽임** → 파서에서 걸러내지 말고 ledger 에서 맥락 분류.
    실측: "짧은 stem 억제" 규칙이 `io.F`·`bc.F` 등 실재 참조 19건을 함께 제거.
31. **노트가 pinned 보다 앞선 서술을 stale 로 오분류** → `AHEAD_OF_SNAPSHOT` 로 구분,
    migration 후 내용 정정 단위로 분리. 실측: `roms_4dvar.md` 28건.
25. **잠금 검증을 root 로 실행해 무의미해짐** → `find <path> -writable` 은 root 에서 권한 비트와 무관하게
    참이다. 잠금 확인은 **소유자가 아닌 일반 사용자 권한으로** 실행하거나 `-perm` 비트로 검사한다.
    실측: sudo 스크립트 최종 단계가 `82713개 쓰기 가능`으로 오탐 실패, 실제 잠금은 정상이었다.

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

### CROSS-MODEL RESOLUTION (2026-09-20 신설, SWAN 파일럿 후속)

**basename 단독 매칭은 참조를 엉뚱한 모델로 귀속시킨다.** Delft3D 가 SWAN 을 번들하고,
ADCIRC 모델 아래 `adcirc` 와 `asgs` 두 저장소가 같은 `wind.F` 를 갖는다.
해소 순서를 고정한다 (`resolver.py`, 게이트 `test_resolver.py`).

1. 소유 모델 안에서 **경로 suffix 일치** (참조가 디렉터리 성분을 가질 때)
2. 소유 모델 안에서 basename 일치
3. 동명 후보가 남으면 좁힌다 — ⑴ **줄 번호 배제**: 인용된 최대 줄보다 짧은 파일은 그 인용의 대상일 수 없다
   ⑵ **주 저장소 우선**: 저장소 디렉터리명이 모델명과 일치하는 쪽. 결과는 `RESOLVED_NARROWED` 로 구분 기록
4. **생성 파일 매핑**: SWAN/SWASH 는 `switch.pl` 이 `.ftn90 → .f90`, `.ftn → .f` 로 전처리한다.
   노트가 생성물 이름을 인용할 수 있다 (`RESOLVED_GENERATED`). 확장자 짝이 어긋나면
   `RESOLVED_GENERATED_EXT_MISMATCH` 로 해소하되 표시한다
5. cross-model: 소유자가 하나면 `RESOLVED_CROSS_MODEL` 로 귀속 기록, 여럿이면 `AMBIGUOUS_CROSS_MODEL`
   (번들 사본 가능성 — 임의 귀속 금지)
6. 실패 → `UNRESOLVED_SOURCE_REFERENCE`

**부분 이름은 추측으로 해소하지 않는다** (`Compdata.f90` ← `SwanCompdata.ftn90`, `PDataSets.ftn90` ← `SwanVTKPDataSets.ftn90`).

#### 이중 배치 소스 — 노트 선언 component 로 귀속 (2026-09-20, ROMS 파일럿)

같은 저장소 안에서 **배포본과 사용자 템플릿이 같은 이름·다른 내용**으로 공존할 수 있다.
ROMS 는 `ana_*.h` 41쌍을 `ROMS/Functionals/`(배포본)와 `User/Functionals/`(템플릿)에 두고
**전부 내용이 다르다**(`ana_grid.h` 1,221 vs 566줄). 줄 번호 배제도 듣지 않는다(78건 중 74건이 양쪽 가능).

3단계(좁히기)가 실패하면 **노트 frontmatter 의 `component:` 선언**을 귀속 근거로 쓴다.
노트가 스스로 대상 경로를 밝힌 것이므로 추측이 아니다. 결과는 `RESOLVED_BY_COMPONENT` 로 구분 기록한다.
선언이 없거나 후보를 가르지 못하면 AMBIGUOUS 를 유지한다 — **임의로 한쪽을 고르지 않는다.**
실측: ROMS AMBIGUOUS_SAME_MODEL 78 → 1.

#### 변종 트리 — `source_scope` 선언 (2026-09-20, Celeris)

`component:` 는 값이 **경로 형태일 때만** 후보를 가른다. 그렇지 않은 모델이 더 많다 —
Celeris 노트 17개는 `component` 자체가 없고, CADMAS-SURF 는 자유서술(`src (CADMAS-SURF/3D2F …)`)이다.

그래서 노트가 **분석한 저장소 상대 디렉터리 접두사**를 직접 선언한다.

```yaml
source_scope: Celeris-WebGPU/js, Celeris-WebGPU/shaders
```

해소 시 이 접두사로 후보를 거르고 `RESOLVED_BY_SCOPE` 로 기록한다.
모델별 등록표가 필요 없고 변종 구조가 달라도 같은 방식이 쓰인다.

**선언 전에 근거를 확인한다.** Celeris 실측: 노트의 `transect` 언급 0건,
인용문 판별 대조에서 `transect만` 0 · `main만` 46, 인용 디렉터리가 11개 노트 모두 동일.
변종 내용은 실제로 다르다(70쌍 중 60쌍). → 484건 전부 `RESOLVED_BY_SCOPE`.

**휴리스틱으로 대체하지 않는다.** "얕은 경로(base tree) 우선" 규칙은 Celeris 만 풀고
CADMAS-SURF(3D vs 3D2F)·FUNWAVE(TVD vs GPU)는 후보 깊이가 같아 듣지 않는다.

| 모델 | 변종 | 내용 차이 | 잔여 |
|---|---|---|---|
| Celeris | `transect_version/` | 70쌍 중 60 | **0** (선언 완료) |
| CADMAS-SURF | `CADMAS-SURF-3D` ↔ `-3D2F` | 212쌍 중 100 | 331 |
| FUNWAVE | `FUNWAVE-TVD` ↔ `FUNWAVE-GPU` | 29쌍 중 27 | 120 |
| LISFLOOD-FP · Delft3D · XBeach | 저장소 내부 중복 | 미조사 | 41 · 37 · 8 |

남은 모델은 해당 migration 착수 시 같은 절차(근거 확인 → 선언)로 처리한다.

#### 모양 기반 억제 금지 (2026-09-20, ROMS 파일럿에서 설계 변경)

참고문헌 이니셜(`Shchepetkin, A.F.` → `A.F`)과 슬래시·플러스 축약(`exchange_2d/3d/4d.F`,
`nl/ad/tl/rp_roms.h`, `i4dvar.F+i4dvar_roms.h`)이 파일 참조로 오인된다.
**"짧은 stem 은 참조가 아니다" 같은 모양 규칙으로 억제하면 안 된다** — 검증 결과 그 규칙은
실재 파일 참조 **19건**(`io.F` 7 · `bc.F` 8 · `gp.c` · `oc.c` · `df.c`)을 함께 죽인다.

따라서 이들은 파서에서 걸러내지 않고, **해소 실패 후 coverage ledger 에서 맥락으로 분류**한다.

| ledger 분류 | 판별 근거 |
|---|---|
| `NOT_A_REFERENCE_BIBLIOGRAPHIC` | 미해소 + 같은 줄이 저자·연도 인용 형식 |
| `NOT_A_REFERENCE_ABBREVIATION` | 미해소 + 슬래시/플러스 축약 표기. **자동 전개 금지**(어느 조합인지 단정 불가) |
| `UNRESOLVED_SOURCE_REFERENCE` | 나머지 |

숫자 stem 축약(`swancom1/5.ftn`)만 파서의 `NUMERIC_STEM` anomaly 로 남긴다 —
그 형태는 실재 파일과 충돌하지 않음이 확인됐기 때문이다.

**migration 롤백 자산(`<tree>.old-<sha>`)은 색인에서 제외한다.** 포함하면 모든 파일이 동명 2중이 되어
전부 AMBIGUOUS 로 오판정된다. 롤백 자산을 트리에 남겨 두는 동안 참조 해소가 오염되는 것은
7일 보관 규칙의 부작용이며, 제외 규칙으로 막는다.

도입 효과 (미해소 참조):

| 모델 | 도입 전 | 도입 후 | 해소 경로 |
|---|---|---|---|
| SWAN | 29 | **5** + AMBIGUOUS 1 | cross-model 15, 생성물 8, 확장자불일치 1 |
| EFDC | 89 | **9** | 대부분 경로·모델 귀속 문제였다 |
| ADCIRC | 30 + 동명 48 | **30** + AMBIGUOUS 1 | 좁히기 47 (`wind.F` 41 포함) |

### UNCITED PROSE SWEEP (2026-09-20 신설, EFDC 파일럿)

**교집합 기반 후보 추출은 인용 없는 산문을 구조적으로 놓친다.** 노트는 근거 절에만 `file:line` 을 달고,
같은 사실을 Decision Guide·Working Rules·Pitfalls·요약에서 인용 없이 반복하는 것이 정상적인 작성 패턴이다.
표만 고치면 같은 노트 안에서 본문이 모순된다.

절차 — UPDATE_REQUIRED 의 원인이 **식별자의 제거·이름변경·의미변경**이면:
1. 그 식별자로 canonical 전체(`models/`·`concepts/`·`textbook/`)를 grep 한다. 인용 유무를 가리지 않는다.
2. 각 출현을 **문장 단위로** 판정한다. 문자열이 있다는 이유로 자동 수정하지 않는다.
   - 같은 사실을 **직접 단언** → 수정 대상
   - 동작을 단언하지 않는 백로그·계획·목차 항목 → 대상 아님. 별도 보고
   - 버전이 명시된 과거 검증 기록(frontmatter `verification_method` 등) → 불변
3. 수정문에는 **적용 버전 범위를 명시**한다. 같은 식별자가 레거시 트리에 살아 있으면 특히 그렇다.
4. 노트 요약·`> 정체` 블록도 검사 대상이다. 본문만 고치면 요약이 모순으로 남는다.

EFDC 실측: `IINTPG` 분기 제거로 산문 **7곳**이 수정 대상이 됐고 그중 후보 목록에 있던 것은 **0곳**이었다.
2곳(백로그 항목, 유지되는 입력 카드 서술)은 판정 결과 제외. 요약 1곳(`efdc_baroclinic_eos.md:21`)은
1차 목록에서 누락돼 사후 검증에서 잡혔다 — 요약 검사를 절차에 넣은 근거다.

### EXCLUDED REFERENCE LEDGER (2026-09-20 신설, EFDC 파일럿)

코드블록·frontmatter 안의 참조는 **탐지하되 자동 수정하지 않는다**(§REFERENCE GRAMMAR). 그 결과
snapshot 을 올린 뒤 이 참조들만 옛 좌표로 남는다. 설계된 동작이지만 **기록하지 않으면 조용한 부채**가 된다.

- 제외 참조 중 **변경 파일을 가리키는 것**을 별도 ledger 에 집계한다(`excluded-refs.csv`: note, line, ref, source, disposition).
- disposition ∈ {STALE_AFTER_BUMP, STILL_VALID, MANUAL_FIXED}. 완료 판정 시 미분류 행이 있으면 안 된다.
- EFDC 실측: **9건**(`efdc_dispersion.md` 의 Fortran 주석 인용 등)이 snapshot 교체 후 실제로 어긋난 상태로 남았다.

### NEW FILE RULE (보완)

신규 파일이 위키에서 **직접 인용되지 않아도**, 변경된 기존 파일에서 로직이 신규 파일로 **이동·분리**됐는지 확인한다. `new file + 관련 기존 파일 변경` 이면 semantic-review candidate 로 올린다.
**regression case**: EFDC v12.5 의 `EFDC/Transport/caltran_quickest.f90`(+503, 신규) · `EFDC/Transport/mod_quickest.f90`(+115, 신규) ↔ `EFDC/Transport/calconc.f90`(+59/−42, 기존·노트 인용 있음).

**신규 파일이 사전 스캔에 없을 수 있다.** 사전 스캔은 변경 파일만 선택적으로 받으므로 신규 파일 본문이
로컬에 없을 수 있다. 이때 좌표는 **patch 전문에서 확정**한다(신규 파일 patch 는 전체가 추가 줄이므로
`+` 줄 순서가 곧 새 파일의 줄 번호다). 근거 없이 추정하면 환각이다 — EFDC 에서 이 경로로
`caltran_quickest.f90:14-33`(서브루틴 헤더)·`mod_quickest.f90:80-101`(ULTIMATE limiter) 을 확정했고
사후 검증에서 patch 원문과 대조했다.

## ACCEPTANCE CRITERIA

v1 1–8 + 추가:
9. coverage ledger 완결(탐지 = resolved + unresolved + excluded), 알려진 실제 인용 예가 탐지에 포함됨.
10. REVIEW_ONLY 전 행에 disposition 또는 보류 사유. unresolved·AMBIGUOUS 잔존 시 완료 판정 금지(보류 결정은 명시적으로).
11. 자동 수정 건은 전부 §AUTOMATION BOUNDARY 5조건 충족 기록.
12. `validate-all` 통과·broken reference 0 은 **필요조건일 뿐** 완료 근거가 아니다.
13. `UNRESOLVED_SOURCE_REFERENCE` 전건이 ledger 에 분류되어 있고 자동 NO_ACTION 으로 처리되지 않음.
14. **PARSER GATE 통과**(§PARSER SELF-TEST) — 실패 시 `PARSER_GATE_FAILED` 로 종료, migration 미착수.
14b. **RESOLVER GATE 통과**(§CROSS-MODEL RESOLUTION) — 실패 시 `RESOLVER_GATE_FAILED` 로 종료.
    참조가 어느 모델·파일에 귀속되는지 틀리면 impact filter 전체가 틀린다.
15. UPDATE_REQUIRED 의 원인이 식별자 변경이면 **§UNCITED PROSE SWEEP 수행 기록**이 있고, 각 출현에 문장 단위 판정이 남아 있음.
16. `excluded-refs.csv` 의 전 행에 disposition 이 있음(§EXCLUDED REFERENCE LEDGER).
17. 분류·좌표 산출물의 조인 결과 건수가 입력 건수와 일치함(§FAILURE MODES 24).
18. 적용 후 **변경 파일 대상 인용이 새 snapshot 에서 전부 해석**됨(파일 존재 + 범위 내). EFDC 실측 374/374.
19. 잠금 확인이 일반 사용자 권한으로 수행됐고 결과가 0임.
20. 동명 다중 후보가 남았으면 AMBIGUOUS 로 보고돼 있고 **조용히 RESOLVED 된 건이 없음**.
    귀속에 쓴 근거(줄 번호 배제 / 주 저장소 / 노트 component)가 건별로 기록돼 있음.
21. `AHEAD_OF_SNAPSHOT` 참조를 가진 노트는 좌표 정비와 **별도 단위**로 분리돼 있음.

## PILOT ROLLOUT ORDER

**commit 수로 난이도를 판단하지 않는다.** 착수 전 ⑴ 변경 파일 ⑵ 인용 교집합 ⑶ 줄 이동 수 ⑷ 의미 변경 후보 ⑸ broad·unresolved 수를 먼저 뽑아 시험 범위를 확인한다.

| 순서 | 대상 | 상태 | 결과·선정 근거 |
|---|---|---|---|
| 1차 | ADCIRC/adcirc | **종료 2026-09-20** | `6037225`→`e8b62a70`. 14커밋/31파일 → 의미 2 + 좌표 116(+bare 58), 노트 35 무변경 |
| 2차 | EFDC/EFDCPlus_Stable | **종료 2026-09-20** | `3ed76b6`→`3b382fd`. 38파일 → 78건 판정(UR 11 / RO 47 / NA 20), 노트 31 반영, 산문 7 |
| 3차 | **SWASH 또는 SWAN** | 다음 | bare 1,246 / file:line 440(SWASH), 문법·문맥 해석 회로 검증. *SWASH 는 CURRENT 이므로 파서 검증 전용* |
| 4차 | ROMS/roms(+6, file:line 1,196), Celeris(+10), asgs, hydromt | | 소규모 다수 |
| 5차 | Delft3D | | 대형 tree·예산 승인 회로 |
| 별도 | non-git 3, FUNWAVE-GPU | | 전용 회로 |

두 파일럿에서 확인된 규모 관계: **커밋 수는 작업량을 예측하지 못한다.** EFDC 는 squash 된 +1 커밋이었으나
38파일·78 판정·31노트로 ADCIRC(14커밋)보다 컸다. 착수 전 사전 스캔 5지표를 뽑는 규칙을 유지한다.

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

## CHANGELOG (v2 후보 → v2.0 FINAL)

EFDC 파일럿(2026-09-20) 실측 반영. 설계 원칙 변경은 없고 **누락된 절차의 명문화**다.

| 추가 | 근거 |
|---|---|
| §AUTOMATION BOUNDARY 4 의 내부 변경 판정표 | "범위 폭" 기준이 실무에서 작동하지 않음. 판정 이력 기준으로 교체(EFDC 31건) |
| §UNCITED PROSE SWEEP | IINTPG 산문 7곳 중 후보 0곳 — 교집합 필터의 구조적 사각지대 |
| §EXCLUDED REFERENCE LEDGER | 제외 영역 참조 9건이 교체 후 어긋난 채 남음 |
| NEW FILE RULE 의 patch 기반 좌표 확정 | 신규 파일이 사전 스캔에 없을 수 있음 |
| §LOCKING 의 단일 게이트·LFS·잠금 검증 권한 | 좌표 기준 일관성, `find -writable` root 오탐 |
| failure mode 22–25, acceptance 15–19 | 위 항목의 게이트화 |

## 미해결 — ADCIRC 파일럿 잔여 (별도 보고, 사용자 결정 대기)

v1 파서 결함(확장자 순서)으로 ADCIRC 파일럿이 놓친 참조가 **2건** 확인됐다(둘 다 `models/ADCIRC/source-analysis/adcirc-swan-coupling.md`).
- 26행 `thirdparty/swan/SwanReadADCGrid.ftn90:44-153` → 새 baseline 기준 `44-158`
- 83행 `SwanReadADCGrid.ftn90:44-103` → `44-108`
같은 파일 참조 11건은 줄 이동이 없어 영향 없음. 처리 여부는 사용자 결정(작은 후속 수정 또는 backlog 편입).
