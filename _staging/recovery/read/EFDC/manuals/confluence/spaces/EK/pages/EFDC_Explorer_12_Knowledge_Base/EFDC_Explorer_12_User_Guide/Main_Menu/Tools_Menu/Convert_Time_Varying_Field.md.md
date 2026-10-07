---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Tools_Menu/Convert_Time_Varying_Field.md
lines: 16
sha256: 4152841b941e41750f5ad1b8a354d7398d022578a0501e105f4225f7e473ae39
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Convert_Time_Varying_Field.md — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–13 | Convert Time Varying Field — EEMS 10의 새 옵션으로 모델 영역 전체의 각 셀에 시간 또는 공간에 따라 변하는 강제력(forcings)을 지정한다고 적는다(10). EE 10은 ASCII·이진(binary) 자료 파일을 불러올 수 있다(10). 자료가 큰 경우의 적용 조건은 `When the time-varying field data is large, users also have an option to convert data from ASCII format to binary format in *Convert Time Varying Field* form.` (12). 빈 줄을 포함한다(11·13). |
| 14–16 | 그림 / Figure 1 — 참조 URL의 파일명 부분을 규칙대로 디코딩한 이름은 `2.png?version=1&modificationDate=1581995776103&cacheVersion=1&api=v2&width=406&height=324`이다(14). 대응 로컬 경로는 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/442827075/2.png?version=1&modificationDate=1581995776103&cacheVersion=1&api=v2&width=406&height=324`이다(14). 그림 파일 없음. `ls`로 해당 첨부 폴더를 확인했으나 폴더도 없어서 그림을 열지 못했다. Figure 1 Convert Time Varying Field 캡션과 빈 줄·그림 마크업을 포함한다(14–16). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: `#Figure1` 링크가 있다. 이 파일에는 해당 앵커 정의가 없다.
- 14: 참조 URL의 파일명 부분에 쿼리 문자열이 `%3Fversion=1%26...` 형태로 인코딩되어 있다.
- 14: 그림 파일 없음. 규칙으로 대응시킨 파일과 `attachments/442827075` 폴더가 없어서 그림을 열지 못했다.

