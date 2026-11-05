---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/stfgl.f
lines: 73
sha256: 62740fe81917151e4d9947fc860825056a426541333ae54aa889f9e379836ac5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# stfgl.f — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | STFGL 입구와 일본어 인수 설명이다(1–8). ESTF를 국소 좌표계에서 전역 좌표계로 변환한다. IMPLICIT·배열을 선언하고 ST를 0으로 초기화한다(10–16). 원문: `      SUBROUTINE STFGL(ESTF,ST,T,N,NDIM)` (1); 주석: `C     ESTF : IN   : 要素剛性行列(local座標系)` (3) (요소 강성행렬, 국소 좌표계(local coordinate system)); 주석: `C            OUT  : 要素剛性行列(global座標系)` (4) (요소 강성행렬, 전역 좌표계(global coordinate system)); 주석: `C     ST   : WORK : ワーク` (5) (작업공간); 주석: `C     T    : IN   : global -> local 座標変換行列` (6) (전역 좌표계에서 국소 좌표계로의 좌표변환행렬(transformation matrix)); 주석: `C     N    : IN   : ESTFの行(列)サイズ` (7) (ESTF의 행 또는 열 크기); 주석: `C     NDIM : IN   : 解析次元(2 or 3)` (8) (해석 차원, 2 또는 3); `      IMPLICIT REAL*8 (A-H,O-Z)` (10); `      DIMENSION  ESTF(1),ST(N,N),T(NDIM,NDIM)` (11); 주석: `C--- 0 CLEAR ---` (14); `      NNN = N * N` (15); `      CALL CLEAR1( ST,NNN )` (16) 3–4행의 `要素剛性行列`은 요소 강성행렬이다. 5행의 `ワーク`는 작업 공간이다. 6행은 T가 global에서 local로 가는 좌표변환행렬임을 뜻한다. 7행은 N이 ESTF의 행 또는 열 크기임을 뜻한다. 8행은 NDIM이 해석 차원 2 또는 3임을 뜻한다. [11-04 전수 검증 보완] |
| 19–53 | 시작 시 STFGL 루틴(1) 안이다. 압축 대칭행렬 ESTF의 주소를 I·JL 비교로 구하고 ESTF와 T의 곱을 작업 배열 ST에 누적한다(19–51). 원문: 주석: `C--- ESTF X T ---` (19); `      IR   = N` (20); `      LAST = 0` (21); `      DO 4000 I=1,N` (22); `         IIC  = 0` (23); `         LP   = 0` (24); `      DO 3000 J=1,N,NDIM` (26); `         DO 2000 K=1,NDIM` (28); `            IC       = IIC` (29); `            JK       = J + K - 1` (30); `         DO 1000 L=1,NDIM` (32); `            JL = J + L - 1` (33); `            IF( I .LE. JL )  THEN` (34); `                IAD = LAST + JL - I + 1` (35); `             ELSE` (36); `                IAD = I  + IC` (37); `                IC  = IC + N - L - LP` (38); `            ENDIF` (39); `            ST(I,JK) = ST(I,JK) + ESTF(IAD)*T(L,K)` (41); ` 1000    CONTINUE` (43); ` 2000    CONTINUE` (44); `            IIC = IC` (45); `            LP  = LP + NDIM` (46); ` 3000 CONTINUE` (48); `         LAST = LAST + IR` (49); `         IR   = IR - 1` (50); ` 4000 CONTINUE` (51) |
| 54–73 | 시작 시 STFGL 루틴(1) 안이다. T 전치와 ST를 곱해 압축 저장 ESTF에 누적한다(54–69). 원문: 주석: `C--- TT X ESTF X T ---` (54); `      IAD = 0` (55); `      DO 8000 I=1,N` (56); `         I3 = I - (I-1)/NDIM * NDIM` (57); `         II = (I-1)/NDIM * NDIM` (58); `      DO 7000 J=I,N` (60); `         IAD       = IAD + 1` (61); `         ESTF(IAD) = 0.0D0` (62); `         DO 6000 K=1,NDIM` (64); `            ESTF(IAD) = ESTF(IAD) + T(K,I3)*ST(II+K,J)` (65); ` 6000    CONTINUE` (66); ` 7000 CONTINUE` (68); ` 8000 CONTINUE` (69); `      RETURN` (72); `      END` (73) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·35–41·61–65: ESTF는 ESTF(1)로 선언한다. 실행문에서는 계산한 IAD를 첨자로 사용한다.
