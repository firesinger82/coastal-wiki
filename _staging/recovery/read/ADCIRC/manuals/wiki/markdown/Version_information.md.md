---
file: models/ADCIRC/raw/manuals/wiki/markdown/Version_information.md
lines: 16
sha256: d1fa585cc386d1f3069b0e91b71304d67631bd5252abfc0fc3b4a662b389a8f9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Version_information.md — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Version information — 제목과 판본 표기를 포함한다(1–3). ADCIRC가 버전 관리(version control)에 Git을 사용하며 공개 GitHub 저장소에 호스팅된다고 적는다(5). 배포판 패키지를 만들 때 버전 정보가 자동으로 생성된다고 설명한다(5). 배포판 패키지를 사용하지 않으면 Git으로 버전을 추적해야 한다고 설명한다(5). |
| 7–13 | Major Model Updates / Version 53 — SWAN 41.01의 Patch B, 즉 41.01B가 ADCIRC에 병합되었다고 설명한다(11). 갱신된 SWAN 수치해법으로 인해 `Wave refraction in SWAN` 절점 속성(nodal attribute)과 SWAN 스펙트럼 제한자(spectral limiters)가 더 이상 필요하지 않아야 한다고 설명한다(12). 상세 설명 링크를 포함한다(12). 원문: `- Patch B of SWAN version 41.01 (i.e. version 41.01B) was merged into ADCIRC.` (11); `[Wave refraction in SWAN](/index.php?title=Wave_refraction_in_SWAN&action=edit&redlink=1) nodal attribute and SWAN spectral limiters should no longer be needed due to updated numerics in SWAN.  [Details here](https://ccht.ccee.ncsu.edu/updates-to-spectral-propagation-velocities/).` (12). |
| 14–16 | Later Versions — 이후 버전의 배포판에는 GitHub의 배포판 페이지에서 배포 안내(release notes)가 함께 제공된다고 설명한다(16). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: `Wave refraction in SWAN` 참조에는 `redlink=1`이 표시되어 있다.
