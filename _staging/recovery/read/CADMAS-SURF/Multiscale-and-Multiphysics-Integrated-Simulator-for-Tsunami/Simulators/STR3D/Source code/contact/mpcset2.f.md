---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcset2.f
lines: 71
sha256: d13fcb631994363e1eb74c7a2dbcd5b7af162d0281b1d09b210929c659bfc28e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcset2.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | MPCSET2는 다점 구속(multipoint constraint, MPC) 주소를 자유도(degree of freedom) 배열에 반영한다. 종속 절점의 방향 INDOF를 -2로 만들고 INDMPC에 우변 시작·끝 주소를 저장한다(14–21). ICOL_R을 통해 독립 절점·방향을 찾아 MPCF에 복사한다(22–27). 인수와 배열 선언을 포함한다. 원문: 연속문(1–3): `      SUBROUTINE MPCSET2(KK,INDOF,INDMPC,MPCF,NIDEP,IDEP,INDP,IROW_R` (1); `     &                  ,ICOL_R,IELM,NM,INDC,IELC,IEDG,IELQ,IFCQ,IEDQ` (2); `     &                  ,IVRQ,ISLV,IFRIC,IDWK)` (3). `      IMPLICIT REAL*8(A-H,O-Z)` (5). 연속문(6–9): `      DIMENSION INDOF(6,*),INDMPC(2,6,*),MPCF(2,*),IDEP(2,NIDEP)` (6); `     &         ,INDP(2,*),IROW_R(NIDEP+1),ICOL_R(*),KK(*),IELM(NM,*)` (7); `     &         ,IDWK(*),INDC(*),IELC(3,*),IEDG(6,*),IELQ(4,*),IFCQ(*)` (8); `     &         ,IEDQ(*),IVRQ(*),ISLV(2,*),IFRIC(10,*),KN(5)` (9). `C     --- INDOF,INDMPC,MPCF ---` (12). `      DO 300 I=1,NIDEP` (14). `        NODE=IDEP(1,I)` (15). `        IFR =IDEP(2,I)` (16). `        INDOF(IFR,NODE)=-2` (17). `        IS=IROW_R(I)` (18). `        IE=IROW_R(I+1)-1` (19). `        INDMPC(1,IFR,NODE)=IS` (20). `        INDMPC(2,IFR,NODE)=IE` (21). `        DO 310 J=IS,IE` (22). `          IC=ICOL_R(J)` (23). `          MPCF(1,J)=INDP(1,IC)` (24). `          MPCF(2,J)=INDP(2,IC)` (25). `  310   CONTINUE` (26). `  300 CONTINUE` (27). |
| 29–50 | 시작 시 1–3행 MPCSET2 루틴 안. KK의 요소 수를 읽고 NCRMAX,NRAMAX를 0으로 초기화한다(31–36). 중간 요소 구간을 건너뛰며 ITYP=1 또는 4이면 NDF=6, 그 밖에는 3으로 설정한다(38–45). 각 요소에 NCRSET을 호출한다(46–49). 원문: `C     ----- NCRMAX, NRAMAX, NESTF -----` (29). `      NELM = KK(12)` (31). `      NELMC = KK(29)` (32). `      NELMX = KK(32)` (33). `      NCRMAX = 0` (35). `      NRAMAX = 0` (36). `      DO I = 1, NELM + NELMC + NELMX` (38). `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (39). `        ITYP = IELM(2,I)` (40). `        IF( ITYP == 1 .OR. ITYP == 4 ) THEN` (41). `          NDF = 6` (42). `        ELSE` (43). `          NDF = 3` (44). `        ENDIF` (45). `        ND = IELM(3,I)` (46). 연속문(47–48): `        CALL NCRSET(ND,NDF,IELM(8,I),INDOF,INDMPC,MPCF,IDWK,NCRMAX` (47); `     &             ,NRAMAX)` (48). `      ENDDO` (49). |
| 51–71 | 시작 시 1–3행 MPCSET2 루틴 안. IFRIC(1,I)=0인 접촉을 건너뛴다(54–55). MSTNOD로 주절점(master node)을 얻고 종속 절점을 앞에 추가하여 NCRSET을 호출한다(56–63). NESTF를 `( NCRMAX + 1 ) * NCRMAX / 2`로 구한다(65). KK(33:35)에 NESTF,NCRMAX,NRAMAX를 저장한다(67–69). 해석: NESTF 식은 삼각형 저장 항 수를 나타내는 식이다. 원문: `      NINDC = KK(95)` (51). `      NINDCX = KK(103)` (52). `      DO I = 1, NINDC + NINDCX` (54). `        IF( IFRIC(1,I) == 0 ) CYCLE` (55). `        NS = INDC(I)` (56). `        IST = ISLV(1,I)` (57). `        MA  = ISLV(2,I)` (58). `        CALL MSTNOD(ND,KN(2),IST,MA,IELC,IEDG,IELQ,IFCQ,IEDQ,IVRQ)` (59). `        ND = ND + 1` (60). `        KN(1) = NS` (61). `        CALL NCRSET(ND,3,KN,INDOF,INDMPC,MPCF,IDWK,NCRMAX,NRAMAX)` (62). `      ENDDO` (63). `      NESTF = ( NCRMAX + 1 ) * NCRMAX / 2` (65). `      KK(33) = NESTF` (67). `      KK(34) = NCRMAX` (68). `      KK(35) = NRAMAX` (69). `      END` (71). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39: NELM보다 크고 NELM+NELMC 이하인 요소는 NCRSET 호출에서 제외된다.
