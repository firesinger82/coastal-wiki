---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_soil.f
lines: 89
sha256: 0b2d0e61bf7b1994a9a3d0b55209cf3f88cf4477aa3670ca8e4448fdfcc574e2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_soil.f — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | FMP_SOIL은 MPI_PARAM과 실수 IMPLICIT 선언을 사용한다. VEL(3,20)·VELG(3,MGP,*)·VELE(3,*) 등을 선언한다. KK에서 절점 수와 요소 수를 얻는다. NAVE·VELP·TVELP를 할당하고 누적 횟수·절점 유량 배열을 0으로 초기화한다. 원문: `      SUBROUTINE FMP_SOIL(IOUT,KK,INDG,IELM,NM,VELG,MGP,VELE,IFL)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      CHARACTER*1 C /','/` (5); `      DIMENSION KK(*),IELM(NM,*),VEL(3,20),VELG(3,MGP,*),VELE(3,*)` (6); `     &         ,INDG(*)` (7); `      INTEGER, POINTER :: NAVE(:)` (9); `      REAL(8), POINTER :: VELP(:,:),TVELP(:)` (10); `      NNOD = KK(8)` (12); `      NELM = KK(12)` (13); `      ALLOCATE( NAVE(NNOD) )` (15); `      ALLOCATE( VELP(3,NNOD) )` (16); `      ALLOCATE( TVELP(NNOD) )` (17); `      NAVE(:) = 0` (19); `      VELP(:,:) = 0.` (20) |
| 22–49 | 요소 루프에서 ITYP가 6이 아니면 CYCLE한다. ND별로 VELTE1·VELTE2·VELPN2·VELHX2를 호출하여 절점 위치의 값을 얻는다. ND=8의 VELHX2 인수 NG는 2, ND=20은 3이다. NG의 선언 근거는 `geo/velhx2.f:1,4`이다. VAVRG로 절점 평균을 갱신한다. 평균 갱신의 근거는 `geo/vavrg.f:6–11`이다. 별도 절점 루프에서 VECML2로 세 성분 크기를 계산한다. 원문: `      DO I = 1, NELM` (22); `        ITYP = IELM(2,I)` (24); `        ND   = IELM(3,I)` (25); `        IF( ITYP /= 6 ) CYCLE` (27); `        SELECT CASE( ND )` (29); `        CASE( 4 )` (30); `          CALL VELTE1(VEL,VELG(1,1,I))` (31); `        CASE( 10 )` (32); `          CALL VELTE2(VEL,VELG(1,1,I))` (33); `        CASE( 6, 15 )` (34); `          CALL VELPN2(VEL,VELG(1,1,I),ND)` (35); `        CASE( 8 )` (36); `          CALL VELHX2(VEL,VELG(1,1,I),VELE(1,I),ND,2)` (37); `        CASE( 20 )` (38); `          CALL VELHX2(VEL,VELG(1,1,I),VELE(1,I),ND,3)` (39); `        END SELECT` (40); `        CALL VAVRG(VELP,VEL,IELM(8,I),ND,NAVE)` (42); `      ENDDO` (44); `      DO I = 1, NNOD` (46); `        CALL VECML2(TVELP(I),VELP(1,I),3)` (47); `      ENDDO` (48) [11-04 전수 검증 정정] |
| 50–89 | MYRANK=0이면 결과 번호 71–74의 전체·X·Y·Z 간극수 유량(pore water flux)을 WT_VEC으로 출력한다. ELSE에서는 `NNODI = KK(26)`으로 전송 크기를 정한다. 목적지 0으로 TVELP의 NNODI개 값과 VELP의 3*NNODI개 값을 전송한다. 해석: NNODI는 해당 랭크의 내부 절점 수로 보인다. 세 포인터 배열을 해제한다. 원문: `      IF( MYRANK == 0 ) THEN` (50); `        WRITE(IFL,'(3(I0,A))') IOUT,C,71,C,1,C` (52); `        WRITE(IFL,'(A)') 'Total Pore Water Flux'` (54); `        CALL WT_VEC(72,73,74,7,INDG,TVELP,1,1,NNOD,IFL)` (56); `        WRITE(IFL,'(3(I0,A))') IOUT,C,72,C,1,C` (58); `        WRITE(IFL,'(A)') 'X Pore Water Flux'` (60); `        CALL WT_VEC(72,0,0,7,INDG,VELP,1,3,NNOD,IFL)` (62); `        WRITE(IFL,'(3(I0,A))') IOUT,C,73,C,1,C` (64); `        WRITE(IFL,'(A)') 'Y Pore Water Flux'` (66); `        CALL WT_VEC(0,73,0,7,INDG,VELP,2,3,NNOD,IFL)` (68); `        WRITE(IFL,'(3(I0,A))') IOUT,C,74,C,1,C` (70); `        WRITE(IFL,'(A)') 'Z Pore Water Flux'` (72); `        CALL WT_VEC(0,0,74,7,INDG,VELP,3,3,NNOD,IFL)` (74); `      ELSE` (76); `        NNODI = KK(26)` (78); `        CALL M_MPI_SEND_D(TVELP,NNODI,0)` (80); `        CALL M_MPI_SEND_D(VELP,3*NNODI,0)` (81); `      ENDIF` (83); `      DEALLOCATE( NAVE )` (85); `      DEALLOCATE( VELP )` (86); `      DEALLOCATE( TVELP )` (87); `      END` (89) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–42: ND 선택에는 CASE DEFAULT가 없다. 선택 뒤 VAVRG 호출은 무조건 수행한다.
- 6·31–39: 절점 작업 배열 VEL은 최대 20개 절점으로 선언되어 있다.
