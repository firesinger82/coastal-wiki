---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/faceout.f
lines: 70
sha256: 930399a2c34c9b63128c7f51b5d62209feede8578e6c27d31757611cb91c7a27
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# faceout.f — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 루틴·암시적 자료형·배열과 TOL1=1.D-10, TOL2=1.D-6을 DATA로 선언한다(1–7). RLCORR로 POSSO·POSO에 대한 보정된 면적 좌표(area coordinates)를 구하고 면 절점 번호를 N에 저장한다(9–13). 원문: `      SUBROUTINE FACEOUT(ISLV,RSLV,POSSO,RLN,IELC,IEDG,IELA,POSO,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IELC(3),POSO(3,*),RLO(3),RLN(3),RLX(3),ISLV(2),RSLV(3)` `     &         ,IEDG(6,*),IELA(3),N(3),POSSO(3)` (4–5, 하나의 고정형식 연속문); `      DATA TOL1 / 1.D-10 /` (6); `      DATA TOL2 / 1.D-6 /` (7); `      CALL RLCORR(RLO,POSSO,IELC,POSO)` (9); `      N(1) = IELC(1)` (11); `      N(2) = IELC(2)` (12); `      N(3) = IELC(3)` (13). 면적 좌표 보정의 근거는 같은 contact 디렉터리의 `rlcorr.f:12–43`이다. [11-04 전수 검증 정정] [11-04 전수 검증 보완] |
| 15–70 | 시작 시 1행 FACEOUT 루틴 안이다. 세 면적 좌표 성분을 순회하며 I2·I3을 순환 선택한다(15–27). 변화량 DRL의 절댓값이 TOL1 미만이면 건너뛰고 경계 교차 비율 S와 교차 좌표를 계산한다(29–34). S가 열린 구간 (0,1)에 있고 교차 좌표가 [0,1]이면 모서리 방향에 맞춰 T를 정한다(36–47). TOL2의 끝점 범위면 상태 11, 나머지는 상태 12와 RSLV(1)=T를 저장하고 반환한다(49–61). 교차를 찾지 못하면 오류 출력 후 ERRSTP를 호출한다(67–68). 루틴을 끝낸다(70). 원문: `      DO I1 = 1, 3` (15); `        SELECT CASE(I1)` (17); `        CASE(1)` (18); `          I2 = 2` (19); `          I3 = 3` (20); `        CASE(2)` (21); `          I2 = 3` (22); `          I3 = 1` (23); `        CASE(3)` (24); `          I2 = 1` (25); `          I3 = 2` (26); `        DRL = RLO(I1) - RLN(I1)` (29); `        IF( DABS(DRL) < TOL1 ) CYCLE` (30); `        S = RLO(I1)/DRL` (32); `        RLX(I2) = ( 1. - S )*RLO(I2) + S*RLN(I2)` (33); `        RLX(I3) = 1. - RLX(I2)` (34); `        IF( ( S > 0.D0 .AND. S < 1.D0 ) .AND.` `     &      ( RLX(I2) >= 0.D0 .AND. RLX(I2) <= 1.D0 ) ) THEN` (36–37, 하나의 고정형식 연속문); `          IEDGE = IELA(I1)` (39); `          IG1 = IEDG(1,IEDGE)` (40); `          IG2 = IEDG(2,IEDGE)` (41); `          IF( IG1 == N(I2) ) THEN` (43); `            T = RLX(I3)` (44); `          ELSE` (45); `            T = RLX(I2)` (46); `          IF( T < TOL2 ) THEN` (49); `            ISLV(1) = 11` (50); `            ISLV(2) = IG1` (51); `          ELSEIF( T > 1.-TOL2 ) THEN` (52); `            ISLV(1) = 11` (53); `            ISLV(2) = IG2` (54); `          ELSE` (55); `            ISLV(1) = 12` (56); `            ISLV(2) = IEDGE` (57); `            RSLV(1) = T` (58); `      WRITE(ITO,'(/X,A)') 'STOP IN SUB. FACEOUT!'` (67); `      CALL ERRSTP(90,ITO)` (68). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–7: 두 허용값은 DATA 상수로 고정되어 있다.
