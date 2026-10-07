---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Lagrangian_Particle_Tracking.md
lines: 38
sha256: cd79ef161e97aedea4c6884733cb7c7ea8e6e872ad6a003932595b6285d6fe6f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Lagrangian_Particle_Tracking.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더인 `models/EFDC/raw/manuals/confluence/spaces/EK/`를 기준으로 적는다.

| 구간 | 내용 |
|---|---|
| 1–9 | Lagrangian Particle Tracking / 문서 메타데이터 — 원문 frontmatter는 문서 식별 정보와 문서 경로를 적는다(1–9). |
| 10–14 | Lagrangian Particle Tracking / 개요·보고 화면 — EFDC+ Explorer는 라그랑주 입자 추적(Lagrangian particle track, LPT)의 전처리와 후처리를 지원한다(10). 문서는 유류 유출, 비상 대응, 수질과 플룸(plume) 추적을 활용 사례로 든다(10). 모듈을 켠 뒤 `LMC`로 보고 화면을 연다고 적는다(10). 문서는 최대 `1.5 million drifters`를 사용한 모의 사례와 입자 수가 많을 때 로딩 시간이 늘어날 수 있음을 적는다(10). 원문: `EFDC+ Explorer incorporates the pre-and post-processing of Lagrangian particle track (LPT). The use of LPT's can be helpful when modeling oil spill tracks, emergency response, water quality applications, and plume tracking. When the *Lagrangian Particle Tracking* module is turned on, a LMC on the menu displays a report, as shown in Figure 1. Here the user can see the total number of particles and the number of groups that have been set, as well as the time for the release of the drifters and the end time for the observation of the drifters. Models with as many as 1.5 million drifters have been simulated, though loading time can increase with a large number of drifters.` (10). 직접 연 로컬 그림 `attachments/240418962/5-10-2019_1-46-47_PM.jpg` (12)은 입자 수, 그룹 수, 추적 시작·종료 시각을 보여주는 보고 화면이다(12–13). 그림 표시값은 `Number of Particles: 5`, `Number of Groups: 1`, `Start Particle Tracking: 0`, `Stop Particle Tracking: 1`이다(12 그림). |
| 15–25 | LPT / 전처리·이동 옵션·설정 폼 — 사용자는 초기 종자 배치(initial particle seeding), 계산 옵션과 플롯(plot)을 제어한다(15). 사용자는 트랙(track)을 화면 또는 AVI로 애니메이션(animation)하고 일부 또는 모든 트랙을 ASCII로 내보낼 수 있다(15). 주요 옵션은 완전한 3차원 이동, 사용자 지정 깊이 고정, 앞의 두 옵션에 임의 보행(random walk) 성분을 추가하는 것이다(17–19). 원문: `- Particles are free to move in full 3D,` (17); `- Particles can be fixed at a user-specified depth, and` (18); `- A random walk component can be added to the two options above.` (19). 문서는 `Model Control`의 `LPT` 탭에서 `RMC`로 옵션 폼을 연다고 적는다(21). 원문: `To set the values related to the drifters, the user should RMC on the *LPT* tab in the *Model Control* form to open LPT Options form, as shown in [Lagrangian Particle Tracking#Figure 2](#Figure2). This displays the various options for setting the drifters as described in detail in the following sections` (21). 직접 연 로컬 그림 `attachments/240418962/5-10-2019_1-42-18_PM.jpg` (23)은 LPT 항목에서 옵션 폼으로 향하는 빨간 화살표와 주 옵션 탭을 보여준다(23–24). 그림의 설정 영역 이름은 `LPT Computational Method & Timing`, `Vertical Movement Option`, `Initial Particle Vertical Position Input Option`, `Random Walk Options`, `Source of Diffusion Coefficients for LPT Computations`, `Wall Slippage`이다(23 그림). 그림 표시값은 `Julian day to turn ON particle tracking: 0`, `Julian day to turn OFF particle tracking: 1`, `Output Freq (min): 1`, `Horizontal (m²/s): 0.0001`, `Vertical (m²/s): 0.0001`, `Slip Factor: 0`이다(23 그림). 그림에서 `Compute Drifters`, `Fully 3D Lagrangian Neutrally Buoyant Particles`, `Allow Water Depth Particle Adjustment`, `Depth is Specified`, `User Specified Constant Diffusivities`가 선택되어 있다(23 그림). `Add Random Walk Component to Particle Movements`는 선택되어 있지 않다(23 그림). |
| 26–29 | LPT / 수치해법 — 수치해는 이류 수송(advective transport)과 임의 성분으로 나뉜다(26). 사용자는 수평 또는 수직 방향의 임의 성분을 켜거나 이류 수송만 남길 수 있다(26). 원문: `Note that the numerical solution is separately divided into the advective transport and random components. This approach allows the user to enable (i.e., turn on random walk) or disable (advective transport only) the random components for either the horizontal and/or the vertical directions.` (26). 미분방정식 해법은 Runge-Kutta 4이고 근사 표기는 `O(∆t4)`이다(28). 문서는 정확도 때문에 이 방법을 선호하고 전체 실행 시간에서 계산 부담이 다른 시험 방법에 비해 크지 않다고 적는다(28). 원문: `The method used to solve the differential equations is the Runge-Kutta 4 method: This method has the approximation of O(∆t4). It has been determined that the Runge-Kutta 4 method is preferred due to its higher level of numerical accuracy. It has been shown that the computational burden of the Runge-Kutta 4 method is not significant within the overall model run times compared to other methods tested.` (28).  |
| 30–38 | LPT / 관련 페이지 링크 — 문서는 설정·보기를 소개하는 문장에서 `LTP`를 쓴다(30). 링크는 `LPT Main Options Tab`, `Seeding Utility: By Group Tab`, `Oil Spill Modeling with LPT`, `View LPT in 2DH View`이다(32·34·36·38). 빈 줄을 포함한다(31·33·35·37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·21행: 이 파일에는 `LMC`와 `RMC`의 정의가 없다.
- 21행: 로컬 Markdown 안에는 링크 대상 `#Figure2`에 대응하는 명시적 앵커나 제목이 없다. 그림 2의 캡션은 일반 굵은 글씨이다(24).
- 28행: 근사 표기는 `O(∆t4)`이다. 원문은 4를 상첨자나 LaTeX 지수로 표시하지 않는다.
- 30행: 링크 소개 문장의 표기는 `LTP`이다. 앞의 본문은 `LPT`를 쓴다(10·15·21).
