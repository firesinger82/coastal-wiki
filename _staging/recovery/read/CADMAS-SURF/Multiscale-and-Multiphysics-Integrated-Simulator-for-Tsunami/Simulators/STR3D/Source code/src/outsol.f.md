---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/outsol.f
lines: 100
sha256: 98dc024a82a1ccd3ec78ff60f25b98b90ba53135be2f076b7030254810cdc0c0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# outsol.f — 판독 구간 기록

구간은 1행부터 100행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | OUTSOL 입구와 포인터(pointer)·배열 선언이다(1–13). 절점별 누적 배열을 할당하고 0으로 초기화한다(15–31). 원문: `      SUBROUTINE OUTSOL(KK,GRID,IELM,NM,EPSG,SIGG,MGP,PG,NP_ENS,NG_ENS`<br>`     &                 ,IG_ENS,ITO,IFL)` (1–2); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*),EPSG(6,MGP,*),SIGG(6,MGP,*),GRID(3,*),IELM(NM,*)`<br>`     &         ,SIG(6,20),EPS(6,20),PRNSIG(3,20),PRNEPS(3,20),VMSIG(20)`<br>`     &         ,NP_ENS(6),NG_ENS(*),IG_ENS(*),IFL(*),PG(*)` (7–9); `      INTEGER, POINTER :: IAVE(:)` (11); `      REAL(8), POINTER :: SIGP(:,:), EPSP(:,:), PRNSIGP(:,:),`<br>`     &                    PRNEPSP(:,:), VMSIGP(:)` (12–13); `      NNOD = KK(8)` (15); `      NELM = KK(12)` (16); `      NNODI = KK(26)` (17); `      ALLOCATE( IAVE(NNOD) )` (19); `      ALLOCATE( SIGP(6,NNOD) )` (20); `      ALLOCATE( EPSP(6,NNOD) )` (21); `      ALLOCATE( PRNSIGP(3,NNOD) )` (22); `      ALLOCATE( PRNEPSP(3,NNOD) )` (23); `      ALLOCATE( VMSIGP(NNOD) )` (24); `      IAVE(:) = 0` (26); `      SIGP(:,:) = 0.` (27); `      EPSP(:,:) = 0.` (28); `      PRNSIGP(:,:) = 0.` (29); `      PRNEPSP(:,:) = 0.` (30); `      VMSIGP(:) = 0.` (31) |
| 33–59 | 시작 시 OUTSOL 루틴(1) 안이다. 요소 루프는 ITYP 2·6만 처리한다(33–38). 절점 수별 STRTE1·STRTE2·STRPN1·STRPN2·STRHX1·STRHX2 호출 뒤 MERGS를 호출한다(40–56). 원문: `      DO I = 1, NELM` (33); `        ITYP = IELM(2,I)` (35); `        NNP = IELM(3,I)` (36); `        IF( ITYP /= 2 .AND. ITYP /= 6 ) CYCLE` (38); `        SELECT CASE( NNP )` (40); `        CASE( 4 )` (41); `          CALL STRTE1(EPS,SIG,EPSG(1,1,I),SIGG(1,1,I))` (42); `        CASE( 10 )` (43); `          CALL STRTE2(EPS,SIG,EPSG(1,1,I),SIGG(1,1,I))` (44); `        CASE( 6 )` (45); `          CALL STRPN1(EPS,SIG,EPSG(1,1,I),SIGG(1,1,I),GRID,IELM(8,I))` (46); `        CASE( 15 )` (47); `          CALL STRPN2(EPS,SIG,EPSG(1,1,I),SIGG(1,1,I))` (48); `        CASE( 8 )` (49); `          CALL STRHX1(EPS,SIG,EPSG(1,1,I),SIGG(1,1,I),GRID,IELM(8,I))` (50); `        CASE( 20 )` (51); `          CALL STRHX2(EPS,SIG,EPSG(1,1,I),SIGG(1,1,I))` (52); `        END SELECT` (53); `        CALL MERGS(IAVE,SIGP,EPSP,SIG,EPS,PRNSIGP,PRNEPSP,PRNSIG`<br>`     &            ,PRNEPS,VMSIGP,VMSIG,IELM(8,I),NNP)` (55–56); `      ENDDO` (58) |
| 60–100 | 시작 시 OUTSOL 루틴(1) 안이다. PG를 SIGP에서 빼는 블록은 주석이다(60–64). 전체 절점에서 PRNSTR을 호출한다(66–69). 루트 rank는 두 파트 구간에 WTSOL을 호출한다(71–83). 비루트 rank는 SIGP·EPSP·PRNSIGP를 전송한다(85–89). 배열을 해제한다(93–98). 원문: 주석: `C      IF( KK(25) > 0 ) THEN` (60); 주석: `C        DO I = 1, NNOD` (61); 주석: `C          SIGP(1:3,I) = SIGP(1:3,I) - PG(I)` (62); 주석: `C        ENDDO` (63); 주석: `C      ENDIF` (64); `      DO I = 1, NNOD` (66); `        CALL PRNSTR(1,SIGP(1,I),EPSP(1,I),PRNSIGP(1,I),PRNEPSP(1,I)`<br>`     &             ,VMSIGP(I),ITO)` (67–68); `      ENDDO` (69); `      IF( MYRANK == 0 ) THEN` (71); `        ICW = 0` (73); `        IPS = 1` (75); `        IPE = NP_ENS(2)` (76); `        CALL WTSOL(SIGP,EPSP,PRNSIGP,NNOD,IPS,IPE,NG_ENS,IG_ENS,IFL,ICW)` (78); `        IPS = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + 1` (80); `        IPE = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + NP_ENS(6)` (81); `        CALL WTSOL(SIGP,EPSP,PRNSIGP,NNOD,IPS,IPE,NG_ENS,IG_ENS,IFL,ICW)` (83); `      ELSE` (85); `        CALL M_MPI_SEND_D(SIGP,6*NNODI,0)` (87); `        CALL M_MPI_SEND_D(EPSP,6*NNODI,0)` (88); `        CALL M_MPI_SEND_D(PRNSIGP,3*NNODI,0)` (89); `      ENDIF` (91); `      DEALLOCATE( IAVE )` (93); `      DEALLOCATE( SIGP )` (94); `      DEALLOCATE( EPSP )` (95); `      DEALLOCATE( PRNSIGP )` (96); `      DEALLOCATE( PRNEPSP )` (97); `      DEALLOCATE( VMSIGP )` (98); `      END` (100) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60–64: SIGP의 첫 세 성분에서 PG를 빼는 블록은 전체가 주석 처리되어 있다.
- 40–56: 절점 수 분기는 4·10·6·15·8·20을 처리한다. CASE DEFAULT는 없으며, SELECT CASE 뒤의 MERGS 호출은 분기 밖에 있다.
