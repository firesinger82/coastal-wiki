---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.76_file_format.md
lines: 24
sha256: e3097976ffa5500cd622134e349013987140df43f0637be6b0b3064f13f2336f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.76_file_format.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.76 file format / 파일 구조 안내 — 문서 제목(1)과 판본 표기 `_revid=656_` (3)를 포함한다. 원문은 각 출력 줄을 굵은 변수명 줄로 나타낸다고 설명한다(5). 빈 줄은 가독성을 위한 것이라고 설명한다(5). 반복문은 여러 출력 줄을 뜻한다고 설명한다(5). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of output. ` (5). |
| 7–10 | 파일 헤더(header) — 첫 줄은 RUNDES, RUNID, AGRID를 순서대로 나열한다(7). 다음 줄은 NDSETGE, NP, DTDP와 NSPOOLGE의 곱, NSPOOLGE, IRTYPE을 순서대로 나열한다(9). 두 줄 사이와 다음 줄 뒤의 빈 줄(8·10)을 포함한다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NDSETGE](/index.php?title=NDSETGE&action=edit&redlink=1), [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9). |
| 11–19 | 반복 출력 형식 — j 반복문은 NDSETGE를 사용한다(11). 이 반복문 안에 TIME, IT 줄과 NP를 사용하는 k 반복문을 둔다(13–14). 절점(node)별 자료 줄은 k, DP(k) 순서다(15). 반복문 종료 줄(16·18)과 빈 줄(12·17·19)을 포함한다. 원문: `for j=1, [NDSETGE](/index.php?title=NDSETGE&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (14); `k, [DP(k)](/index.php?title=DP(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop ` (18). |
| 20–24 | Notes — 모델 매개변수 및 주기 경계조건 파일(Model Parameter and Periodic Boundary Condition File)의 NOUTGE 설정에 따라 출력은 ASCII(ascii) 또는 이진(binary) 형식일 수 있다(22). 이진 출력을 지정하면 절점(node) 번호 k는 출력에 포함하지 않는다(24). 원문: `Output may be in ascii or binary format depending on how [NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1) is set in the Model Parameter and Periodic Boundary Condition File` (22); `If binary output is specified, the node number (k) is not included in the output.` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·7·9·11·13–15: 5행은 변수명이 `bold face type`이라고 설명한다. 형식 줄의 변수 링크에는 굵게 표시하는 Markdown 표기가 없다.
- 7·9·11·13–15·22: `RUNDES`, `RUNID`, `AGRID`, `NDSETGE`, `NP`, `NSPOOLGE`, `IRTYPE`, `TIME`, `IT`, `DP(k)`, `NOUTGE` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 7·9·13·15: `RUNDES`, `RUNID`, `AGRID`, `NDSETGE`, `NP`, `DTDP`, `NSPOOLGE`, `IRTYPE`, `TIME`, `IT`, `DP(k)`의 개별 정의·단위·기본값은 이 파일에 없다.
