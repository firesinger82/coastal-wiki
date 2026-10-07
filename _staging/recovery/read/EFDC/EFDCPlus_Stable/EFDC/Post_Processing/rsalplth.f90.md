---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Post_Processing/rsalplth.f90
lines: 333
sha256: 8343ca24cddc4d1cfc170f4b41e219f55ef23ac3d4d560f5c0ac78bb376ca714
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rsalplth.f90 — 판독 구간 기록

구간은 1행부터 333행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | EFDC+·GPLv2·저작권 머리말(1–8), `SUBROUTINE RSALPLTH(ICON,CONC)` (9). 수평면 잔차(residual) 스칼라 등치선(contour) 출력이라는 주석(11–12). GLOBAL·Variables_MPI 사용, implicit none(16–19). 입력 ICON과 CONC(LCM,KCM), 지역변수 DBS(10)·시간·TOXBT 선언(21–27). `IF( JSRSPH(ICON) /= 1) GOTO 300` (29)은 파일 머리말 초기화를 건너뛴다. `LINES = LA-1` (30), `LEVELS = 2` (31), `LEVELSS = 3` (32), `DBS(1) = 0.` (33), `DBS(2) = 99.` (34), `DBS(3) = -99.` (35). |
| 37–91 | 시작 시 9행 RSALPLTH 안. `IF( ISTRAN(1) >= 1 )THEN` (37), `IF( ISTRAN(2) >= 1 )THEN` (48), `IF( ISTRAN(3) >= 1 )THEN` (59)의 독립 분기는 각각 LUN=11·12·13과 OUTDIR의 RSALCNH.OUT·RTEMCNH.OUT·RDYECNH.OUT을 선택(38–42·49–53·60–64). 파일을 열어 삭제하고 다시 연 뒤 TITLE·LINES/LEVELS·DBS(1:LEVELS)를 쓰고 닫는다(43–46·54–57·65–68). `IF( ISTRAN(6) >= 1 )THEN` (70), `IF( ISTRAN(7) >= 1 )THEN` (81)은 점착성 퇴적물(cohesive sediment)·비점착성 퇴적물(noncohesive sediment)의 LUN=14·15, RSEDCNH.OUT·RSNDCNH.OUT을 같은 방식으로 생성하고 LEVELSS와 DBS(1:LEVELSS)를 쓴다(71–79·82–90). |
| 92–126 | 시작 시 9행 RSALPLTH 안. `IF( ISTRAN(5) >= 1 )THEN` (92)은 독성 오염물(toxic contaminant) RTOXCNH.OUT(LUN=16)과 입자 분율(particulate fraction) RTXPCNH.OUT(LUNF=26)을 삭제 후 재생성한다(93–110). 두 머리말은 LINES·LEVELSS와 DBS(1:LEVELSS)를 사용한다(99–100·108–109). `IF( ISTRAN(4) >= 1 )THEN` (112)은 SFL의 RSFLCNH.OUT(LUN=17)을 같은 방식으로 만들며 LEVELSS를 쓴다(113–121). ITMP=1..7에서 JSRSPH를 모두 0으로 설정(123–125). 300 CONTINUE(126)가 29행 분기의 목적지이다. |
| 127–169 | 시작 시 9행 RSALPLTH 안. 독립 조건 `IF( ICON == 1 )THEN` (127), `IF( ICON == 2 )THEN` (132), `IF( ICON == 3 )THEN` (137), `IF( ICON == 6 )THEN` (142), `IF( ICON == 7 )THEN` (147), `IF( ICON == 5 )THEN` (152), `IF( ICON == 4 )THEN` (160)이 LUN=11·12·13·14·15·16·17과 각각 RSALCNH·RTEMCNH·RDYECNH·RSEDCNH·RSNDCNH·RTOXCNH·RSFLCNH.OUT의 append 열기를 선택한다(128–164). ICON=5는 RTXPCNH.OUT도 LUNF=26으로 연다(156–158). `TIME = TIMESEC/TCON` (165), LUN에 NITER·TIME 출력(166). `IF( ICON == 5 )THEN` (167)은 LUNF에도 NITER·TIME을 쓴다(168). |
| 170–220 | 시작 시 9행 RSALPLTH 안. `IF( ISPHXY(ICON) == 0 )THEN` (170)에서 좌표 없이 L=2..LA를 출력한다. `IF( ICON <= 3 )THEN` (171), `IF( ICON >= 8 )THEN` (176)은 CONC(L,KC)·CONC(L,KSZ(L))의 두 값을 쓴다(173·178). `IF( ICON == 6 )THEN` (181), `IF( ICON == 7 )THEN` (190)은 이 두 값에 각각 SEDBTLPF(L,KBT(L))·SNDBTLPF(L,KBT(L))를 추가(186–187·195–196). `IF( ICON == 5 )THEN` (199)에서는 `TOXBT = 1000.*TOXBLPF(L,KBT(L),1)` (201)을 세 번째 값으로 쓰고(202–203), 별도 L 루프에서 TXPFLPF(L,KC,1,1)·TXPFLPF(L,1,1,1)·TOXBLPF(L,KBT(L),1)을 LUNF에 쓴 뒤 닫는다(205–212). `IF( ICON == 4 )THEN` (214)은 세 번째 값에 SFLSBOT(L)을 쓴다(216–217). 모든 출력은 FORMAT 400이다. SEDBT 계산식은 주석 처리(184·193·207). |
| 221–271 | 시작 시 9행 RSALPLTH 안. `IF( ISPHXY(ICON) == 1 )THEN` (221)은 FORMAT 200에 IL(L)·JL(L)을 앞에 둔다. `IF( ICON <= 3 )THEN` (222), `IF( ICON >= 8 )THEN` (227)은 CONC의 KC·KSZ(L) 값 출력(224·229). `IF( ICON == 6 )THEN` (232), `IF( ICON == 7 )THEN` (241)은 각각 SEDBTLPF·SNDBTLPF 바닥값을 추가(237–238·246–247). `IF( ICON == 5 )THEN` (250)은 `TOXBT = 1000.*TOXBLPF(L,KBT(L),1)` (252)과 두 CONC 값 출력(253–254), 입자 분율 파일에 IL/JL·TXPFLPF(L,KC,1,1)·TXPFLPF(L,1,1,1)·TOXBLPF(L,KBT(L),1)을 쓰고 close(260–263). `IF( ICON == 4 )THEN` (265)은 SFLSBOT(L)을 추가(267–268). L 범위는 각 블록 모두 2..LA이다. 주석 처리된 SEDBT 식도 포함한다(235·244·258). |
| 272–322 | 시작 시 9행 RSALPLTH 안. `IF( ISPHXY(ICON) == 2 )THEN` (272)은 FORMAT 200 출력 앞에 IL/JL·DLON/DLAT을 둔다. `IF( ICON <= 3 )THEN` (273), `IF( ICON >= 8 )THEN` (278)은 두 CONC 값(275·280). `IF( ICON == 6 )THEN` (283), `IF( ICON == 7 )THEN` (292)은 SEDBTLPF·SNDBTLPF 바닥값을 추가(288–289·297–298). `IF( ICON == 5 )THEN` (301)은 `TOXBT = 1000.*TOXBLPF(L,KBT(L),1)` (303), LUN에 두 CONC 값과 TOXBT 출력(304–305), LUNF에 좌표·TXPFLPF(L,KC,1,1)·TXPFLPF(L,1,1,1)·TOXBLPF(L,KBT(L),1)을 쓰고 닫는다(311–314). `IF( ICON == 4 )THEN` (316)은 SFLSBOT(L)을 추가(318–319). 모든 L 루프는 2..LA이다. SEDBT 식은 주석 처리(286·295·309). |
| 323–333 | 시작 시 9행 RSALPLTH 안. LUN close(323). 출력 FORMAT은 A80(324), I10/F12.4(325), 2I10(326), 2I5/1X/6E14.6(327), 12E12.4(328), 1X/6E14.6(329), 1X/13E11.3(330). RETURN·END와 마지막 빈 줄(331–333). 호출하는 별도 계산 루틴은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29·37–125: 초기화 진입은 JSRSPH(ICON)으로 결정한다. 진입 뒤 파일 생성은 해당 ICON만이 아니라 모든 ISTRAN(1:7)의 독립 조건으로 수행하며 JSRSPH(1:7)를 모두 0으로 한다.
- 127–164·176–178·227–229·278–280: 출력 파일과 LUN을 선택하는 조건은 ICON=1..7에만 있다. 데이터 출력에는 ICON>=8 조건도 있고, 이 파일에는 그 값에 대한 LUN 설정이 없다.
- 201·209–210·252·260–261·303·311–312: 독성 오염물의 바닥 출력은 종 인덱스 1로 고정한다. 입자 분율 출력도 마지막 두 인덱스를 1로 고정하고 하부층 인덱스는 KSZ(L) 대신 1을 사용한다.
- 152–158·170–323: ICON=5에서 LUNF를 연다. LUNF close는 ISPHXY(ICON)=0·1·2의 각 분기 안에만 있고, 분기 밖에는 LUN close만 있다.
