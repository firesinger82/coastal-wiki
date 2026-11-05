---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rfcedge.f
lines: 56
sha256: c99738bc8dc326f2eaa4a4388205ba0700b7e547d5c923a9dc1b9190f04f0ab7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rfcedge.f — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | RFCEDGE는 변(edge) 두 절점과 종속 절점(slave node) 좌표를 X에 모아 LENCD로 RL(2)를 구한다(7–10). RL(1)=1-RL(2)이며 DIRCOS로 변 방향 E를 구한다(11–14). F에서 E 방향 투영(projection)을 빼 RF를 계산한다(16). 선언과 주석을 포함한다. 원문: `      SUBROUTINE RFCEDGE(RFCI,NS,IG,IEDQ,IELQ,POS,F)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION X(3,3),POS(3,*),IG(2),RL(2),E(3),V(3),RF(3),F(3),KN(4)` (4); `     &         ,RFCI(3,*),IELQ(4,*)` (5). `      X(:,1:2) = POS(:,IG(:))` (7). `      X(:,3)   = POS(:,NS)` (8). `      CALL LENCD(RL(2),V,X)` (10). `      RL(1) = 1.D0 - RL(2)` (11). `      E(:) = X(:,2) - X(:,1)` (13). `      CALL DIRCOS(E,E,3)` (14). `      RF(:) = F(:) - DOT_PRODUCT(F,E) * E(:)` (16). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/dircos.f:8–15`(E 정규화). [11-04 전수 검증 보완] |
| 18–25 | 시작 시 1행 RFCEDGE 루틴 안. IEDQ=0이면 변 두 절점 RFCI에서 RL 가중 RF를 뺀다(18–24). 원문: `      IF( IEDQ == 0 ) THEN` (18). `        KN(1:2) = IG(:)` (20). `        DO I = 1, 2` (22). `          RFCI(:,KN(I)) = RFCI(:,KN(I)) - RL(I) * RF(:)` (23). `        ENDDO` (24). |
| 26–56 | 시작 시 1행 RFCEDGE 루틴·18행 `IF( IEDQ == 0 ) THEN`의 ELSE 분기에 진입한다. 이 IF는 54행 `ENDIF`에서 닫힌다. IG(1)의 사각형 위치로 KN을 구성한다(28–46). 첫 절점에는 RL(1) 항과 .25D0*RL(2) 항을 적용하고 나머지 세 절점에는 .25D0*RL(2) 항을 적용한다(48–52). 분기 종료와 END를 포함한다. 원문: `      ELSE` (26). `        KN(1) = IG(1)` (28). `        IF( IG(1) == IELQ(1,IEDQ) ) THEN` (30). `          KN(2)=IELQ(2,IEDQ)` (31). `          KN(3)=IELQ(3,IEDQ)` (32). `          KN(4)=IELQ(4,IEDQ)` (33). `        ELSEIF( IG(1) == IELQ(2,IEDQ) ) THEN` (34). `          KN(2)=IELQ(1,IEDQ)` (35). `          KN(3)=IELQ(3,IEDQ)` (36). `          KN(4)=IELQ(4,IEDQ)` (37). `        ELSEIF( IG(1) == IELQ(3,IEDQ) ) THEN` (38). `          KN(2)=IELQ(1,IEDQ)` (39). `          KN(3)=IELQ(2,IEDQ)` (40). `          KN(4)=IELQ(4,IEDQ)` (41). `        ELSEIF( IG(1) == IELQ(4,IEDQ) ) THEN` (42). `          KN(2)=IELQ(1,IEDQ)` (43). `          KN(3)=IELQ(2,IEDQ)` (44). `          KN(4)=IELQ(3,IEDQ)` (45). `        ENDIF` (46). 연속문(48–49): `        RFCI(:,KN(1)) = RFCI(:,KN(1)) - RL(1) * RF(:)` (48); `     &                    - .25D0*RL(2)*RF(:)` (49). `        RFCI(:,KN(2)) = RFCI(:,KN(2)) - .25D0*RL(2)*RF(:)` (50). `        RFCI(:,KN(3)) = RFCI(:,KN(3)) - .25D0*RL(2)*RF(:)` (51). `        RFCI(:,KN(4)) = RFCI(:,KN(4)) - .25D0*RL(2)*RF(:)` (52). `      ENDIF` (54). `      END` (56). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–46: IG(1)이 사각형 네 절점과 모두 다를 때 KN(2:4)를 설정하는 ELSE가 없다.
