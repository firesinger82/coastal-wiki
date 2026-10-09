---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst
lines: 164
sha256: e3ed3abbb579cccebba85768a3f57ab8eeeca43238693eb8500f22d73574b456
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# internal_tide_energy_conversion.rst — 판독 구간 기록

구간은 1행부터 164행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | Internal Tide Energy Conversion — 메타데이터·앵커·제목을 포함한다(1–8). 심해 지형에서 순압(barotropic) 에너지가 경압(baroclinic) 모드로 바뀌며 내부 조석(internal tide)을 생성한다고 설명한다(10–18). 미해상 변환을 선형 마찰(linear friction)로 처리하는 모델과 fort.13 internal_tide_friction 속성을 원문대로 옮긴다. 원문: ` Internal tide energy conversion refers to the energy conversion from barotropic ` (10); ` to baroclinic modes as surface tides flow over steep and rough topography in the ` (11); ` deep ocean generating internal tides. The "lost" barotropic tidal energy is ` (12); ` often accounted for through a linear friction term in large-scale numerical ` (13); ` models that are barotropic or not fine-scaled enough to resolve the energy ` (14); ` conversion. It is implemented in ADCIRC through a spatially varying nodal ` (15); ` attribute called ` (16); `` :ref:`internal_tide_friction <internal_tide_friction>`, in `` (17); `` the :ref:`fort.13 file <fort13>`. `` (18). |
| 20–34 | Background and Theory — Bell 계열 이론과 현대 위성 관측 이후 전역 순압 조석 소산의 약 30% 중요성이 알려졌다는 문서 진술을 옮긴다(23–27). 이론·수치 연구와 대규모 조석 모델의 매개화(parameterization) 문헌 번호를 포함한다(29–33). 원문: ` The basic theory for generation of internal tides in the deep ocean was ` (23); ` established several decades ago. [1]_ However, it was not thought to be ` (24); ` incredibly important to the global energy balance of the surface tides until the ` (25); ` modern satellite era when it was discovered that internal tides are responsible ` (26); ` for approximately 30% of the global barotropic tidal dissipation. [2]_ [3]_ [4]_ ` (27); ` Following this revelation, the past two decades have been subject to a number of ` (29); ` theoretical  [5]_  [6]_  [7]_  [8]_ and numerical  [9]_  [10]_  [11]_ ` (30); ` investigations into internal tide generation and their effects on the surface ` (31); ` tides through parameterization of the energy conversion in large-scale numerical ` (32); ` tidal models.  [12]_  [13]_  [14]_  [15]_  [16]_  [17]_  [18]_ ` (33). |
| 35–54 | Attribute Summary — 큰 심해 영역에서의 필요 가능성, 조석 경계와 조석 퍼텐셜을 포함할 때만 사용해야 한다는 권고, 작은 영역에서 중요하지 않을 수 있다는 표현을 옮긴다(38–44). IT_Fric의 스칼라(scalar) 1 또는 텐서(tensor) 3 차원, [1/time], 속도 곱, 실행 전 수심 정규화(normalization), 자유수면 부분 무시, 통상 100–500m보다 깊은 수심 적용을 원문대로 옮긴다(46–53). 원문: ` In a computational domain covering a large portion of the deep ocean, the effect ` (38); ` of internal tide energy conversion may be needed to obtain more accurate tidal ` (39); ` solutions. The user should only elect to use the internal_tide_friction nodal ` (40); ` attribute when tides are included in the simulation through tidal boundary ` (41); ` conditions and tidal potential functions. The attribute may not be important for ` (42); ` domains that are small in size and/or do not cover a significant portion of the ` (43); ` "deep ocean" (the portion of the ocean excluding the continental shelf). ` (44); ` ADCIRC reads the internal_tide_friction attribute in as the *IT_Fric* variable, ` (46); ` which can have 1 (scalar) or 3 (tensor) dimensions. The attribute has dimensions ` (47); ` of [1/time], meaning that it is a linear friction term which is multiplied by ` (48); ` the velocity in the governing equations, and is normalized by the ocean depth ` (49); ` prior to simulation. Hence, it ignores the water surface elevation portion of ` (50); ` the total water depth, which is reasonable since the term and theory it is based ` (51); ` on is only applicable to deep ocean. Typically, it is only applied to ocean ` (52); ` depths greater than 100-500 m. [14]_ [16]_ ` (53). |
| 55–63 | Specifying IT_Fric Values — Bell의 선형 이론과 아임계 지형(sub-critical topography)에 유효한 해석 공식(analytical formulation), ADCIRC 문헌의 구현 세부 참조를 옮긴다(58–62). 이 파일 자체에는 수식이 제시되지 않는다. 원문: ` *IT_Fric* values are determined through analytical formulations based on Bell's ` (58); ` linear theory [1]_, valid in what is called sub-critical topography. [2]_ ` (59); ` Recent publications using ADCIRC [14]_ [15]_ provide relevant formulation and ` (61); ` implementation details. ` (62). |
| 64–109 | References / 1–8 — raw HTML references 태그와 Bell부터 급격한 지형의 내부 조석까지 문헌 1–8·DOI를 포함한다(64–108). |
| 110–164 | References / 9–18 — Nycander부터 조석 변환 매개화 비교까지 문헌 9–18·DOI와 마지막 행을 포함한다(110–164). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 96: F. Pétrélis, S.L. Smith, W.R. Young의 세 저자 이름이 같은 문헌의 저자 목록에서 두 번 반복된다.
