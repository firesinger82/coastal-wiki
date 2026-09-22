# ADD_EVIDENCE 11건 전수 검토 (Claude, 2026-09-22)

Codex 초안 `corrections.csv` 의 `fix_type=ADD_EVIDENCE` 11건. 전부 confidence LOW.

## 판정: 11건 모두 **접근이 틀렸다** — 채택하지 않는다

Codex 는 원 단언에 "…는 이 근거로 확인되지 않았으며, …를 추가 대조해야 한다" 를 덧붙이는 방식으로 일관한다.
그러나 **확인 가능한 것을 확인하지 않은 채 '확인 불가' 로 적은 것**이며, 검사한 모든 건에서
정확한 수치를 명령 하나로 얻을 수 있었다. 올바른 산출물은 hedge 가 아니라 **수치를 넣은 NARROW** 다.

| # | 노트 | 원 단언 | 실측 | 올바른 처리 |
|---|---|---|---|---|
| A2·A3 | `delft3d_dflowfm_data_io.md:164,240` | "**모든** NetCDF 를 `unc_open`/`unc_create` 통해 열어 추적" | **우회 3곳 실재** — `wricom.f90` 의 `nf90_open` 2곳, `read_land_boundary_netcdf.f90` 1곳 | NARROW(예외 3곳 명시) |
| A5 | `delft3d_flow2d3d_inichk_general.md:140` | "위 **모든** chk\*가 실패 시 `prterr` 호출" | `chk*.f90` **19개 중 18개** 호출, `chkdry.f90` 만 미호출 | NARROW(18/19) |
| A6 | `delft3d_waq_process_library.md:22` | "**모든** 프로세스 루틴이 동일 시그니처" | `waq_process/*.f90` **179개 중 171개**가 `subroutine X(process_space_real, …)` | NARROW(171/179) |
| A8 | `swan-programming-rules.md:65` | "source-analysis 의 **모든** SWAN 서브루틴이 따르는 표준 layout" | `src/` 소스 **75개 중 63개**가 `CALL STRACE` 포함 | NARROW(63/75) + 매뉴얼 규범과 구현 준수 구분 |
| A9 | `swan-unstructured-time-step.md:106` | "SwanCompUnstruc = **모든** 신규 물리 통합 entry" | `SwanCompUnstruc.ftn90` 내 등장: QCM 11 · Bragg 3 · **IEM 0 · GSECorr 0 · SpectPart 0** | NARROW(QCM·Bragg 만, IEM 은 경유하지 않음) |
| A10·A11 | `swash-unstructured-solvers.md:38,81` | "**모든** 'U' 루틴의 기반" | `uvc` 등장 **16파일**, `SwashU*.ftn90` 은 21개 | NARROW(16파일) |

### 반대 방향 — Codex 가 참인 단언을 깎은 것

| # | 노트 | 판정 |
|---|---|---|
| A7 | `efdc_toxics.md:72` | **원문이 옳다.** 노트는 "**water column** 항상 음" 이라 이미 한정했고, Codex 가 근거로 든 양의 분기는 `calsed.f90:422` 의 `SEDF(L,0,NS) = -WSETMP*SED + WESE` 로 **K=0 저면층**이다. 수주(K≥1)는 `:273`·`:284` 의 `-WSETA*SED` 로 음이다. hedge 기각 — 필요하면 "저면층 K=0 은 침식항 `WESE` 때문에 양이 될 수 있다" 를 덧붙이는 편이 낫다 |
| A4 | `delft3d_fbc_flow_boundary.md:156` | `getScalarIndex`/`getVectorIndex` 호출 **116곳**, `iXIn`/`iYOut` 등장 **249곳** — 원 단언을 반증하는 근거가 없다. hedge 기각 |
| A1 | `adcirc-tidal-forcing.md:50` | "constituent truncation 없이" 는 천체력 직접 적분 방식의 정의적 성질이다. Codex 의 근거(`sun_moon_system.F90:49-84`)는 좌표 계산만 보여주므로 **반증도 입증도 아니다**. 비선형 조석 포함 주장만 분리해 한정하는 편이 맞다 |

## 이 검토가 드러낸 것

Codex 에 "과장을 찾아라" 라고 시키면 **반대쪽으로 넘어가 참인 단언까지 '미확인' 으로 격하한다.**
`REPLACE` 버킷에서도 같은 일이 있었다(SWAN Wigner·Celeris render — [[claude-verification]] 참조).
`ADD_EVIDENCE` 는 그 성향이 버킷 전체를 지배했다 — 11건 전부 confidence LOW 이고 11건 전부 hedge 다.

**교훈**: 전칭 단언 검증 과제는 "참/거짓" 이분이 아니라 **"몇 개 중 몇 개인지 세는 일"** 이다.
세지 않고 "확인되지 않았다" 로 적으면 노트는 정확해지는 게 아니라 **덜 유용해진다.**
다음 위임에는 "반증할 수 없으면 수를 세라, 세지 못하면 그 이유를 적어라" 를 계약에 넣는다.
