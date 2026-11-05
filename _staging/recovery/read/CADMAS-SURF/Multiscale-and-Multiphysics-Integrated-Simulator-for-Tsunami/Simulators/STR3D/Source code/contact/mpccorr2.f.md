---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpccorr2.f
lines: 32
sha256: 85f09c5ce6630c04e51d03b9a7d2c6ac3ef3c04f036b72d875def65f1e401bb5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpccorr2.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | MPCCORR2는 두 변 절점과 종속 절점 위치를 XYZ에 복사한다(6–8). 배열 크기와 암시적 형 선언을 포함한다. 원문: `      SUBROUTINE MPCCORR2(UG,POS,NS,INDOF,IG)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION XYZ(3,3),UG(6,*),POS(3,*),IG(2),DUG(3),IC(3),INDOF(3)` (4). `      CALL SHIFT1(XYZ(1,1),POS(1,IG(1)),3)` (6). `      CALL SHIFT1(XYZ(1,2),POS(1,IG(2)),3)` (7). `      CALL SHIFT1(XYZ(1,3),POS(1,NS),3)` (8). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/shift1.f:16–18`(복사), `util/addvec.f:9–11`(합), `contact/lencd.f:13–14`(DUG에 대응하는 V34 계산). [11-04 전수 검증 보완] |
| 10–27 | 시작 시 1행 MPCCORR2 루틴 안. INDOF의 세 방향을 IC로 분류하고 NC를 센다(10–20). NC=0이면 LENCD, 그 밖에는 CORREDGE로 DUG를 구한다(22–26). 원문: `      NC=0` (10). `      DO 200 I=1,3` (11). `        IF( INDOF(I) .EQ. -2 ) THEN` (12). `          IC(I)=2` (13). `        ELSEIF( INDOF(I) .LE. 0 ) THEN` (14). `          IC(I)=1` (15). `          NC=NC+1` (16). `        ELSE` (17). `          IC(I)=0` (18). `        ENDIF` (19). `  200 CONTINUE` (20). `      IF( NC .EQ. 0 ) THEN` (22). `        CALL LENCD(T,DUG,XYZ)` (23). `      ELSE` (24). `        CALL CORREDGE(DUG,IC,XYZ)` (25). `      ENDIF` (26). |
| 28–32 | 시작 시 1행 MPCCORR2 루틴 안. ADDVEC으로 UG와 POS를 같은 DUG만큼 갱신하고 반환한다(28–32). 원문: `      CALL ADDVEC(UG(1,NS),UG(1,NS),DUG,3)` (28). `      CALL ADDVEC(POS(1,NS),POS(1,NS),DUG,3)` (29). `      RETURN` (31). `      END` (32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23: LENCD에서 받는 T는 이 파일의 후속 실행문에서 참조하지 않는다.
