---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cg3fwb2.f
lines: 59
sha256: b680bc324e5f0ef68fe861e0a401e1d38e84d1a380ee985eb49aaeebd4c36c64
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg3fwb2.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | CG3FWB2의 인수와 배열을 선언한다. 주석은 비대칭 스카이라인 행렬(nonsymmetric skyline matrix)의 불완전 분해(incomplete decomposition)를 설명한다. 13–14행의 WRITE·FORMAT은 주석 처리된 코드다. 원문: `      SUBROUTINE CG3FWB2( D,A,X  ,NEQ  ,IDSK,IDCG`<br>`     1                 ,ITO)` (1–2); 주석 원문 `C              SUB FOR INCOMPLETE DECOMPOSITION ` (4); 주석 원문 `C                 ( BLOCKED NONSYMETRIC-SKYLINE MATRIX)` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION  A(*),IDSK(NEQ+1),IDCG(*)` (9); `      DIMENSION  D(NEQ) ,X(NEQ)` (10); 주석 원문 `C===  write(ITO,1009) (X(I),I=1,5),X(NEQ)` (13); 주석 원문 `C1009 FORMAT(' CG3FWB-X=',1P6E15.8)` (14); 주석 원문 `C                    * FOWORD SUBSTITUTION *` (15). |
| 16–30 | 시작 시 1행 CG3FWB2 루틴 안. 전진대입(forward substitution)에서 빈 행이나 현재 행 이상 열을 만나면 1200으로 이동한다. 그 전까지의 하위 항을 뺀 뒤 D를 곱한다. 22–24행은 주석 처리된 대체 코드다. 원문: `      DO 1400 IP=1,NEQ` (16); `      IS=IDSK(IP)+1` (17); `      IE=IDSK(IP+1)-1` (18); `      IF(IS.GT.IE) GO TO 1200` (20); `      DO 1000 J=IS,IE` (21); 주석 원문 `C+++  JP=IDCG(J)` (22); 주석 원문 `C+++  IF(JP.GE.IP) GO TO 1200` (23); 주석 원문 `C+++    X(IP)=X(IP)-A(J)*X(JP)` (24); `      IF(IDCG(J).GE.IP) GO TO 1200` (25); `        X(IP)=X(IP)-A(J)*X(IDCG(J))` (26); ` 1000 CONTINUE` (27); ` 1200 X(IP)=X(IP)*D(IP)` (29); ` 1400 CONTINUE` (30). |
| 31–59 | 시작 시 1행 CG3FWB2 루틴 안. 후진대입(backward substitution)에서 행을 역순으로 방문하고 현재 행보다 크고 NEQ 이하인 열의 곱을 WWW에 더한다. WWW에 D를 곱한 값을 X에서 뺀다. 32–33·44–46·55–56행은 주석 처리된 코드다. 반환문과 루틴 끝을 포함한다. 원문: 주석 원문 `C                    * BACWORD SUBSTITUTION *` (31); 주석 원문 `C===  write(ITO,2209) (X(I),I=1,5),X(NEQ)` (32); 주석 원문 `C2209 FORMAT(' CG3FWB-X=',1P6E15.8)` (33); `      IP=NEQ` (35); `      DO 3200 I=2,NEQ` (36); `      IP=IP-1` (37); `      IS=IDSK(IP)+1` (38); `      IE=IDSK(IP+1)-1` (39); `      IF(IS.GT.IE) GO TO 3200` (41); `      WWW=0.0D0` (42); `      DO 3000 J=IS,IE` (43); 주석 원문 `C+++  JP=IDCG(J)` (44); 주석 원문 `C+++  IF(JP.GT.IP) THEN` (45); 주석 원문 `C+++    WWW=WWW+A(J)*X(JP)` (46); `      IF(IDCG(J).GT.IP .AND. IDCG(J).LE.NEQ) THEN` (47); `        WWW=WWW+A(J)*X(IDCG(J))` (48); `      END IF` (49); ` 3000 CONTINUE` (50); `      X(IP)=X(IP)-WWW*D(IP)` (52); ` 3200 CONTINUE` (53); 주석 원문 `C===  write(ITO,3209) (X(I),I=1,5),X(NEQ)` (55); 주석 원문 `C3209 FORMAT(' CG3FWB-X=',1P6E15.8)` (56); `      RETURN` (58); `      END` (59). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–2·13–14·32–33·55–56: ITO는 인수에 있으나 이 파일에서 ITO를 쓰는 WRITE 문은 모두 주석 처리되어 있다.
