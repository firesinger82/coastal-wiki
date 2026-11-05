---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/outsoil.f
lines: 62
sha256: 4d0194da67d635255ce12d737103c68bf9d9bf8aac46c883b8ea83142957aa75
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# outsoil.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | OUTSOIL은 MPI_PARAM을 사용하여 간극수 유량(pore water flux)을 출력한다. 출력명 근거는 51행 호출 대상 `geo/wtsoil.f:6`의 `pore water flux`이다. 실수 IMPLICIT와 배열 범위를 아래에 적었다. NNOD·NELM·NNODI를 KK에서 얻는다. NAVE·VELP를 할당하고 0으로 초기화한다. 원문: `      SUBROUTINE OUTSOIL(KK,IELM,NM,VELG,MGP,VELE,NP_ENS,NG_ENS,IG_ENS` (1); `     &                  ,IFL)` (2); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION KK(*),IELM(NM,*),VEL(3,20),VELG(3,MGP,*),VELE(3,*)` (6); `     &         ,NP_ENS(6),NG_ENS(*),IG_ENS(*)` (7); `      INTEGER, POINTER :: NAVE(:)` (9); `      REAL(8), POINTER :: VELP(:,:)` (10); `      NNOD = KK(8)` (12); `      NELM = KK(12)` (13); `      NNODI = KK(26)` (14); `      ALLOCATE( NAVE(NNOD) )` (16); `      ALLOCATE( VELP(3,NNOD) )` (17); `      NAVE(:) = 0` (19); `      VELP(:,:) = 0.` (20) [11-04 전수 검증 보완] |
| 22–45 | 요소 I=1,NELM에서 ITYP=6만 처리한다. ND별 VELTE1·VELTE2·VELPN2·VELHX2로 절점 값을 구한다. VELHX2의 방향별 적분점 수 NG는 ND=8에서 2, ND=20에서 3이다. NG의 선언 근거는 `geo/velhx2.f:1,4`이다. VAVRG로 요소 절점 값을 전역 절점 평균에 반영한다. 평균식의 근거는 `geo/vavrg.f:6–11`이다. 원문: `      DO I = 1, NELM` (22); `        ITYP = IELM(2,I)` (24); `        ND   = IELM(3,I)` (25); `        IF( ITYP /= 6 ) CYCLE` (27); `        SELECT CASE( ND )` (29); `        CASE( 4 )` (30); `          CALL VELTE1(VEL,VELG(1,1,I))` (31); `        CASE( 10 )` (32); `          CALL VELTE2(VEL,VELG(1,1,I))` (33); `        CASE( 6, 15 )` (34); `          CALL VELPN2(VEL,VELG(1,1,I),ND)` (35); `        CASE( 8 )` (36); `          CALL VELHX2(VEL,VELG(1,1,I),VELE(1,I),ND,2)` (37); `        CASE( 20 )` (38); `          CALL VELHX2(VEL,VELG(1,1,I),VELE(1,I),ND,3)` (39); `        END SELECT` (40); `        CALL VAVRG(VELP,VEL,IELM(8,I),ND,NAVE)` (42); `      ENDDO` (44) [11-04 전수 검증 정정] |
| 46–62 | MYRANK=0이면 NP_ENS의 2·3·4번째 개수 합 다음 위치부터 6번째 개수만큼을 IPS–IPE로 정한다. WTSOIL에 VELP와 NG_ENS·IG_ENS를 전달한다. ELSE는 VELP의 3*NNODI개 값을 목적지 0에 전송한다. NNODI는 14행에서 KK(26)으로 설정한다. 해석: NNODI는 해당 랭크의 내부 절점 수로 보인다. 작업 배열을 해제한다. 원문: `      IF( MYRANK == 0 ) THEN` (46); `        IPS = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + 1` (48); `        IPE = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + NP_ENS(6)` (49); `        CALL WTSOIL(VELP,NNOD,IPS,IPE,NG_ENS,IG_ENS,IFL)` (51); `      ELSE` (53); `        CALL M_MPI_SEND_D(VELP,3*NNODI,0)` (55); `      ENDIF` (57); `      DEALLOCATE( NAVE )` (59); `      DEALLOCATE( VELP )` (60); `      END` (62) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–42: ND 선택에는 CASE DEFAULT가 없다. 선택 뒤 VAVRG를 무조건 호출한다.
- 6: 절점 작업 배열 VEL은 (3,20)으로 고정한다.
