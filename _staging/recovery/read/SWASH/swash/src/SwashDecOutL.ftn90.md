---
file: models/SWASH/raw/source_code/swash/src/SwashDecOutL.ftn90
lines: 212
sha256: 562f77e45a1ff0602b1668b1e282617a709fd8131bc91162ea044a3e8adf41c5
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashDecOutL.ftn90 — 판독 구간 기록

구간은 1행부터 212행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | `SwashDecOutL ( opi, opr, psname, pstype, mip, mxk, myk )` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2010년 신설·출력점 집합(output point set) 해석 목적(30–40). ocpcomm4·SwashCommdata1·SwashCommdata4·outp_data 사용(44–47), implicit none(49). |
| 51–83 | 시작 시 1행 루틴 안. mip는 intent(inout), mxk/myk는 intent(out), opi(2)·opr(5)·psname(8자)·pstype(1자)는 입력이다(53–59). `integer, save                     :: ient = 0 ! number of entries in this subroutine` (63), 좌표 범위 실수와 실수 비교 함수 EQREAL 선언(65–74). 구조·소스 구분 주석(76–81). `if (ltrace) call strace (ient,'SwashDecOutL')` (82). |
| 84–91 | 시작 시 1행 루틴 안. 기본 회전 계수: `alpq  = 0.` (84), `cospq = 1.` (85), `sinpq = 0.` (86), `alcq  = 0.` (88), `coscq = cos(alcq)` (89), `sincq = sin(alcq)` (90). |
| 92–117 | 시작 시 1행 루틴 안. `if ( pstype == 'F' ) then` (92)은 `mxk = opi(1)` (94)과 `myk = opi(2)` (95)를 설정한다. `mip = mxk * myk` (96), `xpq   = opr(1)` (98)과 `ypq   = opr(2)` (99)를 설정한다. `alpq  = opr(5)` (100)를 설정한다. `cospq = cos(alpq)` (101), `sinpq = sin(alpq)` (102), `xqp = -xpq * cospq - ypq * sinpq` (104), `yqp =  xpq * sinpq - ypq * cospq` (105). `if ( EQREAL(outpar(2),1.) ) then` (107)은 프레임 좌표계(frame coordinate system) 기준 방향으로 `alcq = -alpq` (109). `else` (110)는 기본 사용자좌표계(user coordinate system)로 `alcq = 0.` (112). `coscq = cos(alcq)` (115), `sincq = sin(alcq)` (116). [10-15 전수 검증 보완] |
| 118–128 | 시작 시 1행 루틴·92행 `if ( pstype == 'F' ) then`의 참 분기 안. `if ( mxk > 1 ) then` (118)은 `dxk = opr(3) / float(mxk-1)` (119), `else` (120)는 `dxk = 0.` (121). `if ( myk > 1 ) then` (123)은 `dyk = opr(4) / float(myk-1)` (124), `else` (125)는 `dyk = 0.` (126). [10-15 전수 검증 보완] |
| 129–158 | 시작 시 1행 루틴·92행 `if ( pstype == 'F' ) then`으로 시작한 분기 사슬 안. `else if ( pstype == 'H' ) then` (129)은 `mxk  = opi(1)` (131)과 `myk  = opi(2)` (132)를 설정한다. `mip  = mxk * myk` (133), `alpq  = opr(5)` (135), `cospq = cos(alpq)` (136), `sinpq = sin(alpq)` (137), `xcmax = opr(1)` (139)과 `ycmax = opr(2)` (140)를 설정한다. `xcmin = opr(3)` (141)과 `ycmin = opr(4)` (142)를 설정한다. 범위 초기값: `xpmin =  1.e09` (144), `ypmin =  1.e09` (145), `xpmax = -1.e09` (146), `ypmax = -1.e09` (147). `xpq = xpmin` (149)과 `ypq = ypmin` (150)을 설정한다. `xqp = -xpq` (152), `yqp = -ypq` (153), `alcq  = 0.` (155), `coscq = cos(alcq)` (156), `sincq = sin(alcq)` (157). [10-15 전수 검증 보완] |
| 159–174 | 시작 시 1행 루틴·129행 `else if ( pstype == 'H' ) then` 분기 안. `if ( mxk > 1 ) then` (159)은 `dxk = ( xpmax - xpmin ) / float(mxk-1)` (160), `else` (161)는 `dxk = 0.` (162). `if ( myk > 1 ) then` (164)은 `dyk = ( ypmax - ypmin ) / float(myk-1)` (165), `else` (166)는 `dyk = 0.` (167). `if ( IOUTES >= 20 ) then` (170)은 프레임 계수 출력(171), `if ( pstype == 'H' ) write (PRINTF, 202) xcmin, xcmax, ycmin, ycmax, xpmax, xpmin` (172)으로 좌표 범위를 출력한다. 170행 조건은 173행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 175–195 | 시작 시 1행 루틴·92행 `if ( pstype == 'F' ) then`으로 시작한 분기 사슬 안. `else if (pstype == 'C' .or. pstype == 'P' ) then` (175)은 `mxk = 0` (177)과 `myk = 0` (178)을 설정한다. `else if ( pstype == 'N' ) then` (180)도 `mxk = 0` (182)과 `myk = 0` (183)을 설정한다. `else if ( pstype == 'U' ) then` (185)은 `mxk = mip` (187)과 `myk = 1` (188)을 설정한다. `else` (190)는 `write (PRTEST, '(a)') ' error SwashDecOutL: no pstype defined'` (192)를 실행한다. 출력점 종류 분기 종료(194). [10-15 전수 검증 보완] |
| 196–206 | 시작 시 1행 루틴 안. `if ( psname == 'COMPGRID' ) then` (196)은 `lcompgrd = .true.` (197)를 설정한다. `else` (198)는 `lcompgrd = .false.` (199)를 설정한다. `if ( ITEST >= 100 .or. IOUTES >= 30 ) then` (202)은 이름·종류·점 수 출력(203), `if ( pstype == 'F' .or. pstype == 'H' ) write (PRTEST, 204) mxk, myk, alpq, dxk, dyk` (204)으로 프레임 크기·각도·간격 출력. [10-15 전수 검증 보완] |
| 207–212 | 시작 시 1행 루틴 안. 프레임 계수·좌표 범위·출력 집합·프레임 크기에 대한 format 201–204(207–210), 구분 주석(211), 루틴 종료(212). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 144–167: H 경로는 xpmin/ypmin=1.e09와 xpmax/ypmax=-1.e09를 설정한 뒤 바로 dxk/dyk를 계산한다. 이 루틴에는 이 네 지역변수의 실제 좌표 최솟값·최댓값을 구하는 대입이 없다.
- 54–55·190–194: mxk/myk는 intent(out)이다. 정의되지 않은 pstype의 else는 오류 문구만 출력하며 mxk/myk에 값을 대입하지 않는다.
- 118–126·159–167·175–194: dxk/dyk는 F와 H 경로에서만 대입한다. C/P/N/U 경로에서는 mxk/myk만 대입하며 이 루틴에서 dxk/dyk를 다시 초기화하지 않는다.
