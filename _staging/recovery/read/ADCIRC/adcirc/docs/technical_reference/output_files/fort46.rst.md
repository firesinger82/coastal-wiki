---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort46.rst
lines: 37
sha256: 5841e3003f3c2b099ec3a108b302be95f45fb7e933d111902df24b49960e1139
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort46.rst — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.46: 3D Turbulence at All Nodes — fort.15에 따른 전체 격자 절점의 난류(turbulence) 시계열(time series) 출력이다(3–6). 원문: ``This file contains turbulence time series output at all nodes in the model grid as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.`` (6). |
| 8–26 | File Structure — ASCII 파일 구조를 제시한다(11–25). 자료 집합(data set)마다 TIME·IT와 SIGMA 좌표를 기록한다(19–20). NP 절점별 수직 층 기록은 q20(j,M), l(j,M), EV(j,M)이다(22–25). 원문: `The file is written in ASCII format. The basic structure is shown below:` (11); `.. parsed-literal::` (13); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``     :ref:`NDSET3DGT <NDSET3DGT>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPO3DGT <NSPO3DGT>`, :ref:`NSPO3DGT <NSPO3DGT>`, :ref:`NFEN <NFEN>`, :ref:`IRTYPE <IRTYPE>` `` (17); ``     for k=1, :ref:`NDSET3DGT <NDSET3DGT>` `` (19); ``         :ref:`TIME <TIME>`, :ref:`IT <IT>`, (:ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, N=1, :ref:`NFEN <NFEN>`-1), :ref:`SIGMA(NFEN) <SIGMA>`, :ref:`SIGMA(NFEN) <SIGMA>` `` (20); ``         for j=1, :ref:`NP <NP>` `` (22); ``            j, (:ref:`q20(j,M) <q20(j,M)>`, :ref:`l(j,M) <l(j,M)>`, :ref:`EV(j,M) <EV(j,M)>`, M=1, :ref:`NFEN <NFEN>`)`` (23); `        end j loop` (24); `    end k loop` (25). |
| 27–37 | Notes — ASCII 형식만 제공한다(30). q20은 난류 운동에너지(turbulent kinetic energy)이다(33). l은 난류 길이 척도(turbulent length scale)이다(34). EV는 수직 와점성(vertical eddy viscosity)이다(35). SIGMA 값이 수직 층을 정의한다(36). fort.43과 유사하나 특정 관측점 대신 전체 영역을 기록한다고 적는다(37). 원문: `* Output is only available in ASCII format` (30); `* Time series data is recorded at all nodes in the model grid` (31); `* Turbulence parameters are stored as:` (32); `    * q20: turbulent kinetic energy` (33); `    * l: turbulent length scale` (34); `    * EV: vertical eddy viscosity` (35); `* Data is recorded at multiple vertical levels defined by SIGMA values` (36); `* Similar to fort.43 but provides data for the entire model domain instead of specific stations ` (37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
