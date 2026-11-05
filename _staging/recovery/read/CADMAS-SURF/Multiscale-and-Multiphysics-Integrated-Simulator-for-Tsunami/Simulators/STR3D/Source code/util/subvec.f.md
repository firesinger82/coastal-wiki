---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/subvec.f
lines: 14
sha256: 053eb14fbf4ab2df8def79331ac167bafbdf99ca1633320955c4baee8f5fdf79
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# subvec.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SUBVEC는 실수 벡터(vector) 뺄셈의 목적과 RVEC(I)=RA(I)-RB(I)를 주석으로 설명한다(1–5). 암시적 형(implicit typing)과 NSIZE 크기의 세 배열을 선언한다(6–7). I=1..NSIZE에서 두 입력 성분의 차를 출력에 대입한다(9–11). 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE SUBVEC(RVEC,RA,RB,NSIZE)` (1); `C                          SUBSTITUTE VECTOR     (REAL)` (3); `C                                 RVEC(I)=RA(I)-RB(I)` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION RVEC(NSIZE),RA(NSIZE),RB(NSIZE)` (7); `      DO 1000 I=1,NSIZE` (9); `      RVEC(I)=RA(I)-RB(I)` (10); ` 1000 CONTINUE` (11); `      RETURN` (13); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
