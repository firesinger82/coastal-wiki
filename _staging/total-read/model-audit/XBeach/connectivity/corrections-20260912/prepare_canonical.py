"""Reproducible candidates from the frozen pre-correction commit."""
import difflib
import hashlib
import json
import subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
BASE = 'e11a8c8'
changes = {}

def read(rel):
    return subprocess.check_output(['git', 'show', f'{BASE}:models/XBeach/{rel}'], cwd=ROOT).decode()

def note(rel, text, scope):
    depth = len(Path(rel).parts) + 1
    evidence = '../' * depth + '_staging/total-read/model-audit/XBeach/connectivity/corrections-20260912/evidence.json'
    head, body = text[4:].split('\n---\n', 1)
    head += '\nsource_correction_date: 2026-09-12\nsource_correction_by: "Codex"\nsource_correction_scope: ' + json.dumps(scope, ensure_ascii=False) + '\nsource_correction_human_approval: not-issued'
    body = '\n> **2026-09-12 AI 출처 정정**: ' + scope + '. 위 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인을 뜻하지 않는다. [원문 구간·SHA와 재사용 근거](' + evidence + ')에 결속했다.\n' + body
    changes['models/XBeach/' + rel] = '---\n' + head + '\n---\n' + body

rel = 'source-analysis/xbeach_intrawave_sediment_transport.md'
s = read(rel)
a = s.index('> **정체**:')
b = s.index('## 1. Nielsen2006')
s = s[:a] + '''> `transus`에서 `sedtransform` 외에 직접 호출하는 `Nielsen2006`, `intra_sedtr`, `mccall_vanrijn`을 다룬다. 입력으로 허용하는 이름 수와 실제 공식 호출 분기는 다르다.

## 0. `form` 입력과 `transus` 호출

`sedtrans==1`일 때 `params.F90:928-949`는 `intrasedtr`를 포함한 **12개 이름**을 입력 목록에 등록한다. `parmapply`는 이름을 상수 값으로 바꾸며, 과거 숫자 문자열 `1`~`12`는 각각 상수 값 `0`~`11`에 대응한다. 일반 설정의 기본값은 두 번째 이름 `vanthiel_vanrijn`, `useXBeachGSettings!=0`이면 다섯 번째 이름 `mccall_vanrijn`이다. (`paramsconst.F90:80-91`; `readkey.F90:762-804, 806-824, 866-875`)

| 입력 이름 | 상수 값 | `transus`가 직접 호출하는 공식 루틴 |
|---|---|---|
| `soulsby_vanrijn`, `vanthiel_vanrijn`, `vanrijn1993` | 0, 1, 2 | `sedtransform` |
| `nielsen2006` | 3 | `Nielsen2006` |
| `mccall_vanrijn` | 4 | `mccall_vanrijn` |
| `intrasedtr` | 11 | `intra_sedtr` |
| `wilcock_crow`, `engelund_fredsoe`, `mpm`, `wong_parker`, `fl_vb`, `fredsoe_deigaard` | 5~10 (표기 순서) | 해당 SELECT에 공식 호출 분기 없음 |

이 SELECT에는 `DEFAULT`도 없다. 따라서 5~10은 위 네 공식 루틴을 호출하지 않은 채 뒤의 공통 수송 계산으로 진행한다. 이를 입력 오류 종료나 특정 수치 결과로 해석하지 않는다. `Nielsen2006`과 `mccall_vanrijn` 분기만 `bulk==0`이면 호출 직후 `transus`에서 복귀한다. (`morphevolution.F90:173-204`; `transus` 상위 호출 조건은 `libxbeach.F90:293-310`)

`mccall_vanrijn` 내부에 `FORM_WILCOCK_CROW`와 `FORM_ENGELUND_FREDSOE` 비교가 존재하지만, 그것만으로 해당 입력 값이 이 루틴에 도달한다고 볼 수 없다. 직접 호출자는 위 SELECT다. (`morphevolution.F90:2565-2576`)

''' + s[b:]
s = s.replace('> ★**`FORM_INTRASEDTR=11` 은 `form=` 키워드로 사용자 설정 불가**(params.F90:933-936 목록에 없음) — 비정수압 run 내부 자동선택. [[xbeach_nonh]](수력만 문서화)의 **유사 짝**.', '> **`form=intrasedtr`는 사용자가 설정할 수 있다.** `params.F90:932-943`의 허용 이름과 `morphevolution.F90:182-183`의 호출이 직접 연결된다. nonh용이라는 루틴 헤더는 모드가 이 공식을 자동 선택한다는 근거가 아니다.')
a = s.index('## 4. 주요 findings')
b = s.index('## 5. Primary sources')
s = s[:a] + '''## 4. 적용 범위

[[xbeach_morphology]]의 평형농도 설명은 `sedtransform`의 세 입력 값에 해당한다. 전체 입력 목록은 12개이고, 현재 `transus`의 직접 공식 호출은 여섯 값에서 네 루틴으로 연결된다. `intrasedtr`의 명시 입력과 Nielsen/McCall의 `bulk==0` 조기 복귀를 구분해야 한다. (§0 원문 근거)

''' + s[b:]
s = s.replace('(본 노트가 intra-wave 3형식 보완, 3→6형식 정정)', '(세 평형농도 입력의 계산 설명; 전체 입력·호출 대응은 본 노트 §0)')
note(rel, s, '`form`의 허용 입력 12개와 실제 공식 호출 네 루틴, `intrasedtr` 명시 입력을 구분')

