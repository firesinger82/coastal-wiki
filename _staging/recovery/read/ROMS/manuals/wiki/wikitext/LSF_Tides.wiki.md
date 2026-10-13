---
file: models/ROMS/raw/manuals/wiki/wikitext/LSF_Tides.wiki
lines: 93
sha256: 93043a35589040f40d955cfe89d554a56f4ef8c191f1f8f9f5dadd34470ac26a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# LSF_Tides.wiki — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Least Squares Fit for ROMS Tides — 상태변수(state variable)를 시간 평균(time mean)과 N개 조석 조화 성분(tidal harmonics)의 합으로 나타낸다(1–7). 제목과 빈 줄을 포함한다. 수식 원문: `\phi` (3); `\bar\phi` (3); `N` (3); `\omega_k` (3); `   \phi(t) = \bar\phi + \sum_{k=1}^N A_k \sin\omega_k t + \sum_{k=1}^N B_k \cos\omega_k t` (6). |
| 9–24 | 최소제곱(least squares) 오차 — 미지의 조석 진폭 및 상태 계수를 오차 최소화로 구한다(9). 연속 시간 적분의 오차함수(11–15)와 이산 공간(discrete space)의 오차함수(17–23)를 제시한다. 수식 원문: `A_k` (9); `B_k` (9); `\phi` (9); `   \varepsilon^2 = \frac{1}{T} \int_{t_1}^{t_2} \left[\phi - \left(\bar\phi` (12); `                   + \sum_{k=1}^N (A_k \sin\omega_k t)` (13); `                   + \sum_{k=1}^N (B_k \cos\omega_k t)\right)\right]^2dt` (14); `   \varepsilon^2 = \frac{1}{M} \sum_{i=1}^M \left[\phi_i - \left(\bar\phi` (20); `                   + \sum_{k=1}^N (A_k \sin\omega_k t_i)` (21); `                   + \sum_{k=1}^N (B_k \cos\omega_k t_i)\right)\right]^2` (22). |
| 25–43 | 추가 제약과 선형 방정식 — 평균, A 계수, B 계수에 대한 오차의 편미분을 0으로 놓는다(25). 그 결과로 세 선형식을 제시한다(27–42). 수식 원문: `\frac{\partial \varepsilon^2}{\partial \bar\phi} = 0` (25); `\frac{\partial \varepsilon^2}{\partial A_k} = 0` (25); `\frac{\partial \varepsilon^2}{\partial B_k} = 0` (25); `   \sum_{i=1}^M \left[-2\phi_i + 2\bar\phi + 2 \sum_{k=1}^N (A_k \sin\omega_k t_i)` (28); `                + 2 \sum_{k=1}^N (B_k \sin\omega_k t_i)\right] = 0` (29); `   \sum_{i=1}^M \Bigg[ -2 \phi_i \sin\omega_k t_i + 2 \bar\phi \sin\omega_k t_i` (33); `                + 2\sum_{p=1}^N (A_p \sin\omega_p t_i \sin\omega_k t_i)` (34); `                + 2\sum_{p=1}^N (B_p\cos\omega_p t_i \sin\omega_k t_i)\Bigg] = 0` (35); `   \sum_{i=1}^M \Bigg[ -2 \phi_i \cos\omega_k t_i + 2 \bar\phi \cos\omega_k t_i` (39); `                + 2\sum_{p=1}^N (A_p \sin\omega_p t_i \cos\omega_k t_i)` (40); `                + 2\sum_{p=1}^N (B_p\cos\omega_p t_i \cos\omega_k t_i) \Bigg] = 0` (41). |
| 44–93 | 행렬 표현(matrix form) — 모든 합 기호는 시간 평균 구간의 M개 시간 단계(time steps)에 대한 합이라고 설명한다(44). 행렬, 평균과 A·B 계수 벡터, 관측값과 삼각함수의 곱을 합한 우변 벡터를 제시한다(46–93). 행렬 예시는 7까지의 조화 성분 첨자를 사용한다(60–89). 원문: `in matrix form (<math>N</math> harmonics). Note: all instances of <math>\sum</math> are actually <math>\sum_{i=1}^M</math> where <math>M</math> is the number of time-steps in the time-averaging window.` (44). 수식 원문: `N` (44); `\sum` (44); `\sum_{i=1}^M` (44); `M` (44); `\begin{matrix}` (46); `\begin{bmatrix}` (47); `\\` (48); `M & \sum \sin\omega_1 t_i & \sum \sin\omega_2 t_i` (49); `& \cdots & \sum \cos\omega_1 t_i & \cdots \\` (50); `\\` (51); `\sum \sin\omega_1 t_i & \sum \sin^2 \omega_1 t_i & \sum \sin\omega_2 t_i \sin\omega_1 t_i` (52); `& \cdots & \sum \cos\omega_1 t_i \sin\omega_1 t_i & \cdots \\` (53); `\\` (54); `\sum \sin\omega_2 t_i & \sum \sin\omega_1 t_i \sin\omega_2 t_i & \sum \sin^2 \omega_2 t_i` (55); `& \cdots & \sum \cos\omega_1 t_i \sin\omega_2 t_i & \cdots \\` (56); `\\` (57); `\vdots & \vdots & \cdots & \cdots & \cdots & \cdots \\` (58); `\\` (59); `\sum \sin\omega_7 t_i & \sum \sin\omega_1 t_i \sin\omega_7 t_i & \sum \sin\omega_2 t_i \sin\omega_7 t_i` (60); `& \cdots & \sum \cos\omega_1 t_i \sin\omega_7 t_i & \cdots \\` (61); `\\` (62); `\sum \sin\omega_1 t_i & \sum \sin\omega_1 t_i \cos\omega_1 t_i & \sum \sin\omega_2 t_i \cos\omega_1 t_i` (63); `& \cdots & \sum \cos^2 \omega_1 t_i & \cdots \\` (64); `\\` (65); `\sum \cos\omega_2 t_i & \sum \sin\omega_1 t_i \cos\omega_2 t_i & \sum \sin\omega_2 t_i \cos\omega_2 t_i` (66); `& \cdots & \sum \cos\omega_1 t_i \cos\omega_2 t_i & \cdots \\` (67); `\\` (68); `\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\` (69); `\\` (70); `\sum \cos\omega_7 t_i & \sum \sin\omega_1 t_i \cos\omega_7 t_i & \sum \sin\omega_2 t_2 \cos\omega_7 t_i` (71); `& \cdots & \sum \cos\omega_1 t_i \cos\omega_7 t_i & \cdots \\ \\ \end{bmatrix}` (72); `\;\;&` (73); `\begin{bmatrix}` (74); `\\` (75); `\bar\phi \\ \\ A_1 \\ \\ A_2 \\ \\ \vdots \\ \\ A_7 \\ \\ B_1 \\ \\ B_2 \\ \\ \vdots \\ \\ B_7 \\ \\` (76); `\end{bmatrix}` (77); `& = &` (78); `\begin{bmatrix}` (79); `\\` (80); `\sum\phi_i \\ \\` (81); `\sum\phi_i \sin\omega_1 ti \\ \\` (82); `\sum\phi_i \sin\omega_2 ti \\ \\` (83); `\vdots \\ \\` (84); `\sum\phi_i \sin\omega_7 ti \\ \\` (85); `\sum\phi_i \cos\omega_1 ti \\ \\` (86); `\sum\phi_i \cos\omega_2 ti \\ \\` (87); `\vdots \\ \\` (88); `\sum\phi_i \cos\omega_7 ti \\ \\` (89); `\end{bmatrix}` (90); `\\` (91); `A & x & & b` (92); `\end{matrix}` (93). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 6·14·22·29행: 상태 표현과 두 오차함수의 B 계수 항은 코사인을 사용하지만, 평균에 대한 첫 선형식의 B 계수 항은 `B_k \sin\omega_k t_i`로 적혀 있다(29).
- 44·60·71·76행: 설명은 N개 조화 성분을 말하고, 행렬과 계수 벡터의 끝 첨자는 7로 적혀 있다.
- 63행: 코사인 계수 행의 첫 항은 `\sum \sin\omega_1 t_i`로 적혀 있다. 같은 행의 뒤 항들은 `\cos\omega_1 t_i`를 포함한다.
- 71행: 같은 행의 다른 시간 첨자는 `t_i`지만, 세 번째 열의 한 항은 `\sin\omega_2 t_2`로 적혀 있다.
- 82–89행: 우변 벡터의 삼각함수 시간 표기는 `ti`이고, 앞 행렬은 `t_i`를 사용한다.
- 12·20·44행: 연속 적분의 T와 이산 합의 M을 사용하지만, T의 정의는 이 파일에 없다. M의 정의는 44행에 있다.
