---
title: "Delft3D dimr (Delft3D Integrated Model Runner) — coupling framework 4 packages"
topic: delft3d-dimr-coupling
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/dimr/ + packages/ 직접 ls — 4 packages (dimr, dimr_lib, dimr_lib_tests, dimr_testcomponent) + 보조 (doc, docs, schemas, scripts) 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 디렉토리 ls 직접"
verification_date: 2026-05-24
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_overview.md
  - models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher.md
---

# Delft3D `dimr` — Integrated Model Runner

> 출처: [`models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/dimr/`](../raw/source_code/Delft3D/src/engines_gpl/dimr/) 직접 구조. **Delft3D 의 multi-engine coupling framework** — 여러 엔진 (flow2d3d / dflowfm / wave / waq / rtc / part) 을 단일 orchestrator 로 결합.

## 1. dimr 디렉토리 layout

```
engines_gpl/dimr/
├── doc/         — sphinx docs 소스
├── docs/        — 빌드된 문서
├── packages/    — 4 packages (아래 §2)
├── schemas/     — XML schema (dimr_config.xml 등)
└── scripts/     — 빌드·운영 스크립트
```

## 2. 4 Packages 구조 (verified)

| Package | 역할 |
|---|---|
| `dimr` | **메인 executable** — DIMR launcher (`run_dimr.bat`·`run_dimr.sh`) |
| `dimr_lib` | **공유 라이브러리** — 엔진 인터페이스 (BMI compliant) |
| `dimr_lib_tests` | dimr_lib 단위 테스트 |
| `dimr_testcomponent` | 테스트용 minimal coupling component |

## 3. DIMR 의 역할 — Why multi-engine coupling

D3D-4 시절: flow2d3d ↔ wave (SWAN) coupling 만 가능 (comm file 통신).
DIMR 도입 후: **임의 N 엔진** 결합 가능 — 예시:

| 시나리오 | DIMR 결합 |
|---|---|
| 수리 + 파랑 | dflowfm ↔ wave (SWAN) |
| 수리 + 수질 | dflowfm ↔ waq |
| 수리 + 파랑 + 수질 | dflowfm ↔ wave ↔ waq (3-way) |
| 수리 + 강수-유출 | dflowfm ↔ rr (RR-runoff) |
| 수리 + 실시간 제어 | dflowfm ↔ rtc (RealTime Control) |
| 수리 + 입자 | dflowfm ↔ part |
| 전 결합 (operational) | dflowfm + wave + waq + rr + rtc + part 모두 |

## 4. BMI (Basic Model Interface) 표준

DIMR 의 핵심 설계: **BMI (CSDMS Basic Model Interface)** 준수.

각 엔진은 BMI standard 의 메소드 구현:
- `initialize(config_file)` — 엔진 초기화
- `update(dt)` — 한 시간단계 진행
- `get_variable(name)` — 상태 변수 접근
- `set_variable(name, value)` — 변수 설정
- `finalize()` — 종료

DIMR 가 **orchestrator** 로 각 엔진에 BMI 호출 → 시간 동기화 + 변수 교환.

## 5. dimr_config.xml — 운영 설정

DIMR 의 runtime 설정 파일 (`schemas/` 의 XSD 정의):

```xml
<dimrConfig>
  <documentation>
    <fileVersion>1.00</fileVersion>
    <createdBy>...</createdBy>
  </documentation>
  <control>
    <parallel>
      <startGroup>
        <time>0 60 86400</time>  <!-- start interval end -->
        <coupler name="flow2wave"/>
        <start name="flowEngine"/>
        <start name="waveEngine"/>
      </startGroup>
    </parallel>
  </control>
  <component name="flowEngine">
    <library>dflowfm</library>
    <workingDir>./flow</workingDir>
    <inputFile>model.mdu</inputFile>
  </component>
  <component name="waveEngine">
    <library>wave</library>
    <workingDir>./wave</workingDir>
    <inputFile>wave.mdw</inputFile>
  </component>
  <coupler name="flow2wave">
    <sourceComponent>flowEngine</sourceComponent>
    <targetComponent>waveEngine</targetComponent>
    <item>
      <sourceName>water_level</sourceName>
      <targetName>water_level</targetName>
    </item>
  </coupler>
</dimrConfig>
```

→ 사용자가 XML 한 파일에 결합 토폴로지 명세 → DIMR 가 자동 orchestration.

## 6. 실행 방식

```bash
# Linux
run_dimr.sh dimr_config.xml

# Windows
run_dimr.bat dimr_config.xml
```

→ 단일 명령으로 multi-engine 시뮬레이션 시작.

## 7. flow2d3d 와의 비교

| 항목 | flow2d3d (legacy comm file) | dimr (BMI) |
|---|---|---|
| Coupling 메커니즘 | 파일 IO (comm.dat) | BMI in-memory |
| 동기화 빈도 | 매 communication step (분 단위) | 가능 최대 (time-step 단위) |
| 엔진 수 | 2 (FLOW + WAVE) | 임의 N |
| 통신 비용 | 디스크 IO | 메모리 (빠름) |
| 설정 | mdf + mdw 각각 | dimr_config.xml 한 곳 |
| 신규 사용 | (legacy) | **권장** |

## 8. 운영 시나리오 — 한국 적용

| 한국 시나리오 | DIMR 구성 |
|---|---|
| 항만 hydro + 입자 추적 (oil spill) | dflowfm + part |
| 하구 hydro + 수질 (적조·DO) | dflowfm + waq |
| 연안 hydro + 파랑 (storm wave) | dflowfm + wave (SWAN) |
| 댐 방류 + 강 + 연안 | rr + dflowfm + part |
| 항만 + 실시간 제어 (수문) | dflowfm + rtc |

## 9. 작성 우선순위 (남은 M-D)

- `delft3d_dimr_config_xml_reference.md` — dimr_config.xml 카드 family + XSD 정형
- `delft3d_bmi_interface_walkthrough.md` — BMI 메소드 별 엔진 구현 (initialize·update 등)
- `delft3d_flow_wave_coupling_dimr.md` — dflowfm + wave DIMR 결합 케이스 walkthrough

## 10. 관련 자료

- [[delft3d_engines_overview]] — 12 engines 라인업
- [[delft3d_dflowfm_overview]] — DIMR native coupling 의 주 엔진
- [[delft3d_flow2d3d_dispatcher]] — D3D-4 legacy (DIMR 외 limited)
- [[../manual-notes/delft3d-manuals-overview]] — 53 PDFs 인덱스
- [[../web-refs/delft3d-official-resources]] — Lesser 2004 + Kernkamp 2011 인용
- 외부: [CSDMS BMI](https://csdms.colorado.edu/wiki/BMI), [Deltares DIMR doc](https://oss.deltares.nl/web/delft3dfm/dimr)
