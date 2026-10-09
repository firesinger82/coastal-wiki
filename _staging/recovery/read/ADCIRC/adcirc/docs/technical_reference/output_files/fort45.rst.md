---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort45.rst
lines: 35
sha256: f176a0d803a95c5d5d161155f1b53ce7eda9a32f1d84863095a230ec28a29edc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort45.rst — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.45: 3D Velocity at All Nodes — fort.15에 따른 전체 격자 절점의 3차원 속도(3D velocity) 시계열(time series) 출력이다(1–4). 원문: ``This file contains velocity time series output at all nodes in the model grid as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.`` (4). |
| 6–24 | File Structure — ASCII 파일 구조를 제시한다(9–23). 자료 집합(data set)마다 TIME·IT와 SIGMA 좌표를 기록한다(17–18). NP 절점별 수직 층 기록은 REAL(Q(j,M)), AIMAG(Q(j,M)), WZ(j,M)이다(20–23). 원문: `The file is written in ASCII format. The basic structure is shown below:` (9); `.. parsed-literal::` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NDSET3DGV <NDSET3DGV>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPO3DGV <NSPO3DGV>`, :ref:`NSPO3DGV <NSPO3DGV>`, :ref:`NFEN <NFEN>`, :ref:`IRTYPE <IRTYPE>` `` (15); ``     for k=1, :ref:`NDSET3DGV <NDSET3DGV>` `` (17); ``         :ref:`TIME <TIME>`, :ref:`IT <IT>`, (:ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, N=1, :ref:`NFEN <NFEN>`-1), :ref:`SIGMA(NFEN) <SIGMA>`, :ref:`SIGMA(NFEN) <SIGMA>` `` (18); ``         for j=1, :ref:`NP <NP>` `` (20); ``            j, (:ref:`REAL(Q(j,M)) <REAL(Q(j,M))>`, :ref:`AIMAG(Q(j,M)) <AIMAG(Q(j,M))>`, :ref:`WZ(j,M) <WZ(j,M)>`, M=1, :ref:`NFEN <NFEN>`)`` (21); `        end j loop` (22); `    end k loop` (23). |
| 25–35 | Notes — ASCII 형식만 제공한다(28). Q의 실수부와 허수부는 각각 x방향과 y방향 속도이다(30–32). WZ는 수직 속도 성분이다(33). SIGMA 값이 수직 층을 정의한다(34). fort.42와 유사하나 특정 관측점 대신 전체 영역을 기록한다고 적는다(35). 원문: `* Output is only available in ASCII format` (28); `* Time series data is recorded at all nodes in the model grid` (29); `* Velocity components are stored as:` (30); `    * REAL(Q): x-component of velocity` (31); `    * AIMAG(Q): y-component of velocity` (32); `    * WZ: vertical velocity component` (33); `* Data is recorded at multiple vertical levels defined by SIGMA values` (34); `* Similar to fort.42 but provides data for the entire model domain instead of specific stations ` (35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
