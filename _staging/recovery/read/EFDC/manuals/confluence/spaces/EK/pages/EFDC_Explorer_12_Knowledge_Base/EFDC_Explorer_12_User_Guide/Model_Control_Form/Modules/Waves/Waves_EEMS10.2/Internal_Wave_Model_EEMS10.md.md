---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Waves/Waves_EEMS10.2/Internal_Wave_Model_EEMS10.md
lines: 30
sha256: 114fc170e0f8d9a3eca9b08be1815d82463f815908eae2b414929fdc33219cb2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Internal_Wave_Model_EEMS10.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목 `Internal Wave Model (EEMS10.2)`, space, URL, 버전, 갱신 시각, 문서 계층을 수록한다(1–9). |
| 10–18 | 내부 파랑 모델(Internal Wave Model) — SMB(Sverdrup, Munk, and Bretschneider) 모델은 `wave height`, `wave direction`, `wave period`를 계산한다(10). 파향은 풍향과 같으며 굴절(refraction), 회절(diffraction), 반사(reflection)를 고려하지 않는다(10). 외부 파랑 입력 없이 바닥 전단응력(bed shear stress)과 파랑 유발 흐름을 모의하며 셀별 취송거리(fetch)를 2DH View에서 볼 수 있다(12). Nikuradse 입자 거칠기와 유체역학 바닥 거칠기(hydrodynamic roughness)를 구분한다(14). 수식·매개변수 원문: `The *Wave Parameter & Options* frame allows the user to specify Ks, the Nikuradse sand roughness value as shown in [Internal Wave Model (EEMS10.2)#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/244777193#InternalWaveModel(EEMS10.2)-Figure1). This can be estimated as Ks = 2.5 x d50. The Nikuradse roughness is not the same as the hydrodynamic roughness (i.e., bottom roughness, Z0) used by EFDC to solve the hydrodynamic equations. The Nikuradse roughness is a grain roughness and represents more of a local scale phenomenon.` (14) 적용 조건·입력·방향 수 원문: `For the cases of ISWAVE=3 and ISWAVE=4, available only in EFDC+, the wind time series provided in the WSER.INP file is used to compute the instantaneous values of wave parameters with fetch calculated for each cell in sixteen directions. The effect of shoreline and EFDC internal masks are included in the fetch calculations. The resulting wave parameters are then used to calculate total bed shear stress, with bed shear stress linked to the current generated shear stress via the Grant Madsen approach.` (16) `From the release of EE5, there has been the ability to internally generate wind-induced waves for bed shears only (ISWAVE=3). This can also include the radiation stresses for the whole water column (ISWAVE=4). These options allow the simulation of wave effects and re-suspension of sediments inside EE.` (18) |
| 19–22 | Figure 1 — 그림 참조와 캡션을 포함한다(19–22). 로컬 그림을 직접 열었다(20). 내부 파랑과 `Include Radiation Stress`를 선택한 Wave 설정 화면이다(20 그림). 화면 예시 값은 `Number of Wave Cells: 1252`, `Nikuradse Sand Roughness (Ks, m): 0.0025`, `Rotational Radial Stress: 1`, `Irrotational Radial Stress: 1`, `Fraction of Dissipation in Vertical TKE Closure: 1`, `Moving Bed Effect: 2`, `Weight for Depth as Eddy Viscous Length Scale: 0.1`, `√(ΔxΔy) Weight as Eddy Viscous Length Scale: 0.1`이다(20 그림). 이 값은 화면 예시이며 기본값으로 명시되지 않았다. 그림의 제곱근 표현을 LaTeX로 옮기면 `\sqrt{(\Delta x\Delta y)}` (20)이다. `Include Wave Stokes Drift in Mass Transport` (20)는 선택되지 않았다. |
| 23–28 | 계산 격자 부분집합(Subset of Computational Grid) — 파랑 셀 수의 기본 관계, 체크박스 적용 조건, 다각형 파일 선택, 폼을 닫고 다시 열어 수를 갱신하는 순서를 설명한다(24). 원문: `By default, the number of wave cells is the same as the model active cells. However, the user can define the number of wave cells by using the *Use Subset of Computational Grid* checkbox option. When the option is checked, the user then needs to browse the polygon file. The wave cells are defined within the polygon. To allow EE to properly update the *Number of Wave Cells,*click *OK* button to exit the *Wave* form, then LMC to reopen the *Waves* module, then the *Number of Wave Cells* is updated on the *Wave* form as shown in [Internal Wave Model (EEMS10.2)#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/244777193#InternalWaveModel(EEMS10.2)-Figure2).` (24) Figure 2 로컬 그림을 직접 열었다(26). `Use Subset of Computational Grid`를 선택하고 다각형 파일을 지정한 화면이며 `Number of Wave Cells: 58`을 표시한다(26 그림). 그림 26에도 같은 제곱근 표현 `\sqrt{(\Delta x\Delta y)}` (26)과 선택되지 않은 `Include Wave Stokes Drift in Mass Transport` (26)가 보인다. |
| 29–30 | Wave Parameters & Options — 회전·비회전 스위치와 이동 바닥 효과(Moving Bed Effect)의 값 및 적용 조건을 명시한다(30). 원문: `Some parameters setting inside the *Wave Parameters & Options* are on/off switches. Such as *Rotational Radial Stress* and *Irrotational Radial Stress*,  users can enter 1 to activate the calculation and 0 to de-activate. *Moving Bed Effect* calculation only takes action when users set to include radiation stress (ISWAVE = 2/4), input 2 to have the moving bed effect, and 0 not to include this effect.` (30) |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 거칠기 추정식의 `d50` (14)를 이 문서에서 정의하지 않는다(14).
- 그림의 제곱근 표현에 `\Delta x` (20)와 `\Delta y` (20)가 있다. 이 문서는 두 기호를 정의하지 않는다(20, 26 그림).
