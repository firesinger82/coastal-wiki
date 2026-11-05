---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_pos_updt.f
lines: 82
sha256: cf67d6dac76b9b4848234a16dd3e035ce11fff90b86c44b1162d7c5c64fafcdd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_pos_updt.f — 판독 구간 기록

구간은 1행부터 82행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | SF_POS_UPDT의 선언부다. IRND를 0으로 초기화한다(19–21). ISTM=1이면 IELM(3,I)=2인 요소의 절점을 표시한다(23–30). 각 방향 배열의 DIM=2 최솟값을 구하고 두 번째 성분 중 최소값을 SF_MPI_ALLREDUCE_D로 집약한다(32–38). IFIX를 할당하고 0으로 초기화한다(40–42). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_POS_UPDT(POS,SPC,GRDL,IGFC,IELM,POSN,XX,YY,ZZ)` (1); `      USE SF_TYPE` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_ANUMBI.h'` (8); `      INCLUDE 'SF_STRUCT.h'` (9); `      TYPE(SPACE) :: SPC(NELM)` (11); `      DIMENSION POS(3,NNOD),POSN(3,NNOD),IGFC(NNOD),GRDL(NNOD)` (13); `     &         ,IELM(24,NELM),XX(MAXG1,NUMI),YY(MAXG1,NUMJ)` (14); `     &         ,ZZ(MAXG1,NUMK),XMIN(MAXG1),YMIN(MAXG1),ZMIN(MAXG1)` (15); `      INTEGER, POINTER :: IRND(:), IFIX(:)` (17); `      ALLOCATE( IRND(NNOD) )` (19); `      IRND(:) = 0` (21); `      IF( ISTM == 1 ) THEN` (23); `        DO I = 1, NELM` (24); `          IF( IELM(3,I) == 2 ) THEN` (25); `            N = IELM(4,I)` (26); `            IRND( IELM(5:4+N,I) ) = 1` (27); `          ENDIF` (28); `        ENDDO` (29); `      ENDIF` (30); `      XMIN = MINVAL(XX,DIM=2)` (32); `      YMIN = MINVAL(YY,DIM=2)` (33); `      ZMIN = MINVAL(ZZ,DIM=2)` (34); `      DMIN = DMIN1(XMIN(2),YMIN(2),ZMIN(2))` (36); `      CALL SF_MPI_ALLREDUCE_D(DMIN,D_MIN,1,2)` (38); `      ALLOCATE( IFIX(NNOD) )` (40); `      IFIX(:) = 0` (42). |
| 44–63 | 시작 시 1행 SF_POS_UPDT 루틴 안. SF_POS_UPDT 안이며 앞 분기 밖. 절점마다 IGFC=1이면 D_MIN의 1.D-3배, 그 외 IRND=1이면 GRDL의 1.D-2배, 나머지는 GRDL의 1.D-1배를 TOL로 사용한다(44–52). SF_LENGTH(DP,POSN(1,I),POS(1,I),3)를 호출한다(54). DP<TOL이면 IFIX=1로 표시하고 그 외에는 POS를 POSN으로 갱신한다(56–60). 원문(연속 표시는 앞 문장에 이어짐): `      DO I = 1, NNOD` (44); `        IF( IGFC(I) == 1 ) THEN` (46); `          TOL = D_MIN * 1.D-3` (47); `        ELSEIF( IRND(I) == 1 ) THEN` (48); `          TOL = GRDL(I) * 1.D-2` (49); `        ELSE` (50); `          TOL = GRDL(I) * 1.D-1` (51); `        ENDIF` (52); `        CALL SF_LENGTH(DP,POSN(1,I),POS(1,I),3)` (54); `        IF( DP < TOL ) THEN` (56); `          IFIX(I) = 1` (57); `        ELSE` (58); `          POS(:,I) = POSN(:,I)` (59); `        ENDIF` (60); `      ENDDO` (62). 해석: DP는 POSN과 POS 사이의 이동 거리로 읽힌다. [11-04 전수 검증 정정] |
| 64–82 | 시작 시 1행 SF_POS_UPDT 루틴 안. SF_POS_UPDT 안이며 앞 절점 루프 밖. 요소마다 SPC의 IFIX를 1로 설정한다(64–66). 요소 절점 중 IFIX=0이 하나라도 있으면 SPC의 IFIX를 0으로 만들고 절점 루프를 나간다(68–75). IRND·IFIX를 해제한다(79–80). 원문(연속 표시는 앞 문장에 이어짐): `      DO I = 1, NELM` (64); `        SPC(I)%IFIX = 1` (66); `        N = IELM(4,I)` (68); `        DO J = 1, N` (70); `          IF( IFIX( IELM(4+J,I) ) == 0 ) THEN` (71); `            SPC(I)%IFIX = 0` (72); `            EXIT` (73); `          ENDIF` (74); `        ENDDO` (75); `      ENDDO` (77); `      DEALLOCATE( IRND )` (79); `      DEALLOCATE( IFIX )` (80); `      END` (82). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46–51: IGFC(I)==1 분기가 IRND(I)==1 분기보다 먼저 적용된다. TOL의 계수는 각각 1.D-3·1.D-2·1.D-1로 고정되어 있다.
