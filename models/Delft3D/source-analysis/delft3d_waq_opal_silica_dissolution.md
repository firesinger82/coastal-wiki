---
title: "Delft3D WAQ opal 규소 용해 source-analysis — dissi.f90 (규조 Si 영양염 재순환, 2차/1차 옵션)"
model: Delft3D
component: waq-process
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw 직접 read: src/engines_gpl/waq/waq_process/dissi.f90(153) 전수 — 용해 flux식(SWDISSI 2차/1차)·porosity 게이트·간극수 CSID/POROS 보정 file:line 직접 검증(2026-07-07)."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_waq_process_library.md
  - models/Delft3D/source-analysis/delft3d_waq_algae_models.md
  - models/Delft3D/source-analysis/delft3d_waq_sediment_denitrification.md
---

# Delft3D WAQ opal 규소 용해 — `dissi.f90` (SUBROUTINE DISSI)

> 소스: `.../src/engines_gpl/waq/waq_process/dissi.f90` (153줄, `module m_dissi`).
> **정체**: 생물기원 규소(**opal silicate → 용존 규산 dissolved silicate**) 용해 flux. 규조(diatom) 사후 opal 프러스툴이 재용해되어 **Si 영양염을 수주로 되돌리는 재순환** — 규조 blooms 의 Si 제한(N·P 외 제3 영양염)을 여는 축. 기존 WAQ 노트(DO·N·P·조류·탄소계)가 안 다룬 **규소 순환 신설**.

## 0. flux process
`FL(1+IFLUX)`에 용해율 기입(:129) + 출력 포인터 IP9 에도 FSOL 복제(:130) — 상태변수 OPAL 감소·CSID(용존 Si) 증가 구동. active 셀만(`BTEST(IKNMRK,0)`, :91).

## 1. 용해 flux — 2차(포화의존) / 1차 옵션
```fortran
TEMPC = TC**(TEMP - 20.0)                             ! :107 Arrhenius형 온도계수
IF (NINT(SWDISSi) == 0) THEN                          ! :109 SWDISSI=0 : 2차(기본 물리)
    FSOL = KSOL * TEMPC * OPAL * (CSIDE - CSID/POROS) ! :110
ELSE                                                  ! SWDISSI=1 : 1차
    FSOL = KSOL * TEMPC * OPAL                         ! :112
ENDIF
```
- **2차식**: 용해속도 `KSOL`[m³/gSi/d] × 온도 × opal 농도 × **미포화도** `(CSIDE − CSID/POROS)`. 포화농도 `CSIDE`에 근접하면 용해 둔화(평형 접근), 초과하면 음수(재침전).
- **1차식**(SWDISSI=1): 포화 완전 무시 — opal 농도에만 비례(항상 undersaturated 가정, 표층수·강한 sink 근사).
- `CSIDE`(포화농도)는 입력 파라미터 — 온도 내생 계산 아님(사용자가 T별로 지정 필요, findings).

## 2. ★간극수 농도 보정 `CSID/POROS`
2차식의 미포화도가 `CSIDE − CSID/POROS`(:110) — 벌크 용존 Si `CSID`를 공극률 `POROS`로 나눠 **실제 공극수(pore-water) 농도**로 환산 후 포화농도와 비교. 저니(sediment)에서 물이 차지하는 부피만이 용해 반응 매질이므로, 벌크 농도를 그대로 쓰면 미포화도를 과대평가. 수주(POROS≈1)에서는 보정 무시할 만하나 저니(POROS<1)에서 유의.

## 3. porosity 게이트
```fortran
IF (POROS > 0.05) THEN ... ELSE FSOL=0.0 + 경고     ! :105, :113-124
```
`POROS ≤ 0.05`(거의 고체) 셀은 용해 0 + 로그 경고(25회 상한 후 억제, :117-124) — `CSID/POROS` 0-분할 방지 + 비물리 영역 차단.

## 4. ★주요 findings
- **★2차 기본, 포화 되먹임**: SWDISSI=0(2차)이 물리 표준 — `CSIDE`에 접근하면 용해 정지, 초과 시 음 flux(재침전). 1차(SWDISSI=1)는 이 되먹임 제거(무한 undersaturation) — 표층 규조 sink 우세 영역 근사이나 저니 평형 오표현 위험.
- **★간극수 보정 `CSID/POROS`**: 저니 포화도 판정의 핵심 — 벌크 vs 공극수 농도 구분. 수주-전용 적용 시엔 영향 작으나 sediment diagenesis 결합 시 필수.
- **CSIDE 상수 입력**: 포화농도가 온도 함수로 내생 계산되지 않음(용해 kinetics만 온도의존 TC^(T−20)) — 사용자 파라미터화 필요, 온도-포화 결합은 미모델.
- **porosity 0.05 하한**: 압밀 저니·비다공 셀 배제(0-분할 가드 겸).
- **음수 flux 미클램프**: `(CSIDE−CSID/POROS)<0`(과포화) 시 FSOL<0 = 재침전 허용 — opal 재형성 방향. 물리적으론 규산 침전이나, opal 상태변수 음수 방지는 상위 적분기 몫.

## 5. Primary sources
- Delft3D-WAQ Processes Library — opal 용해 process(`DisSi`) 정의·파라미터(KSOL·CSIDE·TC·SWDISSI). in-code 문헌 인용 없음(경험 kinetics), 정의는 [[delft3d_waq_process_library]].

## 6. 관련
- [[delft3d_waq_algae_models]] — 규조 성장이 opal 생산(본 용해의 상류); Si 제한
- [[delft3d_waq_process_library]] — process 호출 규약·인접 영양염 kinetics
- [[delft3d_waq_sediment_denitrification]] — 인접 저니 flux process(N; 본 노트는 Si)
