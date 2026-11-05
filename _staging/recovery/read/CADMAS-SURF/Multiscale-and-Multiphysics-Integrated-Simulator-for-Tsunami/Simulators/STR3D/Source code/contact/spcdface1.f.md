---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/spcdface1.f
lines: 11
sha256: dbe40087b44dec9d4fe2c8f01c22f8b9ed9aa49e610769d433be2b58daa211fe
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdface1.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | SPCDFACE1은 면(face) 세 점의 RL 가중합으로 P의 세 성분을 계산한다(6–8). 암시적 형, 배열 선언, 주석, RETURN 및 END를 포함한다. RL 합과 범위를 검사하는 조건은 없다. 원문: `      SUBROUTINE SPCDFACE1(P,XYZ,RL)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION P(3),RL(3),XYZ(3,3)` (4). `      DO J=1,3` (6). `        P(J) = RL(1)*XYZ(J,1) + RL(2)*XYZ(J,2) + RL(3)*XYZ(J,3)` (7). `      ENDDO` (8). `      RETURN` (10). `      END` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
