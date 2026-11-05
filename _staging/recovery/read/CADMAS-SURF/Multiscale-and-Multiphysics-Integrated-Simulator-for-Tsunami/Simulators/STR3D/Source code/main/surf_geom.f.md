---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/surf_geom.f
lines: 95
sha256: 7c7ef97fd5714c250acea00617eb16411d0818ff0e57d657279187daee662f10
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# surf_geom.f — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | SURF_GEOM은 표면(surface) 요소 기하를 구성한다. DATA ETYPE은 tria3·quad4·tria6·quad8이다(9). IP(I)=JPART인 IPFC 항목만 선택하고 IPFC(2,I)의 ND=3·4·6·8에 유형 1:4를 대응시킨다(14–29). 요소 목록·사용 절점을 만들고 IG·LG로 부분 절점 대응을 구성한다(31–46). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE SURF_GEOM( NG, IG, NE, IE, IP, IPART, JPART, INDG,` (1) <br> `     &                      GRID, IPFC, NNOD, NPFC, NUG, LG, IFG )` (2) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (4) <br> `      CHARACTER*8 ETYPE(4)` (5) <br> `      DIMENSION NE(4), NUG(NNOD), IPFC(10,NPFC), IE(NPFC,4), IG(NNOD),` (6) <br> `     &          LG(NNOD), INDG(NNOD), GRID(3,NNOD), KN(8), IP(NPFC)` (7) <br> `      DATA ETYPE / 'tria3   ', 'quad4   ', 'tria6   ', 'quad8   ' /` (9) <br> `      NE(:) = 0` (11) <br> `      NUG(:) = 0` (12) <br> `      DO I = 1, NPFC` (14) <br> `        IF( IP(I) /= JPART ) CYCLE` (16) <br> `        ND = IPFC(2,I)` (18) <br> `        SELECT CASE( ND )` (20) <br> `        CASE( 3 )` (21) <br> `          ITYP = 1` (22) <br> `        CASE( 4 )` (23) <br> `          ITYP = 2` (24) <br> `        CASE( 6 )` (25) <br> `          ITYP = 3` (26) <br> `        CASE( 8 )` (27) <br> `          ITYP = 4` (28) <br> `        END SELECT` (29) <br> `        NE(ITYP) = NE(ITYP) + 1` (31) <br> `        IE( NE(ITYP), ITYP ) = I` (32) <br> `        NUG( IPFC(3:2+ND,I) ) = 1` (33) <br> `      ENDDO` (35) <br> `      NG = 0` (37) <br> `      IG(:) = 0` (38) <br> `      DO I = 1, NNOD` (40) <br> `        IF( NUG(I) == 1 ) THEN` (41) <br> `          NG = NG + 1` (42) <br> `          IG(NG) = I` (43) <br> `          LG(I) = NG` (44) <br> `        ENDIF` (45) <br> `      ENDDO` (46) [11-04 전수 검증 정정] |
| 48–95 | 시작 시 SURF_GEOM(1) 안이며 앞 루프 밖이다. 부분 번호 IPART·이름 JPART·외부 절점 번호·좌표를 출력한다(48–66). 4개 유형을 순회하며 빈 유형은 건너뛴다(68–70). 요소 번호에는 IE에서 얻은 면 목록 위치 IENO를 출력한다(76–79). IPFC의 절점 연결(connectivity)을 LG로 변환해 출력하고 루틴을 종료한다(81–95). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      WRITE(IFG,'(A4)') 'part'` (48) <br> `      WRITE(IFG,'(I10)') IPART` (50) <br> `      WRITE(IFG,'(A,X,I0)') 'surface elements', JPART` (52) <br> `      WRITE(IFG,'(A)') 'coordinates'` (54) <br> `      WRITE(IFG,'(I10)') NG` (56) <br> `      DO I = 1, NG` (58) <br> `        WRITE(IFG,'(I10)') INDG(IG(I))` (59) <br> `      ENDDO` (60) <br> `      DO J = 1, 3` (62) <br> `        DO I = 1, NG` (63) <br> `          WRITE(IFG,'(1PE12.5)') GRID(J,IG(I))` (64) <br> `        ENDDO` (65) <br> `      ENDDO` (66) <br> `      DO ITYP = 1, 4` (68) <br> `        IF( NE(ITYP) == 0 ) CYCLE` (70) <br> `        WRITE(IFG,'(A)') ETYPE(ITYP)` (72) <br> `        WRITE(IFG,'(I10)') NE(ITYP)` (74) <br> `        DO I = 1, NE(ITYP)` (76) <br> `          IENO = IE(I,ITYP)` (77) <br> `          WRITE(IFG,'(I10)') IENO` (78) <br> `        ENDDO` (79) <br> `        DO I = 1, NE(ITYP)` (81) <br> `          IENO = IE(I,ITYP)` (83) <br> `          ND = IPFC(2,IENO)` (85) <br> `          KN(1:ND) = IPFC(3:2+ND,IENO)` (87) <br> `          WRITE(IFG,'(20I10)') LG( KN(1:ND) )` (89) <br> `        ENDDO` (91) <br> `      ENDDO` (93) <br> `      END` (95) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–29: 열거된 ND 이외에 ITYP를 설정하는 CASE DEFAULT는 없다.
- 16·50–52: 입력 면의 선택 기준은 JPART이며 출력 부분 번호는 IPART다.
