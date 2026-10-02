---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_timestep.F90
lines: 120
sha256: 13297e7ff3b23640c1697f25e7af980aff5e169fe0be0b9d665dd32f3170c0ac
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# wave_timestep.F90 — 판독 구간 기록

구간은 1행부터 120행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | `wave_timestep_module` 시작(1), 저작권·연락처·LGPL 2.1 이상 및 무보증 머리말(2–27), implicit none·save·private·공개 wave·contains(28–33). |
| 34–55 | `wave` 진입, params/spaceparams/정상방향·비정상파 모듈과 공통 루틴 의존성(36–43), 인자·save gamma 배열 선언(47–50). gamma 미할당 때 격자 크기 최초 할당(52–54). 옛 wave_stationary/wave_directions use는 주석이다(38–39).<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`if (.not.allocated(gamma)) then` (52)<br>`allocate(gamma(s%nx+1,s%ny+1))` (53)<br>`endif` (54) |
| 56–63 | 모든 파 계산의 기본 수심. delta>0일 때 hh+delta*H를 eps 이상으로 제한, else는 hh를 eps 이상으로 제한하여 hhw에 대입(58–62).<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`if (par%delta>0.d0) then` (58)<br>`s%hhw = max(s%hh+par%delta*s%H,par%eps)` (59)<br>`else` (60)<br>`s%hhw = max(s%hh,par%eps) ! hh can be less than eps after morphevolution?` (61)<br>`endif` (62) |
| 64–74 | oldhmin=1이면 hstokes=max(hh,hmin)(64–65). else에서는 gamma=H/hh(67), gamma>1 마스크에 deltahmin*(gamma−1)*H+hh, 나머지는 hh를 hstokes로 사용(68–72). 73행에서 oldhmin 조건 종료.<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`if (par%oldhmin==1) then` (64)<br>`s%hstokes = max(s%hh,par%hmin)` (65)<br>`else` (66)<br>`gamma = s%H/s%hh` (67)<br>`where (gamma>1.d0)` (68)<br>`s%hstokes = par%deltahmin*(gamma-1.d0)*s%H+s%hh` (69)<br>`elsewhere` (70)<br>`s%hstokes = s%hh` (71)<br>`endwhere` (72)<br>`endif` (73) |
| 75–82 | wavemodel select 시작과 Stationary case. t의 wavint 나머지가 0.001*dt 미만이거나 newstatbc=1일 때만 순간 수심 스위치 0으로 분산 계산, callType 0 정상방향 루틴 호출 및 newstatbc 초기화(78–82).<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`select case (par%wavemodel)` (75)<br>`case(WAVEMODEL_STATIONARY)` (76)<br>`if ((abs(mod(par%t,par%wavint))<0.001d0*par%dt) .or. s%newstatbc==1) then` (78)<br>`call wave_dispersion(s,par,0)  ! use instantaneous water depth (and velocity)` (79)<br>`call wave_stationary_directions(s,par,0)` (80)<br>`s%newstatbc   = 0` (81)<br>`endif` (82) |
| 83–96 | 첫 행 진입 시 열린 블록: `select case (par%wavemodel)` (75). 같은 select 안의 병렬 Surfbeat case에서 single_dir=1이면 평활 갱신을 항상 호출(84–86). 그 안의 갱신 시점 조건은 주기·새 경계·t=dt 중 하나(89): 스위치 1 분산·callType 1 방향 계산·newstatbc=0(90–92). 시점 조건 종료(93) 후 같은 single_dir 분기에서 newstatbc를 다시 0으로 설정(95).<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`case(WAVEMODEL_SURFBEAT)` (83)<br>`if (par%single_dir==1) then` (84)<br>`call update_means_wave_flow(s,par)` (86)<br>`if ((abs(mod(par%t,par%wavint))<0.001d0*par%dt) .or. s%newstatbc==1 .or. par%t==par%dt) then` (89)<br>`call wave_dispersion(s,par,1)  ! use s%hhws water depth (and velocity)` (90)<br>`call wave_stationary_directions(s,par,1)` (91)<br>`s%newstatbc   = 0` (92)<br>`endif` (93)<br>`s%newstatbc       = 0 ! not sure if this is needed every timestep, but no overhead to keep in ...` (95) |
| 97–103 | 첫 행 진입 시 열린 블록: `select case (par%wavemodel)` (75)의 `case(WAVEMODEL_SURFBEAT)` (83) 분기 → `if (par%single_dir==1) then` (84). Surfbeat case와 single_dir=1 분기 안이지만 89행 시점 조건 밖이다. WCI이면 평균 비정상 수심 스위치 2, 아니면 순간 수심 스위치 0으로 분산을 다시 계산(98–102). 그 WCI if 밖에서 항상 `wave_instationary` 호출(103).<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`if (par%wci==1) then` (98)<br>`call wave_dispersion(s,par,2) ! use s%hhwcins water depth (and velocity)` (99)<br>`else` (100)<br>`call wave_dispersion(s,par,0) ! use s%hhw water depth` (101)<br>`endif` (102)<br>`call wave_instationary(s,par)` (103) |
| 104–115 | 첫 행 진입 시 열린 블록: `select case (par%wavemodel)` (75)의 `case(WAVEMODEL_SURFBEAT)` (83) 분기 → `if (par%single_dir==1) then` (84). 104행 else는 single_dir 조건의 병렬 비단일방향 분기이다. newstatbc=0(105), WCI이면 평활 갱신과 스위치 2 분산 호출, 아니면 스위치 0 호출(106–112). 그 WCI if 밖에서 `wave_instationary` 호출(113). 114에서 single_dir if, 115에서 wavemodel select 종료.<br>원문 조건·계산·호출 및 블록 경계(행 순서):<br>`else` (104)<br>`s%newstatbc       = 0` (105)<br>`if (par%wci==1) then` (106)<br>`call update_means_wave_flow(s,par)` (108)<br>`call wave_dispersion(s,par,2) ! use s%hhwcins water depth (and velocity)` (109)<br>`else` (110)<br>`call wave_dispersion(s,par,0) ! use s%hhw water depth` (111)<br>`endif` (112)<br>`call wave_instationary(s,par)` (113)<br>`endif` (114)<br>`end select` (115) |
| 116–120 | 빈 줄과 wave 루틴 종료(118), 모듈 종료(120). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 67–72: 새 hstokes 경로의 gamma 식은 `gamma = s%H/s%hh`로 hh 분모에 하한 제한이 없다. gamma<=1인 셀은 `s%hstokes = s%hh` (71)이며 이 경로에는 max(hh,hmin) 대입이 없다.
- 38–40·80·91: 기존 wave_stationary_module과 wave_directions_module의 use는 주석이고, 정상 및 방향 갱신은 모두 wave_stationary_directions에 callType 0/1로 전달한다.
- 89–103: Surfbeat 단일방향 갱신 시점에는 스위치 1의 wave_dispersion 및 방향 루틴을 호출한 뒤, 같은 호출에서 WCI에 따라 스위치 2 또는 0의 wave_dispersion을 다시 호출한다.
- 75–115: wavemodel select에는 Stationary와 Surfbeat case만 있고 case default는 없다.
- 92·95: 단일방향의 방향 갱신 조건 안에서 newstatbc를 0으로 만들고, 그 조건 종료 후 같은 single_dir 분기에서 다시 0으로 만든다.
