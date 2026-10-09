---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/special_features/ice_modifications.rst
lines: 36
sha256: 77be8de9ec50f451366a36eda0ff67d01a53bc764cc866fe30df4cb5d5b928db
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ice_modifications.rst — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | Ice Modifications / Overview — 얼음 피복(ice coverage)이 극지·아극지 유체동역학(hydrodynamics)에 영향을 주는 수정의 취지를 포함한다(1–9). 표면 풍응력(surface wind stress), 흐름에 대한 얼음 마찰(ice friction), 얼음·물 운동량 교환(momentum exchange), 질량 보존식(mass conservation equation) 수정이라는 네 문서상 항목을 옮긴다(11–14). 원문: ` 1. Ice coverage effects on surface wind stress ` (11); ` 2. Ice friction effects on water flow ` (12); ` 3. Changes in momentum exchange due to ice-water interaction ` (13); ` 4. Modifications to mass conservation equations to account for ice presence ` (14). |
| 16–25 | Implementation — 지배방정식(governing equation), 얼음 전용 입력 매개변수, 출력, 부분·전체 얼음 피복 영역의 특수 수치 처리라는 네 설명 항목을 옮긴다(19–24). 구체적인 수식·변수 이름은 이 구간에 없다. 원문: ` The implementation of ice modifications in ADCIRC involves several components: ` (19); ` * Modification of the governing equations to include ice effects ` (21); ` * Addition of ice-specific parameters in input files ` (22); ` * New output options for ice-related variables ` (23); ` * Special numerical treatments for partially and fully ice-covered regions ` (24). |
| 26–36 | Usage / References — fort.15의 특정 매개변수 설정 의무와 별도 얼음 자료 입력의 가능성을 원문대로 옮긴다(29). 구현·사용·이론 세부사항을 동일한 공식 PDF 주소로 안내하는 두 문장과 마지막 행을 포함한다(31·36). 해당 PDF는 이번 대상 목록에 포함되지 않으므로 읽지 않았다. 원문: ` To enable ice modifications in ADCIRC, specific parameters must be set in the fort.15 file. Additionally, ice coverage data may be provided through dedicated input files. ` (29); ` Detailed documentation on the implementation and usage of ice modifications can be found in the ADCIRC documentation: "Modifications to ADCIRC for ICE Coverage" (available at https://adcirc.org/wp-content/uploads/sites/2255/2016/01/adcirc_modifications_for_ice.pdf). ` (31); ` For complete details on the theoretical foundation, implementation, and usage of ice modifications in ADCIRC, please refer to the official documentation at the ADCIRC website: https://adcirc.org/wp-content/uploads/sites/2255/2016/01/adcirc_modifications_for_ice.pdf  ` (36). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 29: 활성화에 specific parameters를 설정해야 한다고 적지만 이 파일은 그 매개변수 이름·값·기본값을 제시하지 않는다.