rel = 'source-analysis/xbeach_morphology.md'
s = read(rel)
a = s.index('Selected in `transus`')
b = s.index('`sedtransform` workflow', a)
s = s[:a] + '''This section describes the three equilibrium-formula inputs that call `sedtransform`: `soulsby_vanrijn`, `vanthiel_vanrijn`, and `vanrijn1993`. They are not the full `form` input list.

| Accepted `form` input | Internal value | Direct formula call in `transus` |
|---|---|---|
| `soulsby_vanrijn`, `vanthiel_vanrijn`, `vanrijn1993` | 0, 1, 2 | `sedtransform` |
| `nielsen2006` | 3 | `Nielsen2006`; returns immediately if `bulk==0` |
| `mccall_vanrijn` | 4 | `mccall_vanrijn`; returns immediately if `bulk==0` |
| `intrasedtr` | 11 | `intra_sedtr` |
| `wilcock_crow`, `engelund_fredsoe`, `mpm`, `wong_parker`, `fl_vb`, `fredsoe_deigaard` | 5~10, in this order | No formula call in this SELECT; continues after it |

The input reader accepts all 12 names, including `intrasedtr`. Legacy numeric strings `1`~`12` map to values `0`~`11`. The default name is `vanthiel_vanrijn` for ordinary settings and `mccall_vanrijn` when `useXBeachGSettings!=0`. This is input/dispatch evidence, not a numerical validation of the six values lacking a SELECT branch. (`params.F90:928-949`; `paramsconst.F90:80-91`; `readkey.F90:762-804`; `morphevolution.F90:173-204`; [[xbeach_intrawave_sediment_transport]] §0)

''' + s[b:]
s = s.replace('## Decision Guide', '## Decision Guide — equilibrium transport and morphology settings')
s = s.replace('- Soulsby-Van Rijn is the default workhorse. Van Thiel-Van Rijn is preferred for surf zone (wave-current interaction in critical velocity).', '- The ordinary input default is `form=vanthiel_vanrijn`; `useXBeachGSettings!=0` changes it to `mccall_vanrijn` (`params.F90:945-949`).')
note(rel, s, '세 평형농도 공식의 설명 범위와 전체 `form` 입력·호출 분기를 구분')

