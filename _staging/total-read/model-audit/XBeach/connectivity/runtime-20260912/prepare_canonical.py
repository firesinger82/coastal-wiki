"""Reproduce bounded runtime documentation corrections from the base commit."""
import difflib
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
BASE = '9f438b9'
changes = {}

def read(rel):
    return subprocess.check_output(['git', 'show', f'{BASE}:models/XBeach/{rel}'], cwd=ROOT).decode()

def replace(s, old, new):
    assert old in s, old
    return s.replace(old, new)

def section(s, start, end, body):
    a, b = s.index(start), s.index(end)
    return s[:a] + body + '\n\n' + s[b:]

def note(rel, s, scope):
    head, body = s[4:].split('\n---\n', 1)
    head += '\nsource_correction_date: 2026-09-12\nsource_correction_by: "Codex"\nsource_correction_scope: ' + json.dumps(scope, ensure_ascii=False) + '\nsource_correction_human_approval: not-issued'
    link = '../../../_staging/total-read/model-audit/XBeach/connectivity/runtime-20260912/evidence.json'
    body = '\n> **2026-09-12 AI 출처 정정**: ' + scope + '. 기존 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인이 아니다. [원문 구간·SHA와 연결 판정](' + link + ')을 따르며 원본 솔버는 수정하지 않았다.\n' + body
    changes['models/XBeach/' + rel] = '---\n' + head + '\n---\n' + body

rel = 'source-analysis/xbeach_flow_solver.md'
s = read(rel)
s = replace(s, s.splitlines()[1], 'title: "XBeach 유동 solver — 운동량 잔차·선박 압력수두·비정수압 보정·연속식 연결"')
s = section(s, '## 1.', '## 2.', '''## 1. Explicit Euler 운동량과 압력수두

아래는 배열 첨자를 생략한 **AI 전사·축약식**이다. 소스의 `dudt`는 속도에 더하는 가속도가 아니라, 갱신에서 **빼는 잔차**다. (`flow_timestep.F90:563-580`)

```text
dudt = ududx + vdudy - viscu + g*dzsdx
       + taubx/(rho*hu) + Fvegu/(rho*hu)
       - lwave*Fx/(rho*hum) - fc*vu
       - rhoa*Cd*windsu*sqrt(windsu²+windnv²)/(rho*hum)
dudt = clamp(dudt, -maxfacg*g, maxfacg*g)
uu = uu - dt*dudt
```

따라서 u의 Coriolis 속도 증분은 `+dt*fc*vu` 방향이다. v 잔차의 Coriolis 항은 `+fc*uv`이며 `vv -= dt*dvdt`로 갱신한다. 두 식은 각각 `wetu==1`, `wetv==1`에서 적용되고 건조점 속도는 0이 된다. (`flow_timestep.F90:563-580, 597-616`)

`dzsdx/dzsdy`는 `zs+ph`의 격자 방향 경사다. 여기서 **`ph`는 선박에 의한 압력수두 [m]**다. `shipwave`는 선박 위치·방향을 보간하고 선박 격자의 압력수두를 `s%ph`로 사상한다. 이 호출은 `ships==1`일 때 `flow`보다 먼저 실행된다. nonh의 압력은 별도의 `s%pres`와 국소 보정량 `dp`로 계산한다. (`variables.def:256`; `ship.F90:287-337, 365-373`; `libxbeach.F90:293-310`; `flow_timestep.F90:131-149`; [[xbeach_nonh]])''')
s = section(s, '## 4.', '## 5.', '''## 4. 실제 실행되는 2차 보정

| 루틴 | 현재 호출 조건과 위치 |
|---|---|
| `flow_secondorder_advUV` | `secorder==1`, `flow_timestep.F90:645-652` |
| `flow_secondorder_huhv` | `secorder==1`, 유량 계산 전 수심 보정, `flow_timestep.F90:706-719` |
| `flow_secondorder_advW` | nonh의 세 predictor에서 `secorder==1`, `nonh.F90:1234-1262, 1844-1883, 2858-2935` |
| `flow_secondorder_con` | 정의는 `flow_secondorder.F90:686-824`에 있지만 `flow_timestep.F90:754-759`의 호출은 주석 처리됨 |

따라서 `secorder=1`을 연속식 MacCormack 보정까지 실행한다는 뜻으로 읽으면 안 된다. 해당 호출 주석은 감쇠 때문에 제거했다고 기록한다. nonh에서는 압력 predictor → 조건부 U/V 2차 보정 → 압력 corrector 순서로 실행한다. (`flow_timestep.F90:635-658`)''')
s = replace(s, '연속방정식 `∂zs/∂t = -∇·(h·u)` 로 수위 `zs` 갱신(`dzsdt`, flux divergence).', '연속식은 격자 유량 발산에 `-infil + rainfallrate`를 더해 `zs += dt*dzsdt`로 갱신한다. 수평 유량 경계 적용 뒤, `rainfall==1`이면 강우를 갱신하고 연속식이 즉시 소비한다. (`flow_timestep.F90:724-751`; [[xbeach_tide_forcing]])')
s = section(s, '## 6.', '## 7.', '''## 6. 모드와 외력의 구분

`flow`의 nonh 압력 호출 조건은 `wavemodel==WAVEMODEL_NONH`다. 이때 `nonh_cor(...,0)`와 `nonh_cor(...,1)`이 예측·보정을 수행한다. 선박 압력수두 `ph`의 공급 조건은 별도 `ships==1`이다. `ph`를 기준으로 stationary/surfbeat와 nonh를 구분할 수 없다. (`flow_timestep.F90:635-658`; `libxbeach.F90:293-310`)

`swave`의 nonh 기본값은 0이지만 입력으로 1도 허용하며, 운동량의 `Fx/Fy`에는 `lwave`가 곱해진다. 따라서 모드 이름만으로 모든 구성에서 파력항이 없다고 단정하지 않는다. (`params.F90:98-109`; `flow_timestep.F90:563-612`)''')
s = replace(s, '- wave action balance(`Fx` radiation stress 공급) / nonh(`ph` 압력) — 후속 노트', '- [[xbeach_wave_action_balance]] — 파력 공급; [[xbeach_nonh]] — `pres/dp` 압력 보정')
note(rel, s, '`ph`의 선박 귀속, 운동량 잔차 부호, 실제 2차 보정 호출과 강우 소비를 정정')

