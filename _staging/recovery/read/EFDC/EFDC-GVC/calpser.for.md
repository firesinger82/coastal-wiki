---
file: models/EFDC/raw/source_code/EFDC-GVC/calpser.for
lines: 67
sha256: 92e9cbf7e5f619c87a7469bef09047876f5843c750035a66d50cdd722c45cd7c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calpser.for — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 주석·구분선과 `SUBROUTINE CALPSER (ISTL)` 입구(6). EFDC-FULL 1.0a·2001-11-01 수정 표기(8–10). 시간 가변 수위(surface elevation) 경계조건 갱신 목적 주석(21–22). `EFDC.PAR`·`EFDC.CMN` 포함(26–27). |
| 31–52 | 시작 시 6행 CALPSER 루틴 안. PSERT/PSERST/PSERZDS/PSERZDF의 인덱스 0을 0으로 설정한다(31–34). NS=1..NPSER 루프(36) 안에서 ISDYNSTP=0이면 DT·N·TBEGIN·TCON·TCPSER로 TIME을 계산하고 ELSE이면 TIMESEC/TCPSER를 쓴다(38–42). 마지막 구간 인덱스 MPTLAST를 M1으로 가져온다(43). 100 표지(44)에서 M2=M1+1(45). TIME이 TPSER(M2,NS)보다 크면 M1=M2로 옮기고 100으로 반복하며, ELSE에서 MPTLAST를 저장한다(46–51). 조건·반복 범위·대입식·호출 원문: `PSERT(0)=0.` (31); `PSERST(0)=0.` (32); `PSERZDS(0)=0.` (33); `PSERZDF(0)=0.` (34); `DO NS=1,NPSER` (36); `IF(ISDYNSTP.EQ.0)THEN` (38); `TIME=DT*FLOAT(N)/TCPSER(NS)+TBEGIN*(TCON/TCPSER(NS))` (39); `ELSE` (40); `TIME=TIMESEC/TCPSER(NS)` (41); `M1=MPTLAST(NS)` (43); `M2=M1+1` (45); `IF(TIME.GT.TPSER(M2,NS))THEN` (46); `M1=M2` (47); `GOTO 100` (48); `ELSE` (49); `MPTLAST(NS)=M1` (50). |
| 53–67 | 시작 시 6행 CALPSER 루틴·36행 NS 루프 안. 두 표본 시간 차 TDIFF와 WTM1/WTM2를 구하고 PSER·PSERS를 각각 선형 보간(linear interpolation)해 PSERT·PSERST에 저장한다(53–57). WRITE(6,6000)은 주석이다(58). NS 루프 종료(60). 6000 출력 형식(62), 빈 줄·구분선·RETURN·END(61–67). 조건·반복 범위·대입식·호출 원문: `TDIFF=TPSER(M2,NS)-TPSER(M1,NS)` (53); `WTM1=(TPSER(M2,NS)-TIME)/TDIFF` (54); `WTM2=(TIME-TPSER(M1,NS))/TDIFF` (55); `PSERT(NS)=WTM1*PSER(M1,NS)+WTM2*PSER(M2,NS)` (56); `PSERST(NS)=WTM1*PSERS(M1,NS)+WTM2*PSERS(M2,NS)` (57); `6000 FORMAT('N, PSERT = ',I6,4X,F12.4)` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·31–60: 인수 ISTL은 이 파일의 실행문에서 참조되지 않는다.
- 43–51: 시간 검색은 MPTLAST에서 시작하여 M2=M1+1을 반복 증가시킨다. 이 검색 블록에는 시계열 상한 인덱스 검사나 TIME이 감소할 때 인덱스를 줄이는 문장이 없다.
- 39·41·53–55: TIME 계산은 TCPSER, 보간 가중치는 TDIFF로 나눈다. 이 블록에 두 분모의 0 여부를 검사하는 조건은 없다.
- 31–34·56–57: PSERZDS/PSERZDF 대입은 인덱스 0 초기화만 있다. NS=1..NPSER 보간 결과 대입은 PSERT/PSERST 두 배열에만 있다.
- 58·62: 6000 형식을 사용하는 WRITE 문은 주석 처리되어 있다.

