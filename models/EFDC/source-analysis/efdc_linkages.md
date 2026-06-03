---
title: "EFDC+ Linkages — 외부모델 결합/출력: WASP(4-8)·CE-QUAL-ICM·food chain(toxics 생물축적)·EFDC_Explorer 바이너리·고빈도 출력"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Linkages/ 10파일 헤더·구조 + foodchain.f90 + 트리거 플래그(input.f90:264 ISWASP / :3140 ISFDCH / :292 ISWASP==99→ISICM) + 호출부(hdmt.f90:1574 FOODCHAIN / :1373 ISICM) 직접 read. file:line 인용. WASP M.Morton 1994 / foodchain Hamrick 2001."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 외부결합 트리거·데이터 흐름 구조 verbatim"
verification_date: 2026-06-03
related:
  - models/EFDC/source-analysis/efdc_toxics.md
  - models/EFDC/source-analysis/efdc_water_quality.md
  - models/EFDC/source-analysis/efdc_caldisp_postprocess.md
---

# EFDC+ Linkages — 외부모델 결합/출력 layer

> `Linkages/` 10파일(12140줄) 직접 read. EFDC 결과를 **외부 수질·생물축적 모델·시각화**로 내보내는 결합/출력 layer (core 물리 아님, I/O). 4 계열: **WASP**(EPA 수질) / **CE-QUAL-ICM**(Corps 수질) / **food chain**(toxics 생물축적) / **EFDC_Explorer + 고빈도 출력**.

## 1. WASP linkage (wasp4-8 + wasp7hydro/wasp8hydro)

- **WASP** (Water Quality Analysis Simulation Program, US EPA) box-model 로 EFDC 수리·분산을 전달. `ISWASP`(input C7, `input.f90:264`) = 버전/모드 선택. 버전별 파일: `wasp4.f90`(637)~`wasp8hydro.f90`(1549). M. Morton 1994.
- 출력: hydrodynamic flow + **dispersion** 을 WASP 입력 그룹(B hydro / C / D dispersion: WASPB/C/D)으로 write.
- **residual transport**: `CALMMT`(mean mass transport averaging) 가 `ISWASP>0` 또는 `ISSSMMT>0` + `RESSTEP>0` 시 호출(`hdmt2t.f90:1055`) — 조석평균 잔차 flux/dispersion 을 WASP box exchange 로 집계. [[efdc_caldisp_postprocess]] 의 잔차 dispersion 텐서와 같은 계열(조석평균 transport).
- **`ISWASP==99 → ISICM=1`** (`input.f90:292`) — WASP 99 = CE-QUAL-ICM 모드 전환.

## 2. CE-QUAL-ICM (ceqicm.f90, 790)

- `CEQICM` = **CE-QUAL-ICM**(US Army Corps 3D 부영양화 모델) interface. EFDC 흐름·분산을 ICM box 격자로 매핑(IDRICM 등).
- `ISICM` 활성 시 `CALMMT` **skip**(`hdmt.f90:1373` `if(ISICM==0) CALL CALMMT`) — ICM 자체 transport 사용. EFDC = hydro 공급자.
- [[efdc_water_quality]](내장 Eutrophication, CE-QUAL-ICM 유래 kinetics)와 구분: 이쪽은 **외부 ICM 실행파일**로 전달.

## 3. Food chain — toxics 생물축적 (foodchain.f90, 696)

- `ISFDCH`(input, `:3140` + `NFDCHZ`(zone 수)·`HBFDCH`(bed depth)·`TFCAVG`(평균 주기)) 활성 + **`ISTRAN(5)≥1`**(toxics) 시 `CALL FOODCHAIN(1)`(`hdmt.f90:1574`). Hamrick 2001.
- **공간·시간 평균 toxics 농도**를 외부 food chain(생물축적) 모델 입력으로 산출. 3-phase 분배 배열:
  - water: `FDCHTXWF`(free dissolved) / `FDCHTXWC`(DOC-complexed) / `FDCHTXWP`(particulate) + `FDCHDOCW/POCW`
  - bed: `FDCHTXBF/BC/BP` + `FDCHDOCB/POCB`
- → [[efdc_toxics]] 의 free/DOC/particulate 3-phase 평형분배를 그대로 받아 `TFCAVG` 주기·`NFDCHZ` zone·`HBFDCH` 깊이로 평균. 어류·저서생물 노출 농도 계산용.

## 4. EFDC_Explorer + 고빈도 출력

- **`mod_efdcout.f90`(3329)** = `EFDCOUT` — **EFDC_Explorer(EE)** 후처리 GUI 용 바이너리 출력(precision EE 고정, RPEM 포함). DSI 의 공식 시각화 도구 연계.
- **`mod_hifreqout.f90`(378)** = `HIFREQOUT` — **고빈도 시계열** 출력(`HFREHYOUT` hydro / `HFRERPEMOUT` RPEM 등). 관측 정점 대응 고해상 시계열.

## 5. 트리거 플래그 요약

| 플래그 | 입력 | 결합 대상 |
|---|---|---|
| `ISWASP` (4-8) | C7 | WASP (99 → ICM) |
| `ISICM` | (ISWASP=99 파생) | CE-QUAL-ICM |
| `ISFDCH` + NFDCHZ/HBFDCH/TFCAVG | C(food chain) | food chain (ISTRAN(5)≥1 필수) |
| EE binary / hi-freq | output 설정 | EFDC_Explorer / 시계열 |

## 6. 위치 (core 아님)

이 layer 는 **EFDC 물리 결과의 export/coupling** 이며 시뮬레이션 동역학에 되먹임 없음(one-way out). 내장 수질은 [[efdc_water_quality]], 내장 toxics 는 [[efdc_toxics]]; 본 노트는 그 결과를 **외부 모델 포맷**으로 내보내는 연계.

## 7. 연결

- [[efdc_toxics]] — food chain 이 받는 toxics 3-phase 분배(free/DOC/particulate)
- [[efdc_water_quality]] — 내장 Eutrophication(CE-QUAL-ICM 유래) vs 외부 ICM/WASP 결합 구분
- [[efdc_caldisp_postprocess]] — CALMMT 잔차 mass transport(WASP box exchange 와 동일 계열)
- 외부: WASP(US EPA) / CE-QUAL-ICM(USACE) / EFDC_Explorer(DSI)
