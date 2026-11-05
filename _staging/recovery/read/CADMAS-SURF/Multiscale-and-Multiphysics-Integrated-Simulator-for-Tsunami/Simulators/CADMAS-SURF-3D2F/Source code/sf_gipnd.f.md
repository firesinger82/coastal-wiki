---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_gipnd.f
lines: 14
sha256: 828aefb05abfdab16fb77910cd12356b186e6f96d2e43f66fa5e8f43e57ad2ac
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_gipnd.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SF_GIPND 선언과 IPGRID(2,NNOD)·IPND(NNOD) 범위(1–3). I=1:NNOD에서 IPGRID(1,I)>0이면 IPND=1로 둔다(5–7). 그 밖에는 첫 지표를 복사하며 두 번째 지표가 1이면 IPND=2로 덮어쓴다(8–11). 원문: `      SUBROUTINE SF_GIPND(IPND,IPGRID,NNOD)` (1)<br>`      DIMENSION IPGRID(2,NNOD),IPND(NNOD)` (3)<br>`      DO I = 1, NNOD` (5)<br>`        IF( IPGRID(1,I) > 0 ) THEN` (6)<br>`          IPND(I) = 1` (7)<br>`        ELSE` (8)<br>`          IPND(I) = IPGRID(1,I)` (9)<br>`          IF( IPGRID(2,I) == 1 ) IPND(I) = 2` (10)<br>`        ENDIF` (11)<br>`      ENDDO` (12)<br>`      END` (14) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
