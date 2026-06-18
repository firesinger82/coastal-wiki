---
title: "ADCIRC + SWAN tightly-coupled surge + wave (비정형 메시 공유, radiation stress 양방향 결합)"
canonical_source: self
citation_status: verified
verification_method: >
  본 예제는 검수완료(verified) source-analysis 노트 + 개념 노트의 메커닉을 절차로
  조립한 재현 템플릿. 결합 메커닉 단언은 모두 cross-link 대상 노트로 위임하며,
  그 노트들의 실재(ls)와 frontmatter(citation_status: verified)를 직접 확인(2026-06-18).
  NWS=3xx 인코딩·time-step 정수비·radiation stress 전달 방향은
  adcirc-swan-coupling.md(couple2swan.F file:line) 직접 read 로 검증. 정량 run 미수록.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - examples/README.md
  - models/ADCIRC/source-analysis/adcirc-swan-coupling.md
  - models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md
  - models/SWAN/source-analysis/swan-unstructured-time-step.md
  - concepts/storm-surge/02-theory.md
  - concepts/waves/06-model-application.md
  - concepts/compound-flooding/06-model-application.md
---

# ADCIRC + SWAN tightly-coupled surge + wave

> 동일한 **비정형 삼각망**(`fort.14`)을 ADCIRC와 SWAN이 공유하면서, ADCIRC(수위·유속·바람)
> 와 SWAN(파랑 → radiation stress)을 **양방향 결합**해 storm surge에 **wave setup**을 더한
> 총수위를 한 번의 coupled run으로 산출하는 표준 워크플로. 단일 `padcswan` 바이너리가
> 두 솔버를 한 프로세스에서 번갈아 호출한다(in-memory 교환).

## 다루는 개념·모델

- 개념:
  - [`concepts/storm-surge`](../../concepts/storm-surge/) — surge 거버닝식·wind setup·ADCIRC GWCE
    ([`02-theory.md` §5.1 GWCE](../../concepts/storm-surge/02-theory.md), §3.2 wind set-up)
  - [`concepts/waves`](../../concepts/waves/) — spectral 파랑·SWAN
    ([`06-model-application.md`](../../concepts/waves/06-model-application.md))
  - [`concepts/compound-flooding`](../../concepts/compound-flooding/) — coastal surge 솔버로서의 ADCIRC
    ([`06-model-application.md`](../../concepts/compound-flooding/06-model-application.md))
- 모델: [`models/ADCIRC`](../../models/ADCIRC/) (GWCE 유한요소 surge) ·
  [`models/SWAN`](../../models/SWAN/) (위상평균 spectral, unstructured 모드)
- 결합 메커닉(검수 근거):
  - ADCIRC측 coupler: [`adcirc-swan-coupling`](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md)
    — `couple2swan.F` (`PADCSWAN_INIT/RUN/FINAL`), NWS=3xx 인코딩, time-step 정수비, RS 전달
  - SWAN측 unstructured 경로: [`swan-adcirc-coupling-implementation`](../../models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md)
    — `SwanReadADCGrid`(fort.14 직접 read), `SwanCompUnstruc`, **unstructured wave setup 비활성** 한계
  - unstructured time-step driver: [`swan-unstructured-time-step`](../../models/SWAN/source-analysis/swan-unstructured-time-step.md)
    — 41.20 Casey Dietrich tightly-coupled ADCIRC+SWAN 기여, vertex-based implicit propagation

## 결합 구조 (양방향)

```
              ┌──────────── 같은 fort.14 (비정형 삼각망) ────────────┐
              │                                                      │
        ┌─────┴──────┐    ETA2, UU2, VV2, (WX2,WY2)   ┌────────────┴───┐
        │   ADCIRC   │ ───────────────────────────▶  │      SWAN       │
        │  (GWCE +   │     수위·유속·(바람)            │ (unstructured,  │
        │  momentum) │                                │  SwanCompUnstruc│
        │            │  ◀─────────────────────────── │  action balance)│
        └────────────┘   SXX,SXY,SYY → RSNX2,RSNY2    └─────────────────┘
                         (radiation stress gradient → 파-유도 nodal force)
```

