---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/rod_geom.f
lines: 65
sha256: 05a7d4570eac551d24e8ae85a3e04017a7af3ac05f63a8305f452895127738bd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rod_geom.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | ROD_GEOM은 IP(I)=IPART인 봉(rod) 요소만 선택해 IE와 두 절점의 NUG를 구성한다(12–17). 전 절점을 순회하여 부분 절점 IG와 역표 LG를 만든다(22–28). 부분 번호·rod elements 이름·외부 절점 번호·좌표를 출력한다(30–48). EnSight 요소 이름은 bar2이며 요소 수·외부 요소 번호·LG로 변환한 연결(connectivity)을 출력한다(50–63). 배열 크기·암시적 배정밀도·주석·루틴 끝을 포함한다. 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ROD_GEOM( NG, IG, NE, IE, IP, IPART, JPART, INDG, GRID,` (1) <br> `     &                     IELM, NM, NNOD, NROD, NUG, LG, IFG )` (2) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (4) <br> `      DIMENSION NUG(NNOD), IELM(NM,NROD), IE(NROD), IG(NNOD), LG(NNOD),` (5) <br> `     &          INDG(NNOD), GRID(3,NNOD), KN(2), IP(NROD)` (6) <br> `      NE = 0` (8) <br> `      IE(:) = 0` (9) <br> `      NUG(:) = 0` (10) <br> `      DO I = 1, NROD` (12) <br> `        IF( IP(I) /= IPART) CYCLE` (13) <br> `        NE = NE + 1` (14) <br> `        IE(NE) = I` (15) <br> `        NUG( IELM(8:9,I) ) = 1` (16) <br> `      ENDDO` (17) <br> `      NG = 0` (19) <br> `      IG(:) = 0` (20) <br> `      DO I = 1, NNOD` (22) <br> `        IF( NUG(I) == 1 ) THEN` (23) <br> `          NG = NG + 1` (24) <br> `          IG(NG) = I` (25) <br> `          LG(I) = NG` (26) <br> `        ENDIF` (27) <br> `      ENDDO` (28) <br> `      WRITE(IFG,'(A4)') 'part'` (30) <br> `      WRITE(IFG,'(I10)') IPART` (32) <br> `      WRITE(IFG,'(A,X,I0)') 'rod elements', JPART` (34) <br> `      WRITE(IFG,'(A)') 'coordinates'` (36) <br> `      WRITE(IFG,'(I10)') NG` (38) <br> `      DO I = 1, NG` (40) <br> `        WRITE(IFG,'(I10)') INDG(IG(I))` (41) <br> `      ENDDO` (42) <br> `      DO J = 1, 3` (44) <br> `        DO I = 1, NG` (45) <br> `          WRITE(IFG,'(1PE12.5)') GRID(J,IG(I))` (46) <br> `        ENDDO` (47) <br> `      ENDDO` (48) <br> `      WRITE(IFG,'(A)') 'bar2'` (50) <br> `      WRITE(IFG,'(I10)') NE` (52) <br> `      DO I = 1, NE` (54) <br> `        IENO = IE(I)` (55) <br> `        WRITE(IFG,'(I10)') IELM(1,IENO)` (56) <br> `      ENDDO` (57) <br> `      DO I = 1, NE` (59) <br> `        IENO = IE(I)` (60) <br> `        KN(1:2) = IELM(8:9,IENO)` (61) <br> `        WRITE(IFG,'(2I10)') LG( KN(1:2) )` (62) <br> `      ENDDO` (63) <br> `      END` (65) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
