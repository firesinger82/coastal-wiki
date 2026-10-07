---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/External_Forcing_Data/Atmospheric.md
lines: 12
sha256: ea5735cc2b71df5ca09bfa2ec59dd2e139a5d5a6993197d034b065bb76a89207
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Atmospheric.md — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Atmospheric / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–12 | Atmospheric / 대기(atmospheric) 자료 양식 — 10행 앞부분은 색상 CSS다. 대기 경계조건(boundary condition)의 Boundary Data Series가 External Forcing Data의 일반 양식과 같다고 적는다(10). 12행 `EE10_162.png`의 로컬 사본을 열었다. 그림은 `ASER_1` 자료 표다. 보이는 열 머리글은 `Time (days)`, `Atmospheric Pressure (mbar)`, `Dry Bulb Temperature`, `Relative Humidity (-)`, `Rainfall (m/day)`, `Evaporation (m/day)`, `Solar Radiation (W/m²)`, `Cloud Cover (-)`이다(12행 그림). 건구 온도(dry bulb temperature) 열에는 단위가 표시되지 않는다. 완전히 보이는 표 행을 `행 번호: Time, Atmospheric Pressure, Dry Bulb Temperature, Relative Humidity, Rainfall, Evaporation, Solar Radiation, Cloud Cover` 순서로 옮긴다: ``1: 1230.000000, 1032.0, 13.36, 0.946, 0.0000e+00, 0.0000e+00, 0.0, 1.000``; ``2: 1230.080000, 1032.0, 12.37, 0.958, 0.0000e+00, 0.0000e+00, 0.0, 1.000``; ``3: 1230.130000, 1032.0, 12.67, 0.951, 0.0000e+00, 0.0000e+00, 0.0, 1.000``; ``4: 1230.170000, 1032.0, 12.57, 0.946, 0.0000e+00, 0.0000e+00, 0.0, 1.000``; ``5: 1230.250000, 1031.0, 11.86, 0.931, 0.0000e+00, 0.0000e+00, 5.3, 1.000``; ``6: 1230.290000, 1031.0, 11.82, 0.937, 0.0000e+00, 0.0000e+00, 22.6, 1.000``; ``7: 1230.330000, 1032.0, 12.03, 0.927, 0.0000e+00, 0.0000e+00, 65.4, 1.000``; ``8: 1230.420000, 1031.0, 12.12, 0.914, 0.0000e+00, 0.0000e+00, 240.2, 1.000``; ``9: 1230.460000, 1031.0, 12.45, 0.900, 0.0000e+00, 0.0000e+00, 336.7, 1.000``; ``10: 1230.500000, 1031.0, 13.27, 0.861, 0.0000e+00, 0.0000e+00, 473.3, 1.000``; ``11: 1230.580000, 1029.0, 14.98, 0.793, 0.0000e+00, 0.0000e+00, 875.0, 1.000``; ``12: 1230.630000, 1029.0, 15.72, 0.768, 0.0000e+00, 0.0000e+00, 606.6, 1.000`` (12행 그림). `# of Points: 7148` 중 위 12개 자료 행만 완전히 보인다. 그림의 값은 예시이며 본문에는 기본값·허용 범위가 없다(10·12). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12행 그림: `Dry Bulb Temperature` 열에 온도의 단위가 없다. 10행 본문에도 해당 단위가 정의되지 않는다.
- 12행 그림: 화면은 전체 점 수를 7148로 표시한다. 완전히 보이는 자료 행은 처음 12개이며 나머지는 화면 밖에 있다.
