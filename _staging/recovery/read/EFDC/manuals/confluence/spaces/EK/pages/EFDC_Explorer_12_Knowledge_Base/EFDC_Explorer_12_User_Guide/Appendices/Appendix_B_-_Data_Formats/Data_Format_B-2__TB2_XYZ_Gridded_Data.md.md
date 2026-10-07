---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-2__TB2_XYZ_Gridded_Data.md
lines: 46
sha256: 887fef4e84f0d8db95f06a55dba486ac85bc4069f3da11d35904556ecff6dfd8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-2__TB2_XYZ_Gridded_Data.md — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–12 | TB2 XYZ Gridded Data — 정규 격자(regular grid)의 X, Y, Z 데이터를 압축해 저장한다(10). X 좌표, Y 좌표와 Z 값 목록을 각각 두며 각 목록의 첫 값은 데이터 점의 수이다(10). 예시 제목과 구분선을 포함한다(11–12). 원문: `This format is a compact way to store regular grid X, Y, and Z data. It contains three lists, each with the number of data points as the first value in the list. The file contains a list of the X coordinates, a list of Y coordinates, and a list of the Z's.   ` (10); `Example  ` (11); `------------------------  ` (12). |
| 13–24 | TB2 X 목록 예시 — Nx를 표시한 점 수, 좌표 값과 생략 표시를 제시한다(13–24). 원문: `195                                                            Nx` (13); `-97516.6484` (15); `-96511.4938` (17); `-95506.3391` (19); `-94501.1845  ` (21); `...  ` (22); `...  ` (23); `...  ` (24). |
| 25–36 | TB2 Y 목록 예시 — Ny를 표시한 점 수, 좌표 값과 생략 표시를 제시한다(25–36). 원문: `113                                                            Ny` (25); `656865` (27); `657873.929` (29); `658882.857` (31); `659891.786  ` (33); `...  ` (34); `...  ` (35); `...  ` (36). |
| 37–46 | TB2 Z 목록 예시 — Nz를 표시한 점 수, Z 값과 생략 표시를 제시한다(37–46). 원문: `22035                                                        Nz` (37); `-28.337` (39); `-28.346999` (41); `-28.1969829  ` (43); `...  ` (44); `...  ` (45); `...` (46). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
