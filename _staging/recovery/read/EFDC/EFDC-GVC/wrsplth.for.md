---
file: models/EFDC/raw/source_code/EFDC-GVC/wrsplth.for
lines: 190
sha256: 11f7bb499ae2a3bd5a8fdc5c3fa596472dc3c16c9ae660504cee2b99fedcf590
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wrsplth.for — 판독 구간 기록

구간은 1행부터 190행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | `WRSPLTH` 시작(6). 버전·수정 날짜·변경 기록 틀을 적는다(8–17). 수평면(horizontal plane)의 잔류 스칼라장 등치선(residual scalar field contouring) 파일을 쓴다는 주석은 루틴명을 RSALPLTH로 적는다(19–20). `EFDC.PAR`·`EFDC.CMN`을 포함한다(24–25). REAL DBS(10)·CHARACTER*80 TITLE을 선언한다(29–30). |
| 34–45 | 시작 시 6행 WRSPLTH 루틴 안. JSWRPH!=1이면 300행 라벨이 있는 90행으로 이동하여 초기 헤더 블록을 건너뛴다(34). 그 외 경로는 출력 셀 수 LINES=LA-1, LEVELS=2·LEVELSS=3·LEVEL1=1과 DBS의 0·99·-99를 설정한다(38–44). 원문 조건·계산식·반복·호출: `IF(JSWRPH.NE.1) GOTO 300` (34), `LINES=LA-1` (38), `LEVELS=2` (39), `LEVELSS=3` (40), `LEVEL1=1` (41), `DBS(1)=0.` (42), `DBS(2)=99.` (43), `DBS(3)=-99.` (44). |
| 46–75 | 시작 시 6행 WRSPLTH 루틴 안. 34행에서 GOTO를 실행하지 않은 초기 헤더 경로. 파랑 레이놀즈 응력(wave Reynolds stress) RXX·RYY·RXY의 TITLE과 장치 21·22·23을 설정한다(46–47·56–57·66–67). WVRXXH.OUT·WVRYYH.OUT·WVRXYH.OUT을 열어 삭제 후 다시 열고 제목·LINES/LEVELS·DBS(1..LEVELS)를 쓴다(48–54·58–64·68–74). 원문 조건·계산식·반복·호출: `TITLE=' WAVE REYNOLDS STRESS RXX '` (46), `LUN=21` (47), `TITLE=' WAVE REYNOLDS STRESS RYY '` (56), `LUN=22` (57), `TITLE=' WAVE REYNOLDS STRESS RXY '` (66), `LUN=23` (67). |
| 76–91 | 시작 시 6행 WRSPLTH 루틴 안. 34행에서 GOTO를 실행하지 않은 초기 헤더 경로. 파랑 소산(wave dissipation) 제목의 단위 표기는 (M/S)**3이며 장치는 53이다(76–77). WVDISP.OUT을 삭제한 뒤 이름 WVDISP로 열어 제목·LINES/LEVEL1·DBS(1)을 쓴다(78–84). JSWRPH=0으로 바꾼다(86). 라벨 300 CONTINUE가 90행에 있고 초기화 경로와 건너뛰기 경로가 여기서 합류한다. 원문 조건·계산식·반복·호출: `TITLE=' WAVE DISSIPATION, (M/S)**3 '` (76), `LUN=53` (77), `JSWRPH=0` (86). |
| 92–108 | 시작 시 6행 WRSPLTH 루틴 안. 응력 COL 파일 세 개를 장치 11·12·13에서 추가 모드로 열고 삭제한 뒤 다시 추가 모드로 연다(92–100). 파랑 힘 COL 파일 WVFXH.COL·WVFYH.COL에도 장치 31·32로 같은 작업을 한다(102–107). 이 블록은 34행의 조건 경로가 합류한 뒤 실행한다. |
| 109–126 | 시작 시 6행 WRSPLTH 루틴 안. WVUBH.COL·WVVBH.COL, WVKX.COL·WVKY.COL, WVDISP.COL을 각각 장치 41·42·51·52·54에서 열고 삭제한 뒤 추가 모드로 다시 연다(109–125). 이 구간은 파일 준비 블록이며 값 계산·출력 루프는 다음 구간에 있다. |
| 127–160 | 시작 시 6행 WRSPLTH 루틴 안. 응력 OUT 세 개는 추가 모드로, WVDISP.OUT은 POSITION 없이 연다(127–130). 응력 OUT에 시간 단계 N을 쓴다(132–134). L=2..LA에서 RXX/RYY의 표층(surface layer)·저층(bottom layer) 합과 RXY를 위치·좌표와 함께 출력한다(136–147). 표층 파랑 소산을 OUT에 출력한다(148). 두 면 파랑 힘의 평균을 COL에 쓴다(149–152). 파랑 속도·방향 성분 계산/출력은 주석이다(153–158). 소산 COL을 출력하고 루프를 닫는다(159–160). 원문 조건·계산식·반복·호출: `DO L=2,LA` (136), `WVRSTOP=WVHUU(L,KC)+WVPP(L,KC)` (137), `WVRSBOT=WVHUU(L,1)+WVPP(L,1)` (138), `WVRSTOP=WVHVV(L,KC)+WVPP(L,KC)` (141), `WVRSBOT=WVHVV(L,1)+WVPP(L,1)` (142), `FXWTMP=0.5*(FXWAVE(L,KC)+FXWAVE(L+1   ,KC))` (149), `FYWTMP=0.5*(FYWAVE(L,KC)+FYWAVE(LNC(L),KC))` (150). |
| 161–176 | 시작 시 6행 WRSPLTH 루틴 안. 장치 11·12·13·21·22·23·31·32·41·42·51·52·53·54를 모두 닫는다(162–175). 빈 주석을 포함한다(161·176). |
| 177–190 | 시작 시 6행 WRSPLTH 루틴 안. 제목 A80, 단계 I10, 헤더 2I10, 자료 2I5/1X/6E14.6, DBS 12E12.4의 FORMAT을 정의한다(179–183). 대체 FORMAT은 주석이다(184–185). 구분 주석·RETURN·END로 끝낸다(177–190). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·19: 실행 루틴명은 WRSPLTH이며 목적 주석의 루틴명은 RSALPLTH이다.
- 78–84·130·148: 초기화는 WVDISP.OUT을 삭제한 뒤 WVDISP라는 다른 이름에 헤더를 쓴다. 후속 자료 출력은 WVDISP.OUT을 연다.
- 40·44·53·63·73·83: LEVELSS=3과 DBS(3)=-99를 설정하지만 실행 출력은 LEVELS=2 또는 LEVEL1=1 범위만 참조한다. LEVELSS는 이후 참조되지 않는다.
- 92–125: COL 파일 열기에 POSITION='APPEND'를 쓰지만 매 호출 이 블록에서 먼저 STATUS='DELETE'로 삭제한다.
- 109–121·153–158·170–173: 장치 41·42·51·52의 COL 파일은 생성·삭제·재생성·닫기를 수행한다. 이 장치들의 값 계산·WRITE 문장은 주석이다.
- 127–130: 응력 OUT 세 개의 OPEN에는 POSITION='APPEND'가 있고 WVDISP.OUT의 OPEN에는 POSITION 지정이 없다.
