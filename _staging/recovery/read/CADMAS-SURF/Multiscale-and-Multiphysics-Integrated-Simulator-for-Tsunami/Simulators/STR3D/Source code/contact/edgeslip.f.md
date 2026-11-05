---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/edgeslip.f
lines: 101
sha256: e314564722923d600c2db6b8952de13bdf65bdf22a55a85597c5c2b791d072a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# edgeslip.f — 판독 구간 기록

구간은 1행부터 101행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 루틴·암시적 자료형·배열과 TOL=75.D0을 DATA로 선언한다(1–6). 끝점과 오른쪽·왼쪽 면 번호를 가져온다(8–11). 오른쪽 면이 0이면 메시지 출력 후 ERRSTP를 호출한다(13–16). SUBVEC·DIRCOS로 모서리 방향 E1을 만든다(18–19). 원문: `      SUBROUTINE EDGESLIP(ISLV,F,EN,IEDGE,IEDG,IELC,POS,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IEDG(6),POS(3,*),V12(3),V13(3),E1(3),E2L(3),E2R(3)` `     &         ,E3L(3),E3R(3),E(3),IELC(3,*),F(3),ISLV(2),EN(3)` (4–5, 하나의 고정형식 연속문); `      DATA TOL /75.D0/` (6); `      IG1=IEDG(1)` (8); `      IG2=IEDG(2)` (9); `      IER=IEDG(3)` (10); `      IEL=IEDG(5)` (11); `      IF(IER .EQ. 0) THEN` (13); `        WRITE(ITO,'(/X,A)') 'STOP IN SUB. EDGESLIP.'` (14); `        CALL ERRSTP(90,ITO)` (15); `      CALL SUBVEC(V12,POS(1,IG2),POS(1,IG1),3)` (18); `      CALL DIRCOS(E1,V12,3)` (19). 모서리 방향 계산의 근거는 같은 STR3D 원문 트리의 `util/subvec.f:9–11`과 `util/dircos.f:8–15`이다. [11-04 전수 검증 보완] |
| 21–55 | 시작 시 1행 EDGESLIP 루틴 안이다. 왼쪽 면이 있으면 SUBVEC·CROSS2로 기저를 만들고 VECML1로 F와 각 기저의 내적 FYL·FZL을 구한다(23–34). 오른쪽 면은 같은 종류의 호출로 기저와 F의 내적 FYR·FZR을 구한다(38–45). 왼쪽 면이 있을 때 CROSS·VECML1로 SIN을 구한다(49–52). LEFT FACE·RIGHT FACE·ANGLE·CHECK 주석은 각각 왼쪽 면·오른쪽 면·각도·검사를 뜻한다(21·36·47·54). 원문: 주석 원문: `C     --- LEFT FACE ---` (21); `      IF( IEL .GT. 0 ) THEN` (23); `        IG3=IELC(IEDG(6),IEL)` (25); `        CALL SUBVEC(V13,POS(1,IG3),POS(1,IG1),3)` (27); `        CALL CROSS2(V13,E1,E2L)` (28); `        CALL CROSS2(E1,E2L,E3L)` (29); `        CALL VECML1(FYL,F,E2L,3)` (31); `        CALL VECML1(FZL,F,E3L,3)` (32); 주석 원문: `C     --- RIGHT FACE ---` (36); `      IG3=IELC(IEDG(4),IER)` (38); `      CALL SUBVEC(V13,POS(1,IG3),POS(1,IG1),3)` (40); `      CALL CROSS2(E1,V13,E3R)` (41); `      CALL CROSS2(E3R,E1,E2R)` (42); `      CALL VECML1(FYR,F,E2R,3)` (44); `      CALL VECML1(FZR,F,E3R,3)` (45); 주석 원문: `C     --- ANGLE ---` (47); `      IF( IEL .GT. 0 ) THEN` (49); `        CALL CROSS(E3R,E2L,E)` (50); `        CALL VECML1(SIN,E,E1,3)` (51); 주석 원문: `C     --- CHECK ---` (54). 내적 계산의 근거는 같은 STR3D 원문 트리의 `util/vecml1.f:19–22`이다. 해석: F를 힘으로 보면 FYL·FZL·FYR·FZR은 각 기저 방향의 힘 성분이다. [11-04 전수 검증 정정] [11-04 전수 검증 보완] |
| 56–101 | 시작 시 1행 EDGESLIP 루틴 안이다. 왼쪽 면이 없으면 FZR·FYR 조건으로 면 상태 3을 설정한다(56–60). 앞 분기가 거짓이고 SIN>0이면 FYL·FZL·FYR 조건으로 모서리 상태 2 또는 왼쪽·오른쪽 면 상태 3을 설정한다(61–71). 그 다음 분기는 FYL·FZR 조건에서 COST와 두 내적을 계산하고 임계값 및 부호 있는 FZL·FYR 값 또는 COSL·COSR 값의 대소로 면을 선택한다(72–98). 분기·루틴을 닫는다(99–101). 원문: `      IF( IEL .EQ. 0 ) THEN` (56); `        IF( FZR .GE. 0. .AND. FYR .GE. 0. ) THEN` (57); `          ISLV(1)=3` (58); `          ISLV(2)=IER` (59); `      ELSEIF( SIN .GT. 0. ) THEN` (61); `        IF( FZL .LE. 0. .AND. FYR .LE. 0. ) THEN` (62); `          ISLV(1)=2` (63); `          ISLV(2)=IEDGE` (64); `        ELSEIF( FYL .GE. 0. .AND. FZL .GT. 0. ) THEN` (65); `          ISLV(1)=3` (66); `          ISLV(2)=IEL` (67); `        ELSEIF( FZR .GE. 0. .AND. FYR .GT. 0. ) THEN` (68); `          ISLV(1)=3` (69); `          ISLV(2)=IER` (70); `      ELSEIF( FYL .GE. 0. .AND. FZR .GE. 0. ) THEN` (72); `        COST=DCOS(TOL/90.D0*DASIN(1.D0))` (73); `        CALL VECML1(COSL,EN,E2L,3)` (74); `        CALL VECML1(COSR,EN,E3R,3)` (75); `        IF( COSL .GT. COST .AND. COSR .GT. COST ) THEN` (76); `          IF( FZL .GE. FYR ) THEN` (77); `            ISLV(1)=3` (78); `            ISLV(2)=IEL` (79); `          ELSE` (80); `            ISLV(1)=3` (81); `            ISLV(2)=IER` (82); `        ELSEIF( COSL .GT. COST ) THEN` (84); `          ISLV(1)=3` (85); `          ISLV(2)=IEL` (86); `        ELSEIF( COSR .GT. COST ) THEN` (87); `          ISLV(1)=3` (88); `          ISLV(2)=IER` (89); `        ELSE` (90); `          IF( COSL .GE. COSR ) THEN` (91); `            ISLV(1)=3` (92); `            ISLV(2)=IEL` (93); `          ELSE` (94); `            ISLV(1)=3` (95); `            ISLV(2)=IER` (96). 56·61·72행 분기 사슬에는 ELSE가 없으며 99행 ENDIF로 닫힌다. 62·65·68행 분기 사슬에도 ELSE가 없으며 71행 ENDIF로 닫힌다. [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·73: 각도 임계값 TOL은 75.D0으로 고정되며 COST 계산에 사용한다.
- 56–99: 일부 조건 조합에서는 ISLV에 대입하는 실행문이 없다.
