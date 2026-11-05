---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/istchk.f
lines: 97
sha256: 670277de8783523e17687c903e5ee2daf19f67b699c336c1f2890bd3ad92d38a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# istchk.f — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | 루틴·암시적 자료형·문자열·배열과 BLK·ICHK의 DATA 초기값을 선언한다(1–10). 현재·이전 상태의 첫 번째 성분만 비교하여 수렴(convergence) 여부 ICONV2를 정한다(12–18). 수렴·최대 반복 도달 여부에 따라 메시지를 고른다(20–26). 이전 상태 보정과 현재 상태의 MOD 연산으로 4×4 전이 행렬을 세고 출력한다(28–44). ICHK=0이면 반환한다(46). 원문: `      SUBROUTINE ISTCHK(ICONV2,NNOD,NINDC,INDG,IELC,INDC,IEDG,ISLV,ISLVO` `     &                 ,ISTEP,ITER2,MAXITER2,ITO)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      CHARACTER*14 MSGCONV,BLK` (5); `      DIMENSION ISLVO(2,NINDC),ISLV(2,NINDC),MASTERO(3),MASTER(3)` `     &         ,IEDG(6,*),IELC(3,*),INDC(NINDC),ISTMAT(4,4),INDG(NNOD)` (6–7, 하나의 고정형식 연속문); `      DATA BLK / '              ' /` (9); `      DATA ICHK / 0 /` (10); `      ICONV2 = 1` (12); `      DO I = 1, NINDC` (14); `        IF( ISLV(1,I) == ISLVO(1,I) ) CYCLE` (15); `        ICONV2 = 0` (16); `        EXIT` (17); `      IF( ICONV2 == 1 ) THEN` (20); `        MSGCONV = 'CONVERGED!'` (21); `      ELSEIF( ITER2 == MAXITER2 ) THEN` (22); `        MSGCONV = 'NOT CONVERGED!'` (23); `      ELSE` (24); `        MSGCONV = BLK` (25); `      ISTMAT(:,:) = 0` (28); `      DO I = 1, NINDC` (30); `        IOLD = ISLVO(1,I) + 1` (31); `        IF( IOLD >= 5 ) IOLD = IOLD - 2` (32); `        INEW = MOD(ISLV(1,I),10) + 1` (33); `        ISTMAT(IOLD,INEW) = ISTMAT(IOLD,INEW) + 1` (34); `      WRITE(ITO,'(/A,I0,2X,A//A)') ` `     &  '   * CONTACT ITER. = ', ITER2, MSGCONV,` `     &  '             FREE  POINT   EDGE   FACE'` (37–39, 하나의 고정형식 연속문); `      WRITE(ITO,'(A,4I7)') '      FREE', ISTMAT(1,:)` (41); `      WRITE(ITO,'(A,4I7)') '     POINT', ISTMAT(2,:)` (42); `      WRITE(ITO,'(A,4I7)') '      EDGE', ISTMAT(3,:)` (43); `      WRITE(ITO,'(A,4I7)') '      FACE', ISTMAT(4,:)` (44); `      IF( ICHK == 0 ) RETURN` (46). |
| 48–97 | 시작 시 1행 ISTCHK 루틴 안이다. ICHK=0 반환을 지나온 경로에서 장치 51에 단계·반복 정보를 쓰고 INDG 최댓값을 구한다(48–50). 바뀐 접촉만 대상으로 이전·현재 상태의 절점 목록을 선택한다(52–75). 원 절점은 INDG로, NNOD 초과 절점은 MAX_INDG 기반 식으로 번호를 바꾸고 상세 정보를 장치 51에 쓴다(77–93). 루프·루틴을 닫는다(95–97). 원문: `      WRITE(51,'(A,I6,I3)') 'STEP, ITER2 = ',ISTEP, ITER2` (48); `      MAX_INDG = MAXVAL( INDG )` (50); `      DO I = 1, NINDC` (52); `        IF( ISLV(1,I) == ISLVO(1,I) ) CYCLE` (54); `        MASTERO(:) = 0` (56); `        MASTER(:) = 0` (57); `        SELECT CASE( ISLVO(1,I) )` (59); `        CASE( 1 )` (60); `          MASTERO(1) = ISLVO(2,I)` (61); `        CASE( 2, 4 )` (62); `          MASTERO(1:2) = IEDG(1:2,ISLVO(2,I))` (63); `        CASE( 3, 5 )` (64); `          MASTERO(1:3) = IELC(1:3,ISLVO(2,I))` (65); `        SELECT CASE( ISLV(1,I) )` (68); `        CASE( 1, 11 )` (69); `          MASTER(1) = ISLV(2,I)` (70); `        CASE( 2, 12 )` (71); `          MASTER(1:2) = IEDG(1:2,ISLV(2,I))` (72); `        CASE( 3, 13 )` (73); `          MASTER(1:3) = IELC(1:3,ISLV(2,I))` (74); `        ISLAVE = INDG( INDC(I) )` (77); `        DO J = 1, 3` (79); `          IF( MASTERO(J) > 0 .AND. MASTERO(J) <= NNOD ) THEN` (80); `            MASTERO(J) = INDG( MASTERO(J) )` (81); `          ELSEIF( MASTERO(J) > NNOD ) THEN` (82); `            MASTERO(J) = MAX_INDG + MASTERO(J) - NNOD` (83); `          IF( MASTER(J) > 0 .AND. MASTER(J) <= NNOD ) THEN` (85); `            MASTER(J) = INDG( MASTER(J) )` (86); `          ELSEIF( MASTER(J) > NNOD ) THEN` (87); `            MASTER(J) = MAX_INDG + MASTER(J) - NNOD` (88); `        WRITE(51,'(I8,I6,4I8,I6,4I8)') ` `     &    ISLAVE,ISLVO(:,I),MASTERO(:),ISLV(:,I),MASTER(:)` (92–93, 하나의 고정형식 연속문). 59행 SELECT는 66행 END SELECT로 닫힌다. 68행 SELECT는 75행 END SELECT로 닫힌다. 두 SELECT에는 CASE DEFAULT가 없다. 80·82행 분기 사슬은 ELSE 없이 84행 ENDIF로 닫힌다. 85·87행 분기 사슬은 ELSE 없이 89행 ENDIF로 닫힌다. 따라서 MASTERO(J)·MASTER(J)의 0 이하 값은 번호 변환으로 바꾸지 않는다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·46: ICHK의 DATA 초기값은 0이고 이 파일에는 ICHK를 바꾸는 대입문이 없다. 상세 출력 경로 앞에는 ICHK==0 반환이 있다.
- 14–18: 수렴 비교는 ISLV(1,I)와 ISLVO(1,I)만 사용한다. 두 번째 성분은 비교하지 않는다. 두 번째 성분은 상태에 따라 절점 번호 또는 IEDG·IELC의 열 번호로 쓰인다(59–74). [11-04 전수 검증 정정]
- 31–34: IOLD는 5 이상에서 2를 빼지만 INEW는 MOD(ISLV(1,I),10)+1만 사용한다. ISTMAT 차원은 (4,4)이다(7).
