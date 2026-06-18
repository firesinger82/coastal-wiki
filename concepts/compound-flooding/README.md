# concepts/compound-flooding — 복합침수 (Compound Flooding)

> 연안에서 **여러 침수 인자(조석·폭풍해일·파 + 강우(pluvial) + 하천유량(fluvial))가 동시·상호작용**하여 발생하는 침수. 단일 인자 합산보다 위험이 증폭(예: 해일이 하천 배수를 막아 내수 범람 가중). 연안도시 재해의 핵심.

## 정체

- **1차 축**: 도메인 개념(복합침수 동역학·위험). 침수 인자들의 co-occurrence/interaction.
- 인접: [`concepts/storm-surge`](../storm-surge/)(해일=연안 인자)·[`concepts/tides`](../tides/)·[`concepts/waves`](../waves/)(파 setup/overtopping)·[`concepts/swash-zone`](../swash-zone/)(runup 범람).
- **모델 스펙트럼**: full-physics([`ADCIRC`](../../models/ADCIRC/)·[`Delft3D-FLOW`](../../models/Delft3D/)·[`EFDC`](../../models/EFDC/)) → reduced-complexity([`SFINCS`](../../models/SFINCS/) compound flooding·[`LISFLOOD-FP`](../../models/LISFLOOD-FP/) inundation) → ML emulator([`storm-surge/07-ml-emulators`](../storm-surge/07-ml-emulators.md)). → [`06-model-application.md`](06-model-application.md).

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | (작성 예정) | 복합침수 정의·인자(coastal/pluvial/fluvial)·복합 메커니즘·위험 |
| `06-model-application.md` | (작성 예정) | 침수 모델 스펙트럼 link-hub (full→reduced→ML) |
| `02~05` | (미생성) | 이론·분석법·예제·(05 한국 연안도시 침수) — 후속 |

## 출처 원칙

신규(2026-06-18). 정의·복합 메커니즘은 textbook(Wijetunge·design-of-coastal-structures·sea-level) + SFINCS 공식문서(compound flooding 정의) 인용. 모델 적용은 본 위키 검수완료 source-analysis cross-link. 한국 연안도시 침수 정량은 source-needed(KHOA/적응계획 자료 확보 후).

## 생성 경위

SFINCS(정의적 compound flooding 모델)·LISFLOOD-FP 신설(2026-06-18)로 침수 모델 5종이 모였으나 1차 축에 복합침수 도메인 토픽이 부재 → 신설. 침수 자산(모델+storm-surge+ML emulator)의 개념 허브.
