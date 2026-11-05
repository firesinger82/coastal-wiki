---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/efrcp.f
lines: 28
sha256: db11981017437d8aca41ed99e94e83d2f6050f58755653caf7d1b276cbd82be1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# efrcp.f — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | EFRCP의 암시적 형(implicit typing)과 배열을 선언한다. KN을 첨자로 사용하여 GRID·PPND의 값을 X·PB에 복사한다. 해석: GRID는 절점좌표이며 PPND는 압력이다. 원문: `      SUBROUTINE EFRCP(FCP,GRID,PPND,KN,ND,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION FCP(3,*),GRID(3,*),PPND(*),KN(ND),X(3,ND),PB(ND)`<br>`     &         ,FP(3,ND)` (4–5); `      X(:,:) = GRID(:,KN(:))` (7); `      PB(:) = PPND(KN(:))` (9). [11-04 전수 검증 정정] |
| 11–24 | 시작 시 1행 EFRCP 루틴 안. ND의 4·10은 EFPTE1·EFPTE2를 호출한다. 6·15는 EFPPN2에 적분점 수 3,2 및 7,3을 전달한다. 8·20은 EFPHX2에 적분점 수 2 및 3을 전달한다. 원문: `      SELECT CASE( ND )` (11); `      CASE( 4 )` (12); `        CALL EFPTE1(FP,X,PB,ITO)` (13); `      CASE( 10 )` (14); `        CALL EFPTE2(FP,X,PB,ITO)` (15); `      CASE( 6 )` (16); `        CALL EFPPN2(FP,ND,3,2,X,PB,ITO)` (17); `      CASE( 15 )` (18); `        CALL EFPPN2(FP,ND,7,3,X,PB,ITO)` (19); `      CASE( 8 ) ` (20); `        CALL EFPHX2(FP,ND,2,X,PB,ITO)` (21); `      CASE( 20 ) ` (22); `        CALL EFPHX2(FP,ND,3,X,PB,ITO)` (23); `      END SELECT` (24). |
| 25–28 | 시작 시 1행 EFRCP 루틴 안. FP를 KN이 가리키는 FCP에 누적하여 조립(assembly)한다. 루틴 끝을 포함한다. 원문: `      FCP(:,KN(:)) = FCP(:,KN(:)) + FP(:,:)` (26); `      END` (28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–26: SELECT CASE에는 CASE DEFAULT가 없다. 지정된 ND 이외의 경우 FP를 설정하는 호출 없이 26행 누적문으로 진행한다.
