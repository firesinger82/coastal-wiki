---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/prncg.f
lines: 19
sha256: 10a79a970b8b1559cda03b0a9330fa5301a46c3afbc29bc83f3fb3d7a0ff8465
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# prncg.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | PRNCG 입구와 INTEGER*8 선언이다(1–3). 공액기울기법(conjugate gradient method) 해법의 방정식 수와 메모리 정보를 출력한다(5–16). 환산식과 FORMAT은 아래 원문과 같다. 원문: `      SUBROUTINE PRNCG(NEQSOL,MALLOC,MAVBL,MREQ,ITO)` (1); `      INTEGER*8 MALLOC, MAVBL, MREQ` (3); `      WRITE(ITO,7439) ` (5); ` 7439 FORMAT(/1X,5(1H*),2X,'CG-METHOD SOLVER MESSAGE',2X,5(1H*) )` (6); `      WRITE(ITO,7449) NEQSOL, MALLOC*4.D-6, (MALLOC-MAVBL)*4.D-6, `<br>`     *                MAVBL*4.D-6, MREQ*4.D-6` (8–9); ` 7449 FORMAT(/3X,19HNUMBER OF EQUATIONS,1X,20(1H-),I8`<br>`     *       /3X,16HALLOCATED MEMORY,1X,23(1H-),F8.1,4H(MB)`<br>`     *       /3X,26HUSED MEMORY FOR DATA TABLE,1X,13(1H-),F8.1,4H(MB)`<br>`     *       /3X,34HAVAILABLE MEMORY FOR MATRIX SOLVER`<br>`     *       ,1X,5(1H-),F8.1,4H(MB)`<br>`     *       /3X,33HREQUIRED MEMORY FOR MATRIX SOLVER`<br>`     *       ,1X,6(1H-),F8.1,4H(MB) )` (10–16); `      RETURN` (18); `      END` (19) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–9: 메모리 환산 계수는 4.D-6으로 고정되어 있다.
