---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mean1.f
lines: 26
sha256: 3c0a7add5d1a96e8ece33f082e98e43401fb32c12395a955edbbc9c60429b414
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mean1.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | SF_MEAN1 선언과 X(N) 범위(1–5). I=2:N에서 앞쪽 원소와 비교하여 더 작은 XX를 찾으면 슬라이스를 한 칸 밀어 삽입하고 EXIT한다(7–16). XM=0부터 정렬된 X를 합산하여 DBLE(N)으로 나누는 산술평균(arithmetic mean)을 계산한다(18–24). 원문: `      SUBROUTINE SF_MEAN1(XM,X,N)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION X(N)` (5)<br>`      DO I = 2, N` (7)<br>`        XX = X(I)` (8)<br>`        DO J = 1, I - 1` (9)<br>`          IF( XX < X(J) ) THEN` (10)<br>`            X(J+1:I) = X(J:I-1)` (11)<br>`            X(J) = XX` (12)<br>`            EXIT` (13)<br>`          ENDIF` (14)<br>`        ENDDO` (15)<br>`      ENDDO` (16)<br>`      XM = 0.` (18)<br>`      DO I = 1, N` (20)<br>`        XM = XM + X(I)` (21)<br>`      ENDDO` (22)<br>`      XM = XM / DBLE(N)` (24)<br>`      END` (26) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–16: 평균 계산 전에 인수 배열 X를 오름차순으로 재배치한다.
- 24: DBLE(N)으로 나누기 전에 N>0 검사는 이 파일에 없다.
