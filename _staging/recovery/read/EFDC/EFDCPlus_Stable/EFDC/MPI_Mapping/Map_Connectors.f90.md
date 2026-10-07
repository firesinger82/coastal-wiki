---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Map_Connectors.f90
lines: 248
sha256: 7caa339b84d6086b01d41e6ebbdfb5ecb309b25800afd01ec625333b3eda1ecb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Map_Connectors.f90 — 판독 구간 기록

구간은 1행부터 248행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | EFDC+·저작권·GPLv2 머리말과 동서·남북 연결(connector)의 지역 매핑 목적·동일 하위 영역 조건·날짜 주석(1–16). `Map_Connectors`를 시작한다(18). GLOBAL·MPI 변수·매핑·출력 변수·Broadcast_Routines·INFOMOD의 SKIPCOM/READSTR를 사용한다(20–27). 지역 정수·allocatable LLSave/III/JJJ·전역 동서/남북 연결 수·길이 200 STR을 선언한다(30–39). |
| 41–70 | 시작 시 18행 Map_Connectors 안. 동서 입력 주석 뒤 `if( ISCONNECT >= 2 )then` (44)은 I2D_Global을 LCM_Global·4 크기로 할당하고 0으로 초기화한다(45–46). `if( process_id == master_id )then` (48)은 mappgew.inp를 장치 1·STATUS='UNKNOWN'으로 열고 READSTR(1)을 호출한다(50–54). NPEWBP_Global 판독 뒤 `if( ISO > 0 ) CALL STOPP('READ ERROR FOR FILE MAPPGEW.INP')` (57). NP=1..NPEWBP_Global에서 좌표 네 개를 읽고 같은 오류 조건을 실행한다(59–62). 이전 좌표 배열 read는 주석이다(60). 파일·master 조건 종료 뒤 Broadcast_Scalar로 개수, Broadcast_Array로 I2D_Global을 배포한다(64–69). |
| 71–109 | 시작 시 18행 Map_Connectors·44행 동서 참 분기 안. III·JJJ는 NPEWBP_Global·2, LLSave는 NPEWBP_Global 크기로 할당하고 배열·NC·NPEWBP를 0으로 초기화한다(72–77). NP=1..NPEWBP_Global에서 M=0(80–81). `III(NP,1) = IG2IL(I2D_Global(NP,1))` (82), `JJJ(NP,1) = JG2JL(I2D_Global(NP,2))` (83). `if( III(NP,1) > 0 .and. III(NP,1) <= IC )then` (84) 안의 `if( JJJ(NP,1) > 0 .and. JJJ(NP,1) <= JC )then` (85)은 `M = M + 1` (86). 두 번째 끝점은 `III(NP,2) = IG2IL(I2D_Global(NP,3))` (90), `JJJ(NP,2) = JG2JL(I2D_Global(NP,4))` (91). `if( III(NP,2) > 0 .and. III(NP,2) <= IC )then` (92), `if( JJJ(NP,2) > 0 .and. JJJ(NP,2) <= JC )then` (93) 안에서 `M = M + 1` (94). `if( M == 1 )then` (98)은 영역 불일치 로그와 STOPP('',1)를 호출한다(99–100). `elseif( M == 2 )then` (101)은 `NPEWBP = NPEWBP + 1` (103), `NC = NC + 1` (105), LLSave(NC)=NP 복사(106). 조건·루프 종료와 빈 줄(107–109). |
| 110–143 | 시작 시 18행 Map_Connectors·44행 동서 참 분기 안. `if( NPEWBP > 0 )then` (111)은 IEPEW·IWPEW·JEPEW·JWPEW를 NPEWBP 크기로 할당한다(112–115). NC=1..NPEWBP에서 LLSave로 전역 연결 번호를 찾고 III/JJJ의 두 끝점을 지역 배열에 복사한다(117–122). 조건 밖에서 WriteBreak와 전역·지역 연결 보고서를 출력한다(127–137). 보고 루프는 NP=1..NPEWBP이며 지역 번호 출력 인수는 NC이다(132–134). I2D_Global·III·JJJ·LLSave를 해제한다(139–140). 동서 조건 종료와 빈 줄(142–143). |
| 144–173 | 시작 시 18행 Map_Connectors 안이며 동서 조건 밖. 남북 입력 주석 뒤 `if( ISCONNECT == 1 .or. ISCONNECT == 3 )then` (147)은 I2D_Global을 LCM_Global·4로 할당하고 0으로 초기화한다(148–149). `if( process_id == master_id )then` (151)은 mappgns.inp를 열고 READSTR(1)을 호출한다(153–157). 개수 판독 뒤 `if( ISO > 0 ) CALL STOPP('READ ERROR FOR FILE MAPPGNS.INP')` (160). NP=1..NPNSBP_Global에서 좌표 네 개를 읽고 같은 오류 조건을 실행한다(162–165). 이전 좌표 배열 read는 주석이다(163). close·master 조건 종료 뒤 Broadcast_Scalar로 개수, Broadcast_Array로 좌표를 배포한다(167–172). |
| 174–212 | 시작 시 18행 Map_Connectors·147행 남북 참 분기 안. III·JJJ는 NPNSBP_Global·2, LLSave는 NPNSBP_Global 크기로 할당한다(175). 배열·NC·NPNSBP를 0으로 초기화한다(176–180). NP=1..NPNSBP_Global에서 M=0(183–184). `III(NP,1) = IG2IL(I2D_Global(NP,1))` (185), `JJJ(NP,1) = JG2JL(I2D_Global(NP,2))` (186). `if( III(NP,1) > 0 .and. III(NP,1) <= IC )then` (187), `if( JJJ(NP,1) > 0 .and. JJJ(NP,1) <= JC )then` (188) 안에서 `M = M + 1` (189). `III(NP,2) = IG2IL(I2D_Global(NP,3))` (193), `JJJ(NP,2) = JG2JL(I2D_Global(NP,4))` (194). `if( III(NP,2) > 0 .and. III(NP,2) <= IC )then` (195), `if( JJJ(NP,2) > 0 .and. JJJ(NP,2) <= JC )then` (196) 안에서 `M = M + 1` (197). `if( M == 1 )then` (201)은 오류 출력·STOPP('',1)(202–203). `elseif( M == 2 )then` (204)은 `NPNSBP = NPNSBP + 1` (206), `NC = NC + 1` (208), LLSave(NC)=NP 복사(209). 조건·루프 종료와 빈 줄(210–212). |
| 213–248 | 시작 시 18행 Map_Connectors·147행 남북 참 분기 안. `if( NPNSBP > 0 )then` (214)은 INPNS·ISPNS·JNPNS·JSPNS를 NPNSBP 크기로 할당한다(215–218). NC=1..NPNSBP에서 LLSave로 전역 번호를 찾고 두 끝점 좌표를 복사한다(220–225). 조건 밖에서 WriteBreak와 남북 연결 보고서를 출력한다(229–239). 보고 루프는 NP=1..NPNSBP이며 지역 번호 출력 인수는 NC이다(234–236). I2D_Global·III·JJJ·LLSave 해제와 남북 조건 종료(241–243). return·빈 줄·루틴 종료·마지막 빈 줄(244–248). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25·30–32: 가져온 SKIPCOM과 지역 변수 MS·L·MMAX·MMIN·NQWR_GL은 사용되지 않는다.
- 45·56–63·148·159–166: I2D_Global의 첫 차원은 LCM_Global이다. 판독 반복 상한은 입력 연결 수이다. 이 블록에는 두 연결 수가 LCM_Global 이하인지 검사하는 문장이 없다.
- 57·62·160·165: 판독 오류 조건은 ISO>0이다. 이 파일에는 ISO<0 검사 분기가 없다.
- 84–96·187–199: 끝점 판정은 지역 i/j의 1..IC·1..JC 범위만 사용한다. 이 판정 블록에는 LIJ의 활성 셀 여부나 고스트 셀(ghost cell) 제외 조건이 없다.
- 132–134·234–236: 보고 루프 변수는 NP이다. 지역 연결 번호 열에는 앞의 NC 루프가 끝난 뒤의 NC를 전달한다.
- 201–203·231–233: 남북 연결 오류 문장은 E/W CELL CONNECTORS로 적는다. 남북 보고서의 좌표 열 제목도 IW·JW·IE·JE이다.