- **ADCIRC → SWAN**: 매 결합 스텝 ADCIRC가 수위 `ETA2`·유속 `UU2/VV2`(흐름-파 상호작용),
  `COUPWIND` 시 바람 `WX2/WY2`를 SWAN 배열로 복사. dry node는 depth/current 0 처리.
  → `couple2swan.F:1128-1142`, `timestep.F:664-682`
  ([adcirc-swan-coupling §D](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md))
- **SWAN → ADCIRC**: SWAN 스펙트럼을 적분해 radiation stress `ADCIRC_SXX/SXY/SYY` 계산
  (`ComputeRadiationStresses`, `couple2swan.F:112`) → 그 gradient를 nodal 파-유도 force
  `RSNX2/RSNY2`로 변환(`ComputeWaveDrivenForces`, `:210`) → ADCIRC momentum의 wind stress에
  가산(`timestep.F:721-725`). **이 RS gradient가 ADCIRC 내부에서 wave setup을 생성**한다.
  ([adcirc-swan-coupling §C](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md))

> **중요(wave setup의 출처)**: SWAN unstructured 경로는 자체 `SETUP` 명령을 **내부적으로 비활성**한다
> (`swanpre1.ftn:2089-2092`,
> [swan-adcirc-coupling-implementation §F](../../models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md)).
> 따라서 coupled run에서 wave setup은 SWAN이 아니라 **ADCIRC가 radiation-stress gradient를 흡수**해
> 수위 응답으로 만들어낸다. SWAN `SETUP` 카드를 켜는 설정은 unstructured에서 무효.

## 워크플로 (실행 순서)

```
0. 비정형 메시 준비 (공유)
   fort.14  : 하나의 unstructured 삼각망 (ne, np, 좌표·수심, 경계 vmark)
   → ADCIRC와 SWAN이 같은 파일을 read (translation 없음).
     SWAN은 fort.26의 'READ UNSTRUC ADC' 로 동일 fort.14 를 직접 parse.

1. ADCIRC 입력
   code/fort.15  : NWS=3xx (예: 320 = GAHM vortex + SWAN waves),
                   DT(ADCIRC dt), RNDAY, NODAL ATTRIBUTES, output 제어,
                   (선택) &SWANTimeControl namelist (PR #498)
   code/fort.13  : nodal attributes (마찰 등, 선택)
   code/fort.22  : 기상 강제 (NWS 베이스 자리; GAHM이면 best track)

2. SWAN 입력
   code/fort.26  : SWAN 명령 파일. 'READ UNSTRUC ADC' + 물리(GEN3/BREAK/FRIC) +
                   COMPUTE NONSTAT (DELTC = 결합 주기) + BLOCK/TABLE 출력

3. 결합 바이너리 실행
   padcswan      : ADCIRC + SWAN을 한 프로세스에서 결합 (makefile 'padcswan' 타겟)
   (병렬) adcprep --np N --partmesh; adcprep --np N --prepall; mpirun -np N padcswan

4. 산출
   ADCIRC: fort.63(수위 η = surge+tide+wave setup), fort.64(유속), maxele.63
   SWAN  : fort.<블록> (Hs, Tp, Dir, RS), 또는 fort.26 BLOCK/TABLE 출력
```

## 결합 주기(time-step) 정합

| 항목 | 규칙 | 근거 |
|---|---|---|
| ADCIRC time step | `DT` (보통 0.5–5 s) | [adcirc-swan-coupling §B](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md) |
| SWAN 결합 주기 | `SWAN_DT` (보통 60–1800 s) — SWAN COMPUTE `DELTC` | 〃 |
| 결합 간격 | 정수비 `SWAN_DT / DT` (예 300/2 = 150) | `couple2swan.F:1079-1081` |
| 호출 조건 | `mod(ITIME, CouplingInterval)==0` 일 때만 SWAN 호출 | `adcirc.F:475-483` |
| 시간 중심화 | SWAN run 중 보간 midpoint 사용 | `couple2swan.F:1212-1215` |

- `SWAN_DT`가 `DT`로 정확히 나눠떨어지지 않으면 간격이 반올림되어 출력 빈도 이상 발생.
- 위 정수비·DELTC 정합은 [swan-adcirc-coupling-implementation Working Rules 5](../../models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md)
  ("COMPUTE NONSTAT DELTC must align with ADCIRC coupling interval")와 일치.

