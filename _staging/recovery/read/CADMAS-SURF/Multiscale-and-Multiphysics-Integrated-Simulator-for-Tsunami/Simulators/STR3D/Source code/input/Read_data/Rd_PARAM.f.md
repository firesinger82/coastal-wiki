---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PARAM.f
lines: 31
sha256: ae850700f4d349a5d3a867e6dbd7f3eb1437e3fa34cd3f9956280e59a5e7abb6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PARAM.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | RD_PARAM의 IMPLICIT·KK(*)·RR(*) 선언을 포함한다(1–5). 7행 루프(loop)가 시작 위치 7–10에서 키(key)를 검색한다. 8행 W4 분기는 RR(5)를 읽는다(9). 11행 LGDISP 분기는 값을 읽고(12), 13·15행 조건으로 1을 KK(2)=2, 2를 KK(2)=1로 변환한다(14·16). 19·22·25행 EPSA·EPSR·EPSC 분기는 각각 RR(3)·RR(6)·RR(14)를 읽는다(20·23·26). 각 인식 분기는 RETURN하며 나머지는 검색을 계속한다. 두 IF 사슬에는 ELSE가 없다(8–28·13–17). LGDISP가 1·2 이외이면 KK(2)를 대입하지 않고 반환한다(13–18). 원문: `      SUBROUTINE RD_PARAM( KK, RR, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION KK(*),RR(*)` (5); `      DO I = 7, 10` (7); `        IF( CHAR(I:I+1) == 'W4' ) THEN` (8); `          READ(CHAR(I+3:),*) RR(5)` (9); `          RETURN` (10); `        ELSEIF( CHAR(I:I+5) == 'LGDISP' ) THEN` (11); `          READ(CHAR(I+7:),*) LGDISP` (12); `          IF( LGDISP == 1 ) THEN` (13); `            KK(2) = 2` (14); `          ELSEIF( LGDISP == 2 ) THEN` (15); `            KK(2) = 1` (16); `          ENDIF` (17); `          RETURN` (18); `        ELSEIF( CHAR(I:I+3) == 'EPSA' ) THEN` (19); `          READ(CHAR(I+5:),*) RR(3)` (20); `          RETURN` (21); `        ELSEIF( CHAR(I:I+3) == 'EPSR' ) THEN` (22); `          READ(CHAR(I+5:),*) RR(6)` (23); `          RETURN` (24); `        ELSEIF( CHAR(I:I+3) == 'EPSC' ) THEN` (25); `          READ(CHAR(I+5:),*) RR(14)` (26); `          RETURN` (27); `        ENDIF` (28); `      ENDDO` (29); `      END` (31). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–18: LGDISP가 1·2 이외이면 KK(2) 대입 없이 반환한다.
