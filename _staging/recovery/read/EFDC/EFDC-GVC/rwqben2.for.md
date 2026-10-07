---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqben2.for
lines: 136
sha256: d06308d3671a25b6af38ee02d14461f22791a6bbbc1e74e8182420795a672a0c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqben2.for — 판독 구간 기록

구간은 1행부터 136행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 머리말과 `SUBROUTINE RWQBEN2 (TIMTMP)` (6). 1998년 시간 변화 저질 플럭스(benthic flux) 추가 및 수정일·버전·변경 이력 주석(10–26). 목적 주석은 PO4D·NH4·NO3·SAD·COD·O2의 공간·시간별 입력이다(31–32). BENFN 형식 예시 주석은 제목 3행, 적용 날짜 270.00000·350.00000, 구역(zone)별 6개 플럭스, IWQZ개 구역, 마지막 큰 날짜 9999.99999를 적는다(35–48). 이 날짜들은 주석의 예시이며 실행 기본값 대입이 아니다. |
| 50–76 | 시작 시 6행 RWQBEN2 안. EFDC.PAR·EFDC.CMN 포함(50–51). NSMZM 크기 6개 플럭스 배열·IZONE, 79자 TITLE(3)·1자 CCMRM 선언(53–56). BENFN을 단위 1·STATUS='UNKNOWN', WQ3D.OUT을 단위 2·append로 연다(58–59). 제목 3행을 읽어 로그에 쓴 뒤(62–64) `REWIND(1)` (68), CCMRM='#'(69), `CALL SKIPCOMM(1, CCMRM)` (70). 다음 자유 형식(list-directed) 입력은 IBENZ 구역 수이다(72). TIMTMP·IBENZ를 FORMAT 65로 출력한다(73–75). 포함 파일과 SKIPCOMM 내부는 판독하지 않았다. |
| 77–101 | 시작 시 6행 RWQBEN2 안. 주석은 BDAY=현재 적용 날짜, BENDAY=다음 변경 날짜라고 정의한다(80–81). 라벨 10의 `READ(1, *, END=15) BENDAY` (83). `IF(BENDAY .GT. TIMTMP) GOTO 20` (84)이면 검색을 끝낸다. 그 밖에는 BDAY=BENDAY 복사(85), I=1..IBENZ에서 MM과 XBFPO4D(MM)·XBFNH4(MM)·XBFNO3(MM)·XBFSAD(MM)·XBFCOD(MM)·XBFO2(MM)을 읽고 IZONE(I)=MM을 저장한다(86–90). 플럭스 READ도 END=15(87). `GOTO 10` (91)으로 다음 날짜를 검사한다. 라벨 15는 예상 밖 파일 끝(end of file)을 BENFN과 함께 경고하고 마지막 날짜 값을 사용한다는 메시지를 쓴다(93–98). 정상 검색과 EOF 경로가 라벨 20으로 합류한다(100). 빈 줄·주석 포함. |
| 102–113 | 시작 시 6행 RWQBEN2 안이며 날짜 검색 루프 밖. BDAY 및 6개 플럭스 열 제목을 로그에 쓴다(102–104). I=1..IBENZ에서 MM=IZONE(I)를 복사해 해당 MM의 6개 플럭스를 출력한다(105–109). 주석은 셀별 진흙(mud)·모래(sand) 플럭스 사이 보간(interpolation)과 XBENMUD를 진흙 백분율이라고 설명한다(111–113). |
| 114–125 | 시작 시 6행 RWQBEN2 안. L=2..LA에서 IZM=IBENMAP(L,1)·IZS=IBENMAP(L,2)·XM=XBENMUD(L)을 복사한다(114–117). 보간 원문: `WQBFPO4D(L) = XM*XBFPO4D(IZM) + (1.0-XM)*XBFPO4D(IZS)` (118), `WQBFNH4(L)  = XM*XBFNH4(IZM)  + (1.0-XM)*XBFNH4(IZS)` (119), `WQBFNO3(L)  = XM*XBFNO3(IZM)  + (1.0-XM)*XBFNO3(IZS)` (120), `WQBFSAD(L)  = XM*XBFSAD(IZM)  + (1.0-XM)*XBFSAD(IZS)` (121), `WQBFCOD(L)  = XM*XBFCOD(IZM)  + (1.0-XM)*XBFCOD(IZS)` (122), `WQBFO2(L)   = XM*XBFO2(IZM)   + (1.0-XM)*XBFO2(IZS)` (123). 루프 종료·주석(124–125). 이 블록에는 XM을 나누거나 범위를 제한하는 문장이 없다. |
| 126–136 | 시작 시 6행 RWQBEN2 안이며 L 루프 밖. 두 파일 CLOSE(126–127). FORMAT 999=1X, 50=A79, 51=I8·10F8.3, 52=I7·1X·A3, 60=날짜 메시지(129–133). 주석·RETURN·END(128·134–136). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35–48·68–72: 파일 형식 예시 주석에는 제목 바로 다음에 날짜가 온다. 활성 코드는 REWIND·SKIPCOMM 호출 뒤 먼저 IBENZ를 읽는다. SKIPCOMM 내부 동작은 이번 판독 범위에 없다.
- 83–90·102–108: 첫 BENDAY가 TIMTMP보다 크면 플럭스와 IZONE 판독 전에 라벨 20으로 이동한다. 이 파일에는 그 경로의 BDAY·IZONE·6개 임시 플럭스 배열 기본 대입이 없다.
- 83·87–98·105–108: 날짜 READ와 구역 플럭스 READ는 모두 END=15로 이동한다. EOF 경로는 경고 후 같은 구역 출력으로 이어지며 이 블록에는 부분 판독 개수를 따로 저장하는 문장이 없다.
- 53–55·72·86–89·114–123: 임시 배열 크기는 NSMZM이다. IBENZ·입력 MM·IBENMAP의 IZM·IZS에 대한 범위 검사는 이 파일에 없다.
- 111–123: 주석은 XBENMUD를 진흙 백분율이라고 적는다. 계산은 XM=XBENMUD(L)을 그대로 사용해 XM과 1.0-XM을 가중치로 쓰며 100으로 나누는 문장은 없다.
- 132–133: FORMAT 52·60이 선언되어 있다. 이 파일의 활성 READ·WRITE는 두 FORMAT을 사용하지 않는다.
