---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/random_normal.f90
lines: 35
sha256: 37a1194aa755646c769c0f5294405f68a39ee3a4b2b4f3cd124ffb447188cb34
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# random_normal.f90 — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 평균 0·표준편차 sigma의 정규 난수 생성 주석(3). `implicit none`(5), 입출력·save iflag=0·save r1/r2와 pi2 상수를 선언한다. 원문: `subroutine random_normal(sigma,rand_norm,ierr)` (1); `!----------------------------------------` (2); `! 正規乱数を生成する（平均値0，標準偏差sigma）` (3); `!----------------------------------------` (4); `    implicit none` (5); `!` (6); `![arguments]` (7); `  real(8),intent(in)::  sigma` (8); `  real(8),intent(out):: rand_norm` (9); `  integer,intent(out):: ierr` (10); `!` (11); `![local variables]` (12); `  integer,save:: iflag=0` (13); `  real(8),save:: r1,r2` (14); `  real(8),parameter:: pi2=6.28318530718d0` (15); `!` (16); `  ierr=0` (17); `!` (18); `!` (19) |
| 20–35 | 시작 시 1행 루틴 안. 박스 뮐러 변환(Box-Muller transform) 주석(20). iflag==0이면 균등 난수 두 개를 받아 sin 성분을 반환하고 다음 호출에서는 저장된 난수의 cos 성분을 사용한다. 결과에 sigma를 곱한다. 원문: `!Box-Muller transform` (20); `  if(iflag==0)then` (21); `    call random_number(r1)` (22); `    call random_number(r2)` (23); `    rand_norm=sqrt(-2.0d0*log(r1))*sin(pi2*r2)` (24); `    iflag=1` (25); `  else` (26); `    rand_norm=sqrt(-2.0d0*log(r1))*cos(pi2*r2)` (27); `    iflag=0` (28); `  endif` (29); `!` (30); `  rand_norm=rand_norm*sigma` (31); `!` (32); `!` (33); `  return` (34); `end subroutine random_normal` (35) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–24·27: r1을 log의 인수로 사용하기 전에 r1=0 여부를 검사하는 문장은 이 루틴에 없다.
