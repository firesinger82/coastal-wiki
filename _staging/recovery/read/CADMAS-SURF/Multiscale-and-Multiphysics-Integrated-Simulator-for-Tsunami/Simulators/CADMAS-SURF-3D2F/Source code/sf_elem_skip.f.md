---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_elem_skip.f
lines: 21
sha256: dbe13d0aa33698ab0dca3c5c6eaaf2cb277806d32645c11a69e0e3dab387f20e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_elem_skip.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | SF_ELEM_SKIP 선언과 배열 범위(1–5). 요소의 x·y 좌표를 모아 축별 최솟값·최댓값을 계산한다(7–13). 요소 경계 상자(bounding box)가 XS:XE·YS:YE 밖이면 ISKIP=1이고, 그 밖에는 0이다(15–19). 경계가 같은 경우는 바깥 조건에 포함되지 않는다. 원문: `      SUBROUTINE SF_ELEM_SKIP(ISKIP,XS,XE,YS,YE,N,NP,GRID)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION X(N),Y(N),NP(N),GRID(3,*)` (5)<br>`      X(:) = GRID(1,NP(:))` (7)<br>`      Y(:) = GRID(2,NP(:))` (8)<br>`      XMIN = MINVAL( X )` (10)<br>`      YMIN = MINVAL( Y )` (11)<br>`      XMAX = MAXVAL( X )` (12)<br>`      YMAX = MAXVAL( Y )` (13)<br>`      IF( XMAX < XS .OR. XMIN > XE .OR. YMAX < YS .OR. YMIN > YE ) THEN` (15)<br>`        ISKIP = 1` (16)<br>`      ELSE` (17)<br>`        ISKIP = 0` (18)<br>`      ENDIF` (19)<br>`      END` (21) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
