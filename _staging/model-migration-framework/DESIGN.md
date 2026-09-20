# MODEL SNAPSHOT MIGRATION FRAMEWORK — 설계안

> 상태: **설계 단계, 미구현.** 이 문서 작성 외에 `models/` 수정·Codex 호출·도구 구현은 하지 않았다.
> 근거: ADCIRC 파일럿(커밋 `e4392f3`·`53f5248`·`1a8e232`)에서 검증된 절차 + 2026-09-20 실측.
> 작성: Claude Opus 5(사용자 승인 예외). 기준 문서: [PROJECT_REQUIREMENTS.md](../../PROJECT_REQUIREMENTS.md), [CLAUDE.md](../../CLAUDE.md), [CONVENTIONS.md](../../CONVENTIONS.md).

## GOALS

1. pinned snapshot → upstream 전환 시 **위키의 어느 근거가 깨지는지**를 저장소 유형과 무관하게 같은 방식으로 판정한다.
2. 읽을 양을 **변경 파일 ∩ 위키 참조 파일 → 변경 hunk ∩ 참조 지점** 순으로 줄여, 커밋 수와 무관하게 비용이 위키 참조 밀도에 비례하게 만든다.
3. 판정·적용·검증의 각 단계가 기계 검증 가능한 산출물(manifest·CSV·hash)을 남긴다.
4. historical provenance 를 보존하면서 current validation 을 따로 기록한다.

## NON-GOALS

- 위키 노트의 기술 서술 개선·정규화(예: bare reference → file-qualified). 별도 hygiene 작업.
- 모든 저장소를 최신으로 올리는 것. 전환은 근거 영향이 확인된 저장소만, 건별 승인.
- upstream 코드 리뷰·결함 탐색. 이 프레임워크는 **위키 근거 영향** 만 다룬다.
- 빌드·실행 검증. 근거 수준(`BUILD-PLAN.md` §4)의 "실행 확인" 이상은 범위 밖.

## REPOSITORY CLASSIFICATION

2026-09-20 실측(26 git + 3 non-git). BEHIND 14 / CURRENT 12 / UNKNOWN 3.

| 유형 | 정의 | 해당 | 비교 방법 |
|---|---|---|---|
| **A. 일반 git** | full clone, HEAD 이동 가능 | (현재 없음 — 전부 shallow) | `git diff old..new` |
| **B. shallow git** | `--depth 1` clone, 대상 커밋만 보유 | BEHIND 13 + CURRENT 다수 | staging 에 `--depth 1` clone 후 baseline 커밋을 **추가 fetch** → 두 커밋 간 `git diff --name-status` (ADCIRC 에서 검증) |
| **C. 대형 차이 git** | 변경 파일 수가 크거나 커밋 수백~수천 | `Delft3D`(+1,771), `hydromt_delft3dfm`(+29), `asgs`(+20) | 커밋 순회 금지. **tree 대 tree** 비교(§CHANGE DETECTION 2단계) |
| **D. local patch 보유** | 추적 파일에 로컬 수정 | `FUNWAVE-GPU`(3파일) | §LOCAL-PATCH HANDLING |
| **E. non-git / provenance 불완전** | commit 부재 또는 로컬 확인 불가 | `LISFLOOD-FP`, `SFINCS`(선언 SHA 있으나 .git 없음), `XBeach/trunk`(svn export) | §NON-GIT FALLBACK |

유형은 배타적이지 않다(예: Delft3D = B+C). 저장소마다 유형 집합을 manifest 에 기록한다.

## INPUTS

| 입력 | 출처 | 비고 |
|---|---|---|
| pinned snapshot | `_staging/source-snapshots-20260919/manifest.csv` | pinned SHA·날짜·branch·shallow·origin |
| provenance 판정 | `provenance-final.csv`, `provenance-notes-adcirc.csv` | historical / current_validated / worktree_state |
| upstream 상태 | GitHub·GitLab API, `git ls-remote` (Claude 가 수집 — Codex 샌드박스는 네트워크 차단) | |
| 위키 참조 | 각 모델 노트(`models/<model>/**/*.md`, raw 제외) | §REFERENCE GRAMMAR |
| 잠금 상태 | `stat`(root·read-only) | 적용 방식 선택에 필요 |