rel = 'source-analysis/xbeach_wave_boundary_generation.md'
s = read(rel)
s = s[:s.index('# XBeach wave boundary 생성 & SWAN 연동')]
s = s.replace(s.splitlines()[1], 'title: "XBeach 활성 파랑 경계 생성 — waveparamsnew.F90의 스펙트럼·bound 장파"')
s += '''# XBeach 파랑 경계 생성과 SWAN 입력

현재 저장 소스의 활성 경로는 `boundaryconditions.F90`의 `wave_bc`가 `waveparamsnew.F90`에 정의된 `spectral_wave_bc_module::spectral_wave_bc`를 호출하는 구조다. `wave_boundary_update.f90`의 `generate_wave_boundary_surfbeat`는 현재 조사한 Autotools/Visual Fortran/IFX 모델 대상의 컴파일 목록에 없다. 이 노트의 생성 알고리즘은 **활성 `waveparamsnew.F90` 기준**이다. (`boundaryconditions.F90:39-44, 205-250`; `waveparamsnew.F90:1-11, 98-106`; [[xbeach-build-mode-connectivity]] 및 결속된 `build-map.json`)

## 1. 입력과 생성 진입

초기 경계 생성에서 stationary의 `jons_table`은 테이블을 직접 읽는다. `parametric/jons_table`의 스펙트럼 생성 호출에는 비stationary 조건이 있고, SWAN/vardens 호출과 함께 `xmaster`에서 실행한다. `reuse`와 직접 시계열 입력은 별도 분기다. (`boundaryconditions.F90:205-250`)

`spectral_wave_bc`는 생성 루프에서 `read_spectrum_input`을 호출하고, 그 안에서 다음 reader를 선택한다. `reuseall`이면 새 생성을 건너뛰는 경로가 있으므로 매 호출마다 다시 생성한다고 해석하지 않는다. (`waveparamsnew.F90:128-151, 167-181, 408-426`)

| 입력 | 스펙트럼 reader | 호출 위치 |
|---|---|---|
| `parametric`, `jons_table` | `read_jonswap_file` | `waveparamsnew.F90:415` |
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
'''
note(rel, s, '활성 파랑 생성 경로와 차주파수 에너지·위상·진폭 부호를 `waveparamsnew.F90`에 맞춤')

rel = 'source-analysis/wave/xbeach_wave_boundary.md'
s = read(rel)
s = s.replace('what the `wave_boundary_datastore.F90` persists', 'what the build-excluded prototype `wave_boundary_datastore.f90` persists')
s = s.replace('legacy `waveparams.F90` vs newer `waveparamsnew.F90`', 'legacy `waveparams.F90` vs active `waveparamsnew.F90`')
s = s.replace('- `waveparamsnew.F90:98, 366-2974` — newer spectral path.', '- `waveparamsnew.F90:98, 340-426` — active spectral entry and reader dispatch.')
s = s.replace('— newer interface main.', '— build-excluded prototype interface main.')
s = s.replace('- `wave_boundary_update.f90:312` — spectral reader dispatch.', '- `wave_boundary_update.f90:312` — build-excluded prototype reader dispatch.')
s = s.replace('- `wave_boundary_datastore.f90:16-63` — persistent state.', '- `wave_boundary_datastore.f90:16-63` — build-excluded prototype state.')
a = s.index('Files involved:')
b = s.index('Actual XBeach runtime dispatch', a)
s = s[:a] + '''The active spectral provider is `spectral_wave_bc_module` from `waveparamsnew.F90` (`boundaryconditions.F90:43`; `waveparamsnew.F90:1-11, 98-106`). Its `read_spectrum_input` dispatches JONSWAP/table, SWAN and vardens to the respective readers (`waveparamsnew.F90:408-426`). The `wave_boundary_main/init/update/datastore` and `wave_bc_nextgen` files are absent from the model compile lists inspected in [[xbeach-build-mode-connectivity]]. Their API descriptions below are historical prototype descriptions.

''' + s[b:]
s = s.replace('| Spectral `parametric/jons_table/swan/vardens` | Calls `spectral_wave_bc` | `:238` |', '| `parametric/jons_table` with nonstationary mode; `swan/vardens` | Calls `spectral_wave_bc` on `xmaster` | `:237-245` |')
s = s.replace('**Newer** (`waveparamsnew.F90`):', '**Active spectral provider** (`waveparamsnew.F90`):')
s = s.replace('`wave_boundary_main.f90:256` — in-memory analogue', '**Build-excluded prototype:** `wave_boundary_main.f90:256` — in-memory analogue')
s = s.replace('## F. Datastore (`wave_boundary_datastore.F90`)\n\nPersists newer-interface state across calls. Holds:', '## F. Prototype datastore (`wave_boundary_datastore.f90`; build-excluded)\n\nThis historical prototype declares state across calls. It is not the datastore of the active `spectral_wave_bc_module` path. The build exclusion is recorded in [[xbeach-build-mode-connectivity]]. Its declarations hold:')
s = s.replace('- 1st = short-wave energy only.\n- 2nd = adds bound long-wave steering.', '- The active generation call uses `nonhspectrum` and `order` together; see [[xbeach_wave_boundary_generation]] §2.\n- In `generate_qbcf`, `nonhspectrum==0` and `order==1` zero the x-flux and elevation slots (`waveparamsnew.F90:2964-2979`), not every flux slot.')
s = s.replace('zeroes generated long-wave flux/elevation', 'zeroes the generated x-flux/elevation slots')
s = s.replace('| Sea-swell only, no IG | `order=1` |', '| First-order boundary steering | `order=1`; observe the component-specific behavior above |')
s = s.replace('Use newer `waveparamsnew.F90` path (default)', 'The active `waveparamsnew.F90` provider')
note(rel, s, '빌드 미포함 경계 prototype의 API·datastore와 활성 스펙트럼 경로를 구분')

