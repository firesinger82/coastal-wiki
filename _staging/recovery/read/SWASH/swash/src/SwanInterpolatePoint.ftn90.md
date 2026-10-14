---
file: models/SWASH/raw/source_code/swash/src/SwanInterpolatePoint.ftn90
lines: 248
sha256: d2a7b8a67ccb47633035a3d4f28f06a2fefd4b780bcaa159385514f4b2b5bc21
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanInterpolatePoint.ftn90 — 판독 구간 기록

구간은 1행부터 248행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–63 | SwanInterpolatePoint 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). 최근접 꼭짓점(vertex)을 찾은 뒤 점이 위치한 삼각형 안에서 스칼라(scalar)를 보간(interpolation)하는 목적·방법(38–44). 사용 모듈 다섯 개(48–52), implicit none(54). excval·finp(nverts)·x·y는 입력, foutp는 출력(58–62). |
| 64–106 | 시작 시 1행 SwanInterpolatePoint 루틴 안. 셀(cell)·꼭짓점·반복 인덱스와 `ient = 0` (67)을 포함한 선언(66–71), 면적·좌표 차·작은 수 eps·각도·이동 벡터·도심(centroid)·기울기(gradient) 변수(73–91), 메시지(93), cellfound·EQREAL(95–96), cell·vert 포인터(pointer)(98–99), 구조·실행부 표제(101–106). [10-15 전수 검증 정정] [10-15 전수 검증 보완] |
| 107–149 | 시작 시 1행 SwanInterpolatePoint 루틴 안. `if (ltrace) call strace (ient,'SwanInterpolatePoint')` (107), 포인터 연결(111–112), `foutp = excval` (116), `call SwanFindPoint ( x, y, ivert )` (120). `if ( ivert < 0 ) then` (124)은 `write (msgstr, '(a,f12.4,a,f12.4,a)') ' Point (',x+XOFFS,',',y+YOFFS,') not given in computational grid'` (125)로 경고를 작성한다. `call msgerr( 1, trim(msgstr) )` (126)을 호출한다. 이어 `return` (127)한다. `if ( EQREAL(finp(ivert),excval) ) return` (132). `dxp = xcugrd(ivert) - x` (136), `dyp = ycugrd(ivert) - y` (137). `if ( EQREAL(dxp,0.) .and. EQREAL(dyp,0.) ) then` (141)은 `foutp = finp(ivert)` (142)로 출력값을 저장한다. 이어 `return` (143)한다. `th = atan2(dyp,dxp)` (146), `cellfound = .false.` (148)로 셀 발견 표시를 초기화한다. [10-15 전수 검증 보완] |
| 150–192 | 시작 시 1행 SwanInterpolatePoint 루틴 안. `celloop: do jc = 1, vert(ivert)%noc` (152)에서 `icell = vert(ivert)%cell(jc)%atti(CELLID)` (156)로 셀을 얻는다. 꼭짓점 대입문은 `v(1) = cell(icell)%atti(CELLV1)` (158), `v(2) = cell(icell)%atti(CELLV2)` (159), `v(3) = cell(icell)%atti(CELLV3)` (160)이다. `do k = 1, 3` (164)의 `if ( v(k) == ivert ) then` (165)은 `th1 = cell(icell)%geom(k)%th1` (166)과 `th2 = cell(icell)%geom(k)%th2` (167)로 각도를 복사한다. 이어 `exit` (168)로 k 반복을 벗어난다. `thdiff = th - th2` (172), do(173)의 `if ( abs(thdiff) <= PI ) exit` (174), `th = th - sign (2., thdiff) * PI` (175), `thdiff = th - th2` (176). `if ( vert(ivert)%atti(VMARKER) == 1 ) then   ! boundary vertex` (181)이면 `eps = PI/360.` (182), `else` (183)는 `eps = 0.` (184)이다. `if ( th > th1-eps .and. th <= th2+eps ) then` (187)이면 `cellfound = .true.` (188)로 셀 발견 표시를 설정한다. 이어 `exit celloop` (189)로 셀 반복을 벗어난다. 173행 `do`는 `enddo` (177)로 닫힌다. 셀 반복은 `enddo celloop` (192)로 닫힌다. [10-15 전수 검증 보완] |
| 193–220 | 시작 시 1행 SwanInterpolatePoint 루틴 안. `if ( .not.cellfound ) then` (196)은 `write (msgstr, '(a,f12.4,a,f12.4,a)') ' No triangle containing point (',x+XOFFS,',',y+YOFFS,') is found'` (197)로 삼각형 미발견 경고를 작성한다. `call msgerr( 1, trim(msgstr) )` (198)을 호출한다. 이어 `return` (199)한다. `phi1 = finp(v(1))` (204), `phi2 = finp(v(2))` (205), `phi3 = finp(v(3))` (206)으로 꼭짓점 스칼라를 복사한다. `if ( .not.EQREAL(phi1,excval) .and. .not.EQREAL(phi2,excval) .and. .not.EQREAL(phi3,excval) ) then` (210)에서 `xc    = cell(icell)%attr(CELLCX  )` (214)와 `yc    = cell(icell)%attr(CELLCY  )` (215)로 도심을 가져온다. `carea = cell(icell)%attr(CELLAREA)` (216)로 면적을 가져온다. `phic = ( phi1 + phi2 + phi3 ) / 3.` (220)으로 도심 값을 구한다. [10-15 전수 검증 보완] |
| 221–248 | 221–246행은 `if ( .not.EQREAL(phi1,excval) .and. .not.EQREAL(phi2,excval) .and. .not.EQREAL(phi3,excval) ) then` (210)에 속한다. 이 조건은 `endif` (246)으로 닫힌다. `vec12(1) = xcugrd(v(2)) - xcugrd(v(1))` (224), `vec12(2) = ycugrd(v(2)) - ycugrd(v(1))` (225), `vec23(1) = xcugrd(v(3)) - xcugrd(v(2))` (226), `vec23(2) = ycugrd(v(3)) - ycugrd(v(2))` (227), `vec31(1) = xcugrd(v(1)) - xcugrd(v(3))` (228), `vec31(2) = ycugrd(v(1)) - ycugrd(v(3))` (229). 외향 법선(outward normal)과 시계 방향 90도 회전 설명(231–233). `xgrs =  vec23(2)*phi1 + vec31(2)*phi2 + vec12(2)*phi3` (235), `ygrs = -vec23(1)*phi1 - vec31(1)*phi2 - vec12(1)*phi3` (236), `xgrs = -0.5*xgrs/carea` (238), `ygrs = -0.5*ygrs/carea` (239), `foutp = phic + xgrs*(x - xc) + ygrs*(y - yc)` (244). 조건·루틴 종료(246–248). 241–242행 주석은 일정한 스칼라 기울기 벡터를 사용하는 2차원 보간이라고 설명한다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 120–244: 이 루틴에는 꼭짓점 active 검사 조건이 없다. 스칼라의 예외값 여부는 검사한다(132·210).
- 216·238–239: carea를 분모로 사용한다. 이 블록에는 carea=0 검사 조건이 없다.
