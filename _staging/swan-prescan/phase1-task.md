# CODEX TASK — SWAN Phase 1 의미 검토 (16건)

```
OBJECTIVE
  SWAN pinned 5544152 → upstream 43e9bbb 변경이 위키 주장의 의미를 바꾸는지
  후보 16건에 대해 판정하고 근거를 반환한다. 위키는 수정하지 않는다.

SCOPE
  읽기: ~/coastal-wiki/models/SWAN (노트, raw 소스는 읽기 전용),
        ~/.cache/coastal-snapshots/swan-43e9bbb (새 스냅샷 git repo),
        ~/coastal-wiki/_staging/swan-prescan/
  쓰기: ~/coastal-wiki/_staging/swan-prescan/ 하위만
  금지: models/ 수정, 위키 본문 수정, chmod/sudo, 범위 밖 파일 조사

STOP CONDITION
  16건 판정과 §추가 조사 1건이 끝나면 종료. 판정 근거가 소스에서 확인되지
  않으면 UNRESOLVED 로 표시하고 추측하지 않는다. 범위를 넓히지 않는다.

DELIVERABLE
  phase1-codex.csv — id, note, note_line, wiki_claim, old_evidence, new_evidence,
    semantic_meaning_changed(yes/no), proposed_classification, reason_type,
    confidence, exact_evidence(file:line + 인용문)
  phase1-codex.md  — 요약, 추가 조사 답, UNRESOLVED 목록
```

## 입력

`phase1-candidates.csv` 16행. 각 행에 이미 들어 있는 것:
- `wiki_claim` — 노트의 해당 줄 원문
- `old_ranges` / `new_ranges` — pinned 좌표와 기계 매핑 결과.
  `REANCHOR(a-b)` 는 **끝점이 변경 블록 안이라 기계 매핑 실패**. 새 좌표는 직접 찾아라.
- `hunks` — 교차하는 변경 hunk 의 신구 원문(최대 4개, 각 6줄)

전체 diff 는 `git -C ~/.cache/coastal-snapshots/swan-43e9bbb diff 5544152 HEAD -- <path>` 로 본다.

## 판정 기준

| 분류 | 조건 |
|---|---|
| UPDATE_REQUIRED | 노트 주장과 새 소스가 불일치. 반드시 `reason_type` 을 하나 이상 붙인다: `SEMANTIC_CHANGE` / `BEHAVIOR_CHANGE` / `INTERFACE_CHANGE` / `SYMBOL_RENAME_ONLY` / `BUGFIX_AFFECTING_DOC` |
| REVIEW_ONLY | 변경 구간과 겹치지만 주장 자체는 유지. 좌표만 갱신하면 됨 |
| NO_ACTION | 주장·좌표 모두 영향 없음 |

**hunk 겹침은 충분조건이 아니다.** 겹쳐도 주장이 그대로면 REVIEW_ONLY 다.
반대로 겹치지 않아도 인터페이스·기본값·호출 관계 서술이 어긋나면 UPDATE_REQUIRED 다.
**broad 인용(span > 60)** 은 그 범위가 뒷받침하던 주장이 무엇인지 보고 판정한다.
범위 안에서 코드가 바뀌었다는 사실만으로 UPDATE_REQUIRED 로 올리지 마라.

## 변경의 성격 (참고)

커밋 10개: "extended to Windows" ×3, "updated src (patch B)", "small bug fix", 나머지는 merge.

| 파일 | 변경 규모 |
|---|---|
| `src/SwanCompUnstruc.ftn90` | 880줄 (파일의 상당 부분) |
| `src/SwanVertlist.ftn90` | +277 |
| `src/SwanThreadBounds.ftn90` | **삭제 (160줄)** |
| `src/SwanConvAccur.ftn90` 51 · `SwanConvStopc.ftn90` 31 · `SwanCompdata.ftn90` 13 | 소규모 |
| `src/swanmain.ftn` 7 · `src/swancom1.ftn` 2 | 극소 |
| `src/srclist.cmake`, `src/srclistnc.cmake` | 각 −1 (삭제 파일 등록 해제) |

## 추가 조사 1건 (필수)

**삭제된 `SwanThreadBounds.ftn90` 의 로직이 어디로 갔는가.**
`subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )` — OpenMP thread 경계 계산으로 보인다.
`SwanVertlist.ftn90`(+277) 또는 `SwanCompUnstruc.ftn90` 으로 흡수됐는지 확인하고,
흡수됐다면 **호출 관계와 인자 의미가 보존됐는지** 답하라. 이동만인지 동작 변경인지 구분해야 한다.
이것이 S1-14·S1-15(`SwanVertlist.ftn90:45-181`)와 S1-16(`SwanCompUnstruc.ftn90:829-987`)의 판정에 직결된다.

호출자 확인: `grep -rn "SwanThreadBounds" src/` 를 신구 양쪽에서.

## 반환하지 말아야 할 것

- 위키 문장 수정안 (Claude 가 결정한다)
- 좌표 일괄 치환 (Phase 2 범위)
- 16건 밖 후보 추가 (발견하면 `phase1-codex.md` 에 별도 항목으로 보고만)
