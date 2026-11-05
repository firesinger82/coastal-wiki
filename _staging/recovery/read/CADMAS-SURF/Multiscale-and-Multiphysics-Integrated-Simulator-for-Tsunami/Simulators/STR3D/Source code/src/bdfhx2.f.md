---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/bdfhx2.f
lines: 51
sha256: 6f5ff1eeeb2cd1fa0b3c4ad5574d30150ef5a5172b184358b4484f147fe50b86
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bdfhx2.f — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | BDFHX2의 암시적 형·배열 선언과 DATA 적분 점·가중치. ND=8이면 NG=2, 그 밖에는 NG=3을 선택한다. 원문: `      SUBROUTINE BDFHX2(FC,XYZ,ND,GRAV,R0,IGR,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 연속문(4–5): `      DIMENSION WG(3,3),XG(3,3),XYZ(3,ND),P(3,20),XJI(3,3),H(20)` <br> `     &         ,FC(3,ND),VEC(3),GRAV(3),R0(3)`; 연속문(6–8): `      DATA XG / 3*0.0D0` <br> `     &        , -.577350269189626D0, .577350269189626D0, 0.0D0` <br> `     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /`; 연속문(9–12): `      DATA WG / 2.0D0, 2*0.0D0` <br> `     &        , 2*1.0D0, 0.0D0` <br> `     &        , 0.55555555555555556D0, 0.88888888888888889D0` <br> `     &        , 0.55555555555555556D0 /`; `C----&------------------------------------------------------------------` (13); `      IF(ND .EQ. 8) THEN` (14); `        NG=2` (15); `      ELSE` (16); `        NG=3` (17); `      ENDIF` (18). |
| 20–51 | BDFHX2 루틴 안. IG·JG·KG의 세 루프에서 좌표와 곱 가중치를 취한다. DERHX2·JACOB3·SFNHX2에 P·XJI·DET·H를 전달한다. 해석: P는 도함수이고 DET는 야코비안 행렬식이며 H는 형상 함수 값으로 읽힌다. 절점별로 IGR=1이면 중력, 그 밖에는 XYZ-R0를 선택한다. 세 성분에 H(I)*VEC(J)*DET*WGT를 누적한다. 원문: `      DO 100 IG=1,NG` (20); `      DO 100 JG=1,NG` (21); `      DO 100 KG=1,NG` (22); `        XG1=XG(IG,NG)` (24); `        XG2=XG(JG,NG)` (25); `        XG3=XG(KG,NG)` (26); `        WGT=WG(IG,NG)*WG(JG,NG)*WG(KG,NG)` (27); `        CALL DERHX2(XG1,XG2,XG3,ND,P)` (29); `        CALL JACOB3(ND,P,XYZ,XJI,DET,ITO)` (30); `        CALL SFNHX2(XG1,XG2,XG3,ND,H)` (32); `        DO 110 I=1,ND` (34); `          IF(IGR .EQ. 1) THEN` (36); `            CALL SHIFT1(VEC,GRAV,3)` (37); `          ELSE` (38); `            CALL SUBVEC(VEC,XYZ(1,I),R0,3)` (39); `          ENDIF` (40); `          DO 120 J=1,3` (42); `            FC(J,I)=FC(J,I)+H(I)*VEC(J)*DET*WGT` (43); `  120     CONTINUE` (44); `  110   CONTINUE` (46); `  100 CONTINUE` (48); `      RETURN` (50); `      END` (51). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43: FC에 기존 값을 더해 누적한다. 이 파일에는 FC 전체 초기화문이 없다.