## REFERENCE GRAMMAR

실측(2026-09-20, 13 모델 472 노트): `file:line` 5,036 · 파일만 8,755 · bare `:NNN` 4,809 · backtick symbol 14,999.

**모델마다 인용 문체가 다르다.** 프레임워크는 이 차이를 전제로 한다.

| 모델 | file:line | 파일만 | bare | 특징 |
|---|---:|---:|---:|---|
| Delft3D | 1,491 | 1,198 | 806 | file:line 중심, 규모 최대 |
| ROMS | 1,196 | 1,227 | 388 | file:line 중심 |
| XBeach | 620 | 484 | 247 | 혼합 |
| EFDC | 510 | 641 | 247 | 혼합 |
| ADCIRC | 339 | 1,014 | 118 | 파일 단위 우세(파일럿 완료) |
| **SWAN** | **0** | 1,353 | 129 | **file:line 없음** — 파일·심볼 기반 |
| **SWASH** | **0** | 740 | **1,246** | **bare 지배** — 절 문맥 의존 |
| SFINCS | 89 | 197 | 890 | bare 지배 |
| LISFLOOD-FP | 27 | 522 | 322 | 파일·bare |

| 유형 | 예 | 자동 식별 | source 해석 | confidence | 자동 수정 |
|---|---|---|---|---|---|
| `file:line` | `` `gwce.F:1064` `` | 가능 | 파일명 → repo 내 유일 경로 | high | **허용**(내용 동일성 확인 시 줄 번호만) |
| `file:start-end` | `` `vsmy.F:1479-1486` `` (hyphen·en dash 모두) | 가능 | 〃 | high | 허용(양 끝 줄 내용 동일성 확인) |
| bare `:line` / `:start-end` | `` (`:2271`) `` | 가능(탐지) | **문맥 해석 필요**: 같은 줄 → 상위 60줄 내 마지막 명시 파일 → 절 머리말 | medium | **조건부**: 심볼 근접 확인(±6줄) 시 허용, 아니면 보고만 |
| 파일만 | `` `couple2swan.F` `` | 가능 | 경로 해석 | high | 수정 불필요(존재 확인만) |
| 심볼 | `` `PADCSWAN_RUN` `` | 가능 | 새 트리 전수 검색 | medium | 수정 금지(존재/소멸만 보고) |
| 파일+심볼 | `` `nodalattr.F` 의 `readNodalAttrXDMF` `` | 가능 | 파일 내 심볼 위치 | high | 줄 번호 동반 시 허용 |
| 산문 내 경로 | "…`models/EFDC/raw/.../svdcmp.for` 를 보면" | 부분 | 경로 그대로 | medium | 존재 확인만 |
| frontmatter·코드블록 내 참조 | `verification_method`, ```` ```fortran ```` 안 | 부분 | 파서에서 **제외**(오탐 방지), 별도 보고 | low | 금지 |

**규칙**: 동명 파일이 여러 repo 에 있으면(예: `wind.F` = adcirc/asgs) 경로 조각으로 좁히고, 그래도 둘 이상이면 **AMBIGUOUS** — 자동 수정 금지. 줄 번호만 보고 파일을 추정하지 않는다.

## CHANGE DETECTION PIPELINE

```
[0] snapshot manifest      pinned SHA / upstream HEAD / release / 유형
        ↓
[1] 참조 인덱스 생성        모델 노트 → REFERENCES.csv (grammar 별 분류)
        ↓
[2] 변경 파일 집합          tree vs tree (대형은 여기서 종료 조건 판정)
        ↓  ∩
[3] 위키 참조 파일 집합      [1] 에서 파일 단위로 축약
        ↓   → 교집합이 0 이면 전체 NO_ACTION, 여기서 종료
[4] 교집합 파일의 diff/hunk  해당 파일만 patch 확보
        ↓  ∩
[5] 참조 지점(줄·심볼)       hunk 범위와 교차 판정 + old→new 줄 매핑
        ↓
