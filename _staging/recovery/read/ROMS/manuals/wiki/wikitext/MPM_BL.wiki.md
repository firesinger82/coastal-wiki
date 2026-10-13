---
file: models/ROMS/raw/manuals/wiki/wikitext/MPM_BL.wiki
lines: 19
sha256: 04176df73fe072e6fcbbfaedacd678b475e02bab8bd53a3f4fce4cb026f643ed
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# MPM_BL.wiki — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Meyer-Peter Müeller Bedload Formulation — Meyer-Peter Müeller (1948)의 소류사(bedload) 공식을 제시한다(1–5). 최대 연산(max), 계수와 지수를 포함한 무차원 수송률식을 그대로 옮긴다(5). 수식 원문: `\Phi  = \max \left[ {8\left( {\theta _{sf}  - \theta _c } \right)^{1.5} ,\quad 0} \right]` (5). |
| 7–14 | Shields 매개변수(Shields parameter)와 저면 응력(bottom stress) — Φ는 퇴적물 등급(sediment class)별 무차원 수송률의 크기이다(7). θ_sf는 표피 응력(skin stress)의 무차원 Shields 매개변수이며 정의식을 제시한다(7–9). 임계 Shields 값과 총 표피 마찰(skin-friction) 성분의 크기 식을 원문 그대로 옮긴다(11–13). 수식 원문: `\Phi` (7); `\theta _{sf}` (7); `\theta _{sf}  = \frac{{\tau _{sf} }}{{\left( {s - 1} \right)gD_{50} }}` (9); `\theta _c  = 0.047` (11); `\tau _{sf}` (11); `\tau _{sf}  = \left( {\tau _{bx}^2  + \tau _{by}^2 } \right)^{0.5}` (13). |
| 15–19 | 벡터 분할 — 저면 응력의 표피 마찰 성분은 흐름만의 응력 또는 파랑·흐름 결합 응력(wave-current combined stress)의 최댓값이라고 설명한다(15). 셀 면(cell faces)의 u·v 위치에서 계산하고 셀 중심(cell centers)의 ρ 지점으로 보간한다(15). 소류사 수송 벡터를 x·y 성분으로 나누는 식을 원문 그대로 옮긴다(17–19). 수식 원문: `{\tau _{bx}}^2` (15); `{\tau _{bx}}^2` (15); `x` (15); `y` (15); `u` (15); `v` (15); `\rho` (15); `x` (15); `y` (15); `q_{blx}  = q_{bl} \frac{{\tau _{bx} }}` (17); `{{\tau _{sf} }};\quad \quad q_{bly}  = q_{bl} \frac{{\tau _{by} }}` (18); `{{\tau _{sf} }}` (19). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13·15행: 저면 응력(bottom stress) 크기 식은 x·y 성분을 사용한다. 뒤 설명의 두 성분 기호는 둘 다 `{\tau _{bx}}^2`로 적혀 있다(15).
- 9·17–19행: 식에 쓰인 s, g, D50 및 q_bl의 별도 정의는 이 파일에 없다. Φ는 무차원 수송률 크기라고 설명한다(7).
