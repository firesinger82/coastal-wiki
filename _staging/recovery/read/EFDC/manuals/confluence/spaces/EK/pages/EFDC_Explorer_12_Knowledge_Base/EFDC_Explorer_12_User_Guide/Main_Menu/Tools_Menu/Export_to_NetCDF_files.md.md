---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Tools_Menu/Export_to_NetCDF_files.md
lines: 26
sha256: bd94ea930827acf427ab1dd1e2867c11f4ab97bb32c12d1511f0b34a9c9f340e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Export_to_NetCDF_files.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–15 | Export to NetCDF files — EFDC+ 이진(binary) 출력을 웹 서버에서 읽고 표시할 수 있는 NetCDF-CF(NetCDF- Climate and Forecast) 자료로 바꾼다고 적는다(10). 출력 존재 조건은 `The NetCDF files can be converted only when the model has outputs.` (12). 변환할 매개변수와 내보낼 기간을 고른다(14). 빈 줄을 포함한다(11·13·15). |
| 16–21 | Time / Time Steps / Deflate Level — Julian 시각 기본 형식과 모델 기간 안의 시작·종료 조건은 `In the *Time* frame, Julian time is the default format for the start and end times. However, the user can define a time range to export by entering a new time for the start and end (note that the entered time must be between the start and end time of the model).` (16). 모델 스냅샷(snapshot) 건너뛰기 설정의 이름·기본값·의미는 `*Time Steps*: This is the time step for skipping the snapshot time of the model. The default value is 1, which means that the NetCDF file contains every model's snapshot.` (18). 압축(compression) 설정의 범위와 파일 크기·내보내기 시간 관계는 `*Deflate Level*: This is the compression factor for the NetCDF file, where the value ranges from 0 to 9. The higher value of the deflate level, the smaller the file size but it will take more time to export to the NetCDF file.` (20). 빈 줄을 포함한다(17·19·21). |
| 22–26 | File Creation / 출력 위치·화면 — 단일 파일·일별 파일 조건과 하루 단위는 `In the *File Creation* frame, the user is given the option of EFDC+ generating a *Single File*, or *Multiple Daily Files.*The *Multiple Daily Files* option provides one netCDF file for each one day (24 hours) of model output.` (22). `.nc` 출력 위치는 `NetCDF files (.nc files) are placed in the *#analysis* folder along with the EFDC output.` (24). 그림 `4-29-2022_3-17-37_PM.png`는 정적 자료 Model Grid·Initial Bottom Elevation, 동적 자료 Water Surface Elevation·Flow Velocity·Temperature·Wind 선택과 기간·압축·파일 생성 설정을 보여 준다(26). 화면의 `Start: 213.000`, `End: 713.000`, `Time Steps: 1`, `Deflate Level: 2`, `Single File`, `UTM Zone Projection: 16`은 이 예시의 표시값이다(26, 그림). 시작·종료 날짜 표시는 `2012-08-01 00:00:00`, `2013-12-14 00:00:00`이다(26, 그림). 26행의 Deflate Level 2를 문서 기본값으로 판단하지 않았다. 빈 줄·마지막 그림 마크업을 포함한다(23·25–26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14: `#ExporttoNetCDFfiles-Figure1` 링크가 있다. 이 파일에는 해당 앵커와 Figure 1 캡션이 없다.

