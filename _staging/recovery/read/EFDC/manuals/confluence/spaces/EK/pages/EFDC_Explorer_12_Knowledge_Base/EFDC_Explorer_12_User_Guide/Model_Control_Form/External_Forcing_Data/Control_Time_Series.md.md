---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/External_Forcing_Data/Control_Time_Series.md
lines: 12
sha256: 2cde869a6b8af4f58aa9346cab0cfedcc30b6b5339a1a24cfdfe37bd8749ec45
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Control_Time_Series.md — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Control Time Series / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–12 | Control Time Series / 제어 시계열과 사용할 매개변수 — 10행 앞부분은 색상 CSS다. 양식은 External Forcing Data의 일반 양식과 거의 같으며 사용할 매개변수의 플래그(flag)를 설정해야 한다(10). 의무의 원문: ``It is also necessary to set the parameter that will be used by checking the flag shown in Figure 2.`` (10). 12행의 두 로컬 그림 `image2024-5-14_15-28-22.png`, `image2024-5-14_15-29-33.png`를 모두 열었다. 첫 그림은 `GATE OPENING` 시계열의 자료 표다. 머리글은 `Time (days)`, `Opening Height (m)`, `Opening Width (m)`, `Sill Level Change (m)`이다. 자료 행을 `행 번호: Time, Opening Height, Opening Width, Sill Level Change` 순서로 옮긴다: ``1: 0.00000, 10.000, 20.000, 0.000``; ``2: 0.50000, 10.000, 20.000, 0.000``; ``3: 0.54167, 0.000, 20.000, 0.000``; ``4: 0.75000, 0.000, 20.000, 0.000``; ``5: 0.79167, 9.000, 20.000, 0.000``; ``6: 0.83333, 10.000, 20.000, 0.000``; ``7: 1.04167, 10.000, 20.000, 0.000``; ``8: 1.08333, 0.500, 20.000, 0.000``; ``9: 1.12500, 0.000, 20.000, 0.000``; ``10: 1.25000, 0.000, 20.000, 0.000``; ``11: 1.29167, 10.000, 20.000, 0.000``; ``12: 1.58333, 10.000, 20.000, 0.000``; ``13: 1.62500, 0.000, 20.000, 0.000`` (12행 첫 그림). `# of Points: 36` 중 화면에 완전히 보이는 처음 13개 행이다. 둘째 그림은 Parameters 탭의 Extra Parameters 표다. 표의 `Parameter, Value`를 행별로 옮긴다: ``Longitude (deg.), 0``; ``Latitude (deg.), 0``; ``X (m), 0.0``; ``Y (m), 0.0``; ``Time Scale (sec.), 86400.00000``; ``Time Offset (sec.), 0.00000``; ``Opening Height, 1``; ``Opening Width, 1``; ``Sill Level Change, 0``; ``Rating Curve, 0`` (12행 둘째 그림). 이 값들은 화면 예시이며 본문에는 기본값·허용 범위가 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12행 첫 그림: 전체 점 수는 36이지만 완전히 보이는 자료 행은 처음 13개다.
- 10·12: 본문은 Figure 2의 flag를 checking한다고 적는다. 둘째 그림은 Opening Height·Opening Width·Sill Level Change·Rating Curve의 Value를 각각 `1`, `1`, `0`, `0`으로 표시하며 해당 표에 체크 상자는 보이지 않는다.
