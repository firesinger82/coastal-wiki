---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpccorr.f
lines: 31
sha256: 146ad73db0f78dd60b650a53e740b2e3869fe317f1c52d21b7b09cb294b60ba8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpccorr.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 루틴·암시적 자료형과 인수 배열을 선언한다(1–6). IR=1..NRANK, I=1..NINDC 순으로 순회하며 IRANK가 IR과 다른 항은 건너뛴다(8–10). 상태 11은 MPCCORR11, 12·14는 MPCCORR12, 13·15는 MPCCORR13을 호출하고 상태에서 10을 뺀다(14–22). 상태 2는 MPCCORR2, 3은 MPCCORR3을 호출한다(23–26). 두 루프·루틴을 끝낸다(28–31). 원문: `      SUBROUTINE MPCCORR(UG,POS,ISLV,RSLV,NINDC,NRANK,INDOF,IELC,INDC` `     &                  ,IEDG,IRANK)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION ISLV(2,NINDC),RSLV(3,NINDC),POS(3,*),IELC(3,*)` `     &         ,INDC(NINDC),IEDG(6,*),UG(6,*),INDOF(6,*),IRANK(NINDC)` (5–6, 하나의 고정형식 연속문); `      DO 200 IR=1,NRANK` (8); `        DO 100 I=1,NINDC` (9); `          IF( IRANK(I) .NE. IR ) CYCLE` (10); `          NS =INDC(I)` (11); `          IST=ISLV(1,I)` (12); `          MA =ISLV(2,I)` (13); `          IF( IST .EQ. 11 ) THEN` (14); `            CALL MPCCORR11(UG,POS,NS,MA)` (15); `            ISLV(1,I)=IST-10` (16); `          ELSEIF( IST .EQ. 12 .OR. IST .EQ. 14 ) THEN` (17); `            CALL MPCCORR12(UG,POS,NS,RSLV(1,I),INDOF(1,NS),IEDG(1,MA))` (18); `            ISLV(1,I)=IST-10` (19); `          ELSEIF( IST .EQ. 13 .OR. IST .EQ. 15 ) THEN` (20); `            CALL MPCCORR13(UG,POS,NS,RSLV(1,I),INDOF(1,NS),IELC(1,MA))` (21); `            ISLV(1,I)=IST-10` (22); `          ELSEIF( IST .EQ. 2 ) THEN` (23); `            CALL MPCCORR2(UG,POS,NS,INDOF(1,NS),IEDG(1,MA))` (24); `          ELSEIF( IST .EQ. 3 ) THEN` (25); `            CALL MPCCORR3(UG,POS,NS,INDOF(1,NS),IELC(1,MA))` (26). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–27: 나열된 상태 이외를 처리하는 ELSE는 없다.
