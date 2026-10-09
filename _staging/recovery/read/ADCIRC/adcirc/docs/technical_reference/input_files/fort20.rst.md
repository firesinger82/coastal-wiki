---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort20.rst
lines: 51
sha256: ef9460eff0a078d43b43f093b44214e483ef77793e8f294175d95cb0450c1fe9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort20.rst — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.20: Non-periodic Normal Flow Boundary Condition File — 0이 아닌 법선 유량(normal flow) 지정 경계의 비주기 입력이며 IBTYPE과 NFFR의 읽기 조건을 제시한다(6). 원문: ``The fort.20 file contains non-periodic, normal flow boundary conditions for "specified non-zero normal flow" boundary nodes. This file is only read when a "specified non-zero normal flow" boundary condition has been specified in the :doc:`Grid and Boundary Information File <fort14>` (IBTYPE=2, 12, or 22) and NFFR=0 in the :doc:`Model Parameter and Periodic Boundary Condition File <fort15>`.`` (6). |
| 8–21 | File Structure — FTIMINC와 경계 절점별 QNIN 반복의 기본 형식이다(11–18). 위 블록을 모의 끝까지 각 시간 단계에 반복하라고 적는다(20). 원문: `.. parsed-literal::` (13); ``    :ref:`FTIMINC <FTIMINC>` `` (15); ``    for k=1 to :ref:`NFLBN <NFLBN>` `` (16); ``       :ref:`QNIN(k) <QNIN>` `` (17); `   end k loop` (18); `   Repeat the block above for each time step until the end of the simulation.` (20). |
| 22–29 | Notes — 처음 자료의 시각과 뒤 자료 간격 및 전체 실행을 덮는 자료 제공 의무를 명시한다(25–26). 경계 절점 순서는 fort.14 법선 유량 경계 순서와 같아야 한다(27). 단위 폭당 양의 유량은 영역 유입이며 음의 유량은 유출이다(28). 원문: `* The first set of normal flow values is provided at TIME=STATIM (as specified in fort.15). Additional sets of normal flow values are provided every FTIMINC.` (25); `* Enough sets of normal flow values must be provided to extend for the entire model run, otherwise the run will crash!` (26); `* The node order in this file must match the order specified in the normal flow boundary condition part of the Grid and Boundary Information File.` (27); `* A positive flow/unit width is into the domain and a negative flow/unit width is out of the domain.` (28). |
| 30–51 | Example — 법선 유량 경계 절점 두 개의 예시이며 간격 3600초와 세 시간 단계의 값을 제시한다(33–43). 첫 절점 유입은 시간에 따라 증가하고 둘째 절점 유출은 크기가 시간에 따라 증가한다고 적는다(47–51). 원문: `.. code-block:: none` (35); `   3600.0` (37); `   10.5` (38); `   -5.2` (39); `   12.0` (40); `   -6.3` (41); `   15.0` (42); `   -8.1` (43); `* A time increment (FTIMINC) of 3600.0 seconds (1 hour)` (47); `* Two normal flow boundary nodes (NFLBN=2)` (48); `* Three time steps of data, with:` (49); `   * Node 1: Flow into the domain (positive values) increasing over time` (50); `   * Node 2: Flow out of the domain (negative values) increasing in magnitude over time` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15–20·37–43행: 형식의 `Repeat the block above` 대상에는 FTIMINC가 포함되어 있으나 예시는 간격 값 `3600.0`을 처음에 한 번만 쓰고 유량 자료 세 집합을 이어서 제시한다.
