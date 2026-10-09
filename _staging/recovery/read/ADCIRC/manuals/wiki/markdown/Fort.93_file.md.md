---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.93_file.md
lines: 9
sha256: b4cad8d38109a4b8f14e9c24585728ee2e3e31f3a2fe3d476679cf8f94e058f7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.93_file.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.93 file — 제목과 판본 표기 `_revid=667_`(1–3)을 포함한다. 해빙장(ice field) 출력은 fort.73 압력 파일 또는 fort.63 수위 파일과 같은 형식이라고 설명한다(5). 해빙장을 사용하고 전역 기상 출력(global meteorology output)을 지정할 때만 이 파일을 생성한다고 설명한다(5). 적용 조건과 출력 제어 변수 원문: `Output ice field files are written to a fort.93 file that has the same format as the [fort.73 pressure file](/Fort.73_file) or [fort.63 elevation file](/Fort.63_file). This file is only generated when ice fields are used and when global meteorology output is specified for outputting. The settings for global meteorology output are ([NOUTGW](/index.php?title=NOUTGW&action=edit&redlink=1), [TOUTSGW](/index.php?title=TOUTSGW&action=edit&redlink=1), [TOUTFGW](/index.php?title=TOUTFGW&action=edit&redlink=1), [NSPOOLGW](/index.php?title=NSPOOLGW&action=edit&redlink=1)) in the [fort.15 file](/Fort.15_file).` (5). |
| 7–9 | File Format — fort.93 file format 문서로 연결한다(7–9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5행: NOUTGW·TOUTSGW·TOUTFGW·NSPOOLGW 참조 URL에 `action=edit&redlink=1`이 들어 있다.
