# CODEX TASK — ROMS Phase 1 의미 검토 (8건 + 추가 조사 2)

```
OBJECTIVE
  ROMS pinned 32c79b7 → upstream 57aecf5 변경이 위키 주장의 의미를 바꾸는지
  후보 8건을 판정하고, 추가 조사 2건에 답한다. 위키는 수정하지 않는다.

SCOPE
  읽기: ~/coastal-wiki/models/ROMS (노트·raw 소스, 읽기 전용),
        ~/.cache/coastal-snapshots/roms-upstream (새 스냅샷 git repo),
        ~/coastal-wiki/_staging/roms-prescan/
  쓰기: ~/coastal-wiki/_staging/roms-prescan/ 하위만
  금지: models/ 수정, 위키 본문 수정, chmod/sudo, 범위 밖 조사

STOP CONDITION
  8건 판정 + 추가 조사 2건이 끝나면 종료. 근거가 소스에서 확인되지 않으면
  UNRESOLVED 로 표시하고 추측하지 않는다.

DELIVERABLE
  phase1-codex.csv — id, note, note_line, wiki_claim, old_evidence, new_evidence,
    semantic_meaning_changed, proposed_classification, reason_type, confidence, exact_evidence
  phase1-codex.md  — 요약, 추가 조사 답, UNRESOLVED 목록
```

## 입력

`phase1-candidates.csv` 8행. 각 행에 노트 원문·신구 좌표·교차 hunk 원문이 있다.
전체 diff: `git -C ~/.cache/coastal-snapshots/roms-upstream diff 32c79b7 57aecf5 -- <path>`

## 변경의 성격

6커밋 / 193파일(신규 35 / 수정 158).

| 커밋 | 내용 |
|---|---|
| f03bcbb (#75) | **multi-scale background error covariance** — 4D-Var. 신규 `convolve_mono/multi.h`, `ad_/tl_convolution_*.h` |
| acfb066 (#77) | bottom albedo reflectance |
| ba5d070 (#78) | MstateVar 선언 정리 |
| b3385fd (#79) | INTEL OneAPI 호환 |
| f65a834 (#80) | 선언부 pointer 초기화 |
| 57aecf5 (#81) | 메모리 사용량 보고 |

## 판정 기준

UPDATE_REQUIRED / REVIEW_ONLY / NO_ACTION. UPDATE_REQUIRED 에는 `reason_type` 필수
(`SEMANTIC_CHANGE` / `BEHAVIOR_CHANGE` / `INTERFACE_CHANGE` / `SYMBOL_RENAME_ONLY` / `BUGFIX_AFFECTING_DOC`).

**hunk 겹침은 충분조건이 아니다.** 겹쳐도 주장이 유지되면 REVIEW_ONLY.
후보 다수가 **broad 인용**(`126-1180`, `369-5081` 등 파일 전체에 가까움)이다.
그 범위가 뒷받침하던 주장이 무엇인지 보고 판정하라. 범위 안에서 코드가 바뀌었다는
사실만으로 UPDATE_REQUIRED 로 올리지 마라.

**R1-1 주의**: `ana_initial.h` 는 `ROMS/Functionals/` 와 `User/Functionals/` 양쪽에 있고
**내용이 다르다**(1121 vs 256줄). resolver 가 AMBIGUOUS_SAME_MODEL 로 남겼다.
노트가 어느 쪽을 가리키는지 증거로 판단하고, 단정할 수 없으면 UNRESOLVED 로 반환하라.
임의로 한쪽을 고르지 마라.

## 추가 조사 (필수)

**A. NEW FILE RULE.** 신규 35개 중 `ROMS/Utility/convolve_mono.h`·`convolve_multi.h`,
`get_state_{adm,frc,generic,nlm}_{nf90,pio}.h`, `ROMS/Adjoint/ad_convolution_*.h`,
`ROMS/Tangent/tl_convolution_*.h` 가 있다.
기존 파일(`convolve.F`, `get_state.F` 등)에서 **로직이 분리·이동**된 것인지,
그 기존 파일이 위키에 인용돼 있는지 확인하라. 이동이면 어느 파일의 어느 구간인지 적어라.

**B. 4D-Var 노트 영향.** `models/ROMS/source-analysis/roms_4dvar.md` 는
`i4dvar.F`·`rbl4dvar.F`·`r4dvar.F`·`ad_congrad.F` 등을 인용한다. 이들은 #75 로 바뀌었다.
이 노트의 주장(알고리즘 흐름·비용함수·최소화 경로)이 여전히 맞는지 확인하라.
교집합 후보에 안 잡힌 인용도 있으니 노트 전체를 읽고 판단하라.

## 반환하지 말 것

위키 문장 수정안, 좌표 일괄 치환, 8건 밖 임의 후보 추가(발견 시 md 에 별도 보고만).
