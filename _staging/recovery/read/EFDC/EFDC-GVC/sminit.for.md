---
file: models/EFDC/raw/source_code/EFDC-GVC/sminit.for
lines: 43
sha256: 8eda8e3ef59ca308ebcdabc25a4956f44a7d2b5176e1a67f4c23d25b1062a416
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sminit.for — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 머리말·SMINIT 선언·버전·두 수정일 표기·변경 이력(1–25). EFDC.PAR·EFDC.CMN 포함과 주석을 적는다(26–28). |
| 29–43 | 시작 시 6행 SMINIT 루틴 안. 장치 번호의 비활성 설정은 `CXH      INSMICI=40` (29); `CXH      INSMRST=40` (30); `CXH      ISMORST=45` (31); `CXH      ISMOZB=46` (32). SMTSNAME의 1·2·3에 SOM·SIM·SBF 문자열을 넣는다(34–36). L=2..LA의 SMHYST를 FALSE로 초기화한다(38–40). 주석·RETURN·END를 포함한다(41–43). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–32: INSMICI·INSMRST·ISMORST·ISMOZB의 장치 번호 설정은 모두 CXH 주석이다.
- 38–40: SMHYST 초기화 범위는 L=2..LA다. 인덱스 1·LC를 초기화하는 문장은 이 파일에 없다.
