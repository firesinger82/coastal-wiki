---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcstkf.f
lines: 63
sha256: 4ecdac31133a108d355ad599731297e136721fa6e871089190c8a32bbf312786
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcstkf.f — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | MPCSTKF는 고착(stick) 상태의 면(face) 구속 주소를 구성한다. INDOF의 처음 세 방향 중 0이 아닌 값이 있으면 ERRSTP(50,ITO)를 호출한다(7–10). 선언과 빈 줄을 포함한다. 원문: `      SUBROUTINE MPCSTKF(IDEP,IDX,IRH,IS,NS,IELC,IFCQ,IELQ,INDOF,ITO)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION IDEP(2,3),IDX(2,3),IRH(2,*),IELC(3),IELQ(4,*),NDQ(4)` (4); `     &         ,INDOF(3)` (5). `      IF( INDOF(1) /= 0 .OR. INDOF(2) /= 0 .OR. INDOF(3) /= 0 ) THEN` (7). `        WRITE(ITO,'(/X,A)') 'SLAVE POINT IS CONSTRAINED.'` (8). `        CALL ERRSTP(50,ITO)` (9). `      ENDIF` (10). |
| 12–27 | 시작 시 1행 MPCSTKF 루틴 안. IFCQ=0이면 NS의 각 방향을 종속 자유도(dependent degree of freedom)로 정하고 세 면 절점의 같은 방향 세 항을 IRH에 배정한다(16–26). IDX는 각 세 항 구간의 주소이다(19–20). 원문: `      IF( IFCQ == 0 ) THEN` (12). `        IP = 0` (14). `        DO I = 1, 3` (16). `          IDEP(1,I) = NS` (17). `          IDEP(2,I) = I` (18). `          IDX(1,I) = IS + 3 * ( I - 1 )` (19). `          IDX(2,I) = IS + 3 * I - 1` (20). `          DO J = 1, 3` (21). `            IP = IP + 1` (22). `            IRH(1,IP) = IELC(J)` (23). `            IRH(2,IP) = I` (24). `          ENDDO` (25). `        ENDDO` (26). |
| 28–63 | 시작 시 1행 MPCSTKF 루틴·12행 `IF( IFCQ == 0 ) THEN`의 ELSE 분기에 진입한다. 이 IF는 61행 `ENDIF`에서 닫힌다. 첫 두 절점을 IELC에서 복사하고 IELC(1)의 사각형 위치에 따라 나머지를 채운다(30–45). NS의 세 방향마다 네 절점의 같은 방향을 IRH에 기록한다(47–59). 분기 종료와 END를 포함한다. 원문: `      ELSE` (28). `        NDQ(1) = IELC(1)` (30). `        NDQ(2) = IELC(2)` (31). `        IF( IELC(1) == IELQ(1,IFCQ) ) THEN` (33). `          NDQ(3) = IELQ(3,IFCQ)` (34). `          NDQ(4) = IELQ(4,IFCQ)` (35). `        ELSEIF( IELC(1) == IELQ(2,IFCQ) ) THEN` (36). `          NDQ(3) = IELQ(1,IFCQ)` (37). `          NDQ(4) = IELQ(4,IFCQ)` (38). `        ELSEIF( IELC(1) == IELQ(3,IFCQ) ) THEN` (39). `          NDQ(3) = IELQ(1,IFCQ)` (40). `          NDQ(4) = IELQ(2,IFCQ)` (41). `        ELSEIF( IELC(1) == IELQ(4,IFCQ) ) THEN` (42). `          NDQ(3) = IELQ(2,IFCQ)` (43). `          NDQ(4) = IELQ(3,IFCQ)` (44). `        ENDIF` (45). `        IP = 0` (47). `        DO I = 1, 3` (49). `          IDEP(1,I) = NS` (50). `          IDEP(2,I) = I` (51). `          IDX(1,I) = IS + 4 * ( I - 1 )` (52). `          IDX(2,I) = IS + 4 * I - 1` (53). `          DO J = 1, 4` (54). `            IP = IP + 1` (55). `            IRH(1,IP) = NDQ(J)` (56). `            IRH(2,IP) = I` (57). `          ENDDO` (58). `        ENDDO` (59). `      ENDIF` (61). `      END` (63). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–45: IELC(1)이 사각형 네 절점과 모두 다를 때 NDQ(3:4)를 설정하는 ELSE가 없다.
