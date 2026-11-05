---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/clear0.f
lines: 22
sha256: e9e41b72de8c7c814750b4f3eb15f2f605d8255eeebc0cfbcfa24a8d6644012e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# clear0.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | CLEAR0는 정수 배열의 0 초기화를 수행한다는 영문 주석을 갖는다(2–7). IT(N)을 선언한다(10). 구분선·빈 주석을 포함한다. 원문: `      SUBROUTINE  CLEAR0( IT,N )` (2); `C  0 CLEAR OF INTEGER TABLE` (4); `C  IT     = CLEAR TABLE                                   --- ( O )` (6); `C  N      = NUMBER OF IT TABLE                            --- ( I )` (7); `      DIMENSION  IT(N)` (10). |
| 13–22 | 시작 시 2행 CLEAR0 루틴 안. N이 0 이하이면 즉시 반환한다(13). 그 외 I=1..N 루프에서 IT(I)를 0으로 설정한다(16–18). RETURN·END까지 포함한다. 원문: `      IF( N .LE. 0 )  RETURN` (13); `C--- 0 CLEAR ---` (15); `      DO 1000 I=1,N` (16); `         IT(I) = 0` (17); ` 1000 CONTINUE` (18); `      RETURN` (21); `      END` (22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