## fort.15 NWS 인코딩 (개략)

`NWS`의 **백의 자리**가 radiation-stress 결합(`NRS`)을 인코딩하고, 나머지가 베이스 기상 강제다
(`read_input.F:1790-1817`). 리터럴 `NWS=83/84`는 본 코드 경로에서 **무효**.

| Input NWS | NRS | 베이스 NWS | 의미 |
|---|---:|---:|---|
| `308` | 3 | 8 | OWI ASCII 기상 + SWAN 파 |
| `312` | 3 | 12 | OWI WIN/PRE + SWAN |
| `320` | 3 | 20 | GAHM vortex + SWAN |
| `300` | 3 | 0 | 기상 없음, SWAN 파만 (테스트) |

→ 표·인코딩 전거: [adcirc-swan-coupling §F](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md)
(`read_input.F:1790-1817, 2255-2261`; "WAVES WILL BE COUPLED TO SWAN" 로그).

### (선택) SWAN 시간창 제한 — PR #498

폭풍 landfall 전후로만 SWAN 계산을 돌려 wall-clock을 줄이는 phase-1 기능
([adcirc-swan-coupling — SWAN Temporal Controls](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md)):

```
# fort.15 끝
&SWANTimeControl RunStartDateTime='YYYYMMDD.HHMMSS' /
# fort.26 COMPUTE 카드를 원하는 구간으로
COMPUTE  YYYYMMDD.HHMMSS  1200 SEC  YYYYMMDD.HHMMSS
```
- 시간창 밖 스텝은 SWAN을 skip하고 radiation stress를 0으로 둠(해당 구간은 ADCIRC-only 효과).
- namelist 미지정 또는 `-` 포함 sentinel(`"-99999"`) 시 **기존 동작(전체 시간 SWAN)** 유지(backward-compat).
- ⚠ 이 기능은 PR #498(OPEN) 기준 — 머지 여부·버전 확인 필요.

## 재현 조건

- **바이너리**: 반드시 `padcswan`(결합 타겟). `padcirc`는 `NWS=3xx`라도 SWAN이 링크되지 않아
  **파 없이 조용히** 실행됨(`makefile:195-233`,
  [adcirc-swan-coupling §G](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md)).
- **메시 단일성**: ADCIRC와 SWAN이 **같은 `fort.14`**를 봐야 함(같은 디스크 경로 권장).
  SWAN은 자신의 copy를 read하므로 두 파일이 다르면 경계에서 결과가 조용히 어긋남
  ([swan-adcirc-coupling-implementation Working Rules 1·Pitfalls](../../models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md)).
- **wave setup**: SWAN `SETUP` 비활성(위 박스). setup은 ADCIRC의 RS 흡수로만 발생.
- **hot-start**: ADCIRC `IHOT=67/68`(또는 NetCDF), SWAN spectral hot-start는 별도(`SwanHotStartUnit`).
  두 시각이 일치해야 함. NetCDF `NRS=3` 재시작은 잠재 이슈 보고됨(`netcdfio.F90:8017-8085`) — 소규모 검증 후 사용.
- **좌표·방향관례**: 두 모델 동일 좌표계, SWAN 방향관례(nautical/cartesian) 일관.
- ⚠ **본 예제는 검수된 source-analysis·개념 노트 기반 절차 템플릿**(입력값은 placeholder).
  실제 케이스는 도메인 메시·수심·태풍 트랙으로 대체. 정량 결과 run은 미수록(reproducible 절차만 제공).

## 파일

| 파일 | 내용 |
|---|---|
| [`code/fort.15`](code/fort.15) | ADCIRC 제어 outline — NWS=3xx, DT, 결합 주기 자리, SWANTimeControl namelist |
| [`code/fort.26`](code/fort.26) | SWAN 명령 outline — READ UNSTRUC ADC, GEN3, COMPUTE NONSTAT DELTC |
| [`code/run_padcswan.sh`](code/run_padcswan.sh) | adcprep 분할 → mpirun padcswan 실행 순서 outline |
| [`results/README.md`](results/README.md) | 검증 포인트 (수위 분해, RS gradient, 로그 확인) |
