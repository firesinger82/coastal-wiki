---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_icopy.f
lines: 7
sha256: 435c7c3dab243cabb78f168b351f5c4c744d0f86f0f8dd16f3eaed06f693e9e5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_icopy.f — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | SF_ICOPY 선언과 IA(N)·IB(N) 정수 배열 범위(1–3). 배열 전체 대입으로 IB를 IA에 복사한다(5). 원문: `      SUBROUTINE SF_ICOPY(IA,IB,N)` (1)<br>`      DIMENSION IA(N),IB(N)` (3)<br>`      IA = IB` (5)<br>`      END` (7) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
