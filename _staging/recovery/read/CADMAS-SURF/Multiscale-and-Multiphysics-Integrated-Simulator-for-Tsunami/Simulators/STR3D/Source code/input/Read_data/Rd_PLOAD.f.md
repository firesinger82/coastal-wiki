---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PLOAD.f
lines: 13
sha256: 8e9dc2e0c71d4fdf27855c3d109e365c85cb5a0b74fc9ca5e6a5a54961a503ad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PLOAD.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RD_PLOAD의 IMPLICIT와 J_PL(5)·IG(4)를 선언한다(1–5). IDS, P와 IG의 네 성분을 읽는다(7). IDS는 J_PL(1), IG는 J_PL(2:5), P는 R_PL로 복사한다(9–11). 주석·END를 포함한다(12–13). 원문: `      SUBROUTINE RD_PLOAD( J_PL, R_PL, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_PL(5), IG(4)` (5); `      READ(CHAR,'(BN,8X,I8,F8.0,4I8)') IDS, P, IG(:)` (7); `      J_PL(1) = IDS` (9); `      J_PL(2:5) = IG(:)` (10); `      R_PL = P` (11); `      END` (13). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
