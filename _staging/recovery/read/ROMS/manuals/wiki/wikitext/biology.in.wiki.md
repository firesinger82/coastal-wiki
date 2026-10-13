---
file: models/ROMS/raw/manuals/wiki/wikitext/biology.in.wiki
lines: 15
sha256: b5dcebe013842992c9831efd6793f07f82a15c653a3c882f6b7dea9fa08a2e8e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# biology.in.wiki — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Biological Model Input Scripts / 도입 — 각 생물 모델(biological model)은 서로 다른 매개변수를 요구한다고 적는다(3). BPARNAM 지정과 해당 CPP 옵션 활성화를 모두 요구한다(3). EcoSim 설정 예제를 원문 그대로 인용한다(3). 입력 문법 링크를 포함한다(6). 원문: `ROMS has several biological models and each model requires different parameters. The name of the biological parameter input file is set by the [[Variables#bparnam\|BPARNAM]] keyword in the [[roms.in]] file. Template standard input ASCII files for each of the biological models can be found in the '''User/External''' subdirectory of the ROMS source code. In order to include a biological model in ROMS you must set [[Variables#bparnam\|BPARNAM]] correctly and activate the corresponding [[Options\|CPP option]]. For example, if you wish to include the '''EcoSim''' model you must set [[Variables#bparnam\|BPARNAM]] to point your [[ecosim.in]] file '''and''' you must activate the [[ECOSIM]] [[Options\|CPP option]].` (3). |
| 8–15 | Current Biological Models — 문서는 생물 모델별 입력 문서 여섯 개를 연결한다(8–15). 목록 값을 원문 그대로 인용한다(10–15). 원문: `*[[bio_Fennel.in]]` (10); `*[[ecosim.in]]` (11); `*[[nemuro.in]]` (12); `*[[npzd_Franks.in]]` (13); `*[[npzd_iron.in]]` (14); `*[[npzd_Powell.in]]` (15). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
