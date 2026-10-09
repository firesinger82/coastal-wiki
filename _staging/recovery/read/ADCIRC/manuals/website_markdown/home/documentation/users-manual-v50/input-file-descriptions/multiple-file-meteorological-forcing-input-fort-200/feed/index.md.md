---
file: models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v50/input-file-descriptions/multiple-file-meteorological-forcing-input-fort-200/feed/index.md
lines: 13
sha256: 0e43429a851fc615dd49f03d3c5d40c6c0e9453aad8793c72b553b9a2386d8a7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | 피드(feed) 선언·빈 줄 — 첫 줄은 XML 버전과 문자 인코딩(encoding) 문자열이다(1). 뒤에는 빈 줄이 이어진다(2–3). 원문: `xml version="1.0" encoding="UTF-8"?` (1). |
| 4–13 | Comments on: Multiple File Meteorological Forcing Input (fort.200, ??) — 댓글 피드(feed) 제목과 원문 주소, 사이트 소개, 갱신 시각, `hourly`, `1`, WordPress 버전 주소를 담는다(4–13). 기술 본문과 댓글 항목은 이 파일에 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 1: 첫 줄은 `xml version="1.0" encoding="UTF-8"?`이다. XML 선언의 시작 구분자 `<?`와 끝 구분자 `?>`는 없다.
