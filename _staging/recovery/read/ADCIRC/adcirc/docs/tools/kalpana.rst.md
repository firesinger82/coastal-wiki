---
file: models/ADCIRC/raw/source_code/adcirc/docs/tools/kalpana.rst
lines: 23
sha256: dc69f6169f66b87068bb239c8a5c7e3ca1452c68b5fe4bc07adcd64a480392b0
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# kalpana.rst — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Kalpana — `:orphan:` 지시문과 제목을 포함한다(1–4). ADCIRC 출력을 지리공간 벡터(geospatial vector)로 바꾸고 최대 수위를 상세화(downscaling)하는 Python 모듈로 소개한다(6). 개발 기관과 지리정보시스템(Geographic Information System, GIS) 시각화·침수(inundation) 표현의 목적을 적는다(6). 원문: `:orphan:` (1); `Kalpana` (3); `=======` (4); `Kalpana is a Python module developed by the Coastal & Computational Hydraulics Team at North Carolina State University for converting ADCIRC model outputs to geospatial vector formats and downscaling maximum water elevations. It enables the visualization of ADCIRC results in common GIS formats and improves inundation representation through high-resolution downscaling.` (6). |
| 8–18 | Features — shapefile·KMZ 변환과 시간 변화(time-varying)·시간 불변(time-constant) 출력 지원, 최대 수위의 높은 해상도 래스터(raster) 상세화를 설명한다(11–13). 예측 영역 너머 지표면까지 수면을 확장하는 기능(surface expansion), 정적(static)·수두 손실(head-loss) 방법, Python 구현과 선·다각형 출력(polyline/polygon)을 열거한다(14–17). 원문: `Features` (8); `--------` (9); `* **Vector Conversion**: Convert ADCIRC outputs to geospatial vector formats (shapefile or KMZ)` (11); `* **Time-Varying Support**: Process both time-varying outputs (fort.63.nc, swan_HS.63.nc) and time-constant outputs (maxele.63.nc)` (12); `* **Downscaling**: Downscale maximum water elevations to higher-resolution raster for improved inundation representation` (13); `* **Surface Expansion**: Expand water surfaces to intersect with ground surface beyond ADCIRC-predicted extents` (14); `* **Multiple Methods**: Support for static and head-loss methods for storm surge expansion and contraction` (15); `* **Python Integration**: Fully implemented in Python with modern package structure` (16); `* **Visualization Options**: Generate polylines or polygons in multiple formats for visualization` (17). |
| 19–23 | Links — GitHub 저장소와 연구 논문(research paper)을 연결한다(22–23). 절 제목·밑줄·빈 줄을 포함한다(19–21). 원문: `Links` (19); `-----` (20); ``* `GitHub Repository <https://github.com/ccht-ncsu/Kalpana>`_`` (22); ``* `Research Paper <https://link.springer.com/article/10.1007/s11069-021-04634-8>`_ `` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

