---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/errmsg.f90
lines: 26
sha256: d73fdf2ba882dffc8f2cebb39b5eef7cae4411acc3a9e7ed06804eb27afbe1e2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# errmsg.f90 — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 오류 메시지의 정형 부분을 출력한다는 주석(3). ierr>0은 계산 계속 경고(4), ierr<0은 계산 정지 오류라는 설명(5). nstep을 가져오고 `implicit none`(8) 및 입력 인수를 선언한다. 원문: `subroutine errmsg(rout,ierr)` (1); `!----------------------------------------` (2); `!エラーメッセージの定型部分を出力する` (3); `!  ierr>0: 計算を継続(Warning)` (4); `!  ierr<0: 計算を停止(Error)` (5); `!----------------------------------------` (6); `  use m_timectl,only: nstep` (7); `  implicit none` (8); `!` (9); `![arguments]` (10); `  character(*),intent(in):: rout` (11); `  integer,intent(in):: ierr` (12); `!` (13); `!` (14) |
| 15–26 | 시작 시 1행 루틴 안. ierr>0이면 Warning, 그 외에는 Error 문자열과 루틴명·오류 코드·스텝을 출력한다. 반환 외에 정지 루틴 호출은 없다. 원문: `  if(ierr>0) then` (15); `     write(*,*) 'Warning at subroutine ',trim(rout)` (16); `     write(*,*) '           error code=',ierr` (17); `     write(*,*) '                 step=',nstep` (18); `  else` (19); `     write(*,*) 'Error   at subroutine ',trim(rout)` (20); `     write(*,*) '           error code=',ierr` (21); `     write(*,*) '                 step=',nstep` (22); `  endif` (23); `!` (24); `  return` (25); `end subroutine errmsg` (26) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–23: ierr=0도 else의 Error 출력으로 들어간다. 이 루틴 자체에는 계산 정지 호출이 없다.
