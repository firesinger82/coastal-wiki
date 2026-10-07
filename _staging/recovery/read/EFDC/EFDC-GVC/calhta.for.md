---
file: models/EFDC/raw/source_code/EFDC-GVC/calhta.for
lines: 341
sha256: f517eb50e57f8b8bb064c24b25336a1baf414f0419a3a1d9321774b12260afb5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calhta.for — 판독 구간 기록

구간은 1행부터 341행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | `SUBROUTINE CALHTA` (6). 두 조석 주기(tidal cycle)에 걸쳐 M2 조석(tide)의 조화 분석(harmonic analysis)을 수행한다는 주석(19–20). 머리말·수정 기록·구분 주석을 포함한다. `INCLUDE 'EFDC.PAR'` (24), `INCLUDE 'EFDC.CMN'` (25). TITLE1·TITLE2·TITLE3·TITLE4·TITLE11·TITLE12는 CHARACTER*80이다(27). 현재 분석 구간의 최초 진입 초기화 주석을 포함한다(31). |
| 33–63 | 시작 시 6행 CALHTA 루틴 안. `IF(NHAR.GT.1) GOTO 1000` (33)이면 초기화를 건너뛰고 1000 레이블로 이동한다. L=2..LA에서 수면과 수심 평균 속도(depth averaged velocity)의 여섯 조화 누적 배열을 0으로 설정한다(35–42). K=1..KC·L=2..LA에서 층별 u·v의 네 조화 누적 배열을 0으로 설정한다(44–51). 수직 속도(vertical velocity)·AB·2AB의 초기화는 주석이다(53–62). |
| 64–88 | 시작 시 6행 CALHTA 루틴 안. SURFAMP.OUT·SURFPHA.OUT·MAJAXIS.OUT·MAJAPHA.OUT·TIDELKC.OUT·TIDELKB.OUT을 각각 단위 1·2·3·4·11·12로 연 뒤 삭제 종료하고 다시 연다(64–86). 여섯 제목 문자열은 수면 변위 진폭(amplitude)·위상(phase), 조류 타원(tidal ellipse) 장축(major axis)·위상, 수면·바닥 조류 타원이다(67·71·75·79·83·87). 주석을 포함한다. |
| 89–110 | 시작 시 6행 CALHTA 루틴 안. 출력 셀 수·층 수·표시 깊이 설정 `LINES=LA-1` (89); `LEVELS=1` (90); `DBS=0.` (91). 단위 1·2·11에 제목, LINES·LEVELS, DBS를 기록하고 각 파일을 닫는다(93–104). 바닥 표시 깊이 `DBS=99.` (105). 단위 12에 같은 구성의 바닥 헤더를 기록하고 닫는다(106–109). |
| 111–125 | 시작 시 6행 CALHTA 루틴 안. 장축·위상 출력의 층 수·표시 깊이 설정 `LEVELS=2` (111); `DBS1=0.` (112); `DBS2=99.` (113). 단위 3·4에 제목, LINES·LEVELS, 두 표시 깊이를 기록하고 닫는다(115–122). 구분 주석을 포함한다. |
| 126–143 | 시작 시 6행 CALHTA 루틴 안. 조화 분석 누적 주석(126) 및 `1000 CONTINUE` (128). L=2..LA에서 LN=LNC(L)(131). 수면 누적식 `AMCP(L)=P(L)*WC(NHAR)+AMCP(L)` (132); `AMSP(L)=P(L)*WS(NHAR)+AMSP(L)` (133), 수심 평균 속도 평균·깊이 및 격자 길이 보정식 `UTMP1=0.5*(UHDYE(L+1)+UHDYE(L))*HPI(L)/DYP(L)` (134); `VTMP1=0.5*(VHDXE(LN)+VHDXE(L))*HPI(L)/DXP(L)` (135), 좌표 변환(coordinate transformation) `UTMP=CUE(L)*UTMP1+CVE(L)*VTMP1` (136); `VTMP=CUN(L)*UTMP1+CVN(L)*VTMP1` (137), 속도 조화 누적식 `AMCUE(L)=UTMP*WC(NHAR)+AMCUE(L)` (138); `AMSUE(L)=UTMP*WS(NHAR)+AMSUE(L)` (139); `AMCVE(L)=VTMP*WC(NHAR)+AMCVE(L)` (140); `AMSVE(L)=VTMP*WS(NHAR)+AMSVE(L)` (141). L 루프 종료·주석(142–143). |
| 144–157 | 시작 시 6행 CALHTA 루틴 안. K=1..KC·L=2..LA에서 LN=LNC(L)(146). 층별 속도 평균 `UTMP1=0.5*(U(L+1,K)+U(L,K))` (147); `VTMP1=0.5*(V(LN,K)+V(L,K))` (148), 좌표 변환 `UTMP=CUE(L)*UTMP1+CVE(L)*VTMP1` (149); `VTMP=CUN(L)*UTMP1+CVN(L)*VTMP1` (150), 네 조화 누적식 `AMCU(L,K)=UTMP*WC(NHAR)+AMCU(L,K)` (151); `AMSU(L,K)=UTMP*WS(NHAR)+AMSU(L,K)` (152); `AMCV(L,K)=VTMP*WC(NHAR)+AMCV(L,K)` (153); `AMSV(L,K)=VTMP*WS(NHAR)+AMSV(L,K)` (154). 두 루프 종료·주석(155–157). |
| 158–178 | 시작 시 6행 CALHTA 루틴 안. 수직 속도·AB·2AB 조화 누적 루프는 주석이다(158–167). 분석 구간 종료 검사 주석(171). `IF(NHAR.LT.NTSPTC2) GOTO 2000` (173)이면 2000 레이블로 이동하여 이번 호출의 결과 출력을 건너뛴다. 그렇지 않으면 조화 분석 완료 경로로 진행한다(177). 구분 주석을 포함한다. |
| 179–193 | 시작 시 6행 CALHTA 루틴 안. L=2..LA에서 수면의 두 조화 계수 변환 `AMC=AS*AMCP(L)-ACS*AMSP(L)` (180); `AMS=-ACS*AMCP(L)+AC*AMSP(L)` (181) 후 AMC·AMS를 원래 수면 배열에 복사한다(182–183). 수심 평균 u 계수 변환 `AMC=AS*AMCUE(L)-ACS*AMSUE(L)` (184); `AMS=-ACS*AMCUE(L)+AC*AMSUE(L)` (185) 후 AMCUE·AMSUE에 복사한다(186–187). 수심 평균 v 계수 변환 `AMC=AS*AMCVE(L)-ACS*AMSVE(L)` (188); `AMS=-ACS*AMCVE(L)+AC*AMSVE(L)` (189) 후 AMCVE·AMSVE에 복사한다(190–191). 루프 종료·주석(192–193). |
| 194–225 | 시작 시 6행 CALHTA 루틴 안. K=1..KC·L=2..LA에서 층별 u 계수 변환 `AMC=AS*AMCU(L,K)-ACS*AMSU(L,K)` (196); `AMS=-ACS*AMCU(L,K)+AC*AMSU(L,K)` (197) 후 AMCU·AMSU에 복사한다(198–199). 층별 v 계수 변환 `AMC=AS*AMCV(L,K)-ACS*AMSV(L,K)` (200); `AMS=-ACS*AMCV(L,K)+AC*AMSV(L,K)` (201) 후 AMCV·AMSV에 복사한다(202–203). 두 루프 종료(204–205). 수직 속도·AB·2AB의 계수 변환은 주석이다(207–222). NHAR=0으로 재설정한다(224). |
| 226–247 | 시작 시 6행 CALHTA 루틴 안. SURFAMP.OUT·SURFPHA.OUT을 APPEND로 열고 N을 기록한다(226–229). L=2..LA에서 수면 진폭 `SSURFAMP=GI*SQRT(AMCP(L)*AMCP(L)+AMSP(L)*AMSP(L))` (232). `IF(AMCP(L).EQ.0.0.AND.AMSP(L).EQ.0.0)THEN` (233)이면 `PHI=999999.` (234), `ELSE` (235)이면 `PHI=ATAN2(AMSP(L),AMCP(L))` (236). 시간 단위 위상 변환 `SSURFPHS=TIDALP*PHI/(3600.*PI2)` (238); `SSURFPSC=TIDALP*PHI/PI2` (239), 음의 초 단위 위상 보정 `IF(SSURFPSC.LT.0.0)SSURFPSC=SSURFPSC+TIDALP` (240). 단위 1은 격자 인덱스·경위도·진폭·초 단위 위상을 출력하고, 단위 2는 격자 인덱스·경위도·시간 단위 위상 두 개를 출력한다(241–242). 루프·파일 종료·주석(243–247). |
| 248–256 | 시작 시 6행 CALHTA 루틴 안. MAJAXIS.OUT·MAJAPHA.OUT·TIDELKC.OUT·TIDELKB.OUT을 APPEND로 열고 각 파일에 N을 기록한다(248–255). 이 구간에는 조건 분기나 계산 대입이 없다. 주석을 포함한다(256). |
| 257–286 | 시작 시 6행 CALHTA 루틴 안. L=2..LA 루프(257)에서 최상층 KC 조류 타원의 네 성분 `TERM1=AMCU(L,KC)+AMSV(L,KC)` (258); `TERM2=AMCV(L,KC)-AMSU(L,KC)` (259); `TERM3=AMCU(L,KC)-AMSV(L,KC)` (260); `TERM4=AMCV(L,KC)+AMSU(L,KC)` (261), 두 회전 성분 반경 `RPLUS=0.5*SQRT(TERM1*TERM1+TERM2*TERM2)` (262); `RMINS=0.5*SQRT(TERM3*TERM3+TERM4*TERM4)` (263). 264–265행의 직접 ATAN2는 주석이다. `IF(TERM1.EQ.0.0.AND.TERM2.EQ.0.0)THEN` (266)이면 `APLUS=999999.` (267), `ELSE` (268)이면 `APLUS=ATAN2(TERM2,TERM1)` (269). 독립 `IF(TERM3.EQ.0.0.AND.TERM4.EQ.0.0)THEN` (271)이면 `AMINS=999999.` (272), `ELSE` (273)이면 `AMINS=ATAN2(TERM4,TERM3)` (274). 장축·단축(minor axis)·방위각(orientation angle) 및 장축 벡터 `RRMAJ=RPLUS+RMINS` (276); `RRMIN=ABS(RPLUS-RMINS)` (277); `AACCWX=0.5*(APLUS+AMINS)` (278); `RMAJUKC=RRMAJ*COS(AACCWX)` (279); `RMAJVKC=RRMAJ*SIN(AACCWX)` (280). `IF(RMAJUKC.LT.0.0)THEN` (281)이면 `RMAJUKC=-RMAJUKC` (282); `RMAJVKC=-RMAJVKC` (283)로 벡터 부호를 바꾼다. 조류 위상 `PHASEKC=(0.25/PI)*TIDALP*(AMINS-APLUS)/3600.` (285). 단위 11에 격자 인덱스·경위도·방위각·장축·단축을 출력한다(286). L 루프는 다음 구간으로 이어진다. |
| 287–320 | 시작 시 6행 CALHTA 루틴·257행 L 루프 안. 최하층 1 조류 타원의 네 성분 `TERM1=AMCU(L,1)+AMSV(L,1)` (287); `TERM2=AMCV(L,1)-AMSU(L,1)` (288); `TERM3=AMCU(L,1)-AMSV(L,1)` (289); `TERM4=AMCV(L,1)+AMSU(L,1)` (290), 두 회전 성분 반경 `RPLUS=0.5*SQRT(TERM1*TERM1+TERM2*TERM2)` (291); `RMINS=0.5*SQRT(TERM3*TERM3+TERM4*TERM4)` (292). 293–294행 직접 ATAN2는 주석이다. `IF(TERM1.EQ.0.0.AND.TERM2.EQ.0.0)THEN` (295)이면 `APLUS=999999.` (296), `ELSE` (297)이면 `APLUS=ATAN2(TERM2,TERM1)` (298). 독립 `IF(TERM3.EQ.0.0.AND.TERM4.EQ.0.0)THEN` (300)이면 `AMINS=999999.` (301), `ELSE` (302)이면 `AMINS=ATAN2(TERM4,TERM3)` (303). 장축·단축·방위각·장축 벡터 `RRMAJ=RPLUS+RMINS` (305); `RRMIN=ABS(RPLUS-RMINS)` (306); `AACCWX=0.5*(APLUS+AMINS)` (307); `RMAJUKB=RRMAJ*COS(AACCWX)` (308); `RMAJVKB=RRMAJ*SIN(AACCWX)` (309). `IF(RMAJUKB.LT.0.0)THEN` (310)이면 `RMAJUKB=-RMAJUKB` (311); `RMAJVKB=-RMAJVKB` (312). 바닥 조류 위상 `PHASEKB=(0.25/PI)*TIDALP*(AMINS-APLUS)/3600.` (314). 단위 3은 최상층·최하층 장축 벡터, 단위 4는 두 위상, 단위 12는 바닥 방위각·장축·단축을 출력한다(315–318). L 루프 종료·주석(319–320). |
| 321–341 | 시작 시 6행 CALHTA 루틴 안. 단위 3·4·11·12 파일을 닫는다(321–324). 공통 종료 레이블 `2000 CONTINUE` (328)에서 `NHAR=NHAR+1` (330)로 NHAR를 증가시킨다. 출력 형식 `99 FORMAT(A80)` (334), `100 FORMAT(I10)` (335), `101 FORMAT(2I10)` (336), `200 FORMAT(2I5,1X,6E13.5)` (337), `250 FORMAT(12E12.4)` (338). 구분 주석 뒤 `RETURN` (340), `END` (341). 이 파일에 실행 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 233–240: 수면의 두 조화 계수가 모두 0이면 PHI=999999.로 설정한다. 다음 두 위상 변환은 이 PHI에도 적용한다. 이 센티널(sentinel)을 별도로 보존하는 출력 분기는 없다.
- 266–285·295–314: 각 회전 성분의 두 TERM이 0이면 APLUS 또는 AMINS를 999999.로 설정한다. 이후 방위각·COS·SIN·조류 위상 계산은 이 값에도 적용한다.
- 134–141·184–191·258–318: 수심 평균 속도의 조화 계수 AMCUE·AMSUE·AMCVE·AMSVE를 누적하고 변환한다. 이 파일의 조류 타원 출력 계산은 층별 AMCU·AMSU·AMCV·AMSV를 사용한다. 수심 평균 계수의 직접 출력문은 없다.
- 281–285·310–314: 장축 u 성분이 음수이면 u·v 장축 성분의 부호를 함께 바꾼다. PHASEKC·PHASEKB는 그 뒤 AMINS-APLUS 식으로 계산한다. 부호 전환 조건 안에는 위상 변경 대입이 없다.
- 91·105·112–113: 출력 헤더의 수면 표시 깊이는 0., 바닥 표시 깊이는 99.로 고정한다. 이 표시 깊이에 HP 또는 수직 격자 좌표를 대입하는 문장은 없다.
