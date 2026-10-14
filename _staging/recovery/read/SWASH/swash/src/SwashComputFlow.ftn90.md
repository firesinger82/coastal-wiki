---
file: models/SWASH/raw/source_code/swash/src/SwashComputFlow.ftn90
lines: 198
sha256: b0886c782601ae9948c402860345b14c457dbd4e4ebe1156e89ef92c45b537c0
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashComputFlow.ftn90 — 판독 구간 기록

구간은 1행부터 198행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | `SwashComputFlow` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2010년 신설(30–36). 천수방정식(shallow water equations)으로 수위와 유속을 계산한다는 목적(38–40). 중력파·바닥 전단응력(bottom shear stress)·수직 와점성(vertical eddy viscosity)에 대해 무조건 안정이라는 반음해법(semi-implicit approach) 설명과 양해적 리프프로그법(explicit leap-frog technique) 대안은 방법 주석이다(42–47). 46–47행 주석에서 양해적 처리의 대상은 수위경사와 수심적분 연속방정식이다. [10-15 전수 검증 보완] |
| 49–77 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·m_genarr·outp_data의 lwavoutp/lcuroutp·SwashFlowdata 사용(51–55). `integer, save :: ient = 0 ! number of entries in this subroutine` (61), STPNOW 선언(62). 구조·소스 구분 주석(64–69).`if (ltrace) call strace (ient,'SwashComputFlow')` (70). `if ( oned ) then` (74)로 1차원 경로를 시작한다. |
| 78–101 | 시작 시 1행 루틴·74행 `if ( oned ) then`의 참 분기 안. `if ( kmax == 1 ) then` (78)은 수심평균(depth-averaged) 경로. `if ( mtimei == 1 ) then` (82)은 `call SwashExpDep1DHflow ( u1(1,1), u0(1,1), ua(1,1), up(1,1), qx(1,1), qm(1,1), q(1,1), dq(1,1), gmatu(1,1,1), rho(1,1), ibl(1), ibr(1), kgrpnt(1,1) )` (86), `if (STPNOW()) return` (87). `else if ( mtimei == 2 ) then` (89) 안 `if ( .not.mimetic ) then` (93)은 `call SwashImpDep1DHflow ( u1(1,1), u0(1,1), ua(1,1), up(1,1), qx(1,1), qm(1,1), q(1,1), dq(1,1), gmatu(1,1,1), rho(1,1), ui(1,1), dqgrd(1,1), ibl(1), ibr(1), kgrpnt(1,1) )` (94), `else` (95)는 `call SwashImpDepM1DHflow ( u1(1,1), u0(1,1), qx(1,1), qm(1,1), q(1,1), dq(1,1), gmatu(1,1,1), rho(1,1), ui(1,1), dqgrd(1,1), ibl(1), ibr(1), kgrpnt(1,1) )` (96). 일반 경로에는 ua/up가 포함되고 두 반음해 경로에는 ui/dqgrd가 포함된다(94·96). `if (STPNOW()) return` (98). 93행 조건은 97행에서 닫힌다. 82행 사슬은 최종 `else` 없이 100행에서 닫힌다. [10-15 전수 검증 보완] |
| 102–133 | 시작 시 1행 루틴·74행 `if ( oned ) then`의 참 분기·78행 `if ( kmax == 1 ) then` 안. `else` (102)는 고정 층수의 층평균(layer-averaged) 경로. `if ( mtimei == 1 ) then` (106) 안 `if ( .not.lsubg ) then` (110)은 `call SwashExpLay1DHflow  ( ibl(1), ibr(1), kgrpnt(1,1) )` (111), `else` (112)는 `call SwashExpLayP1DHflow ( ibl(1), ibr(1), kgrpnt(1,1) )` (113), `if (STPNOW()) return` (115). `else if ( mtimei == 2 ) then` (117) 안 `if ( mimetic ) then` (121)은 `call SwashImpLayM1DHflow ( ibl(1), ibr(1), kgrpnt(1,1) )` (122), `else if ( lsubg ) then` (123)은 `call SwashImpLayP1DHflow ( ibl(1), ibr(1), kgrpnt(1,1) )` (124), `else` (125)는 `call SwashImpLay1DHflow ( ibl(1), ibr(1), kgrpnt(1,1) )` (126); 세 호출의 인수는 ibl(1)·ibr(1)·kgrpnt(1,1)이다. `if (STPNOW()) return` (128). 110행 조건은 114행에서 닫힌다. 121행 사슬은 127행에서 닫힌다. 106행 사슬은 최종 `else` 없이 130행에서 닫힌다. 78행 조건은 132행에서 닫힌다. [10-15 전수 검증 보완] |
| 134–161 | 시작 시 1행 루틴·74행 `if ( oned ) then` 안에서 `else` (134)로 2차원 경로. `if ( kmax == 1 ) then` (138), `if ( mtimei == 1 ) then` (142)은 `call SwashExpDep2DHflow ( u1(1,1), u0(1,1), ua(1,1), ua2(1,1), up(1,1), qx(1,1), qxm(1,1), v1(1,1), v0(1,1), qy(1,1), qym(1,1), q(1,1), dq(1,1), gmatu(1,1,1), gmatv(1,1,1), rho(1,1) )` (146), `if (STPNOW()) return` (147). `else if ( mtimei == 2 ) then` (149) 안 `if ( .not.mimetic ) then` (153)은 `call SwashImpDep2DHflow ( u1(1,1), u0(1,1), ua(1,1), ua2(1,1), up(1,1), qx(1,1), qxm(1,1), v1(1,1), v0(1,1), qy(1,1), qym(1,1), q(1,1), dq(1,1), gmatu(1,1,1), gmatv(1,1,1), rho(1,1), ui(1,1), dqgrdu(1,1), vi(1,1), dqgrdv(1,1) )` (154), `else` (155)는 `call SwashImpDepM2DHflow ( u1(1,1), u0(1,1), qx(1,1), qxm(1,1), v1(1,1), v0(1,1), qy(1,1), qym(1,1), q(1,1), dq(1,1), gmatu(1,1,1), gmatv(1,1,1), rho(1,1), ui(1,1), dqgrdu(1,1), vi(1,1), dqgrdv(1,1) )` (156). 두 반음해 호출에는 ui(1,1)·dqgrdu(1,1)·vi(1,1)·dqgrdv(1,1)가 포함된다(154·156). `if (STPNOW()) return` (158). 153행 조건은 157행에서 닫힌다. 142행 사슬은 최종 `else` 없이 160행에서 닫힌다. [10-15 전수 검증 정정] [10-15 전수 검증 보완] |
| 162–193 | 시작 시 1행 루틴·74행 `if ( oned ) then`의 `else` (134)·138행 `if ( kmax == 1 ) then` 안. `else` (162)는 고정 층수의 층평균 경로. `if ( mtimei == 1 ) then` (166) 안 `if ( .not.lsubg ) then` (170)은 `call SwashExpLay2DHflow` (171), `else` (172)는 `call SwashExpLayP2DHflow` (173), `if (STPNOW()) return` (175). `else if ( mtimei == 2 ) then` (177) 안 `if ( .not.lsubg ) then` (181)은 `call SwashImpLay2DHflow` (182), `else` (183)는 `call SwashImpLayP2DHflow` (184), `if (STPNOW()) return` (186). 170행 조건은 174행에서 닫힌다. 181행 조건은 185행에서 닫힌다. 166행 사슬은 최종 `else` 없이 188행에서 닫힌다. 138행 조건은 190행에서 닫힌다. 74행 조건은 192행에서 닫힌다. [10-15 전수 검증 보완] |
| 194–198 | 시작 시 1행 루틴 안. 출력용 평균 수위 상승(wave setup)·파고·평균 흐름 갱신 주석(194–195). `if ( lwavoutp .or. lcuroutp ) call SwashAverOutp ( 1 )` (196). 루틴 종료(198). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 82–100·106–130·142–160·166–188·196: 네 시간적분 분기는 모두 mtimei=1/2만 처리하며 마지막 else가 없다. 출력 평균 호출은 이 분기들 밖에 있다.
- 121–126·181–184: 1차원 다층 반음해 경로는 mimetic을 먼저 검사하고 lsubg를 다음으로 검사한다. 2차원 다층 반음해 경로에는 lsubg 검사만 있다.
