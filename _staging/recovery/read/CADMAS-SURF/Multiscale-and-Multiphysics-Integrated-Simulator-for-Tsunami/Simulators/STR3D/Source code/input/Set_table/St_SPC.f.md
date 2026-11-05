---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_SPC.f
lines: 30
sha256: 9daab4b2011375e93693d37bc8e8b2ad58803cb277397848ecbcd889c766a0be
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_SPC.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 해석: ST_SPC는 단점 구속(single-point constraint) 세트를 구성하는 루틴으로 읽는다. NSPC(7,NNSPC)·SPC(6,NNSPC)를 선언한다(5–6). 세트 번호 일치 시 입력 2:8 성분을 NSPC로 복사하고 R_SPC에 3:8 성분을 곱해 SPC를 계산한다(10–22). ISPC 두 번째 성분은 누적 끝 위치다(24). NSPC 첫 성분은 INDGR로 변환한다(28). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_SPC( ISPC, NSPC, SPC, NISPC, NNSPC, J_SPC,` (1) <br> `     &                   R_SPC, N_SPC, INDGR )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION ISPC(2,NISPC), NSPC(7,NNSPC), SPC(6,NNSPC), ` (5) <br> `     &          J_SPC(8,N_SPC), R_SPC(N_SPC), INDGR(*)` (6) <br> `      IP = 0` (8) <br> `      DO I = 1, NISPC` (10) <br> `        DO J = 1, N_SPC` (12) <br> `          IF( J_SPC(1,J) == ISPC(1,I) ) THEN` (14) <br> `            IP = IP + 1` (16) <br> `            NSPC(:,IP) = J_SPC(2:8,J)` (17) <br> `            SPC(:,IP) = R_SPC(J) * J_SPC(3:8,J)` (18) <br> `          ENDIF` (20) <br> `        ENDDO` (22) <br> `        ISPC(2,I) = IP` (24) <br> `      ENDDO` (26) <br> `      NSPC(1,:) = INDGR( NSPC(1,:) )` (28) <br> `      END` (30) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
