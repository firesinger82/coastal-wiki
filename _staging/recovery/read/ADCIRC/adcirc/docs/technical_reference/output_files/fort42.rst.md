---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort42.rst
lines: 34
sha256: b567db077ff2c00e1412bb4dac885db6c5c32d3733bfa10d17672ba0c649dd48
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort42.rst — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.42: 3D Velocity at Recording Stations — fort.15에 지정한 기록 관측점(recording station)의 속도 시계열(velocity time series) 출력이다(1–4). 원문: ``This file contains velocity time series output at recording stations as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.`` (4). |
| 6–24 | File Structure — ASCII 파일 구조를 제시한다(9–23). 자료 집합(data set)마다 TIME·IT와 SIGMA 좌표를 기록한다(17–18). NSTA3DV 관측점 반복 안에서 수직 층별 REAL(QSTA(M)), AIMAG(QSTA(M)), WZSTA(k,j)를 기록한다(20–23). 첨자는 원문 그대로 옮긴다(21). 원문: `The file is written in ASCII format. The basic structure is shown below:` (9); `.. parsed-literal::` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NDSET3DSV <NDSET3DSV>`, :ref:`NSTA3DV <NSTA3DV>`, :ref:`DTDP <DTDP>` * :ref:`NSPO3DSV <NSPO3DSV>`, :ref:`NSPO3DSV <NSPO3DSV>`, :ref:`NFEN <NFEN>`, :ref:`IRTYPE <IRTYPE>` `` (15); ``     for k=1, :ref:`NDSET3DSV <NDSET3DSV>` `` (17); ``         :ref:`TIME <TIME>`, :ref:`IT <IT>`, (:ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, N=1, :ref:`NFEN <NFEN>`-1), :ref:`SIGMA(NFEN) <SIGMA>`, :ref:`SIGMA(NFEN) <SIGMA>` `` (18); ``         for j=1, :ref:`NSTA3DV <NSTA3DV>` `` (20); ``            j, (:ref:`REAL(QSTA(M)) <REAL(QSTA(k,j))>`, :ref:`AIMAG(QSTA(M)) <AIMAG(QSTA(k,j))>`, :ref:`WZSTA(k,j) <WZSTA>`, M=1, :ref:`NFEN <NFEN>`)`` (21); `        end j loop` (22); `    end k loop` (23). |
| 25–34 | Notes — ASCII 형식만 제공한다(28). QSTA의 실수부와 허수부는 각각 x방향과 y방향 속도이다(30–32). WZSTA는 수직 속도 성분이다(33). SIGMA 값이 수직 층을 정의한다(34). 원문: `* Output is only available in ASCII format` (28); `* Time series data is recorded at specified recording stations` (29); `* Velocity components are stored as:` (30); `    * REAL(QSTA): x-component of velocity` (31); `    * AIMAG(QSTA): y-component of velocity` (32); `    * WZSTA: vertical velocity component` (33); `* Data is recorded at multiple vertical levels defined by SIGMA values ` (34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 21행: 수직 반복은 `M=1, NFEN`으로 적는다. 같은 기록의 QSTA 표시에는 `M`이 있지만 WZSTA는 `WZSTA(k,j)`로 적는다. REAL·AIMAG의 표시 인수는 `QSTA(M)`이고 참조 대상의 인수는 `QSTA(k,j)`이다.
