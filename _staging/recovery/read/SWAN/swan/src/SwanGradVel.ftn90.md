---
file: models/SWAN/raw/source_code/swan/src/SwanGradVel.ftn90
lines: 251
sha256: fa52ab7f829fa1a76302005e08987b9f4b06ca4e8b5194c19f0078c097884590
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanGradVel.ftn90 — 판독 구간 기록

구간은 1행부터 251행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–58 | `SwanGradVel` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 스펙트럼 공간(spectral space)의 수송속도(transport velocity)에 쓸 유속 성분(velocity component)의 꼭짓점 기울기를 계산한다는 목적(38–41). 무게중심 쌍대 제어체적에 일정 기울기를 가정한 Green–Gauss 방법(43–46). 통신·격자 모듈과 `implicit none`(50–57). |
| 59–108 | 시작 시 1행 루틴 안. 현재 꼭짓점·수심·주변 유속(ambient velocity) 두 성분 입력, 네 유속 미분 출력 선언(61–69). 셀·쌍대영역 면적의 두 배 `area`·보조 배열·수심 극값·무게중심 유속 및 좌표·메시지·객체 포인터 선언(73–101). `ient = 0` 초기값(74). 수심비 상수는 `real, parameter                       :: drat= 5. ! ratio between maximum and minimum depths in centroid dual` (88)이다. 구조·소스 안내 주석(103–108). [10-13 전수 검증 정정] [10-13 전수 검증 보완] |
| 109–158 | 시작 시 1행 루틴 안. 추적 조건은 `if (ltrace) call strace (ient,'SwanGradVel')` (109)이다. 미분 초기값은 `duxdx = 0.`(111), `duxdy = 0.`(112), `duydx = 0.`(113), `duydy = 0.`(114)이다. 주파수 이동(frequency shift)·굴절(refraction)에 관한 반환 조건은 `if ( ITFRE == 0 .and. IREFR == 0 ) return` (118)이다. 파랑-흐름 상호작용(wave-current interaction) 관련 주석(120) 아래 반환 조건은 `if ( IQCM /= 0 ) return` (122)이다. 객체 연결 뒤 경계 반환 조건은 `if ( vert(ivert)%atti(VMARKER) == 1 ) return    ! boundary vertex` (129)이다. 면적의 두 배 초기값 `area  =  0d0`(131), 수심 극값 초기식 `dpmax = -99999.` (132); `dpmin =  99999.` (133). `do jc = 1, vert(ivert)%noc`(137)에서 현재 셀·꼭짓점·수심을 읽는다(141–149). 수심 조건은 `if ( dloc(1) <= DEPMIN .or. dloc(2) <= DEPMIN .or. dloc(3) <= DEPMIN ) goto 10` (151)이며 10번 표지로 이동한다. 극값 계산·갱신식은 `dminc = min ( min( dloc(1), dloc(2) ), dloc(3) )` (153); `if ( dminc < dpmin ) dpmin = dminc` (154), `dmaxc = max ( max( dloc(1), dloc(2) ), dloc(3) )` (156); `if ( dmaxc > dpmax ) dpmax = dmaxc` (157)이다. 셀 번호는 `icell = vert(ivert)%cell(jc)%atti(CELLID)`(141)이다. 꼭짓점 번호는 `v(1) = cell(icell)%atti(CELLV1)`(143), `v(2) = cell(icell)%atti(CELLV2)`(144), `v(3) = cell(icell)%atti(CELLV3)`(145)이다. 수심 대입은 `dloc(1) = dep2(v(1))`(147), `dloc(2) = dep2(v(2))`(148), `dloc(3) = dep2(v(3))`(149)이다. 120행 주석은 파랑과 흐름의 상호작용이 있으면 반환한다고 적는다. [10-13 전수 검증 정정] [10-13 전수 검증 보완] |
| 159–213 | 시작 시 1행 루틴·137행 인접 셀 루프 안. 현재 무게중심 좌표를 읽고(161–162), 평균 유속을 `ux0 = ( ux2(v(1)) + ux2(v(2)) + ux2(v(3)) )/ 3.` (166), `uy0 = ( uy2(v(1)) + uy2(v(2)) + uy2(v(3)) )/ 3.` (170)으로 계산한다. 다음 셀·꼭짓점·수심을 읽는다(174–182). 수심 조건은 `if ( dloc(1) <= DEPMIN .or. dloc(2) <= DEPMIN .or. dloc(3) <= DEPMIN ) goto 10` (184)이다. 다음 무게중심 좌표를 읽고(188–189), 평균 유속을 `ux1 = ( ux2(v(1)) + ux2(v(2)) + ux2(v(3)) )/ 3.` (193), `uy1 = ( uy2(v(1)) + uy2(v(2)) + uy2(v(3)) )/ 3.` (197)로 계산한다. 면적의 두 배와 네 미분 누적식은 `area = area + x0*y1 - x1*y0` (201), `duxdx = duxdx + ( ux0 + ux1 ) * real( y1 - y0 )` (205); `duydx = duydx + ( uy0 + uy1 ) * real( y1 - y0 )` (206), `duxdy = duxdy + ( ux0 + ux1 ) * real( x1 - x0 )` (210); `duydy = duydy + ( uy0 + uy1 ) * real( x1 - x0 )` (211)이다. 셀 루프 종료(213). 현재 무게중심 대입은 `x0 = cell(icell)%attr(CELLCX)`(161), `y0 = cell(icell)%attr(CELLCY)`(162)이다. 다음 셀 번호는 `jcell = vert(ivert)%cell(jc)%atti(NEXTCELL)`(174)이다. 꼭짓점 번호는 `v(1) = cell(jcell)%atti(CELLV1)`(176), `v(2) = cell(jcell)%atti(CELLV2)`(177), `v(3) = cell(jcell)%atti(CELLV3)`(178)이다. 수심 대입은 `dloc(1) = dep2(v(1))`(180), `dloc(2) = dep2(v(2))`(181), `dloc(3) = dep2(v(3))`(182)이다. 다음 무게중심 대입은 `x1 = cell(jcell)%attr(CELLCX)`(188), `y1 = cell(jcell)%attr(CELLCY)`(189)이다. [10-13 전수 검증 정정] [10-13 전수 검증 보완] |
| 214–251 | 시작 시 1행 루틴 안이며 인접 셀 루프 밖. 수심비 제한은 일반 주석 `!if ( dpmax > drat * dpmin ) goto 10` (217)이다. 면적 검사 조건은 `if ( .not. area > 0d0 ) then` (221)이며 `write (msgstr, '(a,i5)') ' Area of centroid dual is negative or zero in vertex ', ivert`(222)로 오류 문자열을 쓴다. 같은 분기에서 `call msgerr( 2, trim(msgstr) )`(223)를 호출한다. 같은 분기에서 `return`(224)으로 반환한다. 조건은 225행에서 닫힌다. 네 미분 정규화 식은 `duxdx =  duxdx/real(area)` (227); `duxdy = -duxdy/real(area)` (228); `duydx =  duydx/real(area)` (229); `duydy = -duydy/real(area)` (230)이다. 구면 조건 `if ( KSPHER > 0 ) then` (234)의 위도·변환식은 `cslat = cos(DEGRAD*(vert(ivert)%attr(VERTY) + YOFFS))` (236), `duxdx = duxdx/(cslat * LENDEG)` (238); `duxdy = duxdy/LENDEG` (239); `duydx = duydx/(cslat * LENDEG)` (240); `duydy = duydy/LENDEG` (241)이다. 정상 반환(245). 10번 표지의 대입은 `10 duxdx = 0.`(246), `duxdy = 0.`(247), `duydx = 0.`(248), `duydy = 0.`(249)이다. 주석·루틴 종료(250–251). 정규화 분모 `area`는 쌍대영역 면적의 두 배이다(80,227–230). 구면 조건은 243행에서 닫힌다. [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 81: 보조 배열 `arr(MSC)`는 선언 이후 이 파일에서 사용되지 않는다.
- 83–88·153–157·217: 수심 극값과 `drat=5` 상수가 있다. 수심비 초과 검사문은 일반 주석으로 처리되어 있다.
- 205–211·221–230: 면적 오류 분기는 누적 미분을 0으로 바꾸지 않고 반환한다. 10번 표지의 0 설정은 수심 조건의 `goto 10` 경로에 있다(151·184·246–249).
