---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/pcnstr.f
lines: 11
sha256: ea7cff58cb634c33c168833f577233cbefe2af40f1cf3d5947ff838424311838
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# pcnstr.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | PCNSTR은 실수 IMPLICIT와 NNOD 길이 배열을 선언한다. I=1,NNOD에서 INDOP0(I)=0이며 IPND(I)=1일 때만 DPG(I)를 PPND(I)-PG2(I)로 설정한다. 해석: DPG는 압력 증분(pressure increment)으로 보인다. 7–8행은 한 조건부 대입 연속문이다. 원문: `      SUBROUTINE PCNSTR(DPG,NNOD,INDOP0,IPND,PPND,PG2)` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      DIMENSION DPG(NNOD),INDOP0(NNOD),PPND(NNOD),PG2(NNOD),IPND(NNOD)` (4); `      DO I = 1, NNOD` (6); `        IF( INDOP0(I) == 0 .AND. IPND(I) == 1 ) ` (7); `     &    DPG(I) = PPND(I) - PG2(I)` (8); `      ENDDO` (9); `      END` (11) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–9: 조건을 만족하지 않는 절점에는 DPG 대입이 없다.
