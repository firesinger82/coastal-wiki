---
file: models/ADCIRC/raw/manuals/wiki/markdown/WTIMINC.md
lines: 5
sha256: ba78568ca568d24879ef11b33757e639571652e64b9235993217e03faca787dd
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# WTIMINC.md — 판독 구간 기록

구간은 1행부터 5행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | WTIMINC — 제목과 판본 표기를 포함한다(1–3). `fort.15 file`에서 기상 강제력(meteorological forcing) 자료 집합 사이의 시간 간격을 초 단위로 정하는 매개변수라고 설명한다(5). 이 변수와 입력 줄의 구성은 `NWS` 값에 의존한다고 설명한다(5). 일반적인 요구 조건에는 매개변수형 와류 모형(parametric vortex models)에 대한 예외가 있다(5). OWI 형식에서 두 번째 시간 간격 변수를 쓰는 조건도 제시한다(5). 원문: `` `WTIMINC` is a parameter in the [fort.15 file](/Fort.15_file) that is the time increment between meteorological forcing data sets (in seconds) in input files like the [fort.22](/Fort.22).  This parameter and the [line on which it appears](/Fort.15_file_format#WTIMINC) depend on the value of `[NWS](/NWS)`.  For a detailed breakdown of what goes on this line in the fort.15 file, see the [supplemental meteorological/wave/ice parameters](/Supplemental_meteorological/wave/ice_parameters) page. Broadly, `WTIMINC` is required for `ABS(NWS)>1` unless you are using one of the parametric vortex models for meteorology. Relatedly, note that when `[NWS](/NWS)=-14`, a second parameter, `[WTIMINC_12](/index.php?title=WTIMINC_12&action=edit&redlink=1)` defines the time increment for meteorological data for the OWI-formatted files. `` (5). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `WTIMINC_12` 참조에는 `redlink=1`이 표시되어 있다.
