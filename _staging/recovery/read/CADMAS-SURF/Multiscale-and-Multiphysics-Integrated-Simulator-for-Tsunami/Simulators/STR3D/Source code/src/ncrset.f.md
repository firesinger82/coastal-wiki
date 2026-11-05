---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ncrset.f
lines: 40
sha256: 565bfd18e182e84533f492eca8240682281726fd5160ad79c1016f322060a23c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ncrset.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | NCRSET의 배열 선언과 NC 계산이다. INDOF == -2인 항목의 MPCF 범위를 순회한다. NODE가 원래 KN에 있으면 건너뛴다. IDWK에 같은 절점·자유도 조합이 있으면 건너뛰고 없을 때만 추가한다. 12행 NCR 감소문은 주석 처리된 코드이다. 원문: `      SUBROUTINE NCRSET(ND,NDF,KN,INDOF,INDMPC,MPCF,IDWK,NCRMAX,NRAMAX)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION INDOF(6,*),KN(ND),INDMPC(2,6,*),MPCF(2,*),IDWK(2,*)` (4)； `      NC=ND*NDF` (6)； `      NCR=0` (7)； `      DO 300 I=1,ND` (9)； `        DO 310 J=1,NDF` (10)； `          IF(INDOF(J,KN(I)) .NE. -2) GOTO 310` (11)； `C+++      NCR=NCR-1` (12)； `          IS=INDMPC(1,J,KN(I))` (13)； `          IE=INDMPC(2,J,KN(I))` (14)； `          DO 320 IAD=IS,IE` (16)； `            NODE=MPCF(1,IAD)` (17)； `            IFR =MPCF(2,IAD)` (18)； `            DO 330 K=1,ND` (19)； `              IF(NODE .EQ. KN(K)) GOTO 320` (20)； `  330       CONTINUE` (21)； `            DO 340 K=1,NCR` (22)； `              IF(NODE .EQ. IDWK(1,K) .AND. IFR .EQ. IDWK(2,K)) GOTO 320` (23)； `  340       CONTINUE` (24)； `            NCR=NCR+1` (25)； `            IDWK(1,NCR)=NODE` (26)； `            IDWK(2,NCR)=IFR` (27)； `  320     CONTINUE` (28)； `  310   CONTINUE` (30)； `  300 CONTINUE` (31)。 |
| 33–40 | 시작 시 1행 NCRSET 루틴 안이며 9·10행 루프 밖이다. NC에 추가 개수를 합하여 NCR을 구하고 NRA를 계산한다. NCRMAX·NRAMAX를 각각 최댓값으로 갱신한다. 34행 MAX0 대입문은 주석 처리된 코드이다. 원문: `      NCR=NC+NCR` (33)； `C+++  NCR=MAX0(NC,NCR)` (34)； `      NRA=NC*NCR` (35)； `      NCRMAX=MAX0(NCRMAX,NCR)` (36)； `      NRAMAX=MAX0(NRAMAX,NRA)` (37)； `      RETURN` (39)； `      END` (40)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–23: 원래 KN에 포함되는지 검사할 때는 NODE만 비교한다. IDWK 중복 검사에서는 NODE와 IFR을 함께 비교한다.
- 12·34: NCR 감소문과 NCR=MAX0(NC,NCR) 문장은 C+++로 시작하는 주석이다.
