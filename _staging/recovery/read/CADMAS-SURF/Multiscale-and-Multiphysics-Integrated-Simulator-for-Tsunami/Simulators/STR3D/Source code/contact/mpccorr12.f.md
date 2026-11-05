---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpccorr12.f
lines: 35
sha256: d2d5ba2e09a1efc930111355bc4b35c05f9e1d6e166de06d5c490536f55bb044
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpccorr12.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | MPCCORR12는 변(edge) 두 절점과 종속 절점(slave node)의 위치를 XYZ로 복사한다(7–9). 선언과 구분 주석을 포함한다. 원문: `      SUBROUTINE MPCCORR12(UG,POS,NS,T,INDOF,IG)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION XYZ(3,3),UG(6,*),POS(3,*),IG(2),DUG(3),IC(3),INDOF(3)` (4); `     &         ,P(3)` (5). `      CALL SHIFT1(XYZ(1,1),POS(1,IG(1)),3)` (7). `      CALL SHIFT1(XYZ(1,2),POS(1,IG(2)),3)` (8). `      CALL SHIFT1(XYZ(1,3),POS(1,NS),3)` (9). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/shift1.f:16–18`(복사), `util/rmult5.f:8–10`(가중합), `util/subvec.f:9–11`(차), `util/addvec.f:9–11`(합). [11-04 전수 검증 보완] |
| 11–28 | 시작 시 1행 MPCCORR12 루틴 안. 세 방향의 INDOF를 IC로 분류하고 -2를 제외한 비양수 방향 수를 NC에 누적한다(11–21). NC=0이면 T로 두 끝점의 가중 위치를 RMULT5에서 구한다(23–24). 그 밖에는 SPCDEDGE를 호출한다(25–27). 원문: `      NC=0` (11). `      DO 200 I=1,3` (12). `        IF( INDOF(I) .EQ. -2 ) THEN` (13). `          IC(I)=2` (14). `        ELSEIF( INDOF(I) .LE. 0 ) THEN` (15). `          IC(I)=1` (16). `          NC=NC+1` (17). `        ELSE` (18). `          IC(I)=0` (19). `        ENDIF` (20). `  200 CONTINUE` (21). `      IF( NC .EQ. 0 ) THEN` (23). `        CALL RMULT5(P,1.D0-T,XYZ(1,1),T,XYZ(1,2),3)` (24). `      ELSE` (25). `        CALL SPCDEDGE(P,IC,XYZ)` (26). `      ENDIF` (27). |
| 29–35 | 시작 시 1행 MPCCORR12 루틴 안. SUBVEC으로 목표 위치와 현재 위치의 차 DUG를 구한다(29). ADDVEC으로 UG와 POS의 처음 세 성분을 같은 DUG만큼 보정하고 반환한다(31–35). 원문: `      CALL SUBVEC(DUG,P,POS(1,NS),3)` (29). `      CALL ADDVEC(UG(1,NS),UG(1,NS),DUG,3)` (31). `      CALL ADDVEC(POS(1,NS),POS(1,NS),DUG,3)` (32). `      RETURN` (34). `      END` (35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–17: INDOF=-2 방향은 IC=2이며 NC에 포함되지 않는다.
- 23–27: NC가 1, 2, 3인 경우는 모두 같은 SPCDEDGE 호출로 들어간다.
