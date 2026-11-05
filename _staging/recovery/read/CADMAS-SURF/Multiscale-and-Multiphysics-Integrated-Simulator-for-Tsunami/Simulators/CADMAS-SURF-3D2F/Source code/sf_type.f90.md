---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_type.f90
lines: 10
sha256: ba25129bdcea1affdc48a1d29d4661dc2e951936205d0c1f1e8bd0fea3f97aa9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_type.f90 — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | SF_TYPE 모듈에 SPACE 파생 형식(derived type)을 정의한다. 정수 IFIX·N, 할당 가능한 정수 ID(:,:)와 배정밀도 P(:,:)를 선언한다(1–10). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `MODULE SF_TYPE` (1)<br>`  TYPE SPACE` (3)<br>`    INTEGER :: IFIX` (4)<br>`    INTEGER :: N` (5)<br>`    INTEGER, ALLOCATABLE :: ID(:,:)` (6)<br>`    REAL(8), ALLOCATABLE :: P(:,:)` (7)<br>`  END TYPE SPACE` (8)<br>`END MODULE SF_TYPE` (10) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–8: SPACE의 IFIX·N 선언에는 기본값 대입이 없다.
