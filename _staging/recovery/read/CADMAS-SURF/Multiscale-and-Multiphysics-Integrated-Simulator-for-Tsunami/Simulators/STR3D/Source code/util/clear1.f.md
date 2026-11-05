---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/clear1.f
lines: 23
sha256: b76e42660e00f82e72f3d0d4d8739699db575f28799513b9f2e70a3170cfa5cb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# clear1.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | CLEAR1는 실수 배열의 0 초기화를 수행한다는 영문 주석을 갖는다(2–7). 암시적 형(implicit typing)과 T(N)을 선언한다(10–11). 구분선·빈 주석을 포함한다. 원문: `      SUBROUTINE  CLEAR1( T,N )` (2); `C  0 CLEAR OF REAL TABLE` (4); `C  T      = CLEAR TABLE                                   --- ( O )` (6); `C  N      = NUMBER OF IT TABLE                            --- ( I )` (7); `      IMPLICIT REAL*8 (A-H,O-Z)` (10); `      DIMENSION  T(N)` (11). |
| 14–23 | 시작 시 2행 CLEAR1 루틴 안. N이 0 이하이면 즉시 반환한다(14). 그 외 I=1..N 루프에서 T(I)를 0.0D0으로 설정한다(17–19). 주석·RETURN·END까지 포함한다. 원문: `      IF( N .LE. 0 )  RETURN` (14); `C--- 0 CLEAR ---` (16); `      DO 1000 I=1,N` (17); `         T(I) = 0.0D0` (18); ` 1000 CONTINUE` (19); `      RETURN` (22); `      END` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
