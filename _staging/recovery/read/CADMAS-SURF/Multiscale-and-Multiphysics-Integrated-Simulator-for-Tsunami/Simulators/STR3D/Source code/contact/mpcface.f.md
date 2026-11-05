---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcface.f
lines: 108
sha256: 9cc416ce4cc2d6f08c1a0b3981ba6ff8eb95950f6d08c14d20cd79a10b41f002
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcface.f — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | MPCFACE는 삼각형 두 변을 SUBVEC으로 구하고 CROSS2로 E를 구한다(8–10). E 성분 절댓값을 기준으로 ISRT를 정렬한다(12–23). 다점 구속(multipoint constraint, MPC) 배열 선언과 구분 주석을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE MPCFACE(IDEP,IDX,IRH,IS,NS,IELC,IFCQ,IELQ,INDOF,POS` (1); `     &                  ,ETOL,ITO)` (2). `      IMPLICIT REAL*8(A-H,O-Z)` (4). 연속문(5–6): `      DIMENSION POS(3,*),IELC(3),E(3),V12(3),V13(3),IDEP(2),IDX(2)` (5); `     &         ,IRH(2,*),ISRT(3),INDOF(3),IELQ(4,*),NDQ(4)` (6). `      CALL SUBVEC(V12,POS(1,IELC(2)),POS(1,IELC(1)),3)` (8). `      CALL SUBVEC(V13,POS(1,IELC(3)),POS(1,IELC(1)),3)` (9). `      CALL CROSS2(V12,V13,E)` (10). `      ISRT(1)=1` (12). `      DO 100 I=2,3` (13). `        DO 110 J=1,I-1` (14). `          JJ=ISRT(J)` (15). `          IF( DABS(E(I)) .GT. DABS(E(JJ)) ) THEN` (16). `            CALL SHIFTB0(ISRT,J,I-1,1)` (17). `            ISRT(J)=I` (18). `            GOTO 100` (19). `          ENDIF` (20). `  110   CONTINUE` (21). `        ISRT(I)=I` (22). `  100 CONTINUE` (23). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/subvec.f:9–11`(차), `util/shiftb0.f:5–7`(삽입 시 배열 이동). [11-04 전수 검증 보완] |
| 25–48 | 시작 시 1–2행 MPCFACE 루틴 안. INDOF와 ETOL로 종속 방향 J1과 나머지 J2,J3를 선택한다(25–42). 실패 시 ERRSTP(50,ITO)를 호출한다(40–41). IDEP를 NS,J1로 설정한다(46–47). 원문: `      IF( INDOF(ISRT(1)) .EQ. 0 ) THEN` (25). `        J1=ISRT(1)` (26). `        J2=ISRT(2)` (27). `        J3=ISRT(3)` (28). 연속문(29–30): `      ELSEIF( INDOF(ISRT(2)) .EQ. 0 .AND.` (29); `     &        DABS( E(ISRT(2)) ) .GT. ETOL ) THEN` (30). `        J1=ISRT(2)` (31). `        J2=ISRT(1)` (32). `        J3=ISRT(3)` (33). 연속문(34–35): `      ELSEIF( INDOF(ISRT(3)) .EQ. 0 .AND.` (34); `     &        DABS( E(ISRT(3)) ) .GT. ETOL ) THEN` (35). `        J1=ISRT(3)` (36). `        J2=ISRT(1)` (37). `        J3=ISRT(2)` (38). `      ELSE` (39). `        WRITE(ITO,'(/X,A)') 'SLAVE POINT IS CONSTRAINED.'` (40). `        CALL ERRSTP(50,ITO)` (41). `      ENDIF` (42). `C     --- IDEP,CIDEP,IDX,IRH ---` (44). `      IDEP(1)=NS` (46). `      IDEP(2)=J1` (47). |
| 49–68 | 시작 시 1–2행 MPCFACE 루틴 안. IFCQ=0이면 길이 11의 IDX 구간을 만든다(49–52). IRH 처음 두 항은 NS의 J2,J3이며 나머지 아홉 항은 면 세 절점의 세 방향이다(54–67). 원문: `      IF( IFCQ .EQ. 0 ) THEN` (49). `        IDX(1)=IS` (51). `        IDX(2)=IS+10` (52). `        IRH(1,1)=NS` (54). `        IRH(2,1)=J2` (55). `        IRH(1,2)=NS` (57). `        IRH(2,2)=J3` (58). `        IP=2` (60). `        DO 130 K1=1,3` (61). `          DO 131 K2=1,3` (62). `            IP=IP+1` (63). `            IRH(1,IP)=IELC(K1)` (64). `            IRH(2,IP)=K2` (65). `  131     CONTINUE` (66). `  130   CONTINUE` (67). |
| 69–108 | 시작 시 1–2행 MPCFACE 루틴·49행 `IF( IFCQ .EQ. 0 ) THEN`의 69행 ELSE 분기에 진입한다. 이 IF는 106행 `ENDIF`에서 닫힌다. 길이 14의 IDX 구간을 만든다(71–72). NDQ의 첫 두 절점을 IELC에서 복사하고 IELC(1)의 사각형 절점 위치로 나머지 두 절점을 결정한다(80–95). IRH 처음 두 항은 NS의 J2,J3이며 이어서 네 절점의 세 방향을 기록한다(97–104). 분기 종료와 END를 포함한다. 원문: `      ELSE` (69). `        IDX(1)=IS` (71). `        IDX(2)=IS+13` (72). `        IRH(1,1)=NS` (74). `        IRH(2,1)=J2` (75). `        IRH(1,2)=NS` (77). `        IRH(2,2)=J3` (78). `        NDQ(1)=IELC(1)` (80). `        NDQ(2)=IELC(2)` (81). `        IF( IELC(1) .EQ. IELQ(1,IFCQ) ) THEN` (83). `          NDQ(3)=IELQ(3,IFCQ)` (84). `          NDQ(4)=IELQ(4,IFCQ)` (85). `        ELSEIF( IELC(1) .EQ. IELQ(2,IFCQ) ) THEN` (86). `          NDQ(3)=IELQ(1,IFCQ)` (87). `          NDQ(4)=IELQ(4,IFCQ)` (88). `        ELSEIF( IELC(1) .EQ. IELQ(3,IFCQ) ) THEN` (89). `          NDQ(3)=IELQ(1,IFCQ)` (90). `          NDQ(4)=IELQ(2,IFCQ)` (91). `        ELSEIF( IELC(1) .EQ. IELQ(4,IFCQ) ) THEN` (92). `          NDQ(3)=IELQ(2,IFCQ)` (93). `          NDQ(4)=IELQ(3,IFCQ)` (94). `        ENDIF` (95). `        IP=2` (97). `        DO 140 K1=1,4` (98). `          DO 141 K2=1,3` (99). `            IP=IP+1` (100). `            IRH(1,IP)=NDQ(K1)` (101). `            IRH(2,IP)=K2` (102). `  141     CONTINUE` (103). `  140   CONTINUE` (104). `      ENDIF` (106). `      END` (108). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–35: 첫 J1 선택 분기에는 E 성분과 ETOL의 비교가 없으며 두 ELSEIF에는 해당 비교가 있다.
- 83–95: IELC(1)이 IELQ의 네 절점 모두와 다르면 NDQ(3:4)를 설정하는 ELSE가 없다.
