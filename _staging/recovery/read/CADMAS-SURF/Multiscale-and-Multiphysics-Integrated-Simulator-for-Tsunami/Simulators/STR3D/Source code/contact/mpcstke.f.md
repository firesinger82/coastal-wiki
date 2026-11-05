---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcstke.f
lines: 66
sha256: c02b4cbf97350abac2a1e8f2f45af8fe6811a8ee9a31696e005ac971febc095c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcstke.f — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | MPCSTKE는 고착(stick) 상태의 변(edge) 구속 주소를 구성한다. INDOF의 처음 세 방향 중 0이 아닌 값이 있으면 오류를 출력하고 ERRSTP(50,ITO)를 호출한다(7–10). 암시적 형 및 배열 선언을 포함한다. 원문: `      SUBROUTINE MPCSTKE(IDEP,IDX,IRH,IS,NS,IG,IEDQ,IELQ,INDOF,ITO)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION IDEP(2,3),IDX(2,3),IRH(2,*),IG(2),IELQ(4,*),NDQ(4)` (4); `     &         ,INDOF(3)` (5). `      IF( INDOF(1) /= 0 .OR. INDOF(2) /= 0 .OR. INDOF(3) /= 0 ) THEN` (7). `        WRITE(ITO,'(/X,A)') 'SLAVE POINT IS CONSTRAINED.'` (8). `        CALL ERRSTP(50,ITO)` (9). `      ENDIF` (10). |
| 12–27 | 시작 시 1행 MPCSTKE 루틴 안. IEDQ=0이면 NS의 세 방향을 종속 자유도(dependent degree of freedom)로 기록한다(16–18). 각 방향에 변 두 절점의 같은 방향 두 항을 배정하고 IDX의 시작·끝 주소를 정한다(19–26). 원문: `      IF( IEDQ == 0 ) THEN` (12). `        IP = 0` (14). `        DO I = 1, 3` (16). `          IDEP(1,I) = NS` (17). `          IDEP(2,I) = I` (18). `          IDX(1,I) = IS + 2 * ( I - 1 )` (19). `          IDX(2,I) = IS + 2 * I - 1` (20). `          DO J = 1, 2` (21). `            IP = IP + 1` (22). `            IRH(1,IP) = IG(J)` (23). `            IRH(2,IP) = I` (24). `          ENDDO` (25). `        ENDDO` (26). |
| 28–66 | 시작 시 1행 MPCSTKE 루틴·12행 `IF( IEDQ == 0 ) THEN`의 ELSE 분기에 진입한다. 이 IF는 64행 `ENDIF`에서 닫힌다. IG(1)의 사각형 위치에 따라 네 절점을 NDQ에 구성한다(30–48). NS의 세 방향마다 네 절점의 같은 방향 네 항을 IRH에 기록한다(50–62). 분기 종료와 END를 포함한다. 원문: `      ELSE` (28). `        NDQ(1)=IG(1)` (30). `        IF( IG(1) .EQ. IELQ(1,IEDQ) ) THEN` (32). `          NDQ(2)=IELQ(2,IEDQ)` (33). `          NDQ(3)=IELQ(3,IEDQ)` (34). `          NDQ(4)=IELQ(4,IEDQ)` (35). `        ELSEIF( IG(1) .EQ. IELQ(2,IEDQ) ) THEN` (36). `          NDQ(2)=IELQ(1,IEDQ)` (37). `          NDQ(3)=IELQ(3,IEDQ)` (38). `          NDQ(4)=IELQ(4,IEDQ)` (39). `        ELSEIF( IG(1) .EQ. IELQ(3,IEDQ) ) THEN` (40). `          NDQ(2)=IELQ(1,IEDQ)` (41). `          NDQ(3)=IELQ(2,IEDQ)` (42). `          NDQ(4)=IELQ(4,IEDQ)` (43). `        ELSEIF( IG(1) .EQ. IELQ(4,IEDQ) ) THEN` (44). `          NDQ(2)=IELQ(1,IEDQ)` (45). `          NDQ(3)=IELQ(2,IEDQ)` (46). `          NDQ(4)=IELQ(3,IEDQ)` (47). `        ENDIF` (48). `        IP = 0` (50). `        DO I = 1, 3` (52). `          IDEP(1,I) = NS` (53). `          IDEP(2,I) = I` (54). `          IDX(1,I) = IS + 4 * ( I - 1 )` (55). `          IDX(2,I) = IS + 4 * I - 1` (56). `          DO J = 1, 4` (57). `            IP = IP + 1` (58). `            IRH(1,IP) = NDQ(J)` (59). `            IRH(2,IP) = I` (60). `          ENDDO` (61). `        ENDDO` (62). `      ENDIF` (64). `      END` (66). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–48: IG(1)이 사각형 네 절점과 모두 다를 때 NDQ(2:4)를 설정하는 ELSE가 없다.
