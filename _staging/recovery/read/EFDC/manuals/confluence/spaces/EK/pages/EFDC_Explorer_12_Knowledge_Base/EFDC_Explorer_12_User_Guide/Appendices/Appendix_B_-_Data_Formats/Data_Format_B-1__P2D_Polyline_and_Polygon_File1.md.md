---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-1__P2D_Polyline_and_Polygon_File1.md
lines: 60
sha256: e1ed8fe16a2317cb184913562832ac1631f1a65db07c861847a875e8b36785ef
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-1__P2D_Polyline_and_Polygon_File1.md — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–11 | P2D 형식 — 한 파일에 임의 개수의 폴리라인(polyline) 또는 다각형(polygon)을 넣을 수 있다(10). 각각 한 줄 ID 헤더 뒤에 2D 또는 3D 데이터를 두며 가져오기는 두 형식을 자동 처리한다(10). 첫 열의 종료 문자는 형상을 반드시 닫는다는 뜻이 아니다(10). 읽는 응용 프로그램의 처리 방식만 폴리라인과 다각형을 구분한다(10). 원문: `Any number of polylines or polygons can reside in the same file. Each one begins with a single line header that is used as the "ID" of the polyline or polygon. Next comes the data in either 2D or 3D format, the importing automatically handles either. Finally, the polyline or polygon is finished (not necessarily "closed") by an "\*" in column 1. There is no difference between polyline and polygon in a P2D file, only how the data are treated by the application reading the file.` (10). |
| 12–36 | Example 1 (Polyline) — 헤더와 3열 좌표 예시, 생략 표시 및 종료 문자를 제시한다(12–35). 빈 줄과 구분선도 포함한다. 원문: `Example 1 (Polyline)  ` (12); `------------------------  ` (13); `Polyline                                                            Test` (14); `609115.69390674        3643612.72035394     0` (16); `608828.057738002      3642922.39387814     0` (18); `608569.186338242      3642232.06904821     0` (20); `608396.604307826      3640908.94563456     0` (22); `...  ` (24); `...  ` (25); `...  ` (26); `601493.350247946      3628713.19503985     0` (27); `601464.586301899      3627763.99747289     0` (29); `601522.11337106        3627016.14485373      0` (31); `601522.11337106        3626642.21854415      0` (33); `\*` (35). |
| 37–50 | Example 2 (Polygon) / Zone1 — Zone1 헤더 뒤 2열 좌표와 종료 문자를 제시한다(37–49). 원문: `Example 2 (Polygon)  ` (37); `------------------------  ` (38); `Zone1` (39); `609115.69390674        3643612.72035394` (41); `608828.057738002      3642922.39387814` (43); `608569.186338242      3642232.06904821` (45); `608396.604307826      3640908.94563456` (47); `\*` (49). |
| 51–60 | Example 2 (Polygon) / Zone2 — Zone2 헤더 뒤 2열 좌표와 종료 문자를 제시한다(51–60). 원문: `Zone2` (51); `601493.350247946      3628713.19503985` (53); `601464.586301899      3627763.99747289` (55); `601522.11337106        3627016.14485373` (57); `601522.11337106        3626642.21854415     ` (59); `\*` (60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
