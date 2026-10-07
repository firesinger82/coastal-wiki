---
file: models/EFDC/raw/source_code/EFDC-GVC/rsalplth.for
lines: 348
sha256: e0e7fda031c251340a998a73d6207ce053ab6e4490ab9bd9547ae4aaa6345e40
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rsalplth.for — 판독 구간 기록

구간은 1행부터 348행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 머리말과 `SUBROUTINE RSALPLTH(ICON,CONC)` (6). 주석은 수평면 잔차 스칼라장(residual scalar field)의 등치선(contour) 파일 작성 목적을 적는다(19–20). `EFDC.PAR`·`EFDC.CMN` 포함(24–25), CONC(LCM,KCM)·DBS(10)·80자 TITLE 선언(29–31). `IF(JSRSPH(ICON).NE.1) GOTO 300` (35)이면 초기화를 건너뛴다. 초기화 경로의 `LINES=LA-1` (39), `LEVELS=2` (40), `LEVELSS=3` (41), `DBS(1)=0.` (42), `DBS(2)=99.` (43), `DBS(3)=-99.` (44). 구분 주석 포함. 포함 파일 내부는 판독하지 않았다. |
| 46–81 | 시작 시 6행 RSALPLTH 안이며 35행 점프를 하지 않은 경로. 독립 `IF(ISTRAN(1).GE.1)THEN` (46), `IF(ISTRAN(2).GE.1)THEN` (58), `IF(ISTRAN(3).GE.1)THEN` (70). 각각 염분(salinity) RSALCNH.OUT·단위 11, 온도(temperature) RTEMCNH.OUT·12, 염료(dye) RDYECNH.OUT·13을 열고 삭제 후 재개방한다(47–51·59–63·71–75). 제목·LINES·LEVELS=2·DBS 앞 2개를 기록하고 닫는다(52–56·64–68·76–80). |
| 82–105 | 시작 시 6행 RSALPLTH 안이며 초기화 경로. `IF(ISTRAN(6).GE.1)THEN` (82)은 점착성 퇴적물(cohesive sediment) RSEDCNH.OUT·단위 14를 재생성한다(83–87). `IF(ISTRAN(7).GE.1)THEN` (94)은 비점착성 퇴적물(noncohesive sediment) RSNDCNH.OUT·단위 15를 재생성한다(95–99). 각 제목·LINES·LEVELSS=3·DBS 앞 3개를 기록하고 닫는다(88–92·100–104). |
| 106–144 | 시작 시 6행 RSALPLTH 안이며 초기화 경로. `IF(ISTRAN(5).GE.1)THEN` (106)은 독성물질(toxic contaminant) RTOXCNH.OUT·단위 16과 입자 결합 분율(particulate fraction) RTXPCNH.OUT·26을 재생성한다(107–124). `IF(ISTRAN(4).GE.1)THEN` (127)은 제목에 SFL을 쓰고 RSFLCNH.OUT·단위 17을 재생성한다(128–136). 세 파일에 제목·LINES·LEVELSS=3·DBS 앞 3개를 쓴다. ITMP=1..7의 JSRSPH를 모두 0으로 설정한다(139–141). 구분 주석(138·142–144). |
| 145–178 | 시작 시 6행 RSALPLTH 안. 점프 도착 라벨 300(145). 독립 `IF(ICON.EQ.1)THEN` (147), `IF(ICON.EQ.2)THEN` (151), `IF(ICON.EQ.3)THEN` (155), `IF(ICON.EQ.6)THEN` (159), `IF(ICON.EQ.7)THEN` (163), `IF(ICON.EQ.5)THEN` (167), `IF(ICON.EQ.4)THEN` (174). 각 초기화와 같은 파일·단위로 append 개방한다(148–176). ICON=5는 RTOXCNH.OUT과 RTXPCNH.OUT을 함께 연다(168–172). |
| 179–190 | 시작 시 6행 RSALPLTH 안. `IF(ISDYNSTP.EQ.0)THEN` (179)이면 `TIME=DT*FLOAT(N)+TCON*TBEGIN` (180), `TIME=TIME/TCON` (181). `ELSE` (182)는 `TIME=TIMESEC/TCON` (183). 단위 LUN에 N·TIME을 쓰고(186), `IF(ICON.EQ.5)THEN` (187)이면 LUNF에도 쓴다(188). |
| 191–215 | 시작 시 6행 RSALPLTH 안. `IF(ISPHXY(ICON).EQ.0)THEN` (191)은 좌표 없이 값을 쓴다. 독립 `IF(ICON.LE.3)THEN` (192), `IF(ICON.GE.8)THEN` (197)은 L=2..LA의 CONC(L,KC)·CONC(L,1)을 출력한다(193–200). `IF(ICON.EQ.6)THEN` (202)은 SEDBTLPF(L,KBT(L))를 추가한다(203–207). `IF(ICON.EQ.7)THEN` (209)은 SNDBTLPF(L,KBT(L))를 추가한다(210–214). SEDBT 계산 대안은 주석이다(204·211). |
| 216–237 | 시작 시 6행 RSALPLTH·191행 좌표 없는 출력 분기 안. `IF(ICON.EQ.5)THEN` (216)은 L=2..LA에서 `TOXBT=1000.*TOXBLPF(L,KBT(L),1)` (218)을 계산해 표층·저층 CONC와 출력한다(219–220). 별도 L 루프에서 TXPFLPF(L,KC,1,1)·TXPFLPF(L,1,1,1)·TOXBLPF(L,KBT(L),1)을 LUNF에 출력하고 닫는다(222–227). SEDBT 대안은 주석(223). `IF(ICON.EQ.4)THEN` (229)은 표층·저층 CONC와 SFLSBOT(L)을 출력한다(230–233). ICON 분기와 191행 분기 종료(234–235), 주석(236–237). |
| 238–262 | 시작 시 6행 RSALPLTH 안. `IF(ISPHXY(ICON).EQ.1)THEN` (238)은 IL(L)·JL(L)을 앞에 쓴다. `IF(ICON.LE.3)THEN` (239), `IF(ICON.GE.8)THEN` (244)은 표층·저층 CONC 출력(240–247). `IF(ICON.EQ.6)THEN` (249)은 SEDBTLPF를 추가한다(250–254). `IF(ICON.EQ.7)THEN` (256)은 SNDBTLPF를 추가한다(257–261). 각 L 범위는 2..LA이다. 대안 SEDBT 식은 주석이다(251·258). |
| 263–284 | 시작 시 6행 RSALPLTH·238행 격자 인덱스 출력 분기 안. `IF(ICON.EQ.5)THEN` (263)은 `TOXBT=1000.*TOXBLPF(L,KBT(L),1)` (265)을 계산하고 IL·JL·표층·저층 CONC·TOXBT를 출력한다(264–268). LUNF에는 IL·JL·표층·저층 TXPFLPF·저질 TOXBLPF를 쓰고 닫는다(269–274). SEDBT 대안은 주석(270). `IF(ICON.EQ.4)THEN` (276)은 IL·JL·표층·저층 CONC·SFLSBOT를 출력한다(277–280). 두 분기 종료(281–282), 주석(283–284). |
| 285–309 | 시작 시 6행 RSALPLTH 안. `IF(ISPHXY(ICON).EQ.2)THEN` (285)은 IL·JL·DLON·DLAT를 앞에 쓴다. `IF(ICON.LE.3)THEN` (286), `IF(ICON.GE.8)THEN` (291)은 표층·저층 CONC를 출력한다(287–294). `IF(ICON.EQ.6)THEN` (296)은 SEDBTLPF를 추가한다(297–301). `IF(ICON.EQ.7)THEN` (303)은 SNDBTLPF를 추가한다(304–308). L 범위는 2..LA이다. 대안 SEDBT 식은 주석(298·305). |
| 310–330 | 시작 시 6행 RSALPLTH·285행 좌표 포함 출력 분기 안. `IF(ICON.EQ.5)THEN` (310)에서 `TOXBT=1000.*TOXBLPF(L,KBT(L),1)` (312), IL·JL·DLON·DLAT·표층·저층 CONC·TOXBT 출력(311–315). LUNF에는 같은 좌표 및 표층·저층 TXPFLPF·저질 TOXBLPF를 출력하고 닫는다(316–321). 주석 대안(317). `IF(ICON.EQ.4)THEN` (323)은 같은 좌표와 표층·저층 CONC·SFLSBOT를 출력한다(324–327). ICON 분기·285행 분기 종료(328–329), 주석(330). |
| 331–348 | 시작 시 6행 RSALPLTH 안이며 좌표 선택 분기 밖. LUN CLOSE(331), 구분 주석(332–334). 제목 A80, 시간 I10·F12.4, 크기 2I10, 좌표 및 실수 `200 FORMAT(2I5,1X,6E14.6)` (338), DBS 12E12.4, 좌표 없는 6E14.6, 추가 13E11.3 형식(335–341). CMRM 대안 FORMAT은 주석(342–343). 구분 주석·RETURN·END(344–348). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35·46–141: JSRSPH(ICON) 하나로 초기화 진입을 결정한다. 초기화 경로는 활성 ISTRAN 전체 파일을 재생성하고 JSRSPH(1..7)을 모두 0으로 설정한다.
- 147–177·197–200·244–247·291–294: ICON>=8 출력 분기가 있다. 파일 선택 분기는 ICON=1..7에만 있으며 ICON>=8에서 LUN을 설정하는 문장은 이 파일에 없다.
- 127–135·229–233·276–280·323–327: SFL 파일 머리말은 LEVELSS=3이다. 세 번째 출력값은 SFLSBOT(L)이다.
- 218–225·265–272·312–319: 주 농도 파일의 저질 독성물질 값은 TOXBLPF에 1000을 곱한다. 입자 결합 분율 파일의 세 번째 값은 TOXBLPF를 그대로 쓴다.
- 187–189·191·227·238·274·285·321: ICON=5의 LUNF는 좌표 선택 전에 열린 상태로 시간 기록을 받는다. LUNF CLOSE는 ISPHXY=0·1·2의 ICON=5 분기 안에만 있다.
- 335–341: FORMAT 420이 선언되어 있다. 이 파일의 WRITE 문은 FORMAT 420을 사용하지 않는다.
