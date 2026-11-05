---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/shell_geom.f
lines: 98
sha256: 7ed86f28dc6781e6947751c51b5fdb274cade8bafee7863fd46cec76c00c10b8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# shell_geom.f — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | SHELL_GEOM은 EnSight 셸(shell) 기하를 준비한다. DATA ETYPE은 tria3·quad4·tria6·quad8이다(9). 선택 부분과 다른 요소는 건너뛰고 9절점 요소는 출력상 8절점으로 취급한다(15–20). ND=3·4·6·8에 유형 1:4를 매기며 요소·사용 절점 목록을 구성한다(22–37). 전 절점에서 IG·LG를 만든다(42–48). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE SHELL_GEOM( NG, IG, NE, IE, IP, IPART, JPART, INDG,` (1) <br> `     &                       GRID, IELM, NM, NNOD, NSHL, NUG, LG, IFG )` (2) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (4) <br> `      CHARACTER*8 ETYPE(4)` (5) <br> `      DIMENSION NE(4), NUG(NNOD), IELM(NM,NSHL), IE(NSHL,4), IG(NNOD),` (6) <br> `     &          LG(NNOD), INDG(NNOD), GRID(3,NNOD), KN(8), IP(NSHL)` (7) <br> `      DATA ETYPE / 'tria3   ', 'quad4   ', 'tria6   ', 'quad8   ' /` (9) <br> `      NE(:) = 0` (11) <br> `      IE(:,:) = 0` (12) <br> `      NUG(:) = 0` (13) <br> `      DO I = 1, NSHL` (15) <br> `        IF( IP(I) /= IPART ) CYCLE` (17) <br> `        ND = IELM(3,I)` (19) <br> `        IF( ND == 9 ) ND = 8` (20) <br> `        SELECT CASE( ND )` (22) <br> `        CASE( 3 )` (23) <br> `          ITYP = 1` (24) <br> `        CASE( 4 )` (25) <br> `          ITYP = 2` (26) <br> `        CASE( 6 )` (27) <br> `          ITYP = 3` (28) <br> `        CASE( 8 )` (29) <br> `          ITYP = 4` (30) <br> `        END SELECT` (31) <br> `        NE(ITYP) = NE(ITYP) + 1` (33) <br> `        IE( NE(ITYP), ITYP ) = I` (34) <br> `        NUG( IELM(8:7+ND,I) ) = 1` (35) <br> `      ENDDO` (37) <br> `      NG = 0` (39) <br> `      IG(:) = 0` (40) <br> `      DO I = 1, NNOD` (42) <br> `        IF( NUG(I) == 1 ) THEN` (43) <br> `          NG = NG + 1` (44) <br> `          IG(NG) = I` (45) <br> `          LG(I) = NG` (46) <br> `        ENDIF` (47) <br> `      ENDDO` (48) |
| 50–98 | 시작 시 SHELL_GEOM(1) 안이며 앞 루프 밖이다. 부분 번호·이름·외부 절점 번호·좌표를 출력한다(50–68). 네 유형을 순회하되 NE=0은 건너뛴다(70–72). 각 유형 이름·요소 수·외부 요소 번호를 출력한다(74–81). 연결(connectivity) 출력에서도 ND=9를 8로 바꾸고 LG로 변환한 절점 목록을 쓴다(83–94). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      WRITE(IFG,'(A4)') 'part'` (50) <br> `      WRITE(IFG,'(I10)') IPART` (52) <br> `      WRITE(IFG,'(A,X,I0)') 'shell elements', JPART` (54) <br> `      WRITE(IFG,'(A)') 'coordinates'` (56) <br> `      WRITE(IFG,'(I10)') NG` (58) <br> `      DO I = 1, NG` (60) <br> `        WRITE(IFG,'(I10)') INDG(IG(I))` (61) <br> `      ENDDO` (62) <br> `      DO J = 1, 3` (64) <br> `        DO I = 1, NG` (65) <br> `          WRITE(IFG,'(1PE12.5)') GRID(J,IG(I))` (66) <br> `        ENDDO` (67) <br> `      ENDDO` (68) <br> `      DO ITYP = 1, 4` (70) <br> `        IF( NE(ITYP) == 0 ) CYCLE` (72) <br> `        WRITE(IFG,'(A)') ETYPE(ITYP)` (74) <br> `        WRITE(IFG,'(I10)') NE(ITYP)` (76) <br> `        DO I = 1, NE(ITYP)` (78) <br> `          IENO = IE(I,ITYP)` (79) <br> `          WRITE(IFG,'(I10)') IELM(1,IENO)` (80) <br> `        ENDDO` (81) <br> `        DO I = 1, NE(ITYP)` (83) <br> `          IENO = IE(I,ITYP)` (85) <br> `          ND = IELM(3,IENO)` (87) <br> `          IF( ND == 9 ) ND = 8` (88) <br> `          KN(1:ND) = IELM(8:7+ND,IENO)` (90) <br> `          WRITE(IFG,'(20I10)') LG( KN(1:ND) )` (92) <br> `        ENDDO` (94) <br> `      ENDDO` (96) <br> `      END` (98) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20·88–92: 9절점 셸은 출력에 8개 절점만 포함하며 9번째 절점을 연결 목록에 쓰지 않는다.
- 22–31: 열거된 ND 이외에 ITYP를 설정하는 CASE DEFAULT는 없다.
