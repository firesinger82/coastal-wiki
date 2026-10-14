---
file: models/SWASH/raw/source_code/swash/src/SwanInterpolateOutput.ftn90
lines: 251
sha256: 99b97248c1a226c4575774d9eb5c6463d16b5941264f42a79edfb9c8ea87451b
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanInterpolateOutput.ftn90 — 판독 구간 기록

구간은 1행부터 251행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–73 | SwanInterpolateOutput 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29). 2007년 신설·2008년 장애물 부근 보간(interpolation) 개선·2009년 최적화 이력(30–40). 최근접 꼭짓점(vertex) 주변 삼각형을 찾아 가중치(weight)를 계산하고 출력량을 보간한다는 목적·방법(42–50). 사용 모듈 여섯 개(54–59), implicit none(61). mip·kvert(mip)·excval·finp(nverts)·x(mip)·y(mip)는 입력, foutp(mip)는 출력(65–72). |
| 74–113 | 시작 시 1행 SwanInterpolateOutput 루틴 안. 셀(cell)·꼭짓점·반복 인덱스와 `ient = 0` (77)을 포함한 선언(76–84), 좌표 차·허용값·각도·좌표·가중치 배열(86–98), 메시지(100), cellfound·EQREAL(102–103), cell·vert 포인터(pointer)(105–106), 구조·실행부 표제(108–113). [10-15 전수 검증 보완] |
| 114–131 | 시작 시 1행 SwanInterpolateOutput 루틴 안. `if (ltrace) call strace (ient,'SwanInterpolateOutput')` (114). `if ( LCOMPGRD .and. mip == nvertsg ) then` (116)이면 `foutp = finp` (117)로 전체를 복사한다. 이어 `return` (118)한다. 116행 조건은 `endif` (119)로 닫힌다. 객체 포인터 연결(123–124), `foutp = excval` (128)로 전체 출력을 예외값으로 초기화한다. 출력점 루프 주석(130–131). [10-15 전수 검증 보완] |
| 132–163 | 시작 시 1행 SwanInterpolateOutput 루틴 안. `pointloop: do ip = 1, mip` (132)에서 `ivert = kvert(ip)` (136)로 꼭짓점 번호를 얻는다. `if ( ivert < 0 ) cycle pointloop` (140), `if ( .not.vert(ivert)%active ) cycle pointloop` (144). `dxp = xcugrd(ivert) - x(ip)` (148), `dyp = ycugrd(ivert) - y(ip)` (149). `if ( EQREAL(dxp,0.) .and. EQREAL(dyp,0.) ) then` (153)이면 `foutp(ip) = finp(ivert)` (154)로 출력값을 저장한다. 이어 `cycle pointloop` (155)로 다음 점으로 이동한다. `th = atan2(dyp,dxp)` (158), `cellfound = .false.` (160)로 셀 발견 표시를 초기화한다. [10-15 전수 검증 보완] |
| 164–204 | 시작 시 `pointloop: do ip = 1, mip` (132) 안이다. 이 반복은 `enddo pointloop` (249)로 닫힌다. `celloop: do jc = 1, vert(ivert)%noc` (164)은 `icell = vert(ivert)%cell(jc)%atti(CELLID)` (168)로 셀을 얻는다. 꼭짓점 대입문은 `v(1) = cell(icell)%atti(CELLV1)` (170), `v(2) = cell(icell)%atti(CELLV2)` (171), `v(3) = cell(icell)%atti(CELLV3)` (172)이다. `do k = 1, 3` (176)의 `if ( v(k) == ivert ) then` (177)은 `th1 = cell(icell)%geom(k)%th1` (178)과 `th2 = cell(icell)%geom(k)%th2` (179)로 각도를 복사한다. 이어 `exit` (180)로 k 반복을 벗어난다. `thdiff = th - th2` (184), do(185)의 `if ( abs(thdiff) <= PI ) exit` (186), `th = th - sign (2., thdiff) * PI` (187), `thdiff = th - th2` (188). `if ( vert(ivert)%atti(VMARKER) == 1 ) then   ! boundary vertex` (193)이면 `eps = PI/360.` (194), `else` (195)는 `eps = 0.` (196)이다. `if ( th > th1-eps .and. th <= th2+eps ) then` (199)이면 `cellfound = .true.` (200)로 발견 표시를 설정한다. 이어 `exit celloop` (201)로 셀 반복을 벗어난다. 셀 루프 종료(204). [10-15 전수 검증 보완] |
| 205–223 | 시작 시 `pointloop: do ip = 1, mip` (132) 안이다. 이 반복은 `enddo pointloop` (249)로 닫힌다. `if ( .not.cellfound ) then` (208)은 `write (msgstr, '(a,f12.4,a,f12.4,a)') ' No triangle containing point (',x(ip)+XOFFS,',',y(ip)+YOFFS,') is found'` (209)로 경고 메시지를 작성한다. `call msgerr( 1, trim(msgstr) )` (210)을 호출한다. 이어 `cycle pointloop` (211)로 다음 점으로 이동한다. `if ( vert(v(1))%active .and. vert(v(2))%active .and. vert(v(3))%active ) then` (216)은 세 꼭짓점 모두 활성일 때만 보간한다. `do k = 1, 3` (220)에서 `xv(k) = xcugrd(v(k))` (221)과 `yv(k) = ycugrd(v(k))` (222)로 좌표를 저장한다. 220행 반복은 `enddo` (223)으로 닫힌다. [10-15 전수 검증 보완] |
| 224–242 | 시작 시 `pointloop: do ip = 1, mip` (132) 안의 `if ( vert(v(1))%active .and. vert(v(2))%active .and. vert(v(3))%active ) then` (216)에 속한다. 216행 조건은 `endif` (247)로 닫힌다. pointloop는 `enddo pointloop` (249)로 닫힌다. `do k = 1, 3` (227)의 `ivc(2) = mod(k  ,3)+1` (228), `ivc(3) = mod(k+1,3)+1` (229), `dxv(k) = xv(ivc(3)) - xv(ivc(2))` (230), `dyv(k) = yv(ivc(3)) - yv(ivc(2))` (231)로 맞은편 변의 좌표 차를 계산한다. `do k = 1, 3` (236)에서 `ivc(1) = k` (237), `ivc(2) = mod(k  ,3)+1` (238), `ivc(3) = mod(k+1,3)+1` (239), `ww(k) = ((x(ip) - xv(ivc(3))) * dyv(ivc(1)) - (y(ip) - yv(ivc(3))) * dxv(ivc(1))) / ( dxv(ivc(2)) * dyv(ivc(1)) - dyv(ivc(2)) * dxv(ivc(1)) )` (240)로 가중치를 구한다. [10-15 전수 검증 보완] |
| 243–251 | 시작 시 `pointloop: do ip = 1, mip` (132) 안의 `if ( vert(v(1))%active .and. vert(v(2))%active .and. vert(v(3))%active ) then` (216)에 속한다. 216행 조건은 `endif` (247)로 닫힌다. pointloop는 `enddo pointloop` (249)로 닫힌다. `foutp(ip) = sum (ww(:) * finp(v(:)))` (245)로 가중합을 출력한다. 활성 분기·점 루프·루틴 종료와 빈 주석(247–251). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 69–70·116–118: finp 길이는 nverts, foutp 길이는 mip이다. 전체 복사 조건은 mip==nvertsg를 검사한다.
- 91: sumww는 선언 이후 사용하지 않는다.
- 216–245: 보간 조건은 세 꼭짓점의 active를 검사한다. finp의 예외값 여부와 가중치 분모 0 여부를 검사하는 조건은 이 블록에 없다.
