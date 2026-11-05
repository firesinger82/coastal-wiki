---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_fill.f
lines: 26
sha256: 9ec4d4195a5a9561a7a6815c7b18e843e2753facea4fe018fa6813050f1bacfa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_fill.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | SF_FILL 선언과 GGF(6) 범위(1–4). FZ를 DZ·H의 최솟값으로 정하여 H에서 뺀다(6–8). FZ=DZ이면 GGW=0, 그 밖에는 1-FZ/DZ이다(10–14). POR를 이용해 GGV를 계산하고 GGF(1:4)에 복사한다(16–18). GGF(5)는 POR이다(19). GGF(6)는 FZ=DZ일 때 POR이고 그 밖에는 1이다(20–24). 해석: POR는 공극률이고 GGF(5)·GGF(6)는 각각 아래쪽·위쪽 면의 값이다. 원문: `      SUBROUTINE SF_FILL(H,GGW,GGV,GGF,DZ,POR)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION GGF(6)` (4)<br>`      FZ = DMIN1(DZ,H)` (6)<br>`      H = H - FZ` (8)<br>`      IF( FZ == DZ ) THEN` (10)<br>`        GGW = 0.D0` (11)<br>`      ELSE` (12)<br>`        GGW = 1.D0 - FZ / DZ` (13)<br>`      ENDIF` (14)<br>`      GGV = 1.D0 - FZ / DZ * ( 1.D0 - POR )` (16)<br>`      GGF(1:4) = GGV` (18)<br>`      GGF(5) = POR` (19)<br>`      IF( FZ == DZ ) THEN` (20)<br>`        GGF(6) = POR` (21)<br>`      ELSE` (22)<br>`        GGF(6) = 1.D0` (23)<br>`      ENDIF` (24)<br>`      END` (26) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–16: FZ는 DMIN1(DZ,H)로만 제한한다. 이 파일에는 H>=0 또는 DZ>0 검사가 없다.
