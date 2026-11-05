---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PLOAD1.f
lines: 25
sha256: 410024247c1adfe455971cdc2db421f13d4c74bdd32f5873c30209a88a42e57f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PLOAD1.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | RD_PLOAD1의 IMPLICIT·J_PL1(3) 선언과 정수 두 값·실수 R_PL1 판독을 포함한다(1–7). 9행 루프(loop)가 25–31 위치에서 FX·FY·FZ 문자열을 검색한다. 10·13·16행 조건의 FX·FY·FZ는 J_PL1(3)=1·2·3에 각각 대응하며 즉시 반환한다(11–18). ELSE는 없으므로 불일치 시 다음 I로 검색을 계속한다(10–20). 검색 실패는 오류 출력과 ERRSTP(90,ITO) 호출이다(22–23). 원문: `      SUBROUTINE RD_PLOAD1( J_PL1, R_PL1, CHAR, ITO )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_PL1(3)` (5); `      READ(CHAR,'(BN,8X,2I8,24X,F8.0)') J_PL1(1:2), R_PL1` (7); `      DO I = 25, 31` (9); `        IF( CHAR(I:I+1) == 'FX' ) THEN` (10); `          J_PL1(3) = 1` (11); `          RETURN` (12); `        ELSEIF( CHAR(I:I+1) == 'FY' ) THEN` (13); `          J_PL1(3) = 2` (14); `          RETURN` (15); `        ELSEIF( CHAR(I:I+1) == 'FZ' ) THEN` (16); `          J_PL1(3) = 3` (17); `          RETURN` (18); `        ENDIF` (19); `      ENDDO` (20); `      WRITE(ITO,*) 'TYPE ERROR, STOP IN SUB. PLOAD1.'` (22); `      CALL ERRSTP(90,ITO)` (23); `      END` (25). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
