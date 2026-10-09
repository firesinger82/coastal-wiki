---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/output-file-descriptions/3d-velocity-at-specified-recording-stations-fort-42/feed/index.md
lines: 13
sha256: 9734ee316d3d2f016ae7cac79595f9478aa8f407fda48477255a7cf2728e0edc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | feed 머리말 — XML 버전·문자 인코딩(encoding) 문자열과 빈 줄이다(1–3). 원문: `xml version="1.0" encoding="UTF-8"?` (1). |
| 4–5 | 댓글 feed 제목 — `Comments on: 3D Velocity at Specified Recording Stations (fort.42) ` (4). 해당 출력 파일 설명의 댓글 제목이다(4). 뒤의 빈 줄도 포함한다(5). |
| 6–9 | feed 출처·시각 — 해당 ADCIRC 문서 URL이 있다(6). 사이트 이름은 `The Official ADCIRC Web Site` (7). 시각 문자열은 `Fri, 27 Mar 2015 14:22:59 +0000` (8). 뒤의 빈 줄도 포함한다(9). |
| 10–13 | feed 갱신·생성기(generator) — 갱신 문자열 `hourly ` (10), 빈 줄(11), 값 `1 ` (12), WordPress 생성기 URL `https://wordpress.org/?v=6.8.5` (13)로 끝난다. 이 파일에는 모델 출력 형식·수식·매개변수·그림이 없다(1–13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 1: 문자열은 `xml version="1.0" encoding="UTF-8"?`이다. XML 선언의 여는 구분자 `<?`와 닫는 구분자 `?>`가 이 행에 없다.
