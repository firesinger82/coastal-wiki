---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_pmgflx.f
lines: 65
sha256: 69bbf903c78040589d3a83696b74f8e8917126aca662e1c2a2fad4daaff75398
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_pmgflx.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | VF_PMGFLX의 연속 문장 선언이다. IMPLICIT NONE과 인수 방향, 배열 범위, 지역변수를 선언한다. 호출부는 `vf_pmgc2p_cf.f:104–106`에서 UDT에 DTNOW*GGX(IC,JC,KC)*UU(IC,JC,KC)를 전달한다. 해석: 이 인수를 이동량으로 보고 면의 VOF 함수를 계산하는 루틴으로 읽을 수 있다. 원문: `      SUBROUTINE VF_PMGFLX(FLF,UDT,FF,BCF,XX,GGV,FLOWER,NF,INDX` (1); 앞 행에서 이어지는 같은 문장: `     &                    ,I,J,K,NUMI,NUMJ,NUMK,MAXG1,NUMB)` (2); `C` (3); `      IMPLICIT NONE` (4); `C` (5); `      INTEGER,INTENT(IN) :: NUMI,NUMJ,NUMK,MAXG1,NUMB` (6); `      REAL(8),INTENT(OUT) :: FLF` (7); `      REAL(8),INTENT(IN) :: UDT` (8); `      REAL(8),INTENT(IN) :: FF(NUMI,NUMJ,NUMK)` (9); `      REAL(8),INTENT(IN) :: BCF(NUMB)` (10); `      REAL(8),INTENT(IN) :: XX(MAXG1,NUMI)` (11); `      REAL(8),INTENT(IN) :: GGV(NUMI,NUMJ,NUMK)` (12); `      REAL(8),INTENT(IN) :: FLOWER` (13); `      INTEGER,INTENT(IN) :: NF(NUMI,NUMJ,NUMK)` (14); `      INTEGER,INTENT(IN) :: INDX(NUMI,NUMJ,NUMK)` (15); `      INTEGER,INTENT(IN) :: I,J,K` (16); `C` (17); `      REAL(8) :: FA,FD,FDMW,FAD,FDM` (18); `      REAL(8) :: V` (19); `      REAL(8) :: CFX,FVX,FVM` (20); `      INTEGER :: LSN,LA,LD,LDM` (21); `      INTEGER :: N` (22); `C` (23). [11-04 전수 검증 정정] |
| 24–51 | 시작 시 1–2행 VF_PMGFLX 루틴 안. UDT가 0 이상이면 LSN=+1, LA=I, LD=I-1, LDM=I-2로 설정한다. 음수이면 LSN=-1, LA=I-1, LD=I, LDM=I+1로 설정한다. `      N = NF(LD,J,K)` (36)으로 검사 대상을 정한다. N=-1이면 `        FD = BCF(INDX(I,J,K))` (43)를 사용한다. N이 -1이 아니면 FD에 FF 값을 넣고 V에 XX(2,LD)*GGV(LD,J,K)를 넣는다. LA 위치의 NF가 -1이면 FA는 FD를 사용한다. 해석: LA·LD·LDM을 각각 수용·공여·상류 인덱스로 읽을 수 있다. 원문: `      IF(UDT.GE.0.0D0) THEN` (24); `        LSN = +1` (25); `        LA  = I` (26); `        LD  = I-1` (27); `        LDM = I-2` (28); `      ELSE` (29); `        LSN = -1` (30); `        LA  = I-1` (31); `        LD  = I` (32); `        LDM = I+1` (33); `      END IF` (34); `C` (35); `      N = NF(LD,J,K)` (36); `      IF(N.NE.-1) THEN` (37); `        FD = FF(LD,J,K)` (38); `        FDMW = 1.0D0` (39); `        IF(NF(LDM,J,K).NE.-1) FDMW = FF(LDM,J,K)` (40); `        V = XX(2,LD)*GGV(LD,J,K)` (41); `      ELSE` (42); `        FD = BCF(INDX(I,J,K))` (43); `        FDMW = 1.0D0` (44); `        V = XX(2,LD)` (45); `      END IF` (46); `      IF(NF(LA,J,K).NE.-1) THEN` (47); `        FA = FF(LA,J,K)` (48); `      ELSE` (49); `        FA = FD` (50); `      END IF` (51). [11-04 전수 검증 정정] |
| 52–65 | 시작 시 1–2행 VF_PMGFLX 루틴 안. 셀 상태 조건으로 FAD를 바꾼다. FLOWER 조건에서 FDM 하한을 0.1로 올린다. CFX·FVX·FVM을 계산하고 MIN으로 제한한 뒤 UDT로 나누어 FLF를 구한다. 원문: `      FAD = FA` (52); `      IF(N.EQ.-1 .OR. N.EQ.3 .OR. N.EQ.4` (53); 앞 행에서 이어지는 같은 문장: `     &           .OR. N.EQ.5 .OR. N.EQ.6) THEN` (54); `        IF(FDMW.NE.0.0D0 .AND. FA.NE.0.0D0) FAD = FD` (55); `      END IF` (56); `      FDM = MAX(FDMW,FD)` (57); `      IF(FDMW.LT.FLOWER .AND. FA.LT.FLOWER) FDM=MAX(FDM,0.1D0)` (58); `      CFX = MAX((FDM-FAD)*ABS(UDT)-(FDM-FD)*V,0.0D0)` (59); `      FVX = FAD*ABS(UDT) + CFX` (60); `      FVM = FD*V` (61); `      FLF = DBLE(LSN)*MIN(FVX,FVM)/UDT` (62); `C` (63); `      RETURN` (64); `      END` (65). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·62: UDT=0을 별도로 제외하는 분기는 없으며 마지막 FLF 식에서 UDT로 나눈다.
- 43: 경계 분기는 INDX(I,J,K)를 BCF 첨자로 직접 사용한다. 이 분기에 양수 인덱스 검사는 없다.
