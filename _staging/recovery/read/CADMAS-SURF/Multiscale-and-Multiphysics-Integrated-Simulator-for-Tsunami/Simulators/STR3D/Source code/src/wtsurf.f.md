---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/wtsurf.f
lines: 31
sha256: 844ff1ec8228755d8dec6d2b82b8c3c288e718eefeb1736564375e7bc76dd5fa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wtsurf.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | WTSURF 입구와 IMPLICIT·CHARACTER·배열·DATA 선언이다(1–7). 유효 표면적(effective surface area) 헤더를 쓴다(9). IP=1:NMAT의 각 파트에서 ITYP=1:4를 순회한다(11–16). 출력 파트 번호는 N_PART+IP이다(14). 해석: NMAT를 재료 수로 보는 설명은 변수 이름에 따른 해석이다. 요소 수 0은 건너뛰고 ETYPE과 해당 AFC를 출력한다(18–29). 원문: `      SUBROUTINE WTSURF( AFC, NMAT, NPFC, N_PART, NE_ENSW, IE_ENSW, IFL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      CHARACTER*8 ETYPE(4)` (4); `      DIMENSION NE_ENSW(4,NMAT), IE_ENSW(NPFC,4,NMAT), AFC(NPFC)` (5); `      DATA ETYPE / 'tria3   ', 'quad4   ', 'tria6   ', 'quad8   ' /` (7); `      WRITE(IFL,'(A)') 'effective surface area'` (9); `      DO IP = 1, NMAT` (11); `        WRITE(IFL,'(A)') 'part'` (13); `        WRITE(IFL,'(I10)') N_PART + IP` (14); `        DO ITYP = 1, 4` (16); `          IF( NE_ENSW(ITYP,IP) == 0 ) CYCLE` (18); `          WRITE(IFL,'(A)') ETYPE(ITYP)` (20); `          DO I = 1, NE_ENSW(ITYP,IP)` (22); `            IENO = IE_ENSW(I,ITYP,IP)` (23); `            WRITE(IFL,'(1PE12.5)') AFC( IENO )` (24); `          ENDDO` (25); `        ENDDO` (27); `      ENDDO` (29); `      END` (31) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
