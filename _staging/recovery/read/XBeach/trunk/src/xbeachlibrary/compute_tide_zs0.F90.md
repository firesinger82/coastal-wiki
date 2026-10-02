---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/compute_tide_zs0.F90
lines: 649
sha256: 54a76088cc149de5d6b041cee66a76f3f3ed41c435f770e07835f4b96e1fb9ad
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# compute_tide_zs0.F90 — 판독 구간 기록

구간은 1행부터 649행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 저작권·작성자·LGPL 2.1 이상 라이선스 머리말. |
| 27–48 | `compute_tide_module`: save·private, 네 모서리 ndist/sdist 저장(34). 공개는 `tide_init`·`tide_boundary_timestep`; 시간·경계 보간과 격자 채움은 private(36–45). |
| 49–73 | master 전역격자 초기화 `tide_init` 선언. 모서리 순서 1=(1,1), 4=(nx+1,1), 3=(nx+1,ny+1), 2=(1,ny+1)의 ndist·sdist를 저장(65–72). |
| 74–100 | zsinitfile 존재하면 `create_new_fid`, j별 nx+1개의 zs0를 읽고 오류 보고(75–85). 없으면 `timeinterp_tide(...,0.d0)` → `boundaryinterp_tide(globalonly=.true.,correctforwetz=.false.)` → `fill_tide_grid`(88–96); wetz 미초기화 때문에 보정 생략한다는 주석. |
| 101–139 | `tide_boundary_timestep`: MPI 최초 호출에 네 모서리 거리 broadcast, initialised=true(118–124). 현재 t에서 `timeinterp_tide`·로컬 `boundaryinterp_tide`, instant/hybrid만 `fill_tide_grid`(128–135). |
| 140–169 | `timeinterp_tide`: tideloc=0이면 네 모서리 모두 par%zs0(159–162), 1이면 첫 시계열을 `LINEAR_INTERP`한 zs01을 나머지에 복사(166–169). |
| 170–194 | tideloc=2·LAND는 첫 열→zs01/zs02, 둘째 열→zs03/zs04(174–177); SEA는 첫 열→zs01/zs04, 둘째 열→zs02/zs03(180–183). tideloc=4는 열 1..4를 모서리별 시간 보간(187–190). 두 select 모두 default 없음. |
| 195–223 | `boundaryinterp_tide` 선언. 선택인수 기본값은 globalonly=false, correctforwetz=true(212–222). |
| 224–242 | tideloc=0/1이면 front 1:2, back nx:nx+1, 좌우 첫/끝 열에 zs01 설정; right는 par%ny>0일 때(227–232). 2·LAND는 front zs01·back zs03, complex ID 3·4로 측면 보간(237–241). |
| 243–265 | 2·SEA: 첫 y경계 zs01·끝 y경계 zs02. ny=0이면 `(zs02-zs01)/dnz(1,1)`, 그 외 모서리 ndist 차로 기울기 계산(250–254); dzs0dn에 wetz를 곱함(255–257). complex ID 1·2 실행 후 내부 두 번째/끝전 행을 경계값으로 복사(261–264). |
| 266–277 | tideloc=4이면 complex front/back/측면 ID 1..4 호출, ID4는 par%ny>0만(268–273). zs0(2,:)와 zs0(nx,:)를 각각 앞·뒤 경계에서 복사(274–275). |
| 278–309 | correctforwetz 참이면 전체 wetz=0 셀의 zs0=zb(280–284). 2D 측면은 이웃이 마르면 두 zb의 min(288–292), front/back도 내부 이웃이 마르면 경계·내부 zb의 min으로 설정(299–304). |
| 310–342 | `boundaryinterp_tide_complex` 선언, boundaryID 1=front·2=back·3=left·4=right라는 주석(332). MPI 관련 크기는 ID1/2에 xmpi_n, ID3/4에 xmpi_m, 비MPI는 0(334–342). |
| 343–368 | ID1은 i=1·j=1..ny+1·top, tide1/2=zs01/zs02·ndist 모서리 1/2(345–353). ID2는 i=nx+1·bot, tide1/2=zs04/zs03·거리 4/3(358–366). front/back의 tidegradient1/2는 0으로 고정(355–356·367–368). |
| 369–403 | ID3은 주석상 left(flow=right MPI), j=ny+1·isright·zs02/zs03·sdist 2/3(370–378). ID4는 right(flow=left MPI), j=1·isleft·zs01/zs04·sdist 1/4(387–395). 횡기울기는 `(zs02-zs01)` 및 `(zs03-zs04)`를 ny=0에서 dnz, 아니면 양끝 ndist 차로 나눔(379–401). |
| 404–451 | MPI globalonly 또는 관련 분할수=1이면 mpidiscretisation=false, 비MPI도 false(409–418). 경계 `maxval(zb)` 및 `maxloc`의 거리 추출(421–427). 분할 시 비경계 rank 극값을 −huge로 제외, MPI_MAX로 maxzb 모으고 차<1e-8인 rank의 위치를 MPI_MAX로 모음(434–446); 단일 격자는 그대로 대입(449–450). |
| 452–484 | 네 수위/바닥 조합 설명 후 관련 경계 rank 또는 globalonly만 실행(465). 두 tide<=maxzb면 최대바닥 위치에서 양쪽 tide1/tide2로 나눠 상수 수위 설정(467–482). 측면은 해당 tidegradient1/2*wetz도 대입(478·481). |
| 485–502 | 두 tide>maxzb면 `ddist=1/(disttide2-disttide1)`, `fac=(거리-disttide1)*ddist`, `zs0=(1-fac)*tide1+fac*tide2`(489–499); 측면 기울기도 같은 fac로 보간 후 wetz를 곱함(499). |
| 503–529 | tide1>maxzb·tide2<=maxzb: 최대바닥까지 tide1 고정, 이후 `fac=(거리-distmaxzb)/(disttide2-distmaxzb)`로 두 tide 보간(507–525). 측면 상수 구간은 gradient1, 보간 구간은 gradient1/2 혼합*wetz(521·525). |
| 530–568 | tide1<=maxzb·tide2>maxzb: 최대바닥까지 `fac=(거리-disttide1)/(distmaxzb-disttide1)` 보간, 이후 tide2 고정(534–552). 뒤쪽 측면 기울기 대입은 `tidegradient1*wetz`(552). 끝에 모든 경계 zs0를 max(zs0,zb)로 제한(559–564). |
| 569–607 | `fill_tide_grid`: instant/hybrid 및 초기 velocity용, MPI는 cross-shore strip에서만 작동한다는 주석(570–571). j=2..ny별 maxzb·maxloc sdist, front/back tide 추출(586–593). i=3..nx−1만 채우고 2/nx는 경계 복사 상태를 유지한다는 주석(605–606). |
| 608–621 | 내부 두 tide<=maxzb면 최대바닥 기준으로 tide1/tide2 상수(608–613); 둘 다 높으면 front/back 전체 sdist 차로 fac를 계산해 선형 보간(615–620). |
| 622–649 | 한쪽 tide만 높으면 최대바닥까지/이후를 상수 또는 보간으로 나누며 분모는 `sdist(nx+1,j)-distmaxzb` 또는 `distmaxzb-sdist(1,j)`(623–638). 끝에 i=3..nx−1의 zs0=max(zs0,zb)(644). 루프·루틴·모듈 종료(645–649). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91·218–222·255–257·478·481·499: 초기화는 correctforwetz=false로 호출하지만, 이 선택인수는 complex 루틴에 전달되지 않는다. 일부 dzs0dn 계산은 선택인수와 관계없이 wetz를 곱한다.
- 239·241·369–391: 호출부의 ID3/4 주석은 left/right이지만 complex 구현은 ID3을 ny+1·xmpi_isright, ID4를 1·xmpi_isleft로 연결하며 이 반대 명칭을 주석에도 적고 있다.
- 530–552: tide2가 높은 쪽의 상수 수위 구간은 zs0=tide2지만 dzs0dn에는 tidegradient1을 사용한다. 두 tide가 낮은 분기의 tide2 구간은 tidegradient2를 사용한다(480–481).
- 507·517·534·544·623·634: 최대바닥 위치와 끝점 거리의 차를 나누는 식에 분모 0 검사는 없다.
- 570–571·586–593: fill_tide_grid의 MPI 제약이 주석으로 명시되어 있으며, 구현은 로컬 s의 front/back 수위와 행별 최대바닥을 사용하고 MPI 통신 호출은 없다.