rel = 'source-analysis/xbeach_nonh.md'
s = read(rel)
s = replace(s, s.splitlines()[1], 'title: "XBeach nonh — pres/dp 압력 예측·보정, 1층·reduced 2층 및 MPI 호출"')
s = s[:s.index('# XBeach non-hydrostatic mode')] + '''# XBeach nonh 압력 보정의 실행 연결

현재 입력 이름은 `wavemodel=nonh`다. 이 모드의 압력 상태는 **`s%pres`**, 선형계의 해·보정 작업 배열은 **`dp`**다. `ph`는 선박 압력수두 [m]이며 nonh 압력의 별칭이 아니다. (`params.F90:70-79`; `variables.def:256`; `nonh.F90:683-697`)

## 1. 유동과 압력의 호출 순서

`flow`는 일반 운동량 갱신 뒤 `wavemodel==WAVEMODEL_NONH`이면 `nonh_cor(...,0)`을 호출한다. 이어 `secorder==1`의 `flow_secondorder_advUV`를 거쳐 `nonh_cor(...,1)`을 호출한다. predictor에서 기존 압력의 명시적 기여를 넣는 부분도 `secorder==1` 조건을 가진다. (`flow_timestep.F90:563-658`; `nonh.F90:1234-1262, 1844-1883, 2858-2935`)

## 2. `nonhq3d`의 정수 분기

| `nonhq3d` | 공간 조건 | `ipredcor==0` | 그 외 (`flow`는 1을 전달) |
|---|---|---|---|
| 1 | `ny==0` | `nonh_2lay_pred_2dV` | `nonh_2lay_cor_2dV` |
| 1 | `ny!=0` | `nonh_2lay_pred_3d` | `nonh_2lay_cor_3d` |
| default (통상 0) | 별도 ny 분기 없음 | `nonh_1lay_pred` | `nonh_1lay_cor` |

이는 `nonh.F90:201-247`의 `SELECT CASE`와 내부 IF를 전사한 표다. `.true./.false.` 논리형 SELECT가 아니다. 각 루틴 내부의 공간 경계·wet 조건은 별도로 적용된다.

## 3. 압력 저장과 속도 보정

세 corrector는 `solver_solvemat(mat,rhs,dp,nx,ny,par)`로 압력 선형계를 풀고 속도를 보정한다. 1층 경로는 `s%pres += dp`를 수행한다. 두 reduced 2층 경로는 `secorder==1`이면 `s%pres += dp`, 그 외에는 `s%pres = dp`를 사용한다. (`nonh.F90:683-697, 1411-1422, 2162-2176`)

이 값은 nonh 루틴 내부의 수평·연직 속도 보정에 쓰인다. 기존 설명의 `dp → ph → g∂(zs+ph)` 연결은 잘못된 귀속이었다. `flow`의 `zs+ph` 경사는 선박 외력 경로이며 비정수압 보정과 별도로 읽어야 한다. (`nonh.F90:1234-1262`; `flow_timestep.F90:131-149`; [[xbeach_flow_solver]])

## 4. MPI 빌드와 실제 guard

`nonh.F90:42-43`의 MPI 제외 문장은 오래된 주석이다. 현재 조사한 MPI 프로젝트에 이 소스가 포함되고, 구현 안에는 `#ifdef USEMPI`로 감싼 `xmpi_shift_ee` 호출이 있다. 이를 `#ifdef CMPI`에 의해 모듈 전체가 제외된다고 설명할 근거는 없다. (`nonh.F90:1446-1449, 1872-1883, 2237-2241, 2927-2935`; [[xbeach-build-mode-connectivity]])

이 판정은 소스와 빌드 포함 관계다. 모든 MPI·nonh 옵션 조합의 수치 실행 검증을 뜻하지 않는다.

## 5. 연결

- [[xbeach_flow_solver]] — 운동량·2차 보정·압력 호출 순서
- [[xbeach_mode_dispatch]] — 파랑 모드 선택
- [[xbeach_wave_action_balance]] — stationary/surfbeat 파랑 계산
- [[xbeach-build-mode-connectivity]] — 컴파일 대상과 실행 모드 근거
'''
note(rel, s, '선박 `ph`와 비정수압 `pres/dp`, 정수 dispatch 및 현재 MPI 구현을 구분')

