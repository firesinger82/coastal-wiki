---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/shiftb0.f
lines: 10
sha256: 46917b94ca1eebd9c7e32e2392705a1a191534b3384279abe45f4972dd398753
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# shiftb0.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | SHIFTB0의 인수와 IA(*)를 선언한다(1–3). I를 IE부터 IS까지 간격 -1로 순회하며 IA(I)를 IA(I+N)에 복사한다(5–7). 구분 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE SHIFTB0(IA,IS,IE,N)` (1); `      DIMENSION IA(*)` (3); `      DO I=IE,IS,-1` (5); `        IA(I+N)=IA(I)` (6); `      ENDDO` (7); `      RETURN` (9); `      END` (10). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
