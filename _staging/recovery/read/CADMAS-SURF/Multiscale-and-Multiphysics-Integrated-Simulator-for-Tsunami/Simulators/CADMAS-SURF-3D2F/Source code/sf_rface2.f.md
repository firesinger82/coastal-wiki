---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_rface2.f
lines: 74
sha256: 4a08a8105326acc7c0c5f0383a59f6ebaf496d547421e4459a6111bfabe2e181
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_rface2.f — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | SF_RFACE2의 선언부다. EPS의 DATA 값은 1.D-1이다(13). IPART=0이면 루트(root)의 IRGRID0를 복사하고 VF_P1BCSI로 배포한다(15–17). IPART=1이면 SF_BCAST_I를 호출한다(18–20). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_RFACE2()` (1); `      USE VF_A2ARRAY` (3); `      USE SF_ARRAY` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      INCLUDE 'VF_A0PRM.h'` (8); `      INCLUDE 'VF_ANUMBI.h'` (9); `      INCLUDE 'VF_APARAI.h'` (10); `      INCLUDE 'SF_STRUCT.h'` (11); `      DATA EPS / 1.D-1 /` (13); `      IF( IPART == 0 ) THEN` (15); `        IF( MYRANK == 0 ) IRGRID(:) = IRGRID0(:)` (16); `        CALL VF_P1BCSI(IRGRID,NNOD,0)` (17); `      ELSEIF( IPART == 1 ) THEN` (18); `        CALL SF_BCAST_I(IRGRID,IGNO,NNOD,IRGRID0,NNOD0,1)` (19); `      ENDIF` (20). 15–20행의 IF/ELSEIF에는 ELSE가 없다. IPART가 0과 1이 아니면 이 배포 호출들을 건너뛴다. [11-04 전수 검증 보완] |
| 22–55 | 시작 시 1행 SF_RFACE2 루틴 안. SF_RFACE2 안이며 배포 분기 밖. IRGRID>0인 절점만 검사한다(22–24). 28행 조건이 참이면 XS에서 XX(2,I)*EPS를 뺀다(29). 34행 조건이 참이면 XE에 XX(2,I)*EPS를 더한다(35). GRID의 X 좌표가 들어오면 Y 방향 구간도 같은 방식으로 만든다(40–54). 원문(연속 표시는 앞 문장에 이어짐): `      DO 10 IG = 1, NNOD` (22); `        IF( IRGRID(IG) <= 0 ) CYCLE` (24); `        DO I = MYIS, MYIE` (26); `          IF( I == MYIS .AND. MYMIS == 1 ) THEN` (28); `            XS = XX(1,I) - XX(2,I) * EPS` (29); `          ELSE` (30); `            XS = XX(1,I)` (31); `          ENDIF` (32); `          IF( I == MYIE .AND. MYMIE == 1 ) THEN` (34); `            XE = XX(1,I+1) + XX(2,I) * EPS` (35); `          ELSE` (36); `            XE = XX(1,I+1)` (37); `          ENDIF` (38); `          IF( GRID(1,IG) >= XS .AND. GRID(1,IG) < XE ) THEN` (40); `            DO J = MYJS, MYJE` (42); `              IF( J == MYJS .AND. MYMJS == 1 ) THEN` (44); `                YS = YY(1,J) - YY(2,J) * EPS` (45); `              ELSE` (46); `                YS = YY(1,J)` (47); `              ENDIF` (48); `              IF( J == MYJE .AND. MYMJE == 1 ) THEN` (50); `                YE = YY(1,J+1) + YY(2,J) * EPS` (51); `              ELSE` (52); `                YE = YY(1,J+1)` (53); `              ENDIF` (54). [11-04 전수 검증 정정] |
| 56–74 | 시작 시 `      DO 10 IG = 1, NNOD` (22), `        DO I = MYIS, MYIE` (26), `          IF( GRID(1,IG) >= XS .AND. GRID(1,IG) < XE ) THEN` (40), `            DO J = MYJS, MYJE` (42) 안이다. 각 블록은 72행 레이블 10, 68행 ENDDO, 66행 ENDIF, 64행 ENDDO에서 닫힌다. Y 구간에 들어오면 I+NUMI*(J-1)을 저장하고 72행 레이블 10으로 이동한다(56–60). X와 Y 구간 조건을 함께 만족하는 I,J 쌍을 찾지 못하면 IRGRID(IG)=0으로 설정한다(70). 원문(연속 표시는 앞 문장에 이어짐): `              IF( GRID(2,IG) >= YS .AND. GRID(2,IG) < YE ) THEN` (56); `                IRGRID(IG) = I + NUMI*(J-1)  ! 節点が属するセル` (58) (절점이 속하는 셀); `                GOTO 10` (60); `              ENDIF` (62); `            ENDDO` (64); `          ENDIF` (66); `        ENDDO` (68); `        IRGRID(IG) = 0  ! 領域外` (70) (영역 밖); `   10 CONTINUE` (72); `      END` (74). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40·56·58: 셀 검색에는 POS가 아닌 GRID의 X·Y 좌표를 사용한다. 저장하는 셀 번호에는 K 항이 없다.
