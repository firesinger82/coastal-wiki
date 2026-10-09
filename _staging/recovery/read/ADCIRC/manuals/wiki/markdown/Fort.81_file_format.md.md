---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.81_file_format.md
lines: 24
sha256: fc4325ab201ced973d9894b9a2cd5ffdfec32bce432ae23d82398c770ce60ccf
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.81_file_format.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.81 file format — 제목과 판본 표기 `_revid=660_`(1–3)을 포함한다. 각 출력 행을 변수 이름으로 나타내며 빈 줄은 가독성을 위한 것이라고 설명한다(5). 반복문(loop)은 여러 출력 행을 나타낸다(5). |
| 7–19 | 파일 구조 — 실행 설명·실행 식별자·격자 이름의 첫 행과 자료 수·관측소 수·출력 간격을 포함하는 둘째 행을 제시한다(7–9). 자료 집합마다 시각과 단계 번호를 쓰며 각 관측소마다 농도(concentration)를 쓴다(11–18). 파일 형식 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NTRSPC](/index.php?title=NTRSPC&action=edit&redlink=1), [NSTAC](/index.php?title=NSTAC&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLC](/index.php?title=NSPOOLC&action=edit&redlink=1), [NSPOOLC](/index.php?title=NSPOOLC&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `for j=1, [NTRSPC](/index.php?title=NTRSPC&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NSTAC](/index.php?title=NSTAC&action=edit&redlink=1)` (14); `k, [CC00(k)](/index.php?title=CC00(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop` (18). |
| 20–24 | Notes — 출력 형식은 fort.15의 NOUTC 설정에 따라 ASCII 또는 이진(binary)일 수 있다(22). 이진 출력이면 관측소 번호 k를 포함하지 않는다(24). 적용 조건 원문: `Output may be in ascii or binary format depending on how [NOUTC](/index.php?title=NOUTC&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file_format)` (22); `If binary output is specified, the station number (k) is not included in the output.` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7–15·22행: 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다. 이 파일은 해당 변수 참조의 정의를 포함하지 않는다.
