---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_main.f90
lines: 386
sha256: 5457f45f75df3500f6bfc00c584128aa9d61e969170fe53ca5874842252d24d9
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# wave_boundary_main.f90 — 판독 구간 기록

구간은 1행부터 386행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `wave_boundary_main_module`, implicit none·save·private, `create_incident_waves` 공개(1–5). 경계조건 필요한 프로세스만 호출하라는 주석(6–15), 미완성 항목 TO FIX 주석(17–21). 인터페이스는 `create_incident_waves_surfbeat`만 활성(35–38), nonhydrostatic procedure는 주석(37). contains와 루틴 절 머리말. |
| 52–92 | `create_incident_waves_surfbeat` 인수 목록(52–60) 및 입력 설명. np·xb/yb·ntheta·dtheta·theta·t·bctype·bcfile, 공통 위상 기준점 x0/y0, 전체 offshore 평균 hboundary(67–85). theta는 x축 기준 Cartesian rad(71–72), randomseed의 주석상 범위 1..2^31-2와 프로세스 간 동일 seed 요구(86–91). 이 구간은 선언 앞 설명이며 범위 검사 코드는 아니다. |
| 93–149 | 출력 eebc(np,ntheta)는 J/m2/rad, qsbc/qnbc(np)는 m2/s, Hbc·Tbc·Dbc와 isRecomputed의 의미(93–106). optional 설명(108–120): nonhspectrum=.false., sprdthr=0.08, trepfac=0.01, nmax=0.8d0, fcutoff=0.d0, rho=1025, Tm01switch=0, nspr=0. datastore 및 `generate_wave_boundary_surfbeat` 사용(121–122), BUILDXBEACH에서 interp 사용(123–125). 입력·출력·optional 선언(130–144), i·itheta·l·dummy·durationlength 지역변수(146–147). nspr는 인수 목록에는 있으나 이 선언부에 없다. |
| 150–190 | 각 optional의 독립 조건: `if(.not.present(nonhspectrum)) then`(151) → `waveBoundaryParameters%nonhspectrum = .false.`(152); `if(.not.present(sprdthr)) then`(156) → `waveBoundaryParameters%sprdthr = 0.08d0`(157); `if(.not.present(trepfac)) then`(161) → `waveBoundaryParameters%trepfac = 0.01d0`(162); `if(.not.present(Tm01switch)) then`(166) → `waveBoundaryParameters%Tm01switch = 0`(167); `if(.not.present(nspr)) then`(171) → `waveBoundaryParameters%nspr = 0`(172); `if(.not.present(nmax)) then`(176) → `waveBoundaryParameters%nmax = 0.8d0`(177); `if(.not.present(fcutoff)) then`(181) → `waveBoundaryParameters%fcutoff = 0.0d0`(182); `if(.not.present(rho)) then`(186) → `waveBoundaryParameters%rho = 1025.d0`(187). 각각 else는 주어진 인수를 해당 필드에 복사(154·159·164·169·174·179·184·189). 범위 검사는 없고 매 호출에서 기본값/인수를 설정한다. |
| 191–237 | `if (.not.waveBoundaryAdministration%initialized) then`(194)에서 master 파일명·점/방향 수·기준점·수심 저장(199–204). 내부 독립 `if(allocated(waveBoundaryParameters%xb)) deallocate(waveBoundaryParameters%xb)`(207), `if(allocated(waveBoundaryParameters%yb)) deallocate(waveBoundaryParameters%yb)`(208), `if(allocated(waveBoundaryParameters%theta)) deallocate(waveBoundaryParameters%theta)`(209). xb(np)·yb(np)·theta(ntheta) 할당 및 복사(211–216). 방향 루프 `waveBoundaryParameters%theta(itheta) = mod(waveBoundaryParameters%theta(itheta),8.d0*atan(1.d0))`(219); 주석은 0..2pi 보장 의도(217). 같은 초기화 조건 안 `if(allocated(waveBoundaryParameters%randomseed)) deallocate(waveBoundaryParameters%randomseed)`(223), seed 복사(224). `initialise_wave_spectrum_parameters` 호출(228), initialized=.true.(229), startComputeNewSeries=t(234). 235에서 초기화 조건 종료. |
| 238–255 | 초기화 조건 밖 별도 `if (t>=waveBoundaryAdministration%startComputeNewSeries) then`(239)에서 startCurrentSeries에 기존 다음 계산 시각 복사(242), `generate_wave_boundary_surfbeat(durationlength)` 호출(245), `waveBoundaryAdministration%startComputeNewSeries = waveBoundaryAdministration%startComputeNewSeries + & durationlength`(249–250), isRecomputed=.true.(253). else 대입은 없다. |
| 256–279 | 239행 조건 밖 보간. BUILDXBEACH에서 `l = size(waveBoundaryTimeSeries%tbc)`(258), 모든 방향·점의 eebct를 `call linear_interp(waveBoundaryTimeSeries%tbc,waveBoundaryTimeSeries%eebct(i,itheta,:),l,& t,eebc(i,itheta),dummy)`(261–262), 각 점 qxbct·qybct를 각각 qsbc·qnbc에 `linear_interp`(266–269). 전처리 else에는 다른 모델의 보간에 관한 주석만 있다(271–273). 전처리 조건 밖 Hbc·Tbc·Dbc를 spectrum administration에서 복사(274–276), 루틴 끝(278). |
| 280–318 | `initialise_wave_spectrum_parameters`(280), datastore 사용; BUILDXBEACH에서 filefunctions·logging·Halt_Program 사용(283–287), 지역 fid·err·i·nspectra·testline·testchar(290–293), 초기화 로그(295–298). repeatwbc=.false.(301), bccount=0(304), spectrumendtime=0.d0(307). lastwaveelevation(np,ntheta) 할당(310–311); 308행 주석의 0 초기화 대입은 없다. BUILDXBEACH에서만 `fid = create_new_fid()`(315), 그 전처리 조건 밖 masterFileName formatted old open(317). |
| 319–330 | 첫 토큰 testline read(319). `if (trim(testline)=='LOCLIST') then`(320) 안 i=0(322), `do while (err==0)`(323)에서 `i=i+1`(324), `read(fid,*,IOSTAT=err)testchar`(325). 루프 뒤 rewind(327), `nspectra = i-1`(328), 관리 구조에 nspectra 저장(330). err의 이 루프 전 초기 대입은 없다. |
| 331–364 | 구간 시작은 320행 LOCLIST 조건 안. `if (nspectra<1) then`(332)의 BUILDXBEACH 부분에서 파일명/최소 위치수 오류 로그·`halt_program`(334–338). 조건 밖 첫 줄 재독(342), bcfiles/xspec/yspec(nspectra) 할당(346–348). 위치마다 좌표와 fname read(351–353), listline=0(354). `if (err /= 0) then`(355)의 BUILDXBEACH 부분에서 i+1 행 오류·형식 로그·`halt_program`(358–361). 위치 루프 종료(364). |
| 365–386 | 구간 시작은 320행 LOCLIST 조건 안, 앞 위치 루프는 종료됨. `else`(365)는 LOCLIST가 아닌 병렬 경로: `nspectra = 1`(366), bcfiles/xspec/yspec 할당(367–369), 첫 fname=masterFileName·listline=0(370–371), xspec=x0·yspec=y0(372–373). 374에서 if 종료 후 무조건 close(fid)(375), BUILDXBEACH 종료 로그(376–378). 루틴·모듈 종료(379·382), 마지막 빈 줄 포함(383–386). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60·142–144·171–174: nspr는 인수와 present 검사·복사에 쓰이지만 이 루틴의 형/optional 선언에 없다. 모듈과 루틴은 implicit none이다(2·127).
- 223: randomseed에 allocated/deallocate를 적용한다. 직접 읽은 `wave_boundary_datastore.f90`의 25행에서는 해당 필드가 allocatable 없는 정수 scalar로 선언되어 있다.
- 130–135·199–224: bctype·dtheta는 입력 선언 뒤 이 파일에서 사용하지 않는다. 나머지 주 격자 정보 및 seed는 initialized가 false일 때만 저장한다.
- 217–219: 주석은 theta를 0..2pi로 제한한다고 적지만 식은 `mod(theta,8.d0*atan(1.d0))`이며 음수 입력을 양수로 옮기는 추가 연산은 없다.
- 138·239–254: intent(out) isRecomputed의 대입은 재생성 조건 안의 .true.뿐이며, 조건을 만족하지 않을 때의 대입은 없다.
- 257–273: BUILDXBEACH가 정의되지 않은 경로에는 eebc·qsbc·qnbc의 시간 보간 구현이 없다.
- 308–311: lastwaveelevation을 0으로 초기화한다는 주석 다음에 할당만 있고 값 대입은 없다.
- 290·319·323–325: err는 지역변수이며 첫 do while 검사 전에 초기화되지 않는다. 첫 testline read에는 IOSTAT도 없다.
- 314–317: fid 설정은 BUILDXBEACH 안에 있고 open은 전처리 조건 밖에 있다.
- 330·365–374: waveSpectrumAdministration%nspectra 대입은 LOCLIST 경로에만 있으며 단일 파일 경로는 지역 nspectra만 1로 설정한다.
