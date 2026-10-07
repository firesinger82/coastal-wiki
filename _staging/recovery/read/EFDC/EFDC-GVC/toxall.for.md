---
file: models/EFDC/raw/source_code/EFDC-GVC/toxall.for
lines: 240
sha256: c368f3c5d87ac29e5c65c50fce04e82ebb11c8f437f5734c52db19ac55c802b3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# toxall.for — 판독 구간 기록

구간은 1행부터 240행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–71 | 머리말과 `SUBROUTINE TOXALL` 입구(1–6).누적 독성물질(toxicant) 플럭스(flux)를 쓴다는 주석(8).EFDC-FULL 1.0a·수정 이력(10–12).변수 설명은 수층(water column) 입자상(particulate)·자유 용존(free dissolved)·복합 용존(complexed dissolved) 이류(advection), 소류사(bed load), 유입·유출·휘발(volatilization), 퇴적층(sediment bed)과 수층 사이 교환, 제방 침식(bank erosion)을 나눈다(16–34).교환 순량·양의 방향·음의 방향 및 공극수(pore water) 이류·확산(diffusion) 플럭스 설명(36–61).입자상 NS 범위 주석은 1..NSED+NSND+2이다(18–19·29·38·44).`INCLUDE 'EFDC.PAR'` (65), `INCLUDE 'EFDC.CMN'` (66), 길이 18의 FNTMP(7) 선언(68).포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 72–112 | 시작 시 6행 TOXALL 안. 디버깅(debugging)용 파일명 7개를 FNTMP에 대입(72–78). `IF(JSTOXALL.EQ.0)THEN` (82)은 TOXALL.OUT/TOXALLBW.OUT/TOXALLB2W.OUT/TOXALLW2B.OUT/TOXALLBWAD.OUT/TOXALLB2WAD.OUT/TOXALLW2BAD.OUT/SEDALL.OUT를 단위 1/2/3/4/11/12/13/14로 열어 DELETE로 닫는다(83–98). 단위 21..27 디버깅 파일 삭제 루프는 주석(100–106). JSTOXALL=1 설정과 조건 종료(108–109), 구분 주석(110–112). |
| 113–151 | 시작 시 6행 TOXALL 안. 위 8개 파일을 POSITION='APPEND'로 연다(113–120). 디버깅 파일 OPEN은 주석(122–127). `IF(ISDYNSTP.EQ.0)THEN` (129)은 `TIME=(DT*FLOAT(N)+TCON*TBEGIN)/86400.` (130). `ELSE` (131)는 `TIME=TIMESEC/86400.` (132). 8개 파일에 TIME을 쓴다(135–142). 디버깅 시간 출력은 주석(144–146). 주석의 NTMP=NSED+NSND+2(148) 대신 실행식 `NTMP=NSED+NSND` (149). `NT=1` (151)로 독성물질 번호를 고정한다. |
| 152–181 | 시작 시 6행 TOXALL 안. `DO L=2,LA` (152)에서 모든 출력에 IL/JL을 붙인다. TOXALL.OUT에는 NS=1..NTMP의 수층 입자상 x/y 플럭스, 자유·복합 용존 x/y 플럭스, NS=1..NSND의 소류사 x/y 플럭스, ATOXSOUR/ATOXSINK/ATOXVOL, 입자상·자유·복합 용존 퇴적층 교환 및 제방 침식 세 플럭스를 쓴다(153–161). TOXALLBW에는 교환 순량(163–164), TOXALLB2W에는 양의 교환 배열(166–167), TOXALLW2B에는 음의 교환 배열(169–170)을 쓴다. 단위 11/12/13에는 공극수 교환 순량/양의 방향/음의 방향 용존 두 배열을 쓴다(172–176). SEDALL에는 NS=1..NTMP의 ASEDFWX/Y와 NS=1..NSND의 ASEDFBLX/Y를 쓴다(178–180). |
| 182–217 | 시작 시 6행 TOXALL·152행 L 루프 안. TOXALL_PFWCADV/FDWCADV/PFBEDLD/SORSINK/PFBD2WC/FDBD2WC/BANKERO별 분리 출력 주석(182–215). 해당 WRITE 및 이어지는 출력 목록은 전부 주석 처리되어 있다. L 루프 종료(217). |
| 218–240 | 시작 시 6행 TOXALL 안. 8개 단위 CLOSE(219–226). 디버깅 파일 CLOSE 루프는 주석(228–232). `100 FORMAT(F10.3)` (234), `101 FORMAT(2I6,64E14.6)` (235). 구분 주석·빈 줄·RETURN·END(236–240). 이 루틴에는 CALL 문과 누적 배열 초기화문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–19·29·38·44·148–154: 입자상 NS 범위 주석은 NSED+NSND+2까지이다. 실행 NTMP는 NSED+NSND이다. +2를 포함하는 NTMP 대입은 주석이다.
- 151–180: 출력 독성물질 번호는 NT=1이다. 이 루틴에는 NT=1..NTOX 루프가 없다.
- 55–61·174–176: 양의 공극수 복합 용존 변수 설명에는 ATOXCDFBWADN을 적는다. 음의 공극수 변수 설명에는 P 접미사를 적는다. 실행 출력은 양의 방향에 P, 음의 방향에 N 접미사를 사용한다.
- 68·72–78·102–106·124–127·184–215·230–232: FNTMP에는 파일명을 대입한다. FNTMP를 사용하는 OPEN 및 별도 디버깅 출력·삭제·CLOSE는 주석이다.
