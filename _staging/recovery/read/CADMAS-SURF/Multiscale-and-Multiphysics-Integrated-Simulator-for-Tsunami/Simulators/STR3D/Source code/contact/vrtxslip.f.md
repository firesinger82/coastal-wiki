---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/vrtxslip.f
lines: 105
sha256: 6049d7fcbaac9a99d42096efa8f2e343792f8a86bce9dae369b8fd859b992600
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vrtxslip.f — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | VRTXSLIP는 정점(vertex)에서 면(face) 또는 변(edge)으로의 미끄럼(slip) 후보를 추가한다. 변 끝점과 양쪽 면 주소를 읽는다(9–12). IE2=0일 때 오류를 내는 14–17행은 주석 처리된 코드이며 실행되지 않는다. 인수·선언과 주석을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE VRTXSLIP(NSLIP,ISLIP,FSLIP,CSLIP,INCOMP,IP1,F,EN,IEDGE` (1); `     &                   ,IEDG,IELC,POS,ITO)` (2). `      IMPLICIT REAL*8(A-H,O-Z)` (4). 연속문(5–7): `      DIMENSION IEDG(6),POS(3,*),V12(3),V13(3),E1(3),E2R(3),E2L(3)` (5); `     &         ,E3R(3),E3L(3),E(3),IELC(3,*),F(3),ISLIP(2,*),FSLIP(*)` (6); `     &         ,CSLIP(*),EN(3),EA(3)` (7). `      IG1=IEDG(1)` (9). `      IG2=IEDG(2)` (10). `      IE1=IEDG(3)` (11). `      IE2=IEDG(5)` (12). `C     IF(IE2 .EQ. 0) THEN` (14) [주석 처리된 코드/선언]. `C       WRITE(ITO,'(/X,A)') 'CONTACT SURFACE IS SMALL.'` (15) [주석 처리된 코드/선언]. `C       CALL ERRSTP(51,ITO)` (16) [주석 처리된 코드/선언]. `C     ENDIF` (17). |
| 19–43 | 시작 시 1–2행 VRTXSLIP 루틴 안. IP1이 IG1 또는 IG2인지에 따라 반대 끝점과 좌·우 면을 정한다(19–34). IG1 분기에서 IEL=0이면 INCOMP=1로 설정하고 반환한다(23–26). 어느 끝점도 아니면 ERRSTP(90,ITO)를 호출한다(35–38). SUBVEC,DIRCOS,VECML1로 변 방향 E1과 힘 성분 FX를 구한다(40–42). 원문: `      IF(IP1 .EQ. IG1) THEN` (19). `        IP2=IG2` (20). `        IEL=IE2` (21). `        IER=IE1` (22). `        IF(IEL .EQ. 0) THEN` (23). `          INCOMP=1` (24). `          RETURN` (25). `        ENDIF` (26). `        IP3L=IELC(IEDG(6),IEL)` (27). `        IP3R=IELC(IEDG(4),IER)` (28). `      ELSEIF(IP1 .EQ. IG2) THEN` (29). `        IP2=IG1` (30). `        IEL=IE1` (31). `        IER=IE2` (32). `        IP3L=IELC(IEDG(4),IEL)` (33). `        IP3R=IELC(IEDG(6),IER)` (34). `      ELSE` (35). `        WRITE(ITO,'(/X,A)') 'STOP IN SUB. VRTXSLIP!'` (36). `        CALL ERRSTP(90,ITO)` (37). `      ENDIF` (38). `      CALL SUBVEC(V12,POS(1,IP2),POS(1,IP1),3)` (40). `      CALL DIRCOS(E1,V12,3)` (41). `      CALL VECML1(FX,F,E1,3)` (42). |
| 44–62 | 시작 시 1–2행 VRTXSLIP 루틴 안. 왼쪽 면의 V13,E2L,E3L 및 FYL,FZL을 구한다(46–51). X3,RL13으로 COS0를 구하고 FX,FZL로 FXZL을 계산한다(53–56). FXZL>1.D-10이면 COS를 계산하고 그 밖에는 반환한다(57–61). 원문: `C     --- LEFT FACE ---` (44). `      CALL SUBVEC(V13,POS(1,IP3L),POS(1,IP1),3)` (46). `      CALL CROSS2(V13,E1,E2L)` (47). `      CALL CROSS2(E1,E2L,E3L)` (48). `      CALL VECML1(FYL,F,E2L,3)` (50). `      CALL VECML1(FZL,F,E3L,3)` (51). `      CALL VECML1(X3,V13,E1,3)` (53). `      CALL VECML2(RL13,V13,3)` (54). `      COS0=X3/RL13` (55). `      FXZL=DSQRT(FX*FX+FZL*FZL)` (56). `      IF(FXZL .GT. 1.D-10) THEN` (57). `        COS=FX/FXZL` (58). `      ELSE` (59). `        RETURN` (60). `      ENDIF` (61). |
| 63–82 | 시작 시 1–2행 VRTXSLIP 루틴 안. IER>0이면 오른쪽 면 V13,E3R,E2R 및 FYR,FZR을 구한다(63–72). CROSS와 VECML1으로 SIN을 얻는다(76–77). 조건 종료와 CHECK 주석을 포함한다. 원문: `      IF(IER .GT. 0) THEN` (63). `C       --- RIGHT FACE ---` (65). `        CALL SUBVEC(V13,POS(1,IP3R),POS(1,IP1),3)` (67). `        CALL CROSS2(E1,V13,E3R)` (68). `        CALL CROSS2(E3R,E1,E2R)` (69). `        CALL VECML1(FYR,F,E2R,3)` (71). `        CALL VECML1(FZR,F,E3R,3)` (72). `C       --- ANGLE ---` (74). `        CALL CROSS(E3R,E2L,E)` (76). `        CALL VECML1(SIN,E,E1,3)` (77). `      ENDIF` (79). `C     --- CHECK ---` (81). |
| 83–105 | 시작 시 1–2행 VRTXSLIP 루틴 안. FYL>=0,FZL>0,COS>COS0이면 면 후보를 추가하고 FSLIP,CSLIP를 설정한 뒤 반환한다(83–90). IER=0이면 반환한다(92). SIN>0,FZL<=0,FYR<=0,FX>0이면 변 후보를 추가하고 합 방향 EA를 DIRCOS로 처리해 CSLIP를 구한다(94–103). END를 포함한다. 원문: `      IF(FYL .GE. 0. .AND. FZL .GT. 0. .AND. COS .GT. COS0) THEN` (83). `        NSLIP=NSLIP+1` (84). `        ISLIP(1,NSLIP)=3` (85). `        ISLIP(2,NSLIP)=IEL` (86). `        FSLIP(NSLIP)=FXZL` (87). `        CALL VECML1(CSLIP(NSLIP),EN,E2L,3)` (88). `        RETURN` (89). `      ENDIF` (90). `      IF(IER .EQ. 0) RETURN` (92). 연속문(94–95): `      IF(SIN .GT. 0. .AND. FZL .LE. 0. .AND. FYR .LE. 0. .AND.` (94); `     &   FX .GT. 0.) THEN` (95). `        NSLIP=NSLIP+1` (96). `        ISLIP(1,NSLIP)=2` (97). `        ISLIP(2,NSLIP)=IEDGE` (98). `        FSLIP(NSLIP)=FX` (99). `        EA(:) = E2L(:) + E3R(:)` (100). `        CALL DIRCOS(EA,EA,3)` (101). `        CALL VECML1(CSLIP(NSLIP),EN,EA,3)` (102). `      ENDIF` (103). `      END` (105). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–17: IE2=0 오류 처리 전체가 주석이다.
- 23–34: IP1=IG1 분기는 IEL=0을 검사하지만 IP1=IG2 분기는 IER=0이어도 IP3R=IELC(IEDG(6),IER)를 먼저 읽는다.
- 55: COS0 계산 앞에 RL13=0 검사가 없다.
- 71–72: FYR,FZR을 계산하지만 이후 조건에는 FYR만 사용한다.
