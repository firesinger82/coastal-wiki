---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v51/output-file-descriptions/screen-output-fort-6/feed/index.md
lines: 13
sha256: eaf8f87c1588496a2c5ea86f3d331ab5e25304c48a6a1bf8862557cbe5d4bed2
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | 댓글 피드(comment feed) / 선언 문자열 — 첫 줄에 XML 버전과 문자 인코딩 문자열이 있다(1). 빈 줄이 이어진다(2–3). 원문: `xml version="1.0" encoding="UTF-8"?` (1). |
| 4–9 | 댓글 피드 / 제목·대상 주소·시각 — 대상 문서의 댓글 피드 제목이 있다(4). 대상 페이지 주소와 공식 ADCIRC 사이트 표제가 있다(6–7). 시각 문자열이 있다(8). 빈 줄도 이 구간에 포함한다(5·9). 원문: `Comments on: Screen output (fort.6) ` (4); `https://adcirc.org/home/documentation/users-manual-v51/output-file-descriptions/screen-output-fort-6/` (6); `The Official ADCIRC Web Site` (7); `Fri, 27 Mar 2015 15:21:18 +0000` (8). |
| 10–13 | 댓글 피드 / 갱신 정보·생성기 주소 — 갱신 정보 문자열이 있다(10·12). WordPress 버전 쿼리를 포함한 주소가 있다(13). 사이 빈 줄도 이 구간에 포함한다(11). 원문: `hourly ` (10); `1 ` (12); `https://wordpress.org/?v=6.8.5` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 1: XML 버전·인코딩 문자열에는 여는 표지 `<?`와 닫는 표지 `?>`가 없다. 원문은 `xml version="1.0" encoding="UTF-8"?` (1)이다.
