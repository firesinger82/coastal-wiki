---
file: models/ROMS/raw/manuals/wiki/wikitext/Curvilinear_Coordinates.wiki
lines: 37
sha256: 346c5851a0f344158c040084335dae099757489d47cd05ecbbaf5da5497a838e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Curvilinear_Coordinates.wiki — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Curvilinear Coordinates / 좌표·길이 — 충분히 매끄러운 영역에서 수평 직교좌표 변환(orthogonal coordinate transformation)으로 경계추종(boundary-following)과 가변 해상도(variable resolution)를 구현한다(3–4). ξ·η와 물리 호 길이(arc length)의 관계, 계량 축척계수(scale factors) m·n을 정의하며 수식은 원문 그대로 옮긴다(4–10). 원문: ` smooth domains) by introducing an appropriate orthogonal coordinate transformation in the horizontal.  Let the new coordinates be <math>\xi(x,y)</math> and <math>\eta(x,y)</math> where the relationship of horizontal arc length to the differential distance is given by: ` (4); ` <math display="block">(ds)_{\xi} = \left( {1 \over m} \right) d \xi</math> ` (6); ` <math display="block">(ds)_{\eta} = \left( {1 \over n} \right) d \eta</math> ` (8); ` Here, <math>m(\xi,\eta)</math> and <math>n(\xi,\eta)</math> are the scale factors which relate the differential distances <math>(\Delta \xi,\Delta \eta)</math> to the actual (physical) arc lengths. ` (10). LaTeX 원문: ` \xi(x,y) ` (4); ` \eta(x,y) ` (4); ` (ds)_{\xi} = \left( {1 \over m} \right) d \xi ` (6); ` (ds)_{\eta} = \left( {1 \over n} \right) d \eta ` (8); ` m(\xi,\eta) ` (10); ` n(\xi,\eta) ` (10); ` (\Delta \xi,\Delta \eta) ` (10). |
| 12–17 | Vector notation / gradient — Batchelor Appendix 2 참조와 스칼라(scalar) φ의 곡선좌표 경사(gradient) 벡터식이다(12–16). 원문: ` <math display="block">\nabla \phi = \hat{\xi} m {\partial \phi \over \partial \xi} + ` (15); `        \hat{\eta} n {\partial \phi \over \partial \eta}</math> ` (16). LaTeX 원문: ` \nabla \phi = \hat{\xi} m {\partial \phi \over \partial \xi} + ` (15); `        \hat{\eta} n {\partial \phi \over \partial \eta} ` (16). |
| 18–22 | Vector notation / divergence — 벡터(vector) a의 곡선좌표 발산(divergence) 식을 원문 그대로 옮긴다(18–21). 원문: ` <math display="block">\nabla \cdot \vec{a} = mn \left[ ` (18); `    {\partial \over \partial \xi} \!\! \left( {a \over n} \right) + ` (19); `    {\partial \over \partial \eta} \!\! \left( {b \over m} \right) ` (20); `    \right]</math> ` (21). LaTeX 원문: ` \nabla \cdot \vec{a} = mn \left[ ` (18); `    {\partial \over \partial \xi} \!\! \left( {a \over n} \right) + ` (19); `    {\partial \over \partial \eta} \!\! \left( {b \over m} \right) ` (20); `    \right] ` (21). |
| 23–30 | Vector notation / curl — 곡선좌표 회전(curl)의 행렬식(determinant), 기저·미분·성분 행을 원문 그대로 옮긴다(23–29). 원문: ` <math display="block">\nabla \times \vec{a} = mn \left\| \begin{matrix} ` (23); `    {\hat{\xi}_1 \over m} & {\hat{\xi}_2 \over n} & \hat{k} \\ ` (24); `    {\partial \over \partial \xi} & ` (25); `    {\partial \over \partial \eta} & ` (26); `    {\partial \over \partial z} \\ ` (27); `    {a \over m} & {b \over n} & c ` (28); `    \end{matrix} \right\|</math> ` (29). LaTeX 원문: ` \nabla \times \vec{a} = mn \left\| \begin{matrix} ` (23); `    {\hat{\xi}_1 \over m} & {\hat{\xi}_2 \over n} & \hat{k} \\ ` (24); `    {\partial \over \partial \xi} & ` (25); `    {\partial \over \partial \eta} & ` (26); `    {\partial \over \partial z} \\ ` (27); `    {a \over m} & {b \over n} & c ` (28); `    \end{matrix} \right\| ` (29). |
| 31–37 | Vector notation / Laplacian·기호 — 스칼라 라플라시안(Laplacian)을 발산과 경사의 합성으로 표현한다(31–35). φ는 스칼라이고 벡터 a의 성분은 a·b·c라고 정의한다(37). 원문: ` <math display="block">\nabla^2 \phi = \nabla \cdot \nabla \phi = mn \left[  ` (31); `    {\partial \over \partial \xi} \!\! \left( {m \over n}  ` (32); `    {\partial \phi \over \partial \xi} \right) + ` (33); `    {\partial \over \partial \eta} \!\! \left( {n \over m}  ` (34); `    {\partial \phi \over \partial \eta} \right) \right]</math> ` (35); ` where <math>\phi</math> is a scalar and <math>\vec{a}</math> is a vector with components <math>a</math>, <math>b</math>, and <math>c</math>. ` (37). LaTeX 원문: ` \nabla^2 \phi = \nabla \cdot \nabla \phi = mn \left[  ` (31); `    {\partial \over \partial \xi} \!\! \left( {m \over n}  ` (32); `    {\partial \phi \over \partial \xi} \right) + ` (33); `    {\partial \over \partial \eta} \!\! \left( {n \over m}  ` (34); `    {\partial \phi \over \partial \eta} \right) \right] ` (35); ` \phi ` (37); ` \vec{a} ` (37); ` a ` (37); ` b ` (37); ` c ` (37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 24행: 회전식의 첫 행에서 기저 기호를 `\hat{\xi}_1`, `\hat{\xi}_2`로 적는다. 15–16행 경사식은 `\hat{\xi}`, `\hat{\eta}`를 쓴다. 전자의 첨자 정의는 이 파일에 없다.
