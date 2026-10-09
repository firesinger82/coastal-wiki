---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.64_file_format.md
lines: 24
sha256: c91f46cc6d26db8f528250b957d120b81aca06236bdd497a5eefb076a823b2e1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.64_file_format.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.64 file format / 파일 구조 안내 — 문서 제목(1)과 판본 표기 `_revid=646_` (3)를 포함한다. 원문은 각 출력 줄을 굵은 변수명 줄로 나타낸다고 설명한다(5). 빈 줄은 가독성을 위한 것이라고 설명한다(5). 반복문은 여러 출력 줄을 뜻한다고 설명한다(5). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of output. ` (5). |
| 7–10 | 파일 헤더(header) — 첫 줄은 RUNDES, RUNID, AGRID를 순서대로 나열한다(7). 다음 줄은 NDSETSV, NP, DTDP와 NSPOOLGV의 곱, NSPOOLGV, IRTYPE을 순서대로 나열한다(9). 두 줄 사이와 다음 줄 뒤의 빈 줄(8·10)을 포함한다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NDSETSV](/index.php?title=NDSETSV&action=edit&redlink=1), [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGV](/index.php?title=NSPOOLGV&action=edit&redlink=1), [NSPOOLGV](/index.php?title=NSPOOLGV&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9). |
| 11–19 | 반복 출력 형식 — j 반복문은 NDSETSV를 사용한다(11). 이 반복문 안에 TIME, IT 줄과 NP를 사용하는 k 반복문을 둔다(13–14). 절점(node)별 자료 줄은 k, UU2(k), VV2(k) 순서다(15). 반복문 종료 줄(16·18)과 빈 줄(12·17·19)을 포함한다. 원문: `for j=1, [NDSETSV](/index.php?title=NDSETSV&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (14); `k, [UU2(k)](/index.php?title=UU2(k)&action=edit&redlink=1), [VV2(k)](/index.php?title=VV2(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop` (18). |
| 20–24 | Notes — 모델 매개변수 및 주기 경계조건 파일(Model Parameter and Periodic Boundary Condition File)의 NOUTGV 설정에 따라 출력은 ASCII(ascii) 또는 이진(binary) 형식일 수 있다(22). 이진 출력을 지정하면 절점(node) 번호 k는 출력에 포함하지 않는다(24). 원문: `Output may be in ascii or binary format depending on how [NOUTGV](/index.php?title=NOUTGV&action=edit&redlink=1) is set in the Model Parameter and Periodic Boundary Condition File` (22); `If binary output is specified, the node number (k) is not included in the output.` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·7·9·11·13–15: 5행은 변수명이 `bold face type`이라고 설명한다. 형식 줄의 변수 링크에는 굵게 표시하는 Markdown 표기가 없다.
- 7·9·11·13–15·22: `RUNDES`, `RUNID`, `AGRID`, `NDSETSV`, `NP`, `NSPOOLGV`, `IRTYPE`, `TIME`, `IT`, `UU2(k)`, `VV2(k)`, `NOUTGV` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 7·9·13·15: `RUNDES`, `RUNID`, `AGRID`, `NDSETSV`, `NP`, `DTDP`, `NSPOOLGV`, `IRTYPE`, `TIME`, `IT`, `UU2(k)`, `VV2(k)`의 개별 정의·단위·기본값은 이 파일에 없다.
