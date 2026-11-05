---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/trnsmtx7.f
lines: 28
sha256: 4c054970efa3abd2497cc8a69fcb18d490833fcbb167f361db08dc99ace44958
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# trnsmtx7.f — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | TRNSMTX7 입구와 배열 선언이다(1–5). KN(1:3)과 KN(4:6)의 대응 GRID 열을 평균하여 X에 대입한다(7). 이 식은 어느 쪽이 위 또는 아래인지 지정하지 않는다. 중점 차 벡터로 DIRCOS·CROSS2를 호출한 뒤 E를 전치하여 TE에 넣는다(9–20). 해석: E를 기저로 보는 설명은 호출 이름과 인수에 따른 해석이다. 첫 중점을 원점으로 여섯 좌표를 이동하고 AXB로 GE를 계산한다(22–26). 원문: `      SUBROUTINE TRNSMTX7(TE,GE,GRID,KN)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,3),GRID(3,*),KN(6),V12(3),V13(3),E(3,3),TE(3,3)`<br>`     &          ,GG(3,6),GE(3,6)` (4–5); `      X(:,:) = ( GRID(:,KN(1:3)) + GRID(:,KN(4:6)) ) * .5D0` (7); `      V12(:) = X(:,2) - X(:,1)` (9); `      V13(:) = X(:,3) - X(:,1)` (10); `      CALL DIRCOS(E(1,1),V12,3)` (12); `      CALL CROSS2(E(1,1),V13,E(1,3))` (13); `      CALL CROSS2(E(1,3),E(1,1),E(1,2))` (14); `      DO I=1,3` (16); `        DO J=1,3` (17); `          TE(I,J)=E(J,I)` (18); `        ENDDO` (19); `      ENDDO` (20); `      DO I=1,6` (22); `        GG(:,I) = GRID(:,KN(I)) - X(:,1)` (23); `      ENDDO` (24); `      CALL AXB(GE,TE,GG,3,3,6)` (26); `      END` (28) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