rel = 'source-analysis/xbeach_vegetation.md'
s = read(rel)
s = replace(s, '- `wave_stationary.F90:235-236`, `wave_instationary.F90:294-295`, `wave_stationary_directions.F90:442-444`, `wave_directions.F90:290` — `Dveg` consumption.', '- `wave_instationary.F90:294-295`, `wave_stationary_directions.F90:442-444` — current `Dveg` consumers; see [[xbeach-build-mode-connectivity]] for the excluded legacy files.')
s = section(s, '`Dveg` stored in', '**Bulk drag coefficient**', '''`Dveg` is stored in `s%Dveg` (`vegetation.F90:400`). Both active wave consumers include `s%Df + s%Dveg`: surfbeat energy propagation (`wave_instationary.F90:294-295`) and the shared stationary/direction calculation (`wave_stationary_directions.F90:442-444`; `wave_timestep.F90:75-114`).

The missing term commented in legacy `wave_directions.F90:290` is not a limitation of the current directional calculation. That file and `wave_stationary.F90` are excluded from the inspected build targets ([[xbeach-build-mode-connectivity]]). Per-step wave calls precede `vegatt`, so the active consumers read the last vegetation update, while `flow` reads the drag computed later in the same step (`libxbeach.F90:293-310`).''')
s = replace(s, 'Flow solver acceleration includes:', 'Flow solver residuals (subtracted from velocity in the update) include:')
s = replace(s, '- `Dveg` missing in `wave_directions.F90:290` is a known limitation — directional wave model does not include vegetation dissipation (only standard surfbeat does).', '- Active stationary and surfbeat single-direction calculations include `Dveg`; their invocation and update timing follow §D.')
s = replace(s, '- ▢ Using `wave_directions` (advanced directional wave model) and expecting vegetation dissipation — currently not implemented.', '- ▢ Treating the build-excluded `wave_directions` comment as the behavior of active `wave_stationary_directions`; see §D.')
note(rel, s, '활성 정상·방향 계산의 `Dveg` 소비와 파랑/식생/유동 갱신 순서를 명시')

