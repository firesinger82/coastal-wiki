---
file: models/SWASH/raw/source_code/swash/src/SwashInitSteady.ftn90
lines: 240
sha256: 6295a4110607737d4b29597eb28388ceb35c079d4f0da7a4bdfd99cd196f4ae8
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashInitSteady.ftn90 — 판독 구간 기록

구간은 1행부터 240행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–89 | `SwashInitSteady` 시작(1). 기관·GPL 3 이상·무보증 머리말(2–28), 저자·2010년 신설(30–36). 등류(uniform flow)의 Chezy 식으로 유속을 초기화한다는 목적(38–40). 주석 원문 식 `!      u = C * sqrt(h * i)` (46). u=유속, C=Chezy 마찰계수, h=수심, i=수면 경사(slope)(48–52). 초기 유속을 Froude 기준으로 제한해 사류(supercritical flow)를 피한다는 주석(54). ocpcomm4·SwashCommdata3·m_genarr·SwashFlowdata 사용(58–61), implicit none(63), 인덱스·Chezy 값·Froude 수·경사·유속·STPNOW 선언(67–82), ient 기본값 `integer, save :: ient = 0 ! number of entries in this subroutine` (67). 구조·원문 안내 주석 포함. |
| 90–129 | 시작 시 1행 SwashInitSteady 루틴 안. `call strace (ient,'SwashInitSteady')`(90). 일차원 조건 `if ( oned ) then` (92), m=mf..ml의 u점 루프(96), 다음 점 식 `mu = m + 1` (98)와 kgrpnt 조회(100–101). 수면 경사 `slope = ( s1(nm) - s1(nmu) ) / dx` (103). 양의 마찰계수 조건 `if ( cfricu(nm) > 0. ) then` (105)이면 Chezy 식 `cz = sqrt( grav / cfricu(nm) )` (106), `else` (107)는 `cz = 0.` (108). 유속 식 `vel = sign(1.,slope) * cz * sqrt( hu(nm) * abs(slope) )` (111). 양의 수심 조건 `if ( hu(nm) > 0. ) then` (113)에서 Froude 수 `froude = abs(vel)/sqrt( grav * hu(nm) )` (115), 제한 조건·식 `if ( froude > 0.9999 ) vel = ( 0.9999 / froude ) * vel` (117). u1(nm,1)에 vel 복사(121). `call SWEXCHG ( u1(1,1), kgrpnt, 1, 1 )`(127), 중단 조건 `if (STPNOW()) return` (128). 대입문·반복문 원문은 `do m = mf, ml`(96), `nm  = kgrpnt(m ,1)`(100), `nmu = kgrpnt(mu,1)`(101), `u1(nm,1) = vel`(121)이다. `if ( hu(nm) > 0. ) then`(113)은 119행에서 닫힌다. `u1(nm,1) = vel`(121)은 이 수심 조건 밖에 있다. [10-15 전수 검증 보완] |
| 130–168 | 시작 시 `if ( oned ) then`(92–222)의 분기 사슬 안이다. `else`(130)가 이 구간에서 시작한다. `else` (130)는 이차원 경로. m=mf..ml·n=nfu..nl의 u점 루프(134·136). 다음 점 `mu = m + 1` (138), kgrpnt 조회(140–141), 영구 건조(permanently dry) 이웃 대체 조건 `if ( nmu == 1 ) nmu = nm` (143). 격자 거리 gvu를 쓰는 경사 `slope = ( s1(nm) - s1(nmu) ) / gvu(nm)` (145). 마찰계수 조건 `if ( cfricu(nm) > 0. ) then` (147), Chezy 식 `cz = sqrt( grav / cfricu(nm) )` (148), `else` (149)는 `cz = 0.` (150). 유속 `vel = sign(1.,slope) * cz * sqrt( hu(nm) * abs(slope) )` (153), 수심 조건 `if ( hu(nm) > 0. ) then` (155), Froude 수 `froude = abs(vel)/sqrt( grav * hu(nm) )` (157), 제한 조건·식 `if ( froude > 0.9999 ) vel = ( 0.9999 / froude ) * vel` (159). u1(nm,1)에 vel 복사(163). 루프 종료(165·167). 대입문·반복문 원문은 `do m = mf, ml`(134), `do n = nfu, nl`(136), `nm  = kgrpnt(m ,n)`(140), `nmu = kgrpnt(mu,n)`(141), `u1(nm,1) = vel`(163)이다. [10-15 전수 검증 보완] |
| 169–205 | 시작 시 `if ( oned ) then`(92)의 `else`(130–222) 안이다. n=nf..nl·m=mfu..ml의 v점 루프(171·173). 다음 점 `nu = n + 1` (175), kgrpnt 조회(177–178), 영구 건조 이웃 대체 조건 `if ( num == 1 ) num = nm` (180). 격자 거리 guv를 쓰는 경사 `slope = ( s1(nm) - s1(num) ) / guv(nm)` (182). 마찰계수 조건 `if ( cfricv(nm) > 0. ) then` (184), Chezy 식 `cz = sqrt( grav / cfricv(nm) )` (185), `else` (186)는 `cz = 0.` (187). 유속 `vel = sign(1.,slope) * cz * sqrt( hv(nm) * abs(slope) )` (190), 수심 조건 `if ( hv(nm) > 0. ) then` (192), Froude 수 `froude = abs(vel)/sqrt( grav * hv(nm) )` (194), 제한 조건·식 `if ( froude > 0.9999 ) vel = ( 0.9999 / froude ) * vel` (196). v1(nm,1)에 vel 복사(200), 루프 종료(202·204). 대입문·반복문 원문은 `do n = nf, nl`(171), `do m = mfu, ml`(173), `nm  = kgrpnt(m,n )`(177), `num = kgrpnt(m,nu)`(178), `v1(nm,1) = vel`(200)이다. [10-15 전수 검증 보완] |
| 206–240 | 시작 시 `if ( oned ) then`(92)의 `else`(130–222) 안이다. 224행부터의 다층 처리는 이 차원 분기 밖에 있다. 영구 건조점 u1(1,1)·v1(1,1)=0(208–209). `call SWEXCHG ( u1(1,1), kgrpnt, 1, 1 )`·`call SWEXCHG ( v1(1,1), kgrpnt, 1, 1 )`(213–214), `if (STPNOW()) return` (215). 반복 격자(repeating grid)의 경계 동기화라는 주석(217), `call periodic ( u1(1,1), kgrpnt, 1, 1 )`·`call periodic ( v1(1,1), kgrpnt, 1, 1 )`(219–220). 차원 분기 종료(222). 다층 조건 `if ( kmax > 1 ) then` (224)에서는 udep에 1층 u 복사(226), vdep 조건 `if ( .not.oned ) vdep(:) = v1(:,1)` (227). 수직 균일 유속 가정 주석(229). k=2..kmax 루프(231)는 u1(:,k)에 udep 복사(233), v1 복사 조건 `if ( .not.oned ) v1(:,k) = vdep(:)` (234). 루프·다층 분기·루틴 종료(236·238·240). 대입문·반복문 원문은 `u1(1,1) = 0.`(208), `v1(1,1) = 0.`(209), `udep(:) = u1(:,1)`(226), `do k = 2, kmax`(231), `u1(:,k) = udep(:)`(233)이다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 111–117·153–159·190–196: 유속의 제곱근 식은 hu/hv>0 검사 앞에서 계산된다. 양의 수심 조건은 뒤의 Froude 수 계산과 제한식만 감싼다.
- 117·159·196: 일차원 u·이차원 u·이차원 v의 Froude 제한값은 모두 0.9999로 고정되어 있다.
- 130–222: 이차원 경로의 periodic 호출 두 개에는 lreptx/lrepty 조건이 없다. 일차원 경로에는 periodic 호출문이 없다. periodic 내부는 판독하지 않았다.
