---
file: models/SWASH/raw/source_code/swash/src/SwashAverOutp.ftn90
lines: 195
sha256: 17d742ea75b409439a467000bada8490aef57133faefe0609ac3f535469e0eb8
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashAverOutp.ftn90 — 판독 구간 기록

구간은 1행부터 195행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | `SwashAverOutp ( iquan )` 시작(1). 저작권·GPL 3 이상·무보증 머리말, 작성자·2012년 신규 이력과 빈 줄·주석(2–36). 파랑 평균 수위 상승(setup), 파고(wave height), 평균 흐름(mean current)·수송 성분(constituents)·난류량(turbulence quantities)을 출력하기 위한 시간 평균 목적(38–40). 모의 후반의 지정 기간을 평균하고 정상 상태에 충분한 모의 기간을 가정한다는 방법 주석(42–46). |
| 48–80 | 시작 시 1행 루틴 안. 통신·유동·출력·시간·격자 모듈 사용과 implicit none(50–57). 입력 iquan 주석은 1=수위 또는 유속, 2=수송 성분, 3=난류량(61–64). 셀·성분·격자 인덱스와 종료 시각까지 간격 dif 선언(68–73). `integer, save :: ient = 0 ! number of entries in this subroutine` (69). 구조·소스 머리말 주석(75–80). |
| 81–116 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashAverOutp')` (81). `dif = tfinc - timco` (83). `if ( lwavoutp .and. iquan == 1 ) then` (85), 그 안 `if ( .not. dif > twavoutp ) then` (89), `nwavoutp = nwavoutp + 1.` (91). `if ( optg /= 5 ) then` (93)은 `do nm = 1, mcgrd` (94)에서 `if ( dps(nm) > 0. ) then` (95)에 따라 `setup (nm) = setup (nm) + s1(nm)` (96), `etavar(nm) = etavar(nm) + s1(nm)*s1(nm)` (97). `else` (98)는 `setup (nm) = 0.`(99), `etavar(nm) = 0.`(100)이다. 격자 종류의 `else` (103)는 `do icell = 1, ncells` (104), `if ( dps(icell) > 0. ) then` (105), `setup (icell) = setup (icell) + s1(icell)` (106), `etavar(icell) = etavar(icell) + s1(icell)*s1(icell)` (107). 셀 수심 조건의 `else` (108)는 `setup (icell) = 0.`(109), `etavar(icell) = 0.`(110)이다. 내부 조건·루프 종료(111–115). [10-15 전수 검증 보완] |
| 117–148 | 시작 시 1행 루틴·85행 `if ( lwavoutp .and. iquan == 1 ) then` 조건 안. `if ( abs(dif) < 0.99*dt .and. nwavoutp > 1. ) then` (117)에서 `setup = setup / nwavoutp` (119), `hsig = 4. * sqrt( max( etavar / (nwavoutp-1.) - setup*setup, 0. ) )` (121). 117행 조건은 123행 `endif`에서 닫힌다. 85행 조건은 125행 `endif`에서 닫힌다. 별도 `if ( lcuroutp .and. iquan == 1 ) then` (127)의 `if ( .not. dif > tcuroutp ) then` (131)에서 `ncuroutp = ncuroutp + 1.` (133), `mvelu = mvelu + u1` (135), `if ( .not.oned .and. optg /= 5 ) mvelv = mvelv + v1` (136). 별도 `if ( abs(dif) < 0.99*dt .and. ncuroutp > 0. ) then` (140)에서 `mvelu = mvelu / ncuroutp` (142), `if ( .not.oned .and. optg /= 5 ) mvelv = mvelv / ncuroutp` (143). 조건 종료·빈 주석(145–148). [10-15 전수 검증 보완] |
| 149–172 | 시작 시 1행 루틴 안. `if ( ltraoutp .and. iquan == 2 ) then` (149). `if ( .not. dif > ttraoutp ) then` (153)에서 `ntraoutp = ntraoutp + 1.` (155), `do l = 1, ltrans` (157)의 `mcons(:,:,l) = mcons(:,:,l) + rp(:,:,l)` (158). 별도 `if ( abs(dif) < 0.99*dt .and. ntraoutp > 0. ) then` (163), `do l = 1, ltrans` (165)에서 `mcons(:,:,l) = mcons(:,:,l) / ntraoutp` (166). 조건·루프 종료(167–171), 빈 주석(172). |
| 173–195 | 시작 시 1행 루틴 안. `if ( lturoutp .and. iquan == 3 ) then` (173). `if ( .not. dif > tturoutp ) then` (177)에서 `nturoutp = nturoutp + 1.` (179), `mtke(:,:) = mtke(:,:) + rtur(:,:,1)` (181), `meps(:,:) = meps(:,:) + rtur(:,:,2)` (182). 별도 `if ( abs(dif) < 0.99*dt .and. nturoutp > 0. ) then` (186)에서 `mtke = mtke / nturoutp` (188), `meps = meps / nturoutp` (189). 조건·루틴 종료와 빈 주석(191–195). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91–121: 파랑 표본 수 nwavoutp는 수심 조건 밖에서 증가한다. dps<=0인 점은 setup·etavar가 0으로 설정된다. hsig의 제곱근 내부는 etavar/(nwavoutp-1.)에서 setup*setup을 빼며, setup에는 119행에서 nwavoutp로 나눈 값이 들어간다.
- 117–123·140–145·163–169·186–191: 종료 근처의 시각 조건은 abs(dif)<0.99*dt이다. 이 분기들은 누적 배열을 제자리에서 나누며, 이 파일에는 이미 정규화했는지 기록하는 플래그가 없다.
- 135–143: mvelv 누적·정규화에는 모두 .not.oned 및 optg/=5 조건이 있다. mvelu 누적·정규화에는 해당 조건이 없다.
