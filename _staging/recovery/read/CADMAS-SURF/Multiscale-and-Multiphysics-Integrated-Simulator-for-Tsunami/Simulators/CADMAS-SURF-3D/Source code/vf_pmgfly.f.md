---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_pmgfly.f
lines: 65
sha256: 1c9faf9e5cb96d60ea875ff8ef5843a918b2ffe2b84b8bfe07264665bbfcd44e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_pmgfly.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | VF_PMGFLY의 연속 문장 선언이다. IMPLICIT NONE과 인수 방향, 배열 범위, 지역변수를 선언한다. 호출부는 `vf_pmgc2p_cf.f:163–165`에서 VDT에 DTNOW*GGY(IC,JC,KC)*VV(IC,JC,KC)를 전달한다. 해석: 이 인수를 이동량으로 보고 면의 VOF 함수를 계산하는 루틴으로 읽을 수 있다. 원문: `      SUBROUTINE VF_PMGFLY(FLF,VDT,FF,BCF,YY,GGV,FLOWER,NF,INDY` (1); 앞 행에서 이어지는 같은 문장: `     &                    ,I,J,K,NUMI,NUMJ,NUMK,MAXG1,NUMB)` (2); `C` (3); `      IMPLICIT NONE` (4); `C` (5); `      INTEGER,INTENT(IN) :: NUMI,NUMJ,NUMK,MAXG1,NUMB` (6); `      REAL(8),INTENT(OUT) :: FLF` (7); `      REAL(8),INTENT(IN) :: VDT` (8); `      REAL(8),INTENT(IN) :: FF(NUMI,NUMJ,NUMK)` (9); `      REAL(8),INTENT(IN) :: BCF(NUMB)` (10); `      REAL(8),INTENT(IN) :: YY(MAXG1,NUMJ)` (11); `      REAL(8),INTENT(IN) :: GGV(NUMI,NUMJ,NUMK)` (12); `      REAL(8),INTENT(IN) :: FLOWER` (13); `      INTEGER,INTENT(IN) :: NF(NUMI,NUMJ,NUMK)` (14); `      INTEGER,INTENT(IN) :: INDY(NUMI,NUMJ,NUMK)` (15); `      INTEGER,INTENT(IN) :: I,J,K` (16); `C` (17); `      REAL(8) :: FA,FD,FDMW,FAD,FDM` (18); `      REAL(8) :: V` (19); `      REAL(8) :: CFX,FVX,FVM` (20); `      INTEGER :: LSN,LA,LD,LDM` (21); `      INTEGER :: N` (22); `C` (23). [11-04 전수 검증 정정] |
| 24–51 | 시작 시 1–2행 VF_PMGFLY 루틴 안. VDT가 0 이상이면 LSN=+1, LA=J, LD=J-1, LDM=J-2로 설정한다. 음수이면 LSN=-1, LA=J-1, LD=J, LDM=J+1로 설정한다. `      N = NF(I,LD,K)` (36)으로 검사 대상을 정한다. N=-1이면 `        FD = BCF(INDY(I,J,K))` (43)를 사용한다. N이 -1이 아니면 FD에 FF 값을 넣고 V에 YY(2,LD)*GGV(I,LD,K)를 넣는다. LA 위치의 NF가 -1이면 FA는 FD를 사용한다. 해석: LA·LD·LDM을 각각 수용·공여·상류 인덱스로 읽을 수 있다. 원문: `      IF(VDT.GE.0.0D0) THEN` (24); `        LSN = +1` (25); `        LA  = J` (26); `        LD  = J-1` (27); `        LDM = J-2` (28); `      ELSE` (29); `        LSN = -1` (30); `        LA  = J-1` (31); `        LD  = J` (32); `        LDM = J+1` (33); `      END IF` (34); `C` (35); `      N = NF(I,LD,K)` (36); `      IF(N.NE.-1) THEN` (37); `        FD = FF(I,LD,K)` (38); `        FDMW = 1.0D0` (39); `        IF(NF(I,LDM,K).NE.-1) FDMW = FF(I,LDM,K)` (40); `        V = YY(2,LD)*GGV(I,LD,K)` (41); `      ELSE` (42); `        FD = BCF(INDY(I,J,K))` (43); `        FDMW = 1.0D0` (44); `        V = YY(2,LD)` (45); `      END IF` (46); `      IF(NF(I,LA,K).NE.-1) THEN` (47); `        FA = FF(I,LA,K)` (48); `      ELSE` (49); `        FA = FD` (50); `      END IF` (51). [11-04 전수 검증 정정] |
| 52–65 | 시작 시 1–2행 VF_PMGFLY 루틴 안. 셀 상태 조건으로 FAD를 바꾼다. FLOWER 조건에서 FDM 하한을 0.1로 올린다. CFX·FVX·FVM을 계산하고 MIN으로 제한한 뒤 VDT로 나누어 FLF를 구한다. 원문: `      FAD = FA` (52); `      IF(N.EQ.-1 .OR. N.EQ.1 .OR. N.EQ.2` (53); 앞 행에서 이어지는 같은 문장: `     &           .OR. N.EQ.5 .OR. N.EQ.6) THEN` (54); `        IF(FDMW.NE.0.0D0 .AND. FA.NE.0.0D0) FAD = FD` (55); `      END IF` (56); `      FDM = MAX(FDMW,FD)` (57); `      IF(FDMW.LT.FLOWER .AND. FA.LT.FLOWER) FDM=MAX(FDM,0.1D0)` (58); `      CFX = MAX((FDM-FAD)*ABS(VDT)-(FDM-FD)*V,0.0D0)` (59); `      FVX = FAD*ABS(VDT) + CFX` (60); `      FVM = FD*V` (61); `      FLF = DBLE(LSN)*MIN(FVX,FVM)/VDT` (62); `C` (63); `      RETURN` (64); `      END` (65). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·62: VDT=0을 별도로 제외하는 분기는 없으며 마지막 FLF 식에서 VDT로 나눈다.
- 43: 경계 분기는 INDY(I,J,K)를 BCF 첨자로 직접 사용한다. 이 분기에 양수 인덱스 검사는 없다.
