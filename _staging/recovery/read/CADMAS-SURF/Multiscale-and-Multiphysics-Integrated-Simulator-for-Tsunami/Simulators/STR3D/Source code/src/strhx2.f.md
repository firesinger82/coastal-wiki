---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/strhx2.f
lines: 22
sha256: 5a340cbe26422ee64532c07525e653ddc5bbfb673d7fccdcba172a6efb652557
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# strhx2.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | STRHX2 입구와 IMPLICIT·배열·INCLUDE·DATA 선언이다(1–10). XG(3,3)의 역수로 계수를 정한다(12). I=1:20에서 EPSG(:,2,2,2)·SIGG(:,2,2,2)와 IG가 지정한 항목의 선형 결합으로 EPS·SIG를 계산한다(14–20). 해석: 두 항목을 중앙 적분점과 대응 적분점으로 보는 것은 배열 구조에 따른 해석이다. 원문: `      SUBROUTINE STRHX2(EPS,SIG,EPSG,SIGG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION EPSG(6,3,3,3),SIGG(6,3,3,3),EPS(6,20),SIG(6,20),IG(3,20)` (4); `      INCLUDE 'gauss_ln_3.h'` (5); `      DATA IG / 1,1,1, 3,1,1, 3,3,1, 1,3,1,`<br>`     &          1,1,3, 3,1,3, 3,3,3, 1,3,3,`<br>`     &          2,1,1, 3,2,1, 2,3,1, 1,2,1,`<br>`     &          1,1,2, 3,1,2, 3,3,2, 1,3,2,`<br>`     &          2,1,3, 3,2,3, 2,3,3, 1,2,3 /` (6–10); `      FAC = 1.D0 / XG(3,3)` (12); `      DO I = 1, 20` (14); `        II = IG(1,I)` (15); `        JJ = IG(2,I)` (16); `        KK = IG(3,I)` (17); `        EPS(:,I) = (1.D0 - FAC) * EPSG(:,2,2,2) + FAC * EPSG(:,II,JJ,KK)` (18); `        SIG(:,I) = (1.D0 - FAC) * SIGG(:,2,2,2) + FAC * SIGG(:,II,JJ,KK)` (19); `      ENDDO` (20); `      END` (22) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·12: INCLUDE 문은 gauss_ln_3.h를 지정한다. FAC는 XG(3,3)의 역수이다. 포함 파일 내부는 이번 판독 대상에 포함하지 않았다. [11-04 전수 검증 정정]
