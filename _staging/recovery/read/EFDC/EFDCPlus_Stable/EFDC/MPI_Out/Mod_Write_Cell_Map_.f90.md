---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Out/Mod_Write_Cell_Map_.f90
lines: 185
sha256: 44f4f24b046586c4107ca8250a8e7e9adf8d53b3d78d3f51d12331a910c2b3e7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Write_Cell_Map_.f90 — 판독 구간 기록

구간은 1행부터 185행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+ 표제·저작권·GPLv2 안내(1–8). 계산 중 MPI용 배열을 출력한다는 설명·날짜·저자(9–12). Mod_Write_Cell_Map 모듈은 Variables_MPI·GLOBAL을 사용한다(14–17). implicit none, 모듈 내부 private 정수 I/J/L, contains 및 빈 줄(19–25). |
| 26–58 | Write_LIJ 입구와 logical intent(in) write_out 선언(26–34). `if( write_out )then` (36) 안에서 WriteBreak(mpi_log_unit)를 호출한다(38). IJCT Global 표제와 열 눈금을 출력한다(40–48). i 눈금은 10..ic_global 간격 10이다(45). j=jc_global..1 간격 -1, i=1..ic_global 루프에서 IJCT_Global(i,j)를 i1 형식으로 출력한다(49–55). 공백과 WriteBreak 호출(56–57). |
| 59–89 | 시작 시 27행 Write_LIJ·36행 write_out 참 분기 안. IJCT Local 표제와 열 눈금을 출력한다(60–67). 눈금은 i=10..ic 간격 10(64). j=jc..1 간격 -1, i=1..ic 루프에서 IJCT(i,j)를 i1 형식으로 출력한다(68–74). 이어서 IL2IG(1)·IL2IG(IC), LA_Global·LA·LC·IC·JC를 mpi_log_unit에 출력한다(78–87). WriteBreak 호출·빈 줄(88–89). |
| 90–125 | 시작 시 27행 Write_LIJ·36행 write_out 참 분기 안. Global L indexing 표제와 i=5..ic_global 간격 5 눈금을 출력한다(90–96). j=JC_Global..1 간격 -1, i=1..ic_global 루프는 lij_global을 I6 형식으로 출력한다(97–103). WriteBreak 호출과 Local L indexing 표제·i=5..ic 간격 5 눈금(105–112). j=jc..1 간격 -1, i=1..ic 루프는 lij를 I6 형식으로 출력한다(113–119). WriteBreak·조건 종료·루틴 종료·빈 줄(120–125). |
| 126–144 | Write_Cell_Indexing 설명·입구·logical write_out 인수(126–133). `if( write_out )then` (135)이면 I/J/L/LWC/LEC/LSC/LNC 머리글을 7A6 형식으로 출력한다(138). 2..LA 루프는 IL(L)·JL(L)·L 및 서·동·남·북 이웃 인덱스(neighbor index)를 7I6 형식으로 mpi_log_unit에 출력한다(139–141). 조건·루틴 종료(142–144). |
| 145–185 | Write_Xloc_Yloc 설명·입구·implicit none(145–150). `if( MPI_Write_Flag )then` (152)이면 WriteBreak 호출(154), i=1..ic_global 루프에서 I와 IG2IL(I)를 2I5 형식으로 출력한다(156–160). j=1..jc_global 루프에서 J와 JG2JL(J)를 2I5 형식으로 출력한다(164–167). WriteBreak 호출(169). 2차원 행렬 출력 루프 전체는 주석이다(171–179). 조건·루틴·모듈 종료와 빈 줄(181–185). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–42: 실행문 앞 주석은 “XLOC-YLOC - local to a process”라고 적는다. 실제 출력 표제는 “IJCT Global”이다.
- 52·71: IJCT_Global과 IJCT 출력은 각각 i1 형식을 사용한다. 값 범위를 검사하는 조건은 두 출력 루프 안에 없다.
- 146–179: 루틴 설명은 xloc/yloc를 적는다. 실행문은 IG2IL·JG2JL 배열을 출력한다. 2차원 출력 루프는 주석 처리되어 있다.

