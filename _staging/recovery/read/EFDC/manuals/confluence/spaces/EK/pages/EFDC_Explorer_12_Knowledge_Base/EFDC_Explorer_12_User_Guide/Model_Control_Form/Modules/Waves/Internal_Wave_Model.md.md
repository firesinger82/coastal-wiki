---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Waves/Internal_Wave_Model.md
lines: 30
sha256: b5d100f3c62603136f55aa9244c6f0ac6ce3939cde385e4d6ebabffc8b8aa753
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Internal_Wave_Model.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Internal Wave Model — 페이지 메타데이터를 담은 frontmatter이다 (1–9). |
| 10–13 | 내부 파랑 모델과 적용 범위. 바람이 흐름과 표면파(surface wave)를 만들며 총 저면 전단응력(total bed shear stress) 계산에 파랑 요인을 고려해야 한다고 설명한다 (10). SMB (Sverdrup, Munk, and Bretschneider) 모델이 파고(wave height), 파향(wave direction), 주기(wave period)를 계산한다 (10). 파향은 풍향(wind direction)과 같으며 굴절(refraction)·회절(diffraction)·반사(reflection)를 고려하지 않는다는 원문은 `The wave direction is the same as the wind direction. This means that the effects of refraction, diffraction, and reflection are not taken into account in this internal wave model.` (10)이다. 바람이 발생시키는 저면 전단응력 및 파랑 유도 흐름(wave-induced current) 효과를 모의하는 데 외부 파랑이 필요하지 않다고 적는다 (12). 바람 구역별 셀의 취송거리(fetch)를 2DH View에서 볼 수 있다 (12). 빈 줄을 포함한다 (11, 13). |
| 14–19 | 조도(roughness), 입력과 모의 옵션. Nikuradse 모래 조도와 식 원문: `The *Wave Parameter & Options* frame allows the user to specify Ks, the Nikuradse sand roughness value as shown in [Figure 1](#Figure1). This can be estimated as Ks = 2.5 x d50. The Nikuradse roughness is not the same as the hydrodynamic roughness (i.e., bottom roughness, Z0) used by EFDC to solve the hydrodynamic equations. The Nikuradse roughness is a grain roughness and represents more of a local scale phenomenon.` (14). `Ks = 2.5 x d50` (14)는 원문 그대로 옮긴 식이다. Ks는 유체역학(hydrodynamics)의 저면 조도 Z0와 같지 않으며 입자 조도(grain roughness)라고 설명한다 (14). 옵션 적용 조건·입력 파일 원문: `For the cases of ISWAVE=3 and ISWAVE=4, available only in EFDC+, the wind time series provided in the WSER.INP file is used to compute the instantaneous values of wave parameters with fetch calculated for each cell in sixteen directions. The effect of shoreline and EFDC internal masks are included in the fetch calculations. The resulting wave parameters are then used to calculate total bed shear stress, with bed shear stress linked to the current generated shear stress via the Grant Madsen approach.` (16). EFDC+의 ISWAVE=3·4는 WSER.INP 풍속 시계열을 사용하며 셀마다 16방향 취송거리를 계산한다 (16). 해안선(shoreline)과 내부 마스크(internal mask)를 취송거리 계산에 포함한다 (16). Grant Madsen 방법으로 흐름 전단응력과 연계한다 (16). 저면 전단만 사용하는 옵션과 수층 전체의 복사응력(radiation stress)을 포함하는 옵션 원문: `From the release of EE5, there has been the ability to internally generate wind-induced waves for bed shears only (ISWAVE=3). This can also include the radiation stresses for the whole water column (ISWAVE=4). These options allow the simulation of wave effects and re-suspension of sediments inside EE.` (18). 빈 줄을 포함한다 (15, 17, 19). |
| 20–23 | Figure 1 — 내부 파랑 모델 설정. `11-23-2020_4-23-18_PM.png`를 열었다 (20). 그림은 SMB Model과 복사응력·Rotational Radial Stress가 선택된 Wave 설정 화면이다 (20). 화면에 보이는 매개변수 문자열은 `√(ΔxΔy) Weight as Eddy Viscous Length Scale: 0.1`이다 (20 그림). 이 값은 그림의 표시 값이며 본문은 기본값이라고 정의하지 않는다 (20). Figure 1 캡션과 빈 줄을 포함한다 (21–23). |
| 24–29 | 파랑 계산 셀의 부분집합(subset). 기본값과 적용 조건 원문: `As default, the number of wave cells is the same as the model active cells. However, the user can define the number of wave cells by using the *Use Subset of Computational Grid* checkbox option. When the option is checked, the user then needs to browse the polygon file. The wave cells are defined within the polygon. To allow EE to properly update the *Number of Wave Cells,*click *OK* button to exit the *Wave* form, then LMC to reopen the *Waves* module, then the *Number of Wave Cells* is updated on the *Wave* form as shown in [Figure 2](#Figure2).` (24). 기본 파랑 셀 수는 활성 모델 셀 수와 같다 (24). 체크 상자를 선택한 뒤 다각형(polygon) 파일을 찾아야 하며 그 안의 셀을 파랑 셀로 정의한다 (24). OK로 폼을 닫고 Waves 모듈을 다시 열어야 Number of Wave Cells가 갱신된다 (24). `11-23-2020_4-34-53_PM.png`를 열었다 (26). 그림은 Use Subset of Computational Grid와 다각형 파일 경로를 지정한 뒤 Number of Wave Cells가 251로 표시되는 설정 화면이다 (26). Figure 2 캡션과 빈 줄을 포함한다 (25, 27–29). |
| 30–30 | 추가 활성화 옵션. 체크 상자 옵션 이름 원문: `Some parameters setting inside the *Wave Parameters & Options* as *Rotational Radial Stress,* *Irrotational Radial Stress* and *Moving Bed Effect*activated options can be used by checking on the option checkboxes.` (30). Rotational Radial Stress, Irrotational Radial Stress, Moving Bed Effect를 체크해 활성화할 수 있다 (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14행의 식에 나오는 `d50`의 정의와 단위가 이 파일의 본문에 없다. `Z0`는 저면 조도로 설명하지만 그 단위는 본문에 없다.
- 14·24행의 `#Figure1`, `#Figure2` 참조에 해당하는 명시적 앵커 정의가 이 파일에 없다. 22·28행에는 캡션이 있다.

