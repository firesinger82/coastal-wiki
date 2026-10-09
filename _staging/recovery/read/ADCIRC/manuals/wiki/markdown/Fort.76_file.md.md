---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.76_file.md
lines: 9
sha256: 1478045f625542dfe4acd50487909dc0e57082e35e3ba720490d35d5d06855c1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.76_file.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | Fort.76 file — 문서 제목(1)과 판본 표기 `_revid=655_` (3)를 포함한다. 빈 줄(2·4)을 포함한다. |
| 5–6 | 시간 변화 수심 지형(time varying bathymetry) 출력 조건 — 이 기능을 활성화하면 fort.76 출력 파일을 생성한다(5). 출력은 fort.15에 지정된 전체 영역(full domain)의 시간 변화 수위(water surface elevation) 출력 제어 설정 NOUTGE 등을 따른다(5). 원문: `If the time varying bathymetry feature of ADCIRC has been activated, the fort.76 output file will be produced according to the output control specifications for full domain time varying water surface elevation output ([NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1), etc) as specified in the [fort.15 file](/Fort.15_file).` (5). |
| 7–9 | File Format — 절 제목과 편집 링크(7)를 포함한다. 상세 형식은 fort.76 file format 문서를 참조한다(9). 원문: `See [fort.76 file format](/Fort.76_file_format) for details.` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `NOUTGE` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
