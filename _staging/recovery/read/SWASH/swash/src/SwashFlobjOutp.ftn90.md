---
file: models/SWASH/raw/source_code/swash/src/SwashFlobjOutp.ftn90
lines: 204
sha256: 2bcd0fcfe87004260142abdd56f13c4f0253d6c25f32b49b464100f3fd52f08d
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashFlobjOutp.ftn90 — 판독 구간 기록

구간은 1행부터 204행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | `SwashFlobjOutp ( oqproc, nvoqp, voqr, voq )` 입구(1). 기관·저작권·GPL 3 이상·무보증 주석(2–29). 작성자와 2018년 신설 이력(30–37). 유체동역학 하중(hydrodynamic load)과 물체 운동(body motion)을 출력 요청에 맞춰 제공한다는 목적 주석(38–41). ocpcomm4, 출력 수·매개변수, ifloat·pi, timco, 강체(rigid body) 자료 모듈을 사용한다(44–48). |
| 50–80 | 시작 시 1행 SwashFlobjOutp 루틴 안. implicit none(50). 입력은 수량 수 nvoqp, 출력 위치 voqr(nmovar), 처리 여부 oqproc(nmovar)이며 출력은 voq(nvoqp)이다(54–57). 진입 횟수 `integer, save                   :: ient = 0 ! number of entries in this subroutine` (61). j·k·l·nflob와 할당 가능한 힘 fx·fy·fz, 모멘트(moment) mx·my·mz를 선언한다(62–73). 구조·소스 머리말 주석(75–80). |
| 81–100 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashFlobjOutp')` (81). 물체 수 분기는 `if ( ifloat == 1 ) then` (85)에서 `nflob = 1` (86), `else if ( ifloat == 2 ) then` (87)에서 `nflob = mbod` (88)이다. 85–89행 분기 사슬에는 `else`가 없다. 조건 종료(89) 뒤 힘·모멘트 여섯 배열을 nflob 크기로 할당한다(93–99). [10-15 전수 검증 보완] |
| 101–129 | 시작 시 1행 루틴 안. `if ( ifloat == 1 ) then` (103)은 고정 물체 경로이다. `do j = 1, ndim` (107)·`do k = 1, 2` (108) 안에서 `l = j + ndim*(k-1)` (109), `bdof(1,j,k) = oqproc(100+l)` (110)로 출력 요청을 저장한다. 루프 종료 뒤 `call SwashHydroLoads ( nflob, fx, fy, fz, mx, my, mz )` (114). 같은 조건의 `else if ( ifloat == 2 ) then` (116)은 움직이는 물체 경로이며 fhyd1의 세 성분을 fx·fy·fz로, thyd1의 세 성분을 mx·my·mz로 복사한다(120–126). 조건 종료·주석(128–129). 103–128행 분기 사슬에는 `else`가 없다. 이동 물체의 복사식은 `fx(:) = fhyd1(:,1)` (120), `fy(:) = fhyd1(:,2)` (121), `fz(:) = fhyd1(:,3)` (122), `mx(:) = thyd1(:,1)` (124), `my(:) = thyd1(:,2)` (125), `mz(:) = thyd1(:,3)` (126)이다. [10-15 전수 검증 보완] |
| 130–163 | 시작 시 1행 루틴 안. 요청 시 출력 시간은 `if ( oqproc(41) ) voq(voqr(41)) = real(timco) - outpar(1)` (134). `do j = 1, nflob` (136)의 요청별 힘·모멘트 출력식은 `if ( oqproc(101) ) voq(voqr(101)+j-1) = fx(j) / 1000.` (140), `if ( oqproc(102) ) voq(voqr(102)+j-1) = fy(j) / 1000.` (144), `if ( oqproc(103) ) voq(voqr(103)+j-1) = fz(j) / 1000.` (148), `if ( oqproc(104) ) voq(voqr(104)+j-1) = mx(j) / 1000.` (152), `if ( oqproc(105) ) voq(voqr(105)+j-1) = my(j) / 1000.` (156), `if ( oqproc(106) ) voq(voqr(106)+j-1) = mz(j) / 1000.` (160)이다. 루프 종료(162). |
| 164–200 | 시작 시 1행 루틴 안. `if ( ifloat == 2 ) then` (166)·`do j = 1, nflob` (168) 안에서 운동과 동력인출장치(power take-off, PTO) 출력을 처리한다. 병진(translation) 출력 조건은 `if ( oqproc(107) ) voq(voqr(107)+j-1) = xfot1(j,1)` (172), `if ( oqproc(108) ) voq(voqr(108)+j-1) = xfot1(j,2)` (176), `if ( oqproc(109) ) voq(voqr(109)+j-1) = xfot1(j,3)` (180). 회전(rotation) 출력은 `if ( oqproc(110) ) voq(voqr(110)+j-1) = xfor1(j,1) * 180./pi` (184), `if ( oqproc(111) ) voq(voqr(111)+j-1) = xfor1(j,2) * 180./pi` (188), `if ( oqproc(112) ) voq(voqr(112)+j-1) = xfor1(j,3) * 180./pi` (192). 동력 출력은 `if ( oqproc(113) ) voq(voqr(113)+j-1) = ptop(j) / 1000.` (196). 루프·조건 종료(198–200). |
| 201–204 | 시작 시 1행 루틴 안. 여섯 힘·모멘트 배열을 `deallocate ( fx, fy, fz, mx, my, mz )` (202)로 해제하고 루틴을 종료한다(204). 주석도 이 구간에 포함한다(201·203). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65·85–99: nflob 선언에는 초기값이 없다. nflob 대입은 ifloat=1 또는 ifloat=2인 경우에만 있으며, 배열 할당은 이 조건 밖에 있다.
- 56·134–196: voq는 intent(out)이다. 이 루틴에는 voq 전체 초기화가 없으며, 각 출력 위치는 해당 oqproc 조건이 참일 때만 대입한다.
