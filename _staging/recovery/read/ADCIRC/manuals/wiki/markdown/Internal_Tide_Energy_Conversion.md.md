---
file: models/ADCIRC/raw/manuals/wiki/markdown/Internal_Tide_Energy_Conversion.md
lines: 91
sha256: 5541b696161fc862001c2405c5a4182946a6fb6aaf34a618c49088846df95785
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Internal_Tide_Energy_Conversion.md — 판독 구간 기록

구간은 1행부터 91행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | Internal Tide Energy Conversion — 제목·판본·버전 표기·목차·빈 줄을 포함한다(1–20). 심해의 가파르고 거친 지형 위로 표면 조석이 흐르면서 순압(barotropic) 에너지가 경압(baroclinic) 모드의 내부조석(internal tide)으로 전환되는 과정을 설명한다(9). ADCIRC는 fort.13의 공간 변화 절점 속성(nodal attribute) internal_tide_friction으로 이 효과를 구현한다고 적는다(9). 원문: `ADCIRC version:` (5); `  &#8805;  53.01  ` (7); `Internal tide energy conversion refers to the energy conversion from barotropic to baroclinic modes as surface tides flow over steep and rough topography in the deep ocean generating internal tides. The "lost" barotropic tidal energy is often accounted for through a linear friction term in large-scale numerical models that are barotropic or not fine-scaled enough to resolve the energy conversion. It is implemented in ADCIRC through a spatially varying nodal attribute called [internal_tide_friction](/Fort.13_file#Internal_Tide_Energy_Conversion), in the [fort.13 file](/Fort.13_file).` (9). |
| 21–42 | Background and Theory — 내부조석 생성 이론의 역사와 표면 조석 에너지 수지(energy balance)에서의 중요성을 설명한다(21–23). 원문은 내부조석이 전지구 순압 조석 소산(dissipation)의 약 30%를 담당한다고 적는다(23). 이론·수치 연구와 대규모 조석 모델의 매개화(parameterization) 연구를 인용한다(25–41). 원문: `The basic theory for generation of internal tides in the deep ocean was established several decades ago.[&#91;1&#93;](#cite_note-Bell1975-1) However, it was not thought to be incredibly important to the global energy balance of the surface tides until the modern satellite era when it was discovered that internal tides are responsible for approximately 30% of the global barotropic tidal dissipation.[&#91;2&#93;](#cite_note-Garrett2007-2)[&#91;3&#93;](#cite_note-3)[&#91;4&#93;](#cite_note-4) ` (23). |
| 43–48 | Attribute Summary — 조석 경계조건과 조석 포텐셜(tidal potential) 함수를 통해 조석이 포함될 때만 internal_tide_friction을 선택해야 한다고 적는다(45). 작은 영역 또는 심해 비중이 작은 영역에서는 중요하지 않을 수 있다(45). IT_Fric의 차원 수, 단위, 속도에 곱하는 선형 마찰(linear friction), 모의 전 수심 정규화(normalization), 수면 고도 부분 제외와 보통 적용하는 수심을 적는다(47). 원문의 조건·차원·단위를 그대로 옮긴다. 원문: `In a computational domain covering a large portion of the deep ocean, the effect of internal tide energy conversion may be needed to obtain more accurate tidal solutions. The user should only elect to use the internal_tide_friction nodal attribute when tides are included in the simulation through tidal boundary conditions and tidal potential functions. The attribute may not be important for domains that are small in size and/or do not cover a significant portion of the "deep ocean" (the portion of the ocean excluding the continental shelf). ` (45); `ADCIRC reads the internal_tide_friction attribute in as the IT_Fric variable, which can have 1 (scalar) or 3 (tensor) dimensions. The attribute has dimensions of [1/time], meaning that it is a linear friction term which is multiplied by the velocity in the governing equations, and is normalized by the ocean depth prior to simulation. Hence, it ignores the water surface elevation portion of the total water depth, which is reasonable since the term and theory it is based on is only applicable to deep ocean. Typically, it is only applied to ocean depths greater than 100-500 m.[&#91;14&#93;](#cite_note-Pringle2018-14)[&#91;16&#93;](#cite_note-Arbic2010-16)` (47). |
| 49–54 | Specifying IT_Fric Values — IT_Fric은 Bell의 선형 이론에 따른 해석식(analytical formulations)으로 정하며 이 이론은 아임계 지형(sub-critical topography)에서 유효하다고 적는다(51). 최근 ADCIRC 논문의 구성·구현 세부사항을 안내한다(53). 이 절은 계산식 자체를 제시하지 않는다(49–54). 원문: `IT_Fric values are determined through analytical formulations based on Bell's linear theory[&#91;1&#93;](#cite_note-Bell1975-1), valid in what is called sub-critical topography.[&#91;2&#93;](#cite_note-Garrett2007-2) ` (51). |
| 55–91 | References — Bell의 내부파(internal wave) 생성 이론, 내부조석 생성과 혼합, 위성 고도계(altimeter)의 에너지 소산 추정, 해석 매개화와 ADCIRC 구현 등 참고문헌 18개를 적는다(55–91). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 67행: 참고문헌 6의 저자 `F. Pétrélis, S.L. Smith, W.R. Young` 목록이 같은 행에서 두 번 반복된다.
