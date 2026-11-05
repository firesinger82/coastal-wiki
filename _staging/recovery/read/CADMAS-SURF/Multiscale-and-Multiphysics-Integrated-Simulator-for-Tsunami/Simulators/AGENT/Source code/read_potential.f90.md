---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/read_potential.f90
lines: 39
sha256: b0d56940be7ff81337367286fb32071f8f193c24383bf59770e957b916fef3d2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# read_potential.f90 — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 포텐셜 관련 입력 파일 읽기 주석(3). `implicit none`(7), 인수와 rout를 선언하고 ierr를 초기화한다. 원문: `subroutine read_potential(ierr)` (1); `!----------------------------------------` (2); `! ポテンシャル関連入力ファイルの読み込み` (3); `!----------------------------------------` (4); `  use m_potential,only: n_signpost,n_shelter` (5); `!` (6); `  implicit none` (7); `!` (8); `![arguments]` (9); `  integer,intent(out):: ierr` (10); `!` (11); `![local variables]` (12); `  character(32):: rout='read_potential'` (13); `!` (14); `  ierr=0` (15); `!` (16); `!` (17) |
| 18–39 | 시작 시 1행 루틴 안. 진입 가능 여부 지정 입력 데이터 읽기이며 디버그용인지 묻는 주석(18). read_move_boundary는 항상 호출한다. 이정표 데이터 읽기(23)는 n_signpost>0, 피난소 데이터 읽기(30)는 n_shelter>0일 때 각각 호출한다. 각 음수 오류는 errstop으로 보낸다. 원문: `!進入可否を指定する入力データ読み込み(Debug用?)` (18); `  write(100,'(a)')"debug: call read_move_boundary"` (19); `  call read_move_boundary(ierr)` (20); `   if(ierr<0) call errstop(rout,ierr)` (21); `!` (22); `!道標データの読み込み` (23); `   write(100,'(a)')"debug: call read_signpost"` (24); `  if(n_signpost>0)then` (25); `     call read_signpost(ierr)` (26); `      if(ierr<0) call errstop(rout,ierr)` (27); `  endif` (28); `!` (29); `!避難所データの読み込み` (30); `  write(100,'(a)')"debug: call read_shelter"` (31); `  if(n_shelter>0)then` (32); `     call read_shelter(ierr)` (33); `      if(ierr<0) call errstop(rout,ierr)` (34); `  endif` (35); `!` (36); `  return` (37); `!` (38); `end subroutine read_potential` (39) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