[6] 영향 분류               UPDATE_REQUIRED / REVIEW_ONLY / NO_ACTION
```

**[2] 변경 파일 집합 — 규모별 방법**

| 규모 | 방법 | 비고 |
|---|---|---|
| 작음(≤ 수십 파일) | GitHub `compare` API | ADCIRC 에서 사용. **파일 300개 상한** — `files` 배열이 잘리면 즉시 아래 방법으로 전환 |
| 큼·불확실 | staging clone(`--depth 1`) + baseline 커밋 fetch → `git diff --name-status <old> <new>` | 상한 없음. ADCIRC 에서 31/31 일치 확인 |
| API 불가·non-git | 두 트리의 **파일 manifest(path·size·sha256)** 비교 | §NON-GIT FALLBACK 과 동일 회로 |

패치는 **교집합 파일에 한해** 확보한다(`git diff <old> <new> -- <path>`). 전체 diff 를 만들지 않는다. Delft3D(+1,771)에서도 읽는 patch 는 교집합 크기에만 비례한다.

## IMPACT CLASSIFICATION

3단계만 유지한다(하위 상태는 열로 표현하고 새 분류를 만들지 않는다).

| 분류 | 판정 기준 |
|---|---|
| **UPDATE_REQUIRED** | 좁은 근거(줄 범위 ≤ 60줄, 심볼 지정, 인용문)와 변경 hunk 가 겹치고 **의미가 달라짐** — 서술·수치·상태(예: "PR OPEN")가 새 baseline 과 불일치 |
| **REVIEW_ONLY** | 변경 파일을 인용하나 의미 영향 미확인 — ⑴ 절·파일 단위 broad reference ⑵ 줄 이동만(내용 동일) ⑶ 심볼 존속 |
| **NO_ACTION** | 변경 파일과 노트 근거가 교차하지 않음 |

보조 열: `line_shift`(yes/no/unknown), `evidence_width`(narrow/broad), `ref_type`, `content_identity`(동일/변경/매핑불가), `escalated_from`.
REVIEW_ONLY 처리 중 내용 불일치가 드러나면 **UPDATE_REQUIRED 로 승격**하고 보고한다(자동 수정 금지).

## NON-GIT FALLBACK

`LISFLOOD-FP`(Zenodo zip v8.2), `SFINCS`(태그 clone, .git 제거), `XBeach/trunk`(svn export r6155).

1. **historical file manifest** 를 만든다: 현재 설치본의 path·size·sha256 (없으면 지금 생성해 고정).
2. upstream 배포본(zip·태그 아카이브·svn export)을 staging 에 받아 같은 형식의 **current manifest** 를 만든다.
3. 두 manifest 를 비교해 ADD/MODIFY/DELETE 집합을 만들고, **[3] 이후 회로는 git 과 동일**하게 적용한다.
4. 버전 메타데이터(`configure.ac $Revision$`, `VersionHistory.h`, `docs/developments.rst`)는 **보조 증거**일 뿐 — 소스 내 버전 문자열을 신뢰하지 않는다(LISFLOOD-FP 8.1.0 stale 헤더 선례).
5. provenance 가 부족하면 `CONFLICTING_EVIDENCE` 또는 `INSUFFICIENT_PROVENANCE` 로 남긴다. 파일 수·크기 일치만으로 MATCH 로 승격하지 않는다(LISFLOOD-FP 3,170 vs 1,672 미해결 선례).

## LOCAL-PATCH HANDLING

대상: `FUNWAVE-GPU`(추적 파일 3개 수정 — Blackwell 포팅).

migration **전에** 고정한다.
1. `git diff HEAD > <staging>/local.patch` + 해당 파일들의 sha256 manifest.
2. `LOCAL_PATCH` 레코드: 파일 목록·패치 해시·작성 경위·관련 노트.
3. 새 snapshot 에 패치 재적용 가능 여부를 staging 에서 시험(`git apply --check`). 충돌 시 **migration 중단**하고 보고 — 자동 3-way merge 금지.
4. 노트 근거는 `BASE_PROVENANCE + LOCAL_PATCH` 조합임을 명시하고, 재현 절차에 패치 경로를 남긴다.

## PROVENANCE MODEL

네 축을 분리한다. 새 snapshot 과 호환된다는 이유로 **historical 을 소급 변경하지 않는다.**

| 축 | 의미 | 갱신 시점 |
|---|---|---|
| `historical_source_provenance` | 그 노트가 작성·검증될 때 본 snapshot | **불변** |
| `current_validated_against` | 새 snapshot 기준으로 실제 재검증된 경우만 | 재검증 수행 시 |
| `worktree_state` | CLEAN / CLEAN_TRACKED / MODIFIED / NO_VCS | 설치본 상태 변화 시 |
| `reproducibility` | BASE_SHA / BASE_SHA_PLUS_LOCAL_PATCH / DECLARED_SHA_UNVERIFIABLE_LOCALLY / SNAPSHOT_UNVERIFIABLE_LOCALLY | 〃 |

노트 상태: `SEMANTICALLY_UPDATED` / `LINE_REFERENCE_ONLY` / `REVIEWED_NO_CHANGE` / `NO_ACTION`. 기계적 줄 갱신은 `maintenance` 열로만 기록하고 새 semantic validation 을 부여하지 않는다.

## LOCKING / APPLY PROCEDURE

`CLAUDE.md` 역할 분담 절의 두 방식을 그대로 쓴다. **작업 시작 전에 어느 방식인지 명시한다.**

- **A. INSTALL-STYLE** (snapshot 교체·root 소유 파일 배치): staging clone → manifest A(staging)·B(설치본)·C(전이) → pre-apply gate → 사용자 sudo(백업 tar → 고유 이름 rename → 복사 → `chown root:root` → `chmod -R a-w`) → post-apply manifest D 전수 대조 → 롤백 자산 보존.
- **B. SCOPED EDIT** (승인된 노트 수정): 대상 경로만 unlock → 승인 범위 수정 → diff·hash·validation → 즉시 relock → 쓰기 가능 0 확인.

공통: 삭제 명령 금지(rename·보존), 기존 rollback 경로·백업이 있으면 덮어쓰지 않고 BLOCKED, 검증 완료 전 롤백 자산 삭제 금지.

## CODEX / CLAUDE ROLE SPLIT

| 단계 | 담당 | 비고 |
|---|---|---|
| upstream 상태 수집(API·ls-remote) | **Claude** | Codex 샌드박스는 네트워크 차단(실측 확인) |
| staging clone·tree manifest·해시 | Codex | bounded task |
| 참조 인덱스 추출(REFERENCES.csv) | Codex | grammar 는 Claude 가 고정 |
| 교집합·hunk 매핑·줄 매핑 | Codex | 결정적 계산 |
| 영향 분류 초안 | Codex | 판정 근거 필수(파일:줄) |
| **분류 검증·승격 판단·의미 수정** | **Claude** | Codex 판정 미채택 원칙(ADCIRC 에서 21→2 로 정정한 선례) |
| provenance 정책·acceptance·최종 판단 | **Claude** | |
| sudo 적용 | **사용자** | |

## OUTPUT SCHEMA

저장소마다 `_staging/<model>-upstream-review-<date>/`:

| 파일 | 내용 |
|---|---|
| `snapshot.json` | pinned/upstream/release/유형/수집 시각·방법 |
| `changed-files.csv` | path, status(A/M/D/R), old_sha, new_sha, in_wiki_refs(bool) |
| `REFERENCES.csv` | note, note_line, ref_type, ref_file, line_start, line_end, symbol, context |
| `impact.csv` | commit_or_none, file, ref(note:line), classification, evidence_width, line_shift, content_identity, rationale |
| `manifest-{A,B,C,D}.csv` | staging / 설치본 / 전이 / 적용후 |
| `note-status.csv` | note, status, historical, current_validated, maintenance |
| `DECISIONS.md` | 승격·제외·AMBIGUOUS 와 근거 |

## FAILURE MODES

| # | 실패 | 방지 |
|---|---|---|
| 1 | GitHub compare 300파일 상한에 잘린 목록을 전체로 오인 | 파일 수 ≥ 300 또는 `truncated` 플래그면 tree 비교로 전환, 두 방법 결과 교차 확인 |
| 2 | 줄 번호만 보고 파일 추정 | bare reference 는 문맥 파일 + 심볼 근접 확인 없으면 AMBIGUOUS |
| 3 | 동명 파일 오결(`wind.F`) | repo·경로 조각으로 좁히고, 남으면 AMBIGUOUS |
| 4 | 노트가 인용한 줄이 hunk 안이라 매핑 불가한데 자동 치환 | 매핑 실패는 수정 금지·보고 |
| 5 | 코드블록·frontmatter 안 텍스트를 참조로 오탐 | 파서에서 제외 |
| 6 | Codex 판정 과다(파일 인용만으로 IMPACTING) | Claude 가 hunk ∩ 참조 폭으로 재판정 |
| 7 | local patch 유실 | migration 전 patch 고정 + `git apply --check` |
| 8 | provenance 소급 오염 | historical 불변 규칙 + 기계적 갱신은 maintenance 열 |
| 9 | 잠금 해제 상태 방치 | SCOPED EDIT 후 즉시 relock + 쓰기 가능 0 확인 |
| 10 | en dash·`L` 접두 등 표기 변형 누락 | 치환 패턴에 `[-–]`·`L?` 포함(ADCIRC 에서 15건 누락 후 수정한 선례) |
| 11 | 대형 저장소에서 교집합이 커 비용 폭증 | 교집합 규모를 먼저 보고하고 **사용자 승인 후** 다음 단계 진행 |

## ACCEPTANCE CRITERIA

저장소 1건 migration 완료 조건:
1. 설치본 HEAD(또는 manifest) = 목표 snapshot, staging ↔ 설치본 해시 전수 일치, 예상 밖 변경 0.
2. 교집합·분류 산출물이 모두 존재하고, Claude 재판정 결과가 기록됨.
3. UPDATE_REQUIRED 전건 수정 또는 사용자 보류 결정.
4. REVIEW_ONLY 의 줄 이동분 갱신 완료, 내용 동일성 검사 통과. AMBIGUOUS 자동 수정 0.
5. `validate-all` 통과, G8e·broken reference 0, semantic 텍스트 변경은 승인 범위 내.
6. provenance 네 축 갱신, historical 불변 확인.
7. 롤백 자산 존재·검증(백업 해시·`.old-<sha>` 보존), 잠금 복구.
8. 커밋 분리: 운영 결과물 / audit artifact.

## PILOT ROLLOUT ORDER

난이도·위험도 = (변경 규모) × (위키 참조 밀도) × (참조 문법 난이도) × (provenance 불확실성).

| 순서 | 대상 | 변경 | 참조(file:line/bare) | 난이도 | 이 단계에서 검증할 것 |
|---|---|---|---|---|---|
| **2차(권장)** | **EFDC/EFDCPlus_Stable** | +1 커밋 | 510 / 247 | 낮음 | ADCIRC 와 다른 인용 문체에서 파이프라인 재현. 모델 가치 높고 변경 작음 |
| 3차 | ROMS/roms | +6 | 1,196 / 388 | 중 | file:line 밀도 최고 수준에서 교집합·줄 매핑 확장 |
| 4차 | Celeris(+10), ADCIRC/asgs(+20), hydromt(+29) | 소~중 | 낮음 | 중 | 부속 저장소 처리, ADCIRC 잔여 repo 정리 |
| 5차 | **SWAN** | ? (GitLab) | **0** / 129 | **높음** | **file:line 이 없는 문법**(파일·심볼 기반) 회로 검증 + GitLab 경로 |
| 6차 | **Delft3D** | **+1,771** | 1,491 / 806 | **최고** | 대형 tree 비교, 교집합 규모 사전 승인 게이트 |
| 7차 | 잔여 소규모(StormEvents·roms_eccofs·roms_matlab·roms_test·roms-jedi·ShorelineS) | +1~6 | 낮음 | 낮음 | 일괄 처리 |
| 별도 | LISFLOOD-FP·SFINCS·XBeach(non-git), FUNWAVE-GPU(local patch) | — | — | 높음 | §NON-GIT / §LOCAL-PATCH 회로 검증 |

**2차 파일럿 제안: EFDC/EFDCPlus_Stable.** 변경이 1커밋이라 실패 비용이 낮고, EFDC 는 노트 50개·file:line 510건으로 파이프라인의 참조 처리 부분을 실질적으로 시험할 수 있다. SWAN·Delft3D 같은 고난도는 그 뒤로 미룬다.
