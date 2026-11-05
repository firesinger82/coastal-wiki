---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/bdfte1.f
lines: 23
sha256: dd92d5029f72429fc094d5908a82d157f75e3bd050b15d1e5c0d003c7f136b79
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bdfte1.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | BDFTE1의 암시적 형·배열 선언. ND=4로 설정하고 TETVOL로 체적을 얻는다. 절점마다 IGR=1이면 GRAV, 그 밖에는 XYZ-R0를 선택한다. RMULT1에 0.25*VOL을 전달해 네 절점 힘을 계산한다. 원문: `      SUBROUTINE BDFTE1(FC,XYZ,GRAV,R0,IGR,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XYZ(3,4),FC(3,4),VEC(3),GRAV(3),R0(3)` (4); `C----&------------------------------------------------------------------` (5); `      ND=4` (6); `      CALL TETVOL(XYZ,VOL)` (8); `      DO 100 I=1,ND` (10); `        IF(IGR .EQ. 1) THEN` (12); `          CALL SHIFT1(VEC,GRAV,3)` (13); `        ELSE` (14); `          CALL SUBVEC(VEC,XYZ(1,I),R0,3)` (15); `        ENDIF` (16); `        CALL RMULT1(FC(1,I),VEC,0.25*VOL,3)` (18); `  100 CONTINUE` (20); `      RETURN` (22); `      END` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–23: ITO는 인수에 있지만 이 파일의 실행문에서 참조하지 않는다.
