---
file: models/SWASH/raw/source_code/swash/src/SwashDryWet.ftn90
lines: 231
sha256: 72076d96508277df63f200ae7919de59cf8cd07b9bead8802c89a84aed65ed83
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashDryWet.ftn90 — 판독 구간 기록

구간은 1행부터 231행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | `SwashDryWet` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 안내(2–29). 저자 Marcel Zijlema, 2010년 3월 신설·2012년 3월 다공성 매질(porous media) 확장 이력(30–37). 수위점과 속도점에서 젖음·마름(wetting and drying)을 검사하고 마스크(mask) 배열을 갱신한다는 주석(39–45). 공통 데이터·격자 배열·유동 모듈 사용과 implicit none(47–54). |
| 55–76 | 시작 시 1행 SwashDryWet 루틴 안. 추적 계수 `integer, save :: ient = 0 ! number of entries in this subroutine` (58). m/n·이웃 인덱스·격자 포인터(pointer), 중단 여부 함수 STPNOW의 logical 형식 선언(59–67). 구조·소스 구분 주석(69–74). `if (ltrace) call strace (ient,'SwashDryWet')` (75). |
| 77–122 | 시작 시 1행 SwashDryWet 루틴 안. `if ( oned ) then` (77)의 1차원 경로. `do m = mf, ml` (81)의 u점 루프에서 `nm = kgrpnt(m,1)` (83)을 설정한다. `if ( hu(nm) > epshu ) then` (85)은 `wetu(nm) = 1` (87)을 설정한다. `else` (89)는 `wetu(nm) = 0` (91)을 설정한다. `call SWEXCHGI ( wetu, kgrpnt, 1, 1 )` (99)로 인접 부분 영역(subdomain)과 교환하고 `if (STPNOW()) return` (100). 수위점의 `do m = mfu, ml` (104)에서 `md = m - 1` (106), `nm  = kgrpnt(m ,1)` (108)을 설정한다. `nmd = kgrpnt(md,1)` (109)는 m-1 인덱스의 포인터이다. `if ( ( 1 - wetu(nm) ) * ( 1 - wetu(nmd) ) == 0 ) then` (111)은 `wets(nm) = 1` (113)을 설정한다. `else` (115)는 `wets(nm) = 0` (117)을 설정한다. 루프 종료·주석(121–122). [10-15 전수 검증 정정] [10-15 전수 검증 보완] |
| 123–157 | 시작 시 1행 SwashDryWet 루틴·77행 `if ( oned ) then` 분기 구조 안. `else` (123)는 2차원 경로이다. `do n = nfu, nl` (127)·`do m = mf, ml` (128)의 u점 루프에서 `nm = kgrpnt(m,n)` (130)을 설정한다. `if ( hu(nm) > epshu ) then` (132)이면 `wetu(nm) = 1` (134)을 설정한다. `else` (136)는 `wetu(nm) = 0` (138)을 설정한다. 루프 종료 후 영구 건조점은 `wetu(1) = 0` (147)으로 설정한다. `call SWEXCHGI ( wetu, kgrpnt, 1, 1 )` (151), `if (STPNOW()) return` (152). 반복 격자(repeating grid)의 해당 경계를 `call periodici ( wetu, kgrpnt, 1, 1 )` (156)로 동기화한다. [10-15 전수 검증 보완] |
| 158–190 | 시작 시 1행 SwashDryWet 루틴·77행 `if ( oned ) then`의 123행 `else` 안. `do m = mfu, ml` (160)·`do n = nf, nl` (161)의 v점 루프에서 `nm = kgrpnt(m,n)` (163)을 설정한다. `if ( hv(nm) > epshu ) then` (165)이면 `wetv(nm) = 1` (167)을 설정한다. `else` (169)는 `wetv(nm) = 0` (171)을 설정한다. 루프 종료 후 영구 건조점은 `wetv(1) = 0` (180)으로 설정한다. `call SWEXCHGI ( wetv, kgrpnt, 1, 1 )` (184), `if (STPNOW()) return` (185), `call periodici ( wetv, kgrpnt, 1, 1 )` (189). [10-15 전수 검증 보완] |
| 191–231 | 시작 시 1행 SwashDryWet 루틴·77행 `if ( oned ) then`의 123행 `else` 안. `do n = nfu, nl` (193)·`do m = mfu, ml` (194)의 수위점 루프에서 `md = m - 1` (196), `nd = n - 1` (197). `nm  = kgrpnt(m ,n )` (199)은 현재 인덱스의 포인터이다. `nmd = kgrpnt(md,n )` (200)은 m-1 인덱스의 포인터이다. `ndm = kgrpnt(m ,nd)` (201)은 n-1 인덱스의 포인터이다. `if ( ( 1 - wetu(nm) ) * ( 1 - wetu(nmd) ) * ( 1 - wetv(nm) ) * ( 1 - wetv(ndm) ) == 0 ) then` (203)이면 `wets(nm) = 1` (205)을 설정한다. `else` (207)는 `wets(nm) = 0` (209)을 설정한다. 루프 종료 후 `wets(1) = 0` (218), `call periodici ( wets, kgrpnt, 1, 1 )` (222). 77행 `if ( oned ) then`의 `endif` (224) 뒤 두 차원 경로 모두 `call SWEXCHGI ( wets, kgrpnt, 1, 1 )` (228), `if (STPNOW()) return` (229). 루틴 종료(231). [10-15 전수 검증 정정] [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 85·132·165: u점 hu와 v점 hv의 젖음 판정은 모두 epshu를 사용한다. 깊이가 epshu와 같은 경우에는 마스크를 0으로 설정한다.
- 77–123·147–156·180–189·218–228: 2차원 경로에는 인덱스 1의 세 마스크를 0으로 만드는 문장과 periodici 호출이 있다. 1차원 경로에는 이 문장들과 periodici 호출이 없다. 수위 마스크의 SWEXCHGI 호출은 oned 분기 밖에 있다.
