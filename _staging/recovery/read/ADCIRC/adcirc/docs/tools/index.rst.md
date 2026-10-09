---
file: models/ADCIRC/raw/source_code/adcirc/docs/tools/index.rst
lines: 43
sha256: 9f2dc7311adc977ab9ab871ef5046e757c57df59dbc97e00b8e17d513b988114
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.rst — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Tools — `tools` 참조 라벨·제목·빈 줄을 포함한다(1–7). 전처리·격자 생성(mesh generation)·모델 설정·후처리·시각화(visualization)를 돕는 ADCIRC 커뮤니티 도구의 문서 링크를 소개한다(6). 원문: `.. _tools:` (1); `Tools` (3); `=====` (4); `ADCIRC users can benefit from various tools that support ADCIRC to assist with pre-processing, mesh generation, model setup, post-processing, and visualization. This page provides links to documentation for several popular tools used by the ADCIRC community.` (6). |
| 8–12 | ADCIRC Utility Programs — ADCIRC 유틸리티 웹페이지를 연결한다(8–11). 절점 속성(nodal attributes)과 fort.13 파일을 만드는 `f13builder`를 예로 적는다(11). 원문: `ADCIRC Utility Programs` (8); `-----------------------` (9); ```The `ADCIRC utilities webpage <https://adcirc.org/home/related-software/adcirc-utility-programs/>`_ hosts a wide range of basic and advanced tools that have been developed by the ADCIRC community over the years, including ``f13builder`` to create nodal attributes and the :ref:`fort.13 file <fort13>`. ``` (11). |
| 13–20 | Multi-Purpose Modeling and Visualization Tools — 지표수 모델(surface water model)의 구성·계산·시각화를 위한 SMS와 Perl·MATLAB·C++·Python 유틸리티 모음을 연결한다(16–19). 원문: `Multi-Purpose Modeling and Visualization Tools` (13); `----------------------------------------------` (14); ``* :doc:`SMS (Surface-water Modeling System) <sms>` - Software for building, simulating, and visualizing surface water models`` (16); ``* `AdcircUtils <https://github.com/natedill/ourPerl/tree/master/AdcircUtils>`_ - A suite of Perl utilities that can be foundon Nate Dill's Github.`` (17); ``* `adcirc_util <https://github.com/BrianOBlanton/adcirc_util>`_ - A suite of utilities in MATLAB.`` (18); ``* `ADCIRCModules <https://github.com/zcobell/ADCIRCModules>`_ - A suite of utilities in C++ and Python.`` (19). |
| 21–27 | Pre-processing and Mesh Generation — MATLAB 삼각 격자(triangular mesh) 생성기 OceanMesh2D, 수직 요소벽(Vertical Element Wall, VEW) 기법의 수로 격자(channel mesh)를 포함한 VEW Utils, 하위격자(subgrid) 입력용 SubgridADCIRCUtility를 연결한다(24–26). 원문: `Pre-processing and Mesh Generation` (21); `----------------------------------` (22); ``* :doc:`OceanMesh2D <oceanmesh2d>` - MATLAB-based triangular mesh generator for coastal models`` (24); ``* :doc:`VEW Utils <vewutils>` - Python and MATLAB utilities for ADCIRC, including channel mesh generation with virtical element wall techniques`` (25); ``* :doc:`SubgridADCIRCUtility <subgrid_adcirc_utility>` - Python toolkit for creating subgrid input files for ADCIRC `` (26). |
| 28–31 | Forcing Data Acquisition — 유체역학 모델(hydrodynamic model)의 기상 강제력(meteorological forcing) 획득·개발 시스템 MetGet을 연결한다(28–30). 마지막 빈 줄을 포함한다(31). 원문: `Forcing Data Acquisition` (28); `------------------------` (29); ``* :doc:`MetGet <metget>` - Meteorological forcing acquisition and development system for hydrodynamic models`` (30). |
| 32–38 | Model Setup and Control — ADCIRC 설정·실행 자동화 라이브러리 ADCIRCpy, 실시간 의사결정용 자동화 기반 ASGS와 고성능 계산(HPC) 환경의 예측 시스템 Floodwater를 연결한다(35–37). 원문: `Model Setup and Control` (32); `-----------------------` (33); ``* :doc:`ADCIRCpy <adcircpy>` - Python library for automating ADCIRC model setup and execution`` (35); ``* :doc:`ASGS (Automated Solution Generation System) <asgs>` - Software infrastructure for automating coastal ocean modeling for real-time decision support`` (36); ``* :doc:`Floodwater <floodwater>` - Modern and extensible forecasting system for hydrodynamic models operating in HPC environments`` (37). |
| 39–43 | Post-processing and Visualization — ADCIRC 출력의 래스터(raster) 변환 도구 FigureGen과 벡터(vector) 변환·상세화(downscaling) 모듈 Kalpana를 연결한다(42–43). 원문: `Post-processing and Visualization` (39); `---------------------------------` (40); ``* :doc:`FigureGen <figuregen>` - Visualization tool for converting ADCIRC outputs to raster formats`` (42); ``* :doc:`Kalpana <kalpana>` - Python module for converting ADCIRC outputs to vector formats and downscaling`` (43). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 25행: VEW 기법의 영문 표현은 `virtical element wall techniques`로 적혀 있다. 대상 VEW Utils 문서의 6·11·18행은 `Vertical Element Wall`로 적는다.

