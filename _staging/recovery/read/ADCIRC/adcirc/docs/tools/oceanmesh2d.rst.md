---
file: models/ADCIRC/raw/source_code/adcirc/docs/tools/oceanmesh2d.rst
lines: 28
sha256: 5c35f8b174237ed25b717ac66da5c0d8a8f3a924af655b5eeb2b5b8a6635c717
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# oceanmesh2d.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | OceanMesh2D — `:orphan:` 지시문·참조 라벨·제목을 포함한다(1–6). 순수 MATLAB으로 작성한 2차원 삼각 격자 생성기(triangular mesh generator)와 전처리(pre-processing)·후처리(post-processing) 유틸리티로 소개한다(8). 천수방정식(shallow-water equations)·파동방정식(wave equations) 연안 모델과 지원 모델을 열거하고 추가 MATLAB 툴박스(toolbox)가 필요 없다고 적는다(8). 원문: `:orphan:` (1); `.. _oceanmesh2d:` (3); `OceanMesh2D` (5); `===========` (6); `OceanMesh2D is a two-dimensional triangular mesh generator with pre- and post-processing utilities written in pure MATLAB. It's specifically designed for building models that solve shallow-water equations or wave equations in coastal environments, including support for ADCIRC, FVCOM, WaveWatch3, SWAN, SCHISM, and Telemac models. The software requires no additional MATLAB toolboxes.` (8). |
| 10–23 | Features — 여러 규모의 해상도(multi-scale resolution), 해안선(coastline)·경계조건·절점 속성(nodal attributes)·Manning 계수, 수심·지형 보간(interpolation)과 수치표고모델(Digital Elevation Model, DEM) 자료를 설명한다(13–17). 조석 경계 생성, 격자 재생성·정리·수정, 도표·시각화, 하천 유량 경계 파일과 격자 품질 평가·개선 기능을 열거한다(18–22). 원문: `Features` (10); `--------` (11); `* **Mesh Generation**: Creates high-quality triangular meshes for coastal simulations with multi-scale resolution` (13); `* **Boundary Handling**: Advanced tools for coastline representation and boundary condition management` (14); `* **Attribute Support**: Tools for assigning and manipulating nodal attributes including Manning's coefficients` (15); `* **Bathymetry Processing**: Interpolation capabilities for bathymetry and topography data` (16); `* **DEM Integration**: Tools for working with Digital Elevation Models of various formats` (17); `* **Tidal Data Support**: Generation of tidal boundary conditions from various datasets` (18); `* **Mesh Editing**: Capabilities for remeshing, cleaning, and modifying mesh elements` (19); `* **Visualization**: Comprehensive plotting functions with support for various visualization types` (20); `* **River Forcing**: Support for creating river flow boundary conditions (fort.20 files)` (21); `* **Mesh Quality Tools**: Functions for assessing and improving mesh quality` (22). |
| 24–28 | Links — GitHub 저장소와 사용자 안내서(User Guide)를 연결한다(27–28). 절 제목·밑줄·빈 줄을 포함한다(24–26). 원문: `Links` (24); `-----` (25); ``* `GitHub Repository <https://github.com/CHLNDDEV/OceanMesh2D>`_`` (27); ``* `User Guide <https://github.com/CHLNDDEV/OceanMesh2D/tree/master/UserGuide>`_ `` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

