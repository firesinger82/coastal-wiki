---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/salinity-boundary-condition-input-fort-36/feed/index.md
lines: 13
sha256: 40a1a7c454f4101c45678341e7d41b7767f0a7f341905a38a72ee9584772112a
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# salinity-boundary-condition-input-fort-36/feed/index.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | 피드(feed) 시작부 — XML 버전·인코딩을 나타내는 한 줄과 빈 줄 두 줄을 포함한다(1–3). 원문: `xml version="1.0" encoding="UTF-8"?` (1). |
| 4–8 | Comments on / 댓글 피드 대상 — 댓글 대상 문서의 제목, 문서 URL, 공식 사이트 이름과 날짜 문자열을 포함한다(4–8). 이 구간에는 모델 입력 형식이나 매개변수 설명이 없다. 원문: `Comments on: Salinity Boundary Condition Input (fort.36) ` (4); `https://adcirc.org/home/documentation/users-manual-v50/input-file-descriptions/salinity-boundary-condition-input-fort-36/` (6); `The Official ADCIRC Web Site` (7); `Thu, 25 Jul 2013 19:14:19 +0000` (8). |
| 9–13 | 피드 갱신·생성기 표기 — 빈 줄과 갱신 주기 `hourly` (10), 수치 `1` (12), WordPress 버전 URL을 포함한다(13). `1`의 항목 이름은 이 파일에 없다(12). 원문: `hourly ` (10); `1 ` (12); `https://wordpress.org/?v=6.8.5` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 1행: `xml version="1.0" encoding="UTF-8"?`로 적혀 있다. 이 줄에는 XML 선언을 감싸는 `<`와 `>`가 없다.
- 12행: `1`만 적혀 있다. 이 값의 항목 이름은 파일 안에 없다.
