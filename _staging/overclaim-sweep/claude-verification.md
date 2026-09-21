# 전칭 단언 스윕 — Claude 표본 검증 (2026-09-22)

Codex 분류 395건 중 `OVERCLAIM` 66건에 대한 표본 검증 기록.
**완료 판정은 위임하지 않는다**(CLAUDE.md 작업규범 4) — Codex 결과를 그대로 반영하지 않고 근거를 직접 열어 대조했다.

## 분류 분포 (Codex, `codex-verdicts.csv`)

| 분류 | 건수 |
|---|---:|
| SUPPORTED | 212 |
| **OVERCLAIM** | **66** |
| NOT_A_CLAIM | 59 |
| SCOPE_STATEMENT | 40 |
| UNVERIFIABLE | 18 |

OVERCLAIM 66건의 영역 분포: Delft3D 21 · ROMS 13 · SFINCS 6 · SWAN 6 · Celeris 4 · SWASH 4 · EFDC 3 · LISFLOOD-FP 2 · concepts 2 · ADCIRC·FUNWAVE·ShorelineS·XBeach·textbook 각 1.
confidence: HIGH 32 / MEDIUM 34. 근거가 비어 있는 행은 0건.

## 표본 검증 결과 — 5/5 정확

층화 표본(영역별 1건)에서 소스 대조가 가능한 5건을 직접 확인했다.

| 건 | 노트의 단언 | 검증 | 결과 |
|---|---|---|---|
| ShorelineS `shorelines-transport-formulations.md:38` | "**모든 공식**의 각도항에 dHS 가산" | `transport.m:194-197` 의 `RAY` 분기는 `WAVE.dPHItdp` 만 쓰고 dHS 항이 없다 | ✅ 과장 |
| XBeach `xbeach_params.md:28` | "`readkey_inio = toall`: 읽은 **모든 키**를 PRINT/log 에 echo" | `readkey.F90:41` 에서 `logical :: readkey_inio`, `:145·232·320·379·459` 에서 `call xmpi_bcast(value, readkey_inio)` — **MPI 브로드캐스트 수신 범위 플래그**이고 echo 와 무관 | ✅ **오독**(과장 아님) |
| ROMS `roms_io_netcdf.md:189` | "**모든** def/wrt/get/nf_ 모듈이 generic INTERFACE 로 추상화" | `def_dim.F:24-29` 는 `INTERFACE def_dim` + `MODULE PROCEDURE` 이나, `def_his.F:73,79` 는 `PUBLIC :: def_his` + `CONTAINS` 로 generic INTERFACE 가 아니다 | ✅ 과장 |
| FUNWAVE `funwave-code-graph.md:23` | "**모든 모듈**이 PARAM·GLOBAL 의존" | `src/*.F` 중 `USE` 를 쓰는 38개 가운데 **15개**가 둘 다 `USE` 하지 않는다(`mod_param.F` 는 둘 다 없음, `mod_global.F` 는 PARAM 만, 다수는 GLOBAL 만) | ✅ 과장 |
| concepts `time-integration-cross-model.md:63` | "ROMS 외 **나머지 전부** implicit/semi-implicit" | **같은 노트**가 XBeach 를 "explicit Euler 1차"(:51), SFINCS 를 "explicit staggered local-inertial"(:57) 로 기재 | ✅ 자기모순 |

선행 사례와 일관된다 — EFDC 파일럿에서 Codex 분류 78건 중 최종 판정과 갈린 것은 1건이었다.

## ★버킷이 균질하지 않다 — 일괄 처리 금지

XBeach 건은 **수량사를 빼도 여전히 틀린다**. "모든 키를 echo" 에서 "모든" 을 제거해도 `readkey_inio` 가 echo 를 제어한다는 전제 자체가 거짓이다. 문장을 갈아야 한다.

따라서 교정은 세 유형으로 나눠 다룬다.

| 유형 | 처리 |
|---|---|
| `NARROW` | 수량사를 근거가 덮는 범위로 좁히고 그 범위를 `file:line` 으로 명시 |
| `REPLACE` | 주장이 거짓이므로 문장 교체 |
| `ADD_EVIDENCE` | 주장은 성립할 수 있으나 인용이 범위를 못 덮음 — 추가 확인 대상 기록 |

## 다음 단계

Codex 에 66건 교정 문안 초안을 위임했다(`corrections.csv`, 읽기 전용 + 그 파일만 쓰기). 초안은 그대로 반영하지 않고 `old_text` 의 유일 매치 여부와 `evidence` 를 다시 대조한 뒤 적용한다.

적용 시 주의: `models/XBeach/source-analysis/xbeach-audit-resolved-claims.md` 류의 **layer 파일은 별도 커밋**이어야 한다(pre-commit `layer-deps` scope guard).
