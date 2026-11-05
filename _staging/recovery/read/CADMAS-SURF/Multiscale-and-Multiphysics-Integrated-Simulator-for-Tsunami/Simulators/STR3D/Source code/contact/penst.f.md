---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/penst.f
lines: 45
sha256: 9987e3d7af917376fefa1d82ba7c0947fd71f7b67362f0fe2dbf5b157471bee6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# penst.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | PENST는 접촉 상태를 면(face), 변(edge), 정점(vertex) 중 하나로 설정한다. DATA TOL=75.D0으로 COST를 계산하고 VECML1로 EN과 RN의 COS를 얻는다(6–10). TOL2=TOL1*1.D0이다(12). RL_MIN은 1.1D0에서 시작한다(14). RL(I)<RL_MIN일 때만 I_MIN과 RL_MIN을 갱신한다(16–21). 세 성분 모두 1.1D0 이상이면 RL_MIN은 1.1D0을 유지한다. 이 경우 I_MIN은 이 루프에서 대입되지 않는다. 배열 선언과 빈 줄을 포함한다. 원문: `      SUBROUTINE PENST(ISLV,RSLV,IEDG,IELA,IFC,RL,P,RN,POS,EN,TOL1)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION RL(3),ISLV(2),RSLV(3),IELA(3),X(3,3),POS(3,*),IEDG(6,*)` (4); `     &         ,P(3,3),V(3),RN(3),EN(3)` (5). `      DATA TOL /75.D0/` (6). `      COST=DCOS(TOL/90.D0*DASIN(1.D0))` (8). `      CALL VECML1(COS,EN,RN,3)` (10). `      TOL2 = TOL1 * 1.D0` (12). `      RL_MIN = 1.1D0` (14). `      DO I = 1, 3` (16). `        IF( RL(I) < RL_MIN ) THEN` (17). `          I_MIN = I` (18). `          RL_MIN = RL(I)` (19). `        ENDIF` (20). `      ENDDO` (21). [11-04 전수 검증 정정] |
| 23–45 | 시작 시 1행 PENST 루틴 안. COS>COST 또는 RL_MIN>TOL1이면 면 상태 13,IFC 및 전체 RL을 저장한다(23–26). ELSE에서는 최소 성분에 대응한 변을 고르고 RL 가중 점의 LENCD 결과 RT를 구한다(28–31). RT<TOL2 또는 RT>1-TOL2이면 해당 끝점 상태 11, 그 밖에는 변 상태 12와 RT를 저장한다(32–42). 조건 종료와 END를 포함한다. 원문: `      IF( COS > COST .OR. RL_MIN > TOL1 ) THEN` (23). `        ISLV(1) = 13` (24). `        ISLV(2) = IFC` (25). `        RSLV(:) = RL(:)` (26). `      ELSE` (27). `        IE = IELA(I_MIN)` (28). `        X(:,1:2) = POS(:,IEDG(1:2,IE))` (29). `        X(:,3) = RL(1) * P(:,1) + RL(2) * P(:,2) + RL(3) * P(:,3)` (30). `        CALL LENCD(RT,V,X)` (31). `        IF( RT < TOL2 ) THEN` (32). `          ISLV(1) = 11` (33). `          ISLV(2) = IEDG(1,IE)` (34). `        ELSEIF( RT > 1.D0 - TOL2 ) THEN` (35). `          ISLV(1) = 11` (36). `          ISLV(2) = IEDG(2,IE)` (37). `        ELSE` (38). `          ISLV(1) = 12` (39). `          ISLV(2) = IE` (40). `          RSLV(1) = RT` (41). `        ENDIF` (42). `      ENDIF` (43). `      END` (45). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·14–21·28: RL_MIN 초기값은 1.1D0이며 I_MIN은 RL(I)<RL_MIN 조건 안에서만 대입된다.
- 32–41: 정점 상태 11 분기에서는 RSLV를 갱신하지 않고 변 상태 12에서는 RSLV(1)만 갱신한다.
