---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_MPC.f
lines: 31
sha256: e79223359a8480176f02dbda8dbaa59ad854ad989c284c13d17b9a9bb5dfb732
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_MPC.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | ST_MPC는 IMPC와 JMPC에 누적 끝 위치를 만든다. 해석: MPC는 다점 구속(multipoint constraint)을 뜻하며 IP는 방정식 수에 해당한다고 읽는다. 인수·암시적 배정밀도·배열을 선언한다(1–6). IP와 IP2를 0에서 시작한다(8–9). 세트 번호 일치 시 입력 IS:IE를 순회해 NMPC와 AMPC를 복사하고 JMPC에 항목 누적 끝을 저장한다(11–25). IMPC 두 번째 성분은 방정식 누적 끝이다(26). NMPC 첫 성분을 INDGR로 변환한다(29). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_MPC( IMPC, JMPC, NMPC, AMPC, NIMPC, NNMPC,` (1) <br> `     &                   J_MPC, J2_MPC, R2_MPC, N_MPC, INDGR )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION IMPC(2,NIMPC), JMPC(*), NMPC(2,NNMPC), AMPC(NNMPC), ` (5) <br> `     &          J_MPC(3,N_MPC), J2_MPC(2,*), R2_MPC(*), INDGR(*)` (6) <br> `      IP = 0` (8) <br> `      IP2 = 0` (9) <br> `      DO I = 1, NIMPC` (11) <br> `        DO J = 1, N_MPC` (12) <br> `          IF( J_MPC(1,J) == IMPC(1,I) ) THEN` (13) <br> `            IS = J_MPC(2,J)` (14) <br> `            IE = J_MPC(3,J)` (15) <br> `            DO K = IS, IE` (16) <br> `              IP2 = IP2 + 1` (17) <br> `              NMPC(1,IP2) = J2_MPC(1,K)` (18) <br> `              NMPC(2,IP2) = J2_MPC(2,K)` (19) <br> `              AMPC(IP2)   = R2_MPC(K)` (20) <br> `            ENDDO` (21) <br> `            IP = IP + 1` (22) <br> `            JMPC(IP) = IP2` (23) <br> `          ENDIF` (24) <br> `        ENDDO` (25) <br> `        IMPC(2,I) = IP` (26) <br> `      ENDDO` (27) <br> `      NMPC(1,:) = INDGR( NMPC(1,:) )` (29) <br> `      END` (31) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
