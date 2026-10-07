---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Scan_Cell.f90
lines: 218
sha256: e661a1d02716bd6af0d2d85b0a7bda5fc12bd2a4ff2a6953a888aa04ac6b357b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Scan_Cell.f90 — 판독 구간 기록

구간은 1행부터 218행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | EFDC+·저작권·GPLv2 머리말과 cell.inp 판독·IJCT 설정·LCM 확장에 관한 목적·작성자·날짜 주석(1–17). `Scan_Cell`을 시작한다(18). GLOBAL·INFOMOD·Variables_MPI·Broadcast_Routines·MPI를 사용하고 implicit none을 선언한다(20–27). L·ierr, 지역 분할 시작·끝 배열 IB/IE/JB/JE, 2차원 IJCT_Read_In, 판독·범위용 정수와 길이 650 STRC를 선언한다(32–43). 빈 줄·구분 주석(44–46). |
| 47–67 | 시작 시 18행 Scan_Cell 안. IB·IE는 n_x_partitions, JB·JE는 n_y_partitions 크기로 할당한다(47–50). IB_Decomp·IE_Decomp·JB_Decomp·JE_Decomp는 `0:active_domains` 범위로 할당한다(51–54). IJCT_Read_In은 IC·JC 크기이다(56). MPI_Write_Flag에 DEBUG를 복사한다(58). 네 전역 분할 범위 배열과 IJCT_Read_In을 0으로 초기화한다(61–65). 파일 판독 주석·빈 줄(66–67). |
| 68–90 | 시작 시 18행 Scan_Cell 안. `if( process_id == master_id )then` (68)에서 cell.inp를 장치 1·STATUS='UNKNOWN'으로 열고 `READSTR(1)`을 호출한다(70–72). 문자열에서 JDUMY를 읽는다(73). `if( JDUMY /= JC )then` (75)은 구형 형식 경로이다. JACROSS=JC 복사(77), `if( JC > 640 ) JACROSS = 640` (78). `do JT = 1,JC,JACROSS` (79)에서 JF=JT, `JLAST = JT + JACROSS - 1` (81), `if( JLAST > JC ) JLAST = JC` (82). 범위를 출력하고 i=1..IC에서 FORMAT 6으로 셀 종류를 읽는다(83–85). `if( ISO > 0 ) CALL STOPP('READ ERROR FOR FILE CELL.INP')` (86). 같은 셀 자료를 FORMAT 66으로 출력한다(87). 루프 종료와 빈 줄(88–90). |
| 91–126 | 시작 시 18행 Scan_Cell·68행 master 참 분기·75행 형식 분기 안. `else` (91)는 신형 형식 경로이다. `if( IC > 640 )then` (94)은 IACROSS=640(95), `do IT = 1,IC,IACROSS` (96)에서 IFIRST=IT와 `ILAST = IT + IACROSS - 1` (98), `if( ILAST > IC ) ILAST = IC` (99). j를 JC부터 1까지 역순으로 돌며 FORMAT 66으로 JDUMY와 셀 종류를 읽는다(100–101). `if(ISO.GT.0 )then` (102)은 오류 출력과 STOP을 실행한다(103–104). 94행 조건의 `else !***IC < 640` (109)는 IFIRST=1·ILAST=IC 설정과 같은 역순 j 판독을 수행한다(111–114). 이 경로도 `if(ISO.GT.0 )then` (115)에서 오류 출력·STOP을 실행한다(116–117). 내부·형식 조건 종료(118–121). `66 FORMAT (I4,1X,640I1)` (122), close(1)과 master 조건 종료·빈 줄(124–126). |
| 127–147 | 시작 시 18행 Scan_Cell 안이며 master 판독 조건 밖. `MPI_BCAST`로 IJCT_Read_In의 size개 MPI_Integer를 master_id·DSIcomm에서 배포하고 MPI_BARRIER를 호출한다(128–129). IB(1)=1, IE(1)=ic_decomp(1)(131–132). NI=2..n_x_partitions에서 `IB(NI) = IE(NI-1) + 1` (134), `IE(NI) = IB(NI)   + ic_decomp(NI) - 1` (135). JB(1)=1, JE(1)=jc_decomp(1)(138–139). NJ=2..n_y_partitions에서 `JB(NJ) = JE(NJ-1) + 1` (141), `JE(NJ) = JB(NJ)   + jc_decomp(NJ) - 1` (142). 주석은 이 범위가 고스트 셀(ghost cell)을 제외한다고 적는다(134–142). 분할별 활성 셀 출력 제목·빈 줄(145–147). |
| 148–176 | 시작 시 18행 Scan_Cell 안. LCM·ii=0, IP=-1을 설정한다(148–150). NJ=1..n_y_partitions와 NI=1..n_x_partitions 루프에서 L=0, 네 범위 변수를 -1로 설정한다(152–158). `if( process_map(NI,NJ) /= -1 )then` (159)이면 `IP = IP + 1` (160). JBEG/JEND에 해당 j 분할 범위를 복사한다(163–164). `if( process_map(NI,NJ-1) /= -1 )  JBEG = JBEG - n_ghost_rows   ! *** South Edge` (165), `if( process_map(NI,NJ+1) /= -1 )  JEND = JEND + n_ghost_rows   ! *** North Edge` (166). JB_Decomp·JE_Decomp의 IP 위치에 복사한다(167–168). i 범위를 복사한 뒤 `if( process_map(NI-1,NJ) /= -1 )  IBEG = IBEG - n_ghost_rows   ! *** West Edge` (172), `if( process_map(NI+1,NJ) /= -1 )  IEND = IEND + n_ghost_rows   ! *** East Edge` (173). IB_Decomp·IE_Decomp의 IP 위치에 복사한다(174–175). |
| 177–194 | 시작 시 18행 Scan_Cell·152행 NJ 루프·153행 NI 루프·159행 활성 분할 참 분기 안. L=1(177) 후 j=JBEG..JEND·i=IBEG..IEND를 순회한다(178–179). `if( IJCT_Read_In(i,j) > 0 .and. IJCT_Read_In(i,j) < 9 )then` (180)이면 `L = L + 1` (181). 셀 루프와 활성 분할 조건 종료(182–185). 각 분할의 범위와 L을 출력한다(187). `LCM = max(LCM,L)` (189)로 최댓값을 유지하고 두 분할 루프를 닫는다(190–191). 루프 밖에서 `LCM = LCM + 4` (193). 빈 줄을 포함한다. |
| 195–218 | 시작 시 18행 Scan_Cell 안이며 분할 루프 밖. `WriteBreak`와 전역 LCM·IC·JC 로그, 해당 process_id의 i/j 시작·끝 로그를 출력한다(195–207). 다시 WriteBreak를 호출한다(208). IJCT_Read_In·IB·IE·JB·JE를 해제한다(210–212). FORMAT 5·6·8 정의와 빈 줄·루틴 종료(214–218). FORMAT 6은 `6 FORMAT(A10,40I5)` (215)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–41·149·214: IS·II·jj·ICUR·JCUR는 실행 계산에 사용되지 않는다. II는 149행의 0 대입만 있다. FORMAT 5는 이 파일에서 참조되지 않는다.
- 78·94–109·193: 구형 형식의 j 폭 상한과 신형 형식의 i 분할 폭은 640이다. `IC > 640`의 else 주석은 IC<640으로 적지만 IC=640도 이 else에 들어간다. LCM에 더하는 값은 4로 고정되어 있다.
- 85–86·101–105·114–118: 세 판독 오류 조건은 모두 ISO가 양수인 경우만 검사한다. 이 블록에는 음수 ISO를 검사하는 분기가 없다.
- 85·215: 구형 형식 read의 입력 목록은 IJCT_Read_In 정수 배열 원소이다. 이 read가 사용하는 FORMAT 6의 첫 편집 기술자는 A10이다.
- 159–175: process_map은 활성 여부와 이웃 존재 여부의 조건에 사용된다. 분할 범위 배열의 인덱스 IP는 활성 분할 순회마다 증가하며 process_map의 번호를 직접 대입하지 않는다.
