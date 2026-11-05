---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/open_file.f90
lines: 45
sha256: 11f4842a3def363c472181f3578ce401a35b7a3116e35c0abd1fb42eee413ae4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# open_file.f90 — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 로그 파일 제어 주석(3). 인수·rout를 선언하고 ierr를 0으로 둔다. 이 파일에는 implicit none 문이 없다. 원문: `subroutine open_file(iflag,ierr)` (1); `!----------------------------------------` (2); `! LOGファイル制御` (3); `!----------------------------------------` (4); `!` (5); `![arguments]` (6); `  integer,intent(in):: iflag` (7); `  integer,intent(out):: ierr` (8); `!` (9); `![local variables]` (10); `  character(32):: rout='open_file'` (11); `!` (12); `  ierr=0` (13); `!` (14); `!` (15) |
| 16–35 | 시작 시 1행 루틴 안. 열기 주석(17)의 iflag==0은 debug.txt를 장치 100으로 replace·formatted 방식으로 연다. 닫기 주석(25)의 iflag==1은 장치 100을 닫는다. 장치 90의 open·close 및 로그 출력은 주석 처리되었다. `if( iflag==0 )then`(19)과 `elseif( iflag==1 )then`(27)의 사슬에는 ELSE가 없다. 다른 iflag 값에서는 파일 조작 없이 34행에서 반환한다. 원문: `!----------------------------------------` (16); `!  (0) オープン` (17); `!----------------------------------------` (18); `  if( iflag==0 )then` (19); `    !open(90,file='log_ma',status='replace',form='formatted',err=91)` (20); `    open(100,file="debug.txt",status='replace',form='formatted',err=91)` (21); `!!!!    write(*,*) 'open file: log_ma'` (22); `!` (23); `!----------------------------------------` (24); `! (2) クローズ` (25); `!----------------------------------------` (26); `  elseif( iflag==1 )then` (27); `    !close(90)` (28); `    close(100)` (29); `!!!!    write(*,*) 'close file: log_ma'` (30); `!` (31); `  endif` (32); `!` (33); `  return` (34); `!` (35) [11-04 전수 검증 보완] |
| 36–45 | 시작 시 1행 루틴 안. 오류 처리 주석(37). open의 err=91은 ierr=-10과 errmsg·오류 문구 출력 후 반환한다. 원문: `!----------------------------------------` (36); `! エラー処理` (37); `!----------------------------------------` (38); `91 continue` (39); `  ierr=-10` (40); `  call errmsg(rout,ierr)` (41); `  write(*,*) 'cannot open log file'` (42); `  return` (43); `end subroutine open_file` (45) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
