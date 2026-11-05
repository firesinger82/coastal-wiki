---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfaddg.f
lines: 8
sha256: 0e1678eb0bd5da3a247e56504c131db1f30376307680b8f7e669deb0d988d91e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfaddg.f — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | ENPFADDG의 암시적 형과 FT·FC·KN의 배열 크기를 선언한다. 해석: FT는 전역 힘이고 FC는 요소 힘이며 KN은 절점 번호이다. 원문: `      SUBROUTINE ENPFADDG(FT,GE,FC,NDF,ND,KN)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION FT(6,*),KN(ND),FC(NDF,*)` (4); 주석 원문 `C-----------------------------------------------------------------------` (5). [11-04 전수 검증 정정] |
| 6–8 | 시작 시 1행 ENPFADDG 루틴 안. FC의 1:ND 열에 GE를 곱하여 KN이 가리키는 FT의 1:NDF 성분에 더한다. 루틴 끝을 포함한다. 원문: `      FT(1:NDF,KN(:)) = FT(1:NDF,KN(:)) + GE * FC(:,1:ND)` (6); `      END` (8). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·6: FT의 첫 번째 크기는 6이다. 대입 범위 1:NDF에 대해 NDF<=6을 검사하는 조건문은 없다.
