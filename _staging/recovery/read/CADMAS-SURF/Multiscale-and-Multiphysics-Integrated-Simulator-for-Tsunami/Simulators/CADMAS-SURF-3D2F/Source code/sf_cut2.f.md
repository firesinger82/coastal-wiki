---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cut2.f
lines: 33
sha256: 414f11c5303eae03c6c1388555b4b1dbd54c9fd5ce22ba479e734a820d6c5260
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cut2.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | SF_CUT2 선언과 2차원 삼각형 작업 배열 범위(1–6). DX·DY와 EPSA를 계산한다(8–11). 해석: EPSA는 격자 사각형 면적에 비례하는 허용값이다. SS=0부터 SF_CUT2X를 XG 하한·상한, YG 하한·상한 순서로 호출한다(13–24). 각 단계 결과 수 N1·N2·N3·N4 범위를 중첩 순회한다(16–31). SF_S34가 반환한 S를 SS에 누적한다(26–27). 해석: S는 마지막 삼각형의 면적이다. 원문: `      SUBROUTINE SF_CUT2(SS,P0,XG,YG,EPS)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>연속문: `      DIMENSION P0(2,3),XG(2),YG(2),P1(2,3,2),P2(2,3,2),P3(2,3,2)` (5); `     &         ,P4(2,3,2)` (6)<br>`      DX = XG(2) - XG(1)` (8)<br>`      DY = YG(2) - YG(1)` (9)<br>`      EPSA = DX * DY * 1.D-9` (11)<br>`      SS = 0.` (13)<br>`      CALL SF_CUT2X(N1,P1(1,1,1),P1(1,1,2),P0,XG(1),EPS,EPSA,1,2,1)` (15)<br>`      DO I = 1, N1` (16)<br>연속문: `        CALL SF_CUT2X(N2,P2(1,1,1),P2(1,1,2),P1(1,1,I),XG(2),EPS,EPSA,1` (17); `     &               ,2,2)` (18)<br>`        DO J = 1, N2` (19)<br>연속문: `          CALL SF_CUT2X(N3,P3(1,1,1),P3(1,1,2),P2(1,1,J),YG(1),EPS,EPSA` (20); `     &                 ,2,1,1)` (21)<br>`          DO K = 1, N3` (22)<br>연속문: `            CALL SF_CUT2X(N4,P4(1,1,1),P4(1,1,2),P3(1,1,K),YG(2),EPS` (23); `     &                   ,EPSA,2,1,2)` (24)<br>`            DO L = 1, N4` (25)<br>`              CALL SF_S34(S,P4(1,1,L),3)` (26)<br>`              SS = SS + S` (27)<br>`            ENDDO` (28)<br>`          ENDDO` (29)<br>`        ENDDO` (30)<br>`      ENDDO` (31)<br>`      END` (33) [11-04 전수 검증 정정] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
