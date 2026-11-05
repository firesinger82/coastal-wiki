---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/mean2.f
lines: 14
sha256: c3d4956b155aba74e4c7f17e9600cfa758dcb25cdc7a32ab19a5c6cb1aea25eb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mean2.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | MEAN2의 인수와 암시적 형(implicit typing), A(*)·INDX(N)을 선언한다(1–4). RMEAN을 0으로 두고 I=1..N에서 A(INDX(I))를 더한 뒤 N으로 나누어 산술평균(arithmetic mean)을 구한다(6–11). 주석·RETURN·END를 포함한다. 원문: `      SUBROUTINE MEAN2(RMEAN,A,INDX,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION A(*),INDX(N)` (4); `      RMEAN=0.` (6); `      DO I=1,N` (8); `        RMEAN = RMEAN + A(INDX(I))` (9); `      ENDDO` (10); `      RMEAN=RMEAN/N` (11); `      RETURN` (13); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–11: N으로 나누기 전에 N이 0인지 검사하는 문장은 없다.
