---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/npfedge.f
lines: 95
sha256: abe363e776ba650560d53863d648e35ee7b4a93aed1ce896eca2f89ff8255be9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# npfedge.f — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | NPFEDGE는 변(edge)의 방향 E를 DIRCOS로 구하고 CROSS1(E,F,FN)을 호출한다(8–11). VR에는 DU(:,3)에서 두 RL0(I)*DU(:,I)를 뺀 결과를 DT로 나누어 넣는다(13–20). 해석: 이 식은 RL0 가중 주절점 변위에 대한 상대 속도를 구하는 식이다. VECML2로 AVR을 구하고 FT를 0으로 초기화한다(22–24). 인수와 배열 선언을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE NPFEDGE(MODE,FN,RKF,FRCI,NS,IG,IEDQ,IELQ,U0,RL0,RMU0` (1); `     &                  ,AVR0,RMUD,UG,POS,F,DT,IFMDL,EPSD,IDYN)` (2). `      IMPLICIT REAL*8(A-H,O-Z)` (4). 연속문(5–6): `      DIMENSION DU(3,3),UG(6,*),U0(3,3),IG(2),RL0(2),VR(3),FT(3)` (5); `     &         ,FRCI(3,*),V(3),POS(3,*),E(3),F(3),KN(4),IELQ(4,*)` (6). `      V(:) = POS(:,IG(2)) - POS(:,IG(1))` (8). `      CALL DIRCOS(E,V,3)` (9). `      CALL CROSS1(E,F,FN)` (11). `      DU(:,1:2) = UG(1:3,IG(:)) - U0(:,1:2)` (13). `      DU(:,3)   = UG(1:3,NS) - U0(:,3)` (14). `      VR(:) = DU(:,3)` (16). `      DO I = 1, 2` (17). `        VR(:) = VR(:) - RL0(I) * DU(:,I)` (18). `      ENDDO` (19). `      VR(:) = VR(:) / DT` (20). `      CALL VECML2(AVR,VR,3)` (22). `      FT(:) = 0.` (24). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/dircos.f:8–15`(정규화). [11-04 전수 검증 정정] |
| 26–52 | 시작 시 1–2행 NPFEDGE 루틴 안. IFMDL=1은 AVR/AVR0<1.D-10에서 선형 근사, 그 밖에는 DATAN으로 RMU를 구해 FT를 계산한다(26–33). IFMDL=2는 MODE=1일 때 IDYN=1 또는 0에 따라 RKF를 정하고 MODE=2로 바꾼다(35–47). 그 뒤 FT=RKF*VR을 적용한다(49). 원문: `      IF( IFMDL == 1 ) THEN` (26). `        IF( AVR / AVR0 < 1.D-10 ) THEN` (28). `          FT(:) = RMU0 / DASIN(1.D0) * FN / AVR0 * VR(:)` (29). `        ELSE` (30). `          RMU = RMU0 / DASIN(1.D0) * DATAN( AVR / AVR0 )` (31). `          FT(:) = RMU * FN * VR(:) / AVR` (32). `        ENDIF` (33). `      ELSEIF( IFMDL == 2 ) THEN` (35). `        IF( MODE == 1 ) THEN` (37). `          IF( IDYN == 1 ) THEN` (39). `            RKF = RMUD * FN / EPSD` (40). `          ELSEIF( IDYN == 0 ) THEN` (41). `            RKF = RMUD * FN / AVR0 * 1.D-1` (42). `          ENDIF` (43). `          MODE = 2` (45). `        ENDIF` (47). `        FT(:) = RKF * VR(:)` (49). `      ENDIF` (51). 26–51행 IFMDL 분기와 39–43행 IDYN 분기에는 ELSE가 없다. IFMDL이 1과 2가 아니면 FT는 24행의 0을 유지한다. 해석: RMU는 마찰계수이다. [11-04 전수 검증 보완] |
| 53–62 | 시작 시 1–2행 NPFEDGE 루틴 안. IEDQ=0이면 변 두 절점에 RL0 가중 FT를 빼고 NS에 FT를 더한다(53–61). 원문: `      IF( IEDQ == 0 ) THEN` (53). `        KN(1:2) = IG(:)` (55). `        DO I = 1, 2` (57). `          FRCI(:,KN(I)) = FRCI(:,KN(I)) - RL0(I) * FT(:)` (58). `        ENDDO` (59). `        FRCI(:,NS) = FRCI(:,NS) + FT(:)` (61). |
| 63–95 | 시작 시 1–2행 NPFEDGE 루틴·53행 `IF( IEDQ == 0 ) THEN`의 ELSE 분기에 진입한다. 이 IF는 93행 `ENDIF`에서 닫힌다. IG(1)을 기준으로 사각형 절점 KN을 구성한다(65–83). RL0(2) 항을 .25D0씩 네 절점에 나누고 첫 절점에는 RL0(1) 항도 뺀다(85–89). NS에는 FT를 더하고 끝낸다(91–95). 원문: `      ELSE` (63). `        KN(1) = IG(1)` (65). `        IF( IG(1) == IELQ(1,IEDQ) ) THEN` (67). `          KN(2)=IELQ(2,IEDQ)` (68). `          KN(3)=IELQ(3,IEDQ)` (69). `          KN(4)=IELQ(4,IEDQ)` (70). `        ELSEIF( IG(1) == IELQ(2,IEDQ) ) THEN` (71). `          KN(2)=IELQ(1,IEDQ)` (72). `          KN(3)=IELQ(3,IEDQ)` (73). `          KN(4)=IELQ(4,IEDQ)` (74). `        ELSEIF( IG(1) == IELQ(3,IEDQ) ) THEN` (75). `          KN(2)=IELQ(1,IEDQ)` (76). `          KN(3)=IELQ(2,IEDQ)` (77). `          KN(4)=IELQ(4,IEDQ)` (78). `        ELSEIF( IG(1) == IELQ(4,IEDQ) ) THEN` (79). `          KN(2)=IELQ(1,IEDQ)` (80). `          KN(3)=IELQ(2,IEDQ)` (81). `          KN(4)=IELQ(3,IEDQ)` (82). `        ENDIF` (83). 연속문(85–86): `        FRCI(:,KN(1)) = FRCI(:,KN(1)) - RL0(1) * FT(:)` (85); `     &                    - .25D0*RL0(2)*FT(:)` (86). `        FRCI(:,KN(2)) = FRCI(:,KN(2)) - .25D0*RL0(2)*FT(:)` (87). `        FRCI(:,KN(3)) = FRCI(:,KN(3)) - .25D0*RL0(2)*FT(:)` (88). `        FRCI(:,KN(4)) = FRCI(:,KN(4)) - .25D0*RL0(2)*FT(:)` (89). `        FRCI(:,NS) = FRCI(:,NS) + FT(:)` (91). `      ENDIF` (93). `      END` (95). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–32·40–42: AVR0 또는 EPSD를 분모로 쓰는 식 앞에 해당 값의 0 검사는 없다.
- 37–49: MODE=1이 아니면 RKF를 재설정하지 않고 FT 계산에 사용한다.
- 67–83: IG(1)이 사각형 네 절점과 모두 다를 때 KN(2:4)를 설정하는 ELSE가 없다.
