---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_FRIC.f
lines: 23
sha256: 4e20a1fae06533f14eb2b19c135a5050ccbc2b2bc6c8fdc4a13f8a4b274d7a1b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_FRIC.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | RD_FRIC는 IMPLICIT와 가변 길이 KK(*)·RR(*)를 선언한다(1–5). 7·9·11·13행 분기는 MITER0·MITER1·MITERD0·MITERD1 값을 KK(110:113)에 각각 읽는다(8·10·12·14). 15·17·19행 분기는 EPS0·EPSD·EPSS 값을 RR(10:12)에 각각 읽는다(16·18·20). 각 키(key) 길이에 따라 READ 시작 열은 11·13·14이다. ELSE는 없으므로 모든 조건이 거짓이면 값을 읽지 않는다(7–21). 분기 종료·주석·END를 포함한다(21–23). 원문: `      SUBROUTINE RD_FRIC( KK, RR, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION KK(*),RR(*)` (5); `      IF( CHAR(6:11) == 'MITER0' ) THEN` (7); `        READ(CHAR(13:),*) KK(110)` (8); `      ELSEIF( CHAR(6:11) == 'MITER1' ) THEN` (9); `        READ(CHAR(13:),*) KK(111)` (10); `      ELSEIF( CHAR(6:12) == 'MITERD0' ) THEN` (11); `        READ(CHAR(14:),*) KK(112)` (12); `      ELSEIF( CHAR(6:12) == 'MITERD1' ) THEN` (13); `        READ(CHAR(14:),*) KK(113)` (14); `      ELSEIF( CHAR(6:9) == 'EPS0' ) THEN` (15); `        READ(CHAR(11:),*) RR(10)` (16); `      ELSEIF( CHAR(6:9) == 'EPSD' ) THEN` (17); `        READ(CHAR(11:),*) RR(11)` (18); `      ELSEIF( CHAR(6:9) == 'EPSS' ) THEN` (19); `        READ(CHAR(11:),*) RR(12)` (20); `      ENDIF` (21); `      END` (23). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
