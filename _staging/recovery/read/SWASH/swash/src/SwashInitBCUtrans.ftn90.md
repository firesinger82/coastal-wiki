---
file: models/SWASH/raw/source_code/swash/src/SwashInitBCUtrans.ftn90
lines: 182
sha256: c8c296b881e6621a2fa84348aab402e3a899169d3a17a7e8286edc613d0ffe2a
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashInitBCUtrans.ftn90 — 판독 구간 기록

구간은 1행부터 182행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–72 | `SwashInitBCUtrans` 시작(1). 기관·GPL 3 이상·무보증 머리말(2–28), 저자와 2023년 신설 주석(30–36). 목적은 비정형 격자(unstructured grid)의 입력 성분을 초기화하고 디리클레 경계조건(Dirichlet boundary condition)을 저장하는 것(38–40). ocpcomm4·SwashCommdata3·m_genarr·SwashFlowdata·SwanGriddata·SwanGridobjects·SwanCompdata 사용(44–50), implicit none(52). 셀·면·꼭짓점 인덱스와 셀/면 포인터 선언(56–65). 추적 횟수 초기값 `integer, save                         :: ient = 0 ! number of entries in this subroutine` (57). 구조·원문 안내 주석 포함. |
| 73–79 | 시작 시 1행 SwashInitBCUtrans 루틴 안. 추적 조건과 호출 `if (ltrace) call strace (ient,'SwashInitBCUtrans')` (73). cell·face는 gridobject의 cell_grid·face_grid를 가리킨다(77–78). 대입문·반복문 원문은 `cell => gridobject%cell_grid`(77), `face => gridobject%face_grid`(78)이다. [10-15 전수 검증 보완] |
| 80–113 | 시작 시 1행 SwashInitBCUtrans 루틴 안. 염도(salinity) 분기 `if ( lsal > 0 ) then` (80). icell=1..ncells 루프(84)는 CELLV1–3 꼭짓점을 얻고(88–90), 셀 중심(centroid) 염도 `rp(icell,:,lsal) = ( salf(v(1),:) + salf(v(2),:) + salf(v(3),:) ) / 3.` (92)를 계산한다. jf=1..nfacesb 루프(98)는 jbface와 FACEV1/2를 얻고(100·104–105), 경계면 평균 `cbndu(jf,:,lsal) = 0.5 * ( salf(vf1,:) + salf(vf2,:) )` (107)을 계산한다. bcrp에 cbndu를 복사(108). 두 루프와 염도 분기 종료(94·110·112). 대입문·반복문 원문은 `do icell = 1, ncells`(84), `v(1) = cell(icell)%atti(CELLV1)`(88), `v(2) = cell(icell)%atti(CELLV2)`(89), `v(3) = cell(icell)%atti(CELLV3)`(90), `do jf = 1, nfacesb`(98), `iface = jbface(jf)`(100), `vf1 = face(iface)%atti(FACEV1)`(104), `vf2 = face(iface)%atti(FACEV2)`(105)이다. `if ( lsal > 0 ) then`(80)은 ELSE 없이 `endif`(112)에서 닫히는 독립 분기이다. 대입문·반복문 원문은 `bcrp (jf,:,lsal) = cbndu(jf,:,lsal)`(108)이다. [10-15 전수 검증 보완] |
| 114–147 | 시작 시 1행 SwashInitBCUtrans 루틴 안. 수온(temperature) 분기 `if ( ltemp > 0 ) then` (114). icell=1..ncells 루프(118)는 세 꼭짓점을 얻고(122–124), 셀 중심 수온 `rp(icell,:,ltemp) = ( tempf(v(1),:) + tempf(v(2),:) + tempf(v(3),:) ) / 3.` (126)을 계산한다. jf=1..nfacesb 루프(132)는 jbface·면 끝점 인덱스를 얻고(134·138–139), 경계 수온 `cbndu(jf,:,ltemp) = 0.5 * ( tempf(vf1,:) + tempf(vf2,:) )` (141)을 계산한 뒤 bcrp에 복사(142). 루프·분기 종료(128·144·146). 대입문·반복문 원문은 `do icell = 1, ncells`(118), `v(1) = cell(icell)%atti(CELLV1)`(122), `v(2) = cell(icell)%atti(CELLV2)`(123), `v(3) = cell(icell)%atti(CELLV3)`(124), `do jf = 1, nfacesb`(132), `iface = jbface(jf)`(134), `vf1 = face(iface)%atti(FACEV1)`(138), `vf2 = face(iface)%atti(FACEV2)`(139)이다. `if ( ltemp > 0 ) then`(114)은 ELSE 없이 `endif`(146)에서 닫히는 독립 분기이다. 대입문·반복문 원문은 `bcrp (jf,:,ltemp) = cbndu(jf,:,ltemp)`(142)이다. [10-15 전수 검증 보완] |
| 148–182 | 시작 시 1행 SwashInitBCUtrans 루틴 안. 퇴적물(sediment) 분기 `if ( lsed > 0 ) then` (148). icell=1..ncells 루프(152)는 세 꼭짓점 입력에서 `rp(icell,:,lsed) = ( sedf(v(1),:) + sedf(v(2),:) + sedf(v(3),:) ) / 3. / rhos` (160)으로 체적 퇴적물(volumetric sediment)을 계산한다. jf=1..nfacesb 루프(166)는 면 끝점에서 `cbndu(jf,:,lsed) = 0.5 * ( sedf(vf1,:) + sedf(vf2,:) ) / rhos` (175)를 계산하고 bcrp에 복사(176). 루프·분기 종료(162·178·180). 주석과 루틴 종료(181–182). 대입문·반복문 원문은 `do icell = 1, ncells`(152), `v(1) = cell(icell)%atti(CELLV1)`(156), `v(2) = cell(icell)%atti(CELLV2)`(157), `v(3) = cell(icell)%atti(CELLV3)`(158), `do jf = 1, nfacesb`(166), `iface = jbface(jf)`(168), `vf1 = face(iface)%atti(FACEV1)`(172), `vf2 = face(iface)%atti(FACEV2)`(173)이다. `if ( lsed > 0 ) then`(148)은 ELSE 없이 `endif`(180)에서 닫히는 독립 분기이다. 대입문·반복문 원문은 `bcrp (jf,:,lsed) = cbndu(jf,:,lsed)`(176)이다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60·88–92·122–126·156–160: 꼭짓점 배열 v의 크기는 3으로 고정되어 있다. 모든 셀 중심 평균식은 세 꼭짓점 합을 3.으로 나눈다.
- 160·175: 퇴적물의 셀 중심값과 경계값은 모두 rhos로 나눈다. 이 루틴에는 rhos의 값이나 0 여부를 검사하는 조건이 없다.
