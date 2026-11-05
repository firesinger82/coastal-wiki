---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_TEMPD.f
lines: 13
sha256: e20c2362332e45f0947b550ec02038f6d01490f6ab4488abdf651f3fd480052c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_TEMPD.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 80자 CHAR와 ID(3)를 선언한다(3–4). BN,8X,3(I8,8X) 형식으로 ID의 정수 3개를 읽는다(6). 해석: ID는 기본 온도(default temperature) 집합 번호이다. I=1..3에서 첫 0 앞까지 N_TMPD를 늘린다(8–11). 원문: `      SUBROUTINE CT_TEMPD( N_TMPD, CHAR )` (1); `      CHARACTER*80 CHAR` (3); `      DIMENSION ID(3)` (4); `      READ(CHAR,'(BN,8X,3(I8,8X))') ID(:)` (6); `      DO I = 1, 3` (8); `        IF( ID(I) == 0 ) EXIT` (9); `        N_TMPD = N_TMPD + 1` (10); `      ENDDO` (11); `      END` (13). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
