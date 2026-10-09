---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/input-file-descriptions/passive-scalar-transport-input-file-fort-10/feed/index.md
lines: 13
sha256: c97b3226f1a0b73293ea283548dfb2bea86d4e10c4d961cdcf7831c16e4ad6de
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# passive-scalar-transport-input-file-fort-10/feed/index.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | 피드(feed) 선언 문자열 — XML 버전과 인코딩(encoding) 문자열을 적는다(1). 뒤의 두 빈 줄을 포함한다(2–3). 원문: `xml version="1.0" encoding="UTF-8"?` (1). |
| 4–9 | 댓글 피드 제목·원문 주소·사이트 이름·시각 — Comments on 제목(4), 해당 입력 파일 설명의 원문 URL(6), 사이트 이름(7), UTC 시각(8)을 적는다. 이 구간에 댓글 본문이나 입력 변수 설명은 없다. 원문: `Comments on: Passive Scalar Transport Input File (fort.10) ` (4); `https://adcirc.org/home/documentation/users-manual-v51/input-file-descriptions/passive-scalar-transport-input-file-fort-10/` (6); `The Official ADCIRC Web Site` (7); `Thu, 26 Mar 2015 19:18:13 +0000` (8). |
| 10–13 | 피드 갱신 정보·WordPress URL — 갱신 정보로 hourly(10)와 1(12)을 적고 WordPress 버전 URL을 적는다(13). 사이의 빈 줄도 포함한다(11). 원문: `hourly ` (10); `1 ` (12); `https://wordpress.org/?v=6.8.5` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 1행: XML 선언처럼 보이는 문자열은 `xml version="1.0" encoding="UTF-8"?`이다. 문자열에 여는 `<?`와 닫는 `?>` 구분자가 온전히 들어 있지 않다.
