---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_vecml.f
lines: 24
sha256: 031ec31227e647209195dfad1600000dfbbdefd044a60ec5e169705e8a7af9df
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_vecml.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 두 벡터의 내적(dot product) 계산이라는 영문 목적·인수·작성자 주석(1–14). 암시적 실수와 D1(N)·D2(N)을 선언한다(15–16). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_VECML(D3,D1,D2,N)` (1)<br>`C` (2)<br>`C 1.PURPOSE` (3)<br>`C         INTERIOR PRODUCT FOR TWO VECTOR` (4)<br>`C` (5)<br>`C 3.ARGUMENT` (6)<br>`C   I D1      D VECTOR` (7)<br>`C   I D2      D VECTOR` (8)<br>`C   O D3      D CALCULATED VECTOR` (9)<br>`C   I N       I DIMENSION FOR VECTOR (=3)` (10)<br>`C` (11)<br>`C 8.PROGRAM` (12)<br>`C    KITAGAWA KAZUSHI (1988-03-10)  MI(910708)` (13)<br>`C` (14)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (15)<br>`      DIMENSION D1(N),D2(N)` (16)<br>`C` (17) |
| 18–24 | 시작 시 1행 루틴 안. D3=0에서 시작하여 DO 100 I=1,N으로 곱을 누적하고 반환한다(18–24). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      D3        =  0.` (18)<br>`      DO  100   I  =  1 , N` (19)<br>`          D3    =  D3  +  D1(I)  *  D2(I)` (20)<br>`  100 CONTINUE` (21)<br>`C` (22)<br>`      RETURN` (23)<br>`      END` (24) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–10·18–20: 인수 주석은 D3를 CALCULATED VECTOR, N을 DIMENSION FOR VECTOR (=3)로 적는다. 구현은 스칼라 D3에 N개 곱을 누적한다.
