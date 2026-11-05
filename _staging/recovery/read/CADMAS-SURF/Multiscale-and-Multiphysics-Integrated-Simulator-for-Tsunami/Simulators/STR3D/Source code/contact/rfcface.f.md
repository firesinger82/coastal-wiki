---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rfcface.f
lines: 49
sha256: c896aa7f3cd542f03a2396c7f1d68499ff99de95f659179bab7135ba2294c159
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rfcface.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RFCFACE는 면(face) 세 절점과 종속 절점(slave node) 좌표를 모아 AREACD로 RL,E,H를 구한다(7–10). F의 E 방향 투영(projection)으로 RF를 계산한다(12). 인수·배열 선언과 주석을 포함한다. 원문: `      SUBROUTINE RFCFACE(RFCI,NS,IELC,IFCQ,IELQ,POS,F)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). 연속문(4–5): `      DIMENSION X(3,4),POS(3,*),IELC(3),RL(3),E(3),RF(3),F(3),KN(4)` (4); `     &         ,RFCI(3,*),IELQ(4,*)` (5). `      X(:,1:3) = POS(:,IELC(:))` (7). `      X(:,4)   = POS(:,NS)` (8). `      CALL AREACD(RL,E,H,X)` (10). `      RF(:) = DOT_PRODUCT(F,E) * E(:)` (12). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `contact/areacd.f:9–11,46`(E에 대응하는 RN 반환), `util/cross2.f:9–16`(정규화된 외적). [11-04 전수 검증 보완] |
| 14–21 | 시작 시 1행 RFCFACE 루틴 안. IFCQ=0이면 삼각형 세 절점의 RFCI에서 RL 가중 RF를 뺀다(14–20). 원문: `      IF( IFCQ == 0 ) THEN` (14). `        KN(1:3) = IELC(:)` (16). `        DO I = 1, 3` (18). `          RFCI(:,KN(I)) = RFCI(:,KN(I)) - RL(I) * RF(:)` (19). `        ENDDO` (20). |
| 22–49 | 시작 시 1행 RFCFACE 루틴·14행 `IF( IFCQ == 0 ) THEN`의 ELSE 분기에 진입한다. 이 IF는 47행 `ENDIF`에서 닫힌다. 첫 두 IELC 절점과 사각형 위치에 따른 나머지 절점으로 KN을 만든다(24–38). RL(3) 항을 .25D0씩 네 절점에 배분하고 처음 두 절점에는 RL(1),RL(2) 항도 뺀다(40–45). 분기 종료와 END를 포함한다. 원문: `      ELSE` (22). `        KN(1:2) = IELC(1:2)` (24). `        IF( IELC(1) == IELQ(1,IFCQ) ) THEN` (26). `          KN(3)=IELQ(3,IFCQ)` (27). `          KN(4)=IELQ(4,IFCQ)` (28). `        ELSEIF( IELC(1) == IELQ(2,IFCQ) ) THEN` (29). `          KN(3)=IELQ(1,IFCQ)` (30). `          KN(4)=IELQ(4,IFCQ)` (31). `        ELSEIF( IELC(1) == IELQ(3,IFCQ) ) THEN` (32). `          KN(3)=IELQ(1,IFCQ)` (33). `          KN(4)=IELQ(2,IFCQ)` (34). `        ELSEIF( IELC(1) == IELQ(4,IFCQ) ) THEN` (35). `          KN(3)=IELQ(2,IFCQ)` (36). `          KN(4)=IELQ(3,IFCQ)` (37). `        ENDIF` (38). 연속문(40–41): `        RFCI(:,KN(1)) = RFCI(:,KN(1)) - RL(1) * RF(:)` (40); `     &                    - .25D0*RL(3)*RF(:)` (41). 연속문(42–43): `        RFCI(:,KN(2)) = RFCI(:,KN(2)) - RL(2) * RF(:)` (42); `     &                    - .25D0*RL(3)*RF(:)` (43). `        RFCI(:,KN(3)) = RFCI(:,KN(3)) - .25D0*RL(3)*RF(:)` (44). `        RFCI(:,KN(4)) = RFCI(:,KN(4)) - .25D0*RL(3)*RF(:)` (45). `      ENDIF` (47). `      END` (49). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10: AREACD에서 얻는 H는 후속 실행문에 사용되지 않는다.
- 26–38: IELC(1)이 사각형 네 절점과 모두 다를 때 KN(3:4)를 설정하는 ELSE가 없다.
