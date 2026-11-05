---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/vrtxchk.f
lines: 73
sha256: ee9cf07408027daffe85bcbef5e4c6cd72f3802b322128b6a9692caea426a4c8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vrtxchk.f — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | VRTXCHK는 정점(vertex) 접촉 후보를 검사한다. DATA TOL=75.D0이며 후보 배열 ISLIP,FSLIP,CSLIP 크기는 20이다(5–8). MASTER 인접 요소마다 VRTXSEPA를 호출하고 ICHK=1이면 210번 표지로 이동한다(10–19). 그런 요소가 없으면 반환한다(21). 원문: 연속문(1–2): `      SUBROUTINE VRTXCHK(ISLV,MASTER,FC,EN,IEDG,IELC,ICELA,ICEL,IBTE` (1); `     &                  ,ICEDA,ICED,POS,ITO)` (2). `      IMPLICIT REAL*8(A-H,O-Z)` (4). 연속문(5–7): `      DIMENSION IEDG(6,*),POS(3,*),ISLIP(2,20),FSLIP(20),CSLIP(20),FC(3)` (5); `     &         ,EN(3),IELC(3,*),ISLV(2),ICELA(2,*),ICEL(*),ICEDA(2,*)` (6); `     &         ,ICED(*),IBTE(4,*)` (7). `      DATA TOL /75.D0/` (8). `      IS=ICELA(1,MASTER)` (10). `      IE=ICELA(2,MASTER)` (11). `      ICHK=0` (13). `      DO 200 I=IS,IE` (15). `        J=ICEL(I)` (16). `        CALL VRTXSEPA(ICHK,MASTER,FC,IBTE(1,J),POS,ITO)` (17). `        IF(ICHK .EQ. 1) GOTO 210` (18). `  200 CONTINUE` (19). `      RETURN` (21). |
| 23–35 | 시작 시 1–2행 VRTXCHK 루틴 안. MASTER의 인접 변(edge) 범위를 얻고 NSLIP,INCOMP를 0으로 초기화한다(23–28). 각 변에 VRTXSLIP을 호출하여 후보 목록을 채운다(30–34). 원문: `  210 IS=ICEDA(1,MASTER)` (23). `      IE=ICEDA(2,MASTER)` (24). `      NSLIP=0` (26). `      INCOMP=0` (28). `      DO 100 I=IS,IE` (30). `        J=ICED(I)` (31). 연속문(32–33): `        CALL VRTXSLIP(NSLIP,ISLIP,FSLIP,CSLIP,INCOMP,MASTER,FC,EN,J` (32); `     &               ,IEDG(1,J),IELC,POS,ITO)` (33). `  100 CONTINUE` (34). |
| 36–62 | 시작 시 1–2행 VRTXCHK 루틴 안. NSLIP>0이면 TOL에서 COST를 계산한다(36–38). CSLIP>COST이고 FSLIP이 현재 최대보다 큰 후보를 우선 선택한다(40–48). 선택하지 못했으면 CMAX=-1.1D0에서 CSLIP 최대 후보를 선택한다(50–61). 원문: `      IF(NSLIP .GT. 0) THEN` (36). `        COST=DCOS(TOL/90.D0*DASIN(1.D0))` (38). `        IP=0` (40). `        FSMAX=0.` (41). `        DO 300 I=1,NSLIP` (43). `          IF(CSLIP(I) .GT. COST .AND. FSLIP(I) .GT. FSMAX) THEN` (44). `            IP=I` (45). `            FSMAX=FSLIP(I)` (46). `          ENDIF` (47). `  300   CONTINUE` (48). `        IF(IP .EQ. 0) THEN` (50). `          CMAX=-1.1D0` (52). `          DO 400 I=1,NSLIP` (54). `            IF(CSLIP(I) .GT. CMAX) THEN` (55). `              IP=I` (56). `              CMAX=CSLIP(I)` (57). `            ENDIF` (58). `  400     CONTINUE` (59). `        ENDIF` (61). |
| 63–73 | 시작 시 1–2행 VRTXCHK 루틴·36행 `IF(NSLIP .GT. 0) THEN`의 참 분기 안. 이 IF는 71행 `ENDIF`에서 닫힌다. 선택한 후보의 두 상태를 ISLV로 복사한다(63–64). NSLIP>0이 아니고 INCOMP=0이면 정점 상태 1과 MASTER를 저장한다(66–69). 분기 종료와 END를 포함한다. 원문: `        ISLV(1)=ISLIP(1,IP)` (63). `        ISLV(2)=ISLIP(2,IP)` (64). `      ELSEIF(INCOMP .EQ. 0) THEN` (66). `        ISLV(1)=1` (68). `        ISLV(2)=MASTER` (69). `      ENDIF` (71). `      END` (73). 이 분기 사슬에는 ELSE가 없다. NSLIP<=0이고 INCOMP/=0이면 ISLV를 갱신하지 않는다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·30–34: 후보 배열 크기는 20이며 VRTXSLIP 호출 앞에 NSLIP 상한 검사는 없다.
- 50–64: IP=0인 경우 CMAX=-1.1D0보다 큰 CSLIP이 있어야 IP가 새로 설정되며 복사 직전 별도 IP 검사는 없다.
