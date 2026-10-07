---
file: models/SFINCS/raw/source_code/sfincs/docs/waves.rst
lines: 15
sha256: 5d322125224709ea7751785c92e903798948f3c7e0d6cae38b88111b5020c98b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# waves.rst — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Wave input / Introduction — 문서 제목·Introduction 제목·구분선·빈 줄을 포함한다(1–6). 이 구간에는 설명 본문이 없다. |
| 7–15 | Introduction / 사용하지 말라는 파일 목록 — 원문은 파랑 경계조건 입력을 아직 작업 중이라고 적고, 바로 아래 파일들을 현재 사용하지 말아야 한다고 적는다(7). 적용 조건·금지 문장과 네 설정 줄을 그대로 옮긴다(7·9·11·13·15). 각 키의 값은 빈 문자열로 적혀 있다. 원문은 이 값을 기본값이라고 정의하지 않는다. 각 설정 사이의 빈 줄과 마지막 cstfile 줄까지 포함한다(8–15). 원문: `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:` (7); `bwvfile = ''` (9); `bhsfile = ''` (11); `btpfile = ''` (13); `cstfile = ''` (15). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9·11·13·15행: bwvfile·bhsfile·btpfile·cstfile은 빈 문자열 설정으로 나열되어 있다. 이 파일 안에는 각 키의 의미·파일 형식·단위·허용 범위·기본값 여부를 정의하는 설명이 없다.
- 1–2행: 제목 밑줄은 각 제목의 끝 공백을 제외한 문자 수보다 짧다.
