# concepts/littoral-drift — 연안표사 (Longshore Sediment Transport)

> 연안 breaker zone (쇄파대) 의 wave + nearshore current 에 의해 발생하는 **해변에 나란한 (longshore) 모래 이동**.

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·driver (radiation stress·longshore current)·empirical formula (CERC/Komar)·budget·한국 적용 |
| `02-theory.md` | (미생성) | radiation stress 유도, longshore current Battjes/Bowen 식, breaker line dynamics |
| `03-analysis-methods.md` | (미생성) | sediment budget (control volume), tracer 실험, beach profile survey |
| `04-code-and-tools.md` | (미생성) | XBeach + Delft3D-SED + UNIBEST-LT (1D longshore) + GENESIS |
| `05-examples.md` | (미생성) | 한국 안목항·울산항·태안 longshore drift 사례 |
| `06-model-application.md` | (미생성) | XBeach (surf zone) + EFDC SED — `models/XBeach/` 작성 후 |

## sediment-transport 와의 경계

본 토픽 = 연안 **특정 환경** (breaker zone, wave-dominated, shore-parallel 방향) 의 sediment transport.
인접 토픽 [`concepts/sediment-transport/`](../sediment-transport/) = 일반 표사 (bedload + suspended, 모든 환경).

| 항목 | sediment-transport | littoral-drift |
|---|---|---|
| 범위 | 전반 (강·해저·천해·해변) | 해변 surf zone 한정 |
| 주 driver | bottom shear stress, turbulence | wave radiation stress, longshore current |
| 시간 scale | 분~ 년 | 사건 (storm) ~ 연간 budget |
| 정형화 | Shields, Soulsby 1997 | CERC SPM 1984, Komar & Inman 1970 |
| 모델 | EFDC SED, Delft3D-SED | XBeach, GENESIS, UNIBEST-LT |

## 사용된 source_id

- `cerc-spm-1984` — CERC "Shore Protection Manual" U.S. Army Corps of Engineers 1984 (외부, 본 위키 내 PDF 없음 — TODO sources.yml 등록)
- `komar-inman-1970` — Komar & Inman (1970) "Longshore Sand Transport on Beaches" J. Geophys. Res. 75(30):5914-5927 (외부)
- `marine-sands-manual` — Soulsby (1997) [`concepts/sediment-transport/`](../sediment-transport/) 공유
- `wijetunge-coastal-eng` — [`textbook/md/412319423-...Wijetunge-JJ.md`](../../textbook/md/412319423-An-Introduction-to-Coastal-Engineering-Processes-Theory-Hazards-and-Design-Practice-Wijetunge-JJ.md) (Coastal Engineering Processes book)
- `holthuijsen-waves` — [`textbook/md/Waves-Holthuijsen2007.md`](../../textbook/md/Waves-Holthuijsen2007.md) (Ch 11 sediment transport by waves)

## 연결

- [`concepts/sediment-transport/`](../sediment-transport/) — 일반 표사 (인접)
- [`concepts/waves/`](../waves/) — wave (driver)
- [`concepts/currents/`](../currents/) — nearshore current
- [`concepts/storm-surge/`](../storm-surge/) — storm 시 littoral drift 폭증
- [`models/XBeach/`](../../models/XBeach/) — surf zone 단기 모델

## 작업 계획

[CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일 시작.

다음 단계 후보:
1. ✅ `01-concept.md` verified (2026-05-23)
2. `02-theory.md` — radiation stress 유도 (Longuet-Higgins-Stewart 1964) + longshore current Battjes 1974, Bowen 1969
3. `04-code-and-tools.md` — XBeach surf zone module + GENESIS shoreline change
4. `05-examples.md` — 한국 안목항·울산항·태안 longshore drift survey 사례
5. CERC SPM 1984 source_id 등록 + Komar-Inman 1970 paper citation 추가
