---
file: models/EFDC/raw/source_code/EFDC-GVC/lvelplth.for
lines: 221
sha256: 9fedeaa8b7d21e0ff35853855c988646b908589238947308c66454dd4fae21d9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# lvelplth.for — 판독 구간 기록

구간은 1행부터 221행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 구분 주석과 `SUBROUTINE LVELPLTH` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 주석(7–18). 수평 라그랑주 평균 속도(Lagrangian mean velocity) 벡터와 평균 속도 파일을 쓴다는 주석(19–21). `INCLUDE 'EFDC.PAR'`·`INCLUDE 'EFDC.CMN'` (25–26). DBS(10)과 길이 80 제목 두 개를 선언한다(30–31). 포함 파일 내부는 이 판독에 포함하지 않았다. |
| 35–63 | 시작 시 6행 LVELPLTH 안. 출력점 NLR=1..NLRPD를 순회하여 I/J와 L을 찾는다(39–42). `IF(ISRED(L).EQ.1)NRLRPD=NRLRPD+1` (43), `IF(ISRED(L).EQ.0)NBLRPD=NBLRPD+1` (44)로 두 집합의 점 수를 센다. 제목을 설정한다(47–48). `IF(IPLRPD.EQ.1) LINES=NLRPD` (49), `IF(IPLRPD.EQ.2) LINES=NRLRPD` (50), `IF(IPLRPD.EQ.3) LINES=NBLRPD` (51) 뒤 무조건 LINES=NLRPD를 대입한다(52). 헤더 값은 `LEVELS=2` (53), `DBS(1)=0.` (54), `DBS(2)=99.` (55). LMVVECH.OUT을 열어 삭제하고 다시 연다(57–59). 제목·LINES/LEVELS·DBS를 쓴다(60–62). |
| 64–84 | 시작 시 6행 LVELPLTH 안. `IF(IPLRPD.EQ.1)THEN` (64)에서 M=1..MLRPDRT·NLR=1..NLRPD를 순회한다(65·67). M별 NLRPDRT를 쓰고 I/J/L을 찾는다(66·68–70). 최상층 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,KC,M)` (71), `VTMP=100.*STCUV(L)*YLRPD(NLR,KC,M)` (72), `VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (73), `VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (74). 최하층 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,1,M)` (75), `VTMP=100.*STCUV(L)*YLRPD(NLR,1,M)` (76), `VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (77), `VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (78). 격자 인덱스·경위도·두 층의 동/북 성분을 쓰고 루프와 조건을 닫는다(79–83). |
| 85–107 | 시작 시 6행 LVELPLTH 안. `IF(IPLRPD.EQ.2)THEN` (85)에서 M·NLR 루프를 연다(86·88). `IF(ISRED(L).EQ.1)THEN` (92)인 점만 출력한다. 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,KC,M)` (93), `VTMP=100.*STCUV(L)*YLRPD(NLR,KC,M)` (94), `VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (95), `VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (96), `UTMP=100.*STCUV(L)*XLRPD(NLR,1,M)` (97), `VTMP=100.*STCUV(L)*YLRPD(NLR,1,M)` (98), `VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (99), `VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (100). 각 기록의 열은 앞 분기와 같다(101–102). 조건과 루프 종료·주석도 포함한다(103–107). |
| 108–134 | 시작 시 6행 LVELPLTH 안. `IF(IPLRPD.EQ.3)THEN` (108)의 M·NLR 루프(109·111)에서 `IF(ISRED(L).EQ.0)THEN` (115)인 점만 출력한다. 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,KC,M)` (116), `VTMP=100.*STCUV(L)*YLRPD(NLR,KC,M)` (117), `VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (118), `VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (119), `UTMP=100.*STCUV(L)*XLRPD(NLR,1,M)` (120), `VTMP=100.*STCUV(L)*YLRPD(NLR,1,M)` (121), `VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (122), `VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (123). 기록을 쓰고 조건·루프를 닫는다(124–129). LMVVECH.OUT을 닫고 구분 주석으로 끝난다(131–134). |
| 135–161 | 시작 시 6행 LVELPLTH 안. ALMVVCH.OUT을 열어 삭제하고 다시 연 뒤 제목·LINES/LEVELS·DBS 헤더를 쓴다(135–140). `IF(IPLRPD.EQ.1)THEN` (142)에서 M=MLRAVG로 정하고 NTS를 쓴다(143–144). NLR 루프(145)의 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,KC,M)` (149), `VTMP=100.*STCUV(L)*YLRPD(NLR,KC,M)` (150), `VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (151), `VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (152), `UTMP=100.*STCUV(L)*XLRPD(NLR,1,M)` (153), `VTMP=100.*STCUV(L)*YLRPD(NLR,1,M)` (154), `VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (155), `VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (156). 점별 기록을 쓰고 루프와 조건을 닫는다(157–160). |
| 162–183 | 시작 시 6행 LVELPLTH 안. `IF(IPLRPD.EQ.2)THEN` (162)에서 M=MLRAVG·NTS 기록·NLR 루프를 설정한다(163–165). `IF(ISRED(L).EQ.1)THEN` (169) 안의 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,KC,M)` (170), `VTMP=100.*STCUV(L)*YLRPD(NLR,KC,M)` (171), `VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (172), `VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (173), `UTMP=100.*STCUV(L)*XLRPD(NLR,1,M)` (174), `VTMP=100.*STCUV(L)*YLRPD(NLR,1,M)` (175), `VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (176), `VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (177). 기록 후 조건과 루프를 닫는다(178–182). |
| 184–207 | 시작 시 6행 LVELPLTH 안. `IF(IPLRPD.EQ.3)THEN` (184)에서 M=MLRAVG·NTS 기록·NLR 루프를 설정한다(185–187). `IF(ISRED(L).EQ.0)THEN` (191) 안의 식은 `UTMP=100.*STCUV(L)*XLRPD(NLR,KC,M)` (192), `VTMP=100.*STCUV(L)*YLRPD(NLR,KC,M)` (193), `VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (194), `VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (195), `UTMP=100.*STCUV(L)*XLRPD(NLR,1,M)` (196), `VTMP=100.*STCUV(L)*YLRPD(NLR,1,M)` (197), `VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (198), `VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (199). 기록 후 조건과 루프를 닫는다(200–204). ALMVVCH.OUT을 닫는다(206). |
| 208–221 | 시작 시 6행 LVELPLTH 안. 제목 A80, 단계 I10, 헤더 2I10, 점별 2I5·6E14.6, 층 값 12E12.4의 FORMAT을 정의한다(210–214). CMRM 대체 FORMAT 두 줄은 주석이다(215–216). 구분 주석·RETURN·END로 끝난다(217–221). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49–52·92·115·169·191: IPLRPD별 LINES 대입 뒤 무조건 LINES=NLRPD를 실행한다. IPLRPD=2·3의 데이터 기록은 각각 ISRED=1·0인 점으로 제한한다.
- 53–55·71–78: 출력 층 수는 2로 고정한다. 층 헤더 값은 0·99이며 실제 배열 참조의 층은 KC·1이다.
- 143·149–156·163·170–177·185·192–199: 평균 파일의 M은 MLRAVG이다. 이 루틴은 해당 M의 배열값을 읽으며 평균을 누적하거나 나누는 문장은 없다.
