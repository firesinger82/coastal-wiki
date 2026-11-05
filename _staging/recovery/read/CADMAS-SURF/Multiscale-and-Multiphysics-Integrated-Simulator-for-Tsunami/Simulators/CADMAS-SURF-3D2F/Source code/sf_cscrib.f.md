---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cscrib.f
lines: 15
sha256: ba247afa9ac16721b4ecb6bd48e05eb051c0eb4676091f384bac1ac4255ef634
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cscrib.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | SF_CSCRIB 선언과 X(2,3)·XG(2) 배열 범위(1–4). 세 꼭짓점 좌표의 평균을 XG에 넣는다(6). RMAX=0부터 세 꼭짓점과 XG의 거리를 SF_LENGTH로 구하여 최댓값을 남긴다(8–13). 원문: `      SUBROUTINE SF_CSCRIB(XG,RMAX,X)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION X(2,3),XG(2)` (4)<br>`      XG(:) = ( X(:,1) + X(:,2) + X(:,3) ) / 3.D0` (6)<br>`      RMAX = 0.` (8)<br>`      DO I = 1, 3` (10)<br>`        CALL SF_LENGTH(R,X(1,I),XG,2)` (11)<br>`        IF( R > RMAX ) RMAX = R` (12)<br>`      ENDDO` (13)<br>`      END` (15) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
