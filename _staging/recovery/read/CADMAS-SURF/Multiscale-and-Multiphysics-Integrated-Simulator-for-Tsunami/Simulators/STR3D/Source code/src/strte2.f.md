---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/strte2.f
lines: 23
sha256: c9b68fb5d33051bad3a389d713f7395941f8733c3661d956ee74520d33f52997
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# strte2.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | STRTE2 입구와 IMPLICIT·배열·DATA 선언이다(1–5). I=1:4에서는 EPSG(J,I)·SIGG(J,I)의 3배에서 각 배열의 (J,5) 항목의 2배를 뺀다(7–12). I=5:10에서는 II가 지정한 두 항목 합의 1.5배에서 각 배열의 (J,5) 항목의 2배를 뺀다(14–21). 해석: I=1:4를 꼭짓점, EPSG·SIGG 항목을 적분점 값으로 보는 설명은 배열 구조에 따른 해석이다. 원문: `      SUBROUTINE STRTE2(EPS,SIG,EPSG,SIGG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION EPSG(6,5),SIGG(6,5),EPS(6,10),SIG(6,10),II(2,10)` (4); `      DATA II / 8*0,  1,2,  2,3,  3,1,  1,4,  2,4,  3,4 /` (5); `      DO 400 I=1,4` (7); `        DO 410 J=1,6` (8); `          EPS(J,I)=3.D0*EPSG(J,I)-2.D0*EPSG(J,5)` (9); `          SIG(J,I)=3.D0*SIGG(J,I)-2.D0*SIGG(J,5)` (10); `  410   CONTINUE` (11); `  400 CONTINUE` (12); `      DO 500 I=5,10` (14); `        DO 510 J=1,6` (15); `          EPS(J,I)=1.5D0*( EPSG(J,II(1,I)) + EPSG(J,II(2,I)) )`<br>`     &            -2.D0*EPSG(J,5)` (16–17); `          SIG(J,I)=1.5D0*( SIGG(J,II(1,I)) + SIGG(J,II(2,I)) )`<br>`     &            -2.D0*SIGG(J,5)` (18–19); `  510   CONTINUE` (20); `  500 CONTINUE` (21); `      END` (23) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
