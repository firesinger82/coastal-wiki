---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_volchk.f
lines: 60
sha256: e84946b72add70ebd6a1b072ad1f1e6ab0850a05192379f5a1f72df1c9d87e90
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_volchk.f — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 체적 확인(volume check) 루틴의 암시적 실수·네 INCLUDE 및 배열·포인터 선언. IFIX(NNOD)를 할당하고 0으로 초기화한다(1–18). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_VOLCHK(IFIX0,IELM,IGNO,GRID,POS,XX,YY)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      INCLUDE 'VF_APARAI.h'` (7)<br>`      INCLUDE 'SF_STRUCT.h'` (8)<br>`      DIMENSION IFIX0(NNOD0),IELM(24,NELM),NP(20),XG(3),GRID(3,NNOD)` (10)<br>`     &         ,POS(3,NNOD),XX(MAXG1,NUMI),YY(MAXG1,NUMJ),IGNO(NNOD)` (11)<br>`     &         ,P0(3,4,24),P(3,4,24)` (12)<br>`      INTEGER, POINTER :: IFIX(:)` (14)<br>`      ALLOCATE( IFIX(NNOD) )` (16)<br>`      IFIX(:) = 0` (18) |
| 20–51 | 시작 시 1행 루틴 안. LTYP가 2가 아니면 다음 I로 넘어간다(26). SF_MEAN4 호출 뒤 XG(1)·XG(2)가 30–31행의 하한 이상·상한 미만이면 GRID와 POS에 SF_TETDIV를 각각 호출한다(28–34). SF_TETVOL 결과의 비 V/V0<.2D0이면 `IFIX( NP(1:N) ) = 1`을 수행한다(38–42). 43행 EXIT는 36–46행 J 루프를 나간다. 해석: 평균 위치에 따른 영역 판정과 체적 감소에 따른 절점 고정 표시에 해당한다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      DO I = 1, NELM` (20)<br>`        LTYP = IELM(3,I)` (22)<br>`        N = IELM(4,I)` (23)<br>`        NP(1:N) = IELM(5:4+N,I)` (24)<br>`        IF( LTYP /= 2 ) CYCLE` (26)<br>`        CALL SF_MEAN4(XG,POS,3,NP,N)` (28)<br>`        IF( XG(1) >= XX(1,MYIS) .AND. XG(1) < XX(1,MYIE+1) .AND.` (30)<br>`     &      XG(2) >= YY(1,MYJS) .AND. XG(2) < YY(1,MYJE+1) ) THEN` (31)<br>`          CALL SF_TETDIV(NT,P0,N,NP,GRID)` (33)<br>`          CALL SF_TETDIV(NT,P,N,NP,POS)` (34)<br>`          DO J = 1, NT` (36)<br>`            CALL SF_TETVOL(P0(1,1,J),V0)` (38)<br>`            CALL SF_TETVOL(P(1,1,J),V)` (39)<br>`            IF( V/V0 < .2D0 ) THEN` (41)<br>`              IFIX( NP(1:N) ) = 1` (42)<br>`              EXIT` (43)<br>`            ENDIF` (44)<br>`          ENDDO` (46)<br>`        ENDIF` (48)<br>`      ENDDO` (50) [11-04 전수 검증 정정] |
| 52–60 | 시작 시 1행 루틴 안. IPART=0이면 SF_MPI_REDUCE_I, IPART=1이면 SF_REDUCE_I를 호출하여 IFIX0를 인수로 전달한다(52–56). 이 분기 사슬에는 ELSE가 없다. IFIX는 분기 밖에서 해제한다(58). 해석: REDUCE라는 이름으로 볼 때 IFIX0에 결과를 모으는 호출이다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      IF( IPART == 0 ) THEN` (52)<br>`        CALL SF_MPI_REDUCE_I(IFIX,IFIX0,NNOD,0)` (53)<br>`      ELSEIF( IPART == 1 ) THEN` (54)<br>`        CALL SF_REDUCE_I(IFIX0,NNOD0,IFIX,IGNO,NNOD)` (55)<br>`      ENDIF` (56)<br>`      DEALLOCATE( IFIX )` (58)<br>`      END` (60) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–41: V/V0 계산 앞에 V0=0을 따로 검사하는 문장은 이 루틴에 없다.
- 41: 고정 표시 임계값은 .2D0이다.
