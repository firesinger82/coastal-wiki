---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/bdyfc.f
lines: 66
sha256: 64abea80221d1b786eb539b117cf9db1c2b17935d3fdf1fe7d5ea93afc0b0309
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bdyfc.f — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | BDYFC의 연속 인수·암시적 형·배열 선언과 DATA PI=3.141592654D0. IGR=0이면 RFRC에 2.*PI를 곱해 OMEGA를 만든다. IR0=0이면 원점을 사용하고 그 밖에는 지정 절점 좌표를 R0로 사용한다. 원문: 연속문(1–2): `      SUBROUTINE BDYFC(FT,SI,IGR,GRAV,IR0,RFRC,GRID,NELM,NM,IELM,AMAT` <br> `     &                ,RODA,BARD,ITO)`; `      IMPLICIT REAL*8(A-H,O-Z)` (4); 연속문(5–7): `      DIMENSION R0(3),GRID(3,*),IELM(NM,*),KN(20),AMAT(33,*),XYZ(3,20)` <br> `     &         ,FC(3,20),GRAV(3),FT(6,*),OMEGA(3),WK(3),RFRC(3),RODA(*)` <br> `     &         ,BARD(6,*)`; `      DATA PI /3.141592654D0/` (8); `C----&------------------------------------------------------------------` (9); `      IF(IGR .EQ. 0) THEN` (10); `        CALL RMULT1(OMEGA,RFRC,2.*PI,3)` (11); `        IF(IR0 .EQ. 0) THEN` (12); `          CALL CLEAR1(R0,3)` (13); `        ELSE` (14); `          CALL SHIFT1(R0,GRID(1,IR0),3)` (15); `        ENDIF` (16); `      ENDIF` (17). |
| 19–51 | BDYFC 루틴 안. 요소별 유형·절점·재료·연결·밀도를 취하고 좌표를 모은다. FC를 0으로 초기화한다. 유형 2·6의 절점 수 4·10·6·15에 대해 BDFTE1·BDFTE2·BDFPN1·BDFPN2를 호출하고 그 밖에는 BDFHX2를 호출한다. 유형 3은 BDFTRS, 유형 4는 BDFBM을 호출한다. 원문: `      DO 100 IENO=1,NELM` (19); `        ITYP=IELM(2,IENO)` (21); `        ND=IELM(3,IENO)` (22); `        IMAT=IELM(4,IENO)` (23); `        I5=IELM(5,IENO)` (24); `        CALL SHIFT0(KN,IELM(8,IENO),ND)` (25); `        RHO=AMAT(3,IMAT)` (26); `        DO 110 I=1,ND` (28); `          CALL SHIFT1(XYZ(1,I),GRID(1,KN(I)),3)` (29); `  110   CONTINUE` (30); `        CALL CLEAR1(FC,3*ND)` (32); `        IF(ITYP .EQ. 2 .OR. ITYP .EQ. 6) THEN` (34); `          IF(ND .EQ. 4) THEN` (35); `            CALL BDFTE1(FC,XYZ,GRAV,R0,IGR,ITO)` (36); `          ELSEIF(ND .EQ. 10) THEN` (37); `            CALL BDFTE2(FC,XYZ,GRAV,R0,IGR,ITO)` (38); `          ELSEIF(ND .EQ. 6) THEN` (39); `            CALL BDFPN1(FC,XYZ,GRAV,R0,IGR,ITO)` (40); `          ELSEIF(ND .EQ. 15) THEN` (41); `            CALL BDFPN2(FC,XYZ,GRAV,R0,IGR,ITO)` (42); `          ELSE` (43); `            CALL BDFHX2(FC,XYZ,ND,GRAV,R0,IGR,ITO)` (44); `          ENDIF` (45); `        ELSEIF(ITYP .EQ. 3) THEN` (46); `          CALL BDFTRS(FC,XYZ,RODA(I5),GRAV,R0,IGR,ITO)` (47); `        ELSEIF(ITYP .EQ. 4) THEN` (48); `          CALL BDFBM(FC,XYZ,BARD(2,I5),BARD(1,I5),GRAV,R0,IGR,ITO)` (49); `        ENDIF` (50). 34·46·48행의 ITYP IF/ELSEIF 사슬에는 ELSE가 없다. 내부 ND 분기에는 43행 ELSE가 있다. [11-04 전수 검증 보완] |
| 52–66 | 시작 시 `DO 100 IENO=1,NELM` (19, 종료 레이블 `100 CONTINUE`는 64행) 안. IGR=1이면 FC에 RHO를 곱한다. 그 밖에는 두 CROSS 호출로 OMEGA의 이중 벡터곱을 계산하고 -RHO를 곱한다. FRCADD에 SI를 전달해 전체 힘 FT에 합친다. 원문: `        IF(IGR .EQ. 1) THEN` (52); `          CALL RMULT1(FC,FC,RHO,3*ND)` (53); `        ELSE` (54); `          DO 120 I=1,ND` (55); `            CALL CROSS(OMEGA,FC(1,I),WK)` (56); `            CALL CROSS(OMEGA,WK,FC(1,I))` (57); `  120     CONTINUE` (58); `          CALL RMULT1(FC,FC,-RHO,3*ND)` (59); `        ENDIF` (60); `        CALL FRCADD(ND,FC,KN,SI,FT)` (62); `  100 CONTINUE` (64); `      END` (66). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–17·52–60: OMEGA·R0의 초기 설정은 IGR=0 분기 안에 있다. 후반의 회전력 분기는 IGR=1이 아닌 모든 값에서 실행된다.
- 34–50: 유형 2·6의 절점 수가 4·10·6·15 이외이면 BDFHX2를 호출한다. 이 분기 안에는 절점 수 8·20만 허용하는 별도 검사가 없다.
