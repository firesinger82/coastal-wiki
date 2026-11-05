---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_SPC.f
lines: 20
sha256: 1c26f9ba99f718b1f7076f5cced13cd41f76ede55193c1174d0d53e84affcb2a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_SPC.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | RD_SPC의 IMPLICIT·문자열 C(2)·배열 범위 선언을 포함한다(1–6). 8–9행 연속문에서 IDS와 두 묶음의 IG(I)·C(I)·D(I)를 읽는다. 11행 루프(loop)는 IG(I)=0에서 EXIT한다(12). IP를 증가시키고 IDS·IG(I)를 저장한다(13–15). RESFR에 J_SPC(3,IP)와 C(I)를 전달한다(16). D(I)를 R_SPC(IP)에 저장한다(17). 원문: `      SUBROUTINE RD_SPC( J_SPC, R_SPC, IP, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8  C(2)` (5); `      DIMENSION J_SPC(8,*), R_SPC(*), IG(2), D(2)` (6); `      READ(CHAR,'(BN,8X,I8,2(I8,A8,F8.0))') ` / `     &  IDS, ( IG(I), C(I), D(I), I = 1, 2 )` (8–9; 하나의 고정형식 연속문); `      DO I = 1, 2` (11); `        IF( IG(I) == 0 ) EXIT` (12); `        IP = IP + 1` (13); `        J_SPC(1,IP) = IDS` (14); `        J_SPC(2,IP) = IG(I)` (15); `        CALL RESFR( J_SPC(3,IP), C(I) )` (16); `        R_SPC(IP) = D(I)` (17); `      ENDDO` (18); `      END` (20). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
