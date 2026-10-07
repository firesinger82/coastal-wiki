---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Model_Grid/Layers.md
lines: 60
sha256: 8cf27e7f1a4cde6e06055b6e5f0497a4076963c74bb972e2e4c2028d6b377ee5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Layers.md — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Layers / 메타데이터 — 페이지 식별자 `241696991` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–14 | Layers / 설정 진입 — Sigma-Zed(SGZ)와 Standard Sigma(SIG) 층 체계를 선택하고 층 수를 설정한다(10). 로컬 `2019-09-16_2-22-31_PM.png`를 열었다(12). 표의 `(Layer #, Layer Fraction, Number of Active Cells in the Layer)` 표시값은 `(55,0.0182,1183); (54,0.0182,1183); (53,0.0182,1070); (52,0.0182,1030); (51,0.0182,988); (50,0.0182,947); (49,0.0182,908); (48,0.0182,864); (47,0.0182,833)`이다(12, 그림; 마지막 행은 화면 아래에서 일부 잘려 있다). 오른쪽 Thickness 표는 55–53층 `0.018180`, 52–46층 `0.018182`를 표시한다. SGZ 옵션의 값은 `Maximum Number of Layers (KC): 55`, `Minimum Active Layers (must be >= 1) (KMin): 2`, `Typical Water Rise of Above Initial Conditions (m): 0`이다(12, 그림). |
| 15–24 | Standard Sigma Stretch Grid — 절 제목·빈 줄을 포함한다. Standard Sigma 선택 시 SGZ 옵션은 표시되지 않는다(17). 원문: `KC = the number of water layers` (19); `The relative thicknesses must add up to 1 (or very close).` (21); `layer 1 is the bottom-most layer` (21); `the highest layer number is the surface layer (i.e. KC).` (21). EE는 층 수에 맞춰 균등 비율을 자동 배분하고 KC 변경에 맞춰 경계조건도 조정한다(21·23). 본문은 이 기능을 주의해서 사용하라고 적는다(23). |
| 25–41 | Sigma-Zed Vertical Layering — 급격한 하상고 변화에서 압력 경사 오차(pressure gradient error)를 줄이기 위한 층 체계를 설명한다(25–29). SIG는 모든 셀에 같은 층 수와 상대 두께를 사용한다(27). SGZ는 셀별 층 수를 다르게 둘 수 있지만 각 셀의 층 수는 시간에 대해 일정하고 두께는 시간에 따라 변한다(29). 원문: `maximum and minimum number of layers` (29); `20 to 50 layers or more` (29). 로컬 `image2016-6-20_155529.png`를 열었다(33). 왼쪽 SIG는 하상 경사를 따라 휘고 얇아지는 층, 오른쪽 SGZ는 수평 층과 계단형 하상 경계를 보여 준다. 두 세로축의 눈금은 위에서 아래로 `0, 250, 500, 750, 1000`이고 축 단위·가로축 이름·화살표는 없다. 선택 원문은 `Specified Bottom Layer`와 `(GRIDV=1)`, `Uniform Layer Thickness`와 `(GRDIV=2)`, `Specified Thickness from Top`과 `(GRIDV=3)` (38)이다. 로컬 `image2024-6-11_13-55-11.png`를 열었다(40). 메뉴는 Standard Sigma와 SGZ 세 방식을 보여 준다. Thickness 표는 15층 `0.066662`, 14–5층 각각 `0.066667`이며 `Layer Sum: 1.00000`, `Maximum Depth (m): 7.8500`이다(40, 그림). |
| 42–45 | Specified Bottom Layer (GRIDV=1) — 원문 옵션명은 `Specified Bottom Layer (GRIDV=1)` (42)이다. 인접 셀의 수직 층이 같은 평면에 정렬되지 않으며, 먼저 최대 수심과 최대 층 두께를 계산한다(44). 구역화(zonation)를 허용한다(44). 수면고가 영역별로 크게 다른 연안과 성층·급변 하상 시스템에 적합하다고 적는다(44). |
| 46–57 | Uniform Layer Thickness (GRIDV=2) — 옵션명은 `Uniform Layer Thickness (GRIDV=2)` (46)이다. 저층 범위 원문은 `The bottom layer thickness can vary from 20-120% of the overlying layer.` (48)이다. 최대 두께에 `DZCK` (48)를 곱하여 최대 수심 셀의 각 층 두께를 계산한다. `Zonation cannot be applied in *Uniform Layers* option.` (48)이며 외부 유입 영향이 작은 정온 시스템에 적합하다고 적는다. 부력 적분(buoyancy integral)의 두께와 고도차를 설명한다(50). `Typical Rise Above Initial Conditions` (52)는 모든 Sigma Z 옵션에서 쓸 수 있지만 특히 `SGZ =2` (52)를 위해 설계되었다. 수위가 통상값보다 1 m 낮으면 `typical water rise value to 1` (52)로 설정하는 예를 들고, 조석 시스템에서는 평균 조위 가까이 설정할 수 있다고 적는다. 폴리곤(polygon)으로 일부 영역만 조정할 수 있다(52). `After selecting *Set SGZ Layering* and *OK*, the layers are all automatically updated to the Sigma Stretch layering.` (54)를 그대로 적는다. 로컬 `6-18-2024_10-44-55_AM.jpg`를 열었다(56). 표는 `Maximum Number of Layers (KC): 10`; `Minimum Active Layers (must be >= 1) (KMin): 2`; `Typical Water Rise of Above Initial Conditions (m): 0.1`을 표시한다(56, 그림). |
| 58–60 | Sigma-Zed Specified Thickness from Top (GRIDV=3) — 옵션명은 `Sigma-Zed Specified Thickness from Top (GRIDV=3)` (58)이다. 초기 층 두께를 정확히 지정할 수 있다(60). 네 방향 모두 연결이 없는 최하층 고립 셀은 EE가 자동 제거하고 위쪽 셀에 병합한다(60). 본문은 수문(gate) 시나리오와 수심에 따른 수리구조물 모의에 적합하다고 적는다(60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 38·46: Uniform Layer Thickness의 코드가 38행에서는 `GRDIV=2`, 46행에서는 `GRIDV=2`이다.
- 52·54: SGZ 설정 설명 뒤의 갱신 문장은 `Sigma Stretch layering`이라고 적는다.
- 29: Figure 4를 가리키지만 이 파일에는 Figure 4 번호 캡션이 없다.
- 33: 격자 그림의 세로축에는 수치만 있고 단위가 없다.

