---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_71A.md
lines: 52
sha256: 156b6b41f11a5cbdf03be4fb0a1ae5d0961422ee9df19719631041d9337600e1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_71A.md — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–48 | C71A CONTROLS FOR HORIZONTAL PLANE SEDIMENT BED PROPERTIES CONTOURING — 수평면 퇴적층 특성(sediment bed properties) 등치선(contouring) 출력을 다룬다(10). `ISBEXP`에 Explorer 이진 형식(binary format)과 출력 빈도(output frequency)를 언급한다(18). 나머지 열거된 설명은 `NOT USED`라고 적는다(14·20–30·36·42–44). `SBSED`와 `ISBSED`를 별개 원문 이름으로 보존한다(30·36). 반복 주석 표식과 빈 줄을 포함한다(11–48). 원문: `C71A CONTROLS FOR HORIZONTAL PLANE SEDIMENT BED PROPERTIES CONTOURING` (10); `\* ISBPH: NOT USED` (14); `\* ISBEXP: 0 >0 EXPLORER BINARY FORMAT, OUTPUT FREQUENCY` (18); `\* NPBPH: NOT USED` (20); `\* ISRBPH: NOT USED` (22); `\* ISBBDN: NOT USED` (24); `\* ISBLAY: NOT USED` (26); `\* ISBPOR: NOT USED` (28); `\* SBSED: NOT USED` (30); `\* ISBSED: NOT USED` (36); `\* ISBVDR: NOT USED` (42); `\* ISBARD: NOT USED` (44). |
| 49–52 | C71A 입력 예시 — 입력 열 제목과 수치 값 행을 제시한다(50·52). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(49·51). 원문: `C71A ISBPH ISBEXP NPBPH ISRBPH ISBBDN ISBLAY ISBPOR ISBSED ISBSND ISBVDR ISBARD` (50); `               0        0          1            0           0           1           0           1            1           1           0` (52). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18행: `ISBEXP` 설명은 `0 >0 EXPLORER BINARY FORMAT, OUTPUT FREQUENCY`로 적혀 있다. `0`의 의미를 구분해서 설명하지 않는다.
- 30·36·50행: 주석에는 `SBSED`와 `ISBSED`가 각각 등장한다. 입력 열 제목은 `ISBSED`와 `ISBSND`를 포함한다. `ISBSND`의 설명은 없다.

