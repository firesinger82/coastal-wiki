---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.37_file.md
lines: 9
sha256: 46ff42de2482f3d7b201867ccaa2551eb72e060cb21edaa0dd0638f90d0d456d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.37_file.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | Fort.37 file — 문서 제목(1)과 판본 표기 `_revid=671_` (3)를 포함한다. 빈 줄(2·4)을 포함한다. |
| 5–6 | 온도 경계조건(temperature boundary condition) 입력 — fort.37는 온도 경계조건 입력 파일이다(5). fort.15의 RES_BC_FLAG가 -3, 3, -4 또는 4일 때 읽는다(5). 원문: `The fort.37 file is the Temperature Boundary Condition Input File. It is read in when the [RES_BC_FLAG](/index.php?title=RES_BC_FLAG&action=edit&redlink=1) is set to -3, 3, -4, or 4 in the [fort.15 file](/Fort.15_file).` (5). |
| 7–9 | File Format — 절 제목과 편집 링크(7)를 포함한다. 상세 형식은 fort.37 file format 문서를 참조한다(9). 원문: `See [fort.37 file format](/Fort.37_file_format) for details.` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `RES_BC_FLAG` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
