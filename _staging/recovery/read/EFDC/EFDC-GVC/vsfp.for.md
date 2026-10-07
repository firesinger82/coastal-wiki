---
file: models/EFDC/raw/source_code/EFDC-GVC/vsfp.for
lines: 282
sha256: c048ba2437ad66cbd0a1d28ef98ea51a3ca02315dd50b130c14a776a4849904a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# vsfp.for — 판독 구간 기록

구간은 1행부터 282행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 머리말과 `SUBROUTINE VSFP` 입구(1–6). EFDC-FULL 1.0a·수정 이력(8–17). 지정된 수평 위치·시각에서 순간 수직 스칼라장(vertical scalar field) 프로파일(profile)을 VSFP.OUT에 쓴다는 주석(19–21). `INCLUDE 'EFDC.PAR'` (25), `INCLUDE 'EFDC.CMN'` (26). 염분(salinity)·온도(temperature)·염료(dye)·SFL·독성물질(toxicant)·퇴적물(sediment)·모래(sand)의 층별 작업 배열과 지정 깊이 출력 배열, 수면 아래 깊이(depth below surface) DBLWSF·바닥 위 높이(height above bottom) DABVBT 선언(28–34). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 38–52 | 시작 시 6행 VSFP 안. `IF(JSVSFP.EQ.0) GOTO 100` (38)은 초기 파일 삭제를 건너뛴다. VSFP1.OUT를 열어 DELETE로 닫고 다시 연 뒤 닫는다(39–44). 헤더 WRITE는 주석(42–43). VSFP2.OUT는 열어 DELETE로 닫는다(45–46). JSVSFP=0(47), 구분 주석과 이동 대상 `100 CONTINUE` (51). |
| 53–89 | 시작 시 6행 VSFP 안. ML=1..MLVSFP 루프(53), `IF(NTVSFP(ML).EQ.N)THEN` (54). MDMAX=1 초기화(55), I/J/L 조회(56–58). `DABVBT(1)=0.5*HP(L)*DZC(1)` (59), K=2..KC(60)에서 `DABVBT(K)=DABVBT(K-1)+0.5*HP(L)*(DZC(K)+DZC(K-1))` (61). K=1..KC(63)에서 `DBLWSF(K)=HP(L)-DABVBT(K)` (64). SAL/TEM/DYE/SFL 각 층 복사(66–71). NT=1..NTOX·K=1..KC에서 TOX 복사(72–76), NS=1..NSED·K=1..KC에서 SED 복사(77–81), NX=1..NSND·K=1..KC에서 SND 복사(82–86). MD=1..MDVSFP 루프(87) 안 `IF(DMVSFP(MD).LT.HP(L)) MDMAX=MD` (88). |
| 90–109 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 일치 분기 안. MD=1..MDMAX 루프(90), `ZZSVSFP=(HP(L)-DMVSFP(MD))*HPI(L)` (91). `IF(ZZSVSFP.GE.0.0.AND.ZZSVSFP.LE.1.0)THEN` (92) 안 `IF(ZZSVSFP.GE.ZZ(KC))THEN` (93)은 상부 두 층으로 선형 보간(linear interpolation)/외삽(extrapolation)한다. `SOUTMPU= (ZZSVSFP-ZZ(KS))/(ZZ(KC)-ZZ(KS))` (94), `SOUTMPB=-(ZZSVSFP-ZZ(KC))/(ZZ(KC)-ZZ(KS))` (95). `SALOT(MD)=SOUTMPU*SALVS(KC)+SOUTMPB*SALVS(KS)` (96), `TEMOT(MD)=SOUTMPU*TEMVS(KC)+SOUTMPB*TEMVS(KS)` (97), `DYEOT(MD)=SOUTMPU*DYEVS(KC)+SOUTMPB*DYEVS(KS)` (98), `SFLOT(MD)=SOUTMPU*SFLVS(KC)+SOUTMPB*SFLVS(KS)` (99). NT/NS/NX 종류 루프(100·103·106)의 식은 `TOXOT(MD,NT)=SOUTMPU*TOXVS(KC,NT)+SOUTMPB*TOXVS(KS,NT)` (101), `SEDOT(MD,NS)=SOUTMPU*SEDVS(KC,NS)+SOUTMPB*SEDVS(KS,NS)` (104), `SNDOT(MD,NX)=SOUTMPU*SNDVS(KC,NX)+SOUTMPB*SNDVS(KS,NX)` (107). `ELSE` (109)는 상부 조건 불성립 경로를 연다. |
| 110–126 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 분기·90행 MD 루프·92행 좌표 범위 분기·109행 상부 조건 ELSE 안. `IF(ZZSVSFP.LE.ZZ(1))THEN` (110)은 하부 두 층으로 보간/외삽한다. `SOUTMPU= (ZZSVSFP-ZZ(1))/(ZZ(2)-ZZ(1))` (111), `SOUTMPB=-(ZZSVSFP-ZZ(2))/(ZZ(2)-ZZ(1))` (112), `SALOT(MD)=SOUTMPU*SALVS(2)+SOUTMPB*SALVS(1)` (113), `TEMOT(MD)=SOUTMPU*TEMVS(2)+SOUTMPB*TEMVS(1)` (114), `DYEOT(MD)=SOUTMPU*DYEVS(2)+SOUTMPB*DYEVS(1)` (115), `SFLOT(MD)=SOUTMPU*SFLVS(2)+SOUTMPB*SFLVS(1)` (116). NT/NS/NX 루프(117·120·123)의 식은 `TOXOT(MD,NT)=SOUTMPU*TOXVS(2,NT)+SOUTMPB*TOXVS(1,NT)` (118), `SEDOT(MD,NS)=SOUTMPU*SEDVS(2,NS)+SOUTMPB*SEDVS(1,NS)` (121), `SNDOT(MD,NX)=SOUTMPU*SNDVS(2,NX)+SOUTMPB*SNDVS(1,NX)` (124). `ELSE` (126)는 내부 층 검색 경로를 연다. |
| 127–152 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 분기·90행 MD 루프·92행 범위 분기·109/126행 두 ELSE 안. K=1(127), 이동 대상 200의 `K=K+1` (128). `IF(ZZSVSFP.GT.ZZ(K-1).AND.ZZSVSFP.LE.ZZ(K))THEN` (129)이면 `SOUTMPU= (ZZSVSFP-ZZ(K-1))/(ZZ(K)-ZZ(K-1))` (130), `SOUTMPB=-(ZZSVSFP-ZZ(K))/(ZZ(K)-ZZ(K-1))` (131), `SALOT(MD)=SOUTMPU*SALVS(K)+SOUTMPB*SALVS(K-1)` (132), `TEMOT(MD)=SOUTMPU*TEMVS(K)+SOUTMPB*TEMVS(K-1)` (133), `DYEOT(MD)=SOUTMPU*DYEVS(K)+SOUTMPB*DYEVS(K-1)` (134), `SFLOT(MD)=SOUTMPU*SFLVS(K)+SOUTMPB*SFLVS(K-1)` (135). NT/NS/NX 루프(136·139·142)의 식은 `TOXOT(MD,NT)=SOUTMPU*TOXVS(K,NT)+SOUTMPB*TOXVS(K-1,NT)` (137), `SEDOT(MD,NS)=SOUTMPU*SEDVS(K,NS)+SOUTMPB*SEDVS(K-1,NS)` (140), `SNDOT(MD,NX)=SOUTMPU*SNDVS(K,NX)+SOUTMPB*SNDVS(K-1,NX)` (143). `ELSE` (145)는 `GOTO 200` (146)으로 K 검색을 반복한다. 내부 검색·하부·상부·좌표 범위 조건 및 MD 루프 종료(147–151), 주석(152). |
| 153–173 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 분기 안. VSFP1.OUT를 APPEND로 연다(153). TIMVSFP/NTVSFP/I/J/HP 헤더와 SAL/TEM/DYE/SFL 열 제목(154–155), MD=1..MDMAX의 DMVSFP와 보간 값 4개(156–158), 빈 행(159). 두 번째 헤더와 퇴적물/모래 열 제목(160–161), MD 루프에서 SEDOT 전 종류 및 SNDOT 전 종류 출력(162–165), 빈 행(166). `NTXX=MIN(NTOX,6)` (167), 헤더·TOX 1..6 제목(168–169), MD 루프에서 TOXOT의 NT=1..NTXX 출력(170–172), 빈 행(173). |
| 174–202 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 분기 안. `IF(NTOX.GT.6)THEN` (174)은 `NTXX=MIN(NTOX,12)` (175), 헤더·7..12 제목·MD=1..MDMAX의 NT=7..NTXX 출력(176–181). 독립 `IF(NTOX.GT.12)THEN` (183)은 `NTXX=MIN(NTOX,18)` (184), 헤더·13..18 제목·NT=13..NTXX 출력(185–190). `IF(NTOX.GT.18)THEN` (192)은 `NTXX=MIN(NTOX,24)` (193), 헤더·19..24 제목·NT=19..NTXX 출력(194–199). 각 조건 종료(182·191·200), CLOSE(201), 주석(202). |
| 203–224 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 분기 안. VSFP2.OUT를 APPEND로 열고 시각·위치·수심 및 층별 열 제목 출력(203–205). `DO K=KC,1,-1` (206)은 K/DBLWSF/DABVBT와 SALVS/TEMVS/DYEVS/SFLVS 출력(207–208). 빈 행·두 번째 헤더·퇴적물/모래 제목(210–212), 같은 역순 K 루프(213)에서 SEDVS/SNDVS 전 종류 출력(214–215). `NTXX=MIN(NTOX,6)` (218), 헤더와 TOX 1..6 제목(219–220), 역순 K 루프(221)에서 NT=1..NTXX의 TOXVS 출력(222). |
| 225–255 | 시작 시 6행 VSFP·53행 ML 루프·54행 시각 분기 안. `IF(NTOX.GT.6)THEN` (225)은 `NTXX=MIN(NTOX,12)` (226), 헤더·7..12 제목·K=KC..1 역순의 TOXVS NT=7..NTXX 출력(227–232). `IF(NTOX.GT.12)THEN` (234)은 `NTXX=MIN(NTOX,18)` (235), 헤더·13..18 제목·NT=13..NTXX 출력(236–241). `IF(NTOX.GT.18)THEN` (243)은 `NTXX=MIN(NTOX,24)` (244), 헤더·19..24 제목·NT=19..NTXX 출력(245–250). 각 조건 종료(233·242·251), CLOSE(252), 시각 조건·ML 루프 종료(254–255). |
| 256–282 | 시작 시 6행 VSFP 안. 구분 주석(256–258). 프로파일·빈 행·시각/위치/수심·깊이별/층별 열 제목 FORMAT 정의(259–275). 값 FORMAT은 `105 FORMAT(1X,F8.2,4X,6F11.4)` (276), `106 FORMAT(1X,I2,2X,2F8.2,2X,6F11.4)` (277). 구분 주석·RETURN·END(278–282). 이 루틴에는 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–21·39–46·153·203: 머리말의 파일명은 VSFP.OUT이다. 실행 OPEN 파일명은 VSFP1.OUT와 VSFP2.OUT이다.
- 55·87–92·156–157: MDMAX는 1에서 시작하며 조건을 만족한 마지막 MD를 저장한다. 지정 깊이 순서 검사와 MDMAX=0 경로는 이 파일에 없다. 출력은 MD=1..MDMAX 전체를 사용한다.
- 92–151·153–157: 보간 대입은 ZZSVSFP가 0..1일 때만 있다. 범위 밖 ELSE 대입은 없다. 출력은 좌표 범위 조건 밖에서 SALOT/TEMOT/DYEOT/SFLOT 등을 읽는다.
- 93–112: 상부 식은 KC/KS, 하부 식은 2/1 인덱스를 사용한다. 이 블록에는 KC=1 별도 경로가 없다.
- 127–146: 내부 층 검색은 K를 증가시키며 GOTO 200을 반복한다. 이 검색에는 별도의 K<=KC 종료 조건이 없다.
- 72–76·167–200·218–251: TOX 작업 배열 복사는 NT=1..NTOX이다. 두 출력 파일의 독성물질 값 블록은 NT=24까지 있다. NT>=25 출력 블록은 없다.
- 162–164·214–215·276–277: 퇴적물·모래 WRITE 목록은 NSED와 NSND 전 종류를 포함한다. 값 FORMAT의 농도 서식은 6F11.4로 고정되어 있다.
