---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/trnsmtx3.f
lines: 45
sha256: 92db0f1a819951f4a8db7a3ef78f230330259940c5887870364494d33da09468
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# trnsmtx3.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | TRNSMTX3 입구와 배열 선언이다(1–6). KN(1·4·5·8), KN(2·3·6·7), KN(1·2·5·6), KN(4·3·8·7)의 GRID 성분 평균을 각각 CENTER1:4에 대입한다(11–20). 해석: 이 네 평균을 면 중심으로 볼 수 있다. SUBVEC·DIRCOS·CROSS2를 호출한 뒤 E를 전치하여 TE를 만든다(22–32). 해석: E를 두 중심 차에서 구성한 기저로 볼 수 있다. 두 중심의 평균을 기준으로 ND개 절점 좌표를 옮기고 AXB로 GE를 계산한다(34–42). 원문: `      SUBROUTINE TRNSMTX3(ND,KN,GRID,TE,GE)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GG(3,20),GRID(3,*),E(3,3),TE(3,3),GE(3,ND),KN(ND)`<br>`     &         ,V12(3),V34(3),CENTER(3),CENTER1(3),CENTER2(3)`<br>`     &         ,CENTER3(3),CENTER4(3)` (4–6); `      DO 500 I=1,3` (11); `        CENTER1(I) = ( GRID(I,KN(1)) + GRID(I,KN(4)) + GRID(I,KN(5))`<br>`     &               + GRID(I,KN(8)) ) * 0.25` (12–13); `        CENTER2(I) = ( GRID(I,KN(2)) + GRID(I,KN(3)) + GRID(I,KN(6))`<br>`     &               + GRID(I,KN(7)) ) * 0.25` (14–15); `        CENTER3(I) = ( GRID(I,KN(1)) + GRID(I,KN(2)) + GRID(I,KN(5))`<br>`     &               + GRID(I,KN(6)) ) * 0.25` (16–17); `        CENTER4(I) = ( GRID(I,KN(4)) + GRID(I,KN(3)) + GRID(I,KN(8))`<br>`     &               + GRID(I,KN(7)) ) * 0.25` (18–19); `  500 CONTINUE` (20); `      CALL SUBVEC(V12,CENTER2,CENTER1,3)` (22); `      CALL SUBVEC(V34,CENTER4,CENTER3,3)` (23); `      CALL DIRCOS(E(1,1),V12,3)` (24); `      CALL CROSS2(E(1,1),V34,E(1,3))` (25); `      CALL CROSS2(E(1,3),E(1,1),E(1,2))` (26); `      DO 100 I=1,3` (28); `        DO 110 J=1,3` (29); `          TE(I,J)=E(J,I)` (30); `  110   CONTINUE` (31); `  100 CONTINUE` (32); `      DO 400 I=1,3` (34); `        CENTER(I) = ( CENTER1(I) + CENTER2(I) ) * 0.5` (35); `  400 CONTINUE` (36); `      DO 200 I=1,ND` (38); `        CALL SUBVEC(GG(1,I),GRID(1,KN(I)),CENTER,3)` (39); `  200 CONTINUE` (40); `      CALL AXB(GE,TE,GG,3,3,ND)` (42); `      RETURN` (44); `      END` (45) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·11–19·38–39: KN의 선언 크기는 ND이다. CENTER1:4 계산은 KN(8)까지 참조하며, GG의 두 번째 차원은 20으로 고정되어 있다. [11-04 전수 검증 정정]
