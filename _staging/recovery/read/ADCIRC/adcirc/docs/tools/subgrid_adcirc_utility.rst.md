---
file: models/ADCIRC/raw/source_code/adcirc/docs/tools/subgrid_adcirc_utility.rst
lines: 23
sha256: de9aac41ba69ed61b0470c2188de42ac90380f13670ce245b1dd69c15b60cb4a
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# subgrid_adcirc_utility.rst — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | SubgridADCIRCUtility — `:orphan:` 지시문과 제목을 포함한다(1–4). 하위격자(subgrid) 기능을 사용하는 ADCIRC의 입력 파일 생성용 Python 도구 모음(toolkit)을 소개한다(6). 매우 미세한 격자 해상도 없이 높은 해상도의 지형·토지피복(landcover)을 표현하는 목적을 설명한다(6). 원문: `:orphan:` (1); `SubgridADCIRCUtility` (3); `====================` (4); `SubgridADCIRCUtility is a Python-based toolkit for creating subgrid input files for subgrid-enabled ADCIRC. It enables the representation of high-resolution terrain and landcover features without requiring extremely fine mesh resolution, improving simulation accuracy while maintaining computational efficiency.` (6). |
| 8–19 | Features — 하위격자 조회표(lookup table), 높은 해상도의 수치표고모델(Digital Elevation Model, DEM), 토지피복별 Manning's n 할당과 사용자 수위 범위의 보정값을 설명한다(11–14). 조회표 단순화, 여러 DEM·토지피복 파일의 동시 계산, 기본·맞춤 Manning's n 값 표와 NetCDF 출력을 열거한다(15–18). 원문: `Features` (8); `--------` (9); `* **Subgrid Lookup Tables**: Generate lookup tables that store subgrid information for ADCIRC` (11); `* **DEM Integration**: Process high-resolution Digital Elevation Models for subgrid calculations` (12); `* **Landcover Processing**: Incorporate landcover data for Manning's n coefficient assignment` (13); `* **Water Level Range**: Compute subgrid corrections over user-defined water surface elevation ranges` (14); `* **Table Simplification**: Optimize lookup tables for efficiency in ADCIRC simulations` (15); `* **Multiple Data Sources**: Support for multiple DEM and landcover files in a single calculation` (16); `* **Manning's Value Customization**: Support for both default and custom Manning's n value tables` (17); `* **NetCDF Output**: Generate outputs in NetCDF format for direct use with subgrid ADCIRC` (18). |
| 20–23 | Links — GitHub 저장소를 연결한다(23). 절 제목·밑줄·빈 줄을 포함한다(20–22). 원문: `Links` (20); `-----` (21); ``* `GitHub Repository <https://github.com/ccht-ncsu/subgridADCIRCUtility>`_ `` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