rel = 'source-analysis/xbeach_wave_action_balance.md'
s = read(rel)
s = s.replace('(wave_instationary.F90 + wave_directions.F90) —', '(wave_instationary.F90 + wave_stationary_directions.F90) —', 1)
s = s.replace('> `wave_instationary.F90`(479) + `wave_directions.F90`(400) 직접 read.', '> 활성 surfbeat 에너지 전파는 `wave_instationary.F90`, 조건부 정상 방향 계산은 `wave_stationary_directions.F90`에 연결된다 (`wave_timestep.F90:75-114`).')
a = s.index('## 5. Stationary 모드')
b = s.index('## 7. 연결', a)
s = s[:a] + '''## 5. 활성 정상 계산과 구형 파일

현재 `wave_timestep`은 stationary에서 `wave_stationary_directions(s,par,0)`을 호출한다. 이때 `callType=0`은 `s%ntheta`를 사용한다. surfbeat의 `single_dir` 경로도 같은 루틴을 `callType=1`로 호출하지만, 이때는 `s%ntheta_s`로 평균 방향을 계산한다. 호출은 `wavint` 간격 조건과 새 stationary 경계 조건으로 제어하며, surfbeat single_dir에는 `t==dt` 조건도 있다. (`wave_timestep.F90:75-114`; `wave_stationary_directions.F90:33-49, 71-76`)

`wave_directions.F90`와 `wave_stationary.F90`는 현재 조사한 빌드 목록에 포함되지 않는다. 두 파일을 읽은 이전 검증 이력은 보존하되 현재 solver로 귀속하지 않는다. ([[xbeach-build-mode-connectivity]]; 상세는 [[xbeach_wave_stationary]])

## 6. 모드별 활성 wave 호출

| 모드 | 호출 | 조건 |
|---|---|---|
| stationary | `wave_dispersion(...,0)` → `wave_stationary_directions(...,0)` | `wavint` 또는 새 경계 조건에 따른 정상 계산 |
| surfbeat, `single_dir==1` | 평균장 갱신 → 조건부 `wave_dispersion(...,1)`과 `wave_stationary_directions(...,1)` | 정상 방향 계산 (`wavint` 조건, 새 경계 조건 또는 `t==dt`); 이후 에너지 전파는 별도 실행 |
| surfbeat | `wave_dispersion(...,0 또는 2)` → `wave_instationary` | 매 파랑 스텝의 에너지 전파; WCI 조건에 따라 분산 계산 인수 선택 |

위 표는 `wave_timestep.F90:75-114`의 stationary/surfbeat 분기다. nonh의 수력 계산은 [[xbeach_mode_dispatch]]와 [[xbeach_nonh]]를 따른다.

''' + s[b:]
note(rel, s, 'stationary와 surfbeat single_dir의 활성 공유 루틴·callType·방향 격자를 정정')

