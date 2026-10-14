---
file: models/SWASH/raw/source_code/swash/src/SwanFindPoint.ftn90
lines: 173
sha256: b7a2af324b9e3f5a69fb36e8fd1aa4c8966d98c669ec54175ad83aa823453cf3
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanFindPoint.ftn90 — 판독 구간 기록

구간은 1행부터 173행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–58 | `subroutine SwanFindPoint ( x, y, kvert )` (1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). 주어진 점의 가장 가까운 꼭짓점(vertex) 인덱스를 찾는다는 목적(38–40). ocpcomm4·SwashCommdata3·SwanGriddata·SwanGridobjects·SwanCompdata 사용(44–48), implicit none(50). kvert는 intent(out), 미발견 표시 -1이라는 주석(54–55). x·y는 intent(in)(56–57). |
| 59–96 | 시작 시 1행 SwanFindPoint 루틴 안. `ient = 0` (61)과 면(face)·꼭짓점·경계 반복 인덱스(61–66), 거리·면 길이 성분·투영 비율·좌표(68–79), 논리 함수 SwanPointinMesh(81), face 포인터(pointer)(83)를 선언한다. 구조·실행부 표제(85–90), `if (ltrace) call strace (ient,'SwanFindPoint')` (91), face를 gridobject%face_grid에 연결(95). [10-15 전수 검증 보완] |
| 97–124 | 시작 시 1행 SwanFindPoint 루틴 안. `if ( x < XCGMIN .or. x > XCGMAX .or. y < YCGMIN .or. y > YCGMAX ) then` (99)이면 `kvert = -1` (101)로 미발견 값을 저장한다. 이어 `return` (102)한다. `if ( SwanPointinMesh( x, y ) ) then` (106)은 최소 거리값을 `dismin = 1.e20` (110)으로 둔다. `do ivert = 1, nverts` (112)에서 `xc = xcugrd(ivert)` (114)와 `yc = ycugrd(ivert)` (115)로 꼭짓점 좌표를 얻는다. `dist = sqrt( (x-xc)**2 + (y-yc)**2 )` (117)을 계산한다. `if ( dist < dismin ) then` (118)이면 `kvert  = ivert` (119)와 `dismin = dist` (120)로 최근접 꼭짓점과 최소 거리를 갱신한다. [10-15 전수 검증 보완] |
| 125–173 | 이 구간은 `if ( SwanPointinMesh( x, y ) ) then` (106)의 `else` (125)부터 이어진다. 이 바깥 분기는 `endif` (171)로 닫힌다. `else` (125)는 경계 면을 `faceloop: do jb = 1, nfacesb` (131)로 순회한다. `iface = jbface(jb)` (133)로 경계 면 번호를 얻는다. `v1 = face(iface)%atti(FACEV1)` (135)과 `v2 = face(iface)%atti(FACEV2)` (136)로 두 꼭짓점을 얻는다. 좌표 대입문은 `x1 = xcugrd(v1)` (138), `y1 = ycugrd(v1)` (139), `x2 = xcugrd(v2)` (140), `y2 = ycugrd(v2)` (141)이다. `dxb = x2 - x1` (143), `dyb = y2 - y1` (144), `reldis = abs( dyb*(x-x1) - dxb*(y-y1) ) / ( dxb*dxb + dyb*dyb )` (146). `if ( reldis < 0.01 ) then` (148)에서 `r   = ( dxb*(x-x1) + dyb*(y-y1) ) / ( dxb*dxb + dyb*dyb )` (150)이다. `if ( r < -0.01 .or. r > 1.01 ) then      ! 41.13` (152)은 `kvert = -1` (153), `else` (154)는 `if ( r < 0.5 ) then` (156)에서 `kvert = v1` (157)로 첫 끝점을 선택한다. `else` (158)는 `kvert = v2` (159)로 두 번째 끝점을 선택한다. 이 끝점 선택은 `endif` (160)으로 닫힌다. `exit faceloop` (161)는 152행 조건의 `else` (154) 안에서 실행한다. 148행의 `else` (165)는 `kvert = -1` (166)이다. 경계 면 반복은 `enddo faceloop` (169)로 닫힌다. 분기·루프·루틴 종료(167–173). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 110–123·131–169: kvert의 공통 초기값 대입은 루프 앞에 없다. 격자 내부 분기에서는 더 짧은 거리를 찾을 때 대입한다. 경계 분기에서는 각 면의 조건 안에서 대입한다.
- 146·150: 두 거리식의 분모는 `dxb*dxb + dyb*dyb`이다. 이 블록에는 분모가 0인지 검사하는 조건이 없다.
- 148·152·156: 경계 허용값은 0.01, 투영 비율 범위는 -0.01..1.01, 끝점 선택 기준은 0.5로 고정한다.
