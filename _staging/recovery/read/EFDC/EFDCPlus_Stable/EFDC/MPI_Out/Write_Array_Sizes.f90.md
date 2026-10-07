---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Out/Write_Array_Sizes.f90
lines: 154
sha256: a1055622cdc7fe17acbfe9f07368f2fe9a514aa587b7b842fc36e7340625617d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Write_Array_Sizes.f90 — 판독 구간 기록

구간은 1행부터 154행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | EFDC+ 표제·저작권·GPLv2 안내(1–8). Varalloc.f90에 있던 배열 크기 출력이라는 설명·저자·날짜(9–11). Write_Array_Sizes는 GLOBAL·Variables_WQ·Variables_MPI를 사용한다(13–20). 정수 파일 유닛(file unit), 길이 3 process_id_txt, 길이 200 STR 선언(22–23). `Array_Sizes_Unit = 888 + process_id` (25)로 유닛을 정한다. process_id를 I3.3 문자열로 만든다(26). `open(Array_Sizes_Unit, FILE = OUTDIR//'log_arraysize_proc_'//process_id_txt//'.log',STATUS = 'UNKNOWN')` (27)로 프로세스(process)별 로그를 연다. 실행 파일명·버전·별표 줄·RUNTITLE을 출력한다(29–34). |
| 36–65 | 시작 시 13행 Write_Array_Sizes 안. 격자(grid)의 ICM/JCM/KCM/LCM을 출력한다(36–41). 유량 경계(flow boundary)의 NQSIJ/NQSERM(43–48), 제트·플룸(jet/plume) NQJPIJ(50–52), 수리 구조물(hydraulic structure)의 NHYDST/NQCTTM/NDQCLT(54–58), 취수·회귀(withdrawal/return)의 NQWRM/NQWRSRM/NDQWRSR(60–64)를 A,I10 형식으로 출력한다. 구분용 빈 write와 빈 줄을 포함한다. |
| 66–93 | 시작 시 13행 Write_Array_Sizes 안. 개방 경계(open boundary)의 동·북·남·서 수위/압력 셀 NPBE/NPBN/NPBS/NPBW와 농도 셀 NCBE/NCBN/NCBS/NCBW를 출력한다(66–75). NPSER/NDPSER/MTM은 수위 시계열(time series)·자료점·조석 성분(tidal constituents) 수이다(76–78). 대기·바람·열(atmospheric/wind/heat) 구역은 NASER/NWSER/NISER를 출력한다(80–84). 지하수(groundwater) NGWSERM/NDGWSER(86–89)와 전체 농도 시계열 NCSERM(91–92)을 출력한다. 구분용 write·빈 줄 포함. |
| 94–119 | 시작 시 13행 Write_Array_Sizes 안. 염료(dye) 분류 NDYM 출력(94–96). 퇴적물(sediment) 구역은 KB/NSCM/NSNM/NSTM/NSICM 및 제방·하상 침식(bank/bed erosion) NBEPAIRM/NBESERM/NDBESER를 출력한다(98–107). 독성물질(toxic) NTXM/NPMXPTSM 출력(109–112). 수질(water quality) NWQV/NSTVM 출력(114–118). 각 숫자는 A,I10 형식이며 구분용 write와 빈 줄을 포함한다. |
| 120–154 | 시작 시 13행 Write_Array_Sizes 안. 식생(vegetation) NVEGTPM/NVEGSERM(120–124), 장치(MHK devices) TCOUNT/MHKTYP(126–130)를 출력한다. Output 구역의 NSMTS/MLTMSRM 출력문은 주석이다(132–134). MPI 구역은 NMAXBC/NBBEM/NBBNM/NBBSM/NBBWM/NCHANM을 출력한다(136–143). Misc 구역의 NTSSTSP/MTSSTSP 출력문도 주석이다(145–149). 부분 차단 셀(partially blocked cells) NBLOCKED 출력(150), 로그 close와 루틴 종료(152–154). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·25–27: 프로세스 번호 문자열 길이와 출력 형식은 3 및 I3.3으로 고정되어 있다. 파일 유닛은 888+process_id이다. 이 루틴에는 번호 범위 검사와 open의 iostat 처리가 없다.
- 132–134·147–149: 시간별 출력 위치 수 및 start-stop 시나리오 크기 출력문은 주석 처리되어 있다.

