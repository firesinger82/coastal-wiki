---
title: "ROMS 침수-노출(wetting & drying) source-analysis — wetdry.F (Dcrit 마스크 + one-way flux)"
model: ROMS
component: wetting-drying
canonical_source: self
citation_status: verified
last_source_check: "2026-10-14 (recovery 대조 반영)"
verification_method: "ROMS raw 직접 read: ROMS/Nonlinear/wetdry.F(928) — Dcrit 게이트·RHO/U/V mask 유도·부호기반 방향판정·corrector DU_avg1 결합 file:line 직접 검증(2026-07-07). 매뉴얼 교차: raw/manuals/wiki/wikitext/WET_DRY.wiki:13(one-way flux 규칙). DCRIT 입력 예제 0.10 m의 출처는 User/External/roms.in:404이다. 2026-10-14 ROMS recovery 대조 보고서 반영." # [10-14 전수 검증 정정]
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/ROMS/source-analysis/roms_barotropic_2d.md
  - concepts/compound-flooding/wetting-drying-cross-model.md
---

# ROMS 침수-노출 — `wetdry.F` (SUBROUTINE WETDRY / WETDRY_MASK_TILE)

> 소스: `.../roms/ROMS/Nonlinear/wetdry.F` (928줄). 매뉴얼: `raw/manuals/wiki/markdown/WET_DRY.md`.
> **정체**: `MASKING`+`WET_DRY` CPP 활성 시 매 fast(순압) 스텝마다 **wet/dry 마스크**(`rmask_wet`/`umask_wet`/`vmask_wet`/`pmask_wet`)를 재계산한다(`ROMS/Nonlinear/wetdry.F:38–90`, `ROMS/Nonlinear/wetdry.F:208`).
> 관련 자료는 [침수·노출 모델 대조](../../../concepts/compound-flooding/wetting-drying-cross-model.md)이다.

## 0. 진입 — init vs per-step

`Linitialize`=T 이면 `wetdry_ini_tile`(초기 draping), 이후 매 스텝 `wetdry_tile`(:38-90). fast 루프(`iif≤nfast`)에서만 마스크 갱신(:208).

## 1. Dcrit 게이트 (cell-center 판정)

```fortran
      real(r8), parameter :: eps = 1.0E-10_r8
          wetdry(i,j)=1.0_r8
# ifdef MASKING
          wetdry(i,j)=wetdry(i,j)*rmask(i,j)
# endif
          IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN
            wetdry(i,j)=0.0_r8
```

