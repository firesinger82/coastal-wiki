---
file: models/SWAN/raw/source_code/swan/src/SwanInterpolateAc.ftn90
lines: 296
sha256: f8a47f3607d0e54c2ee4af5acf19ab6bbd261063109720d24381ad7cc5ed5187
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanInterpolateAc.ftn90 — 판독 구간 기록

구간은 1행부터 296행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | `SwanInterpolateAc` 입구(1). 기관·GPL 3 이상·무보증·작성자·장애물 근처 보간 개선 이력(3–38). 주어진 점의 작용밀도를 보간(interpolation)한다는 목적(40–42). 최근접 꼭짓점·대상 삼각형을 찾고 꼭짓점 가중치(weight)를 계산한다. 점과 꼭짓점 사이에 장애물이 있으면 해당 가중치를 0으로 한다는 방법 주석(44–49). 통신·장애물·격자 모듈과 `implicit none`(53–60). |
| 62–119 | 시작 시 1행 루틴 안. 입력 작용밀도·점 좌표, 출력 보간 작용밀도·정의되지 않은 값 플래그 `excpt` 선언(64–68). 셀·꼭짓점·순환 번호·순회·장애물 모서리 수, 좌표차·각도·가중치·장애물 끝점·메시지 변수 선언(72–100). 셀 발견·교차·동등 비교·장애물 셀 플래그, `TCROSS`, 사용되지 않는다는 주석의 `xonobst`, 장애물·셀·꼭짓점 포인터 선언(102–112). 초기값 선언은 `integer, save                         :: ient = 0  ! number of entries in this subroutine`(73)이다. 구조·소스 안내 주석(114–119). [10-13 전수 검증 보완] |
| 120–159 | 시작 시 1행 루틴 안. 추적 조건은 `if (ltrace) call strace (ient,'SwanInterpolateAc')` (120)이다. 객체 연결은 `vert => gridobject%vert_grid`(124)와 `cell => gridobject%cell_grid`(125)이다. 보간 결과 초기값은 `acintp = 0.`(129)이다. 예외 플래그 초기값은 `excpt = .true.`(131)이다. `SwanFindPoint(x,y,ivert)` 호출(135). 미발견 반환 조건은 `if ( ivert < 0 ) return` (139)이다. 점에서 꼭짓점까지 좌표차는 `dxp = xcugrd(ivert) - x` (143); `dyp = ycugrd(ivert) - y` (144)이다. 같은 위치 조건은 `if ( EQREAL(dxp,0.) .and. EQREAL(dyp,0.) ) then` (148)이며 참 분기의 대입은 `excpt  = .false.`(149)와 `acintp = ac2(:,:,ivert)`(150)이다. 이어 `return`(151)한다. 이 조건은 152행에서 끝난다. 방향각 식은 `th = atan2(dyp,dxp)` (154)이다. 셀 발견 플래그 초기값은 `cellfound = .false.`(156)이다. [10-13 전수 검증 보완] |
| 160–200 | 시작 시 1행 루틴 안. `celloop: do jc = 1, vert(ivert)%noc`(160)에서 셀 번호 대입은 `icell = vert(ivert)%cell(jc)%atti(CELLID)`(164)이다. 꼭짓점 대입은 `v(1) = cell(icell)%atti(CELLV1)`(166), `v(2) = cell(icell)%atti(CELLV2)`(167), `v(3) = cell(icell)%atti(CELLV3)`(168)이다. `do k = 1, 3`(172)의 일치 조건은 `if ( v(k) == ivert ) then` (173)이다. 참 분기의 방향 대입은 `th1 = cell(icell)%geom(k)%th1`(174)과 `th2 = cell(icell)%geom(k)%th2`(175)이다. `exit`(176)는 172행 내부 루프를 벗어난다. 방향차 식은 `thdiff = th - th2` (180)이다. 무조건 `do`(181)의 종료 조건은 `if ( abs(thdiff) <= PI ) exit` (182)이며 각도 보정은 `th = th - sign (2., thdiff) * PI` (183); `thdiff = th - th2` (184)이다. 경계 조건은 `if ( vert(ivert)%atti(VMARKER) == 1 ) then   ! boundary vertex` (189)이고 참 분기 여유각은 `eps = PI/360.` (190)이다. `else` (191) 분기의 대입은 `eps = 0.`(192)이다. 셀 방향 범위 조건은 `if ( th > th1-eps .and. th <= th2+eps ) then` (195)이며 참 분기에서 `cellfound = .true.`(196)를 대입한다. 이어 `exit celloop`(197)로 160행 셀 루프를 벗어난다. 이 조건은 198행에서 끝난다. 셀 루프의 종료문은 `enddo celloop`(200)이다. [10-13 전수 검증 보완] |
| 201–230 | 시작 시 1행 루틴 안이며 셀 루프 밖. 미발견 조건은 `if ( .not.cellfound ) then` (204)이다. 참 분기의 메시지 작성은 `write (msgstr, '(a,f12.4,a,f12.4,a)') ' No triangle containing point (',x+XOFFS,',',y+YOFFS,') is found'`(205)이다. `call msgerr( 1, trim(msgstr) )`(206) 뒤에 `return`(207)한다. 이 조건은 208행에서 끝난다. 예외 플래그 대입은 `excpt = .false.`(212)이다. `do k = 1, 3`(216)에서 좌표 대입은 `xv(k) = xcugrd(v(k))`(217)와 `yv(k) = ycugrd(v(k))`(218)이다. 교차 플래그 대입은 `cross(k) = .false.`(219)이다. 다음 `do k = 1, 3`(224)의 순환 꼭짓점·마주 보는 변의 좌표차 식은 `ivc(2) = mod(k  ,3)+1` (225); `ivc(3) = mod(k+1,3)+1` (226); `dxv(k) = xv(ivc(3)) - xv(ivc(2))` (227); `dyv(k) = yv(ivc(3)) - yv(ivc(2))` (228)이다. [10-13 전수 검증 보완] |
| 231–269 | 시작 시 1행 루틴 안. 장애물 조건은 `if ( NUMOBS > 0 ) then` (233)이다. 첫 장애물 포인터 연결은 `COBST => FOBSTAC`(235)이다. `do jc = 1, NUMOBS`(237)에서 모서리 수 대입은 `numcor = COBST%NCRPTS`(239)이다. 시작점 대입은 `xb = COBST%XCRP(1)`(242)과 `yb = COBST%YCRP(1)`(243)이다. 진단 출력 조건은 `if ( ITEST >= 120 ) write (PRINTF,10) jc, numcor` (240), `if ( ITEST >= 120 ) write (PRINTF,20) 1, xb+XOFFS, yb+YOFFS` (244)이다. `do l = 2, numcor`(246)에서 끝점 대입은 `xe = COBST%XCRP(l)`(248)과 `ye = COBST%YCRP(l)`(249)이다. 진단 출력 조건은 `if ( ITEST >= 120 ) write (PRINTF,20) l, xe+XOFFS, ye+YOFFS` (250)이다. `do k = 1, 3`(254)의 선분 교차 검사·`TCROSS` 호출은 `if ( TCROSS(x, xv(k), xb, xe, y, yv(k), yb, ye, xonobst) ) cross(k) = .true.` (255)이다. 다음 선분 시작점 대입은 `xb = xe`(258)와 `yb = ye`(259)이다. 다음 장애물 존재 검사·종료 조건은 `if (.not.associated(COBST%NEXTOBST)) exit` (263)이다. 다음 포인터 연결은 `COBST => COBST%NEXTOBST`(264)이다. 장애물 루프는 266행에서 끝난다. 233행 장애물 조건은 ELSE 없이 268행에서 끝난다. [10-13 전수 검증 보완] |
| 270–296 | 시작 시 1행 루틴 안. 장애물 셀 플래그 초기값은 `obstcell = .false.`(272)이다. `do k = 1, 3`(273)의 교차 조건은 `if (cross(k)) then` (274)이다. 참 분기 대입은 `ww(k) = 0.`(275)과 `obstcell = .true.`(276)이다. `else` (277) 분기의 첫 순환 번호 대입은 `ivc(1) = k`(278)이다. 나머지 순환 번호·가중치 식은 `ivc(2) = mod(k  ,3)+1` (279); `ivc(3) = mod(k+1,3)+1` (280); `ww(k) = ((x - xv(ivc(3))) * dyv(ivc(1)) - (y - yv(ivc(3))) * dxv(ivc(1))) / ( dxv(ivc(2)) * dyv(ivc(1)) - dyv(ivc(2)) * dxv(ivc(1)) )` (281)이다. 가중치 합산 조건·식은 `if (obstcell) sumww = sum(ww)` (284)이다. `do k = 1, 3`(288)의 정규화 조건·식은 `if (obstcell) ww(k) = ww(k) / sumww` (289)이다. 보간 누적식은 `acintp(:,:) = acintp(:,:) + ww(k) * ac2(:,:,v(k))` (290)이다. 루프·장애물 진단 출력 형식 10·20·루틴 종료(291–296). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 274–289: 교차된 꼭짓점 가중치는 0이다. 장애물 셀이면 `sumww=sum(ww)`로 정규화한다. `sumww`가 0인지 검사하는 조건은 이 블록에 없다.
- 148–152·233–268: 입력 점이 꼭짓점과 같은 위치이면 해당 작용밀도를 복사하고 즉시 반환한다. 장애물 선분 검사는 그 뒤에 있다.
- 107·255: `xonobst`는 사용되지 않는다는 선언 주석을 갖는다. 이 변수는 `TCROSS`의 인수로 전달되지만 반환 후 값을 읽는 문장은 없다.
- 281: 가중치 계산은 두 좌표차의 교차곱 차로 나눈다. 이 대입 앞에는 해당 분모의 0 검사가 없다.
