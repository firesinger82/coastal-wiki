---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_PLOAD1.f
lines: 32
sha256: 19b0a1745e447a6cd8899ee0b3f6f678dd21f7ad287882ec85eb3b5229d433a7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_PLOAD1.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 해석: ST_PLOAD1은 세트별 선 하중(line load) 항목을 구성하는 루틴으로 읽는다. IPL1·NPL1·PLD1(3,NNPL1)과 입력 배열 범위를 선언한다(1–6). 세트 식별자가 일치하면 요소 번호와 입력 성분 IC의 값을 복사한다(10–24). IPL1의 두 번째 성분은 누적 끝 위치다(26). 요소 번호는 IELR로 변환한다(30). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_PLOAD1( IPL1, NPL1, PLD1, NIPL1, NNPL1, J_PL1,` (1) <br> `     &                      R_PL1, N_PL1, IELR )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION IPL1(2,NIPL1), NPL1(NNPL1), PLD1(3,NNPL1), ` (5) <br> `     &          J_PL1(3,N_PL1), R_PL1(N_PL1), IELR(*)` (6) <br> `      IP = 0` (8) <br> `      DO I = 1, NIPL1` (10) <br> `        DO J = 1, N_PL1` (12) <br> `          IF( J_PL1(1,J) == IPL1(1,I) ) THEN` (14) <br> `            IP = IP + 1` (16) <br> `            NPL1(IP) = J_PL1(2,J)` (18) <br> `            IC = J_PL1(3,J)` (19) <br> `            PLD1(IC,IP) = R_PL1(J)` (20) <br> `          ENDIF` (22) <br> `        ENDDO` (24) <br> `        IPL1(2,I) = IP` (26) <br> `      ENDDO` (28) <br> `      NPL1(:) = IELR( NPL1(:) )` (30) <br> `      END` (32) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–20: 입력 IC를 PLD1의 첨자로 직접 사용한다. 이 파일에는 IC의 1:3 범위 검사나 나머지 성분의 초기화가 없다.
