# Codex 교정 초안 66건 전수 검토 (Claude, 2026-09-22)

대상: `_staging/overclaim-sweep/corrections.csv` (66행).
검토 기준: ⑴ `old_text` 유일 매치 ⑵ 근거가 실재하고 주장하는 바를 말하는가 ⑶ 교정이 **참인 단언을 깎지 않는가**.

## 형식 검사 — 통과

66행 전부 `old_text` 가 대상 노트에서 **유일하게 매치**한다(불일치 0·중복 0·빈값 0). 유형 분류도 계약대로 갈렸다.

## 내용 검사 — 절반이 재작업 대상

결정적 지표는 **hedge 문구**(`확인되지 않았`·`추가 대조해야`·`확정할 수 없`)의 출현이다.

| 유형 | 건수 | hedge 포함 | 수치 제시 | 판정 |
|---|---:|---:|---:|---|
| ADD_EVIDENCE | 11 | **11 (100%)** | 0 | **전건 기각** — 재작성 |
| REPLACE | 11 | 5 | 0 | 5건 재검토, 6건 수용 |
| NARROW | 44 | 16 | 1 | 16건 재검토, 28건 수용 |
| **합계** | **66** | **32 (48%)** | **1** | **34 수용 / 32 재작업** |

## 왜 hedge 가 문제인가

과제는 "참/거짓" 이분이 아니라 **"몇 개 중 몇 개인지 세는 일"** 이다. 검사한 모든 건에서
정확한 수치를 명령 하나로 얻을 수 있었다.

| 노트 | 원 단언 | Codex | 실측(Claude) |
|---|---|---|---|
| `delft3d_flow2d3d_inichk_general.md:140` | "**모든** chk\*가 `prterr` 호출" | "호출 여부는 확인되지 않았다" | **19개 중 18개**(`chkdry.f90` 만 미호출) |
| `delft3d_waq_process_library.md:22` | "**모든** 프로세스 루틴이 동일 시그니처" | "동일 계약은 확인되지 않았다" | **179개 중 171개**가 `subroutine X(process_space_real, …)` |
| `swan-programming-rules.md:65` | "**모든** SWAN 서브루틴이 표준 layout" | "준수 여부는 확인되지 않았다" | 소스 **75개 중 63개**가 `CALL STRACE` 포함 |
| `swan-unstructured-time-step.md:106` | "**모든** 신규 물리 통합 entry" | "경유 여부는 확인되지 않았다" | QCM 11·Bragg 3 등장, **IEM·GSECorr·SpectPart 는 0** |
| `delft3d_dflowfm_data_io.md:164` | "**모든** NetCDF 를 `unc_open` 경유" | "전 경로 준수는 확인되지 않았다" | **우회 3곳 실재** — `wricom.f90` 2, `read_land_boundary_netcdf.f90` 1 |
| `swash-unstructured-solvers.md:38,81` | "**모든** 'U' 루틴의 기반" | "의존 여부는 확인되지 않았다" | `uvc` 등장 **16파일**(`SwashU*` 는 21개) |

"확인되지 않았다" 를 쓰면 노트는 정확해지는 게 아니라 **덜 유용해진다.** 위 6건은 전부
수치를 넣은 NARROW 로 다시 쓴다.

## 참인 단언을 깎은 것 — 기각 4건

| 노트 | Codex 주장 | 실측 판정 |
|---|---|---|
| `swan-quasi-coherent.md:86` | "모든 점에서 양수" → "0인 경우도 있는 반면" | **기각.** 원문의 대비(action density ≥ 0 vs Wigner 는 음수 가능)가 파괴된다. Codex 근거 `swanmain.ftn:7903-7913` 은 ZERO/NODATA **출력 처리**이지 수학적 성질이 아니다. 올바른 교정은 **"음이 아닌(non-negative)"** |
| `celeris-render.md:117` | "수치 비변경은 확인되지 않았다" | **기각.** `Handler_Render.js` 의 바인드그룹은 `texture:`(샘플링)와 uniform `buffer:` 뿐이고 **storage 텍스처가 없다** — 쓰기가 구조적으로 불가능하다. 확인 가능한 참이다 |
| `efdc_toxics.md:72` | "수주 전 구간 항상 음인지 확인되지 않았다" | **기각.** 노트는 "**water column**" 으로 이미 한정했고, Codex 가 든 양의 분기 `calsed.f90:422` 는 `SEDF(L,0,NS)` = **K=0 저면층**(침식항 `WESE` 포함)이다. 수주(K≥1)는 `:273`·`:284` 의 `-WSETA*SED` 로 음이다 |
| `delft3d_fbc_flow_boundary.md:156` | "전 rule·trigger 인덱스 해석 경로 확정 불가" | **기각.** `getScalarIndex`/`getVectorIndex` 호출 116곳, `iXIn`/`iYOut` 249곳 — 반증 근거가 없다 |

## 수용 — 확인된 개선

| 노트 | 내용 |
|---|---|
| `xbeach_params.md:28` | `readkey_inio` 는 `xmpi_bcast` 인자(MPI 수신 범위)로 echo 와 무관. **오독 교정, 수용** |
| `lisflood-fp-io-boundary.md:68` | `input.cpp:1339,1369-1372` 실측 — `H`·`maxH` = xsz×ysz, `Qx/Qy` = (xsz+1)×(ysz+1). 원문 괄호가 H 까지 (xsz+1)×(ysz+1) 로 읽히게 쓰여 있었다. **수용** |
| `roms_tangent_linear_model.md:28` | "54개 `.F`/`.h`" → 실측 `.F` 54 + `.h` 18 = **72**. 수용하되 내역을 병기하도록 보완 |
| `delft3d_fbc_flow_boundary.md:52` | "in-place 풀이" → `stateOld`/`stateNew` 별도 포인터이므로 in-place 가 아니다. **수용** |
| NARROW 28건 | 문장 구조·용어·링크를 보존하고 범위만 좁히며 `file:line` 을 넣었다. 표본 6건 품질 양호. **수용** |

## 부수 발견 — 반복되는 결함 패턴

**하위 집합 계수를 총계로 라벨링**하는 오류가 세 번째다.

| 노트 | 표기 | 실제 |
|---|---|---|
| `swan-source-coverage-audit.md` | "58 source files" | `.ftn90` 58개(구 스냅샷), 총 소스는 75 |
| `roms_tangent_linear_model.md` | "54개 `.F`/`.h`" | `.F` 54 + `.h` 18 = 72 |
| `lisflood-fp-io-boundary.md` | "`H`, `Qx/Qy`는 (xsz+1)×(ysz+1)" | `H` 는 xsz×ysz |

세 건 모두 **세어 보면 즉시 드러나는** 오류다. 파일 수·배열 크기를 단언할 때 실측 명령을 함께
기록하는 규칙을 게이트에 넣을 가치가 있다.

## 다음 단계

1. 수용 34건(NARROW 28 + REPLACE 6)을 적용한다.
2. 재작업 32건은 **수치를 세어** 다시 쓴다 — 위 표의 6건은 실측이 이미 끝났다.
3. 적용 시 layer 파일은 커밋을 분리한다(pre-commit `layer-deps` scope guard).

다음 위임 계약에 넣을 문구: **"반증할 수 없으면 수를 세라. 세지 못하면 세지 못한 이유를 적어라.
'확인되지 않았다' 는 마지막 수단이다."**
