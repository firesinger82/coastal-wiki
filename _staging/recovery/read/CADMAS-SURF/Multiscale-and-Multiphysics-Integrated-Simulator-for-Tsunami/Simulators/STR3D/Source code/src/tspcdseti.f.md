---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/tspcdseti.f
lines: 64
sha256: a5c38266b01fa0cb456c269293ad247da55c216ec247872a90303369f657cbbb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tspcdseti.f — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | TSPCDSETI 입구와 배열 선언이다(1–6). IDLOAD에 일치하는 IDLD 집합을 찾아 ADDSET으로 펼친다(8–19). 원문: `      SUBROUTINE TSPCDSETI(INDOF,IDLOAD,KK,IDLD,LIDL,ITL1,ISPD,NSPD`<br>`     &                    ,IDYN)` (1–2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION KK(*),INDOF(6,*),IDLD(2,*),LIDL(*),ITL1(4,*),ISPD(2,*)`<br>`     &         ,NSPD(7,*)` (5–6); `      NDLD  = KK(66)` (8); `      NTLD1 = KK(77)` (9); `      IDLFLG=0` (11); `      DO 100 I=1,NDLD` (13); `        IF( IDLD(1,I) .EQ. IDLOAD ) THEN` (14); `          CALL ADDSET(I,IDLD,IS,NN)` (15); `          IDLFLG=1` (16); `          GOTO 200` (17); `        ENDIF` (18); `  100 CONTINUE` (19) `GOTO 200`(17)의 대상은 21행이다. [11-04 전수 검증 보완] |
| 21–43 | 시작 시 TSPCDSETI 루틴(1) 안이다. IDLFLG==1이면 하위 LI별로 시간 하중을 찾는다(21–30). IDYN==0이고 ITYPE>=2이면 현재 J 반복을 건너뛰고, 일치하는 ITYPE>0의 IEX를 SPCDSETI로 처리한다(32–42). 원문: `  200 IF(IDLFLG .EQ. 1) THEN` (21); `        DO 300 I=1,NN` (23); `          LI=LIDL(IS-1+I)` (25); `          DO 310 J=1,NTLD1` (27); `            ID=ITL1(1,J)` (29); `            ITYPE=ITL1(3,J)` (30); `            IF( IDYN == 0 .AND. ITYPE >= 2 ) CYCLE` (32); `            IF( ID .EQ. LI .AND. ITYPE .GT. 0 ) THEN` (34); `              IEX=ITL1(2,J)` (35); `              CALL SPCDSETI(IEX,INDOF,KK,ISPD,NSPD)` (36); `              GOTO 300` (37); `            ENDIF` (38); `  310     CONTINUE` (40); `  300   CONTINUE` (42) `GOTO 300`(37)의 대상은 42행이다. [11-04 전수 검증 정정] |
| 44–64 | 시작 시 TSPCDSETI 루틴(1)·IDLFLG 분기(21) 안이다. ELSE(44)는 직접 IDLOAD에 일치하는 시간 하중을 찾는다(46–53). 같은 ITYPE 제외 조건을 적용하고 첫 일치 항목을 SPCDSETI로 처리한 뒤 반환한다(55–64). 원문: `      ELSE` (44); `        DO 410 J=1,NTLD1` (46); `          ID=ITL1(1,J)` (48); `          ITYPE=ITL1(3,J)` (49); `          IF( IDYN == 0 .AND. ITYPE >= 2 ) CYCLE` (51); `          IF( ID .EQ. IDLOAD .AND. ITYPE .GT. 0 ) THEN` (53); `            IEX=ITL1(2,J)` (54); `            CALL SPCDSETI(IEX,INDOF,KK,ISPD,NSPD)` (55); `            GOTO 500` (56); `          ENDIF` (57); `  410   CONTINUE` (59); `      ENDIF` (61); `  500 RETURN` (63); `      END` (64) 바깥 블록은 `IF(IDLFLG .EQ. 1) THEN`(21)이며 61행에서 닫힌다. `GOTO 500`(56)의 대상은 63행의 RETURN이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
