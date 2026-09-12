---
title: "XBeach 활성 파랑 경계 생성 — waveparamsnew.F90의 스펙트럼·bound 장파"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_update.f90 (2768) + waveparamsnew.F90(spectral_wave_bc 98, read_swan_file 418) 직접 read — generate_wave_boundary_surfbeat(73), generate_qbcf bound long wave(2460: Herbers1994 eq.1 E=2D²Sf²df, Van Dongeren2003 eq.21 phase/eq.22 angle theta3=atan2(KKy,KKx)) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — bound long wave 생성·SWAN 연동 chain verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_swan_handoff.md
  - models/XBeach/source-analysis/wave/xbeach_wave_boundary.md
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
  - models/SWAN/source-analysis/swan-output-formats.md
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "활성 파랑 생성 경로와 차주파수 에너지·위상·진폭 부호를 `waveparamsnew.F90`에 맞춤"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: 활성 파랑 생성 경로와 차주파수 에너지·위상·진폭 부호를 `waveparamsnew.F90`에 맞춤. 위 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인을 뜻하지 않는다. [원문 구간·SHA와 재사용 근거](../../../_staging/total-read/model-audit/XBeach/connectivity/corrections-20260912/evidence.json)에 결속했다.

# XBeach 파랑 경계 생성과 SWAN 입력

현재 저장 소스의 활성 경로는 `boundaryconditions.F90`의 `wave_bc`가 `waveparamsnew.F90`에 정의된 `spectral_wave_bc_module::spectral_wave_bc`를 호출하는 구조다. `wave_boundary_update.f90`의 `generate_wave_boundary_surfbeat`는 현재 조사한 Autotools/Visual Fortran/IFX 모델 대상의 컴파일 목록에 없다. 이 노트의 생성 알고리즘은 **활성 `waveparamsnew.F90` 기준**이다. (`boundaryconditions.F90:39-44, 205-250`; `waveparamsnew.F90:1-11, 98-106`; [[xbeach-build-mode-connectivity]] 및 결속된 `build-map.json`)

## 1. 입력과 생성 진입

현재 `wbctype` 입력 이름 `jonstable`은 내부 상수 `WBCTYPE_JONS_TABLE`에 대응한다. (`params.F90:321-334`)

초기 경계 생성에서 stationary의 `jonstable`은 테이블을 직접 읽는다. `parametric/jonstable`의 스펙트럼 생성 호출에는 비stationary 조건이 있고, SWAN/vardens 호출과 함께 `xmaster`에서 실행한다. `reuse`와 직접 시계열 입력은 별도 분기다. (`boundaryconditions.F90:205-250`)

`spectral_wave_bc`는 생성 루프에서 `read_spectrum_input`을 호출하고, 그 안에서 다음 reader를 선택한다. `reuseall`이면 새 생성을 건너뛰는 경로가 있으므로 매 호출마다 다시 생성한다고 해석하지 않는다. (`waveparamsnew.F90:128-151, 167-181, 408-426`)

| 입력 | 스펙트럼 reader | 호출 위치 |
|---|---|---|
| `parametric`, `jonstable` | `read_jonswap_file` | `waveparamsnew.F90:415` |
| `swan` | `read_swan_file` | `:418` (정의는 `:936`) |
| `vardens` | `read_vardens_file` | `:421` |

SWAN 스펙트럼 파일의 해석은 [[xbeach_swan_handoff]], 경계 파일·보간 설정은 [[xbeach_wave_boundary]]를 따른다.

## 2. 활성 생성 순서와 모드 조건

입력 스펙트럼에 대해 `interpolate_spectrum`, 성분과 시간축 선정, 방향분산·성분 특성 계산, Fourier 성분 구성을 차례로 수행한다. 이어지는 생성 호출은 `nonhspectrum`, `swkhmin`, `order`, `highcomp`에 따라 달라진다. (`waveparamsnew.F90:167-290`)

| 조건 | 생성 호출 |
|---|---|
| `nonhspectrum==0`, `swkhmin<=0` | `generate_ebcf`로 단파 에너지 시계열 생성 |
| `nonhspectrum==0`, `swkhmin>0` | `generate_ebcf`와 `generate_swts` 호출 |
| `nonhspectrum!=0` | 성분 방향 분배 후 `generate_swts` 호출 |
| `nonhspectrum==0` 또는 `nonhspectrum==1`이면서 `order>1` | `generate_qbcf` 호출 |
| `nonhspectrum==1`, `highcomp==1`, `order>1` | `generate_secondorder` 추가 호출 |
| `nonhspectrum==1` | `generate_nhtimeseries_file`로 nonh 시계열 기록 |

## 3. Bound 장파: `generate_qbcf`

이 루틴의 정의는 `waveparamsnew.F90:2695`다. 단파 성분 쌍의 차주파수 `deltaf=m*dfgen`과 파수벡터 차를 구성하고, 차파의 속도를 `nmax`로 제한한다. 코드 주석은 상호작용 계수 `D`가 Okihiro 식의 **수면변위용 계수**임을 명시한다. 예전 바닥압력→수면변위 보정 곱셈은 주석 처리되어 있다. (`:2783-2828`)

에너지 배열의 실제 대입은 다음과 같다. `j`는 경계 위치, `i`와 `i+m`은 서로 다른 주파수 성분이다.

```text
Eforc(m,i) = 2 D(m,i)^2 S(j,i) S(j,i+m) dfgen
Abnd(m,i) = sqrt(2 Eforc(m,i) dfgen) sign(1,D(m,i))
```

`Sfold==1`이면 위 `S`에 `Sfinterpq`, 그 외에는 `Sfinterp`를 쓴다. 따라서 주석의 축약형 `S²`를 같은 주파수 성분의 제곱으로 옮기면 실제 쌍별 곱과 달라진다. (`:2872-2899`)

위상도 첫 대입만 읽으면 안 된다. `dphi3=pi+위상차`는 바로 다음 대입에서 **pi 없는 위상차**로 덮어쓴다. `D`의 부호는 위의 진폭에 반영된다. 진행 방향은 `atan2(KKy,KKx)`이고, 공간 위상·역 FFT·taper를 거쳐 시계열을 만든다. 주파수 하한과 `fcutoff`에 의한 상호작용 제외도 적용된다. (`:2831-2854, 2902-2935`)

`nonhspectrum==0`의 기록 분기에서 `order==1`은 `q(:,:,1)`(x방향 유량)과 `q(:,:,4)`(수면변위)을 0으로 만든다. 여기서 모든 유량 성분을 0으로 만든다고 일반화하지 않는다. `nonhspectrum==1`의 경로는 계산한 성분을 nonh 속도·수면변위 시계열에 더한다. (`:2964-2982, 3032-3037`)

## 4. 생성 결과의 소비와 구형 코드의 위치

surfbeat 경계 파일은 `boundaryconditions.F90`에서 시각 보간하고, 유량을 회전·수심 변환하여 `ui/vi`로 소비한다. 내부 에너지 전파는 [[xbeach_wave_action_balance]], 흐름 경계는 [[xbeach_flow_boundary_conditions]]에서 다룬다. (`boundaryconditions.F90:655-671`)

`wave_boundary_main/init/update/datastore`와 `wave_bc_nextgen`은 조사 대상 빌드의 미포함 파일이다. 기존 분석에서 이들의 API·배열을 읽었다는 사실은 현재 실행 경로의 근거가 아니다. 활성 모듈과 구형 구현의 수식·위상 처리가 같다는 판정도 하지 않는다. ([[xbeach-build-mode-connectivity]]; 이 정정의 `evidence.json`에 결속된 `build-map.json`)
