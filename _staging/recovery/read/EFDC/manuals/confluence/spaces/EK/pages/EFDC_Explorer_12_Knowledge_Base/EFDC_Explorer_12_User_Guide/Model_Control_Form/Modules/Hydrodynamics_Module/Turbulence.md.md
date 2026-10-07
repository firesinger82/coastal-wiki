---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Turbulence.md
lines: 56
sha256: b8c9f6deed4a0ee26d0e61ff942c18a3ac61ca590b0bfdf619e2a73698de2151
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Turbulence.md — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Turbulence / 메타데이터 — 페이지 식별자 `240288479` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–19 | Turbulent Diffusion / 메뉴·표시값 — 수평·수직 와점성(eddy viscosity)과 확산계수(diffusivity), HMD 셀, 파랑 유도 난류(wave-induced turbulence) 옵션을 소개한다(10–14). 로컬 `Turbulence01.png`를 열었다(16). 화면 값은 `Background/Constant Horizontal Eddy Viscosity (AHO, m²/s): 1`; `Horizontal Momentum Diffusivity (AHD, dimensionless): 0.05`; `Wall Roughness: 0.002`; `Large Cell Aspect Ratio (m/m): 0`; `Time Advance Filter: Average: T = ([t-1] + t)/2`; `Vertical Eddy Viscosity (AVO, m²/s): 1E-07`; `Vertical Molecular Diffusivity (ABO, m²/s): 1E-08`; `Max. Kinematic Eddy Viscosity (AVMX, m²/s): 1E-06`; `Max. Eddy Diffusivity (ABMX, m²/s): 1E-08`; `Number of HMD Cells: 0`이다(16, 그림). 시간 필터 식을 LaTeX로 옮기면 `T = ([t-1] + t)/2`이다(16, 그림의 기호·괄호 유지). 빈 줄·절 제목·Figure 1 캡션을 포함한다. |
| 20–33 | Horizontal Momentum Diffusion / 공간 가변 — 수평 운동량 확산(Horizontal Momentum Diffusion, HMD) 비활성 선택에서는 배경 상수 `AHO` (20)를 사용한다. 코드 원문은 `ISHM flag set to 0 (ISHMD=0)` (20)이다. Spatially Varying 선택은 셀별 AHO를 계산하여 넓은 셀 크기 범위의 수치 확산 오차를 줄인다고 적는다(22). Smagorinsky 설정의 원문은 `AHD, Smagorinsky’s Coefficient`, `Dimensionless`, `(ISHMD=1)`, `AHD>0` (24)이다. 이 옵션에서는 오염물질 확산을 적용하지 않는다(24). `If AHD=0 then the *Constant Horizontal Eddy Viscosity*option will be used.` (24)이다. 공간 가변 AHD는 두 체크박스를 선택하고 Assign으로 지정한다(26). `AHMAP.INP` (26)는 셀별 AHO·AHD 목록을 저장한다. AHO가 음수이면 `use the cell area times the input value to compute the cell’s AHO` (26)라고 적는다. 상수·연산자·폴리곤으로 영역별 값을 설정하고 2DH View로 확인한다(28–30). 로컬 `Turbulence02_03combine.png`를 열었다(32). 화면은 AHO/AHD 계수 선택과 폴리곤·산포자료 배정 폼을 보여 준다. |
| 34–37 | ISHMD=2 / 수직 확산 — `Smagorinsky with Wall Drag and WC Diffusion`, `(ISHMD=2)` (34)는 전체 HMD·벽 영향과 염분·수온을 포함한 모든 성분 수송 확산을 적용한다. 매우 균일한 유동계에서 성분 수송이 필요할 때 사용해야 한다고 적는다(34). 속도 자료가 있으면 수평 확산계수를 ViewPlan에서 볼 수 있다(34). 수직 배열 원문은 `AVO & ABO arrays in EFDC, respectively` (34)이다. 설정 항목 원문은 `Time Advance Filter`, `Vertical Eddy Viscosity`, `Vertical Molecular Diffusivity`, `Maximum Magnitude for Diffusivity Terms`, `Maximum Kinetic Eddy Viscosity`, `Maximum Eddy Diffusivity` (36)이다. 빈 줄을 포함한다(35·37). |
| 38–50 | Turbulent Intensity / 제한·폐합 상수 — 난류 강도(turbulent intensity) 절 제목·빈 줄을 포함한다(38–39). 생산 실행 설정 원문은 `Advection Scheme`와 `to 1`, `Sub-Option`, `Galerpin (Sub-option=1), Kantha and Clayson (Sub-option=2) or Kantha (Sub-option=3)` (40)이다. 길이 척도·RIQMAX 제한은 `no length scale and RIQMAX limitation`, `to limit RIQMAX in the stability function only`, `to limit both the length scale and RIQMAX` (42)이다. 다층에서 수직 난류를 제한할 때 마지막 옵션이 중단 가능성을 줄인다고 적는다(42). 벽 근접 함수(wall proximity function)는 `no wall proximity effects on the turbulence`, `parabolic over depth wall proximity`, `open channel wall proximity` (44)이다. `Modify` (46) 후 폐합 상수를 바꿀 수 있지만 충분한 근거 없이 바꾸지 않아야 한다고 적는다. 로컬 `image2020-10-5_15-44-7.png`를 열었다(48). 화면의 표시값은 `Von Karman Constant, κ: 0.4`; `Min. Turbulent Intensity Squared (m/s)²: 1E-08`; `Min. Turbulent Intensity Squared * Length Scale (m/s)²: 1E-12`; `Min. Dimensionless Length Scale: 0.0001`; `Max. Richardson Number, RIQMAX: 0.28`; `Turbulent Constant, CTURB2: 10.1`; `Constant 1: 1.8`; `Constant 2: 1`; `Constant 3: 1.8`; `Constant 4: 1.33`; `Constant 5: 0.25`; `CTURB1: 16.6`이다(48, 그림). |
| 51–56 | Momentum Correction — 운동량 보정(momentum correction) 절 제목·빈 줄·설명·그림·캡션을 포함한다(51–56). 로컬 `2019-05-02_10-26-09_AM.jpg`를 열었다(55). 선택 목록은 `No Correction`, `Momentum Correction`, `Curvature Correction`이다(55, 그림). 표시된 VV·UV Momentum Flux Correction, UU·VV·UV Curvature Acceleration Correction, Correction for Curvature X Equation 및 Y Equation 값은 각각 `0.0825`이다(55, 그림). UU Momentum Flux Correction 값은 펼친 메뉴가 가려서 읽지 못했다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 20: 같은 문장에 `ISHM`과 `ISHMD=0` 두 이름이 나온다.
- 22·26: 22행은 `using the expression`, 26행은 `according to the equation above`라고 적지만 이 파일에는 AHO 계산식이 없다.
- 40·48: 본문은 `Galerpin`, 그림은 `Galperin et al. (1988)`로 적는다.
- 48: 강도 제곱과 길이 척도의 곱 항목에도 단위가 `(m/s)²`로 표시되어 있다.
- 55: 펼친 메뉴가 UU Momentum Flux Correction 값을 가린다.

