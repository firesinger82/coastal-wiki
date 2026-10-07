---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Initial_Conditions/Salinity_IC.md
lines: 16
sha256: d7adbb6779bd21b53856375ec22e7ef47f2c3275b5c55acea77d7c3dab7893c6
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Salinity_IC.md — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Salinity IC — 문서 식별자, 제목, space, URL, 판본, 갱신 시각과 문서 계층의 frontmatter(1–9). |
| 10–16 | Salinity IC — 염분(salinity) 초기조건의 Assign을 누르면 다각형(polygon) 배정 양식이 열린다(10). 파일 옵션·형식은 Bathymetry를 참조한다(12). 층 선택 조건 원문: `Users are able to select to apply cell properties for a specific layer or all layers in the model.` (12) 결측 자료의 다운로드와 적용 범위 원문: `The data for *Salinity IC* if missing may be downloaded from online open sources` (14) `Users are able to select to apply the downloaded data for the whole model domain or just a specific missing data area.` (14) 빈 줄과 그림을 포함한다(11,13,15–16). `2019-09-16_5-15-07_PM.png`을 열었다(16). 그림은 초기염분 보고서·농도 설정·다각형 배정 양식이다. 보고서의 `Average (ppt)`, `Minimum (ppt)`, `Maximum (ppt)`는 모두 `2.568`이다. `Use Spatially Varying Initial Conditions`가 체크되어 있고 `Average Salinity (ppt): 2.568`이다. 배정 양식은 `All grid cells`, `For All Layers`, `Constant: 0`, `Replacement`를 선택하며 `Only grid cells inside polygons`, `For A Specific Layer: 1`, `From Scatter (XYZ) Data`, `From Profile Data`, `Maximum value`, `Minimum value`도 표시한다. Assign·Download와 More 버튼을 볼 수 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: Figure 1 링크는 `#Figure1`을 가리킨다. 이 파일에는 해당 anchor 정의가 없다. 링크 뒤에 닫는 괄호가 하나 더 있다.
