---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/idcrset.f
lines: 53
sha256: dedf0ab19862cad5e85872a262a0ca01e16937c42719d502935270f3df702d09
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# idcrset.f — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | IDCRSET의 선언과 기본 절점·자유도 목록 생성이다. ND와 NDF의 조합을 IDCR에 저장하고 NCR을 증가시킨다. IMPC == 0이면 900으로 이동한다. 원문: `      SUBROUTINE IDCRSET(IMPC,KN,ND,NDF,INDOF,INDMPC,MPCF,IDCR,NCR)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION KN(ND),IDCR(2,*),INDMPC(2,6,*),MPCF(2,*),INDOF(6,*)` (4)； `      NCR=0` (6)； `      DO 100 I=1,ND` (7)； `      DO 100 J=1,NDF` (8)； `        NCR=NCR+1` (9)； `        IDCR(1,NCR)=KN(I)` (10)； `        IDCR(2,NCR)=J` (11)； `  100 CONTINUE` (12)； `      IF(IMPC .EQ. 0) GOTO 900` (14)。 |
| 16–39 | 시작 시 1행 IDCRSET 루틴 안이다. 14행 `IF(IMPC .EQ. 0) GOTO 900`에서 이동하지 않았으므로 IMPC가 0이 아닌 상태이다. 레이블 900은 52행 `RETURN`이다. INDOF == -2인 항목의 INDMPC 범위를 순회한다. MPCF의 절점·자유도 조합이 IDCR에 없을 때 추가한다. INDOF(J,KN(I))가 -2인 항목을 하나도 만나지 않아 IRAMFLG가 0이면 52행 레이블 900으로 이동한다. 원문: `      IRAMFLG=0` (16)； `      DO 300 I=1,ND` (17)； `        DO 310 J=1,NDF` (18)； `          IF(INDOF(J,KN(I)) .NE. -2) GOTO 310` (19)； `          IRAMFLG=1` (20)； `          IS=INDMPC(1,J,KN(I))` (21)； `          IE=INDMPC(2,J,KN(I))` (22)； `          DO 320 IAD=IS,IE` (24)； `            NODE=MPCF(1,IAD)` (25)； `            IFR =MPCF(2,IAD)` (26)； `            DO 330 K=1,NCR` (27)； `              IF(NODE .EQ. IDCR(1,K) .AND. IFR .EQ. IDCR(2,K)) GOTO 320` (28)； `  330       CONTINUE` (29)； `            NCR=NCR+1` (30)； `            IDCR(1,NCR)=NODE` (31)； `            IDCR(2,NCR)=IFR` (32)； `  320     CONTINUE` (33)； `  310   CONTINUE` (35)； `  300 CONTINUE` (36)； `      IF(IRAMFLG .EQ. 0) GOTO 900` (38)。 [11-04 전수 검증 보완] [11-04 전수 검증 정정] |
| 40–53 | 시작 시 1행 IDCRSET 루틴 안이다. 14행 `IF(IMPC .EQ. 0) GOTO 900`과 38행 `IF(IRAMFLG .EQ. 0) GOTO 900`에서 이동하지 않았으므로 IMPC와 IRAMFLG가 모두 0이 아니다. 원래 절점·자유도 목록을 순회한다. INDOF == -2이면 SHIFT0로 뒤 항목을 옮기고 NCR을 줄인다. ELSE에서는 IP를 증가시킨다. 900에서 반환한다. 원문: `      IP=1` (40)； `      DO 400 I=1,ND` (41)； `        DO 410 J=1,NDF` (42)； `          IF(INDOF(J,KN(I)) .EQ. -2) THEN` (43)； `            CALL SHIFT0(IDCR(1,IP),IDCR(1,IP+1),2*(NCR-IP))` (44)； `            NCR=NCR-1` (45)； `          ELSE` (46)； `            IP=IP+1` (47)； `          ENDIF` (48)； `  410   CONTINUE` (49)； `  400 CONTINUE` (50)； `  900 RETURN` (52)； `      END` (53)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·9–11·30–32: IDCR의 두 번째 차원은 가정 크기이다. NCR 증가 전에 저장 용량을 확인하는 조건은 이 파일에 없다.
