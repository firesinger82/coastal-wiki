---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/sid_count2.f
lines: 21
sha256: fa33375bf649c2304e015b49f91fde7ca90411c6a8a8c32838c46d82dc12765d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sid_count2.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | SID_COUNT2는 NITMP를 N_TMPD로 초기화한다(5). J_TMP(1,I)가 J_TMPD(1:N_TMPD)에 있거나 앞선 J_TMP(1,1:I-1)에 있으면 19행 레이블 10으로 건너뛴다(7–19). 두 검색 모두 미일치인 경우만 NITMP를 증가시킨다(17). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE SID_COUNT2( NITMP, J_TMPD, N_TMPD, J_TMP, N_TMP )` (1) <br> `      DIMENSION J_TMPD(N_TMPD), J_TMP(2,N_TMP)` (3) <br> `      NITMP = N_TMPD` (5) <br> `      DO 10 I = 1, N_TMP` (7) <br> `        DO J = 1, N_TMPD` (9) <br> `          IF( J_TMP(1,I) == J_TMPD(J) ) GOTO 10` (10) <br> `        ENDDO` (11) <br> `        DO J = I - 1, 1, -1` (13) <br> `          IF( J_TMP(1,I) == J_TMP(1,J) ) GOTO 10` (14) <br> `        ENDDO` (15) <br> `        NITMP = NITMP + 1` (17) <br> `   10 CONTINUE` (19) <br> `      END` (21) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·9–10: 초기 NITMP는 N_TMPD를 그대로 사용한다. J_TMPD 내부의 중복을 제거하는 루프는 이 파일에 없다.
