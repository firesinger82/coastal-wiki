---
file: models/ROMS/raw/manuals/wiki/wikitext/Eigenproblem_Parameters.wiki
lines: 7
sha256: 5454f7425c0b81db30c0873ec71838db2ee324318954c8f6b7805f364c481930
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Eigenproblem_Parameters.wiki — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Eigenproblem Parameters — 고유치문제(eigenproblem) 제목, Variables의 NEV·NCV 절 포함 지시문과 빈 줄이다(1–6). 포함될 정의는 이 파일에 없다(2·4). 원문: ` {{#lst:Variables\|NEV}} ` (2); ` {{#lst:Variables\|NCV}} ` (4). |
| 7–7 | NCV·NEV 선택 — 선행 분석(a-priori analysis)이 없다는 불확실성을 보존한다(7). 유일한 형식 요구, 최적 교란(optimal perturbations) 권고, 유한시간 고유모드(finite time eigenmodes, FTE)·수반 고유모드(adjoint finite time eigenmodes, AFTE)의 요구와 NEV 크기에 따른 효율·시작값 조건을 모두 원문 그대로 옮긴다(7). 원문: ` '''Notice:''' At present, there is no a-priori analysis to guide the selection of <span class="twilightBlue">NCV</span> relative to <span class="twilightBlue">NEV</span>.  The only formal requirement is that <span class="twilightBlue">NCV > NEV</span>. However in optimal perturbations, it is recommended to have <span class="twilightBlue">NCV &ge; 2*NEV</span>. In Finite Time Eigenmodes (FTE) and Adjoint Finite Time Eigenmodes (AFTE) the requirement is to have <span class="twilightBlue">NCV &ge; 2*NEV+1</span>. The efficiency of calculations depends critically on the combination of <span class="twilightBlue">NEV</span> and <span class="twilightBlue">NCV</span>.  If <span class="twilightBlue">NEV</span> is large (greater than 10 say), you can use <span class="twilightBlue">NCV=2*NEV+1</span> but for <span class="twilightBlue">NEV</span> small (less than 6) it will be inefficient to use <span class="twilightBlue">NCV=2*NEV+1</span>. In complicated applications, you can start with <span class="twilightBlue">NEV=2</span> and <span class="twilightBlue">NCV=10</span>. Otherwise, it will iterate for very long time. ` (7). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 2·4행: NEV·NCV 정의는 외부 Variables 절 포함 지시문으로만 제공된다. 해당 정의 본문은 이 파일에 없다.
