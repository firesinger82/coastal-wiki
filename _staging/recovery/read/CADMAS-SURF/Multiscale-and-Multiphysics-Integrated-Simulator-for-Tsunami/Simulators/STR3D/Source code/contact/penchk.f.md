---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/penchk.f
lines: 65
sha256: 53210b6c573dbc8b9db24b5a71bc4185a8f7388dc15e1f44479b1f06f1f28c90
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# penchk.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | PENCHK는 이전·새 종속 절점(slave node) 좌표를 XYZO,XYZN의 네 번째 열로 복사한다(13–14). AREAIN을 LOGICAL로 선언한다(11). 인수·배열 선언과 구분 주석을 포함한다. 원문: 연속문(1–3): `      SUBROUTINE PENCHK(ISLV,RSLV,POSSO,POSSN,EN,IBDY,NBDY,ICBD,IELC` (1); `     &                 ,IELCB,IEDG,IELA,ICELA,ICEL,IBTE,GELC,ICTB,POSO` (2); `     &                 ,POSN,TOLA,IPFLG)` (3). `      IMPLICIT REAL*8(A-H,O-Z)` (5). 연속문(6–10): `      DIMENSION IELC(3,*),GELC(*),POSO(3,*),POSN(3,*),XYZO(3,4)` (6); `     &         ,XYZN(3,4),RSLV(3),ISLV(2),RL(3),ICTB(NBDY,NBDY)` (7); `     &         ,ICBD(NBDY),RLO(3),RLN(3),RNO(3),RNN(3),GXN(3)` (8); `     &         ,ICELA(2,*),ICEL(*),IBTE(4,*),IEDG(6,*),IELA(3,*),EN(3)` (9); `     &         ,POSSO(3),POSSN(3),IELCB(*)` (10). `      LOGICAL AREAIN` (11). `      CALL SHIFT1(XYZO(1,4),POSSO,3)` (13). `      CALL SHIFT1(XYZN(1,4),POSSN,3)` (14). |
| 16–41 | 시작 시 1–3행 PENCHK 루틴 안. ICTB=0인 물체 쌍을 제외한다(16–18). ICBD로 상대 물체의 면(face) 범위를 정한다(20–27). IPFLG=1이고 IELCB(I)=0이면 해당 면을 건너뛴다(29–31). 이 검사에서 건너뛰지 않은 면의 좌표는 IPFLG 값과 무관하게 복사한다(33–36). 새 면 중심 GXN과의 거리가 2*GELC보다 크면 건너뛴다(38–40). 원문: `      DO 100 JBDY=1,NBDY` (16). `        IF(ICTB(IBDY,JBDY) .EQ. 0) GOTO 100` (18). `        IF(JBDY .EQ. 1) THEN` (20). `          IS=1` (21). `        ELSE` (22). `          IS=ICBD(JBDY-1)+1` (23). `        ENDIF` (24). `        IE=ICBD(JBDY)` (25). `        DO 110 I=IS,IE` (27). `          IF(IPFLG .EQ. 1) THEN` (29). `            IF(IELCB(I) .EQ. 0) GOTO 110` (30). `          ENDIF` (31). `          DO 111 J=1,3` (33). `            CALL SHIFT1(XYZO(1,J),POSO(1,IELC(J,I)),3)` (34). `            CALL SHIFT1(XYZN(1,J),POSN(1,IELC(J,I)),3)` (35). `  111     CONTINUE` (36). `          GXN(:) = ( XYZN(:,1) + XYZN(:,2) + XYZN(:,3) ) / 3.D0` (38). `          CALL LENGTH(DIST,XYZN(1,4),GXN,3)` (39). `          IF( DIST .GT. 2.D0*GELC(I) ) GOTO 110` (40). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/length.f:6–12`(거리), `util/shift1.f:16–18`(복사). [11-04 전수 검증 정정] |
| 42–65 | 시작 시 1–3행 PENCHK 루틴·16행 `DO 100 JBDY=1,NBDY`와 27행 `DO 110 I=IS,IE` 안. I 루프는 GOTO 110의 목적지인 61행 `110 CONTINUE`에서 닫힌다. JBDY 루프는 GOTO 100의 목적지인 63행 `100 CONTINUE`에서 닫힌다. AREACD로 이전·새 좌표의 RLO,RNO,HO와 RLN,RNN,HN을 구한다(42–43). HO<=1.D-10이고 HN>1.D-10이면 T를 계산하여 RMULT5로 RL을 보간한다(45–48). AREAIN과 GRAZEEL의 ICHK=1을 모두 만족하면 PENST를 호출하고 즉시 반환한다(50–57). 조건과 루프 종료 및 END를 포함한다. 원문: `          CALL AREACD(RLO,RNO,HO,XYZO)` (42). `          CALL AREACD(RLN,RNN,HN,XYZN)` (43). `          IF( HO .LE. 1.D-10 .AND. HN .GT. 1.D-10 ) THEN` (45). `            T = ( 1.D-10 - HO )/( HN - HO )` (47). `            CALL RMULT5(RL,1.D0-T,RLO,T,RLN,3)` (48). `            IF( AREAIN(RL,1.D-10) ) THEN` (50). `              CALL GRAZEEL(ICHK,POSSN,RL,IELC(1,I),ICELA,ICEL,IBTE,POSN)` (51). `              IF( ICHK .EQ. 1 ) THEN` (52). 연속문(53–54): `                CALL PENST(ISLV,RSLV,IEDG,IELA(1,I),I,RL,XYZN,RNN,POSN` (53); `     &                    ,EN,TOLA)` (54). `                RETURN` (55). `              ENDIF` (56). `            ENDIF` (57). `          ENDIF` (59). `  110   CONTINUE` (61). `  100 CONTINUE` (63). `      END` (65). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/rmult5.f:8–10`(가중합). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40·45·47·50: 거리 제한 계수 2.D0과 교차·영역 판정 상수 1.D-10이 코드에 직접 들어 있다.
- 53–55: 첫 PENST 호출 뒤 즉시 반환하며 이후 후보 면은 탐색하지 않는다.
