---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.77_file_format.md
lines: 39
sha256: b6fe2ee669f4fbfacf5dbeae2dbd22ca31f5f6479e92827659e7d59f0f903fe6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.77_file_format.md — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.77 file format / 파일 구조 안내 — 문서 제목(1)과 판본 표기 `_revid=658_` (3)를 포함한다. 원문은 각 출력 줄을 굵은 변수명 줄로 나타낸다고 설명한다(5). 빈 줄은 가독성을 위한 것이라고 설명한다(5). 반복문은 여러 출력 줄을 뜻한다고 설명한다(5). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of output. ` (5). |
| 7–10 | 첫 번째 파일 헤더(header) — 첫 줄은 RUNDES, RUNID, AGRID를 나열한다(7). 다음 줄은 NDSETSE, NP, DTDP와 NSPOOL_TVW의 곱, NSPOOL_TVW, IRTYPE을 나열한다(9). 빈 줄(8·10)을 포함한다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NDSETSE](/index.php?title=NDSETSE&action=edit&redlink=1), [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOL_TVW](/index.php?title=NSPOOL_TVW&action=edit&redlink=1), [NSPOOL_TVW](/index.php?title=NSPOOL_TVW&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9). |
| 11–19 | 첫 번째 반복 출력 형식 — j 반복문은 NDSETSE를 사용한다(11). 이 반복문 안에 TIME, IT 줄과 NP를 사용하는 k 반복문을 둔다(13–14). 자료 줄은 k, DP(k) 순서다(15). 반복문 종료 줄(16·18)과 빈 줄(12·17·19)을 포함한다. 원문: `for j=1, [NDSETSE](/index.php?title=NDSETSE&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (14); `k, [DP(k)](/index.php?title=DP(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop ` (18). |
| 20–23 | Notes / 두 번째 파일 구조 안내 — Notes 제목과 편집 링크(20) 뒤에서 5행과 같은 출력 줄·빈 줄·반복문 설명을 다시 적는다(22). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of output. ` (22). |
| 24–27 | 두 번째 파일 헤더 — 첫 줄은 RUNDES, RUNID, AGRID를 나열한다(24). 다음 줄은 NDSETGE, NP, DTDP와 NSPOOLGE의 곱, NSPOOLGE, IRTYPE을 나열한다(26). 빈 줄(25·27)을 포함한다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (24); `[NDSETGE](/index.php?title=NDSETGE&action=edit&redlink=1), [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (26). |
| 28–36 | 두 번째 반복 출력 형식 — j 반복문은 NDSETGE를 사용한다(28). 이 반복문 안에 TIME, IT 줄과 NP를 사용하는 k 반복문을 둔다(30–31). 자료 줄은 k, DP(k) 순서다(32). 반복문 종료 줄(33·35)과 빈 줄(29·34·36)을 포함한다. 원문: `for j=1, [NDSETGE](/index.php?title=NDSETGE&action=edit&redlink=1)` (28); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (30); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (31); `k, [DP(k)](/index.php?title=DP(k)&action=edit&redlink=1)` (32); `end k loop` (33); `end j loop ` (35). |
| 37–39 | Notes / 희소 출력 — 희소 형식(sparse format)으로 쓰여 위어(weir)에 해당하는 소수 절점의 자료만 받는 경우, 번호는 전역 절점 번호(global node number)를 참조한다(39). 기존 fort.14에서 지정한 높이(elevation)로부터의 변화량만 파일에 기록한다(39). 원문: `When this file is written in sparse format and therefore only receiving data for a small portion of the nodes (the weirs) the numbering will be referenced to the global node number. Only the change in elevation from the original fort.14 specified elevation will be written to the file.` (39). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·7–18·22·24–35: 5·22행은 변수명이 `bold face type`이라고 설명한다. 형식 줄의 변수 링크에는 굵게 표시하는 Markdown 표기가 없다.
- 7·9·11·13–15·24·26·28·30–32: `RUNDES`, `RUNID`, `AGRID`, `NDSETSE`, `NP`, `NSPOOL_TVW`, `IRTYPE`, `TIME`, `IT`, `DP(k)`, `NDSETGE`, `NSPOOLGE` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 7·9·24·26: `RUNDES`, `RUNID`, `AGRID`, `NDSETSE`, `NP`, `DTDP`, `NSPOOL_TVW`, `IRTYPE`, `NDSETGE`, `NSPOOLGE`의 개별 정의·단위·기본값은 이 파일에 없다.
- 9·11·26·28: 첫 형식은 `NDSETSE`와 `NSPOOL_TVW`를 사용한다. 두 번째 형식은 `NDSETGE`와 `NSPOOLGE`를 사용한다. 두 형식을 선택하는 조건은 이 파일에 없다.
- 5·20·22·37: 파일 구조 안내 문장은 5·22행에서 반복된다. `Notes` 절 제목은 20·37행에서 반복된다.
