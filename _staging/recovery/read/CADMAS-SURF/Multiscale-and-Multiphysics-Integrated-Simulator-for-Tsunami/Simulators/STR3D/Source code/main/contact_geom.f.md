---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/contact_geom.f
lines: 65
sha256: b9ba07b2c41dffacf3f48ee06e9ef1301f5002d4ec147071e92c467fe1c7b561
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# contact_geom.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | CONTACT_GEOM은 JPART=1이면 IS=1, 그 외에는 앞 ICBD 끝+1을 시작 위치로 사용한다(8–12). IE는 현재 ICBD 끝이다(14). IS:IE의 삼각 접촉 요소 절점을 표시하고 부분 절점 목록 IG·LG를 만든다(18–31). 부분 번호·이름·절점 번호·좌표를 출력한다(33–51). tria3 요소 수 IE-IS+1과 요소 번호·LG 연결을 출력한다(53–63). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE CONTACT_GEOM( NG, IG, IPART, JPART, INDG, GRID, ICBD,` (1) <br> `     &                         IELC, NNOD, NUG, LG, IFG )` (2) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (4) <br> `      DIMENSION NUG(NNOD), IG(NNOD), LG(NNOD), INDG(NNOD), GRID(3,NNOD),` (5) <br> `     &          ICBD(*), IELC(3,*)` (6) <br> `      IF( JPART == 1 ) THEN` (8) <br> `        IS = 1` (9) <br> `      ELSE` (10) <br> `        IS = ICBD(JPART-1) + 1` (11) <br> `      ENDIF` (12) <br> `      IE = ICBD(JPART)` (14) <br> `      NUG(:) = 0` (16) <br> `      DO I = IS, IE` (18) <br> `        NUG( IELC(:,I) ) = 1` (19) <br> `      ENDDO` (20) <br> `      NG = 0` (22) <br> `      IG(:) = 0` (23) <br> `      DO I = 1, NNOD` (25) <br> `        IF( NUG(I) == 1 ) THEN` (26) <br> `          NG = NG + 1` (27) <br> `          IG(NG) = I` (28) <br> `          LG(I) = NG` (29) <br> `        ENDIF` (30) <br> `      ENDDO` (31) <br> `      WRITE(IFG,'(A4)') 'part'` (33) <br> `      WRITE(IFG,'(I10)') IPART` (35) <br> `      WRITE(IFG,'(A,X,I0)') 'contact elements', JPART` (37) <br> `      WRITE(IFG,'(A)') 'coordinates'` (39) <br> `      WRITE(IFG,'(I10)') NG` (41) <br> `      DO I = 1, NG` (43) <br> `        WRITE(IFG,'(I10)') INDG(IG(I))` (44) <br> `      ENDDO` (45) <br> `      DO J = 1, 3` (47) <br> `        DO I = 1, NG` (48) <br> `          WRITE(IFG,'(1PE12.5)') GRID(J,IG(I))` (49) <br> `        ENDDO` (50) <br> `      ENDDO` (51) <br> `      WRITE(IFG,'(A)') 'tria3   '` (53) <br> `      WRITE(IFG,'(I10)') IE - IS + 1` (55) <br> `      DO I = IS, IE` (57) <br> `        WRITE(IFG,'(I10)') I` (58) <br> `      ENDDO` (59) <br> `      DO I = IS, IE` (61) <br> `        WRITE(IFG,'(3I10)') LG( IELC(:,I) )` (62) <br> `      ENDDO` (63) <br> `      END` (65) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
