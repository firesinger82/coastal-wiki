---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/etabm.f
lines: 91
sha256: ab4f462bdde25e2044c07bb27f7b4bcd1e66d940ebe8842bb11bbf733c445c81
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# etabm.f — 판독 구간 기록

구간은 1행부터 91행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 해석: ETABM은 보의 응력 강성에 쓰는 E를 계산한다. 배열을 선언하고 단위행렬 RI를 준비한다. UX·UY·UZ를 복사한 뒤 각각 1·2·3번 성분에 1을 더한다. 해석: 이 벡터들은 변위 기울기 보정 벡터이다. CXX·CXY·CXZ를 0으로 한다. 원문: `      SUBROUTINE ETABM(E,S,T,RL,D1,D2,VST,VTT,BX,BY,BZ,UX,UY,UZ)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(4–8): `      DIMENSION RI(3,3),UX(3),UY(3),UZ(3),UXD(3),UYD(3),UZD(3)` (4)； `     &         ,CXX(12,12),CXY(12,12),CXZ(12,12),WK1(3,3),WK2(3,3)` (5)； `     &         ,WK3(3,3),WK4(3,3),WK5(3,3),WK6(3,3),VST(3,2),VTT(3,2)` (6)； `     &         ,BX(3,12),BY(3,12),BZ(3,12),BXTBX(12,12),BXTBY(12,12)` (7)； `     &         ,BXTBZ(12,12),E(78,3)` (8)； `      RI(:,:) = 0.` (10)； `      RI(1,1) = 1.D0` (12)； `      RI(2,2) = 1.D0` (13)； `      RI(3,3) = 1.D0` (14)； `      UXD(:) = UX(:)` (16)； `      UYD(:) = UY(:)` (17)； `      UZD(:) = UZ(:)` (18)； `      UXD(1) = UXD(1) + 1.D0` (20)； `      UYD(2) = UYD(2) + 1.D0` (21)； `      UZD(3) = UZD(3) + 1.D0` (22)； `      CXX(:,:) = 0.` (24)； `      CXY(:,:) = 0.` (25)； `      CXZ(:,:) = 0.` (26)。 [11-04 전수 검증 정정] |
| 28–72 | 시작 시 1행 ETABM 루틴 안이다. I=1일 때 IS:IE는 4:6이고 P는 -.5D0이다. I=2일 때 IS:IE는 10:12이고 P는 .5D0이다. 해석: 이 범위는 두 절점의 회전 성분에 대응한다. AXB와 VECML1을 호출한다. CXX·CXY·CXZ의 해당 대각 블록을 계산한다. 해석: AXB 호출은 열벡터와 행벡터의 곱을 계산하고 VECML1 호출은 내적을 계산한다. 원문: `      DO I = 1, 2` (28)； `        IS = 3 + 6 * ( I - 1 ) + 1` (30)； `        IE = IS + 2` (31)； `        SELECT CASE( I )` (33)； `        CASE( 1 )` (34)； `          P = -.5D0` (35)； `        CASE( 2 ) ` (36)； `          P = .5D0` (37)； `        END SELECT` (38)； `        CALL AXB(WK1,VST(1,I),UXD,3,1,3)` (40)； `        CALL AXB(WK2,VTT(1,I),UXD,3,1,3)` (41)； `        CALL VECML1(C1,VST(1,I),UXD,3)` (43)； `        CALL VECML1(C2,VTT(1,I),UXD,3)` (44)； 연속문(46–48): `        CXX(IS:IE,IS:IE)` (46)； `     &  = .5D0 / RL * P * ( S * D1 * ( WK1(:,:) - C1 * RI(:,:) )` (47)； `     &                    + T * D2 * ( WK2(:,:) - C2 * RI(:,:) ) )` (48)； `        CALL AXB(WK3,VST(1,I),UYD,3,1,3)` (50)； `        CALL AXB(WK4,VTT(1,I),UYD,3,1,3)` (51)； `        CALL VECML1(C3,VST(1,I),UYD,3)` (53)； `        CALL VECML1(C4,VTT(1,I),UYD,3)` (54)； 연속문(56–59): `        CXY(IS:IE,IS:IE)` (56)； `     &  = .125D0 * ( WK1(:,:) - C1 * RI(:,:) )` (57)； `     &    + .25D0 / RL * P * ( S * D1 * ( WK3(:,:) - C3 * RI(:,:) )` (58)； `     &                       + T * D2 * ( WK4(:,:) - C4 * RI(:,:) ) )` (59)； `        CALL AXB(WK5,VST(1,I),UZD,3,1,3)` (61)； `        CALL AXB(WK6,VTT(1,I),UZD,3,1,3)` (62)； `        CALL VECML1(C5,VST(1,I),UZD,3)` (64)； `        CALL VECML1(C6,VTT(1,I),UZD,3)` (65)； 연속문(67–70): `        CXZ(IS:IE,IS:IE)` (67)； `     &  = .125D0 * ( WK2(:,:) - C2 * RI(:,:) )` (68)； `     &    + .25D0 / RL * P * ( S * D1 * ( WK5(:,:) - C5 * RI(:,:) )` (69)； `     &                       + T * D2 * ( WK6(:,:) - C6 * RI(:,:) ) )` (70)； `      ENDDO` (72)。 [11-04 전수 검증 정정] |
| 73–91 | 시작 시 1행 ETABM 루틴 안이며 28행 I 루프 밖이다. MATML을 세 번 호출한다. 해석: 각 호출은 BX의 전치와 BX·BY·BZ의 곱을 구한다. 상삼각 순서로 C 행렬의 대칭 합과 곱을 E의 세 열에 저장한다. 마지막 빈 줄도 포함한다. 원문: `      CALL MATML(BXTBX,2,BX,3,BX,2,12,12,3)` (74)； `      CALL MATML(BXTBY,2,BX,3,BY,2,12,12,3)` (75)； `      CALL MATML(BXTBZ,2,BX,3,BZ,2,12,12,3)` (76)； `      IP = 0` (78)； `      DO I = 1, 12` (80)； `        DO J = I, 12` (81)； `          IP = IP + 1` (82)； `          E(IP,1) = CXX(I,J) + CXX(J,I) + BXTBX(I,J)` (83)； `          E(IP,2) = CXY(I,J) + CXY(J,I) + .5D0*(BXTBY(I,J)+BXTBY(J,I))` (84)； `          E(IP,3) = CXZ(I,J) + CXZ(J,I) + .5D0*(BXTBZ(I,J)+BXTBZ(J,I))` (85)； `        ENDDO` (86)； `      ENDDO` (87)； `      END` (89)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–31·46–70: CXX·CXY·CXZ에서 직접 채우는 블록의 첨자 범위는 I=1일 때 4:6이고 I=2일 때 10:12이다.
