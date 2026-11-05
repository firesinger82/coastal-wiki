---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/harfc.f
lines: 30
sha256: e387a97c73244b70219cd9bc81c7336b03cb4e67960a20257535f54c22b5397a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# harfc.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | HARFC는 A=B*C에서 C가 압축 저장(packed storage) 행렬이라는 주석을 갖는다(1–3). 암시적 형과 A(N1,N2)·B(N1,N2)·C(*)를 선언한다(5–6). 구분 주석을 포함한다. 원문: `      SUBROUTINE  HARFC( A,B,C, N1,N2 )` (1); `C     A = B X C  ( C MATRIX IS HARF MATRIX )` (3); `      IMPLICIT REAL*8 (A-H,O-Z)` (5); `      DIMENSION  A(N1,N2),B(N1,N2),C(*)` (6). |
| 8–30 | 시작 시 1행 HARFC 루틴 안. I=1..N1, J=1..N2에서 A(I,J)를 0으로 두고 K=1..N2를 순회한다(8–11). K<=J 여부로 IROW·ICOL에 작은 첨자와 큰 첨자를 배치한다(13–19). IP를 계산하고 B(I,K)*C(IP)를 누적한다(21–23). 루프 종료·주석·RETURN·END를 포함한다. 원문: `      DO 100 I=1,N1` (8); `        DO 200 J=1,N2` (9); `          A(I,J)=0.` (10); `          DO 300 K=1,N2` (11); `            IF(K .LE. J) THEN` (13); `              IROW=K` (14); `              ICOL=J` (15); `            ELSE` (16); `              IROW=J` (17); `              ICOL=K` (18); `            ENDIF` (19); `            IP=(2*N2-IROW+2)*(IROW-1)/2+ICOL-IROW+1` (21); `            A(I,J)=A(I,J)+B(I,K)*C(IP)` (23); `  300     CONTINUE` (25); `  200   CONTINUE` (26); `  100 CONTINUE` (27); `      RETURN` (29); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
