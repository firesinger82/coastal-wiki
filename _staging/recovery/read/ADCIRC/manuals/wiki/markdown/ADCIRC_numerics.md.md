---
file: models/ADCIRC/raw/manuals/wiki/markdown/ADCIRC_numerics.md
lines: 11
sha256: 5cfa48941347fc6f5767607c63c826cd70351918253cb90095f3438dc91c5bde
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ADCIRC_numerics.md — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 제목·판본 표기·빈 줄을 포함한다(1–4). ADCIRC numerics — 2차원·3차원 수치 정식화가 다름을 설명하고 ADCIRC Theory Report를 연결한다(5). 공간 유한요소법(finite element method)·시간 유한차분법(finite difference method), 반암시적 및 집중 명시적 해법의 속도·정확도·안정성 차이, 시간 가중치와 Jacobi 질량행렬 해법을 설명한다(5). 원문: `ADCIRC is both a 2-dimensional (2D) and 3D model, and the numerical formulations of these are somewhat different. The best documentation of the base model numerics for both is currently in the [ADCIRC Theory Report](https://adcirc.org/files/2018/11/adcirc_theory_2004_12_08.pdf). ADCIRC is finite element in space and finite difference in time. Solution can be carried out either semi-implicitly or in [lumped explicit](/IM) mode, with the latter being faster but somewhat less accurate and less stable. If not operating in lumped explicit mode, time weights at t-1, t, and t+1 can be specified in the user in the [fort.15 file](/Fort.15_file), and a Jacobi solver is used to solve the mass matrix. ` (5). |
| 7–10 | 2D ADCIRC Numerics — 연속·수평 운동량 천수방정식(shallow water equations)을 사용한다(9). 원시 Galerkin 유한요소 정식화의 가짜 진동(spurious oscillation)을 처리하기 위해 일반화 파동 연속방정식(Generalized Wave Continuity Equation, GWCE)을 사용한다고 설명한다(9). |
| 11–11 | 3D ADCIRC Numerics — 절 제목만 있고 본문은 없다(11). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11: `3D ADCIRC Numerics`는 제목만 있으며 본문이 없다.