dry 판정은 `IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`이다(`ROMS/Nonlinear/wetdry.F:200–201`).
코드의 tolerance는 `eps = 1.0E-10_r8`이다(`ROMS/Nonlinear/wetdry.F:181`).
`MASKING`의 `rmask`가 0인 cell도 dry로 남는다(`ROMS/Nonlinear/wetdry.F:196–201`).
`User/External/roms.in`의 `DCRIT` 예제는 0.10 m이다(`User/External/roms.in:404`).
`read_phypar`가 이 값을 읽는다(`ROMS/Utility/read_phypar.F:972–973`).
`mod_scalars`는 `Dcrit`를 0.10 m로 초기화하지 않는다([inputs:RI1-1047](../../../_staging/recovery/compare/roms-inputs-vs-code.md#5-차이-결론)).
실제 `Dcrit`는 사용자가 제공한 `DCRIT` 입력값이다([mixing-bc-forcing:RMF1-801](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)).
RHO-point의 `rmask_wet = wetdry` 대입은 `ROMS/Nonlinear/wetdry.F:624`에 있다.

초기화에서 `IF (cff1.le.(Dcrit(ng)-h(i,j))) THEN`이면 `cff1=Dcrit(ng)-h(i,j)`로 바꾼다(`ROMS/Nonlinear/ini_fields.F:860–861`).
`rmask=0`인 셀의 masked `zeta_new`에 `Dcrit-h`를 더하면 `h+zeta=Dcrit`이다(`ROMS/Nonlinear/step2d_LF_AM3.h:1029–1032`).
이 보정은 영구 land mask에 대한 규칙이다([mixing-bc-forcing:RMF1-798](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)).
3D 두께는 시간 평균 자유수면으로 계산한다(`ROMS/Nonlinear/set_depth.F:216–222`).

## 2. ★U/V-point mask — 부호로 flux 방향 표현
```fortran
          umask_wet(i,j)=wetdry(i-1,j)+wetdry(i,j)
          IF (umask_wet(i,j).eq.1.0_r8) THEN
            umask_wet(i,j)=wetdry(i-1,j)-wetdry(i,j)
          END IF
```
- 양쪽 wet(1+1) → **2**, 양쪽 dry(0+0) → **0**, **한쪽만 wet(합=1) → 차 ±1**(왼 wet=+1, 오른 wet=−1).
- ★즉 edge mask 값이 단순 0/1 이 아니라 `{0, ±1, 2}` — **부호가 젖은 쪽 방향**을 인코딩. 뒤 momentum 에서 이 부호로 flux 를 방향 선택적으로 통제.

## 3. one-way flux — wet-dry face

매뉴얼 규칙(WET_DRY.md:22): *"If the water level is less than Dcrit, then **no flux is allowed out of that cell. Water can always flow into a cell**."*

wet-dry face에서 dry cell의 유출을 막고 유입을 허용한다(`ROMS/Nonlinear/wetdry.F:630–645`, `ROMS/Nonlinear/step2d_LF_AM3.h:2583–2588`).
두 cell이 모두 dry이면 face flux를 막는다([mixing-bc-forcing:RMF1-940](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)).

corrector(fast-time 평균) 버전이 이를 구현(:805-817):
```fortran
          cff1=wetdry(i-1,j)+wetdry(i,j)
          IF (cff1.eq.1.0_r8) THEN
            cff1=wetdry(i-1,j)-wetdry(i,j)
          END IF
          cff5=ABS(ABS(cff1)-1.0_r8)
          cff6=0.5_r8+DSIGN(0.5_r8,DU_avg1(i,j))*cff1
          umask_wet(i,j)=0.5_r8*cff1*cff5+cff6*(1.0_r8-cff5)
!                                                       catch lone ponds
          IF (DU_avg1(i,j).eq.0.0_r8) THEN
            IF ((wetdry(i-1,j)+wetdry(i,j)).le.1.0_r8) THEN
              umask_wet(i,j)=0.0_r8
            END IF
          END IF
```

`DU_avg1=0`이고 이웃 wet 합이 1 이하이면 `umask_wet`를 0으로 만든다(`ROMS/Nonlinear/wetdry.F:813–817`).

## 4. 마스크 합성·소비
```fortran
rmask_full = rmask_wet · rmask                          ! :285 정적×동적
pmask_full = MAX(pmask_wet·pmask, 2.0)                  ! :290 corner
```
`SOLVE3D` 경로는 fast 스텝이 끝나면 `wetdry(i,j)=AINT(rmask_wet_avg(i,j)*cff)`로 이진 마스크를 계산한다(`ROMS/Nonlinear/wetdry.F:217–258`). [10-14 전수 검증 정정]
`pmask_full`의 `MAX(...,2)`는 scalar rho wet mask와 다른 표현이다(`ROMS/Nonlinear/wetdry.F:285–290`, [mixing-bc-forcing:RMF1-942](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안)).

## 5. 대조 반영 사실

- wet-dry face에서 dry cell의 유출을 막고 유입을 허용한다(`ROMS/Nonlinear/step2d_LF_AM3.h:2583–2588`).
- 두 cell이 모두 dry이면 face flux를 막는다([mixing-bc-forcing:RMF1-940](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)).
- u/v mask는 두 wet cell이면 2이다(`ROMS/Nonlinear/wetdry.F:630–645`).
- 두 dry cell이면 0이다(`ROMS/Nonlinear/wetdry.F:630–645`).
- 한쪽만 wet이면 +1 또는 -1이다(`ROMS/Nonlinear/wetdry.F:630–645`).
- `DU_avg1=0`이고 이웃 wet 합이 1 이하이면 `umask_wet`를 0으로 만든다(`ROMS/Nonlinear/wetdry.F:813–817`).
- `User/External/roms.in`의 `DCRIT` 예제는 0.10 m이다(`User/External/roms.in:404`).
- 실제 `Dcrit`는 사용자가 제공한 `DCRIT` 입력값이다([mixing-bc-forcing:RMF1-801](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)).

## 6. Primary sources
- ROMS wiki [WET_DRY.wiki](../raw/manuals/wiki/wikitext/WET_DRY.wiki) — one-way flux·draping 규칙.
- 입력 예제 `User/External/roms.in:404`는 `DCRIT == 0.10d0`를 지정한다.
- 소스 `ROMS/Nonlinear/wetdry.F`는 마스크 알고리즘을 구현한다.
- 소스 `ROMS/Utility/read_phypar.F:972–973`은 `DCRIT` 입력을 읽는다.
- 계보: Warner et al. 2013 (ROMS wetting/drying, *Computers & Geosciences*) — WET_DRY 표준 참조.

## 7. 관련
- [순압 2D 노트](roms_barotropic_2d.md) — 마스크 소비처와 `DU_avg1` fast 평균 transport.
- [침수·노출 모델 대조](../../../concepts/compound-flooding/wetting-drying-cross-model.md).

## 문서와 코드 차이 (10-14 대조)

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs:RI1-1047 | 현재 노트: Dcrit 기본값 | `models/ROMS/source-analysis/roms_wetting_drying.md:7` `verification_method: "ROMS raw 직접 read: ROMS/Nonlinear/wetdry.F(928) — Dcrit 게이트·RHO/U/V mask 유도·부호기반 방향판정·corrector DU_avg1 결합 file:line 직접 검증(2026-07-07). 매뉴얼 교차: raw/manuals/wiki/markdown/WET_DRY.md(Dcrit 기본 0.10 m·one-way flux 규칙)."`<br>`models/ROMS/source-analysis/roms_wetting_drying.md:28` ``총수심 `D = ζ + h ≤ Dcrit` 이면 dry(0). **`Dcrit` 기본 0.10 m**(매뉴얼, roms.in 입력 `read_phypar.F:973`). RHO-point(cell-center) `rmask_wet = wetdry`(:624).``<br>`models/ROMS/source-analysis/roms_wetting_drying.md:64` `- **Dcrit=0.10 m 기본**: 다른 범람 모델(LISFLOOD 1e-3, SFINCS 0.05)보다 큼 — ROMS 는 해양순환 지향이라 보수적. 조간대 정밀 침수엔 하향 필요.`<br>`models/ROMS/source-analysis/roms_wetting_drying.md:68` `- ROMS wiki **WET_DRY.md**(raw/manuals/wiki) — Dcrit 0.10 m·one-way flux·draping 규칙 정본.` | `User/External/roms.in:404` `DCRIT == 0.10d0                     ! m`<br>`ROMS/Modules/mod_scalars.F:801` `real(r8), allocatable :: Dcrit(:)`<br>`ROMS/Modules/mod_scalars.F:2641` `IF (.not.allocated(Dcrit)) THEN`<br>`ROMS/Modules/mod_scalars.F:2642` `allocate ( Dcrit(Ngrids) )`<br>`ROMS/Utility/read_phypar.F:972` `CASE ('DCRIT')`<br>`ROMS/Utility/read_phypar.F:973` `Npts=load_r(Nval, Rval, Ngrids, Dcrit)`<br>`ROMS/Modules/mod_scalars.F:3889` `IF (allocated(Dcrit))             deallocate ( Dcrit )` | B 문서 오기 | User/External/roms.in의 DCRIT 예제는 0.10 m이다. read_phypar가 이 값을 읽는다. mod_scalars는 Dcrit를 0.10 m로 초기화하지 않는다. 기본값이라는 표현을 예제 값으로 고친다. |
| mixing-bc-forcing:RMF1-803 | wet_dry_masking 출력 이름 | `WET_DRY.wiki:14` <code>* For output, a variable &#91;&#91;Variables#rmask_wet&amp;#124;wet_dry_masking&#93;&#93; provides the time history of the wet/dry masking at &amp;rho;-points.</code> | `ROMS/Utility/def_his.F:605–620` `!  Define wet/dry mask on RHO-points.`<br>`!`<br>`        Vinfo( 1)=Vname(1,idRwet)`<br>`        Vinfo( 2)=Vname(2,idRwet)`<br>`        Vinfo( 3)=Vname(3,idRwet)`<br>`        Vinfo( 9)='land'`<br>`        Vinfo(10)='water'`<br>`        Vinfo(14)=Vname(4,idRwet)`<br>`        Vinfo(16)=Vname(1,idtime)`<br>`        Vinfo(21)=Vname(6,idRwet)`<br>`        Vinfo(22)='coordinates'`<br>`        Aval(5)=REAL(Iinfo(1,idRwet,ng),r8)`<br>`        status=def_var(ng, model, HIS(ng)%ncid, HIS(ng)%Vid(idRwet),    &`<br>`     &                 NF_FOUT, nvd3, t2dgrd, Aval, Vinfo, ncname,      &`<br>`     &                 SetFillVal = .FALSE.)`<br>`        IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN`<br>`ROMS/Utility/wrt_his.F:288–300` `!  Write out wet/dry mask at RHO-points.`<br>`!`<br>`      scale=1.0_dp`<br>`      gtype=gfactor*r2dvar`<br>`      status=nf_fwrite2d(ng, model, HIS(ng)%ncid, idRwet,               &`<br>`     &                   HIS(ng)%Vid(idRwet),                           &`<br>`     &                   HIS(ng)%Rindex, gtype,                         &`<br>`     &                   LBi, UBi, LBj, UBj, scale,                     &`<br>`# ifdef MASKING`<br>`     &                   GRID(ng) % rmask,                              &`<br>`# endif`<br>`     &                   GRID(ng) % rmask_wet,                          &`<br>`     &                   SetFillVal = .FALSE.)`<br>`roms-3.1:ROMS/External/varinfo.dat:2445` `'wet_dry_masking'                                  ! Input/Output`<br>`roms-3.1:ROMS/External/varinfo.dat:2446` `  'wet_dry mask'`<br>`roms-3.1:ROMS/External/varinfo.dat:2447` `  '1'                                              ! []`<br>`roms-3.1:ROMS/External/varinfo.dat:2448` `  'wet masking, scalar, series'`<br>`roms-3.1:ROMS/External/varinfo.dat:2449` `  'ocean_time'`<br>`roms-3.1:ROMS/External/varinfo.dat:2450` `  'idWmsk'`<br>`roms-3.1:ROMS/External/varinfo.dat:2451` `  'r2dvar'`<br>`ROMS/External/varinfo.yaml:763` `  - variable:       wetdry_mask_rho                                  # Input/Output`<br>`ROMS/External/varinfo.yaml:764` `    standard_name:  wet_dry_mask_at_cell_center`<br>`ROMS/External/varinfo.yaml:765` `    long_name:      wet/dry mask on RHO-points`<br>`ROMS/External/varinfo.yaml:766` `    units:          nondimensional`<br>`ROMS/External/varinfo.yaml:767` `    field:          wet-dry rho-mask`<br>`ROMS/External/varinfo.yaml:768` `    time:           ocean_time`<br>`ROMS/External/varinfo.yaml:769` `    index_code:     idRwet` | A 판 차이 | wet_dry_masking은 ROMS 3.1의 출력 이름이다. b7229401 이후 RHO점 출력 이름은 wetdry_mask_rho이다. 현재 출력 배열은 rmask_wet이다. git 판정 근거는 `71bd6f1e`(2008-03-18)·`b7229401`(2008-12-05)·`d2530aaa`(2022-02-27)이다. |
| mixing-bc-forcing:RMF1-939 | wet depth와 Dcrit default | `models/ROMS/source-analysis/roms_wetting_drying.md:28` ``총수심 `D = ζ + h ≤ Dcrit` 이면 dry(0). **`Dcrit` 기본 0.10 m**(매뉴얼, roms.in 입력 `read_phypar.F:973`). RHO-point(cell-center) `rmask_wet = wetdry`(:624).`` | `ROMS/Nonlinear/wetdry.F:181–201` `      real(r8), parameter :: eps = 1.0E-10_r8`<br>``<br>`      real(r8), dimension(IminS:ImaxS,JminS:JmaxS) :: wetdry`<br>``<br>`# include "set_bounds.h"`<br>`!`<br>`!-----------------------------------------------------------------------`<br>`! If wet/drying, compute new masks for cells with depth < Dcrit.`<br>`!-----------------------------------------------------------------------`<br>`!`<br>`! Compute local mask at RHO-points in terms of free-surface. The local`<br>`! array allows computations in the same parallel region.`<br>`!`<br>`      DO j=Jstr-1,JendR`<br>`        DO i=Istr-1,IendR`<br>`          wetdry(i,j)=1.0_r8`<br>`# ifdef MASKING`<br>`          wetdry(i,j)=wetdry(i,j)*rmask(i,j)`<br>`# endif`<br>`          IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`<br>`            wetdry(i,j)=0.0_r8`<br>`ROMS/Utility/read_phypar.F:972–973` `            CASE ('DCRIT')`<br>`              Npts=load_r(Nval, Rval, Ngrids, Dcrit)`<br>`ROMS/External/nl_roms.tmp:402–404` `! Minimum depth for wetting and drying.`<br>``<br>`       DCRIT == 0.10d0                     ! m` | B 문서 오기 | dry 판정은 `IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`이며 eps는 1.0E-10_r8이다. 동봉 입력 템플릿의 DCRIT는 0.10 m이다. 실제 Dcrit는 DCRIT 입력값이다. |
| mixing-bc-forcing:RMF1-941 | lone pond 대상 | `models/ROMS/source-analysis/roms_wetting_drying.md:50` `` `DU_avg1`(fast 평균 U-transport) 부호가 wet→dry 방향이면 그 edge 흐름 허용(유입), 반대면 차단(유출). ★유량이 0 인 고립 웅덩이(lone pond)는 강제 dry. `` | `ROMS/Nonlinear/wetdry.F:805–817` `          cff1=wetdry(i-1,j)+wetdry(i,j)`<br>`          IF (cff1.eq.1.0_r8) THEN`<br>`            cff1=wetdry(i-1,j)-wetdry(i,j)`<br>`          END IF`<br>`          cff5=ABS(ABS(cff1)-1.0_r8)`<br>`          cff6=0.5_r8+DSIGN(0.5_r8,DU_avg1(i,j))*cff1`<br>`          umask_wet(i,j)=0.5_r8*cff1*cff5+cff6*(1.0_r8-cff5)`<br>`!                                                       catch lone ponds`<br>`          IF (DU_avg1(i,j).eq.0.0_r8) THEN`<br>`            IF ((wetdry(i-1,j)+wetdry(i,j)).le.1.0_r8) THEN`<br>`              umask_wet(i,j)=0.0_r8`<br>`            END IF`<br>`          END IF` | B 문서 오기 | `DU_avg1=0`이고 이웃 wet 합이 1 이하이면 umask_wet를 0으로 만든다. receiving rho cell을 강제로 dry로 바꾸는 처리라고 쓰지 않는다. |
| mixing-bc-forcing:RMF1-802 | dry cell 유출 차단·유입 허용 | `WET_DRY.wiki:13` <code>* During computation, the water level in each cell is compared to &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;. If the water level is less than &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;, then no flux is allowed out of that cell. Water can always flow into a cell.</code> | `ROMS/Nonlinear/wetdry.F:630–635` `      DO j=JstrR,JendR`<br>`        DO i=Istr,IendR`<br>`          umask_wet(i,j)=wetdry(i-1,j)+wetdry(i,j)`<br>`          IF (umask_wet(i,j).eq.1.0_r8) THEN`<br>`            umask_wet(i,j)=wetdry(i-1,j)-wetdry(i,j)`<br>`          END IF`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:2583–2588` `#ifdef WET_DRY`<br>`            cff5=ABS(ABS(umask_wet(i,j))-1.0_r8)`<br>`            cff6=0.5_r8+DSIGN(0.5_r8,ubar(i,j,knew))*umask_wet(i,j)`<br>`            cff7=0.5_r8*umask_wet(i,j)*cff5+cff6*(1.0_r8-cff5)`<br>`            ubar(i,j,knew)=ubar(i,j,knew)*cff7`<br>`            rhs_ubar(i,j)=rhs_ubar(i,j)*cff7`<br>`ROMS/Nonlinear/wetdry.F:181` `      real(r8), parameter :: eps = 1.0E-10_r8`<br>`ROMS/Nonlinear/wetdry.F:194–201` `      DO j=Jstr-1,JendR`<br>`        DO i=Istr-1,IendR`<br>`          wetdry(i,j)=1.0_r8`<br>`# ifdef MASKING`<br>`          wetdry(i,j)=wetdry(i,j)*rmask(i,j)`<br>`# endif`<br>`          IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`<br>`            wetdry(i,j)=0.0_r8` | C 문서 누락 | `IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`이면 dry로 둔다. wet-dry 인접 face는 dry cell의 유출을 막는다. 두 cell이 모두 dry이면 face flux도 막는다. 위키의 무조건 유입 허용 설명에는 이 조건이 빠졌다. |
| mixing-bc-forcing:RMF1-866 | total depth의 tolerance | `WET_DRY.wiki:13` <code>* During computation, the water level in each cell is compared to &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;. If the water level is less than &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;, then no flux is allowed out of that cell. Water can always flow into a cell.</code> | `ROMS/Nonlinear/wetdry.F:181–201` `      real(r8), parameter :: eps = 1.0E-10_r8`<br>``<br>`      real(r8), dimension(IminS:ImaxS,JminS:JmaxS) :: wetdry`<br>``<br>`# include "set_bounds.h"`<br>`!`<br>`!-----------------------------------------------------------------------`<br>`! If wet/drying, compute new masks for cells with depth < Dcrit.`<br>`!-----------------------------------------------------------------------`<br>`!`<br>`! Compute local mask at RHO-points in terms of free-surface. The local`<br>`! array allows computations in the same parallel region.`<br>`!`<br>`      DO j=Jstr-1,JendR`<br>`        DO i=Istr-1,IendR`<br>`          wetdry(i,j)=1.0_r8`<br>`# ifdef MASKING`<br>`          wetdry(i,j)=wetdry(i,j)*rmask(i,j)`<br>`# endif`<br>`          IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`<br>`            wetdry(i,j)=0.0_r8` | C 문서 누락 | 코드의 tolerance는 `eps = 1.0E-10_r8`이다. `IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`이면 wetdry를 0으로 둔다. MASKING의 rmask가 0인 cell도 dry로 남는다. |
| mixing-bc-forcing:RMF1-867 | face mask 네 상태 | `WET_DRY.wiki:11` <code>* In the model, the wet/dry masks are stored in the &#91;&#91;Variables#rmask_wet&amp;#124;rmask_wet&#93;&#93;, &#91;&#91;Variables#umask_wet&amp;#124;umask_wet&#93;&#93;, and &#91;&#91;Variables#vmask_wet&amp;#124;vmask_wet&#93;&#93; arrays.</code> | `ROMS/Nonlinear/wetdry.F:630–645` `      DO j=JstrR,JendR`<br>`        DO i=Istr,IendR`<br>`          umask_wet(i,j)=wetdry(i-1,j)+wetdry(i,j)`<br>`          IF (umask_wet(i,j).eq.1.0_r8) THEN`<br>`            umask_wet(i,j)=wetdry(i-1,j)-wetdry(i,j)`<br>`          END IF`<br>`        END DO`<br>`      END DO`<br>`!`<br>`!  Wet/dry mask at V-points.`<br>`!`<br>`      DO j=Jstr,JendR`<br>`        DO i=IstrR,IendR`<br>`          vmask_wet(i,j)=wetdry(i,j-1)+wetdry(i,j)`<br>`          IF (vmask_wet(i,j).eq.1.0_r8) THEN`<br>`            vmask_wet(i,j)=wetdry(i,j-1)-wetdry(i,j)` | C 문서 누락 | u/v mask는 두 wet cell이면 2이다. 두 dry cell이면 0이다. 한쪽만 wet이면 +1 또는 -1이다. |
| mixing-bc-forcing:RMF1-940 | one-way 항상 유입 | `models/ROMS/source-analysis/roms_wetting_drying.md:41` `매뉴얼 규칙(WET_DRY.md:22): *"If the water level is less than Dcrit, then **no flux is allowed out of that cell. Water can always flow into a cell**."* — 마른 셀에서 나가는 flux 는 0, 들어오는 flux 는 허용(범람 전진 보장).` | `ROMS/Nonlinear/wetdry.F:630–645` `      DO j=JstrR,JendR`<br>`        DO i=Istr,IendR`<br>`          umask_wet(i,j)=wetdry(i-1,j)+wetdry(i,j)`<br>`          IF (umask_wet(i,j).eq.1.0_r8) THEN`<br>`            umask_wet(i,j)=wetdry(i-1,j)-wetdry(i,j)`<br>`          END IF`<br>`        END DO`<br>`      END DO`<br>`!`<br>`!  Wet/dry mask at V-points.`<br>`!`<br>`      DO j=Jstr,JendR`<br>`        DO i=IstrR,IendR`<br>`          vmask_wet(i,j)=wetdry(i,j-1)+wetdry(i,j)`<br>`          IF (vmask_wet(i,j).eq.1.0_r8) THEN`<br>`            vmask_wet(i,j)=wetdry(i,j-1)-wetdry(i,j)`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:2583–2588` `#ifdef WET_DRY`<br>`            cff5=ABS(ABS(umask_wet(i,j))-1.0_r8)`<br>`            cff6=0.5_r8+DSIGN(0.5_r8,ubar(i,j,knew))*umask_wet(i,j)`<br>`            cff7=0.5_r8*umask_wet(i,j)*cff5+cff6*(1.0_r8-cff5)`<br>`            ubar(i,j,knew)=ubar(i,j,knew)*cff7`<br>`            rhs_ubar(i,j)=rhs_ubar(i,j)*cff7` | C 문서 누락 | wet-dry face에서 dry cell의 유출을 막고 유입을 허용한다. 두 cell이 모두 dry이면 face flux를 막는다. always라는 요약을 이 조건으로 제한한다. |
| mixing-bc-forcing:RMF1-798 | 영구 dry cell의 Dcrit 수심 | `WET_DRY.wiki:10` <code>: Cells that are permanently dry (''i.e.'' cells with a &#91;&#91;Variables#mask_rho&amp;#124;mask_rho&#93;&#93; '''= 0''') have a water depth equal to &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;.</code> | `ROMS/Nonlinear/step2d_LF_AM3.h:1029–1032` `          zeta(i,j,knew)=zeta_new(i,j)`<br>`#if defined WET_DRY && defined MASKING`<br>`          zeta(i,j,knew)=zeta(i,j,knew)+                                &`<br>`     &                   (Dcrit(ng)-h(i,j))*(1.0_r8-rmask(i,j))`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:1022–1028` `#ifdef WET_DRY`<br>`!  Modify new free-surface to Ensure that depth is > Dcrit for masked`<br>`!  cells.`<br>`#endif`<br>`!`<br>`      DO j=Jstr,Jend`<br>`        DO i=Istr,Iend` | F 표기 차이 | 해석: `rmask=0`인 셀의 masked zeta_new에 `Dcrit-h`를 더하면 `h+zeta=Dcrit`이다. 이는 영구 land mask에 대한 규칙이다. |
| mixing-bc-forcing:RMF1-800 | 초기 depth·zeta clamp | `WET_DRY.wiki:12` <code>* In the present formulation for wetting/drying, at initialization, the model computes for each cell the total depth of water as:&lt;div class="box"&gt;D(i,j)=&#91;&#91;Variables#h&amp;#124;h(i,j)&#93;&#93;+&#91;&#91;Variables#zeta&amp;#124;zeta(i,j,1)&#93;&#93;&lt;/div&gt; If the total depth is less than a user specified minimum depth (&#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;), then the water level is increased to&lt;div class="box"&gt;&#91;&#91;Variables#zeta&amp;#124;zeta(i,j,1)&#93;&#93; = &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93; - &#91;&#91;Variables#h&amp;#124;h(i,j)&#93;&#93;&lt;/div&gt; This ''drapes'' the water level over all the land cells. The default value for &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93; is 0.10 m.</code> | `ROMS/Nonlinear/ini_fields.F:855–867` `            cff1=zeta(i,j,kstp)`<br>`# ifdef MASKING`<br>`            cff1=cff1*rmask(i,j)`<br>`# endif`<br>`# ifdef WET_DRY`<br>`            IF (cff1.le.(Dcrit(ng)-h(i,j))) THEN`<br>`              cff1=Dcrit(ng)-h(i,j)`<br>`!!            rmask_wet(i,j)=0.0_r8`<br>`!!          ELSE`<br>`!!            rmask_wet(i,j)=1.0_r8*rmask(i,j)`<br>`            END IF`<br>`# endif`<br>`            zeta(i,j,kstp)=cff1` | F 표기 차이 | 해석: `cff1<=Dcrit-h`일 때 `cff1=Dcrit-h`로 바꾸면 `h+zeta>=Dcrit`이다. 문서는 <를 쓰고 코드는 <=를 쓰지만 등호에서는 대입 결과가 같다. |
| mixing-bc-forcing:RMF1-801 | Dcrit 기본값 0.10 m | `WET_DRY.wiki:12` <code>* In the present formulation for wetting/drying, at initialization, the model computes for each cell the total depth of water as:&lt;div class="box"&gt;D(i,j)=&#91;&#91;Variables#h&amp;#124;h(i,j)&#93;&#93;+&#91;&#91;Variables#zeta&amp;#124;zeta(i,j,1)&#93;&#93;&lt;/div&gt; If the total depth is less than a user specified minimum depth (&#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93;), then the water level is increased to&lt;div class="box"&gt;&#91;&#91;Variables#zeta&amp;#124;zeta(i,j,1)&#93;&#93; = &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93; - &#91;&#91;Variables#h&amp;#124;h(i,j)&#93;&#93;&lt;/div&gt; This ''drapes'' the water level over all the land cells. The default value for &#91;&#91;Variables#Dcrit&amp;#124;Dcrit&#93;&#93; is 0.10 m.</code> | `ROMS/Modules/mod_scalars.F:2641–2644` `      IF (.not.allocated(Dcrit)) THEN`<br>`        allocate ( Dcrit(Ngrids) )`<br>`        Dmem(1)=Dmem(1)+REAL(Ngrids,r8)`<br>`      END IF`<br>`ROMS/Utility/read_phypar.F:972–973` `            CASE ('DCRIT')`<br>`              Npts=load_r(Nval, Rval, Ngrids, Dcrit)`<br>`ROMS/External/nl_roms.tmp:402–404` `! Minimum depth for wetting and drying.`<br>``<br>`       DCRIT == 0.10d0                     ! m` | F 표기 차이 | 동봉 입력 템플릿의 DCRIT 값은 0.10 m이다. 실제 Dcrit는 사용자가 제공한 DCRIT 입력값이다. |
| outputs-metadata:OMD-K005 | 평균의 젖은 횟수 정규화 | 지정 문서에 이 조건·검사를 적지 않는다. | `ROMS/Nonlinear/set_avg.F:2976` `# ifdef WET_DRY`<br>`ROMS/Nonlinear/set_avg.F:2977` `!  In wetting and drying, the sums are devided by the number of times`<br>`ROMS/Nonlinear/set_avg.F:2978` `!  that each qrid point is wet.`<br>`ROMS/Nonlinear/set_avg.F:2981` `# ifdef WET_DRY`<br>`ROMS/Nonlinear/set_avg.F:2984` `            pfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%pmask_avg(i,j))`<br>`ROMS/Nonlinear/set_avg.F:2985` `            rfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%rmask_avg(i,j))`<br>`ROMS/Nonlinear/set_avg.F:2986` `            ufac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%umask_avg(i,j))`<br>`ROMS/Nonlinear/set_avg.F:2987` `            vfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%vmask_avg(i,j))`<br>`ROMS/Nonlinear/set_avg.F:2991` `        fac=1.0_r8/REAL(nAVG(ng),r8)` | C 문서 누락 | WET_DRY의 평균 정규화 분모는 각 격자의 젖은 횟수와 1 중 큰 값이다. 예를 들어 `rfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%rmask_avg(i,j))`이다. WET_DRY가 없으면 `fac=1.0_r8/REAL(nAVG(ng),r8)`을 사용한다. |
| outputs-metadata:OMD-K006 | 진단 평균의 젖은 횟수 정규화 | 지정 문서에 이 조건·검사를 적지 않는다. | `ROMS/Utility/set_diags.F:388` `# ifdef WET_DRY`<br>`ROMS/Utility/set_diags.F:389` `!  In wetting and drying, the sums are devided by the number of times`<br>`ROMS/Utility/set_diags.F:390` `!  that each qrid point is wet.`<br>`ROMS/Utility/set_diags.F:393` `# ifdef WET_DRY`<br>`ROMS/Utility/set_diags.F:396` `            rfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%rmask_dia(i,j))`<br>`ROMS/Utility/set_diags.F:397` `            ufac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%umask_dia(i,j))`<br>`ROMS/Utility/set_diags.F:398` `            vfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%vmask_dia(i,j))`<br>`ROMS/Utility/set_diags.F:402` `        fac=1.0_r8/REAL(nDIA(ng),r8)` | C 문서 누락 | WET_DRY의 진단 평균 정규화 분모는 rmask_dia·umask_dia·vmask_dia 각각과 1 중 큰 값이다. 예를 들어 `rfac(i,j)=1.0_r8/MAX(1.0_r8, GRID(ng)%rmask_dia(i,j))`이다. WET_DRY가 없으면 `fac=1.0_r8/REAL(nDIA(ng),r8)`을 사용한다. |
| theory-numerics:RTN-116 | 건조 영역의 3D 두께=Dcrit 주장 | `Numerical_Solution_Technique.wiki:107` `*The wetting and drying only happens during the 2-D computations; the 3-D computations see a depth of <math>D_{crit}</math> in the "dry" areas.` | `ROMS/Nonlinear/step2d_LF_AM3.h:1029` `          zeta(i,j,knew)=zeta_new(i,j)`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:1030` `#if defined WET_DRY && defined MASKING`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:1031` `          zeta(i,j,knew)=zeta(i,j,knew)+                                &`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:1032` `     &                   (Dcrit(ng)-h(i,j))*(1.0_r8-rmask(i,j))`<br>`ROMS/Nonlinear/set_depth.F:216` `              z_w(i,j,k)=Zt_avg1(i,j)+(Zt_avg1(i,j)+hwater)*cff2_w`<br>`ROMS/Nonlinear/set_depth.F:217` `              z_r(i,j,k)=Zt_avg1(i,j)+(Zt_avg1(i,j)+hwater)*cff2_r`<br>`ROMS/Nonlinear/set_depth.F:218` `# ifdef ICESHELF`<br>`ROMS/Nonlinear/set_depth.F:219` `              z_w(i,j,k)=z_w(i,j,k)-ABS(zice(i,j))`<br>`ROMS/Nonlinear/set_depth.F:220` `              z_r(i,j,k)=z_r(i,j,k)-ABS(zice(i,j))`<br>`ROMS/Nonlinear/set_depth.F:221` `# endif`<br>`ROMS/Nonlinear/set_depth.F:222` `              Hz(i,j,k)=z_w(i,j,k)-z_w(i,j,k-1)` | B 문서 오기 | 3D 두께는 시간 평균 자유수면으로 계산한다. 영구 masked cell 보정과 동적 dry cell을 구분한다. |
| tools-guides:RTG-1957 | Dcrit의 적용 조건 | `Frequently_Asked_Questions.wiki:190` `a critical water column thickness (<span class="red">Dcrit</span>) in wetting and drying` | `ROMS/Utility/read_phypar.F:973` `              Npts=load_r(Nval, Rval, Ngrids, Dcrit)`<br>`ROMS/Nonlinear/wetdry.F:200` `          IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`<br>`ROMS/Nonlinear/wetdry.F:201` `            wetdry(i,j)=0.0_r8`<br>`ROMS/Nonlinear/wetdry.F:3` `#ifdef WET_DRY` | C 문서 누락 | WET_DRY 경로는 `IF ((zeta(i,j)+h(i,j)).le.(Dcrit(ng)+eps)) THEN`일 때 `wetdry(i,j)=0.0_r8`을 설정한다. |
