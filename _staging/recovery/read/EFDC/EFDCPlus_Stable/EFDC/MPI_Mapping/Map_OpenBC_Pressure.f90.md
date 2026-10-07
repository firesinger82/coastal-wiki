---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Map_OpenBC_Pressure.f90
lines: 165
sha256: bb6d4beb4a326811e8a4310c39c65e99bff3a97de7f3831abfdd0a8bbe824acb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Map_OpenBC_Pressure.f90 — 판독 구간 기록

구간은 1행부터 165행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | EFDC+ 출처·2021–2024 저작권·GPLv2 머리말(1–8). 직렬(serial) 경계 셀 위치를 자식 분할 영역(partition)에 매핑한다는 설명과 저자·날짜 주석(9–16). `Map_OpenBC_Pressure` 시작(18). GLOBAL·MPI 변수·매핑 모듈 사용(20–22). implicit none과 ii·I·J·LL·M 선언(24–27). 빈 줄 포함. |
| 29–47 | 시작 시 18행 Map_OpenBC_Pressure 루틴 안. 네 방향 경계 수를 NPBW_GL·NPBE_GL·NPBN_GL·NPBS_GL에 보존한다(29–33). `WriteBreak(mpi_log_unit)` 호출과 수면고(surface elevation) 또는 압력(pressure) 경계의 전역 수 로그(35–40). 네 방향 지역 경계 수를 모두 0으로 초기화한다(42–46). |
| 48–74 | 시작 시 18행 Map_OpenBC_Pressure 루틴 안. ii=0(48). `do LL = 1,NPBW_GL` (49)에서 IG2IL·JG2JL로 서쪽 지역 좌표를 얻는다(50–51). `if( I > 0 .and. I <= IC )then` (53), `if( J > 0 .and. J <= JC )then` (54), `if( IJCT(I,J)  >  0  .and. IJCT(I,J).LT.9 )then` (55). 세 조건 안에서 `II = II + 1` (56), 지역 좌표 복사(57–58). `do M = 1,MTIDE` (59)에서 PCBW·PSBW를 복사한다(60–61). ISPRW·NPSERW·ISPBW 복사(63–65). `if( NPFORT >= 1 ) NPSERW1(II) = NPSERW1_GL(LL)` (66). TPCOORDW 복사(67), `NPBW = NPBW + 1` (69). 조건·루프 종료(70–73). |
| 75–102 | 시작 시 18행 Map_OpenBC_Pressure 루틴 안. II=0(75). `do LL = 1,NPBS_GL` (76), 남쪽 좌표 조회(77–78). `if( I > 0 .and. I <= IC )then` (80), `if( J > 0 .and. J <= JC )then` (81), `if( IJCT(I,J) >  0 .and. IJCT(I,J) .LT. 9 )then` (82). 참이면 `II = II + 1` (83), 지역 좌표 복사(84–85). `do M  = 1,MTIDE` (86)에서 PCBS·PSBS 복사(87–88). ISPRS·NPSERS·ISPBS 복사(90–92). `if( NPFORT >= 1 ) NPSERS1(II) = NPSERS1_GL(LL)` (93). TPCOORDS 복사(94), `NPBS = NPBS  + 1` (96). 조건·루프 종료와 빈 줄(97–102). |
| 103–129 | 시작 시 18행 Map_OpenBC_Pressure 루틴 안. II=0(103). `do LL = 1,NPBE_GL` (104), 동쪽 좌표 조회(105–106). `if( I > 0 .and. I <= IC )then` (108), `if( J > 0 .and. J <= JC )then` (109), `if( IJCT(I,J)  >  0 .and. IJCT(I,J).LT.9 )then` (110). 참이면 `II = II + 1` (111), 지역 좌표 복사(112–113). `do M = 1, MTIDE` (114)에서 PCBE·PSBE 복사(115–116). ISPRE·NPSERE·ISPBE 복사(118–120). `if( NPFORT >= 1 ) NPSERE1(II) = NPSERE1_GL(LL)` (121). TPCOORDE 복사(122), `NPBE = NPBE  + 1` (124). 조건·루프 종료(125–128). |
| 130–155 | 시작 시 18행 Map_OpenBC_Pressure 루틴 안. II=0(130). `do LL = 1,NPBN_GL` (131), 북쪽 좌표 조회(132–133). `if( I > 0 .and. I <= IC )then` (134), `if( J > 0 .and. J <= JC )then` (135), `if( IJCT(I,J)  >  0  .and. IJCT(I,J).LT.9 )then` (136). 참이면 `II = II + 1` (137), 지역 좌표 복사(138–139). `do M = 1,MTIDE` (140)에서 PCBN·PSBN 복사(141–142). ISPRN·NPSERN·ISPBN 복사(144–146). `if( NPFORT >= 1 ) NPSERN1(II) = NPSERN1_GL(LL)` (147). TPCOORDN 복사(148), `NPBN = NPBN  + 1` (150). 조건·루프 종료(151–154). |
| 156–165 | 시작 시 18행 Map_OpenBC_Pressure 루틴 안. 네 방향 지역 경계 수 로그(156–160). `WriteBreak(mpi_log_unit)` 호출(161). return·루틴 종료와 빈 줄(163–165). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55·82·110·136: 네 방향 모두 IJCT 값이 0보다 크고 9보다 작을 때만 경계를 채택한다. 비교 상수 0·9는 조건식에 직접 적혀 있다.
- 66·93·121·147: NPSERW1·NPSERS1·NPSERE1·NPSERN1의 복사는 NPFORT>=1일 때만 실행한다. 이 루틴에는 해당 배열을 초기화하거나 이 조건이 거짓일 때 대입하는 문장이 없다.
