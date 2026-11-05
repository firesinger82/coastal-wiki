---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_TEMP.f
lines: 17
sha256: c1ac76d58d2e02d4eb7542517c42b962e4bfa37dbf4725ee2718c23016e42add
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_TEMP.f — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | RD_TEMP의 IMPLICIT와 J_TMP(2,*)·R_TMP(*)·IG(3)·T(3)을 선언한다(1–5). 최초 카드(card)에서 IDS와 IG(I)·T(I) 세 쌍을 읽는다(7). 9행 루프(loop)는 IG(I)=0에서 EXIT한다(10). 나머지 항목은 IP 증가 후 IDS·IG(I)·T(I)를 각각 J_TMP(1,IP)·J_TMP(2,IP)·R_TMP(IP)에 저장한다(11–14). 원문: `      SUBROUTINE RD_TEMP( J_TMP, R_TMP, IP, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_TMP(2,*), R_TMP(*), IG(3), T(3)` (5); `      READ(CHAR,'(BN,8X,I8,3(I8,F8.0))') IDS, ( IG(I), T(I), I = 1, 3 )` (7); `      DO I = 1, 3` (9); `        IF( IG(I) == 0 ) EXIT` (10); `        IP = IP + 1` (11); `        J_TMP(1,IP) = IDS` (12); `        J_TMP(2,IP) = IG(I)` (13); `        R_TMP(IP) = T(I)` (14); `      ENDDO` (15); `      END` (17). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
