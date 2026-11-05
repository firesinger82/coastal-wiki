---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/part_geom.f
lines: 109
sha256: a300135886c84cd363a199d6208e0879c04c0fa9c9d3ff5418e723f6e4172fba
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# part_geom.f — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | PART_GEOM의 인수·암시적 형·배열 선언과 DATA 요소 이름 표. 현재 IPART 요소만 선택한다. 절점 수 4·6·8·10·15·20을 여섯 요소 유형에 대응시키고 사용 절점을 표시한다. 원문: 연속문(1–2): `      SUBROUTINE PART_GEOM( INDG, GRID, IELM, NM, NNOD, NSOL, IE, NUG,` <br> `     &                      IG, LG, IFG, IEP, IPART )`; `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      CHARACTER*8 ETYPE(6)` (5); 연속문(6–8): `      DIMENSION NE(6), NUG(NNOD), IELM(NM,NSOL), IE(NSOL,6), IG(NNOD),` <br> `     &          LG(NNOD), INDG(NNOD), GRID(3,NNOD), KN(20), IWK(4),` <br> `     &          IEP(NSOL)`; 연속문(10–11): `      DATA ETYPE / 'tetra4  ', 'penta6  ', 'hexa8   ', 'tetra10 ',` <br> `     &             'penta15 ', 'hexa20  ' /`; `      NE(:) = 0` (13); `      NUG(:) = 0` (14); `      DO I = 1, NSOL` (16); `        IF( IEP(I) /= IPART ) CYCLE` (18); `        ND = IELM(3,I)` (20); `        SELECT CASE( ND )` (22); `        CASE( 4 )` (23); `          ITYP = 1` (24); `        CASE( 6 )` (25); `          ITYP = 2` (26); `        CASE( 8 )` (27); `          ITYP = 3` (28); `        CASE( 10 )` (29); `          ITYP = 4` (30); `        CASE( 15 )` (31); `          ITYP = 5` (32); `        CASE( 20 )` (33); `          ITYP = 6` (34); `        END SELECT` (35); `        NE(ITYP) = NE(ITYP) + 1` (37); `        IE( NE(ITYP), ITYP ) = I` (38); `        NUG( IELM(8:7+ND,I) ) = 1` (39); `      ENDDO` (41). |
| 43–72 | PART_GEOM 루틴 안. 사용 절점의 지역 번호를 만들고 part 머리말·좌표 수·절점 식별자·세 좌표 성분을 출력한다. 원문: `      NG = 0` (43); `      DO I = 1, NNOD` (45); `        IF( NUG(I) == 1 ) THEN` (46); `          NG = NG + 1` (47); `          IG(NG) = I` (48); `          LG(I) = NG` (49); `        ENDIF` (50); `      ENDDO` (51); `      WRITE(IFG,'(A4)') 'part'` (53); `      WRITE(IFG,'(I10)') IPART` (55); `      WRITE(IFG,'(A,I0)') 'PART ', IPART` (57); `      WRITE(IFG,'(A)') 'coordinates'` (59); `      WRITE(IFG,'(I10)') NG` (61); `      DO I = 1, NG` (63); `        WRITE(IFG,'(I10)') INDG(IG(I))` (64); `      ENDDO` (65); `      DO J = 1, 3` (67); `        DO I = 1, NG` (68); `          WRITE(IFG,'(1PE12.5)') GRID(J,IG(I))` (69); `        ENDDO` (70); `      ENDDO` (71). |
| 73–109 | PART_GEOM 루틴 안. 비어 있지 않은 요소 유형별로 이름·개수·식별자를 출력한다. 15절점 요소의 10:12와 13:15, 20절점 요소의 13:16과 17:20을 교환한 뒤 지역 연결 번호를 출력한다. 원문: `      DO ITYP = 1, 6` (73); `        IF( NE(ITYP) == 0 ) CYCLE` (75); `        WRITE(IFG,'(A)') ETYPE(ITYP)` (77); `        WRITE(IFG,'(I10)') NE(ITYP)` (79); `        DO I = 1, NE(ITYP)` (81); `          IENO = IE(I,ITYP)` (82); `          WRITE(IFG,'(I10)') IELM(1,IENO)` (83); `        ENDDO` (84); `        DO I = 1, NE(ITYP)` (86); `          IENO = IE(I,ITYP)` (88); `          ND = IELM(3,IENO)` (90); `          KN(1:ND) = IELM(8:7+ND,IENO)` (91); `          IF( ND == 15 ) THEN` (93); `            IWK(1:3) = KN(10:12)` (94); `            KN(10:12) = KN(13:15)` (95); `            KN(13:15) = IWK(1:3)` (96); `          ELSEIF( ND == 20 ) THEN` (97); `            IWK(:) = KN(13:16)` (98); `            KN(13:16) = KN(17:20)` (99); `            KN(17:20) = IWK(:)` (100); `          ENDIF` (101); `          WRITE(IFG,'(20I10)') LG( KN(1:ND) )` (103); `        ENDDO` (105); `      ENDDO` (107); `      END` (109). 93·97행의 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–39: SELECT CASE는 여섯 절점 수만 열거한다. CASE DEFAULT와 해당 문장 직전 ITYP 초기화는 없다.
- 45–51: LG는 NUG(I)==1인 절점에서만 대입한다. 전체 LG 초기화문은 없다.
