---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpccorr3.f
lines: 35
sha256: f25c9a80bf74da8c970056db95ace7ae45c566563432892886e6ef8445e1e73a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpccorr3.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | MPCCORR3는 면의 세 절점 및 종속 절점 위치를 모은다(6–9). 선언과 주석을 포함한다. 원문: `      SUBROUTINE MPCCORR3(UG,POS,NS,INDOF,IELC)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION XYZ(3,4),UG(6,*),POS(3,*),IELC(3),DUG(3),IC(3),INDOF(3)` (4). `      DO 100 I=1,3` (6). `        CALL SHIFT1(XYZ(1,I),POS(1,IELC(I)),3)` (7). `  100 CONTINUE` (8). `      CALL SHIFT1(XYZ(1,4),POS(1,NS),3)` (9). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/shift1.f:16–18`(복사), `util/addvec.f:9–11`(합). [11-04 전수 검증 보완] |
| 11–30 | 시작 시 1행 MPCCORR3 루틴 안. 세 방향 INDOF로 IC와 NC를 만든다(11–21). NC=0,1,2일 때 CORRFACE1, CORRFACE2, CORRFACE3를 각각 호출하여 DUG를 구한다(23–29). 원문: `      NC=0` (11). `      DO 200 I=1,3` (12). `        IF( INDOF(I) .EQ. -2 ) THEN` (13). `          IC(I)=2` (14). `        ELSEIF( INDOF(I) .LE. 0 ) THEN` (15). `          IC(I)=1` (16). `          NC=NC+1` (17). `        ELSE` (18). `          IC(I)=0` (19). `        ENDIF` (20). `  200 CONTINUE` (21). `      IF( NC .EQ. 0 ) THEN` (23). `        CALL CORRFACE1(DUG,XYZ)` (24). `      ELSEIF( NC .EQ. 1 ) THEN` (25). `        CALL CORRFACE2(DUG,IC,XYZ)` (26). `      ELSEIF( NC .EQ. 2 ) THEN` (27). `        CALL CORRFACE3(DUG,IC,XYZ)` (28). `      ENDIF` (29). |
| 31–35 | 시작 시 1행 MPCCORR3 루틴 안. DUG를 UG와 POS에 더하고 반환한다(31–35). 원문: `      CALL ADDVEC(UG(1,NS),UG(1,NS),DUG,3)` (31). `      CALL ADDVEC(POS(1,NS),POS(1,NS),DUG,3)` (32). `      RETURN` (34). `      END` (35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–31: NC=3인 경우에는 DUG를 설정하는 분기가 없으며 이후 ADDVEC의 인수로 DUG를 전달한다.
