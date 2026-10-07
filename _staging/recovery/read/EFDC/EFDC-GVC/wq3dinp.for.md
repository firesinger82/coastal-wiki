---
file: models/EFDC/raw/source_code/EFDC-GVC/wq3dinp.for
lines: 266
sha256: 0bf709949e5ade555b05573b82cfbbeebc4a42779d09a965e4a14a9c92e1e298
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wq3dinp.for — 판독 구간 기록

구간은 1행부터 266행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | 주석·구분선(1–5), `SUBROUTINE WQ3DINP` (6). 수질 하위 모델(submodel) 입력 목적·작성자·수정 이력·버전 주석(7–30). EFDC.PAR·EFDC.CMN 포함(31–32). 길이 3의 CWQHDR(NWQVM)·길이 11의 HHMMSS 선언(34·36). `DATA IWQTICI,IWQTAGR,IWQTSTL,IWQTSUN,IWQTBEN,IWQTPSL,IWQTNPL/7*0/` (38), `DATA ISMTICI/0/` (39). 이 8개 변수는 자기 자신을 대입한다(40–47), 주석(33·35·37·48). |
| 49–81 | 시작 시 6행 루틴 안. WQWCTS.OUT 삭제는 주석이다(49–50). WQ3D.OUT를 열어 삭제한다(52–53). 계수 지도 우회 설정 ISWQCMAP=0·ISWQSMAP=0은 주석이다(55–58). NWQKCNT=0(60), `NWQKDPT=1` (61). UHEQ(1)·UHEQ(LC)=0(63–64). 65행 ND=1..NDMWQ에서 `LF=2+(ND-1)*LDMWQ` (66), `LL=LF+LDM-1` (67). 68행 L=LF..LL에서 UHEQ=1(69). TINDAY=0·자기 대입, ITNWQ=0(73–75). `RKCWQ = 1.0/REAL(KC)` (77). 78행 K=1..KC에서 `WQHT(K)=REAL(KC-K)*RKCWQ` (79). 루프 종료·주석(80–81). |
| 82–138 | 시작 시 6행 루틴 안. 입력·출력 장치 번호 21..31 지정은 주석이다(82–91). 이전 WQTSNAME(1..21) 목록은 주석이다(93–113). 활성 고정 문자열은 인덱스 순서대로 CHC, CHG, CHD, ROC, LOC, DOC, ROP, LOP, DOP, P04, RON, LON, DON, NHX, NOX, SUU, SAA, COD, DOX, TAM, FCB이다(115–135). 대형조류(macroalgae) MAC를 WQTSNAME(22)에 지정한다(136–138). |
| 139–175 | 시작 시 6행 루틴 안. 140행 M=0..NWQPS에서 WQPSQ·WQPSQC=0(141–142), 143행 J=1..NWQV에서 WQWPSLC=0(144). 148행 K=1..KC에서 1·LC 경계 셀의 IWQPSC·WQDSQ=0(149–152). 155행 ND 루프의 `LF=2+(ND-1)*LDMWQ` (156), `LL=LF+LDM-1` (157). 158행 K·159행 L=LF..LL에서 IWQPSC·IWQPSV·WQDSQ=0(160–162). 167행 J·168행 K·169행 L=1..LC에서 WQWDSL·WQWPSL=0(170–171). 루프·주석(172–175). 점오염원 부하(point source loading) 관련 배열을 초기화하는 구간이다. |
| 176–213 | 시작 시 6행 루틴 안. `CALL RWQC1(IWQDT)` (176). RWQC2·RWQMAP 호출은 주석이다(177–178). WQWCTS.OUT 삭제·재열기(181–183). NWQVOUT=0(185). 186행 NW=1..NWQV에서 `IF(ISTRWQ(NW).EQ.1)THEN` (187) 참이면 `NWQVOUT=NWQVOUT+1` (188), CWQHDR에 선택한 WQTSNAME 복사(189). 대형조류 출력 추가 주석(193–194), `NWQVOUT=NWQVOUT+1` (195), `CWQHDR(NWQVOUT)=WQTSNAME(NWQV+1)` (196). 출력 머리말 WRITE는 NW=1..NWQVOUT(198). FORMAT 1969는 셀 I,J,K·TIME 고정 머리말과 A3 문자열 슬롯을 정의한다(200–203). 이전 고정 머리말은 주석이다(205–210). 파일 close·주석(212–213). |
| 214–226 | 시작 시 6행 루틴 안. 일주기(diurnal) 용존산소(dissolved oxygen, DO) 분석 초기화 주석(214–215). `IF(NDDOAVG.GE.1)THEN` (216) 참이면 DIURNDO.OUT를 열어 삭제한다(217–218). 219행 K=1..KC·220행 L=2..LA에서 `DDOMAX(L,K)=-1.E6` (221), `DDOMIN(L,K)=1.E6` (222). 두 루프·조건 종료·주석(223–226). |
| 227–240 | 시작 시 6행 루틴 안. 광 소멸(light extinction) 분석 초기화 주석(227–228). `IF(NDLTAVG.GE.1)THEN` (229) 참이면 LIGHT.OUT를 열어 삭제한다(230–231), NDLTCNT=0(232). 233행 K=1..KC·234행 L=2..LA에서 RLIGHTT·RLIGHTC=0(235–236). 두 루프·조건 종료·주석(237–240). |
| 241–254 | 시작 시 6행 루틴 안. 수질 평균 합산 배열 초기화 주석(241–242), `CALL WQZERO` (243). `IF(IWQICI.EQ.2) CALL RWQRST` (245)이면 RWQRST로 재시작(restart)을 읽는다. `IF(IWQBEN.EQ.1)THEN` (247) 안 `CALL SMINIT` (248), `CALL SMRIN1(IWQDT)` (249). SMRIN2·RSMMAP 호출은 주석이다(250–251). 같은 저서 모델 분기 안 `IF(ISMICI.EQ.2) CALL RSMRST` (252)이면 RSMRST를 호출한다. 조건 종료·주석(253–254). |
| 255–266 | 시작 시 6행 루틴 안. TFILE 시각 로그 open·TIME 호출·삭제·재열기·WRITE·close는 전체 주석이다(255–260). FORMAT 100은 시각 문자열 HH.MM.SS.HH(262). 대체 HH:MM:SS.SS 형식은 주석이다(263). RETURN·END 및 사이 주석(261·264–266). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–47: DATA로 0을 지정한 8개 일정 변수는 자기 대입만 한다. 이 파일의 나머지 활성 실행문에는 이 8개 변수 참조가 없다.
- 65–69·155–162: LF 계산은 LDMWQ를 사용한다. 같은 블록의 LL 계산은 LF+LDM-1이다.
- 115–137·185–198: WQTSNAME은 22개 고정 이름을 설정한다. 출력 머리말의 대형조류 추가는 조건 없이 NWQVOUT을 1 증가시키고 WQTSNAME(NWQV+1)을 복사한다.
- 34·186–196: CWQHDR 크기는 NWQVM이다. 선택 출력과 대형조류 추가 뒤 NWQVOUT<=NWQVM을 검사하는 문장은 이 블록에 없다.
- 148–153·155–165: 1·LC 경계 셀 초기화는 IWQPSC와 WQDSQ를 설정한다. 이 명시적 경계 블록은 IWQPSV를 설정하지 않는다. IWQPSV 설정은 뒤의 LF..LL 루프에 있다.
- 36·255–260: HHMMSS 선언은 활성 상태이다. HHMMSS를 사용하는 TIME 호출과 WRITE는 주석이다.
