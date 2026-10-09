---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.36_file.md
lines: 9
sha256: 0d5c07a2c932513dacdd97dd4f495548f350ac14d1399f92e0a7ec0eebb19126
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.36_file.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | Fort.36 file — 문서 제목(1)과 판본 표기 `_revid=463_` (3)를 포함한다. 빈 줄(2·4)을 포함한다. |
| 5–6 | 염분 경계조건(salinity boundary condition) 입력 — fort.36는 ADCIRC 염분 경계조건 입력 파일이다(5). fort.15의 RES_BC_FLAG가 -2, 2, -4 또는 4일 때 읽는다(5). 원문: `The fort.36 file is the ADCIRC Salinity Boundary Condition Input File. It is read in when the [RES_BC_FLAG](/index.php?title=RES_BC_FLAG&action=edit&redlink=1) is set to -2, 2, -4, or 4 in the [fort.15 file](/Fort.15_file).` (5). |
| 7–9 | File Format — 절 제목과 편집 링크(7)를 포함한다. 상세 형식은 fort.36 file format 문서를 참조한다(9). 원문: `See [fort.36 file format](/Fort.36_file_format) for details.` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `RES_BC_FLAG` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
