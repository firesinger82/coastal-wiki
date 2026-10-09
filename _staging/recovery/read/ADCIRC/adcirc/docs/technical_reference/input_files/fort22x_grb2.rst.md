---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort22x_grb2.rst
lines: 72
sha256: aff2518abb2bd7f122866af95f83ef3b85f0e56b0038441d171a86ae69fdcae3
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort22x_grb2.rst — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | Fort.22x.grb2: Meteorological Inputs in GRIB2 Format — 메타데이터(metadata)·라벨·제목 및 버전 55 이후의 GRIB2 이진(binary) 기상 입력을 소개한다(1–15). wgrib2api 정적 라이브러리(static library)가 모의 시작에 변수와 유효 시각의 목록(inventory)을 자동 생성한다(14–18). 사용자가 제공할 파일 이름·변수 이름과 fort.15 설정을 제시한다(18–22). 원문: `Fort.22x.grb2 files can be used with ADCIRC version 55 and later.` (10); `The fort.22x.grb2 files are meteorological inputs in` (12); `` `GRIB2 <https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/>`_ binary. `` (13); `These GRIB2 files are read by ADCIRC through the` (14); `` `wgrib2api <https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/wgrib2api.html>`_ `` (15); `static library. The API automatically generates an inventory of the GRIB2 file` (16); `at the beginning of simulation to determine variable and valid datetime` (17); `information in the files. The user does not need to do anything other than` (18); `provide the correct filenames with valid GRIB2 variable names, in addition to` (19); ``specifying the :ref:`fort.15 file <fort15>` attributes correctly;`` (20); ``:ref:`NWS <nws_parameter>` = 14, correct :ref:`WTIMINC <wtiminc_supplemental>`, and correct`` (21); ``` ``NCDATE``. ``` (22). |
| 24–45 | fort.221.grb2 — 표면 또는 평균 해수면 압력(surface/mean sea level pressure)의 유효 변수 이름을 제시한다(27–32). GFS에서는 MSLET이 더 나은 선택이라고 적고 CFSv2에서는 제공되지 않아 PRMSL을 사용하도록 적는다(34–40). 표면 압력의 해상 동등성과 해륙 마스크(land/ocean mask) 해상도 차이로 문제가 생길 가능성을 설명한다(40–44). 원문: `Contains the surface pressure/sea level pressure data. Valid GRIB2 variable` (27); `names for this file are:` (28); ```-  ``:PRMSL:mean sea level:`` *or*``` (30); ```-  ``:MSLET:mean sea level:`` *or*``` (31); ``` -  ``:PRES:surface:`` ``` (32); `The mean sea level pressure, MSLET, is known to be a better choice than its` (34); `counterpart, PRMSL, in the` (35); `` `GFS <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs>`_ `` (36); ``model `1 <https://luckgrib.com/tutorials/2018/08/28/gfs-prmsl-vs-mslet.html>`_.`` (37); `In comparison, the` (38); `` `CFSv2 <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/climate-forecast-system-version2-cfsv2>`_ `` (39); `model does not provide MSLET, thus PRMSL should be used. PRES:surface (surface` (40); `pressure) should be equivalent to PRMSL/MSLET over the ocean and in general can` (41); `be used. However, problems could arise at the land/ocean interface when there is` (42); `a significant discrepancy between the ocean/land mask in ADCIRC and the` (43); `meteorological model due to resolution differences.` (44). |
| 46–54 | fort.222.grb2 — 높이 10m 풍속(wind velocity)의 두 성분을 모두 제공해야 하는 변수 이름을 제시한다(49–53). 원문: `Contains the wind velocity at 10-m height data. Valid GRIB2 variable names for` (49); `this file are:` (50); `-  :UGRD:10 m above ground: *and*` (52); `-  :VGRD:10 m above ground:` (53). |
| 55–64 | fort.225.grb2 [optional] — 선택적인 표면 얼음 면적 비율(surface ice concentration as an area fraction)의 변수 이름이다(57–63). 원문: `fort.225.grb2 [optional]` (57); `------------------------` (58); `Contains the surface ice concentration as an area fraction. Valid GRIB2 variable` (60); `names for this file are:` (61); `-  :ICEC:surface:` (63). |
| 65–72 | GRIB2 utility — WGRIB2 도구를 bash·perl 등의 스크립트로 GRIB2 조작과 생성에 사용할 수 있다고 적는다(70–72). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
