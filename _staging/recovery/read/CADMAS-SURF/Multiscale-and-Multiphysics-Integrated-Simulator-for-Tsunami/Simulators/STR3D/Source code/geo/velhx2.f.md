---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/velhx2.f
lines: 36
sha256: 09141c1a089fde5dacd42e7500dd8f0fb41535436653274d1d0106d1a2149296
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# velhx2.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | VELHX2는 VELG와 VELE로 VEL을 계산한다. 해석: 루틴 이름과 대응 표는 육면체(hexahedron)의 적분점 값을 절점으로 외삽(extrapolation)하는 용도로 보인다. 실수 IMPLICIT와 배열 범위는 아래와 같다. XG 적분 좌표 및 8절점 IG1·20절점 IG2의 대응 표를 DATA 연속문 전체로 인용한다. FAC는 XG(NG,NG)의 역수이다. 원문: `      SUBROUTINE VELHX2(VEL,VELG,VELE,ND,NG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XG(3,3),IG1(3,8),IG2(3,20),VELG(3,NG,NG,NG),VELE(3)` (4); `     &         ,VEL(3,ND)` (5); `      DATA XG / 3*0.0D0` (7); `     &        , -.577350269189626D0, .577350269189626D0, 0.0D0` (8); `     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (9); `      DATA IG1 / 1,1,1, 2,1,1, 2,2,1, 1,2,1,` (10); `     &           1,1,2, 2,1,2, 2,2,2, 1,2,2 /` (11); `      DATA IG2 / 1,1,1, 3,1,1, 3,3,1, 1,3,1,` (12); `     &           1,1,3, 3,1,3, 3,3,3, 1,3,3,` (13); `     &           2,1,1, 3,2,1, 2,3,1, 1,2,1,` (14); `     &           1,1,2, 3,1,2, 3,3,2, 1,3,2,` (15); `     &           2,1,3, 3,2,3, 2,3,3, 1,2,3 /` (16); `      FAC = 1.D0 / XG(NG,NG)` (18) [11-04 전수 검증 정정] |
| 20–36 | 절점 I=1,ND에서 ND=8이면 IG1, ELSE는 IG2로 적분점 첨자 II·JJ·KK를 얻는다. VELE에 1-FAC, VELG(:,II,JJ,KK)에 FAC를 곱해 VEL(:,I)를 계산한다. VELE의 중심점 값 계산 근거는 `geo/gnpfhx2.f:57–78`이다. 원문: `      DO I = 1, ND` (20); `        IF( ND == 8 ) THEN` (22); `          II = IG1(1,I)` (23); `          JJ = IG1(2,I)` (24); `          KK = IG1(3,I)` (25); `        ELSE` (26); `          II = IG2(1,I)` (27); `          JJ = IG2(2,I)` (28); `          KK = IG2(3,I)` (29); `       ENDIF` (30); `        VEL(:,I) = ( 1.D0 - FAC ) * VELE(:) + FAC * VELG(:,II,JJ,KK)` (32); `      ENDDO` (34); `      END` (36) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18: FAC는 XG(NG,NG)로 나눈다. 이 파일에는 NG의 범위 및 분모의 0 검사문이 없다.
- 22–30: ND=8 이외의 모든 값은 20열 IG2 표를 사용한다.
