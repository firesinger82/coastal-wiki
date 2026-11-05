---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PBARL.f
lines: 27
sha256: 1a4159808ec50fe2b564b11723eac08c9fbe54ae7dabe9a8782c17830fcba906
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PBARL.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | RD_PBARL의 IMPLICIT·배열 선언과 최초 정수 두 성분 판독을 포함한다(1–7). 9행 루프(loop)가 33–40 위치에서 ROD·BAR·TUBE 문자열을 검색한다. ELSE는 없으므로 불일치 시 다음 I로 검색을 계속한다(10–20). 10·13·16행 조건은 ROD·BAR·TUBE를 각각 J_PBAR(3)=1·2·3으로 대응시키고 GOTO 10으로 이동한다(11–18). 검색 실패는 오류 출력과 ERRSTP(90,ITO) 호출이다(22–23). 라벨(label) 10은 다음 레코드(record)의 실수 두 값을 읽는다(25). 원문: `      SUBROUTINE RD_PBARL( J_PBAR, R_PBAR, CHAR, ITI, ITO )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION J_PBAR(3), R_PBAR(6)` (5); `      READ(CHAR,'(BN,8X,2I8)') J_PBAR(1:2)` (7); `      DO I = 33, 40` (9); `        IF( CHAR(I:I+2) == 'ROD' ) THEN` (10); `          J_PBAR(3) = 1` (11); `          GOTO 10` (12); `        ELSEIF( CHAR(I:I+2) == 'BAR' ) THEN` (13); `          J_PBAR(3) = 2` (14); `          GOTO 10` (15); `        ELSEIF( CHAR(I:I+3) == 'TUBE' ) THEN` (16); `          J_PBAR(3) = 3` (17); `          GOTO 10` (18); `        ENDIF` (19); `      ENDDO` (20); `      WRITE(ITO,*) 'TYPE ERROR, STOP IN SUB. RD_PBARL.'` (22); `      CALL ERRSTP(90,ITO)` (23); `   10 READ(ITI,'(BN,8X,2F8.0)') R_PBAR(1:2)` (25); `      END` (27). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·25: R_PBAR의 선언 길이는 6이지만 이 루틴은 R_PBAR(1:2)만 읽는다.
