---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/prnase.f
lines: 25
sha256: 77671015c61a134fa7ff81d39a669ddc3c2d9a9b9d806bc7f9283246279a6420
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# prnase.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | PRNASE 입구와 IMPLICIT·INTEGER*8 선언이다(1–5). 다중 프런트 해법(multifrontal solver) ASE의 방정식 수와 할당·사용·가용·필요 메모리를 출력한다(7–22). 메모리 환산식과 출력 FORMAT의 연속행은 아래 원문과 같다. 원문: `      SUBROUTINE PRNASE(NEQSOL,NALLOC,NREQ,LNUMI,LNUMO,NSIZ,ZFACT,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INTEGER*8 NALLOC, NSIZ, NREQ` (5); `      WRITE(ITO,7439) ` (7); ` 7439 FORMAT(/1X,5(1H*),2X,'MULTIFRONTAL SOLVER (ASE) MESSAGE',2X`<br>`     *       ,5(1H*) )` (8–9); `      WRITE(ITO,7449) NEQSOL, NALLOC*4.D-6, (NALLOC-NSIZ)*4.D-6, `<br>`     *                NSIZ*4.D-6, NREQ*4.D-6 + LNUMI*8.D-6*ZFACT, `<br>`     *                NREQ*4.D-6 + LNUMO*8.D-6*ZFACT` (11–13); ` 7449 FORMAT(/3X,19HNUMBER OF EQUATIONS,1X,31(1H-),I8`<br>`     *       /3X,16HALLOCATED MEMORY,1X,34(1H-),F8.1,4H(MB)`<br>`     *       /3X,26HUSED MEMORY FOR DATA TABLE,1X,24(1H-),F8.1,4H(MB)`<br>`     *       /3X,34HAVAILABLE MEMORY FOR MATRIX SOLVER`<br>`     *       ,1X,16(1H-),F8.1,4H(MB)`<br>`     *       /3X,47HREQUIRED MEMORY FOR MATRIX SOLVER (INCORE ONLY)`<br>`     *       ,1X,3(1H-),F8.1,4H(MB)`<br>`     *       /3X,47HREQUIRED MEMORY FOR MATRIX SOLVER (OUTCORE USE)`<br>`     *       ,1X,3(1H-),F8.1,4H(MB) )` (14–22); `      RETURN` (24); `      END` (25) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–13: NALLOC·NSIZ·NREQ에 곱하는 계수는 4.D-6이다. LNUMI·LNUMO에는 8.D-6과 ZFACT를 곱한다. 해석: 전자를 정수 작업공간, 후자를 수치 인수분해 작업공간으로 보는 설명은 이 구간에서 자료형까지 확인한 사실이 아니다. [11-04 전수 검증 정정]
