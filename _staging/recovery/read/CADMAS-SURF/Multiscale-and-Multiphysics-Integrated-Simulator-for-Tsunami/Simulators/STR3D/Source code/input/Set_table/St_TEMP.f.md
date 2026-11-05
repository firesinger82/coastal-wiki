---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_TEMP.f
lines: 33
sha256: db593ad400256881022b76b5251d47aa98b2b64597c32da5aa67449e4ff04565
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_TEMP.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 해석: ST_TEMP는 온도(temperature) 세트와 절점 온도를 구성하는 루틴으로 읽는다. 기본 온도 세트 J_TMPD를 먼저 복사하고 아직 없는 J_TMP 세트를 추가한다(8–18). 기본 온도가 있는 각 세트의 모든 절점을 R_TMPD로 채운다(20–22). 각 세트와 일치하는 절점 입력을 찾고 INDGR로 변환한 IG의 온도를 덮어쓴다(24–31). TEMP의 크기는 (NNOD,NITMP)다(5–6). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_TEMP( ITMP, TEMP, NITMP, J_TMPD, R_TMPD, N_TMPD,` (1) <br> `     &                    J_TMP, R_TMP, N_TMP, INDGR, NNOD )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION ITMP(NITMP), TEMP(NNOD,NITMP), J_TMPD(N_TMPD),` (5) <br> `     &          R_TMPD(N_TMPD), J_TMP(2,N_TMP), R_TMP(N_TMP), INDGR(*)` (6) <br> `      ITMP(1:N_TMPD) = J_TMPD(:)` (8) <br> `      N = N_TMPD` (10) <br> `      DO 10 I = 1, N_TMP` (12) <br> `        DO J = 1, N` (13) <br> `          IF( J_TMP(1,I) == ITMP(J) ) GOTO 10` (14) <br> `        ENDDO` (15) <br> `        N = N + 1` (16) <br> `        ITMP(N) = J_TMP(1,I)` (17) <br> `   10 CONTINUE` (18) <br> `      DO I = 1, N_TMPD` (20) <br> `        TEMP(:,I) = R_TMPD(I)` (21) <br> `      ENDDO` (22) <br> `      DO I = 1, NITMP` (24) <br> `        DO J = 1, N_TMP` (25) <br> `          IF( J_TMP(1,J) == ITMP(I) ) THEN` (26) <br> `            IG = INDGR( J_TMP(2,J) )` (27) <br> `            TEMP(IG,I) = R_TMP(J)` (28) <br> `          ENDIF` (29) <br> `        ENDDO` (30) <br> `      ENDDO` (31) <br> `      END` (33) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–28: 전체 절점에 기본 온도를 대입하는 루프는 1:N_TMPD다. 뒤에 추가된 세트는 일치하는 절점 입력 위치만 대입한다.
