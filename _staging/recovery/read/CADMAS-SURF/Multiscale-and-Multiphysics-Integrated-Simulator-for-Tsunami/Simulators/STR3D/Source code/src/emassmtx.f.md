---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/emassmtx.f
lines: 28
sha256: 65c6c83701d5a6cdf688186696890710fb6a9111c8c6576e15e06dc4db008f0f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# emassmtx.f — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | EMASSMTX의 인수와 배열을 선언한다. EMASR의 선언 길이는 400이다. 해석: EMASR은 요소 질량 작업 배열이다. 원문: `      SUBROUTINE EMASSMTX(EMASS,GRID,ITYP,NDF,ND,IBTYP,KN,AMAT,RODA,BARD`<br>`     &                   ,LUMP,ITO)` (1–2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION EMASS(*),AMAT(*),GRID(3,*),KN(ND),EMASR(400),BARD(*)` (5); 주석 원문 `C-----------------------------------------------------------------------` (6). [11-04 전수 검증 정정] |
| 7–23 | 시작 시 1–2행 EMASSMTX 루틴 안. ITYP 2·6에서는 ND 4·10·6·15별로 EMASSTE1·EMASSTE2·EMASSPN1·EMASSPN2를 호출하고 나머지는 EMASSHX2를 호출한다. ITYP 3은 EMASSTRS, ITYP 4는 EMASSBM을 호출한다. 원문: `      IF(ITYP.EQ.2 .OR. ITYP.EQ.6) THEN` (7); `        IF(ND.EQ.4) THEN` (8); `          CALL EMASSTE1(EMASR,AMAT,GRID,KN,LUMP,ITO)` (9); `        ELSEIF(ND.EQ.10) THEN` (10); `          CALL EMASSTE2(EMASR,AMAT,GRID,KN,LUMP,ITO)` (11); `        ELSEIF(ND.EQ.6) THEN` (12); `          CALL EMASSPN1(EMASR,AMAT,GRID,KN,LUMP,ITO)` (13); `        ELSEIF(ND.EQ.15) THEN` (14); `          CALL EMASSPN2(EMASR,AMAT,GRID,KN,LUMP,ITO)` (15); `        ELSE` (16); `          CALL EMASSHX2(EMASR,AMAT,GRID,KN,ND,LUMP,ITO)` (17); `        ENDIF` (18); `      ELSEIF(ITYP .EQ. 3) THEN` (19); `        CALL EMASSTRS(EMASR,AMAT,RODA,GRID,KN,LUMP,ITO)` (20); `      ELSEIF(ITYP.EQ.4) THEN` (21); `        CALL EMASSBM(EMASR,AMAT,BARD,GRID,IBTYP,KN,LUMP,ITO)` (22); `      ENDIF` (23). |
| 24–28 | 시작 시 1–2행 EMASSMTX 루틴 안. TRNSEMASS에 EMASR·ND·NDF·LUMP를 전달하여 EMASS를 구성한다. 반환문과 루틴 끝을 포함한다. 원문: `      CALL TRNSEMASS(EMASS,EMASR,ND,NDF,LUMP)` (25); `      RETURN` (27); `      END` (28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–25: ITYP가 2·6·3·4가 아니면 EMASR을 설정하는 호출 없이 TRNSEMASS 호출로 진행한다.
