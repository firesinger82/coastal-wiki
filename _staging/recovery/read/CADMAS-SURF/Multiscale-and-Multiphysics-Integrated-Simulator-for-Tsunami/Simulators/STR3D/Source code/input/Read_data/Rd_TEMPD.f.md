---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TEMPD.f
lines: 16
sha256: 78ed2c05de99b81042e2159f5fb5888ed90d4539b96a69db4492ef2b88c39c40
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TEMPD.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | RD_TEMPD의 IMPLICIT와 J_TMPD(*)·R_TMPD(*)·ID(3)·T(3)을 선언한다(1–5). 카드(card)에서 ID(I)·T(I) 세 쌍을 읽는다(7). 9행 루프(loop)는 ID(I)=0에서 EXIT한다(10). 나머지 항목은 IP 증가 후 J_TMPD·R_TMPD에 저장한다(11–13). 원문: `      SUBROUTINE RD_TEMPD( J_TMPD, R_TMPD, IP, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_TMPD(*), R_TMPD(*), ID(3), T(3)` (5); `      READ(CHAR,'(BN,8X,3(I8,F8.0))') ( ID(I), T(I), I = 1, 3 )` (7); `      DO I = 1, 3` (9); `        IF( ID(I) == 0 ) EXIT` (10); `        IP = IP + 1` (11); `        J_TMPD(IP) = ID(I)` (12); `        R_TMPD(IP) = T(I)` (13); `      ENDDO` (14); `      END` (16). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
