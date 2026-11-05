---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/pcnstri.f
lines: 16
sha256: 17dd15e4e9320e093e4279b44115c5b6fcdebab0d4e33a78bc0b8be588020794
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# pcnstri.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | PCNSTRI는 INDOP(NNOD)와 IELM(NM,NELM)를 선언한다. INDOP 전체를 1로 초기화한다. 요소 루프에서 ITYP·NNP를 읽고 ITYP=6이면 해당 요소 절점 범위 IELM(8:7+NNP,I)의 INDOP를 0으로 바꾼다. 원문: `      SUBROUTINE PCNSTRI(INDOP,IELM,NNOD,NELM,NM)` (1); `      DIMENSION INDOP(NNOD),IELM(NM,NELM)` (3); `      INDOP(:) = 1` (5); `      DO I = 1, NELM` (7); `        ITYP = IELM(2,I)` (9); `        NNP = IELM(3,I)` (10); `        IF( ITYP == 6 ) INDOP( IELM(8:7+NNP,I) ) = 0` (12); `      ENDDO` (14); `      END` (16) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
