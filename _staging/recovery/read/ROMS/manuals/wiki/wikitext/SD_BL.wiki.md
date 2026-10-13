---
file: models/ROMS/raw/manuals/wiki/wikitext/SD_BL.wiki
lines: 30
sha256: 0092cb7c04ff6ac4c21544a2bb3af1b053d2ef8e6c73a46613eaed5532cac1ea
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# SD_BL.wiki — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Soulsby & Damgaard Bedload Formulation — 평균 흐름과 비대칭 파랑의 결합 효과를 소류사(bedload) 플럭스에 반영하며 파 주기 동안 무차원 수송식을 수치 적분한다고 적는다(1–3). 수송·Shields 매개변수(Shields parameter) 벡터의 흐름 평행·수직 성분과 임계값, 반경험 계수를 정의한다(5–9). 원문: `<math>{\overrightarrow {\theta _{sf} }}=\left( {\theta _{sf\parallel}  ,\,\theta _{sf\bot}  } \right)</math>, <math>\theta _{sf}  = \left\| {\overrightarrow {\theta _{sf} } } \right\|</math>, <math>\theta_c</math> is the critical Shields parameter, and <math>A2 = 12</math> is a semi-empirical coefficient. The implementation of this method requires computation of transport rates in the directions parallel and perpendicular to the currents as:` (9); `\overrightarrow \Phi   = \max \left[ {A_2 \theta ^{0.5} \left( {\theta _{sf}  - \theta _c } \right)\frac{{\overrightarrow {\theta _{sf} } }}` (5); `{{\theta _{sf} }},\quad 0} \right]` (6); `\overrightarrow \Phi` (8); `\overrightarrow {\theta _{sf} }` (8); `\overrightarrow \Phi   = \left( {\Phi _\parallel  ,\,\Phi _ \bot  } \right)` (8); `{\overrightarrow {\theta _{sf} }}=\left( {\theta _{sf\parallel}  ,\,\theta _{sf\bot}  } \right)` (9); `\theta _{sf}  = \left\| {\overrightarrow {\theta _{sf} } } \right\|` (9); `\theta_c` (9); `A2 = 12` (9). |
| 11–24 | 평행·수직 수송률 — 흐름에 평행한 두 후보 중 최댓값, 각 후보의 식과 흐름에 수직인 수송식을 제시한다(11–23). 원문: `\Phi _\parallel   = \max \left[ {\Phi _{\parallel 1} ,\quad \Phi _{\parallel 2} } \right]` (11); `\Phi _{\parallel 1}  = A_2 \theta _m^{0.5} \left( {\theta _m  - \theta _c } \right)` (15); `\Phi _{\parallel 2}  = A_2 \left( {0.9534 + 0.1907\cos 2\varphi } \right)\theta _w^{0.5} \theta _m  + A_2 \left( {0.229\gamma _w \theta _w^{1.5} \cos \varphi } \right)` (18); `\Phi _ \bot   = A_2 \frac{{0.1907\theta _w^2 }}` (21); `{{\theta _w^{3/2}  + 1.5\theta _m^{1.5} }}\left( {\theta _m \sin 2\varphi  + 1.2\gamma _w \theta _w \sin \varphi } \right)` (22). |
| 25–30 | 평균 응력·비대칭 계수 — 평균 Shields 매개변수와 평균 응력식, 흐름만·파랑만의 저면 응력(bottom stress)을 설명한다(25–30). 비대칭 계수는 진동 파 응력의 제2 조화 진폭 대 제1 조화 진폭 비이며 Stokes 2차 이론으로 추정하고 0.2보다 작게 제한한다고 적는다(30). 플럭스를 x·y로 회전하고 입도별 유량으로 차원화한다고 설명한다(30). 원문: `and <math>\tau_c</math> is the bottom stress from the currents only, <math>\tau_w</math> is the bottom stress from the waves only calculated in the bottom-boundary layer routines (see below). The asymmetry factor <math>\gamma _w</math> is the ratio between the amplitude of the second harmonic and the amplitude of the first harmonic of the oscillatory wave stress. Following the suggestion of Soulsby and Damgaard (2005), we estimate the asymmetry factor using Stokes second-order theory (e.g., Fredsøe and Deigaard, 1992) and constrain it to be less than 0.2. The non-dimensional fluxes (Eqns. (30) and (33)) are rotated into <math>x</math> and <math>y</math> directions using the directions for mean current and waves and dimensionalized with Eqn. (24) to yield values for <math>q_{blx}</math> and <math>q_{bly}</math> for each sediment class.` (30); `\theta _m` (25); `\tau_m` (25); `\tau _m  = \tau _c \left( {1 + 1.2\left( {\frac{{\tau _w }}` (27); `{{\tau _w  + \tau _c }}} \right)^{1.5} } \right)` (28); `\tau_c` (30); `\tau_w` (30); `\gamma _w` (30); `x` (30); `y` (30); `q_{blx}` (30); `q_{bly}` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·18·21–22행: 수송식의 `\theta`, `\theta _w`, `\varphi`는 이 파일에 별도 정의가 없다.
- 30행: `Eqns. (30) and (33)`과 `Eqn. (24)`를 참조하지만 이 파일의 식에는 해당 번호가 없다.
