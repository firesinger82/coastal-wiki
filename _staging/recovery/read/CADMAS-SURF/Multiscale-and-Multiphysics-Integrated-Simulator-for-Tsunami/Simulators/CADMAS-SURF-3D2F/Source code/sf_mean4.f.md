---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mean4.f
lines: 14
sha256: 5e6683f41ad844a4b6c22df46a7a98acf7b0f9b9c2f82d29ba547362c72f93e1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mean4.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SF_MEAN4 선언과 A(N)·B(N,*)·IDX(M) 범위(1–4). A=0부터 IDX의 M개 열을 합산하고 DBLE(M)으로 나누어 성분별 산술평균(arithmetic mean)을 구한다(6–12). 원문: `      SUBROUTINE SF_MEAN4(A,B,N,IDX,M)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION A(N),B(N,*),IDX(M)` (4)<br>`      A(:) = 0.` (6)<br>`      DO I = 1, M` (8)<br>`        A(:) = A(:) + B(:,IDX(I))` (9)<br>`      ENDDO` (10)<br>`      A(:) = A(:) / DBLE(M)` (12)<br>`      END` (14) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12: DBLE(M)으로 나누기 전에 M>0 검사는 이 파일에 없다.
