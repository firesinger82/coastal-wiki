---
file: models/EFDC/raw/source_code/EFDC-GVC/tmsrbin.for
lines: 103
sha256: b9019bad27c13921421b6ea8d411debd1b16cb4d815404bc0c72ac2ad6b64b8c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# tmsrbin.for — 판독 구간 기록

구간은 1행부터 103행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 머리말과 `SUBROUTINE TMSRBIN` 입구(1–6). EFDC-FULL 1.0a·수정 이력 주석(10–21). 이진(binary) 유동 배열을 0으로 초기화한다는 주석(25–26). `INCLUDE 'EFDC.PAR'` (30), `INCLUDE 'EFDC.CMN'` (31). 최근 값을 누적 배열에 더한다는 주석(33). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 35–57 | 시작 시 6행 TMSRBIN 안. `DO LL=2,LA` (35)에서 `PPTMP = GI*P(LL)` (36), `HHTMP = PPTMP - BELV(LL)` (37), `SELSUM(LL) = SELSUM(LL) + PPTMP` (38), `DEPSUM(LL) = DEPSUM(LL) + HHTMP` (39)로 수위(surface elevation)와 수심(depth)을 누적한다. LN=LNC 복사(40). `UTMP1 = 50.*(UHDYE(LL+1) + UHDYE(LL))/(DYP(LL)*HP(LL))` (41), `VTMP1 = 50.*(VHDXE(LN)   + VHDXE(LL))/(DXP(LL)*HP(LL))` (42). `IF(SPB(LL) .EQ. 0)THEN` (43)은 `UTMP1 = 2.*UTMP1` (44), `VTMP1 = 2.*VTMP1` (45). `UTMP = CUE(LL)*UTMP1 + CVE(LL)*VTMP1` (47), `VTMP = CUN(LL)*UTMP1 + CVN(LL)*VTMP1` (48), `VXXSUM(LL) = VXXSUM(LL) + UTMP` (49), `VYYSUM(LL) = VYYSUM(LL) + VTMP` (50)로 동·북 방향 유속(velocity)을 누적한다. 옛 유량 누적식은 주석(51–52). 실행식은 `UTMP = MAX( UHDYE(LL), UHDYE(LL+1) )` (53), `VTMP = MAX( VHDXE(LL), VHDXE(LN) )` (54), `QXXSUM(LL) = QXXSUM(LL) + UTMP` (55), `QYYSUM(LL) = QYYSUM(LL) + VTMP` (56). 루프 종료(57). |
| 58–68 | 시작 시 6행 TMSRBIN 안. `IF(ISDYNSTP.EQ.0)THEN` (58)은 `TIMTMP=DT*FLOAT(N)+TCON*TBEGIN` (59), `TIMTMP=TIMTMP/TCTMSR` (60). `ELSE` (61)는 `TIMTMP=TIMESEC/TCTMSR` (62). 조건 종료 뒤 `TIMEHYD = TIMEHYD + TIMTMP` (64), `NHYCNT = NHYCNT + 1` (65). 이진 파일 출력 시점 검사 주석(67–68). |
| 69–83 | 시작 시 6행 TMSRBIN 안. `IF(N .GE. NBTMSR .AND. N .LE. NSTMSR)THEN` (69), `IF(NCTMSR .EQ. NWTMSR)THEN` (70)이 모두 참이면 `NREC0 = NREC0+1` (71), `TIMTMP = TIMEHYD / NHYCNT` (72). HYDTS.BIN을 단위 2, ACCESS='DIRECT', FORM='UNFORMATTED', STATUS='UNKNOWN', RECL=MAXRECL0으로 연다(73–74). REC=1에서 NDUM·XDUM 두 번·XDT·IXDT·NPARM·NCELLS·NLAYERS를 읽는다(76–77). NDUM/XDUM 자기 대입(78–79). REC=1에 NREC0·TBEGIN·TIMTMP와 나머지 헤더를 쓰고(80–81), REC=NR0에 평균 시간을 쓴다(83). |
| 84–103 | 시작 시 6행 TMSRBIN·69행 N 범위 분기·70행 출력 주기 분기 안. LL=2..LA 루프(84)에서 `SELSUM(LL) = SELSUM(LL)  / FLOAT(NHYCNT)` (85), `DEPSUM(LL) = DEPSUM(LL)  / FLOAT(NHYCNT)` (86), `VXXSUM(LL) = VXXSUM(LL)  / FLOAT(NHYCNT)` (87), `VYYSUM(LL) = VYYSUM(LL)  / FLOAT(NHYCNT)` (88), `QXXSUM(LL) = QXXSUM(LL)  / FLOAT(NHYCNT)` (89), `QYYSUM(LL) = QYYSUM(LL)  / FLOAT(NHYCNT)` (90). `WRITE(2) SELSUM(LL), DEPSUM(LL), VXXSUM(LL), VYYSUM(LL),` (92); `*        QXXSUM(LL), QYYSUM(LL), BELV(LL), ZBR(LL)` (93)로 셀별 평균과 바닥 값을 쓴다. 루프 종료(94), `INQUIRE(UNIT=2, NEXTREC=NR0)` (95), CLOSE(96), `CALL HYDZERO` (98). 두 조건 종료·주석·RETURN·END(99–103). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–26·35–65·98: 머리말은 배열을 0으로 초기화한다고 적는다. 실행 부분은 값을 누적하고 출력 후 HYDZERO를 호출한다. HYDZERO 내부는 판독하지 않았다.
- 51–56: 한 면의 유량을 더하는 식은 주석이다. 실행식은 두 면 유량의 MAX를 취한다. 이 식에는 ABS가 없다.
- 73–74·83·92–95: 파일은 직접 접근으로 열고 시간 WRITE에는 REC=NR0를 지정한다. 셀 값 WRITE(2)에는 REC 지정이 없다. NEXTREC 조회는 셀 루프 뒤에 있다.
- 76–79: 헤더 READ에서 XDUM을 두 번 사용한다. 뒤의 NDUM=NDUM 및 XDUM=XDUM은 자기 대입이다.
