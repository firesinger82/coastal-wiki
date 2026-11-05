---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_recv_cont.f
lines: 116
sha256: 74ec8df0e1900d0ba36a40f6e185d858d009df94099a22a9976b82541a5e0299
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_recv_cont.f — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | SF_RECV_CONT의 선언부다. 루트(root)가 ICON을 받아 양수 값을 1로 정규화한다(15–18). VF_P1BCSI로 배포한 뒤 ICON=0 또는 MYRANK>0이면 반환한다(20–22). 루트가 NICRG·NNCRG와 ICRG·ICSF·ICTB를 받는다(24–34). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_RECV_CONT()` (1); `      USE SF_ARRAY` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_APARAI.h'` (8); `      INCLUDE 'SF_STRUCT.h'` (9); `      DIMENSION IP(3),JP(4),X(3,3)` (11); `      INTEGER, POINTER :: ICSF(:,:)` (13); `      IF( MYRANK == 0 ) THEN` (15); `        CALL SF_C_MPI_RECV_I(ICON,1,IROOTS)` (16); `        IF( ICON > 0 ) ICON = 1` (17); `      ENDIF` (18); `      CALL VF_P1BCSI(ICON,1,0)` (20); `      IF( ICON == 0 .OR. MYRANK > 0 ) RETURN` (22); `      CALL SF_C_MPI_RECV_I(NICRG,1,IROOTS)` (24); `      CALL SF_C_MPI_RECV_I(NNCRG,1,IROOTS)` (25); `      ALLOCATE( ICRG(NICRG), STAT=IERR )` (27); `      ALLOCATE( ICSF(5,NNCRG), STAT=IERR )` (28); `      ALLOCATE( ICTB(NICRG,NICRG), STAT=IERR )` (29); `      IF( IERR /= 0 ) CALL VF_A2ERR('SF_RECV_CONT','CAN NOT ALLOC.')` (30); `      CALL SF_C_MPI_RECV_I(ICRG,NICRG,IROOTS)` (32); `      CALL SF_C_MPI_RECV_I(ICSF,5*NNCRG,IROOTS)` (33); `      CALL SF_C_MPI_RECV_I(ICTB,NICRG*NICRG,IROOTS)` (34). |
| 36–54 | 시작 시 1행 SF_RECV_CONT 루틴 안. SF_RECV_CONT 안이며 22행 조기 반환을 통과한 상태다. ICSF의 삼각면은 1개, 사각면은 삼각면 2개로 계산하여 NCTR을 구한다(41–48). ICTR(4,NCTR)을 할당하고 J를 0으로 초기화한다(50–53). 원문(연속 표시는 앞 문장에 이어짐): `      ! ICSF の４角形面は２つの３角形面に分割して ICTR にセット` (36) (ICSF의 사각형 면을 삼각형 면 두 개로 나누어 ICTR에 설정); `      !      の３角形面は３角形面のまま` (37) (ICSF의 삼각형 면은 삼각형 그대로 둠); `      NCTR = 0` (39); `      DO I = 1, NNCRG` (41); `        SELECT CASE( ICSF(1,I) )` (42); `        CASE( 3 )` (43); `          NCTR = NCTR + 1` (44); `        CASE( 4 )` (45); `          NCTR = NCTR + 2` (46); `        END SELECT` (47); `      ENDDO` (48); `      ALLOCATE( ICTR(4,NCTR), STAT=IERR )` (50); `      IF( IERR /= 0 ) CALL VF_A2ERR('SF_RECV_CONT','CAN NOT ALLOC.')` (51); `      J = 0` (53). |
| 55–90 | 시작 시 1행 SF_RECV_CONT 루틴 안. SF_RECV_CONT 안이며 앞 계수 루프 밖. IBDY=1,NICRG 루프에서 IS·IE를 정한다(55–63). 삼각면은 절점 순서를 뒤집고 사각면은 두 삼각형으로 나누어 ICTR에 넣는다(65–82). ICRG를 새 삼각면 누계로 바꾸고 ICSF를 해제한다(84–89). 원문(연속 표시는 앞 문장에 이어짐): `      DO IBDY = 1, NICRG` (55); `        IF( IBDY == 1 ) THEN` (57); `          IS = 1` (58); `        ELSE` (59); `          IS = IE + 1` (60); `        ENDIF` (61); `        IE = ICRG(IBDY)` (63); `        DO I = IS, IE` (65); `          SELECT CASE( ICSF(1,I) )` (66); `          CASE( 3 )` (67); `            J = J + 1` (68); `            ICTR(2,J) = ICSF(4,I)` (69); `            ICTR(3,J) = ICSF(3,I)` (70); `            ICTR(4,J) = ICSF(2,I)` (71); `          CASE( 4 )` (72); `            J = J + 1` (73); `            ICTR(2,J) = ICSF(2,I)` (74); `            ICTR(3,J) = ICSF(4,I)` (75); `            ICTR(4,J) = ICSF(3,I)` (76); `            J = J + 1` (77); `            ICTR(2,J) = ICSF(2,I)` (78); `            ICTR(3,J) = ICSF(5,I)` (79); `            ICTR(4,J) = ICSF(4,I)` (80); `          END SELECT` (81); `        ENDDO` (82); `        ICRG(IBDY) = J  ! ICRG セットし直し(ICSF用 -> ICTR用)` (84) (ICRG를 ICSF용에서 ICTR용으로 다시 설정); `      ENDDO` (86); `      DEALLOCATE( ICSF, STAT=IERR )` (88); `      IF( IERR /= 0 ) CALL VF_A2ERR('SF_RECV_CONT','CAN NOT DEALLOC.')` (89). 해석: IBDY는 물체 번호로 읽힌다. [11-04 전수 검증 정정] |
| 91–104 | 시작 시 1행 SF_RECV_CONT 루틴 안. SF_RECV_CONT 안이며 앞 물체 루프 밖. 각 삼각면과 외표면을 SF_COLTR로 대조한다(91–96). IBING=1이면 ICTR 첫 행에 외표면 번호를 저장하고 103행 레이블 10의 ENDDO로 이동한다(97–100). 찾지 못하면 VF_A2ERR를 호출한다(102). 원문(연속 표시는 앞 문장에 이어짐): `      DO I = 1, NCTR` (91); `        IP(:) = ICTR(2:4,I)` (92); `        DO J = 1, NPFC0` (93); `          NP = IPFACE0(4,J)` (94); `          JP(1:NP) = IPFACE0(5:4+NP,J)` (95); `          CALL SF_COLTR(IBING,IP,JP,NP)` (96); `          IF( IBING == 1 ) THEN` (97); `            ICTR(1,I) = J` (98); `            GOTO 10` (99); `          ENDIF` (100); `        ENDDO` (101); `        CALL VF_A2ERR('SF_RECV_CONT','P.G ERROR.')` (102); `   10 ENDDO` (103). [11-04 전수 검증 보완] |
| 105–116 | 시작 시 1행 SF_RECV_CONT 루틴 안. SF_RECV_CONT 안이며 앞 대조 루프 밖. SF_STRIA(S,X,3)를 호출한 뒤 DSQRT(2.D0*S)를 E_MEAN에 누적한다(105–112). NCTR로 나누어 E_MEAN을 계산한다(114). 원문(연속 표시는 앞 문장에 이어짐): `      E_MEAN = 0.` (105); `      DO I = 1, NCTR` (107); `        X(:,:) = POS0(:,ICTR(2:4,I))` (108); `        CALL SF_STRIA(S,X,3)` (109); `        EDGE = DSQRT(2.D0*S)` (110); `        E_MEAN = E_MEAN + EDGE` (111); `      ENDDO` (112); `      E_MEAN = E_MEAN / NCTR` (114); `      END` (116). 해석: S는 삼각형 면적으로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–30: 세 ALLOCATE가 같은 IERR를 사용하며 세 번째 호출 뒤에만 IERR 검사가 있다.
- 11·94–96: JP의 크기는 4이며 NP는 IPFACE0(4,J)에서 받는다. JP(1:NP) 복사 앞에는 NP<=4 검사문이 없다.
- 41–47·66–81: ICSF 절점 수 SELECT CASE에는 3·4만 있으며 CASE DEFAULT가 없다.
- 114: E_MEAN을 NCTR로 나눈다. 이 루틴에는 NCTR>0 검사문이 없다.
