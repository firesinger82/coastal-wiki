---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/strhx1.f
lines: 29
sha256: fe206b43aba0a7853459ec694b6f8ec5a6ae33ff115feef3d58938ffda509d62
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# strhx1.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | STRHX1 입구와 IMPLICIT·배열·INCLUDE·DATA 선언이다(1–9). TRNSMTX3·CHTNSR를 차례로 호출한다(11–12). MEAN3을 EPSG와 SIGG에 대해 호출한다(14–15). FAC에 XG(2,2)의 역수를 대입한다(17). I=1:8에서 IG가 지정한 II·JJ·KK를 RMULT5 인수의 첨자로 사용한다(19–24). 이어서 ATXB를 두 번 호출한다(25–26). 해석: 이 호출 순서는 적분점 평균과 대응 적분점 값의 외삽 및 텐서 변환으로 볼 수 있다. 원문: `      SUBROUTINE STRHX1(EPS0,SIG0,EPSG,SIGG,GRID,KN)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XYZ(3,8),GRID(3,*),KN(8),TE(3,3),TE1(6,6),TE2(6,6)`<br>`     &         ,EPS(6),SIG(6),EPS0(6,8),SIG0(6,8),EPSEL(6),SIGEL(6)`<br>`     &         ,EPSG(6,2,2,2),SIGG(6,2,2,2),IG(3,8)` (4–6); `      INCLUDE 'gauss_ln_3.h'` (7); `      DATA IG / 1,1,1, 2,1,1, 2,2,1, 1,2,1,`<br>`     &          1,1,2, 2,1,2, 2,2,2, 1,2,2 /` (8–9); `      CALL TRNSMTX3(8,KN,GRID,TE,XYZ)` (11); `      CALL CHTNSR(TE,TE1,TE2)` (12); `      CALL MEAN3(EPSEL,EPSG,6,8)` (14); `      CALL MEAN3(SIGEL,SIGG,6,8)` (15); `      FAC=1.D0/XG(2,2)` (17); `      DO 300 I=1,8` (19); `        II=IG(1,I)` (20); `        JJ=IG(2,I)` (21); `        KK=IG(3,I)` (22); `        CALL RMULT5( EPS, 1.-FAC, EPSEL, FAC, EPSG(1,II,JJ,KK), 6 )` (23); `        CALL RMULT5( SIG, 1.-FAC, SIGEL, FAC, SIGG(1,II,JJ,KK), 6 )` (24); `        CALL ATXB(EPS0(1,I),TE1,EPS,6,6,1)` (25); `        CALL ATXB(SIG0(1,I),TE2,SIG,6,6,1)` (26); `  300 CONTINUE` (27); `      END` (29) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·17: INCLUDE 문은 gauss_ln_3.h를 지정한다. FAC는 XG(2,2)의 역수이다. 포함 파일 내부는 이번 판독 대상에 포함하지 않았다. [11-04 전수 검증 정정]
