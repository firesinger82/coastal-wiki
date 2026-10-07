---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Parent_Grid.f90
lines: 70
sha256: 13cef7c498101f8c99fc8b40c827ed291382dfbf480a30afa944ad443d2f13ae
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Parent_Grid.f90 — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+·저작권·GPLv2 머리말과 전역 인덱스를 지역 인덱스로 매핑하는 목적·작성자·날짜 주석(1–16). `Parent_Grid`를 시작하고 GLOBAL·variables_mpi·Mod_Write_Cell_Map의 Write_Xloc_Yloc를 사용한다(18–24). 지역 정수 ii·jj·i·j·ierr를 선언한다(29). 주석·빈 줄을 포함한다. |
| 31–43 | 시작 시 18행 Parent_Grid 안. ic_pos·jc_pos를 0으로 설정한다(31–32). 주석은 ic_decomp·jc_decomp가 고스트 셀(ghost cell)을 제외한다고 적는다(34). `Do ii = 2, x_id` (35)에서 `ic_pos = ic_pos + ic_decomp(ii-1)` (36). `Do jj = 2, y_id` (40)에서 `jc_pos = jc_pos + jc_decomp(jj-1)` (41). 두 루프 종료와 빈 줄(37–43). |
| 44–57 | 시작 시 18행 Parent_Grid 안. ii=0(45). `Do i = IB_Decomp(process_id),IE_Decomp(process_id)` (46)에서 `ii = ii + 1` (47) 후 IG2IL(i)에 ii를 복사한다(48). jj=0(52). `Do j = JB_Decomp(process_id),JE_Decomp(process_id)` (53)에서 `jj = jj + 1` (54) 후 JG2JL(j)에 jj를 복사한다(55). 지역 인덱스는 1부터 증가한다. 루프 종료와 빈 줄(49–57). |
| 58–70 | 시작 시 18행 Parent_Grid 안. `if( MPI_Write_Flag )then` (58)일 때 `WriteBreak(mpi_log_unit)`·`Write_Xloc_Yloc`를 호출한다(59–60). x_id·y_id·ic_pos·jc_pos·ic·jc를 로그에 쓰고 다시 WriteBreak를 호출한다(61–67). 조건 종료·빈 줄·루틴 종료(68–70). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29: ierr는 선언 이후 사용되지 않는다.
- 31–55·63–64: ic_pos·jc_pos의 누적 결과는 이 파일에서 로그 출력에만 사용된다. IG2IL·JG2JL의 매핑은 IB_Decomp·IE_Decomp·JB_Decomp·JE_Decomp 범위를 직접 사용한다.
