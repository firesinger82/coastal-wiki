---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcrank.f
lines: 81
sha256: 1ad6ef689795c9ba878e5814cefd76c3a095071b68aaa0ef7d894d80c1d5527b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcrank.f — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | MPCRANK는 순위(rank) IRANK를 0으로 초기화한다(8). ICORR를 1로 채우고 ISLV(1,I)>0인 접촉 절점은 0으로 바꾼다(10–14). NRANK는 0에서 시작한다(16). 원문: 연속문(1–2): `      SUBROUTINE MPCRANK(NRANK,IRANK,ICORR,NNOD,NINDC,INDC,IEDG,IELC` (1); `     &                  ,IELQ,IFCQ,IEDQ,IVRQ,ISLV)` (2). 연속문(4–6): `      DIMENSION IRANK(NINDC),ICORR(NNOD),ISLV(2,NINDC),INDC(NINDC)` (4); `     &         ,IVRQ(*),IEDQ(*),IFCQ(*),IELQ(4,*),IELC(3,*),IEDG(6,*)` (5); `     &         ,IG(4)` (6). `      IRANK(:) = 0` (8). `      ICORR(:) = 1` (10). `      DO I = 1, NINDC` (12). `        IF( ISLV(1,I) > 0 ) ICORR( INDC(I) ) = 0` (13). `      ENDDO` (14). `      NRANK = 0` (16). |
| 18–55 | 시작 시 1–2행 MPCRANK 루틴 안. 종료 조건 없는 DO에서 NRANK를 증가시킨다(18–20). 아직 순위가 없는 활성 접촉의 IST를 SELECT CASE로 분류한다(22–29). 1/11은 한 절점 또는 사각형 네 절점, 2/12/14는 변 두 절점 또는 사각형, 3/13/15는 면 세 절점 또는 사각형을 IG에 넣는다(30–54). 원문: `      DO` (18). `        NRANK = NRANK + 1` (20). `        DO I = 1, NINDC` (22). `          IST = ISLV(1,I)` (24). `          MA = ISLV(2,I)` (25). `          IF( IST > 0 .AND. IRANK(I) == 0 ) THEN` (27). `            SELECT CASE( IST )` (29). `            CASE( 1, 11 )` (30). `              IF( IVRQ(MA) > 0 ) THEN` (31). `                N = 4` (32). `                IG(:) = IELQ(:,IVRQ(MA))` (33). `              ELSE` (34). `                N = 1` (35). `                IG(1) = MA` (36). `              ENDIF` (37). `            CASE( 2, 12, 14 )` (38). `              IF( IEDQ(MA) > 0 ) THEN` (39). `                N = 4` (40). `                IG(:) = IELQ(:,IEDQ(MA))` (41). `              ELSE` (42). `                N = 2` (43). `                IG(1:2) = IEDG(1:2,MA)` (44). `              ENDIF` (45). `            CASE( 3, 13, 15 )` (46). `              IF( IFCQ(MA) > 0 ) THEN` (47). `                N = 4` (48). `                IG(:) = IELQ(:,IFCQ(MA))` (49). `              ELSE` (50). `                N = 3` (51). `                IG(1:3) = IELC(:,MA)` (52). `              ENDIF` (53). `            END SELECT` (54). |
| 56–81 | 시작 시 1–2행 MPCRANK 루틴·18행 `DO`·22행 `DO I = 1, NINDC`·27행 `IF( IST > 0 .AND. IRANK(I) == 0 ) THEN` 안이며 SELECT CASE 밖. 이 IF는 62행에서 닫힌다. 22행 루프는 GOTO 10의 목적지인 64행 `10 ENDDO`에서 닫힌다. 18행 DO는 79행에서 닫힌다. 참조 절점 중 ICORR=0이 있으면 현재 항을 건너뛰며, 없으면 현재 NRANK를 부여한다(56–64). 현재 순위의 절점을 ICORR=1로 바꾸고 미지정 접촉 수 NCORR를 센다(66–75). NCORR=0에서 바깥 DO를 끝낸다(77–79). 원문: `            DO J = 1, N` (56). `              IF( ICORR( IG(J) ) == 0 ) GOTO 10` (57). `            ENDDO` (58). `            IRANK(I) = NRANK` (60). `          ENDIF` (62). `   10   ENDDO` (64). `        NCORR = 0` (66). `        DO I = 1, NINDC` (68). `          IF( ISLV(1,I) == 0 ) CYCLE` (69). `          IF( IRANK(I) == NRANK ) THEN` (70). `            ICORR( INDC(I) ) = 1` (71). `          ELSEIF( IRANK(I) == 0 ) THEN` (72). `            NCORR = NCORR + 1` (73). `          ENDIF` (74). `        ENDDO` (75). `        IF( NCORR == 0 ) EXIT` (77). `      ENDDO` (79). `      END` (81). 70–74행 분기 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–54: SELECT CASE에는 IST=4,5와 CASE DEFAULT가 없다.
- 18–79: 반복 상한이나 NCORR가 줄지 않을 때의 별도 탈출 조건은 없으며 EXIT 조건은 NCORR=0이다.
