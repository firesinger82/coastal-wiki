---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/allocate_cadmas.f90
lines: 29
sha256: e4d03153e7df0cef75d6400c181d24f7fbffa9c954d88ddd9168a53e20fba981
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# allocate_cadmas.f90 — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `allocate_cadmas` 진입부. 재격자화(remesh)한 CADMAS 데이터를 담는 배열의 메모리 할당이라는 주석(3). 모듈과 인수, 지역 변수 및 `implicit none`(7)을 선언하고 ierr를 0으로 설정한다. 원문: `subroutine allocate_cadmas(ierr)` (1); `!----------------------------------------` (2); `! remeshしたCADMASデータを格納する配列へのメモリ割り当て` (3); `!----------------------------------------` (4); `  use m_potential,only: ipmax,jpmax` (5); `  use m_cadmas,only: height,depth,uu,vv,max_depth` (6); `  implicit none` (7); `!` (8); `!  [arguments]` (9); `  integer,intent(out):: ierr` (10); `!` (11); `!  [local variables]` (12); `  integer::ierror` (13); `  character(32):: rout='allocate_cadmas'` (14); `!` (15); `  ierr=0` (16); `!` (17) |
| 18–29 | 시작 시 1행 루틴 안. height·depth·uu·vv·max_depth를 `(ipmax,jpmax)`로 할당한다(18–20). max_depth는 -9999로 초기화한다(21). ierror가 0이 아니면 ierr=-10, errmsg 호출 및 오류 출력 뒤 반환한다(22–29). 원문: `  allocate(height(ipmax,jpmax),depth(ipmax,jpmax) &` (18); `        & ,uu(ipmax,jpmax),vv(ipmax,jpmax)        &` (19); `        & ,max_depth(ipmax,jpmax),stat=ierror)` (20); `  max_depth(:,:)=-9999` (21); `  if(ierror/=0) then` (22); `     ierr=-10` (23); `     call errmsg(rout,ierr)` (24); `     write(*,*) 'cannot allocate cadmas data arrays'` (25); `  endif` (26); `!` (27); `  return` (28); `end subroutine allocate_cadmas` (29) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–22: max_depth 전체 대입은 할당의 ierror 검사보다 먼저 실행된다.
