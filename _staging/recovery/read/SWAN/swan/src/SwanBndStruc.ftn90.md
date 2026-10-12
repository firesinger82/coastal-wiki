---
file: models/SWAN/raw/source_code/swan/src/SwanBndStruc.ftn90
lines: 223
sha256: f4d53da9f92842032d89fe1f99fb3e92aa06739793d9f7a35f3a66c5884576f7
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanBndStruc.ftn90 — 판독 구간 기록

구간은 1행부터 223행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–57 | SwanBndStruc 선언과 기관·작성자·GPL 머리말을 포함한다(1–29). 2010년 도입 이력과 정형 격자(structured grid)의 BOUNDARY·BOUND_01..BOUND_04 출력 곡선(output curve) 생성 목적을 주석에 적는다(30–41). 원점에서 반시계 방향으로 이동하는 방법 주석과 공통·출력 모듈 사용을 포함한다(43–56). |
| 58–92 | 시작 시 1행 SwanBndStruc 루틴 안. 입력 좌표 xcgrid·ycgrid는 (MXC,MYC) 크기이다(58–61). 경계점 수·면 번호·이동 증분·지역 좌표 배열·이름·OPSDAT 포인터를 선언한다(63–85). iside 주석 범위는 1..4이다(67). IENT의 SAVE 선언 기본값은 0이다(74). 구조와 원문 안내 주석을 포함한다(87–92). 원문: `integer, save                        :: ient = 0 ! number of entries in this subroutine` (74); `character(len=8)                     :: psname   ! name assigned to output curve` (83). |
| 93–98 | 시작 시 1행 SwanBndStruc 루틴 안. LTRACE이면 STRACE를 호출한다(93). 미할당 xbnd·ybnd의 크기는 2*(mxc+myc-2)이다(95–96). ibnd=0으로 시작해 네 면을 순회한다(97–98). 원문: `if (ltrace) call strace (ient,'SwanBndStruc')` (93); `if (.not.allocated(xbnd)) allocate (xbnd(1:2*(mxc+myc-2)))` (95); `if (.not.allocated(ybnd)) allocate (ybnd(1:2*(mxc+myc-2)))` (96); `ibnd = 0` (97); `do iside = 1, 4` (98). |
| 99–132 | 시작 시 1행 SwanBndStruc 루틴·98행 iside 루프 안. 면 번호에 따라 시작 인덱스·끝 인덱스·증분·면의 점 수를 설정한다(99–131). 첫 면은 iy=1에서 ix를 1부터 mxc까지 증가시키도록 설정한다(99–106). 둘째 면은 ix=mxc에서 iy를 1부터 myc까지 증가시키도록 설정한다(107–114). 셋째 면은 iy=myc에서 ix를 mxc부터 1까지 감소시키도록 설정한다(115–122). 넷째 면은 ix=1에서 iy를 myc부터 1까지 감소시키도록 설정한다(123–130). 원문: `if (iside==1) then` (99); `ix0 = 1` (100); `ix1 = mxc` (101); `xstep = 1` (102); `iy0 = 1` (103); `iy1 = 1` (104); `ystep = 0` (105); `lside = mxc` (106); `elseif (iside==2) then` (107); `ix0 = mxc` (108); `ix1 = mxc` (109); `xstep = 0` (110); `iy0 = 1` (111); `iy1 = myc` (112); `ystep = 1` (113); `lside = myc` (114); `elseif (iside==3) then` (115); `ix0 = mxc` (116); `ix1 = 1` (117); `xstep = -1` (118); `iy0 = myc` (119); `iy1 = myc` (120); `ystep = 0` (121); `lside = mxc` (122); `elseif (iside==4) then` (123); `ix0 = 1` (124); `ix1 = 1` (125); `xstep = 0` (126); `iy0 = myc` (127); `iy1 = 1` (128); `ystep = -1` (129); `lside = myc` (130). [10-13 전수 검증 정정] 이 IF/ELSEIF 사슬에는 ELSE가 없다. 이 사슬은 `endif` (131)로 닫힌다. [10-13 전수 검증 보완] |
| 133–163 | 시작 시 1행 SwanBndStruc 루틴·98행 iside 루프 안. 면별 좌표 배열이 미할당이면 lside 크기로 할당한다(133–134). 시작 인덱스를 복사하고 ispt=0으로 설정한다(135–137). 면 점 루프에서 좌표가 두 예외값(exception value)과 모두 다를 때 유효 좌표를 면 배열에 추가한다(139–156). 면의 마지막 점은 전체 BOUNDARY 배열에 넣지 않아 모서리 중복을 피한다(150–155). ystep=0이면 x 인덱스를 갱신하고 else는 y 인덱스를 갱신한다(157–161). 원문: `if (.not.allocated(xsid)) allocate (xsid(1:lside))` (133); `if (.not.allocated(ysid)) allocate (ysid(1:lside))` (134); `ix = ix0` (135); `iy = iy0` (136); `ispt = 0` (137); `do ii = 1, lside` (139); `xp = xcgrid(ix,iy)` (143); `yp = ycgrid(ix,iy)` (144); `if (.not.(EQREAL(xp,OVEXCV(1)).or.EQREAL(yp,OVEXCV(2)))) then` (145); `ispt = ispt + 1` (147); `xsid(ispt) = xp` (148); `ysid(ispt) = yp` (149); `if (ii<lside) then` (150); `ibnd = ibnd + 1` (152); `xbnd(ibnd) = xp` (153); `ybnd(ibnd) = yp` (154); `if (ystep==0) then` (157); `ix = ix + xstep` (158); `else` (159); `iy = iy + ystep` (160). |
| 164–193 | 시작 시 1행 SwanBndStruc 루틴·98행 iside 루프 안. BOUND_와 두 자리 면 번호로 psname을 만든다(164). 유효 면 점 수가 양수이면 OPSDAT와 좌표를 할당·복사하고 면별 배열을 해제한다(165–177). NEXTOPS를 nullify한다(178). LOPS가 거짓이면 FOPS·COPS·LOPS를 설정하고 else는 연결 목록(linked list)에 OPSTMP를 잇는다(179–186). ITEST>=10이면 생성 로그를 출력한다(187–188). 점이 없으면 MSGERR(1)를 호출한다(189–191). 네 면 루프를 끝낸다(192). 원문: `write (psname, '(A6, I2.2)') 'BOUND_', iside` (164); `mip = ispt` (165); `if (mip>0) then` (166); `OPSTMP%PSNAME = psname` (168); `OPSTMP%PSTYPE = 'C'` (169); `OPSTMP%MIP = mip` (170); `do jj = 1, mip` (173); `OPSTMP%XP(jj) = xsid(jj)` (174); `OPSTMP%YP(jj) = ysid(jj)` (175); `if ( .not.LOPS ) then` (179); `FOPS = OPSTMP` (180); `COPS => FOPS` (181); `LOPS = .TRUE.` (182); `else` (183); `COPS%NEXTOPS => OPSTMP` (184); `COPS => OPSTMP` (185); `if (ITEST>=10) write (PRTEST, *) 'Output curve ', psname,    &` (187); `' with ', mip, ' points is generated'` (188); `else` (189); `call MSGERR(1,'No output points found in '//psname)` (190). |
| 194–223 | 시작 시 1행 SwanBndStruc 루틴 안. psname='BOUNDARY'와 mip=ibnd를 설정한다(194–195). 점 수가 양수이면 전체 경계 OPSDAT와 좌표를 할당·복사하고 xbnd·ybnd를 해제한다(196–207). NEXTOPS nullify와 LOPS에 따른 목록 설정을 수행한다(208–216). ITEST>=10이면 생성 로그를 출력하며 점이 없으면 MSGERR(1)를 호출한다(217–221). 루틴 종료까지 포함한다(222–223). 원문: `psname = 'BOUNDARY'` (194); `mip = ibnd` (195); `if (mip>0) then` (196); `OPSTMP%PSNAME = psname` (198); `OPSTMP%PSTYPE = 'C'` (199); `OPSTMP%MIP = mip` (200); `do jj = 1, mip` (203); `OPSTMP%XP(jj) = xbnd(jj)` (204); `OPSTMP%YP(jj) = ybnd(jj)` (205); `if ( .not.LOPS ) then` (209); `FOPS = OPSTMP` (210); `COPS => FOPS` (211); `LOPS = .TRUE.` (212); `else` (213); `COPS%NEXTOPS => OPSTMP` (214); `COPS => OPSTMP` (215); `if (ITEST>=10) write (PRTEST, *) 'Output curve ', psname,    &` (217); `' with ', mip, ' points is generated'` (218); `else` (219); `call MSGERR(1,'No output points found in '//psname)` (220). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 72·99–130·139–162: ix1·iy1은 선언과 면별 값 설정에만 등장한다. 점 루프는 lside와 xstep·ystep을 사용한다.
- 82·85: msgstr와 ROPS는 선언 이후 이 파일에서 사용되지 않는다.
- 133–134·166–191: xsid·ysid 해제는 mip>0 참 분기 안에 있다. mip=0이면 배열이 할당된 상태로 다음 면으로 이동하며 다음 면의 할당 조건은 allocated 여부만 검사한다.
- 145–155: 좌표 유효성은 각 점에서 검사한다. 전체 BOUNDARY에 넣는 조건은 ii<lside이며 그 면의 유효점 순서와 별도로 적용된다.
