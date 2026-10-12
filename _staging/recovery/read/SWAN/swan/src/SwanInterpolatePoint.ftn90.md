---
file: models/SWAN/raw/source_code/swan/src/SwanInterpolatePoint.ftn90
lines: 248
sha256: 780b79e603e6d166f3181eaccfefdb1f0b2fb82307845df7e38a05c287d750df
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanInterpolatePoint.ftn90 — 판독 구간 기록

구간은 1행부터 248행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | `SwanInterpolatePoint` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 가장 가까운 꼭짓점을 찾고 대상 삼각형 안에서 스칼라(scalar)를 주어진 점으로 보간한다는 목적·방법(38–44). 통신·격자 모듈과 `implicit none`(48–54). |
| 56–106 | 시작 시 1행 루틴 안. 예외값(exception value) `excval`, 입력 꼭짓점 스칼라 `finp`, 출력 `foutp`, 점 좌표 입력(58–62). 셀·꼭짓점·순회·면적·점 좌표차·여유각·세 스칼라 및 평균·방향각·세 변위벡터·무게중심·스칼라 기울기(scalar gradient)·메시지·셀 발견 및 실수 비교 함수·객체 포인터 선언(66–99). 초기값 선언은 `integer, save                         :: ient = 0  ! number of entries in this subroutine`(67)이다. 구조·소스 안내 주석(101–106). [10-13 전수 검증 보완] |
| 107–151 | 시작 시 1행 루틴 안. 추적 조건은 `if (ltrace) call strace (ient,'SwanInterpolatePoint')` (107)이다. 객체 연결은 `vert => gridobject%vert_grid`(111)와 `cell => gridobject%cell_grid`(112)이다. 출력 초기값 대입은 `foutp = excval`(116)이다. `SwanFindPoint(x,y,ivert)` 호출(120). 미발견 조건은 `if ( ivert < 0 ) then` (124)이며 메시지 작성은 `write (msgstr, '(a,f12.4,a,f12.4,a)') ' Point (',x+XOFFS,',',y+YOFFS,') not given in computational grid'`(125)이다. `call msgerr( 1, trim(msgstr) )`(126) 뒤에 `return`(127)한다. 이 조건은 128행에서 끝난다. 최근접 꼭짓점의 예외값 반환 조건은 `if ( EQREAL(finp(ivert),excval) ) return` (132)이다. 좌표차 식은 `dxp = xcugrd(ivert) - x` (136); `dyp = ycugrd(ivert) - y` (137)이다. 같은 위치 조건은 `if ( EQREAL(dxp,0.) .and. EQREAL(dyp,0.) ) then` (141)이며 `foutp = finp(ivert)`(142)로 스칼라를 복사한다. 이어 `return`(143)한다. 이 조건은 144행에서 끝난다. 방향각은 `th = atan2(dyp,dxp)` (146)이다. 셀 발견 플래그 초기값은 `cellfound = .false.`(148)이다. [10-13 전수 검증 보완] |
| 152–200 | 시작 시 1행 루틴 안. `celloop: do jc = 1, vert(ivert)%noc`(152)에서 셀 번호 대입은 `icell = vert(ivert)%cell(jc)%atti(CELLID)`(156)이다. 꼭짓점 대입은 `v(1) = cell(icell)%atti(CELLV1)`(158), `v(2) = cell(icell)%atti(CELLV2)`(159), `v(3) = cell(icell)%atti(CELLV3)`(160)이다. `do k = 1, 3`(164)의 일치 조건은 `if ( v(k) == ivert ) then` (165)이며 방향 대입은 `th1 = cell(icell)%geom(k)%th1`(166)과 `th2 = cell(icell)%geom(k)%th2`(167)이다. `exit`(168)는 164행 내부 루프를 벗어난다. 방향차는 `thdiff = th - th2` (172)이다. 무조건 `do`(173)의 종료 조건은 `if ( abs(thdiff) <= PI ) exit` (174), 각도 보정은 `th = th - sign (2., thdiff) * PI` (175); `thdiff = th - th2` (176)이다. 경계 조건은 `if ( vert(ivert)%atti(VMARKER) == 1 ) then   ! boundary vertex` (181)이며 여유각은 `eps = PI/360.` (182)이다. `else` (183) 분기의 대입은 `eps = 0.`(184)이다. 셀 방향 범위 조건은 `if ( th > th1-eps .and. th <= th2+eps ) then` (187)이며 참 분기에서 `cellfound = .true.`(188)를 대입한다. 이어 `exit celloop`(189)로 셀 루프를 벗어난다. 셀 루프의 종료문은 `enddo celloop`(192)이다. 미발견 조건은 `if ( .not.cellfound ) then` (196)이며 메시지 작성은 `write (msgstr, '(a,f12.4,a,f12.4,a)') ' No triangle containing point (',x+XOFFS,',',y+YOFFS,') is found'`(197)이다. `call msgerr( 1, trim(msgstr) )`(198) 뒤에 `return`(199)한다. 이 조건은 200행에서 끝난다. [10-13 전수 검증 보완] |
| 201–233 | 시작 시 1행 루틴 안이며 셀 루프 밖. 꼭짓점 스칼라 대입은 `phi1 = finp(v(1))`(204), `phi2 = finp(v(2))`(205), `phi3 = finp(v(3))`(206)이다. 예외값이 없는 경우의 계산 조건은 `if ( .not.EQREAL(phi1,excval) .and. .not.EQREAL(phi2,excval) .and. .not.EQREAL(phi3,excval) ) then` (210)이다. 참 분기의 무게중심 대입은 `xc    = cell(icell)%attr(CELLCX  )`(214)와 `yc    = cell(icell)%attr(CELLCY  )`(215)이다. 면적 대입은 `carea = cell(icell)%attr(CELLAREA)`(216)이다. 무게중심 스칼라 평균식은 `phic = ( phi1 + phi2 + phi3 ) / 3.` (220)이다. 세 변위벡터 식은 `vec12(1) = xcugrd(v(2)) - xcugrd(v(1))` (224); `vec12(2) = ycugrd(v(2)) - ycugrd(v(1))` (225); `vec23(1) = xcugrd(v(3)) - xcugrd(v(2))` (226); `vec23(2) = ycugrd(v(3)) - ycugrd(v(2))` (227); `vec31(1) = xcugrd(v(1)) - xcugrd(v(3))` (228); `vec31(2) = ycugrd(v(1)) - ycugrd(v(3))` (229)이다. 외향 법선(outward normal)을 변위벡터의 시계 방향 90도 회전으로 구한다는 주석(231–233). [10-13 전수 검증 보완] |
| 234–248 | 시작 시 1행 루틴·210행 세 꼭짓점 비예외값 참 분기 안. 스칼라 기울기 성분 식은 `xgrs =  vec23(2)*phi1 + vec31(2)*phi2 + vec12(2)*phi3` (235); `ygrs = -vec23(1)*phi1 - vec31(1)*phi2 - vec12(1)*phi3` (236)이며 면적 정규화 식은 `xgrs = -0.5*xgrs/carea` (238); `ygrs = -0.5*ygrs/carea` (239)이다. 일정 기울기를 쓰는 2차원 보간식은 `foutp = phic + xgrs*(x - xc) + ygrs*(y - yc)` (244)이다. 예외값 조건·루틴 종료·주석(246–248). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 116·132·210–246: 최근접 꼭짓점이 예외값이면 즉시 반환한다. 선택한 삼각형의 세 꼭짓점 중 하나라도 예외값이면 보간 대입을 실행하지 않으며 출력은 초기 예외값을 유지한다.
- 238–239: 스칼라 기울기를 셀 면적 `carea`로 나눈다. 이 대입 앞에는 면적의 0 또는 양수 검사가 없다.
- 181–187: 경계 꼭짓점에서 방향 허용 여유각은 `PI/360.`이다. 내부 꼭짓점에서는 여유각을 0으로 설정한다.
