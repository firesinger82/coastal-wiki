---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_REST.f
lines: 16
sha256: c4687f35efae700d44562774f980a699a4210216b87ad55d97797c59289149a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_REST.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | RD_REST의 IMPLICIT와 RTIM(*) 선언을 포함한다(1–5). 7행 RUN 조건은 RTIM(1)을 읽는다(8). 9행 DT 조건은 RTIM(2)를 읽는다(10). 11행 TIME 조건은 IP를 증가시키고 RTIM(2+IP)를 읽는다(12–13). ELSE는 없으므로 세 조건이 모두 거짓이면 IP·RTIM을 변경하지 않는다(7–14). 분기 종료·주석·END를 포함한다(14–16). 원문: `      SUBROUTINE RD_REST( RTIM, IP, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION RTIM(*)` (5); `      IF( CHAR(6:8) == 'RUN' ) THEN` (7); `        READ(CHAR(10:),*) RTIM(1)` (8); `      ELSEIF( CHAR(6:7) == 'DT' ) THEN` (9); `        READ(CHAR(9:),*) RTIM(2)` (10); `      ELSEIF( CHAR(6:9) == 'TIME' ) THEN` (11); `        IP = IP + 1` (12); `        READ(CHAR(11:),*) RTIM(2+IP)` (13); `      ENDIF` (14); `      END` (16). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
