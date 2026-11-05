---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/bdfbm.f
lines: 23
sha256: 11936f20cb404c49e42334d460f275243ca440afe36f6bbf69b3d40b9942fc01
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bdfbm.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | BDFBM의 암시적 형·배열 선언. ND=2로 설정하고 LENGTH로 두 절점 사이 길이를 얻는다. 절점마다 IGR=1이면 GRAV를, 그 밖에는 XYZ-R0 벡터를 사용한다. RMULT1에 D1*D2*RL*.5를 전달해 두 절점 힘을 계산한다. 원문: `      SUBROUTINE BDFBM(FC,XYZ,D1,D2,GRAV,R0,IGR,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION  XYZ(3,2),VEC(3),GRAV(3),R0(3),FC(3,2)` (4); `C----&------------------------------------------------------------------` (5); `      ND=2` (6); `      CALL LENGTH(RL,XYZ(1,1),XYZ(1,2),3)` (8); `      DO 100 I=1,ND` (10); `        IF(IGR .EQ. 1) THEN` (12); `          CALL SHIFT1(VEC,GRAV,3)` (13); `        ELSE` (14); `          CALL SUBVEC(VEC,XYZ(1,I),R0,3)` (15); `        ENDIF` (16); `        CALL RMULT1(FC(1,I),VEC,D1*D2*RL*.5,3)` (18); `  100 CONTINUE` (20); `      RETURN` (22); `      END` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–23: ITO는 인수에 있지만 이 파일의 실행문에서 참조하지 않는다.