rel = 'source-analysis/xbeach_wave_stationary.md'
s = read(rel)
s = s[:s.index('# XBeach stationary wave 모드')]
s = s.replace(s.splitlines()[1], 'title: "XBeach 정상 파랑 계산 — 활성 wave_stationary_directions와 구형 wave_stationary 구분"')
s += '''# XBeach 정상 파랑 계산

현재 `wave_timestep`의 stationary 호출 대상은 `wave_stationary_directions(s,par,0)`이다. 같은 루틴을 surfbeat `single_dir`의 평균 방향 계산에도 다른 `callType`으로 사용한다. 이름이 유사한 `wave_stationary.F90`와 `wave_directions.F90`는 조사한 Autotools/Visual Fortran/IFX 모델 빌드 목록에 포함되지 않는다. (`wave_timestep.F90:75-114`; [[xbeach-build-mode-connectivity]])

## 1. `wave_stationary` — 구형·빌드 미포함 구현

기존 원문 판독은 `wave_stationary.F90`의 `wave_stationary`가 반복 cross-shore sweep과 `Herr/thetaerr` 수렴을 사용하는 구현임을 기록했다 (`wave_stationary.F90:7, 34, 152`). 이 설명은 해당 구형 파일의 내용이며, 현재 stationary 모드의 호출 대상을 뜻하지 않는다. 기존 `verification_*`의 두 파일 판독 이력도 이 구분을 따른다.

## 2. 활성 `wave_stationary_directions`

루틴은 `callTypeStationary=0`, `callTypeDirections=1`을 구분하고 사용할 방향 격자를 선택한다. 따라서 이 루틴 자체를 single_dir와 대비되는 전용 full-directional 경로로 설명하면 두 호출 역할을 놓친다. (`wave_stationary_directions.F90:33-49, 71-76`)

| 호출자 모드 | 호출 인수 | 방향 격자 | 계산 주기 |
|---|---|---|---|
| stationary | `callType=0` | `s%ntheta` | `abs(mod(t,wavint))<0.001*dt` 또는 `newstatbc==1` |
| surfbeat, `single_dir==1` | `callType=1` | `s%ntheta_s` | 평균장 갱신 뒤 `abs(mod(t,wavint))<0.001*dt`, `newstatbc==1` 또는 `t==dt` |

두 경로 모두 정상 계산 전에 해당 인수의 `wave_dispersion`을 호출한다. surfbeat의 시간에 따른 에너지 전파는 이 방향 계산 뒤 `wave_instationary`에서 별도로 진행한다. (`wave_timestep.F90:75-114`)

## 3. 연결

- [[xbeach_wave_action_balance]] — surfbeat 에너지·roller 전파
- [[xbeach_mode_dispatch]] — stationary/surfbeat/nonh 실행 분기
- [[xbeach_single_dir]] — surfbeat 평균 방향 계산
- [[xbeach-build-mode-connectivity]] — 현재 빌드 목록과 비활성 파일의 근거
'''
note(rel, s, '구형 wave_stationary의 역할을 한정하고 현재 정상 계산의 두 호출을 구분')

