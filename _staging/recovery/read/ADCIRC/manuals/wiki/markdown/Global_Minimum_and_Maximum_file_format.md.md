---
file: models/ADCIRC/raw/manuals/wiki/markdown/Global_Minimum_and_Maximum_file_format.md
lines: 31
sha256: 0bb00455fb6a831f71b3f5235105278826e9671148d1ab0a578f837413d35bb7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Global_Minimum_and_Maximum_file_format.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Global Minimum and Maximum file format — 제목과 판본 표기 `_revid=626_`(1–3)을 포함한다. 각 출력 행의 변수 이름과 반복문(loop)으로 파일 구조를 나타내며 빈 줄은 가독성을 위한 것이라고 설명한다(5). |
| 7–26 | 파일 구조 — 실행 정보 다음에 자료 집합 수를 2로 쓰는 행을 제시한다(7–9). TIME·IT 다음에 모든 절점(node)의 extreme(k)를 쓰는 반복문이 있다(11–17). 둘째 TIME·IT 다음에는 모든 절점의 time_of_extreme(k)를 쓰는 반복문이 있다(19–25). 파일 형식 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `2, [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (11); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (13); `k, extreme(k)` (15); `end k loop` (17); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (19); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (21); `k, time_of_extreme(k)` (23); `end k loop` (25). |
| 27–31 | Notes — 출력 형식은 fort.15의 NOUTGE 설정에 따라 ASCII 또는 이진(binary)일 수 있다(29). 이진 출력이면 절점 번호 k를 포함하지 않는다(31). 적용 조건 원문: `Output may be in ascii or binary format depending on how [NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file_format)` (29); `If binary output is specified, the node number (k) is not included in the output.` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7–13·19–21·29행: 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다. 이 파일은 해당 변수 참조의 정의를 포함하지 않는다.
