---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/estfedge.f
lines: 129
sha256: 80fdf41fbfe1c80747eac5734d2898f96d63c9d513ce99e8e0d44d8bf881ba61
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfedge.f — 판독 구간 기록

구간은 1행부터 129행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 루틴·암시적 자료형과 인수 및 작업 배열을 선언한다(1–6). ND=3으로 두 끝점·접촉점 번호를 KN에 넣는다(8–11). DU는 UG(1:3,KN(1:3))에서 U0을 뺀 배열이다(13). VR은 DU(:,3)에서 I=1,2의 `RL0(I) * DU(:,I)`를 차례로 뺀 뒤 DT로 나눈 값이다(15–19). VECML2로 AVR을 구한다(21). 해석: UG와 U0을 변위로 보고 DT를 시간 간격으로 보면 VR은 가중 상대 속도이다. 원문: `      SUBROUTINE ESTFEDGE(ND,KN,ESTF,NS,IG,IEDQ,IELQ,U0,RL0,RMU0,AVR0` `     &                   ,FN,RKF,UG,DT,IFMDL)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION KN(5),DU(3,3),UG(6,*),U0(3,3),IG(2),RL0(2),VR(3)` `     &         ,A(3,3),RK(9,9),ESTF(*),TR(9,15),WK(15,9),IELQ(4,*)` (5–6, 하나의 고정형식 연속문); `      ND = 3` (8); `      KN(1:2) = IG(:)` (10); `      KN(3) = NS` (11); `      DU(:,:) = UG(1:3,KN(1:3)) - U0(:,:)` (13); `      VR(:) = DU(:,3)` (15); `      DO I = 1, 2` (16); `        VR(:) = VR(:) - RL0(I) * DU(:,I)` (17); `      VR(:) = VR(:) / DT` (19); `      CALL VECML2(AVR,VR,3)` (21). [11-04 전수 검증 정정] |
| 23–60 | 시작 시 1행 ESTFEDGE 루틴 안이다. IFMDL=1에서 AVR/AVR0<1.D-10이면 A를 0으로 초기화한 뒤 대각 성분에 `RMU0 / DASIN(1.D0) * FN / AVR0`를 대입한다(23–31). ELSE에서는 DATAN과 유리식으로 C1·C2·C3을 만들고 외적 항과 대각 항을 합쳐 A를 구한다(33–49). IFMDL=2이면 A를 0으로 초기화하고 대각값을 RKF로 설정한다(51–59). 원문: `      IF( IFMDL == 1 ) THEN` (23); `        IF( AVR / AVR0 < 1.D-10 ) THEN` (25); `          A(:,:) = 0.` (27); `          DO I = 1, 3` (29); `            A(I,I) = RMU0 / DASIN(1.D0) * FN / AVR0` (30); `        ELSE` (33); `          C1 = RMU0 / DASIN(1.D0) * FN / AVR` (35); `          C2 = ( 1.D0 / ( 1.D0 + ( AVR / AVR0 ) * ( AVR / AVR0 ) ) /AVR0` `     &           - DATAN( AVR / AVR0 ) / AVR ) / AVR` (36–37, 하나의 고정형식 연속문); `          C3 = DATAN( AVR / AVR0 )` (38); `          DO I = 1, 3` (40); `            DO J = 1, 3` (41); `              A(I,J) = VR(I) * VR(J) * C2` (42); `              IF( I == J ) A(I,J) = A(I,J) + C3` (43); `          A(:,:) = C1 * A(:,:)` (47); `      ELSEIF( IFMDL == 2 ) THEN` (51); `        A(:,:) = 0.` (53); `        DO I = 1, 3` (55); `          A(I,I) = RKF` (56). [11-04 전수 검증 정정] |
| 61–99 | 시작 시 1행 ESTFEDGE 루틴 안이다. 세 절점의 FI·FJ를 접촉점에서 1, 나머지에서 -RL0으로 정하여 3×3 블록을 RK 상부에 넣는다(61–85). RK를 DT로 나누고 상삼각 성분을 ESTF에 순차 저장한다(87–96). IEDQ=0이면 반환한다(98). 원문: `      DO I = 1, 3` (61); `        IP = 3*(I-1) + 1` (63); `        IF( I == 3 ) THEN` (65); `          FI = 1.D0` (66); `        ELSE` (67); `          FI = -RL0(I)` (68); `        DO J = I, 3` (71); `          JP = 3*(J-1) + 1` (73); `          IF( J == 3 ) THEN` (75); `            FJ = 1.D0` (76); `          ELSE` (77); `            FJ = -RL0(J)` (78); `          RK( IP:IP+2, JP:JP+2 ) = FI * FJ * A(:,:)` (81); `      RK(:,:) = RK(:,:) / DT` (87); `      IP = 0` (89); `      DO I = 1, 9` (91); `        DO J = I, 9` (92); `          IP = IP + 1` (93); `          ESTF(IP) =  RK(I,J)` (94); `      IF( IEDQ == 0 ) RETURN` (98). |
| 100–129 | 시작 시 1행 ESTFEDGE 루틴 안이다. IEDQ=0 반환을 지나온 경로에서 ND=5로 바꾼다(100). IG(1)의 사각 면 내 위치에 따라 나머지 세 절점 번호를 고르고 접촉점 NS를 마지막에 놓는다(102–122). TREDGE와 두 MATML 호출로 ESTF를 변환한다(124–127). 루틴을 끝낸다(129). 원문: `      ND = 5` (100); `      KN(1) = IG(1)` (102); `      IF( IG(1) == IELQ(1,IEDQ) ) THEN` (104); `        KN(2)=IELQ(2,IEDQ)` (105); `        KN(3)=IELQ(3,IEDQ)` (106); `        KN(4)=IELQ(4,IEDQ)` (107); `      ELSEIF( IG(1) == IELQ(2,IEDQ) ) THEN` (108); `        KN(2)=IELQ(1,IEDQ)` (109); `        KN(3)=IELQ(3,IEDQ)` (110); `        KN(4)=IELQ(4,IEDQ)` (111); `      ELSEIF( IG(1) == IELQ(3,IEDQ) ) THEN` (112); `        KN(2)=IELQ(1,IEDQ)` (113); `        KN(3)=IELQ(2,IEDQ)` (114); `        KN(4)=IELQ(4,IEDQ)` (115); `      ELSEIF( IG(1) == IELQ(4,IEDQ) ) THEN` (116); `        KN(2)=IELQ(1,IEDQ)` (117); `        KN(3)=IELQ(2,IEDQ)` (118); `        KN(4)=IELQ(3,IEDQ)` (119); `      KN(5) = NS` (122); `      CALL TREDGE(TR)` (124); `      CALL MATML(WK,2,TR,3,ESTF,1,15,9,9)` (126); `      CALL MATML(ESTF,1,WK,2,TR,2,15,15,9)` (127). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·25–38·87: DT와 AVR0를 분모로 사용하며 이 파일 안에는 두 값의 0 여부 검사가 없다.
- 23–59: IFMDL이 1·2 이외이면 A를 설정하는 분기가 없다.
- 61–87: RK의 아래쪽 비대각 블록을 대입하는 문장은 없으며 87행은 RK 전체를 DT로 나눈다. ESTF 저장은 상삼각 성분만 읽는다(91–96).
- 104–120: IG(1)이 IELQ의 네 절점과 모두 다를 때 KN(2:4)를 지정하는 ELSE가 없다.
