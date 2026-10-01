# XBeach R1-G1 판정 결과 (2026-10-01)

계획: [PLAN.md](PLAN.md) v2 + §5(A-K1·멈춤 규칙). 범위: 동결 후보 3,228건([call-candidates.jsonl](../runtime-20260912/call-candidates.jsonl)).
최종 판정: `G1-final.jsonl` (압축 [G1-final.jsonl.gz](G1-final.jsonl.gz)). 결정적 검사 `check_g1.py` 오류 0, B1 빌드 계열 `correct/check_b1.py` 3,228건 일치.

## 1. 공정과 모델

| 단계 | 대상 | 모델 | 결과 |
|---|---|---|---|
| 계획 적대 검토 | PLAN v1 | gpt-6-astra | blocker 3·major 6 → v2 |
| 파일럿 판정·검증 | 60 | gpt-6.1-sol / gpt-6-astra | 59 유지·1 NARROWED |
| 본 판정 | 3,168 (28배치) | gpt-6.1-sol | check 오류 0 |
| 적대 검증 1차 | 2,042 (전건 1,906 + 층화 10% 136, seed 20260930) | gpt-6.1-sol max | 유지 1,909·NARROWED 130·**REFUTED 3** |
| 정정 1차 | verdict 133 + 유형 스윕 B1 1,745·B2 692·B3 157 | gpt-6.1-sol max | 이견 0 |
| 재검증 | 의미 변경 982 (B1 은 결정적 대조로 대체) | gpt-6.1-sol max | 유지 774·NARROWED 208·REFUTED 0 |
| 정정 2차 | 208 (A-K1 140·prior-exit 60·note 1·기타 7) | gpt-6.1-sol max | 이견 0, 비대상 3,020 바이트 보존 |
| 재검증 2 | kind 외 변경 68 | gpt-6.1-sol max | 유지 66·NARROWED 2 |

**한계**: 1차 판정 모델과 적대 검증 모델이 같다(gpt-6.1-sol, 사용자 지시). 계획 적대 검토와 파일럿 검증만 gpt-6-astra 다.

**REFUTED 3 (원문 확인·정정 완료)**: `waveparams.F90:246·459·802` `writelog` — 4번째 실인자 `fname` 이 `character(len=*)` 이므로 `writelog_afa` 가 아니라 `writelog_aaa`(generated `writelog.inc:580`).

## 2. 최종 분포

| resolution | 건수 |
|---|---:|
| direct_edge | 1,802 |
| generic_edge | 1,054 |
| external_interface | 279 |
| unresolved | 56 |
| intrinsic | 33 |
| indirect_interface | 2 |
| not_a_call | 2 |

bindings applicability status: confirmed 2,840 · excluded 1,495 · undetermined 466. (인벤토리이며 결함 수·진행률이 아니다.)

## 3. 미해결 56 ([unresolved.json](unresolved.json))

| 원인 | 건수 | 성격 |
|---|---:|---|
| `flush` | 17 | 선언 없는 컴파일러 확장 서브루틴 — 허용 소스로 대상 확정 불가 |
| `xmpi_reduce`·`xmpi_allreduce` | 14 | rank·type 으로 specific 은 정해지나 외부 `MPI_MIN` 등 상수의 kind 미확인 |
| MPE 로깅 (`mpe_*`) | 14 | MPI 성능 로깅 라이브러리 — 모델 쪽 선언 없음, 부속 도구 내부 미판독(범위 통제) |
| `sleepqq`·`usleep`·`sleep`·`getcwd`·`backtrace` | 6 | 컴파일러·OS 확장 — 링크 근거 없음 |
| `indextos`·`printsum`·`makeaveragenames` | 3 | **죽은 코드** — 호출자가 `#if 0` 안 (debugging.F90·varoutput.F90), 어느 빌드에도 없음 |
| `writelog` (`wave_stationary_directions.F90:668·671`) | 2 | **표준 위반 후보** — `MIN(real*8 식, 0.99)` 혼합 kind 인자(표준은 동일 kind 요구), 컴파일러 확장 의존. 의도 대상 `writelog_aiaiaf` 는 가설 |

모델 내부 결속 누락으로 확인된 것은 없다. 표준 위반 후보 2건은 이식성 결함 후보로 남긴다.

## 4. 확정 시 남긴 NARROWED (멈춤 규칙)

- `boundaryconditions.F90:9:wave_bc@717:5:report_file_read_error` — SURFBEAT 형제 ELSEIF 분기의 종료 12개(@492…@642)가 runtime 조건에 남음(과잉). 대상·빌드는 맞음.
- `xmpi.F90:1619:xmpi_getrow@1669:5:mpi_recv` — IFX MPI_netcdf x64 두 구성을 undetermined 로 둠. 실행 파일 `src/xbeach/xbeach_IFX.vfproj:32·43·76·87` 이 `AdditionalDependencies="impi.lib"` 로 MPI 를 링크한다.

## 5. 후속 확인 (R1-G1 해소 판단에 영향)

- **외부 MPI 기록 98건**: 정정 1차가 "IFX MPI+netCDF x64 설정별 링크 근거 확인 필요"(라이브러리 vfproj 의존성은 NetCDF 만 명시)로 보고. 위 §4 의 `xbeach_IFX.vfproj` `impi.lib` 링크가 해당 근거일 가능성이 높다 — 일괄 반영은 하지 않았다.
- **동결 후보 밖 호출 2건** (G2 적대 검토에서 발견, 분모에 추가하지 않음): `wave_boundary_update.f90:1308 → linear_interp_2d` (source edge, 빌드 도달 미확정), `test/testgenmodule.F90:306 → xmpi_getrow` (test-only). 3,228건 완료는 호출 그래프 완전성을 뜻하지 않는다.

## 6. 상태

- G1 **판정 기록 완료** (PLAN §4).
- **R1-G1 공백 해소 선언은 사용자 수용 결정 대기** — §3 미해결 56·undetermined 466·§5 후속 2항목을 수용할지.
- R1 종료 = G1 해소 + G2/G3([review-response-20260930](../interfaces-20260912/review-response-20260930.json), 58건 중 55 유지·3 정정). `models/` 반영은 R1 단위 SCOPED EDIT 1회. R2·R3 전체·R4 는 자동 착수 안 함. 사람 승인 발급 없음.
