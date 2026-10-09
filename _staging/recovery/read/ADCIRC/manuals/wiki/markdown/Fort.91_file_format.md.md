---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.91_file_format.md
lines: 22
sha256: 4ee5fa669b41c2f258a67a966782fa7c70283b560552be61f451906f75cf74f0
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.91_file_format.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.91 file format — 제목과 판본 표기 `_revid=666_`(1–3)을 포함한다. 각 출력 행의 변수 이름과 반복문으로 파일 구조를 나타내며 빈 줄은 가독성을 위한 것이라고 설명한다(5). |
| 7–19 | 파일 구조 — 실행 정보 다음에 자료 집합 수·기상 관측소 수·출력 간격을 제시한다(7–9). 각 자료 집합에서 TIME·IT 다음에 각 관측소의 RMICE00(k)를 쓴다(11–18). 파일 형식 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NDSET](/index.php?title=NDSET&action=edit&redlink=1), [NSTAM](/index.php?title=NSTAM&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLM](/index.php?title=NSPOOLM&action=edit&redlink=1), [NSPOOLM](/index.php?title=NSPOOLM&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `for j=1, [NDSET](/index.php?title=NDSET&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NSTAM](/index.php?title=NSTAM&action=edit&redlink=1)` (14); `k, [RMICE00(k)](/index.php?title=RMICE00(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop` (18). |
| 20–22 | Notes — 출력 형식은 fort.15의 NOUTM 설정에 따라 ASCII 또는 이진(binary)일 수 있다(22). 적용 조건 원문: `Output may be in ascii or binary format depending on how [NOUTM](/index.php?title=NOUTM&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file_format)` (22). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7–15·22행: 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다. 이 파일은 해당 변수 참조의 정의를 포함하지 않는다.
