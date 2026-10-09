---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.22x.grb2_file.md
lines: 49
sha256: 7248bfa921af7280dfbc4617909ae04b5fa02f6801652d10e6f67df1675037cf
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.22x.grb2_file.md — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Fort.22x.grb2 file / 버전·역할·제어 — 제목·판본·빈 줄과 버전 조건을 포함한다(1–7). GRIB2 이진(binary) 기상 입력을 wgrib2api 정적 라이브러리(static library)로 읽으며 시작 시 변수·유효 시각 목록(inventory)을 자동 생성한다고 적는다(9). 올바른 파일 이름·GRIB2 변수 이름과 fort.15의 세 설정 항목을 요구한다(9). 원문: `ADCIRC version:` (5); ` =  55 ` (7); `The fort.22x.grb2 files are meteorological inputs in [GRIB2](https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/) binary. These GRIB2 files are read by ADCIRC through the [wgrib2api](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/wgrib2api.html) static library. The API automatically generates an inventory of the GRIB2 file at the beginning of simulation to determine variable and valid datetime information in the files. The user does not need to do anything other than provide the correct filenames with valid GRIB2 variable names, in addition to specifying the [fort.15 file](/Fort.15_file) attributes correctly; [NWS](/NWS) = 14, correct [WTIMINC](/WTIMINC), and correct [NCDATE](/index.php?title=NCDATE&action=edit&redlink=1).` (9). |
| 11–20 | Contents — 압력·바람·선택적인 얼음 파일과 GRIB2 도구의 목차를 나열한다(11–19). 마지막 빈 줄을 포함한다(20). |
| 21–32 | fort.221.grb2 — 표면·해수면 기압(surface pressure / sea level pressure)의 허용 GRIB2 변수 이름 세 가지를 제시한다(23–29). 문서는 GFS와 CFSv2에서 선택할 기압 변수와 해양에서의 표면 기압 사용 가능성을 설명한다(31). 해양·육지 마스크(land/ocean mask)가 해상도 차이로 크게 불일치하면 경계에서 문제가 생길 수 있다고 적는다(31). 원문: `Contains the surface pressure/sea level pressure data. Valid GRIB2 variable names for this file are: ` (23); `- :PRMSL:mean sea level: or` (25); `- :MSLET:mean sea level: or` (27); `- :PRES:surface:` (29); `The mean sea level pressure, MSLET, is known to be a better choice than its counterpart, PRMSL, in the [GFS](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs) model [[1]](https://luckgrib.com/tutorials/2018/08/28/gfs-prmsl-vs-mslet.html). In comparison, the [CFSv2](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/climate-forecast-system-version2-cfsv2) model does not provide MSLET, thus PRMSL should be used. PRES:surface (surface pressure) should be equivalent to PRMSL/MSLET over the ocean and in general can be used. However, problems could arise at the land/ocean interface when there is a significant discrepancy between the ocean/land mask in ADCIRC and the meteorological model due to resolution differences.` (31). |
| 33–40 | fort.222.grb2 — 10 m 높이 바람 속도(wind velocity) 자료의 두 필수 GRIB2 변수 이름을 제시한다(35–39). 원문의 연결어 `and`를 그대로 옮긴다(37). 원문: `Contains the wind velocity at 10-m height data. Valid GRIB2 variable names for this file are: ` (35); `- :UGRD:10 m above ground: and` (37); `- :VGRD:10 m above ground:` (39). |
| 41–46 | fort.225.grb2 [optional] — 선택적인 표면 얼음 농도(surface ice concentration)를 면적 비율(area fraction)로 담는 파일의 GRIB2 변수 이름을 제시한다(41–45). 원문: `## fort.225.grb2 [optional][[edit](/index.php?title=Fort.22x.grb2_file&action=edit&section=3)]` (41); `Contains the surface ice concentration as an area fraction. Valid GRIB2 variable names for this file are: ` (43); `- :ICEC:surface:` (45). |
| 47–49 | GRIB2 utility — bash·perl 같은 스크립트를 통해 GRIB2 파일을 조작·생성하는 WGRIB2 도구 링크를 제시한다(49). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9: `NCDATE` 참조 URL에 `action=edit&redlink=1`이 들어 있다.
