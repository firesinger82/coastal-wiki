---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpccorr13.f
lines: 38
sha256: 346bd9924f2956e919e007dd7973adbc3d0f256b5470d674c696136b6faa08e6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpccorr13.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | MPCCORR13는 면(face)의 세 절점과 종속 절점 위치를 XYZ에 모은다(7–10). RL은 길이 3 배열로 선언된다(4–5). 원문: `      SUBROUTINE MPCCORR13(UG,POS,NS,RL,INDOF,IELC)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION XYZ(3,4),UG(6,*),POS(3,*),IELC(3),DUG(3),IC(3),INDOF(3)` (4); `     &         ,P(3),RL(3)` (5). `      DO 100 I=1,3` (7). `        CALL SHIFT1(XYZ(1,I),POS(1,IELC(I)),3)` (8). `  100 CONTINUE` (9). `      CALL SHIFT1(XYZ(1,4),POS(1,NS),3)` (10). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/shift1.f:16–18`(복사), `util/subvec.f:9–11`(차), `util/addvec.f:9–11`(합), `contact/spcdface1.f:6–8`, `contact/spcdface2.f:31–44`, `contact/spcdface3.f:31–39`(목표 위치). [11-04 전수 검증 보완] |
| 12–31 | 시작 시 1행 MPCCORR13 루틴 안. INDOF=-2, 그 밖의 비양수, 양수를 IC=2,1,0으로 분류한다(13–22). NC=0,1,2일 때 각각 SPCDFACE1, SPCDFACE2, SPCDFACE3로 목표 위치를 구한다(24–30). 원문: `      NC=0` (12). `      DO 200 I=1,3` (13). `        IF( INDOF(I) .EQ. -2 ) THEN` (14). `          IC(I)=2` (15). `        ELSEIF( INDOF(I) .LE. 0 ) THEN` (16). `          IC(I)=1` (17). `          NC=NC+1` (18). `        ELSE` (19). `          IC(I)=0` (20). `        ENDIF` (21). `  200 CONTINUE` (22). `      IF( NC .EQ. 0 ) THEN` (24). `        CALL SPCDFACE1(P,XYZ,RL)` (25). `      ELSEIF( NC .EQ. 1 ) THEN` (26). `        CALL SPCDFACE2(P,IC,XYZ,RL)` (27). `      ELSEIF( NC .EQ. 2 ) THEN` (28). `        CALL SPCDFACE3(P,IC,XYZ)` (29). `      ENDIF` (30). |
| 32–38 | 시작 시 1행 MPCCORR13 루틴 안. 목표 위치에서 현재 위치를 빼 DUG를 구하고 UG 및 POS에 더한다(32–35). 반환과 END를 포함한다. 원문: `      CALL SUBVEC(DUG,P,POS(1,NS),3)` (32). `      CALL ADDVEC(UG(1,NS),UG(1,NS),DUG,3)` (34). `      CALL ADDVEC(POS(1,NS),POS(1,NS),DUG,3)` (35). `      RETURN` (37). `      END` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–32: NC=3인 경우에는 P를 설정하는 분기가 없으며 이후 SUBVEC의 인수로 P를 전달한다.
