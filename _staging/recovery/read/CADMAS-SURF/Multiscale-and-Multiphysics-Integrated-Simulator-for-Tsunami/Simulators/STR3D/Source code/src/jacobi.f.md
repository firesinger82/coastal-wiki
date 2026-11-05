---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/jacobi.f
lines: 89
sha256: 89129c412bde610bd854145cc75fd89b4b29000c786099c4ea447edd3378ef3a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# jacobi.f — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | JACOBI의 배열 선언과 영어 인수 설명이다. 대칭행렬(symmetric matrix)의 고유값(eigenvalue)과 열별 고유벡터(eigenvector)를 구한다. V를 단위행렬로 초기화한다. 원문: `      SUBROUTINE JACOBI(A,E,V,N,M,FAC,I9,ND,K,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION A(ND,ND),E(ND),V(ND,ND)` (5)； `C      JACOBI EIGENVALUE SUBR` (7)； `C      A      SYMMETRIC MATRIX TO BE SOLVED` (9)； `C      E      EIGENVALUE                             (OUTPUT)` (10)； `C      V      EIGENVECTOR (COLUMNWISE MODE)          (OUTPUT)` (11)； `C      M      MAX ITERATION CYCLE` (12)； `C      FAC    CONVERGENCE FACTOR` (13)； `C      I9     DEBUG WRITE OPTION` (14)； `C      K      ACTUAL ITERATION CYCLE FOR CONVERGENCE (OUTPUT)` (15)； `      DO 2000 I=1,N` (17)； `      DO 1700 J=1,N` (18)； ` 1700 V(I,J)=0.0D0` (19)； ` 2000 V(I,I)=1.0D0` (20)。 |
| 22–55 | 시작 시 1행 JACOBI 루틴 안이다. K 반복에서 절댓값이 가장 큰 비대각 원소의 위치 IP·IQ를 찾는다. FAC보다 작으면 7200으로 이동한다. I9에 따라 중간 값을 출력한다. 두 대각값이 같으면 48행 레이블 5000으로 이동하여 고정 각도를 쓴다. 같지 않으면 44–45행에서 DATAN으로 회전 각도(rotation angle)를 구한다. 이 분기는 ELSE 문 없이 조건부 GOTO와 무조건 GOTO로 구성된다. 원문: `      DO 7000 K=1,M` (22)； `      IF(I9.EQ.0) GO TO 3500` (23)； ` 3500 IP=1` (26)； `      IQ=2` (27)； `      NM=N-1` (28)； `      DO 4100 I=1,NM` (29)； `      IR=I+1` (30)； `      DO 4000 J=IR,N` (31)； `      IF(DABS(A(I,J)).LE.DABS(A(IP,IQ))) GO TO 4000` (32)； `      IP=I` (33)； `      IQ=J` (34)； ` 4000 CONTINUE` (35)； ` 4100 CONTINUE` (36)； `      IF(DABS(A(IP,IQ)).LT.FAC) GO TO 7200` (38)； `      IF(I9.EQ.0) GO TO 4500` (40)； `      WRITE(ITO,4209) K,IP,IQ` (41)； ` 4209 FORMAT(' ITERATION=',I4,'  P AND Q=',2I5)` (42)； ` 4500 IF(A(IP,IP).EQ.A(IQ,IQ)) GO TO 5000` (43)； `      R=2.0D0*A(IP,IQ)/(A(IP,IP)-A(IQ,IQ))` (44)； `      T=0.5D0*DATAN(R)` (45)； `      GO TO 5500` (46)； ` 5000 T=0.78539818D0` (48)； ` 5500 IF(I9.EQ.0) GO TO 6000` (50)； `      WRITE(ITO,5509) T` (51)； ` 5509 FORMAT(' T=',E13.5)` (52)； ` 6000 S=DSIN(T)` (53)； `      C=DCOS(T)` (54)。 [11-04 전수 검증 정정] |
| 56–89 | 시작 시 1행 JACOBI 루틴과 22행 `DO 7000 K=1,M` 안이다. 이 바깥 루프는 79행 `7000 CONTINUE`에서 닫힌다. 먼저 행 방향 회전으로 A를 바꾼다. 다음 I 루프에서 열 방향 A와 V를 회전한다. 7000은 I 루프와 K 루프의 공통 종료 표지이다. 81행 레이블 7200에서 대각 원소를 E로 옮긴다. 84행 주석은 내림차순 재배열을 명시한다. 86행은 ORDRNF를 호출한다. 원문: `C      HALF NEW A=P*A` (56)； `      DO 6500 J=1,N` (58)； `      A1=A(IP,J)` (59)； `      A2=A(IQ,J)` (60)； `      A(IP,J)= A1*C+A2*S` (61)； `      A(IQ,J)=-A1*S+A2*C` (62)； ` 6500 CONTINUE` (63)； `C      NEW A=P*A*Q` (65)； `      DO 7000 I=1,N` (67)； `      A1=A(I,IP)` (68)； `      A2=A(I,IQ)` (69)； `      A(I,IP)= A1*C+A2*S` (70)； `      A(I,IQ)=-A1*S+A2*C` (71)； `C      NEW X=X*Q` (73)； `      V1=V(I,IP)` (75)； `      V2=V(I,IQ)` (76)； `      V(I,IP)= V1*C+V2*S` (77)； `      V(I,IQ)=-V1*S+V2*C` (78)； ` 7000 CONTINUE` (79)； ` 7200 DO 7500 I=1,N` (81)； ` 7500 E(I)=A(I,I)` (82)； `C      REARRANGE INTO DESCENDING ORDER` (84)； `      CALL ORDRNF(E,V,N,ND)` (86)； `      RETURN` (88)； `      END` (89)。 [11-04 전수 검증 보완] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–27·38: IP=1·IQ=2를 설정한 뒤 A(IP,IQ)를 참조한다. N < 2를 검사하는 조건은 이 파일에 없다.
- 48: 대각값이 같은 경우의 각도는 0.78539818D0로 고정한다.
- 22·79–86: 반복 상한에 도달한 뒤 별도 비수렴 오류 분기 없이 E를 만들고 ORDRNF를 호출한다.
