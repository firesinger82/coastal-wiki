---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_MATS1.f
lines: 29
sha256: bb358e03e3b58dda8ff1ebb0aa41e5e80bd47a288e586c2ae3e6f2bbc9272c0c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_MATS1.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | RD_MATS1의 IMPLICIT·J_MATS1(2)·R_MATS1(3)을 선언하고 MID·HD·IYF·SY·ALP를 읽는다(1–9). 11행 SELECT CASE로 항복 함수(yield function)를 선택한다. CASE(1)는 내부 값 1(12–13), CASE(2,3)는 오류 출력과 ERRSTP(90,ITO) 호출(14–16), CASE(4)는 내부 값 2(17–18), CASE DEFAULT는 1이다(19–20). 원문: `      SUBROUTINE RD_MATS1( J_MATS1, R_MATS1, CHAR, ITO )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_MATS1(2), R_MATS1(3)` (5); `      READ(CHAR,'(BN,8X,I8,16X,F8.0,I8,8X,2F8.0)') MID, HD, IYF, SY, ALP` (7); `      J_MATS1(1) = MID` (9); `      SELECT CASE( IYF )` (11); `      CASE( 1 )` (12); `        J_MATS1(2) = 1` (13); `      CASE( 2, 3 )` (14); `        WRITE(ITO,*) 'YIELD FUNCTION ERROR, STOP IN SUB. RD_MATS1.'` (15); `        CALL ERRSTP(90,ITO)` (16); `      CASE( 4 )` (17); `        J_MATS1(2) = 2` (18); `      CASE DEFAULT` (19); `        J_MATS1(2) = 1` (20); `      END SELECT` (21). |
| 23–29 | 시작 시 1행 RD_MATS1 안. HD·SY를 R_MATS1(1:2)에 복사한다(23–24). 26행 조건부 기본값 식으로 ALP=0일 때 7.D-2를 대입한 후 R_MATS1(3)에 저장한다(27). 끝 주석·END를 포함한다(28–29). 원문: `      R_MATS1(1) = HD` (23); `      R_MATS1(2) = SY` (24); `      IF( ALP == 0.D0 ) ALP = 7.D-2` (26); `      R_MATS1(3) = ALP` (27); `      END` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26: 입력 ALP가 0이면 7.D-2로 대체한다.
