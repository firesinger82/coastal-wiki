---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/prnstr.f
lines: 22
sha256: cc5440b1d404b0b13398c9b2bbdbaa802a24efb6b8afc89f0d81863ab15b6127
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# prnstr.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | PRNSTR 입구와 배열 선언이다(1–5). 각 I에서 KOJI3D에 SIG·PRNSIG를 전달한다(11–12). 이어서 KOJI3E에 EPS·PRNEPS를 전달한다(13). VMSIG(I)는 아래 식으로 대입한다(14–18). 해석: 이 호출과 식은 주응력·주변형률·von Mises 응력을 구하는 것으로 볼 수 있다. 원문: `      SUBROUTINE PRNSTR(ND,SIG,EPS,PRNSIG,PRNEPS,VMSIG,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION SIG(6,ND),EPS(6,ND),PRNSIG(3,ND),PRNEPS(3,ND),VMSIG(ND)`<br>`     &         ,CMX(3,3)` (4–5); `      DO 100 I=1,ND` (11); `        CALL KOJI3D(SIG(1,I),PRNSIG(1,I),CMX,ITO)` (12); `        CALL KOJI3E(EPS(1,I),PRNEPS(1,I),CMX,ITO)` (13); `        VMSIG(I)=DSQRT(0.5D0*( (SIG(2,I)-SIG(3,I))*(SIG(2,I)-SIG(3,I))`<br>`     &                        +(SIG(3,I)-SIG(1,I))*(SIG(3,I)-SIG(1,I))`<br>`     &                        +(SIG(1,I)-SIG(2,I))*(SIG(1,I)-SIG(2,I)) )`<br>`     &                +3.0D0*( SIG(4,I)*SIG(4,I)+SIG(5,I)*SIG(5,I)`<br>`     &                        +SIG(6,I)*SIG(6,I) )  )` (14–18); `  100 CONTINUE` (19); `      RETURN` (21); `      END` (22) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