rel = 'source-analysis/xbeach_tide_forcing.md'
s = read(rel)
s = section(s, '## 3.', '## 4.', '''## 3. Rainfall의 단위와 소비 시점

`rainfall_init`은 `xmaster`에서 실행하며, 상수 입력과 파일의 강우율을 **mm/hr에서 m/s로 변환**한다 (`/1000/3600`). 파일 입력은 시각 0으로 초기 보간하고, 강우가 꺼져 있으면 `rainfallrate=0`으로 초기화한다. (`rainfall.F90:22-70`; 초기 호출 `libxbeach.F90:177`)

`flow`는 수평 유량 경계를 적용한 뒤 `rainfall==1`이면 `rainfall_update`를 호출한다. 시계열 경로는 현재 `par%t`로 보간하며, 이어지는 1D/2D 연속식 모두 `-infil + rainfallrate`를 사용한다. (`rainfall.F90:92-100`; `flow_timestep.F90:724-751`)

MPI에서 `constantRainfall` 방송은 `t<=dt` 조건을 가진다 (`rainfall.F90:86-90`). 지하수의 `gwflow`는 이 강우 갱신과 `flow`보다 먼저 호출되므로, 여기서 갱신한 강우를 같은 스텝의 앞선 침투 계산에 직접 넘긴다고 해석하지 않는다. 강우는 우선 연속식의 표면수 공급항이다. (`libxbeach.F90:304-307`; [[xbeach-coupled-physics-contracts]])''')
s = replace(s, '- [[xbeach_groundwater]] — rainfall infiltration', '- [[xbeach_groundwater]] — 연속식이 함께 소비하는 `infil` 계산')
note(rel, s, '강우 단위 변환·시각 보간·연속식 소비와 지하수 계산 순서를 결속')

rel = 'source-analysis/xbeach_output.md'
s = read(rel)
s = replace(s, '- `varoutput.F90` — 출력 변수 registry/선택 (xpoints/ypoints, Avarpoint/Avarcross 점·cross-section별 출력변수 index, mnemmodule mnemonic). 전역/점/단면 출력변수 관리 (2026-06-03).', '- `varoutput.F90` — compiled legacy output implementation. Its `var_output_init` calls in current `output_init` are commented out (`output.F90:54-80`); it is not the active output provider.')
s = replace(s, '`output_init` dispatches to Fortran, NetCDF, or both (debug mode) (`output.F90:54-80`).', '''`output_init` selects `fortoutput_init`, `ncoutput_init`, or both (debug with `USENETCDF`). The active provider is `ncoutput_module`, including the Fortran writer. `OUTPUTFORMAT_NETCDF` without `USENETCDF` logs the missing support and halts. Old `var_output_init` calls are commented out. (`output.F90:5-8, 51-80`)

At runtime `output` calls `ncoutput`; its non-`xomaster` return is before **both** the NetCDF and Fortran write branches. Thus `outputformat=fortran` does not make every MPI rank write the same files in this path. (`output.F90:164`; `ncoutput.F90:1118-1164`)''')
s = replace(s, '- ▢ MPI run with `outputformat=fortran` — every rank tries to write — collision.', '- ▢ Assuming Fortran output bypasses the MPI output master: both file formats share the `xomaster` guard (`ncoutput.F90:1118-1164`).')
note(rel, s, '활성 `ncoutput_module` 공급자와 두 출력 형식에 공통인 `xomaster` 쓰기 조건을 정정')

