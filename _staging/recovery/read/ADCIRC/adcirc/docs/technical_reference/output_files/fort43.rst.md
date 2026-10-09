---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort43.rst
lines: 30
sha256: c2ce849d8879744c0185d3f95ccb4fa221b7121db69d86f94df6924c93fef7a8
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort43.rst — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.43: 3D Turbulence at Specified Recording Stations — fort.15에 지정한 기록 관측점(recording station)의 난류(turbulence) 시계열(time series) 출력이다(1–4). 원문: ``This file contains turbulence time series output at the recording stations as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.`` (4). |
| 6–24 | File Structure — ASCII 파일 구조를 제시한다(9–23). 자료 집합(data set)마다 TIME·IT와 SIGMA 좌표를 기록한다(17–18). NSTA3DT 관측점별 수직 층 기록은 q20STA(M), ISTA(M), EVSTA(M)이다(20–23). 원문: `The file is written in ASCII format. The basic structure is shown below:` (9); `.. parsed-literal::` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NDSET3DST <NDSET3DST>`, :ref:`NSTA3DT <NSTA3DT>`, :ref:`DTDP <DTDP>` * :ref:`NSPO3DST <NSPO3DST>`, :ref:`NSPO3DST <NSPO3DST>`, :ref:`NFEN <NFEN>`, :ref:`IRTYPE <IRTYPE>` `` (15); ``     for k=1, :ref:`NDSET3DST <NDSET3DST>` `` (17); ``         :ref:`TIME <TIME>`, :ref:`IT <IT>`, (:ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, :ref:`SIGMA(N) <SIGMA>`, N=1, :ref:`NFEN <NFEN>`-1), :ref:`SIGMA(NFEN) <SIGMA>`, :ref:`SIGMA(NFEN) <SIGMA>` `` (18); ``         for j=1, :ref:`NSTA3DT <NSTA3DT>` `` (20); ``            j, (:ref:`q20STA(M) <q20STA>`, :ref:`ISTA(M) <ISTA>`, :ref:`EVSTA(M) <EVSTA>`, M=1, :ref:`NFEN <NFEN>`)`` (21); `        end j loop` (22); `    end k loop` (23). |
| 25–30 | Notes — ASCII 형식만 제공한다(28). 지정한 관측점의 여러 수직 층에서 난류 매개변수를 기록하며 수직 층은 SIGMA 값이 정의한다(29–30). 원문: `* Output is only available in ASCII format` (28); `* Time series data is recorded at specified recording stations` (29); `* The output includes turbulence parameters at multiple vertical levels defined by SIGMA values ` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
