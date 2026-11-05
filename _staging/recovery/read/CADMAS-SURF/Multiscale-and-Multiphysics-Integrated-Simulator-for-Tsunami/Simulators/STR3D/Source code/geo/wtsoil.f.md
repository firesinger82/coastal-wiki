---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/wtsoil.f
lines: 23
sha256: f9c4387716a962108d548de82d8aa6f206fdfae1e7691685ea3ab4b65b611d72
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wtsoil.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | WTSOIL은 실수 IMPLICIT·VELG(3,NNOD)·NG_ENS(*)·IG_ENS(NNOD,*)를 선언한다. pore water flux 제목을 출력한다. IP=IPS,IPE의 부품(part)마다 번호와 coordinates 표제를 쓴다. J=1,3 성분별로 I=1,NG_ENS(IP) 절점을 순회하며 IG_ENS의 절점 번호에 해당하는 VELG(J,IG)를 출력한다. 원문: `      SUBROUTINE WTSOIL( VELG, NNOD, IPS, IPE, NG_ENS, IG_ENS, IFL )` (1); `C` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION VELG(3,NNOD), NG_ENS(*), IG_ENS(NNOD,*)` (4); `C` (5); `      WRITE(IFL,'(A)') 'pore water flux'` (6); `C` (7); `      DO IP = IPS, IPE` (8); `C` (9); `        WRITE(IFL,'(A)') 'part'` (10); `        WRITE(IFL,'(I10)') IP` (11); `        WRITE(IFL,'(A)') 'coordinates'` (12); `C` (13); `        DO J = 1, 3` (14); `          DO I = 1, NG_ENS(IP)` (15); `            IG = IG_ENS(I,IP)` (16); `            WRITE(IFL,'(1PE12.4)') VELG(J,IG)` (17); `          ENDDO` (18); `        ENDDO` (19); `C` (20); `      ENDDO` (21); `C` (22); `      END` (23) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·17: 표제는 coordinates이며 이 표제 뒤에 쓰는 배열 값은 VELG(J,IG)이다.
