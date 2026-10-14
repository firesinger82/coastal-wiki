---
file: models/SWASH/raw/source_code/swash/src/SwashUDryWet.ftn90
lines: 124
sha256: 5c95a2c8d2f7615c5c0e0fe2261b1bc35e6b3946bcd7b04b3a728f7a157f8aad
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUDryWet.ftn90 — 판독 구간 기록

구간은 1행부터 124행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | SwashUDryWet를 시작한다(1). 기관·저작권·GPL 3 이상·무보증 머리말(3–27). Marcel Zijlema의 2020년 2월 신규 루틴이다(30–36). 삼각형 격자(triangular mesh)의 셀과 면에서 젖음·마름(wetting and drying)을 검사하고 마스크 배열(mask array)을 갱신한다는 주석이다(38–44). |
| 48–72 | 시작 시 1행 SwashUDryWet 루틴 안. ocpcomm4·SwashCommdata3·SwashFlowdata·SwanGriddata·SwanGridobjects를 사용한다(48–52). ient는 save 정수로 0 초기화한다(58). 셀·면·면 순회 인덱스와 ival을 선언한다(59–62). cell·face 자료구조 포인터와 구조·소스 구분 주석이다(64–72). 원문: `integer, save :: ient = 0` (58). [10-15 전수 검증 보완] |
| 73–95 | 시작 시 1행 루틴 안. ltrace이면 strace를 호출하고 cell·face 포인터를 gridobject에 연결한다(73–78). 모든 면을 순회하여 hu(iface)>epshu이면 wetu=1, else이면 wetu=0으로 설정한다(82–94). 원문: `if (ltrace) call strace (ient,'SwashUDryWet')` (73). `cell => gridobject%cell_grid` (77). `face => gridobject%face_grid` (78). `do iface = 1, nfaces` (82). `if ( hu(iface) > epshu ) then` (84). `wetu(iface) = 1` (86). `else` (88). `wetu(iface) = 0` (90). |
| 96–124 | 시작 시 1행 루틴 안이며 면 루프 밖. 모든 셀에서 ival=1로 시작하여 셀의 모든 면 FACEID를 얻는다(98–106). 각 면의 1−wetu를 ival에 곱한다(108). ival=0이면 wets=1, else이면 wets=0으로 저장한다(112–120). 앞 면 루프가 정한 0/1 마스크 기준으로 하나라도 젖은 면이 있으면 셀을 젖은 상태로 표시한다. 셀 루프와 루틴을 닫는다(122–124). 원문: `do icell = 1, ncells` (98). `ival = 1` (100). `do jf = 1, cell(icell)%nof` (102). `iface = cell(icell)%face(jf)%atti(FACEID)` (106). `ival = ival * ( 1 - wetu(iface) )` (108). `if ( ival == 0 ) then` (112). `wets(icell) = 1` (114). `else` (116). `wets(icell) = 0` (118). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65·78: face 포인터는 선언하고 gridobject%face_grid에 연결하지만 이후 이 루틴에서 참조하지 않는다. 셀의 면 주소는 cell 포인터를 통해 얻는다(106).
- 98–120: 셀 젖음 여부는 `ival = 1` (100)에서 시작한 `ival = ival * ( 1 - wetu(iface) )` (108)의 반복 곱과 `if ( ival == 0 ) then` (112)으로 정한다. 이 셀 판정 블록은 셀 수심 hs를 참조하지 않는다. [10-15 전수 검증 정정]
