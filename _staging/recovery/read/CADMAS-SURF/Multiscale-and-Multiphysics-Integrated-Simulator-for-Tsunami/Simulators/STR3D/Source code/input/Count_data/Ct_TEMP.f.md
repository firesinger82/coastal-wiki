---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_TEMP.f
lines: 13
sha256: 10c896e85ca18f417f083dcfe510673f175cb4a21bb1add53d3de3de2422fc67
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_TEMP.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 80자 CHAR와 IG(3)를 선언한다(3–4). BN,16X,3(I8,8X) 형식으로 IG의 정수 3개를 읽는다(6). 해석: IG는 온도(temperature) 지정 절점 번호이다. I=1..3에서 첫 0 앞까지 N_TMP를 늘린다(8–11). 원문: `      SUBROUTINE CT_TEMP( N_TMP, CHAR )` (1); `      CHARACTER*80 CHAR` (3); `      DIMENSION IG(3)` (4); `      READ(CHAR,'(BN,16X,3(I8,8X))') IG(:)` (6); `      DO I = 1, 3` (8); `        IF( IG(I) == 0 ) EXIT` (9); `        N_TMP = N_TMP + 1` (10); `      ENDDO` (11); `      END` (13). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
