---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_all_raster_maps.cu
lines: 45
sha256: 3ab352b9faf32f1e68c1f824b02dd5fb80619d55690b27d0bea209edeb909f5f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_all_raster_maps.cu — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–16 | 헤더 포함과 `write_all_raster_maps` 정의이다(1–14). 출력 설정·조립 해·최세 x/y간격·모의/해석기 매개변수·저장 간격·첫 시간 단계 표시를 받는다(5–12). 래스터 지도(raster map) 저장 로그를 출력한다(15). 전처리 조건 분기는 없다. |
| 17–30 | 시작 시 3–14행 `write_all_raster_maps` 안. HWFV1 조건이면 `write_all_raster_maps_fv1`을 호출한다(17–29). 함수의 여덟 인수를 같은 순서로 전달한 뒤 분기를 닫는다(21–30). 원문: `if (solver_params.solver_type == HWFV1)` (17). |
| 31–45 | 시작 시 3–14행 `write_all_raster_maps` 안이며 17행 조건 불성립 경로. MWDG2 조건이면 `write_all_raster_maps_dg2`를 호출한다(31–43). 여덟 인수를 같은 순서로 전달하고 분기와 함수를 닫는다(35–45). 원문: `else if (solver_params.solver_type == MWDG2)` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–45: 저장 함수 선택에는 HWFV1과 MWDG2 두 조건만 있다. 마지막 else나 그 밖의 해석기 종류에 대한 오류 처리는 없다.
