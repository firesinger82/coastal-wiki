---
file: models/SFINCS/raw/source_code/sfincs/source/src/snapwave/snapwave_data.f90
lines: 292
sha256: b57ac4c27232b093763f9a80f72bef5283a1c83a1383825d080b36d9097c4926
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# snapwave_data.f90 — 판독 구간 기록

구간은 1행부터 292행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | `module snapwave_data` 시작(1). 빌드 판본·날짜 문자열 선언(3–4). 배정밀도 좌표 x/y와 단정밀도 좌표 xs/ys, 좌표 기준 xmn/ymn을 선언한다(6–8). msk의 주석은 0=land, 1=inner point, 2=boundary이다(9). 바닥·수심·수심 기울기·단주기파와 IG파의 파수 및 Cg/C·위상속도와 군속도·마찰계수·rms 파고·첨두주기·쇄파 및 바닥마찰 소산·파력·바람·평균 파향·출력 버퍼 배열을 선언한다(10–30). 초기값 선언은 `real*4                                      :: u10dmean=-999.          ! average wind direction` (27), `real*4                                      :: thetamean=-999.         ! mean wave direction` (29)이다. F와 Fx/Fy 선언의 `Dw/C/rho/depth`는 주석이다(24–25). |
| 31–79 | 시작 시 1행 snapwave_data 모듈 안. 주변 점 kp, 내부점 inner, Neumann 연결 배열 및 점 수를 선언한다(31–34). 부분 방향격자와 360도 방향격자, 두 격자의 대응 i360, 바람 방향분포, 상류점 prev/prev360, 가중치 w/w360, 보간 상류점 거리 ds/ds360, 굴절속도 ctheta/ctheta_ig/ctheta360을 선언한다(35–49). xn/yn/zn 선언은 주석 처리되어 있다(50). 바닥 경사, 면·변의 노드 연결, bndindx/tau/Hmax, sinhkh/Hmx와 IG 대응 배열을 선언한다(51–62). Fluxtab/F0tab 선언은 주석 처리되어 있다(56–57). 방향별 에너지 ee/ee_ig, DoverE, 작용량 aa, 평균 주파수 sig, 바람 입력 에너지·작용량과 방향 적분값, beta/srcig/alphaig, SnapWave와 quadtree 간 인덱스 배열을 선언한다(63–79). 이 구간은 선언과 주석만 포함한다. |
| 80–125 | 시작 시 1행 snapwave_data 모듈 안. 기준·시작·종료 시각 문자열을 선언한다(81–85). 단일 지점 시변 경계 파일 snapwave_jonswapfile과 공간·시간 변화 경계 파일 bnd/enc/bhs/btp/bwd/bds 및 netsnapwavefile을 선언한다(87–99). 경계 지점 수 nwbnd, 시각 수 ntwbnd, 시각별 평균 파고·주기·파향·수위, 배정밀도 경계 좌표와 enclosure 좌표, 단정밀도 경계 시각, 현재 시각의 파고·주기·파향·방향퍼짐·수위·방향 스펙트럼·수심을 선언한다(101–119). 모든 지점·시각의 hs/tp/wd/ds/zs 배열을 선언한다(121–125). wd와 ds의 주석 단위는 각각 nautical deg와 deg이다(123–124). |
| 126–160 | 시작 시 1행 snapwave_data 모듈 안. IG 경계 평균주기, 현재 파고·주기, 전체 시공간 파고·주기, 방향 스펙트럼을 선언한다(127–133). jonswapgam의 주석은 offshore 스펙트럼과 Herbers IG 경계 계산에 쓰는 JONSWAP gamma이며 default=3.3이라고 적는다(134). 이 선언에는 초기값 대입이 없다. 경계 갱신 논리값, 마지막 경계 시각 인덱스, 격자 경계 및 활성점 인덱스, 가까운 두 경계 지점과 가중치를 선언한다(136–143). 정규격자 mmax/nmax, dx/dy, 원점, 회전각 및 삼각함수 값을 선언한다(145–153). tstart/tstop은 real*8, timestep은 real*4로 선언한다(155–159). |
| 161–220 | 시작 시 1행 snapwave_data 모듈 안. 출력 파일명과 지역 입력값을 선언한다(161–165). nx/ny·m/n 선언은 주석 처리되어 있다(166–167). 방향 간격·sector, 단주기파와 IG파 마찰계수, 초기 주기, 공간 마찰 적용 수심, Baldock alpha/gamma, 최대 파고수심비, 쇄파 제어값, 최소 수심, 격자·수심·마찰·상류점·mask·index·관측 파일, 관측점 좌표·참조점·가중치·이름·결과를 선언한다(168–200). baldock_ratio 주석의 기본값은 0.2이고 baldock_exponent 주석은 `(Hloc / Hmax)**iexp`와 0(기본)·1·2를 적는다(177–178). 실행 기본값 대입은 아니다. dt·tol·비정규격자 노드/면/변 수, 테이블 이름, Neumann 파일·좌표, 지형고 기준 마찰 배율, DoverA/DoverE 완화계수를 선언한다(201–220). 초기값 선언은 `integer                                   :: ntab = 10` (208)이다. 완화계수 주석은 1.0이면 비활성이라고 적는다(219–220). |
| 221–244 | 시작 시 1행 snapwave_data 모듈 안. 출력 형식과 반복별 출력 선택 ja_save_each_iter를 선언한다(222–223). rho/pi/g, 타이머 t0..t4, nb/np와 부분·360도 방향 수를 선언한다(225–234). 바람 입력용 jadcgdx/c_dispT/mwind/Tini/sigmin/sigmax/wind_opt를 선언한다(236–244). wind_opt 주석은 1=on, 0=off이다(244). 이 구간에는 값 대입과 루틴 호출이 없다. |
| 245–259 | 시작 시 1행 snapwave_data 모듈 안. 식생 선택, 식생 지도 파일, 종 수, 수직 구간 수와 최대 수직 구간 수, 구간 높이·bulk drag coefficient·줄기 직경·단위 면적당 줄기 수의 2차원 배열을 선언한다(246–256). 높이 주석은 초기 바닥 zb_ini(zb0) 기준 m, 줄기 직경은 m, 줄기 수는 m-2이다(253–256). Dveg는 단정밀도 1차원 allocatable 배열이다(258). 초기값·범위 검사는 없다. |
| 260–275 | 시작 시 1행 snapwave_data 모듈 안. IG 선택과 Baldock 계수, 최대 단주기 쇄파점 결정용 gamma 배율, 단주기 에너지에서 IG source를 빼는 비율 shinc2ig, source/sink 배율 alphaigfac, 경계 IG 에너지·주기 추정비, IG 쇄파 임계비, IG 사용·반복 source 재계산·Herbers·IG 주기 선택을 선언한다(262–275). 주석은 ig_opt=1 기본, shinc2ig 범위 0–1 및 기본 0, alphaigfac 기본 1.0, baldock_ratio_ig 기본 0.2, herbers_opt=1 기본, tpig_opt의 1=Tm01(기본)·2=Tpsmooth·3=Tp·4=Tm-1,0을 적는다(262·265–266·270·274–275). 주석의 값에 대한 실행 대입은 이 구간에 없다. |
| 276–292 | 시작 시 1행 snapwave_data 모듈 안. IG·바람·식생·Herbers·반복 source 계산의 논리 switch, crit/nr_sweeps, restart/coupled_to_sfincs/storesnapwavegrid, nr_quadtree_points를 선언한다(277–290). 빈 줄·구분 주석과 `end module snapwave_data`로 끝난다(291–292). 모듈 전체에는 contains와 실행 루틴이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–292: 모듈에는 implicit none 문장이 없다. 선언 초기값은 u10dmean=-999., thetamean=-999., ntab=10에만 있다(27·29·208).
- 134·177–178·262·265–266·270·274–275: 여러 기본값과 선택 범위는 선언 주석에만 적혀 있다. 해당 선언에는 그 값의 대입이 없다.
- 228: pi 선언의 주석은 `water density`이다. rho 선언에도 같은 주석이 있다(227).
- 218: fwigratio 선언의 주석은 IG 마찰에 곱하는 값의 이름을 `fwratio`로 적는다.
