---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Introduction.md
lines: 14
sha256: b5bf3ec321fe73ff18ec1745c1bf79e150a24f805fc0022bdf11f5bd10c0e828
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Introduction.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Introduction / 문서 메타데이터 — 페이지 ID `2818253`, 제목, space, 원문 URL, 버전 `3`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–11 | Introduction / 프로그램 대상 — DSI가 개발한 2차원 격자 생성 소프트웨어이며 곡선 직교 모형(curvilinear orthogonal model)에 사용한다고 적는다(10). 대상 모형은 원문 표기로 `EFDC\_DSI`, `EFDC\_SGZ`, `EFDC\_EPA`, `EFDC\_Hydro`다(10). 이 도구는 `EFDC\_DSI/EFDC+ Explorer Modeling System`에 추가 최적화되었다고 적는다(10). 대상·적용 조건 원문: `CVLGrid is 2-D grid generation software developed by Dynamic Solutions International, LLC for use with curvilinear orthogonal models, and in particular for use with EFDC\_DSI, EFDC\_SGZ, EFDC\_EPA, and EFDC\_Hydro models. As all EFDC models require 2D curvilinear orthogonal grids this tool has been developed to meet this need for DSI and our clients and customers. This tool has been further optimized for us with the EFDC\_DSI/EFDC+ Explorer Modeling System.` (10). |
| 12–13 | Introduction / 격자와 직교 편차 — Navier–Stokes 방정식(Navier-Stokes equations)의 수치 모형에서 격자가 핵심 요소라고 적는다(12). Laplace 방정식(Laplace equations)을 사용해 곡선 격자(curvilinear grid)를 생성하며 표준 직사각형 격자보다 정확한 계산을 가능하게 한다고 주장한다(12). 최적 정확도를 위해 영역 형상을 따르고 직교성(orthogonality)을 유지해야 한다고 적는다(12). 평균 직교 편차(average orthogonal deviation)는 원문 기준 `less than 3o`여야 한다고 적는다(12). 기준값·조건 원문: `Grids are a key component when generating models using Navier-Stokes equations with the numerical method. This software uses Laplace equations to generate curvilinear grids that allow for more accurate modeling calculations than a standard rectangular grid. In order to achieve optimal accuracy of a model, the grid should be shaped to the model domain and maintain orthogonality. The average orthogonal deviation for grid computation should be less than 3o to maintain the accuracy of the numerical model.` (12). 각도 표기 `3o`를 원문 그대로 유지한다(12). |
| 14–14 | Introduction / SOR와 최적 완화 계수 — 연속 과완화법(Successive Over-Relaxations, SOR)으로 Laplace 방정식을 푼다고 적는다(14). 계산 효율과 반복 수 감소를 위해 최적 완화 계수(optimum relaxation factor)를 정해 SOR 식에 사용해야 한다고 적는다(14). CVLGrid가 현재 격자의 최적 계수를 자동 계산·적용한다고 적는다(14). 매개변수·조건 원문: `This program uses the method of Successive Over-Relaxations (SOR) to solve the Laplace equations. To maximize calculation efficiency and reduce the number of iterations required, an optimum relaxation factor ![](https://eemodelingsystem.atlassian.net/wiki/download/attachments/2818253/image2016-6-30%2010:17:57.png?version=1&modificationDate=1467281876272&cacheVersion=1&api=v2)must be determined and used in the SOR equations. CVLGrid automatically calculates and implements this optimum relaxation factor for the current grid.` (14). 직접 연 인라인 수식 그림 `attachments/2818253/image2016-6-30_101757.png`에는 괄호 안 소문자 오메가만 있으며 LaTeX 표기는 `(\omega)`다(14행 참조 그림). 계수의 수치 기본값·범위·단위와 SOR 방정식은 이 파일에 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
