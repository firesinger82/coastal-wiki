---
file: models/ADCIRC/raw/manuals/wiki/markdown/NOLIFA.md
lines: 45
sha256: 6b4f819799659b95e3fe7c3bef88d265918fde0479b3c78a8a45f23cb3f97323
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# NOLIFA.md — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | NOLIFA / Parameter Summary — NOLIFA는 fort.15에서 유한 진폭 항(finite amplitude terms)과 습윤·건조(wetting-drying)를 제어한다(5). H0의 의미와 함께 지정할 추가 입력에 영향을 준다고 적는다(5). 제목·판본·표의 열 제목·빈 줄을 포함한다(1–18). 원문: `NOLIFA is a parameter in the [fort.15 file](/Fort.15_file) controlling controlling the finite amplitude terms and wetting-drying in ADCIRC. The value of NOLIFA effects the meaning of the minimum water depth parameter ([H0](/index.php?title=H0&action=edit&redlink=1)) and requires the specification of additional parameters together with [H0](/index.php?title=H0&action=edit&redlink=1). ` (5). |
| 19–26 | Parameter Summary / 값 0 — 유한 진폭 항과 습윤·건조를 사용하지 않는다(19–21). 연속방정식(continuity equation)의 과도 항(transient term)을 제외한 모든 항에서 전체 수심 대신 지형 수심(bathymetric depth)을 쓴다(23). 초기 수심은 fort.14 수심과 같다고 가정한다(23). H0와 NOLICA=0을 입력으로 제시한다(25). 원문: `0` (19); `No finite amplitude terms and no wetting-drying` (21); `The depth is linearized by using the bathymetric depth, rather than the total depth, in all terms except the transient term in the continuity equation. Wetting and drying of elements is disabled. Initial water depths are assumed equal to the bathymetric water depth specified in the [fort.14 file](/Fort.14_file).` (23); `[H0](/index.php?title=H0&action=edit&redlink=1), [NOLICA](/index.php?title=NOLICA&action=edit&redlink=1) = 0` (25). |
| 27–34 | Parameter Summary / 값 1 — 유한 진폭 항을 포함하고 요소(element)의 습윤·건조는 사용하지 않는다(27–31). 초기 수심은 fort.14 수심과 같다고 가정한다(31). H0와 NOLICA=1을 입력으로 제시한다(33). 원문: `1` (27); `Finite amplitude terms without wetting-drying` (29); `Finite amplitude terms are included in the model run and wetting and drying of elements is disabled. Initial water depths are assumed equal to the bathymetric water depth specified in the [fort.14 file](/Fort.14_file).` (31); `[H0](/index.php?title=H0&action=edit&redlink=1), [NOLICA](/index.php?title=NOLICA&action=edit&redlink=1) = 1` (33). |
| 35–42 | Parameter Summary / 값 2 — 유한 진폭 항과 요소의 습윤·건조를 사용한다(35–39). 초기 수심은 fort.14 수심과 같다고 가정한다(39). H0와 NOLICA=1을 입력으로 제시한다(41). 원문: `2` (35); `Finite amplitude terms with wetting-drying` (37); `Finite amplitude terms are included in the model run and wetting and drying of elements is enabled. Initial water depths are assumed equal to the bathymetric water depth specified in the [fort.14 file](/Fort.14_file).` (39); `[H0](/index.php?title=H0&action=edit&redlink=1), [NOLICA](/index.php?title=NOLICA&action=edit&redlink=1) = 1` (41). |
| 43–45 | Usage Notes — 질량 보존(mass conservation)과 일관성을 위해 유한 진폭 항을 사용하면 이류항(advective terms)의 시간 미분 부분도 사용해야 한다고 적는다(45). 조건과 설정값을 원문 그대로 옮긴다. 원문: `When the finite amplitude terms are turned on, the time derivative portion of the advective terms should also be turned on for proper mass conservation and consistency (i.e., when NOLIFA > 0, then [NOLICA](/index.php?title=NOLICA&action=edit&redlink=1) = 1).` (45). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·25·33·41·45행: H0와 NOLICA 링크에 `action=edit&redlink=1`이 있다.
