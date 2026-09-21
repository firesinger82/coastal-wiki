# CODEX TASK — Delft3D Phase 1 의미 검토 (45건)

```
OBJECTIVE
  Delft3D pinned 513eccd → upstream 231bbf2 변경이 위키 주장의 의미를 바꾸는지
  후보 45건(delft3d_dflowfm_data_io.md 단일 노트)을 판정한다. 위키는 수정하지 않는다.

SCOPE
  읽기: ~/coastal-wiki/models/Delft3D (노트·raw 소스, 읽기 전용),
        ~/.cache/coastal-snapshots/delft3d-upstream (새 스냅샷 git repo),
        ~/coastal-wiki/_staging/delft3d-prescan/
  쓰기: ~/coastal-wiki/_staging/delft3d-prescan/ 하위만
  금지: models/ 수정, 위키 본문 수정, chmod/sudo, 45건 밖 조사

STOP CONDITION
  45건 판정이 끝나면 종료. 근거가 소스에서 확인되지 않으면 UNRESOLVED.

DELIVERABLE
  phase1-codex.csv — id, note, note_line, wiki_claim, old_evidence, new_evidence,
    semantic_meaning_changed, proposed_classification, reason_type, confidence, exact_evidence
  phase1-codex.md  — 요약, UNRESOLVED 목록, 재앵커 근거
```

## 입력

`phase1-candidates.csv` 45행. 노트 원문·신구 좌표·교차 hunk 원문 포함.
**`REANCHOR(a-b)` 가 39건**으로 많다 — 변경이 커서 기계 매핑이 실패했다. 새 좌표를 직접 찾아라.

대상 파일: `m_flow.f90`(17) · `unstruc_netcdf.f90`(15) · `unstruc_model.f90`(6) ·
`m_transport.f90`(5) · `m_flowgeom.f90`(1) · `unc_write_his.F90`(1).
전부 `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/` 아래다.

## 변경의 성격

1,771커밋 / 27,933파일(삭제 19,432 · 신규 7,394 · 수정 1,077 · rename 17).
저장소가 30,755 → 18,717 파일로 **재구조화**됐다. 다만 삭제분은 위키 인용과
겹치지 않으며, 교집합은 137파일 / +12,690 −10,082줄이다.

## 판정 기준

UPDATE_REQUIRED / REVIEW_ONLY / NO_ACTION. UPDATE_REQUIRED 에는 `reason_type` 필수
(`SEMANTIC_CHANGE` / `BEHAVIOR_CHANGE` / `INTERFACE_CHANGE` / `SYMBOL_RENAME_ONLY` / `BUGFIX_AFFECTING_DOC`).

**hunk 겹침은 충분조건이 아니다.** 변경 규모가 커서 대부분 겹친다.
그 범위가 뒷받침하던 주장이 여전히 성립하는지로 판정하라.

**주석 함정 주의**: 교체된 코드가 주석으로 남아 있으면 옛 텍스트의 정확한 사본은
주석 쪽이고 실행 줄은 인자·식이 바뀌어 있다. **주석에 정박하지 마라.**
일치가 전부 주석이면 주변에서 같은 signature 의 실행 줄을 찾고, 없으면 UNRESOLVED.

## 반환하지 말 것

위키 문장 수정안, 좌표 일괄 치환, 45건 밖 후보 추가.
