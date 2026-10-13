---
file: models/ROMS/raw/manuals/wiki/wikitext/RPM2.wiki
lines: 17
sha256: 534f1fb2b234b179236f6f8982796093ec772bd260305617b592a9243646243e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# RPM2.wiki — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Ripple Predictor Mark 2 — RPM2에서 Soulsby와 Whitehouse(2005)의 시간 의존 연흔(ripple) 형상을 구현한다고 적는다(1–3). 연흔 높이·파장·방향과 높이·파장의 m 단위, y축에서 시계방향을 양으로 하는 방향을 정의한다(5). 일방향 흐름에서는 흐름 방향, 순수 파랑에서는 전파 방향이며 선형 연흔 방향은 마루에 수직이라고 적는다(5). 방향은 x·y 성분으로 저장한다(5). 원문: `Time-dependent ripple geometry is implemented in subroutine RPM2 using the approach described in [[Bibliography#SoulsbyR2005a \| Soulsby and Whitehouse (2005)]]. Presently, this routine is in the version of SSW_BBL.h located in [https://www.myroms.org/projects/cstm/browser/branches/crs/cstm_trunk Sherwood's branch].` (3); `Ripple geometry is described by ripple height <math>\eta</math> (m), wavelength <math>\lambda</math> (m), and orientation <math>\theta</math> (positive clockwise from the <math>y</math>-axis). The orientation is defined as follows. Under unidirectional flow (no waves), ripple orientation is the same as the current direction. Under pure waves, ripple orientation is in the direction of wave propagation. For linear ripples (assumed here), ripple orientation is perpendicular to the ripple crest. In a slight modification of the original algorithm, the ripple orientation is actually stored as <math>x</math>- and <math>y</math>- components <math>\theta_x</math> and <math>\theta_y</math>.` (5); `\eta` (5); `\lambda` (5); `\theta` (5); `y` (5); `x` (5); `y` (5); `\theta_x` (5); `\theta_y` (5). |
| 7–17 | 평형 형상으로의 갱신 — 현재 조건의 평형 연흔을 계산하고 퇴적물 수송 조건에 따른 속도로 기존 형상을 평형에 접근시킨다(7). 수송 임계값을 넘지 않으면 연흔은 변하지 않는다고 적는다(7). 높이 갱신식과 기호 정의를 제시하며 파장·방향 성분에도 유사식을 사용한다(9–12). 파랑만의 Shields 매개변수(Shields parameter)와 흐름만의 값 중 큰 값으로 평형 형상·변화율을 정한다(14). 결합 파류 응력에 따른 wash-out 기준과 변화율은 가능한 수정안으로 적는다(17). 원문: `The [[Bibliography#SoulsbyR2005a \| Soulsby and Whitehouse (2005)]] approach is to calculate equilibrium ripple geometry under existing conditions, and then nudge the existing ripple geometry toward equilibrium at a rate that depends on sediment-transport conditions. Ripples remain unchanged if the transport threshold is not exceeded. The formula for updating ripple height is as follows.` (7); `where <math>\eta_t</math> is the ripple height to be calculated for the present time, <math>\eta_{t-1}</math> is ripple height at the previous step,` (11); `<math>\eta_{eq}</math> is the equilibrium ripple height under present conditions, <math>\beta</math> is the evolution rate of ripple height under present conditions, <math>T_{e}</math> is the time scale for ripple evolution, and <math>\Delta t</math> is the time step. Similar equations are used to nudge <math>\lambda</math> and components of ripple direction <math>\theta_x</math> and <math>\theta_y</math> toward the equilibrium associated with present sediment-transport conditions.` (12); `The Shields parameters for waves alone and for currents alone are calculated, and the equilibrium geometry and evolution rate is determined by the larger of the two.` (14); `One potential modification to this routine might be to calculate wash-out criteria and evolution rates based on the combined wave-current stress.` (17); `\eta _{t}  = \eta _{t-1}  + (\eta _{eq}  - \eta _{t-1} )(1 - \exp ( -\frac{\beta}{T_e} \Delta t) )` (9); `\eta_t` (11); `\eta_{t-1}` (11); `\eta_{eq}` (12); `\beta` (12); `T_{e}` (12); `\Delta t` (12); `\lambda` (12); `\theta_x` (12); `\theta_y` (12). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
