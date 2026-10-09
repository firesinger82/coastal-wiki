---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.10_file.md
lines: 35
sha256: 5b337a406d3e015aa90c3bd73553fcf5ad697a4028d753d8046a9773d5b65790
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.10_file.md — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 제목·판본 표기·빈 줄을 포함한다(1–4). Fort.10 file — 수동 스칼라 수송(passive scalar transport)에 필요한 농도장을 담는다고 설명한다(5). |
| 7–10 | File Format — 입력의 각 줄을 변수 이름으로 표현하며 빈 줄은 가독성용이고 반복문은 여러 입력 줄을 뜻한다고 설명한다(9). |
| 11–22 | File structure for a 2DDI run — 헤더 두 줄, `NVP`, `k=1`부터 `NVP`까지의 `jki`·`DACONC(jki)` 입력 구조를 원문 그대로 옮긴다(13–21). 원문의 링크 및 백틱 표기도 보존한다. 원문: `` `Header Line 1` `` (13); `` `Header Line 2` `` (15); `` `[NVP](/index.php?title=NVP&action=edit&redlink=1)` `` (17); `for k=1 to [NVP](/index.php?title=NVP&action=edit&redlink=1)` (19); `` [jki](/index.php?title=Jki&action=edit&redlink=1),`[DACONC(jki)](/index.php?title=DACONC(jki)&action=edit&redlink=1)` `` (20); `end k loop` (21). |
| 23–35 | File structure for a 3D run — 헤더 두 줄, `NVN`·`NVP`, `k`·`j`의 중첩 반복문과 `NHNN`·`NVNN`·`CONC(NHNN,NVNN)` 입력 구조를 원문 그대로 옮긴다(25–35). 원문: `` `Header Line 1` `` (25); `` `Header Line 2` `` (27); `` `[NVN](/index.php?title=NVN&action=edit&redlink=1)`, `[NVP](/index.php?title=NVP&action=edit&redlink=1)` `` (29); `for k=1 to [NVP](/index.php?title=NVP&action=edit&redlink=1)` (31); `for j=1 to [NVN](/index.php?title=NVN&action=edit&redlink=1)` (32); `` `[NHNN](/index.php?title=NHNN&action=edit&redlink=1)`,`[NVNN](/index.php?title=NVNN&action=edit&redlink=1)`,`[CONC(NHNN,NVNN)](/index.php?title=CONC(NHNN,NVNN)&action=edit&redlink=1)` `` (33); `end j loop` (34); `end k loop` (35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 17·19·20·29·31–33: NVP·jki·DACONC(jki)·NVN·NHNN·NVNN·CONC(NHNN,NVNN) 링크에는 `action=edit&redlink=1`이 붙어 있다.
