---
file: models/EFDC/raw/source_code/EFDC-GVC/lvelpltv.for
lines: 389
sha256: 4e982bba323b918f4340135f8a1fbd2224155357e11efc4508961bbc58d0e85f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# lvelpltv.for — 판독 구간 기록

구간은 1행부터 389행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 구분 주석과 `SUBROUTINE LVELPLTV` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 주석(7–18). 임의 I/J 점 열의 수직면(vertical plane) 법선 속도(normal velocity) 등치선과 접선 속도(tangential velocity)·수직 속도 벡터를 쓴다는 주석(19–21). EFDC.PAR·EFDC.CMN 포함(25–26). RVELN/RVELT/RW는 KCM×100, HLRAVG는 LCM 크기이다(30–32). 길이 80 제목 여섯 개와 구분 주석을 포함한다(34–39). 포함 파일 내부는 판독하지 않았다. |
| 40–70 | 시작 시 6행 LVELPLTV 안. 법선·접선 등치선 및 접선/수직 벡터의 일반·평균 제목을 설정하고 LEVELS=KC로 정한다(42–49). `IF(ISECVPV.GE.1)THEN` (51)이면 LMVCNV1.OUT·ALVCNV1.OUT·LMVCVT1.OUT·ALVCVT1.OUT·LMVVCV1.OUT·ALVVCV1.OUT을 각각 단위 11·21·41·51·71·81로 열고 삭제한 뒤 다시 연다(52–69). 조건을 닫는다(70). |
| 71–110 | 시작 시 6행 LVELPLTV 안. `IF(ISECVPV.GE.2)THEN` (71)에서 같은 여섯 접두사의 2.OUT 파일을 단위 12·22·42·52·72·82로 열고 삭제한 뒤 다시 연다(72–90). 별도 `IF(ISECVPV.GE.3)THEN` (91)에서 3.OUT 파일을 단위 13·23·43·53·73·83로 같은 순서로 처리한다(92–110). |
| 111–150 | 시작 시 6행 LVELPLTV 안. `IF(ISECVPV.GE.4)THEN` (111)에서 여섯 4.OUT 파일을 단위 14·24·44·54·74·84로 열고 삭제한 뒤 다시 연다(112–130). 별도 `IF(ISECVPV.GE.5)THEN` (131)에서 여섯 5.OUT 파일을 단위 15·25·45·55·75·85로 같은 순서로 처리한다(132–150). |
| 151–190 | 시작 시 6행 LVELPLTV 안. `IF(ISECVPV.GE.6)THEN` (151)에서 여섯 6.OUT 파일을 단위 16·26·46·56·76·86으로 열고 삭제한 뒤 다시 연다(152–170). 별도 `IF(ISECVPV.GE.7)THEN` (171)에서 여섯 7.OUT 파일을 단위 17·27·47·57·77·87로 같은 순서로 처리한다(172–190). |
| 191–231 | 시작 시 6행 LVELPLTV 안. `IF(ISECVPV.GE.8)THEN` (191)에서 여섯 8.OUT 파일을 단위 18·28·48·58·78·88로 열고 삭제한 뒤 다시 연다(192–210). 별도 `IF(ISECVPV.GE.9)THEN` (211)에서 여섯 9.OUT 파일을 단위 19·29·49·59·79·89로 같은 순서로 처리한다(212–230). 끝 주석을 포함한다(231). |
| 232–261 | 시작 시 6행 LVELPLTV 안. IS=1..ISECVPV 루프(232)에서 `LUN1=10+IS` (233), `LUN2=20+IS` (234), `LUN4=40+IS` (235), `LUN5=50+IS` (236), `LUN7=70+IS` (237), `LUN8=80+IS` (238)로 출력 단위를 계산한다. LINES=NIJVPV(IS)(239). 여섯 파일에 제목·CVTITLE, LINES/LEVELS, K=1..KC의 ZZ를 쓴다(240–257). 루프 종료·구분 주석도 포함한다(258–261). |
| 262–284 | 시작 시 6행 LVELPLTV 안. M=1..MLRPDRT와 IS=1..ISECVPV 루프를 연다(262·264). `LUN1=10+IS` (265), `LUN4=40+IS` (266), `LUN7=70+IS` (267)로 일반 파일 단위를 계산하고 NLRPDRT(M)를 쓴다(268–270). 회전 계수는 `COSC=COS(PI*ANGVPV(IS)/180.)` (271), `SINC=SIN(PI*ANGVPV(IS)/180.)` (272). NN=1..NIJVPV(IS), K=1..KC 루프(273·277)의 법선 식은 `RVELN(K,NN)=100.*(XLRPD(NLRPDL(L),K,M)*COSC` (278), `&            +YLRPD(NLRPDL(L),K,M)*SINC)` (279). 접선 식은 `RVELT(K,NN)=-100.*XLRPD(NLRPDL(L),K,M)*SINC` (280), `&            +100.*YLRPD(NLRPDL(L),K,M)*COSC` (281). 수직 식은 `RW(K,NN)=100.*ZLRPD(NLRPDL(L),K,M)` (282). K·NN 루프를 닫는다(283–284). |
| 285–306 | 시작 시 6행 LVELPLTV·262행 M·264행 IS 루프 안. 새 NN 루프에서 I/J/L을 찾는다(285–288). `ZETA=HLPF(L)-HMP(L)` (289), HBTMP=HMP(L)(290). 대체 `C      HBTMP=SHPLTV*HMP(L)+SBPLTV*BELV(L)` (291)과 HMP 직접 출력문 세 개(292–294)는 주석이다. 세 일반 파일에 위치·ZETA/HBTMP를 쓰고 법선 배열, 접선 배열, 접선/수직 배열을 각각 쓴다(295–301). NN·IS·M 루프를 닫고 주석으로 끝난다(302–306). |
| 307–317 | 시작 시 6행 LVELPLTV 안. IS 루프에서 `LUN1=10+IS` (308), `LUN4=40+IS` (309), `LUN7=70+IS` (310)를 다시 계산하여 세 일반 파일을 닫는다(311–314). 구분 주석도 포함한다(315–317). |
| 318–331 | 시작 시 6행 LVELPLTV 안. NLR=1..NLRPD의 HLRAVG를 0으로 초기화한다(318–320). M=1..MLRPDRT·NLR 루프(321–322)에서 `HLRAVG(NLR)=HLRAVG(NLR)+HLRPD(NLR,M)` (323)를 누적한다. 이어 NLR 루프(326)의 `HLRAVG(NLR)=HLRAVG(NLR)/FLOAT(MLRPDRT)` (327)로 평균한다. M=MLRAVG를 설정한다(330). |
| 332–352 | 시작 시 6행 LVELPLTV 안. IS 루프(332)에서 `LUN2=20+IS` (333), `LUN5=50+IS` (334), `LUN8=80+IS` (335)로 평균 파일 단위를 계산하고 N을 쓴다(336–338). `COSC=COS(PI*ANGVPV(IS)/180.)` (339), `SINC=SIN(PI*ANGVPV(IS)/180.)` (340). NN·K 루프(341·345)의 식은 `RVELN(K,NN)=100.*(XLRPD(NLRPDL(L),K,M)*COSC` (346), `&            +YLRPD(NLRPDL(L),K,M)*SINC)` (347), `RVELT(K,NN)=-100.*XLRPD(NLRPDL(L),K,M)*SINC` (348), `&            +100.*YLRPD(NLRPDL(L),K,M)*COSC` (349), `RW(K,NN)=100.*ZLRPD(NLRPDL(L),K,M)` (350). K·NN 루프를 닫는다(351–352). |
| 353–375 | 시작 시 6행 LVELPLTV·332행 IS 루프 안. 새 NN 루프에서 I/J/L을 찾는다(353–356). `ZETA=HLPF(L)-HMP(L)` (357), HBTMP=HMP(L)(358). `C      HBTMP=SHPLTV*HMP(L)+SBPLTV*BELV(L)` (359)과 HMP 직접 출력문(360–362)은 주석이다. 위치·ZETA/HBTMP와 법선·접선·접선/수직 배열을 평균 파일에 쓴다(363–369). NN 루프 종료 뒤 세 평균 파일을 닫고 IS 루프를 닫는다(370–374). |
| 376–389 | 시작 시 6행 LVELPLTV 안. 제목 A40/2X/A20, 단계 I10, 헤더 2I10, 위치 2I5·6E14.6, 배열 12E12.4의 FORMAT(378–382). CMRM 대체 FORMAT은 주석이다(383–384). 구분 주석·RETURN·END로 끝난다(385–389). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–32·273·277–282·341·345–350: 속도 작업 배열의 두 번째 크기는 100이다. NN의 상한 NIJVPV(IS)를 100과 비교하는 문장은 이 파일에 없다.
- 51–230·232–258: 명시적 OPEN 블록은 단면 1..9에만 있다. 헤더 출력 루프의 상한은 ISECVPV이며, 이 파일에는 ISECVPV<=9 검사가 없다.
- 318–327·357–358: HLRAVG를 누적·평균한 뒤 이 파일의 출력식에서 다시 참조하지 않는다. 평균 파일의 ZETA와 HBTMP는 HLPF·HMP에서 계산한다.
- 327: HLRAVG 평균의 분모는 FLOAT(MLRPDRT)이다. 이 나눗셈 앞에 MLRPDRT=0을 검사하는 조건은 없다.
- 268–270·336–338: 일반 파일의 단계 기록은 NLRPDRT(M)이다. 평균 파일의 단계 기록은 N이다.