rel = 'manual-notes/xbeach-manual-equation-code-contracts.md'
s = read(rel).replace('파수 보정·지형 갱신"', '파수 보정·지형 갱신·침투"', 1)
a = s.index('이 두 수식 묶음의 의미 대조 결과이며')
s = s[:a] + '''## 불포화 침투식: 판본 표기와 시간 이산화

원본 WMF와 MathType Native 판독에서 Kingsday `oleObject133`, Master `oleObject143/81`의 분수 뒤 `1` 앞에는 연산자가 없다. Kingsday `oleObject70` 대응식에는 `+1`이 있다. 이 차이는 원본의 표기 차이로 남긴다. 구현이 더하기를 쓴다는 사실로 원본 저자의 미기재 의도를 확정하거나 원본 식을 수정하지 않는다. ([원본 객체·주변 문단·코드와 대수 검산](../../../_staging/total-read/model-audit/XBeach/connectivity/infiltration-document-code-comparison.json), [객체별 복원 PDF p.1 시각 판독](../../../_staging/total-read/model-audit/XBeach/connectivity/manuals-docx-read/conditional-visual-read/receipt.json))

`groundwater.F90:1554-1573`의 기본 관계는 다음과 같다. `d=dinfil`, `h=hh`, `D=dt/por`로 놓으며, 여기서 `D`는 시간 이산화 계수다.

```text
w = K (1 + h/(d + D w))
D w² + (d − D K) w − K(d+h) = 0
w = (−d + D K + sqrt(d² + 2D dK + 4D hK + D² K²))/(2D)
```

이 양의 근은 `K>0, d>0, h>=0, D>0`에서 코드의 계산과 대수적으로 대응한다. 층류 분기와 난류 첫 추정에는 `par%kz`, 난류 반복에는 갱신한 `kze`가 들어간다. 기존 세 수치 예의 대수 잔차는 0 또는 약 `3.4e-17`이었으며, 이는 전체 Fortran 실행 시험이 아니다. (`groundwater.F90:1574-1630`; 위 대수 검산 기록)

실제 반환 `infil`은 이 순간 식의 `w` 그대로가 아니다. 코드가 불포화 상태로 남는 시간 비율 `fracdt`를 `[0,1]`로 제한하고 `infil=vest*fracdt`를 계산하므로, 반환량은 전체 스텝에 대한 평균 침투속도다. 이어 표층 가용수 `max((hh-eps)/dt,0)`로 제한한다. 호출은 비연결·젖은 셀에서 지하수위가 바닥 아래일 때이며, 양의 `infil`은 해수→지하수 방향이다. 침투층 깊이는 양의 침투 때 `dt*infil/por`만큼 증가하고 그 외에는 리셋된다. (`groundwater.F90:1631-1643, 610-638, 283-285`; [[xbeach_groundwater]])

이 노트는 위 세 수식 묶음의 대응을 기록한다. 전체 매뉴얼 수식의 검증이나 새로운 사람 승인을 뜻하지 않는다.
'''
changes['models/XBeach/' + rel] = s
rel = 'README.md'
s = read(rel).replace('(2.5)~(2.10)의 파수 보정과 B.37/C.37의 지형 갱신 부호·sourcesink 분기를 대조했다.', '(2.5)~(2.10)의 파수 보정, B.37/C.37의 지형 갱신, 불포화 침투식의 판본 표기·시간 이산화를 대조했다.')
changes['models/XBeach/' + rel] = s

files = []
patch = []
for rel, text in changes.items():
    if rel.endswith('xbeach_wave_boundary_generation.md'):
        text = text.replace('`jons_table`', '`jonstable`').replace('parametric/jons_table', 'parametric/jonstable')
        text = text.replace('## 1. 입력과 생성 진입\n', '## 1. 입력과 생성 진입\n\n현재 `wbctype` 입력 이름 `jonstable`은 내부 상수 `WBCTYPE_JONS_TABLE`에 대응한다. (`params.F90:321-334`)\n')
    if rel.endswith('wave/xbeach_wave_boundary.md'):
        text = text.replace('| Stationary `jons_table` |', '| Stationary `jonstable` |').replace('parametric/jons_table', 'parametric/jonstable')
        text = text.replace('`wbctype=jons_table`', '`wbctype=jonstable`')
        text = text.replace('## A. `wbctype` dispatch\n', '## A. `wbctype` dispatch\n\nThe current table-input name is `jonstable`, mapped to `WBCTYPE_JONS_TABLE`; the legacy `instat` spelling below is distinct (`params.F90:321-334`).\n')
    old = subprocess.check_output(['git', 'show', f'{BASE}:{rel}'], cwd=ROOT)
    candidate = HERE / 'canonical' / rel
    candidate.parent.mkdir(parents=True, exist_ok=True)
    candidate.write_text(text)
    files.append({'target': rel, 'candidate': str(candidate.relative_to(ROOT)),
                  'before_sha256': hashlib.sha256(old).hexdigest(), 'after_sha256': hashlib.sha256(candidate.read_bytes()).hexdigest()})
    patch.extend(difflib.unified_diff(old.decode().splitlines(True), text.splitlines(True), fromfile='a/'+rel, tofile='b/'+rel, n=0))
(HERE / 'install-manifest.json').write_text(json.dumps({'basis_commit': BASE, 'scope': 'R3-C1..C4 only', 'human_approval_issued': False, 'files': files}, ensure_ascii=False, indent=2) + '\n')
(HERE / 'canonical.patch').write_text(''.join(patch))
print(f'Prepared {len(files)} canonical corrections from {BASE}')
