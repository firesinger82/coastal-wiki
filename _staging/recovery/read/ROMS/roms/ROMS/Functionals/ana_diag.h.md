---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_diag.h
lines: 160
sha256: 563474358712d62b73358825c092ee433d80cf1e89e488994c54ea96a34f7105
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_diag.h — 판독 구간 기록

구간은 1행부터 160행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | ana_diag 시작(2), 저작권·라이선스와 사용자 진단(user diagnostics)을 매 3차원 방정식 시간 단계(time step) 끝에 호출한다는 주석(4–16). 모듈·인수·MyFile 선언(17–28). `#include "tile.h"` (30)로 tile.h를 끼워 넣는다. ana_diag_tile 호출의 `#ifdef SOLVE3D` (35)에서 OCEAN(ng)%u·v를 전달(36–37), `#endif` (38) 뒤 ubar·vbar 전달(39–40). `#ifdef DISTRIBUTE` (44)의 `IF (Lanafile) THEN` (45), `#else` (46)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (47), `#endif` (48) 뒤 ANANAME(5)=MyFile(49). 조건 종료·RETURN·루틴 종료·주석(50–54). |
| 55–77 | ana_diag_tile 시작(56–62). 인수 목록의 `#ifdef SOLVE3D` (59)는 u·v를 포함(60), `#endif` (61) 뒤 ubar·vbar(62). 공통 모듈(65–67), `#ifdef SEAMOUNT` (68)에서 mod_stepping 사용(69), `#endif` (70). ng·tile·model·경계 인수 선언(74–76), 주석(77). |
| 78–103 | 시작 시 56행 ana_diag_tile 안. `#ifdef ASSUMED_SHAPE` (78), 그 안 `# ifdef SOLVE3D` (79)에서 u·v assumed-shape 입력 배열(80–81), `# endif` (82), ubar·vbar 입력 배열(83–84). `#else` (85), 그 안 `# ifdef SOLVE3D` (86)에서 u·v를 (LBi:UBi,LBj:UBj,N(ng),2)로 선언(87–88), `# endif` (89). ubar·vbar 선언은 `real(r8), intent(in) :: ubar(LBi:UBi,LBj:UBj,:)` (90); `real(r8), intent(in) :: vbar(LBi:UBi,LBj:UBj,:)` (91), `#endif` (92). i·io_err·j·k·최대 속도·io_errmsg 선언(96–100). `#include "set_bounds.h"` (102)로 set_bounds.h를 끼워 넣는다. |
| 104–123 | 시작 시 56행 ana_diag_tile 안. 진단 계산 주석(104–107), `#ifdef SEAMOUNT` (108). `IF (iic(ng).eq.ntstart(ng)) THEN` (112)이면 usrout을 USRname 파일로 formatted·status='unknown'·IOSTAT·IOMSG 인수와 함께 OPEN(113–114). `IF (io_err.ne.0) THEN` (115)이면 파일명·오류 메시지를 출력하고 exit_flag=5·RETURN(116–118). 오류 FORMAT과 조건 종료·주석(119–123). |
| 124–152 | 시작 시 56행 ana_diag_tile·108행 `#ifdef SEAMOUNT` 안. 최대 속도 계산 주석(124–125). `umax=0.0_r8` (126); `vmax=0.0_r8` (127); `ubarmax=0.0_r8` (128); `vbarmax=0.0_r8` (129). k=1..N(ng) 루프(130)의 j=0..Mm+1·i=1..Lm+1 루프(131–132)에서 `umax=MAX(umax,u(i,j,k,nnew(ng)))` (133). 같은 k 루프의 j=1..Mm+1·i=0..Lm+1 루프(136–137)에서 `vmax=MAX(vmax,v(i,j,k,nnew(ng)))` (138). k 루프 종료(141). j=0..Mm+1·i=1..Lm+1 루프(142–143)에서 `ubarmax=MAX(ubarmax,ubar(i,j,knew(ng)))` (144). j=1..Mm+1·i=0..Lm+1 루프(147–148)에서 `vbarmax=MAX(vbarmax,vbar(i,j,knew(ng)))` (149). 루프 종료·주석 포함(134–135·139–140·145–146·150–152). |
| 153–160 | 시작 시 56행 ana_diag_tile·108행 `#ifdef SEAMOUNT` 안. usrout에 tdays·ubarmax·vbarmax·umax·vmax를 출력(155), FORMAT(156), `#endif` (157). 주석·RETURN·루틴 종료(158–160). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 126–149: 최대값 누적은 0에서 시작하며 ABS를 사용하지 않는다. 음수 속도만 들어오는 경우 해당 누적값은 0이다.
- 130–151: 속도 검색 루프는 Istr·Iend·Jstr·Jend 대신 Lm·Mm의 전체 영역 인덱스를 사용한다. 이 블록에는 타일 번호 검사나 프로세스 간 최댓값 교환 호출이 없다.
- 108–155: SEAMOUNT 계산 블록은 u·v를 참조한다. u·v 인수와 선언은 별도 SOLVE3D 전처리 조건으로 감싼다(35–38·59–61·79–89).
- 112–122·155: 사용자 파일 OPEN과 WRITE에는 Master 또는 tile 번호 조건이 없다.
