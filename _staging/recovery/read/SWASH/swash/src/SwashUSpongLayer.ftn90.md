---
file: models/SWASH/raw/source_code/swash/src/SwashUSpongLayer.ftn90
lines: 232
sha256: 27d6562472aaf1c3506d84ea0b0674214a98c79025783e5939f825a580d6d27f
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUSpongLayer.ftn90 — 판독 구간 기록

구간은 1행부터 232행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | `SwashUSpongLayer` 시작(1). 기관·개발팀·SWASH·2010–2026 저작권·GPL 3 이상·무보증 머리말(3–27). 저자·2020년 5월 신규 이력(30–36). 비구조 격자(unstructured mesh)에서 흡수층(sponge layer)의 흐름 변수 감쇠함수를 정한다는 목적(40). Mayer 등의 1998년 논문 식 43·44 사용 설명과 문헌(44–48). |
| 50–98 | 시작 시 1행 `SwashUSpongLayer` 안. vmspon/wdspon·통신·흐름·격자 모듈을 가져온다(52–58). 고정 이완 증가율은 `real, parameter :: grt = 0.5  ! growth rate of relaxation` (64). 경계/현재 셀·면, 세 꼭짓점 v와 두 경계 꼭짓점 vb, 경계 표지(boundary marker) vm, 거리·정규화 거리·흡수층 폭·좌표와 객체 포인터를 선언한다(68–91). 초기 선언은 `integer, save         :: ient = 0` (72)이다. 구조·소스 구분 주석(93–98). [10-15 전수 검증 보완] |
| 99–144 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashUSpongLayer')` (99). 셀·면 객체 연결(103–104). `do i = 1, nspl` (106)에서 vm=vmspon(i), width=wdspon(i)(108–109). `do iface = 1, nfaces` (111)에서 면 중점 좌표를 얻고(113–114) `dmin = 100.*max(xclen,yclen)` (116). 경계 면 루프(118)에서 jbface의 면 번호와 두 꼭짓점을 얻는다(120–125). `if ( vmark(vb(1)) == vm .and. vmark(vb(2)) == vm ) then` (129)이면 경계 면 중점 좌표를 얻고(131–132) `dist = sqrt ( ( x - xb )**2 + ( y - yb )**2 )` (134). `if ( dist < dmin ) then` (136)은 최소 거리와 bface를 갱신한다(137–138). 경계 면 루프 종료(143). 경계 선택 값은 `vm    = vmspon(i)` (108)과 `width = wdspon(i)` (109)이다. 경계 면 반복은 `do jb = 1, nfacesb` (118)이다. 최소 거리 갱신은 `dmin  = dist` (137)이다. 경계 면 저장은 `bface = j` (138)이다. 136행 조건은 139행 `endif`에서 닫힌다. 129행 조건은 141행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 145–164 | 시작 시 106행 `do i = 1, nspl`과 111행 `do iface = 1, nfaces` 안이다. 111행 루프는 163행 `enddo`에서 닫힌다. 106행 루프는 230행 `enddo`에서 닫힌다. `if ( .not. dmin > width ) then` (145)에서 `dnb = 1. - dmin / width` (147). `if ( dnb > 0. ) then` (149)은 `sponu(iface,i)%gamma = grt * dnb**3 + (1.-grt) * dnb**6` (151), bface 저장(152). else(154)는 gamma=0·bface=1(156–157). 조건과 현재 면 루프 종료(159–163). 경계 번호 저장은 `sponu(iface,i)%bface = bface` (152)이다. 154행 `else`의 기본값은 `sponu(iface,i)%gamma = 0.` (156)과 `sponu(iface,i)%bface = 1` (157)이다. 149행 조건은 159행 `endif`에서 닫힌다. 145행 조건에는 ELSE가 없으며 161행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 165–193 | 시작 시 106행 `do i = 1, nspl` 안이다. 이 루프는 230행 `enddo`에서 닫힌다. `do icell = 1, ncells` (165)에서 셀 중심 좌표를 얻고(167–168) `dmin = 100.*max(xclen,yclen)` (170). `do jb = 1, ncellsb` (172)에서 jbcell의 셀 번호와 세 꼭짓점을 얻는다(174–180). `do k = 1, 3` (184)의 `if ( vmark(v(k)) == 0 ) then` (185)은 `vb(1) = v(mod(k  ,3)+1)` (186), `vb(2) = v(mod(k+1,3)+1)` (187), exit(188)로 두 경계 꼭짓점을 선택한다. 경계 표지 검사 주석(192). 185행 조건은 189행 `endif`에서 닫힌다. 184행 꼭짓점 루프는 190행 `enddo`에서 닫힌다. 172행 경계 셀 루프는 208행 `enddo`에서 닫힌다. 165행 셀 루프는 228행 `enddo`에서 닫힌다. [10-15 전수 검증 보완] |
| 194–209 | 시작 시 106행 `do i = 1, nspl`과 165행 `do icell = 1, ncells` 및 172행 `do jb = 1, ncellsb` 안이다. 이 루프들은 각각 230·228·208행 `enddo`에서 닫힌다. `if ( vmark(vb(1)) == vm .and. vmark(vb(2)) == vm ) then` (194)이면 경계 셀 중심 좌표를 얻는다(196–197). `dist = sqrt ( ( x - xb )**2 + ( y - yb )**2 )` (199). `if ( dist < dmin ) then` (201)은 `dmin  = dist` (202)와 `bcell = j` (203). 표지 조건과 경계 셀 루프를 닫는다(206–208). 201행 조건은 204행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 210–232 | 시작 시 106행 `do i = 1, nspl`과 165행 `do icell = 1, ncells` 안이다. 이 루프들은 각각 230·228행 `enddo`에서 닫힌다. `if ( .not. dmin > width ) then` (210)에서 `dnb = 1. - dmin / width` (212). `if ( dnb > 0. ) then` (214)은 `spons(icell,i)%gamma = grt * dnb**3 + (1.-grt) * dnb**6` (216), bcell 저장(217). else(219)는 gamma=0·bcell=1(221–222). 조건·셀 루프·흡수층 루프 종료(224–230). 루틴 종료(232). 경계 번호 저장은 `spons(icell,i)%bcell = bcell` (217)이다. 219행 `else`의 기본값은 `spons(icell,i)%gamma = 0.` (221)과 `spons(icell,i)%bcell = 1` (222)이다. 214행 조건은 224행 `endif`에서 닫힌다. 210행 조건에는 ELSE가 없으며 226행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 109·145–147·210–212: width를 wdspon(i)에서 복사한다. dmin/width 계산 앞에는 width의 양수 여부를 검사하는 조건이 없다.
- 145–161·210–226: dmin>width인 경로에는 sponu/spons의 gamma나 경계 번호 대입이 없다. 이 루틴에는 두 배열 전체 초기화문이 없다.
- 184–194: 경계 셀의 vb 선택은 vmark(v(k))=0인 꼭짓점을 찾았을 때만 수행한다. 세 꼭짓점 모두 이 조건을 만족하지 않을 때 vb를 설정하는 문장은 이 경계 셀 반복 안에 없다.
- 68–69·116·136–138·152·170·201–203·217: bface/bcell 선언에는 초기값이 없다. 두 변수는 dist<dmin인 경로에서만 설정된다. 감쇠 블록 진입 조건은 `if ( .not. dmin > width ) then`이다(145·210). 이 조건은 경계 검색 성공을 별도로 검사하지 않는다. [10-15 전수 검증 정정]
