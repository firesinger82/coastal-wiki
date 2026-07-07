---
title: "ROMS 침수-노출(wetting & drying) source-analysis — wetdry.F (Dcrit 마스크 + one-way flux)"
model: ROMS
component: wetting-drying
canonical_source: self
citation_status: verified
verification_method: "ROMS raw 직접 read: ROMS/Nonlinear/wetdry.F(928) — Dcrit 게이트·RHO/U/V mask 유도·부호기반 방향판정·corrector DU_avg1 결합 file:line 직접 검증(2026-07-07). 매뉴얼 교차: raw/manuals/wiki/markdown/WET_DRY.md(Dcrit 기본 0.10 m·one-way flux 규칙)."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/ROMS/source-analysis/roms_barotropic_2d.md
  - concepts/compound-flooding/wetting-drying-cross-model.md
---

# ROMS 침수-노출 — `wetdry.F` (SUBROUTINE WETDRY / WETDRY_MASK_TILE)

> 소스: `.../roms/ROMS/Nonlinear/wetdry.F` (928줄). 매뉴얼: `raw/manuals/wiki/markdown/WET_DRY.md`.
> **정체**: `MASKING`+`WET_DRY` CPP 활성 시 매 fast(순압) 스텝마다 **wet/dry 마스크**(`rmask_wet`/`umask_wet`/`vmask_wet`/`pmask_wet`)를 재계산해 마른 셀의 flux 를 차단. [[wetting-drying-cross-model]] 8모델 대조서 **유일 전용노트 부재였던 갭**을 채움.

## 0. 진입 — init vs per-step
`Linitialize`=T 이면 `wetdry_ini_tile`(초기 draping), 이후 매 스텝 `wetdry_tile`(:38-90). fast 루프(`iif≤nfast`)에서만 마스크 갱신(:208).

## 1. Dcrit 게이트 (cell-center 판정)
```fortran
wetdry(i,j) = 1.0 * rmask(i,j)                         ! 정적 land mask 곱
IF ((zeta(i,j)+h(i,j)) <= (Dcrit(ng)+eps)) wetdry(i,j)=0.0   ! :200
```
총수심 `D = ζ + h ≤ Dcrit` 이면 dry(0). **`Dcrit` 기본 0.10 m**(매뉴얼, roms.in 입력 `read_phypar.F:973`). RHO-point(cell-center) `rmask_wet = wetdry`(:624).

**초기화 draping**(매뉴얼): D<Dcrit 셀은 `ζ = Dcrit − h` 로 수위를 올려 육지에 물을 덮음 — 영구 dry(rmask=0) 셀도 수심 Dcrit 유지. 음수심 방지의 ROMS 방식(set_depth.F 에서 `h=0→eps` 치환과 병행).

## 2. ★U/V-point mask — 부호로 flux 방향 표현
```fortran
umask_wet(i,j) = wetdry(i-1,j) + wetdry(i,j)           ! :632
IF (umask_wet==1.0) umask_wet = wetdry(i-1,j) - wetdry(i,j)   ! :633-634
```
- 양쪽 wet(1+1) → **2**, 양쪽 dry(0+0) → **0**, **한쪽만 wet(합=1) → 차 ±1**(왼 wet=+1, 오른 wet=−1).
- ★즉 edge mask 값이 단순 0/1 이 아니라 `{0, ±1, 2}` — **부호가 젖은 쪽 방향**을 인코딩. 뒤 momentum 에서 이 부호로 flux 를 방향 선택적으로 통제.

## 3. ★one-way flux — "유출 차단, 유입 허용"
매뉴얼 규칙(WET_DRY.md:22): *"If the water level is less than Dcrit, then **no flux is allowed out of that cell. Water can always flow into a cell**."* — 마른 셀에서 나가는 flux 는 0, 들어오는 flux 는 허용(범람 전진 보장).

corrector(fast-time 평균) 버전이 이를 구현(:805-817):
```fortran
cff1 = ±(wetdry 합/차)                                  ! 방향부호
cff6 = 0.5 + sign(0.5, DU_avg1(i,j))·cff1               ! flux 방향과 결합
umask_wet = 0.5·cff1·cff5 + cff6·(1−cff5)               ! :811
IF (DU_avg1==0 .and. 이웃합≤1) umask_wet=0              ! :813-816 lone pond 차단
```
`DU_avg1`(fast 평균 U-transport) 부호가 wet→dry 방향이면 그 edge 흐름 허용(유입), 반대면 차단(유출). ★유량이 0 인 고립 웅덩이(lone pond)는 강제 dry.

## 4. 마스크 합성·소비
```fortran
rmask_full = rmask_wet · rmask                          ! :285 정적×동적
pmask_full = MAX(pmask_wet·pmask, 2.0)                  ! :290 corner
```
`rmask_wet_avg` 를 fast 스텝 누적 후 `AINT(avg·cff)` 로 이진화(:258) — 순압 substep 평균으로 채터링 완화. 최종 `*_full` 마스크가 momentum·transport 항에 곱해져 dry 셀 계산 배제.

## 5. ★주요 findings
- **★one-way flux(유입 항상 허용)**: 마른 셀로의 flux 만 허용, 유출 차단 — 범람 전선이 한 방향으로 전진. hysteresis(이중임계) 대신 이 방향성으로 채터링 억제. Delft3D/ADCIRC(수위 이중임계)와 다른 접근.
- **★edge mask = 부호 있는 {0,±1,2}**: 단순 0/1 아님 — 방향 인코딩(:634). 다른 모델(SFINCS kfuv 0/1, LISFLOOD MaskTest bool)과 근본적으로 다른 표현.
- **lone pond 차단**(:813): DU_avg1=0 이고 이웃이 부분 dry 면 강제 dry — 고립 웅덩이 수치 잔재 제거.
- **fast-step 평균 이진화**(rmask_wet_avg, :258): 순압 substep 진동을 평균으로 흡수 후 3D 로 전달.
- **Dcrit=0.10 m 기본**: 다른 범람 모델(LISFLOOD 1e-3, SFINCS 0.05)보다 큼 — ROMS 는 해양순환 지향이라 보수적. 조간대 정밀 침수엔 하향 필요.
- **초기 draping = ζ 상향**: 마른 셀 수위를 Dcrit−h 로 세팅 — 음수심 방지가 flux clip 이 아니라 **수위 재정의** 방식.

## 6. Primary sources
- ROMS wiki **WET_DRY.md**(raw/manuals/wiki) — Dcrit 0.10 m·one-way flux·draping 규칙 정본.
- 소스 `ROMS/Nonlinear/wetdry.F`(마스크 알고리즘)·`set_depth.F`(h→eps)·`read_phypar.F:973`(Dcrit 입력).
- 계보: Warner et al. 2013 (ROMS wetting/drying, *Computers & Geosciences*) — WET_DRY 표준 참조.

## 7. 관련
- [[roms_barotropic_2d]] — 순압 2D 모드(마스크 소비처, DU_avg1 fast 평균 transport)
- [[wetting-drying-cross-model]] — 8모델 대조(본 노트로 ROMS 행 완성)