rel = 'source-analysis/xbeach-coupled-physics-contracts.md'
s = read(rel)
s += '''
## 외력의 생산·소비 시점 (2026-09-12 R1 보강)

아래는 동일한 동결 소스의 추가 연결 판정이다. [원문 구간과 SHA](../../../_staging/total-read/model-audit/XBeach/connectivity/runtime-20260912/evidence.json)에 결속했으며 이 노트의 미승인 상태는 유지한다.

| 상태 | 생산과 조건 | 소비와 시점 |
|---|---|---|
| 선박 `ph` [m] | `ships==1`의 `shipwave`, 선박 격자의 압력을 `grmap2`로 모델 격자에 사상 | 같은 스텝 `flow`의 `zs+ph` 경사. nonh 압력은 `pres/dp`라는 별도 상태 |
| `Dveg` / `Fvegu,Fvegv` | `vegetation==1`의 `vegatt`; 표준 경로는 `swvegatt`·`momeqveg`, `porcanflow==1`은 별도 분기 | 파랑은 `vegatt`보다 앞서므로 마지막 식생 갱신의 `Dveg`, 유동은 뒤에 있어 같은 스텝 항력 소비 |
| `rainfallrate` [m/s] | 초기 상수/파일 mm/hr 변환; `rainfall==1`의 시간 보간 | 같은 `flow`의 연속식에 가산. `gwflow`는 이 갱신보다 앞서 실행 |
| `D90top` → `cfu/cfv` | 이전 지형 갱신의 입경 상태; White-Colebrook 입경 옵션과 `ngd>1`에서 조도 계산 | `flow`의 `bedroughness_update`가 운동량 계산 전에 사용. 뒤의 `bed_update` 결과는 이후 유동 호출에 전달 |

선박은 첫 처리에서 `zs -= ph`도 수행한다 (`ship.F90:403-410`). 표의 시점은 해당 옵션이 실행되는 경우의 호출 순서이며 스텝 사이 모든 상태가 재초기화된다는 뜻이 아니다. 입경 배열 덮어쓰기의 기존 판정·한계는 위 절을 그대로 따른다. (`libxbeach.F90:293-312`; `ship.F90:287-337,365-373`; `vegetation.F90:318-345,400,563-564`; `wave_instationary.F90:294-295`; `wave_stationary_directions.F90:442-444`; `rainfall.F90:22-70,86-100`; `flow_timestep.F90:120,131-149,176-177,563-612,724-751`; `bedroughness.F90:220-249`)
'''
changes['models/XBeach/' + rel] = s

rel = 'README.md'
s = read(rel)
s = replace(s, '입경 배열 덮어쓰기, 침투량 단위, 수심 갱신 시점, Q3D 실행 조건을 추적했다.', '입경 배열 덮어쓰기, 침투량 단위, 수심 갱신 시점, Q3D 실행 조건과 선박·식생·강우·조도의 생산/소비 시점을 추적했다.')
changes['models/XBeach/' + rel] = s

files, patch = [], []
for target, s in sorted(changes.items()):
    old = subprocess.check_output(['git', 'show', f'{BASE}:{target}'], cwd=ROOT)
    candidate = HERE/'canonical'/Path(target).relative_to('models/XBeach')
    candidate.parent.mkdir(parents=True, exist_ok=True)
    candidate.write_text(s)
    files.append({'target': target, 'candidate': str(candidate.relative_to(ROOT)),
                  'before_sha256': hashlib.sha256(old).hexdigest(),
                  'after_sha256': hashlib.sha256(s.encode()).hexdigest()})
    patch.extend(difflib.unified_diff(old.decode().splitlines(True), s.splitlines(True), fromfile='a/'+target, tofile='b/'+target))
# Git's suppressBlankEmpty form omits the lone context marker on empty lines.
(HERE/'canonical.patch').write_text(''.join('\n' if line == ' \n' else line for line in patch))
(HERE/'install-manifest.json').write_text(json.dumps({'base_commit': BASE, 'scope': 'Seven fixed-scope runtime documentation targets; no solver mutation or new human approval', 'files': files}, ensure_ascii=False, indent=2)+'\n')
print('Prepared', len(files), 'canonical targets')
