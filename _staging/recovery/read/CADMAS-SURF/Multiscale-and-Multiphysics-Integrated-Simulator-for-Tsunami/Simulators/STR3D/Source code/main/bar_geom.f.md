---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/bar_geom.f
lines: 65
sha256: 1a6d1ab4fa9f324b2b41967146f0c9c903188a5797c6b5470eb053ec30a756c7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bar_geom.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | BAR_GEOM은 IP(I)=IPART인 보(bar) 요소를 선택하고 해당 두 절점의 NUG를 표시한다(12–17). NNOD를 순회해 IG·LG의 전역·부분 절점 대응을 만든다(22–28). 부분(part) 번호와 이름을 먼저 출력한다. 이어 절점 수와 외부 절점 번호를 출력한다. 마지막으로 좌표 성분별 값을 출력한다(30–48). bar2 요소 종류와 요소 수·외부 요소 번호·LG로 변환한 2절점 연결(connectivity)을 출력한다(50–63). 배열 범위와 암시적 배정밀도 선언도 보존한다(4–6). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE BAR_GEOM( NG, IG, NE, IE, IP, IPART, JPART, INDG, GRID,` (1) <br> `     &                     IELM, NM, NNOD, NBAR, NUG, LG, IFG )` (2) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (4) <br> `      DIMENSION NUG(NNOD), IELM(NM,NBAR), IE(NBAR), IG(NNOD), LG(NNOD),` (5) <br> `     &          INDG(NNOD), GRID(3,NNOD), KN(2), IP(NBAR)` (6) <br> `      NE = 0` (8) <br> `      IE(:) = 0` (9) <br> `      NUG(:) = 0` (10) <br> `      DO I = 1, NBAR` (12) <br> `        IF( IP(I) /= IPART) CYCLE` (13) <br> `        NE = NE + 1` (14) <br> `        IE(NE) = I` (15) <br> `        NUG( IELM(8:9,I) ) = 1` (16) <br> `      ENDDO` (17) <br> `      NG = 0` (19) <br> `      IG(:) = 0` (20) <br> `      DO I = 1, NNOD` (22) <br> `        IF( NUG(I) == 1 ) THEN` (23) <br> `          NG = NG + 1` (24) <br> `          IG(NG) = I` (25) <br> `          LG(I) = NG` (26) <br> `        ENDIF` (27) <br> `      ENDDO` (28) <br> `      WRITE(IFG,'(A4)') 'part'` (30) <br> `      WRITE(IFG,'(I10)') IPART` (32) <br> `      WRITE(IFG,'(A,X,I0)') 'bar elements', JPART` (34) <br> `      WRITE(IFG,'(A)') 'coordinates'` (36) <br> `      WRITE(IFG,'(I10)') NG` (38) <br> `      DO I = 1, NG` (40) <br> `        WRITE(IFG,'(I10)') INDG(IG(I))` (41) <br> `      ENDDO` (42) <br> `      DO J = 1, 3` (44) <br> `        DO I = 1, NG` (45) <br> `          WRITE(IFG,'(1PE12.5)') GRID(J,IG(I))` (46) <br> `        ENDDO` (47) <br> `      ENDDO` (48) <br> `      WRITE(IFG,'(A)') 'bar2'` (50) <br> `      WRITE(IFG,'(I10)') NE` (52) <br> `      DO I = 1, NE` (54) <br> `        IENO = IE(I)` (55) <br> `        WRITE(IFG,'(I10)') IELM(1,IENO)` (56) <br> `      ENDDO` (57) <br> `      DO I = 1, NE` (59) <br> `        IENO = IE(I)` (60) <br> `        KN(1:2) = IELM(8:9,IENO)` (61) <br> `        WRITE(IFG,'(2I10)') LG( KN(1:2) )` (62) <br> `      ENDDO` (63) <br> `      END` (65) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
