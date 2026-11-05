---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_PLOAD4.f
lines: 46
sha256: c19b7ceb8e9e27b72e8f1cc6b9cd45dad45f32d1970034fa8bd84692b5afd43f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_PLOAD4.f — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | 해석: ST_PLOAD4는 압력 하중을 세트별로 구성하는 루틴으로 읽는다. NPL4·PLD4의 첫 차원은 각각 4다(5–7). 세트 일치 시 요소 외부 번호 IS:IE를 순회하고 IELR(K)>0인 요소만 등록한다(11–37). IPL4 두 번째 성분에 누적 끝을 저장한다(35). 등록 후 NPL4(1,I)는 IELR로 변환한다(40). 양수인 NPL4(2,I)와 NPL4(3,I)는 각각 INDGR로 변환한다(41–42). 양수인 NPL4(4,I)는 ICRDR로 변환한다(43). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_PLOAD4( IPL4, NPL4, PLD4, NIPL4, NNPL4, J_PL4,` (1) <br> `     &                      R_PL4, N_PL4, ICRDR, INDGR, IELR )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION IPL4(2,NIPL4), NPL4(4,NNPL4), PLD4(4,NNPL4), ` (5) <br> `     &          J_PL4(6,N_PL4), R_PL4(4,N_PL4), IELR(*), INDGR(*),` (6) <br> `     &          ICRDR(*)` (7) <br> `      IP = 0` (9) <br> `      DO I = 1, NIPL4` (11) <br> `        DO J = 1, N_PL4` (13) <br> `          IF( J_PL4(1,J) == IPL4(1,I) ) THEN` (15) <br> `            IS = J_PL4(2,J)` (17) <br> `            IE = J_PL4(3,J)` (18) <br> `            DO K = IS, IE` (20) <br> `              IF( IELR(K) > 0 ) THEN` (21) <br> `                IP = IP + 1` (22) <br> `                NPL4(1,IP) = K` (23) <br> `                NPL4(2,IP) = J_PL4(4,J)` (24) <br> `                NPL4(3,IP) = J_PL4(5,J)` (25) <br> `                NPL4(4,IP) = J_PL4(6,J)` (26) <br> `                PLD4(:,IP) = R_PL4(:,J)` (27) <br> `              ENDIF` (28) <br> `            ENDDO ` (29) <br> `          ENDIF` (31) <br> `        ENDDO` (33) <br> `        IPL4(2,I) = IP` (35) <br> `      ENDDO` (37) <br> `      DO I = 1, NNPL4` (39) <br> `        NPL4(1,I) = IELR( NPL4(1,I) )` (40) <br> `        IF( NPL4(2,I) > 0 ) NPL4(2,I) = INDGR( NPL4(2,I) )` (41) <br> `        IF( NPL4(3,I) > 0 ) NPL4(3,I) = INDGR( NPL4(3,I) )` (42) <br> `        IF( NPL4(4,I) > 0 ) NPL4(4,I) = ICRDR( NPL4(4,I) )` (43) <br> `      ENDDO` (44) <br> `      END` (46) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
