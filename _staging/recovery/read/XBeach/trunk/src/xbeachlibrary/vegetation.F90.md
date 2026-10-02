---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/vegetation.F90
lines: 886
sha256: e58ebd47d62d4637baae7bee4e90570a859b1eb0467e486a599f877b380df2c2
reader: claude-opus-5-5 (main session, format sample)
read_date: 2026-10-02
---

# vegetation.F90 — 판독 구간 기록

구간은 1행부터 886행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 저작권·LGPL 2.1 머리말 |
| 27–41 | 모듈 설명: v1.0 단파·IG 감쇠(van Thiel de Vries 2013, Phan et al. 2015), v2.0 비선형파 효과(van Rooijen et al. 2016 JGR) |
| 42–72 | `vegetation_module` 선언. `veggie` 형(종별 이름·`nsec`·`ah`·`Cd`·`bv`·`N`(정수)·canopy 계수 `Kp_can`·`beta_can`·`cf_can`·`cm_can`·`por_can`·`lp_can`), 공개 루틴 `veggie_init`·`vegatt`·`porcanflow` |
| 73–101 | `veggie_init` 머리: `vegetation==1`일 때 세 입력(종 목록 `veggiefile`, 종별 속성 파일, 공간 분포 `veggiemapfile`)을 읽는다는 주석 |
| 102–129 | 종 수 = `veggiefile` 행 수(103), master에서 종 파일명 읽기, `vegtype`·`Dveg`·`Fvegu/v`·`ucan/vcan` 할당·0 초기화 |
| 130–155 | `veggiemapfile` 읽기: 격자형식 XBEACH·DELFT3D 두 분기 모두 `vegtype(i,j)`를 행(j) 단위로 읽음(두 분기 내용 동일, Delft3D는 `status='old'`만 다름) |
| 156–207 | 종별 속성 읽기. `isCanopy`(161, canopy면 `porcanflow==1` 필수 165), `nsec` 기본 1 범위 1–100(168), canopy면 `nsec=1` 강제(170). `ah` 기본 0.1 범위 0.01–2(180). 비canopy: `bv` 0.01(0.001–1), `N` 100(1–5000, `nint`로 정수화), **`Cd` 기본 0.0 범위 0–3**(183–185), canopy 계수는 무효값. canopy: `bv=N=Cd=0`, `Kp_can` 1e-4·`beta_can` 15·`cf_can` 0.01·`cm_can` 1.5·`por_can` 0.1, `lp_can=1-por_can`(198–203). `nsecvegmax` 갱신(206) |
| 208–257 | 종 속성을 셀 중심 배열로 펼침: `nsecveg`·`Cdveg`·`ahveg`·`bveg`·`Nveg`(3차원, 단면 m) 및 canopy 2차원 배열. 식생 없는 셀은 0, `Kp_can=huge`, `lp_can=1e-12`. 끝에 `veg` 해제(256) |
| 258–304 | 완료 로그. `vegetation==0`이면 master에서 같은 배열을 단면 1로 할당하고 0·기본값으로 채움 |
| 305–346 | `vegatt`: `porcanflow==1`이면 `porcanflow`만 호출(319–320). 아니면 셀별 단면별 `Cdveg<0`일 때 `bulkdragcoeff`로 계산해 `Cdveg`에 덮어씀(327–329, 덮어쓴 뒤엔 음수가 아니므로 이후 재계산 없음) → `swvegatt`(339) → `momeqveg`(342) |
| 347–403 | `swvegatt`(단파 에너지 소산). `kmr=min(max(k,0.01),100)`. 단면별 누적 높이 `aht=ahveg+ahtold`, 수심으로 제한(382). `hterm=(sinh³(k·aht)+3sinh(k·aht))/(3k·cosh³(k·h))`(385). `Dvgt=0.5/√π·ρ·Cd·bv·N·(0.5·k·g/σ)³·(hterm−htermold)·H³`(388), 하부 단면 몫을 빼는 Suzuki et al.(2012) 방식. 결과 `s%Dveg`(400). 범위는 `imin_zs..imax_zs` |
| 404–474 | `momeqveg` 선언·초기화. 고려 성분 주석(장파·Stokes·비선형 잔차·역류·canopy 흐름, 429–434). `costhm/sinthm=cos/sin(thetamean−alfaz)`(456–457). `totT`는 `dt==t`인 첫 단계에 `Trep`로 초기화(460–462). `vegnonlin==1`이고 비정수압 파랑모델이 아니면 `Trep`마다 `swvegnonlin`으로 `unl`·`etaw` 재계산(463–473) |
| 475–501 | 셀 루프는 `i=1..nx+1, j=1..ny+1` 전체(다른 루틴의 `imin_zs..` 범위와 다름). 단면 높이는 현재 바닥 기준 `aht=ahveg+zb0−zb`(489). 비선형이면 파곡·파봉 수위 `watr/wacr=hh+min/max(etaw)`, 아니면 둘 다 `hh` |
| 502–511 | 단면이 파봉보다 위(`ahtold>wacr`)면 `Fvgtu/v`·`Fvgnlu/v`를 0으로. **`FvgCau/FvgCav`는 이 분기에서 0으로 되돌리지 않음** — 직전 단면 값이 남은 채 554–556에서 더해질 수 있다(`vegcanflo==1`일 때) |
| 512–522 | 평균류·장파 항력. `veguntow==1`: `Fvgtu=h_layer·0.5·Cd·bv·N·ueu·vmageu`, `Fvgtv=…·vev·vmageu`(515–516). `veguntow==0`: `uu·vmagu`, `vv·vmagu`(519–520). `h_layer=max(min(aht,watr)−ahtold,0)`. **v 방향도 u점 속력(`vmageu`/`vmagu`)을 곱함** — v점 속력 `vmagev`는 `flow_timestep.F90:934`에 있음. 식생 계수는 셀 중심 `(i,j)` 값을 u·v 양쪽에 그대로 사용 |
| 523–533 | 비선형파 항력: 유효 높이 `hvegeff=max(etaw+hh−ahtold,0)`, `Fvgnlt=trapz(0.5·Cd·bv·N·min(hvegeff,aht)·unl·|unl|, Trep/50)/hh`(527), `costhm/sinthm`으로 분해 |
| 534–541 | canopy 내부 흐름(Luhar et al. 2010): `ucan=√(4·k·Trep·urms³/(6π²))`(535), `FvgCan=h_layer/hh·0.5·Cd·bv·N·ucan²`(536), 파향으로 분해 |
| 542–567 | 단면 합산: 항상 `Fvgtu/v`, 비선형이면 `Fvgnlu/v`, `vegcanflo==1`이면 `FvgCau/v` 추가. 최종 `s%Fvegu/v = Fvgu/v·ρ`(N/m², 563–564) |
| 568–601 | `swvegnonlin` 선언과 배경 주석: 비대칭·왜도 파에서 `u|u|` 주기 적분이 0이 아님(Dean & Bender 2006), Rienecker & Fenton(1981) 표 기반(morphevolution과 같은 방식). `RFveg.inc` 포함(601) |
| 602–645 | RF 표 보간 준비: 최초 1회 `dh=0.03`, `dt=1.25`, `nh=floor(0.54/dh)`, `nt=floor(25/dt)`, 8성분×50시점 cos/sin 기저(613–618). `h0=min(nh·dh,max(dh,min(H,hh)/hh))`, `t0=min(nt·dt,max(dt,Trep√(g/hh)))`. Ursell `Urs=H/k²/hh³`(638), 위상 `phi=π/2·(1−tanh(0.815/Urs^0.672))`(Ruessink et al. 2012), `w1=1−phi/(π/2)`, `w2=1−w1` |
| 646–685 | 셀별 쌍선형 보간으로 성분 진폭(`RFveg(irf+3,…)`, 641 주석의 4–11 성분), `w1·cos+w2·sin` 가중 합, `unl0=urf2·√(g·hh)`, `etaw0=unl0·√(hh/g)` |
| 686–700 | `trapz`: 사다리꼴 적분 |
| 701–729 | `bulkdragcoeff` 선언(M. Bendoni). `myflag=2` 고정(728) → Mendez & Losada(2004)만 사용 |
| 730–749 | `Tp=2π/sigm`(731), `alfav=min(ahh/hh,1)`(734–738), `um=0.5·H·σ·cosh(k·alfav·hh)/sinh(k·hh)`(742), `KC=um·Tp/bv`(745). 746–748은 효과 없는 `KC=KC` |
| 750–774 | Ozeren(2013) 분기(쓰이지 않음): `0.036+50/KC^0.926`, KC<10이면 KC=10 값. Mendez–Losada 분기: `Q=KC/alfav^0.76`, `Q≥7`이면 `exp(−0.0138Q)/Q^0.3`, 아니면 Q=7 값 ≈0.506(766–770) |
| 775–815 | `porcanflow` 선언. `Fcanu/v`·`isCanopyCell` 최초 할당(`isCanopyCell`은 이후 쓰이지 않음). 셀 중심에서 계산한 뒤 u/v점으로 보간한다는 주석(812–814) |
| 816–857 | canopy 셀이고 젖어 있으면: `hcan=min(ahveg(:,:,1),hh)`, `A=(1+cm·lp/(1−lp))/dt`, 자유류 `U=ue`, `V=ve`, 수면+비정수압 기울기(중앙차분 840–845). canopy 속도 반음해 갱신(847–850), canopy 힘 = `ρ·hcan·(β·|U|·ucan + μ(1−lp)/Kp·ucan_old + cm·lp/(1−lp)·(ucan−ucan_old)/dt)`(852–857), μ=1e-6(796) |
| 858–867 | 마른 canopy 셀은 힘·속도 0, 그 외 셀은 갱신 없음 |
| 868–884 | 셀 중심 힘을 u점(`(Fcanu(i)+Fcanu(i+1))/2`, 871)·v점(`(Fcanv(j)+Fcanv(j+1))/2`, 877)으로 평균해 `s%Fvegu/v`에 넣음. 1차원(`ny=0`)이면 `Fvegv=Fcanv`(881). 이 경로는 격자점 보간을 하지만 `momeqveg` 경로(512–521)는 하지 않는다 |
| 885–886 | 모듈 끝 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 516·520: v 방향 항력에 u점 속력 사용. `porcanflow`(871·877)는 u/v점으로 보간하는 것과 대비된다.
- 502–511: 파봉 위 단면에서 `FvgCau/FvgCav`가 0으로 초기화되지 않는다.
- 475–476: `momeqveg`만 전체 `1..nx+1` 범위로 돈다(MPI 분할 시 경계 셀 포함 여부는 이 파일만으로 판단 불가).
- 799·807: `isCanopyCell`은 할당만 되고 쓰이지 않는다.
