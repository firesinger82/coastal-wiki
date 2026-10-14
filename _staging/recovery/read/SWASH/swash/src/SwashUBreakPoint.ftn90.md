---
file: models/SWASH/raw/source_code/swash/src/SwashUBreakPoint.ftn90
lines: 170
sha256: 6daa76881a3eee4b1ffe0d5fc6cf61f7db5bdaefc097100487dc08a4b07ef82d
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUBreakPoint.ftn90 — 판독 구간 기록

구간은 1행부터 170행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | SwashUBreakPoint를 시작한다(1). 기관·저작권·GPL 3 이상·무보증 머리말(3–27). Marcel Zijlema의 2020년 3월 신규 루틴이다(30–36). 비구조 격자(unstructured mesh)의 급경사 단파형 전면(bore-like wave front) 셀을 찾아 쇄파(wave breaking) 처리한다는 주석이다(38–40). 자유수면의 수직속도가 위상속도(phase speed)의 일부를 넘는 셀에 정수압(hydrostatic pressure)을 적용한다는 설명이다(44–46). 주석은 해당 셀의 마스크 배열을 갱신한다고 적는다(44–45). 주석은 쇄파 전면에서 정수압 가정을 유지한다고 적는다(45–46). 운동량 보존(momentum conservation)과 결합한 에너지 소산(energy dissipation), 비대칭성(asymmetry)·왜도(skewness) 보존을 주석에 적는다(48–50). [10-15 전수 검증 보완] |
| 54–86 | 시작 시 1행 SwashUBreakPoint 루틴 안. ocpcomm4·SwashCommdata3·dt·iwrk·SwashFlowdata·SwanGriddata·SwanGridobjects를 사용한다(54–60). 셀·이웃 셀·면·면 순회 인덱스와 ient=0 save를 선언한다(66–71). alpha는 쇄파 개시 임계계수(threshold parameter), beta는 쇄파 이후 영역의 재개 임계계수, dsdt는 수면 수직속도, rootgh는 천해 파속(shallow water celerity)이다(73–76). cell·face 포인터와 구조·소스 주석을 포함한다(78–86). 원문: `integer, save :: ient = 0` (69). [10-15 전수 검증 보완] |
| 87–118 | 시작 시 1행 루틴 안. ltrace이면 strace를 호출하고 cell·face 포인터를 연결한다(87–92). alpha·beta를 psurf(1/2)에서 가져오고 기존 brks를 iwrk(:,1)에 복사한다(94–99). 셀마다 wets=1일 때 sqrt(grav*hs)와 (s1−s0)/dt를 계산한다(101–107). dsdt>alpha*rootgh이면 brks=1로 놓고 전 수직 q를 0으로 설정한다(109–113). else if dsdt>beta*rootgh는 이웃 셀 탐색 분기를 연다(115). 원문: `if (ltrace) call strace (ient,'SwashUBreakPoint')` (87). `cell => gridobject%cell_grid` (91). `face => gridobject%face_grid` (92). `alpha = psurf(1)` (94). `beta  = psurf(2)` (95). `iwrk(:,1) = brks(:)` (99). `do icell = 1, ncells` (101). `if ( wets(icell) == 1 ) then` (103). `rootgh = sqrt( grav * hs(icell) )` (105). `dsdt = ( s1(icell) - s0(icell) ) / dt` (107). `if ( dsdt > alpha * rootgh ) then` (109). `brks(icell) = 1` (111). `q(icell,:) = 0.` (113). `else if ( dsdt > beta * rootgh ) then` (115). |
| 119–143 | 시작 시 101행 `do icell = 1, ncells` 안이며 이 루프는 `enddo` (160)에서 닫힌다. 103행 `if ( wets(icell) == 1 ) then` 참 분기 안이며 이 조건은 `endif` (158)에서 닫힌다. 109행 `if ( dsdt > alpha * rootgh ) then`이 거짓인 뒤 115행 `else if ( dsdt > beta * rootgh ) then` 참 분기 안이다. 이 분기 사슬은 `endif` (152)에서 닫힌다. 셀의 모든 면에서 FACEID와 FACEC1·FACEC2를 가져온다(119–128). icell2/=0이고 현재 셀 반대편 이웃의 iwrk(:,1)=1이면 brks=1, 전 수직 q=0을 대입한다(130–138). 132행 이웃 조건은 `endif` (138)에서 닫힌다. 130행 조건은 `endif` (140)에서 닫힌다. 면 루프는 `enddo` (142)에서 닫힌다. 130·132행 조건에는 ELSE가 없다. 판단에는 현재 갱신 중 brks가 아닌 99행의 복사본을 사용한다. 원문: `do jf = 1, cell(icell)%nof` (119). `iface = cell(icell)%face(jf)%atti(FACEID)` (123). `icell1 = face(iface)%atti(FACEC1)` (127). `icell2 = face(iface)%atti(FACEC2)` (128). `if ( icell2 /= 0 ) then` (130). `if ( (icell == icell1 .and. iwrk(icell2,1) == 1) .or. (icell == icell2 .and. iwrk(icell1,1) == 1) ) then` (132). `brks(icell) = 1` (134). `q(icell,:) = 0.` (136). [10-15 전수 검증 보완] |
| 144–161 | 시작 시 101행 `do icell = 1, ncells` 안이며 이 루프는 `enddo` (160)에서 닫힌다. 103행 `if ( wets(icell) == 1 ) then` 참 분기 안이며 이 조건은 `endif` (158)에서 닫힌다. 109행 `if ( dsdt > alpha * rootgh ) then`과 115행 `else if ( dsdt > beta * rootgh ) then`이 모두 거짓이면 144행 ELSE IF 조건을 검사한다. else if dsdt>0 및 brks=1이면 q만 0으로 설정한다(144–146). 148행 else는 brks=0을 대입한다(150). dsdt 분기 사슬을 `endif` (152)에서 닫은 뒤 154행 else는 wets/=1 셀의 brks를 0으로 설정한다(156). 젖음 조건과 셀 루프를 닫는다(158–160). 원문: `else if ( dsdt > 0. .and. brks(icell) == 1 ) then` (144). `q(icell,:) = 0.` (146). `else` (148). `brks(icell) = 0` (150). `else` (154). `brks(icell) = 0` (156). [10-15 전수 검증 보완] |
| 162–170 | 시작 시 1행 루틴 안이며 첫 셀 루프 밖. 쇄파 지점을 고려하여 셀의 젖음·마름(wetting and drying) 마스크(mask)를 다시 갱신한다는 주석이다(162). 모든 셀에서 wets=1 및 brks=1이면 wets=0으로 바꾼다(164–168). 루틴을 종료한다(170). 원문: `do icell = 1, ncells` (164). `if ( wets(icell) == 1 .and. brks(icell) == 1 ) wets(icell) = 0` (166). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 99·115–142: beta 초과 분기의 이웃 쇄파 검사는 iwrk에 복사한 호출 시작 시 brks를 사용한다. 이 분기에는 이웃 조건을 만족하지 않을 때 현재 brks나 q를 새 값으로 설정하는 else가 없다.
- 105–107: rootgh는 hs의 제곱근을 사용하고 dsdt는 dt로 나눈다. 이 루틴에는 hs의 비음수 검사와 dt의 비영 검사가 없다.
- 113·136·146·166: 쇄파 처리 셀의 q를 0으로 설정한다. 마지막 셀 루프는 wets=1 및 brks=1인 셀의 wets를 0으로 바꾼다. 이 루틴은 그 단계에서 wetu를 갱신하지 않는다.
