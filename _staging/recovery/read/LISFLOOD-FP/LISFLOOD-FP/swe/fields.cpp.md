---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/fields.cpp
lines: 43
sha256: 92b966fc7e8c9017ce16711027aff2e1424ee3e723653ed2986b59cd864920b8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# fields.cpp — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 헤더 포함(1–2) 뒤 `allocate_swe_fields`(4–24)가 천수방정식(shallow water equations)용 유량·플럭스·수정 지형·수정 수심 배열을 0으로 할당한다. HU·HV와 수정 수심 네 개는 셀 수 크기다. 플럭스 여섯 개와 Zstar 두 개는 각 방향 한 칸을 더한 크기다. 조건부 전처리 분기와 실행 조건문은 없다. 원문: `Arrptr->HU = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);` (10); `Arrptr->HV = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);` (11); `Arrptr->FHx = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (12); `Arrptr->FHUx = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (13); `Arrptr->FHVx = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (14); `Arrptr->FHy = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (15); `Arrptr->FHUy = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (16); `Arrptr->FHVy = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (17); `Arrptr->Zstar_x = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (18); `Arrptr->Zstar_y = memory_allocate_zero_numeric_legacy((Parptr->xsz + 1)*(Parptr->ysz + 1));` (19); `Arrptr->Hstar_neg_x = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);` (20); `Arrptr->Hstar_pos_x = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);` (21); `Arrptr->Hstar_neg_y = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);` (22); `Arrptr->Hstar_pos_y = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);` (23). |
| 26–43 | `deallocate_swe_fields`는 대응하는 배열 열네 개를 `memory_free_legacy`에 주소로 넘겨 해제한다(28–41). 마지막 빈 줄도 이 구간에 포함한다. 별도 조건 검사는 이 함수에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
