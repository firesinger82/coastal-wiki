---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Child_Grid.f90
lines: 78
sha256: f446c7d6f93a4d8bdaaba9056e7fab44ba5c25e42084b2617b6551cc096c3ae9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Child_Grid.f90 — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | EFDC+·저작권·GPLv2 머리말과 하위 영역(subdomain) 셀 매핑 목적·작성자·날짜 주석(1–15). 빈 줄 뒤 `Child_Grid`를 시작하고 GLOBAL·Variables_MPI·MPI를 사용한다(17–24). i·ii·j·jj·ierr와 고스트 셀(ghost cell)의 시작·끝·개수용 정수 여섯 개를 선언한다(29–36). 분할별 고스트 셀 배열 할당에 관한 주석과 3×3 프로세서 배치 그림 주석이 있다(38–44). 이 구간에 실행 할당문은 없다. |
| 46–59 | 시작 시 17행 Child_Grid 안. ii를 0으로 설정한다(47). `Do i = IB_Decomp(process_id),IE_Decomp(process_id)` (48)에서 `ii = ii + 1` (49) 후 IL2IG(ii)에 전역 i를 복사한다(50). jj를 0으로 설정한다(54). `Do j = JB_Decomp(process_id),JE_Decomp(process_id)` (55)에서 `jj = jj + 1` (56) 후 JL2JG(jj)에 전역 j를 복사한다(57). 두 지역 인덱스는 1부터 증가한다. 루프 종료와 빈 줄(51–59). |
| 60–78 | 시작 시 17행 Child_Grid 안. 디버그 로그 주석(60–61). `if( MPI_Write_Flag )then` (63) 안에서 IL2IG를 i=1..IC, JL2JG를 j=1..jc 범위로 출력한다(65–74). 같은 조건 안에서 `MPI_Barrier(DSIcomm, ierr)`를 호출한다(75). 조건 종료·빈 줄·루틴 종료(76–78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–36: ghost_cells_i_start·ghost_cells_j_start·ghost_cells_i_end·ghost_cells_j_end·total_ghost_i·total_ghost_j는 선언 이후 사용되지 않는다.
- 38–59: 주석은 고스트 셀 개수 배열의 할당을 언급한다. 실제 실행문은 IL2IG·JL2JG 매핑을 채우며 이 파일에는 allocate 문장이 없다.
- 63–76: MPI_Barrier 호출은 MPI_Write_Flag 참 분기 안에 있다.
