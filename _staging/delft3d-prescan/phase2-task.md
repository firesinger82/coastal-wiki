# CODEX TASK — Delft3D Phase 2 의미 검토 (41건)

```
OBJECTIVE
  Delft3D pinned 513eccd → upstream 231bbf2 변경이 위키 주장의 의미를 바꾸는지
  후보 41건(11개 노트)을 판정한다. 위키는 수정하지 않는다.

SCOPE
  읽기: ~/coastal-wiki/models/Delft3D (노트·raw 소스, 읽기 전용),
        ~/.cache/coastal-snapshots/delft3d-upstream, ~/coastal-wiki/_staging/delft3d-prescan/
  쓰기: ~/coastal-wiki/_staging/delft3d-prescan/ 하위만
  금지: models/ 수정, 위키 본문 수정, chmod/sudo, 41건 밖 조사

STOP CONDITION
  41건 판정이 끝나면 종료. 근거가 소스에서 확인되지 않으면 UNRESOLVED.

DELIVERABLE
  phase2-codex.csv — id, batch, note, note_line, wiki_claim, old_evidence, new_evidence,
    semantic_meaning_changed, proposed_classification, reason_type, confidence, exact_evidence
  phase2-codex.md  — 배치별 요약, UNRESOLVED 목록, 재앵커 근거
```

## 입력

`phase2-candidates.csv` 41행. 노트 원문·신구 좌표·교차 hunk 원문 포함.
`REANCHOR(a-b)` 19건, broad 인용(span>60) 15건.

| 배치 | 대상 | 건수 |
|---|---|---|
| B | dflowfm 계열 — waves 10 · compute_core 5 · transport_sediment 3 · kernel_scheme 1 | 19 |
| C | 퇴적·준설 — sediment 9 · dredge_dump 5 | 14 |
| D | wave/waq/flow2d3d — wave_swan_module 3 · waq_kernel_integration 2 · flow2d3d_io 1 | 6 |
| Z | heat 1 · sediment_transport_formulae 1 | 2 |

## Phase 1 에서 확인된 변경의 성격 (참고)

커밋 `0da71c3` "flowgeom object v2" 가 **데이터·타입을 별도 모듈로 분리**했다.
`unstruc_netcdf.f90` → `unstruc_netcdf_data.f90`, `unstruc_model.f90` → `m_unstruc_model_data.f90`,
`m_transport.f90` → `fm_external_forcings_data.f90`.

**선언이 다른 모듈로 이동한 것만으로는 UPDATE_REQUIRED 가 아니다** — 주장이 그대로면
REVIEW_ONLY 다(인용 재지정). Phase 1 에서 이 구분으로 UPDATE_REQUIRED 가 2건으로 좁혀졌다.

또 하나: Fortran **선언 문법이 바뀌었다**.
`real(kind=dp), allocatable, target :: s1max(:)` → `..., dimension(:) :: s1max`.
심볼은 그대로다. 이것도 REVIEW_ONLY 다.

## 판정 기준

UPDATE_REQUIRED / REVIEW_ONLY / NO_ACTION. UPDATE_REQUIRED 에는 `reason_type` 필수.

**값·인터페이스·조건이 실제로 바뀐 것만 UPDATE_REQUIRED 다.** Phase 1 의 실제 사례:
- `unc_create` 에 `overwrite_cmode` 선택 인자가 생겨 전역 cmode 합성이 조건부가 됨 (BEHAVIOR_CHANGE)
- `ExtfileNewMajorVersion` 2.02 → 3.00 (INTERFACE_CHANGE)

**노트가 파일 줄 수·개수 같은 수치를 적었으면 그것도 확인하라.** Phase 1 에서
"unstruc_netcdf 18,974줄" 이 16,909 로 바뀐 것을 놓칠 뻔했다.

**주석 함정**: 교체된 코드가 주석으로 남으면 옛 텍스트의 사본은 주석 쪽이다.
주석에 정박하지 마라. 전부 주석이면 주변에서 같은 signature 의 실행 줄을 찾고 없으면 UNRESOLVED.

## 반환하지 말 것

위키 문장 수정안, 좌표 일괄 치환, 41건 밖 후보 추가.
