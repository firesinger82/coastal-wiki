# 모델별 근거 준비 상태 — 2026-09-13

**13개 모델 모두 로컬 본체와 문서 근거가 있다. 그러나 수집 집합의 완결이나 모델 전체 설명의 정확성까지 확인된 상태는 아니다.** 현재 기술 노트는 437편(frontmatter citation_status 기준 verified 433, draft-unsourced 4)이다. 기존 독립 비교 노트 5편의 직접 모델 링크는 모두 해석되지만, 연결 대상의 공개 갭·미승인 정정과 비교표의 조건 누락이 남아 있다. 조사 결과는 아래처럼 **자료·모델 노트 보강 → 근거가 확인된 연결 → 비교** 순서에 적용한다.

이 문서는 로컬 자료·기록을 조사한 AI 작성 보고서다. 원문 판독 영수증이나 사람 승인이 아니다. [범위](scope.md), [기계 집계·출처 해시](readiness.json), [직접 확인한 문제](observations.md), [작업 계획](../../plan.md#현재-작업)을 함께 본다. 실제 과학 내용 변경은 이번 조사에 포함하지 않았다.

## 1. 앞선 조사를 어떻게 적용하는가

[Grok·Claude·논문 조사](../../research/digests/2026-09-12-wiki-purpose-review.md)는 자료 수집량, 게시 주장 검증, 모델 연결 검증, 질문에 대한 활용을 구분했다. 여기에 사용자의 이번 순서 정정을 반영한다.

1. **모델 자료 수집·정리**: 본체 판본, 이론·매뉴얼, 입력/출력, 구현 설명의 대응을 모델 안에서 정리한다. 필요한 근거가 부족하면 해당 자료를 보강한다.
2. **모델별 설명 확인**: 식·단위·조건·버전과 미확정 부분을 확인한다. 이미 있는 근거를 재사용하고, 해당 주장에 필요한 검토·승인 조건을 유지한다.
3. **연결 노드 구성**: 앞 단계에서 뒷받침된 모델 항목끼리 개념·이론의 관계를 연결한다. 링크가 있다는 사실과 내용이 서로 맞는다는 판정을 구분한다.
4. **비교 노트 작성/갱신**: 연결된 근거에서 비교 축을 만든다. 아직 근거가 없는 모델 행·수치는 확정 설명으로 채우지 않는다.

여러 모델을 비교하려면 그 비교에 참여하는 각 모델의 해당 항목이 먼저 준비되어야 한다. 모델 전체 감사의 종료 조건은 별도로 유지한다. 현재 조사에서 과거 감사 대기열을 다시 실행하거나 그 고정 범위를 바꾸지 않는다.

## 2. 모델별 수집·정리 상태

노트 수 = source-analysis / manual-notes / web-refs의 Git 추적 파일(하위 폴더 포함), 각 README 제외. 갭 수 = `has_source_needed`가 **true / false / 표기 없음**인 노트 수이며, 표기 없음은 **미상**이다. 정정 미승인 수는 `source_correction_human_approval: not-issued` 표기 기준이다. false도 해당 기록의 판정이지 이번 재검증이 아니다. 본문에는 메타데이터에 반영되지 않은 source-needed가 있을 수 있다.

모든 행에서 본체 디렉터리와 이름을 지정한 원문 파일/문서 디렉터리의 존재를 확인했다. 이는 필요한 모든 자료가 수집되었다는 판정이 아니다. 실제 경로·현재 로컬 Git HEAD·확인한 문서 경로는 [readiness.json](readiness.json)에 있다. HEAD 조회는 노트 인용 판본과의 일치 검증을 대신하지 않는다.

| 모델 | 노트 수 | 갭 true/false/미상 | 확보된 문서 진입점 | 연결 전에 확인할 사항 |
|---|---:|---:|---|---|
| ADCIRC | 38 / 21 / 2 | 14 / 7 / 40 | [경계·forcing 공식 문서 목록](../../models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md), PDF 모음 | 조석 입력 설명 재사용 가능. ETRF 설명 오류와 외부 조석 DB 위상규약 근거부터 보완 |
| CADMAS-SURF | 17 / 5 / 0 | 3 / 3 / 16 | [동봉 매뉴얼 목록](../../models/CADMAS-SURF/manual-notes/cadmas-manuals-catalogue.md), SURF3D 영문 PDF | SURF3D·2F 등 대상 변형을 고정하고 필요한 일문/결합 설명의 공개 갭 선별. 부속 GUI 내부 조사로 확대하지 않음 |
| Celeris | 9 / 1 / 3 | 0 / 0 / 13 | [상류 architecture/config 문서](../../models/Celeris/manual-notes/celeris-architecture-and-config.md) | 원논문은 이 노트에서 서지만 확인한 상태. 논문에 기대는 주장은 원문 확보·판독 여부부터 구분 |
| Delft3D | 48 / 11 / 1 | 0 / 0 / 60 | [FLOW 등 모듈별 매뉴얼](../../models/Delft3D/manual-notes/delft3d-manuals-overview.md) | FLOW와 FM을 분리하고 사용할 매뉴얼 판본·구현의 대응 및 주장별 갭 확인 |
| EFDC | 38 / 9 / 1 | 0 / 1 / 47 | [운영 r8.5.0·이론 v12 문서](../../models/EFDC/manual-notes/efdc-manuals-overview.md) | EFDC+ 12.4 본체와 문서 버전차 확인. GVC는 별도 계보로 유지 |
| FUNWAVE | 11 / 3 / 2 | 0 / 0 / 16 | [2016 사용자 매뉴얼](../../models/FUNWAVE/manual-notes/funwave-user-manual-full.md), TVD/GPU 본체 | TVD/GPU·문서의 차이를 항목별 확인. 아래 preflight의 미완을 연결 완료로 바꾸지 않음 |
| LISFLOOD-FP | 8 / 1 / 1 | 0 / 0 / 10 | [동봉 사용자 매뉴얼](../../models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md), v8.2 아카이브 | ACC/FV1/DG2/GPU 등 솔버별 적용 범위를 확인한 뒤 연결 |
| ROMS | 37 / 4 / 6 | 1 / 3 / 43 | [공식 wiki 문서 목록](../../models/ROMS/manual-notes/roms-wiki-overview.md) | CPP 옵션과 본체 판본에 맞는 주장 확인. 동봉 WRF 내부로 확장하지 않음 |
| SFINCS | 9 / 5 / 1 | 0 / 0 / 15 | [공식 RST 기반 수치 노트](../../models/SFINCS/manual-notes/sfincs-numerical-implementation.md) | 일부 RST는 제목만 있는 문서. 수치식은 구현 근거 사용; manifest의 후속 Galibier 판본 확정 기록 함께 확인 |
| SWAN | 30 / 29 / 4 | 1 / 0 / 62 | [사용자·기술·구현 문서 묶음](../../models/SWAN/manual-notes/swan-documentation-stack.md) | 쇄파 옵션별 command·식의 공개 갭부터 해당 주장에 한정해 확인 |
| SWASH | 21 / 3 / 1 | 0 / 0 / 25 | [동봉 기술문서](../../models/SWASH/manual-notes/swash-tech-documentation-overview.md) | 모델 노트에 있는 beta 자동선택 조건을 비교표로 전달해야 함. 기술문서 미작성 장은 본체/논문 근거와 구분 |
| ShorelineS | 5 / 2 / 1 | 0 / 0 / 8 | [동봉 Roelvink 2020 논문](../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md) | 해안선 변화·수송공식별 근거와 미상 갭을 확인 후 연결 |
| XBeach | 40 / 8 / 1 | 0 / 9 / 40 | [master·Kingsday·비정수압 문서 차이](../../models/XBeach/manual-notes/xbeach-document-discrepancies-and-version-drift.md) | 초안 4편, 정정 사람 승인 미발급 14편. R1–R4 미완 유지; 연결 대상 정정의 영향과 적용 게이트를 확인 |

`raw/manuals/`가 없는 모델도 동봉 PDF·RST·architecture 문서를 가지고 있다. 별도 폴더가 없다는 이유로 “매뉴얼 미수집”으로 분류하지 않았다. 반대로 문서 카탈로그가 있다는 이유로 원문 전체 판독 완료로 표시하지 않았다.

### 서로 다른 검수 이력

[AUDIT-LEDGER](../../models/AUDIT-LEDGER.md)의 7월 “13/13 종결”은 해당 snapshot의 단위가 하나 이상의 모델/매뉴얼 노트로 실질 커버되었음을 뜻한다. XBeach 절은 이후 9월 기록으로 갱신되어 있다. 이 원장의 done을 이후 독립 2회 판독·연결 감사 완료로 해석하면 안 된다.

[8월 말 이후 공정표](../total-read/codex-defect-reports/PROGRESS.md)는 더 강한 P0/R1/R2/CW/SUP/V/HG 감사의 기록이다. 이 표에서는 ADCIRC·ROMS·Delft3D·EFDC가 코어 부분 검토, CADMAS·Celeris·LISFLOOD-FP·SFINCS·SWAN·SWASH·ShorelineS는 **그 후속 감사 공정의 미착수**로 남아 있다. 이는 기존 모델 노트가 없다는 뜻이 아니다. 오래된 표의 비율과 다음 작업 지시는 이번 상태·실행 순서로 재사용하지 않는다.

- **FUNWAVE**: [preflight](../total-read/model-audit/FUNWAVE/connectivity-preflight/coverage-summary.json)의 기존 코드 집합 277건은 의미 판독 기록이 있으나 독립 2회 판독 없는 34건(솔버 29·스크립트 5), 문서/매뉴얼 의미 판독 없는 93건이 남아 있다. 이는 저장된 snapshot의 집계이며 이번에 전체 원본을 재검증한 수치가 아니다.
- **XBeach**: [현재 잔여 목록](../total-read/model-audit/XBeach/connectivity/remaining-20260912/remaining.json)의 R1–R4는 미완이다. 이번 준비 상태 조사는 그 범위·완료·승인 상태를 바꾸지 않는다.

## 3. 기존 비교 노트의 연결 상태

아래는 파일명이 `*-cross-model.md`인 5편의 **본문 직접 링크** 조사다. 각주식 wikilink와 Markdown 링크를 실제 모델 노트에 해석했다. 모델 노트 내부에 삽입된 EOS·스칼라 수송 등의 비교 전체는 포함하지 않는다. 연결된 노트 수는 비교표의 모델 행 수와 다르다. 예를 들어 시간적분은 Delft3D-FLOW/FM을 따로 기술한다.

| 비교 노트 | 직접 모델 노트 수 | 비교 노트 자체 갭 | 선행 확인 |
|---|---:|---|---|
| [쇄파](../../concepts/waves/wave-breaking-cross-model.md) | 7 | true | SWASH beta 조건이 본문에는 있으나 표에 누락. SWAN/XBeach 일부 옵션의 공개 갭; XBeach 정정 미승인 대상 1편 |
| [저면마찰](../../concepts/currents/bottom-friction-cross-model.md) | 18 | true | ADCIRC NOLIBF·HBREAK/FTHETA·3D BBL 설명의 공개 갭. 대상 노트 18편 모두 갭 플래그 미상 |
| [연직혼합](../../concepts/currents/vertical-mixing-cross-model.md) | 7 | true | ADCIRC MY2.5 안정함수·q² 경계식은 기반 모델 설명 보강이 선행되어야 함 |
| [시간적분](../../concepts/currents/time-integration-cross-model.md) | 32 | false | XBeach flow/nonh 정정 미승인 2편의 영향을 주장별 대조해야 함. 비교 노트 false를 재사용 승인으로 삼지 않음 |
| [침수·노출](../../concepts/compound-flooding/wetting-drying-cross-model.md) | 10 | false | 연결 노트 중 공개 갭 true 1편·미상 9편, XBeach flow 정정 미승인 1편의 영향을 확인 |

5편에서 해석 실패한 본문 링크는 0개다. **내용 검증 통과를 뜻하지 않는다.** 날짜가 오래되었거나 정정 대상과 연결되었다는 이유만으로 모든 비교 문장이 틀렸다고 판정하지도 않았다. 위 항목의 상세 경로·본문 줄·메타데이터는 [readiness.json](readiness.json)에 있다.

## 4. 다음 작업과 종료 조건

**첫 보강 묶음은 사용자가 실제로 질문한 ADCIRC 조석 입력 설명이다.** 대상은 [harmonic-prep](../../models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md)와 [forcing-implementation](../../models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md) 두 노트다.

- fort.14 경계 노드 순서 ↔ fort.15 NBFR/EMO/EFA, 위상·시간 기준, 경계 조석과 조석 퍼텐셜의 구분을 원문과 대응시킨다.
- `ETRF=0` 설명 오류를 조건을 보존해 정정할 변경안으로 만든다. 외부 DB 위상규약·지역 성능·SAL 정량값은 각 공식/원문 근거 확보 전까지 미확정으로 유지한다.
- 종료 조건: 핵심 입력 절차의 각 주장에 출처·조건이 연결되고, 발견한 ETRF 모순이 검토된 변경안에서 해소되며, 남은 외부 자료 갭을 명시한다. 적용되는 독립 검토와 사람 결정은 해당 변경에 대해 거친다. ADCIRC 전체 감사나 외부 DB 변환기 제작으로 확대하지 않는다.

그다음 SWASH의 이미 정리된 조건을 기존 비교표에 전달하는 작은 정정, ADCIRC 연직혼합의 부족한 모델 근거 보강을 각각 별도 범위로 다룰 수 있다. **새로운 비교 노트를 먼저 늘리는 작업은 잡지 않는다.** 다른 모델도 실제 연결에 사용할 항목을 정한 뒤 위 표의 판본·갭을 확인한다.

## 5. 검토·보존

수집 결과는 [collect.py](collect.py)로 재현한다. 기존 노트 snapshot의 SHA가 현재 437개 모델 노트와 5개 비교 노트에 모두 일치함을 확인하고 메타데이터를 재사용했다. 원본 트리 전체를 다시 복제하지 않았다. 검토 결과와 최종 변경 범위 확인은 [validation.md](validation.md)에 기록한다.
