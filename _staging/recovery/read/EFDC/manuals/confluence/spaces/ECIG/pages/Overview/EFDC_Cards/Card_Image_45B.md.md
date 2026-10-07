---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_45B.md
lines: 52
sha256: 96f19eda1613e1244390a9b8aab961dde6fe4e103ebb045d6ddddc329e2a358b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_45B.md — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31752223(2), 제목 Card Image 45B(3), space ECIG(4), 원문 URL(5), 버전 2(6), 수정 시각 2018-01-11T08:51:15.490Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–22 | C45B TOXIC CONTAMINANT NON-SEDIMENT BASED ORGANIC CARBON (OC) INTERACTION PARAMETERS — 퇴적물에 기반하지 않는 유기탄소(organic carbon, OC) 상호작용을 다룬다(10). 각 독성 오염물질(toxic contaminant)에 대해 용존 유기탄소(dissolved organic carbon, DOC) 행을 먼저, 입자상 유기탄소(particulate organic carbon, POC) 행을 다음에 둔다(16–22). 이름·입력 순서 원문: `\* NTOXC: TOXIC CONTAMINANT NUMBER ID. FOR EACH TOXIC CONTAMINANT` (16); `\* NOC : FIRST LINE FOR DISSOLVED ORGANIC CARBON (DOC)` (18); `\*            SECOND LINE FOR PARTICULATE ORGANIC CARBON (POC)` (20); `\*                REPEATED FOR EACH CONTAMINANT` (22). |
| 23–42 | 분배 매개변수 — 수주(water column)의 정상 분배(partitioning)·고형물 의존 분배와 계수·지수식을 적는다(24–32). 퇴적층(sediment bed)의 ITXPARBC와 CONPARBC는 Not Used로 적는다(34·40). 이름·단위·적용 조건·식과 별도 수치 주석을 보정하지 않고 옮긴다(24–42). 원문: `\* ITXPARWC: O FOR NORMAL WC PARTITIONING` (24); `\*                     1 FOR SOLIDS DEPENDENT WC PARTITIONING TOXPAR=PARO\*(CSED\*\*CONPAR)` (26); `\* TOXPARWC: WATER COLUMN PARO (ITXPARW=1) OR EQUIL TOX CON PART COEFF BETWEEN` (28); `\*                       EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (liters/mg)` (30); `\* CONPARWC: EXPONENT IN TOXPAR=PARO\*(CSED\*\*CONPARW) IF ITXPARW=1` (32); `\* ITXPARBC: Not Used` (34); `\* TOXPARBC: SEDIMENT BED PARO (ITXPARB=1) OR EQUIL TOX CON PART COEFF BETWEEN` (36); `\*                      EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (liters/mg)` (38); `\* CONPARBC: Not Used` (40); `\*                                                  1                    0.8770             -0.943                                         0.025` (42). |
| 43–52 | C45B 입력 표 — 빈 줄·표 마크업과 여섯 입력 행을 포함한다(43–52). 각 오염물질 번호마다 NOC 1·2의 두 행을 제시한다(47–52). 마지막 CARBON 열의 입력 칸은 비어 있다(46–52). 표의 수치를 기본값으로 표시하지 않는다. 머리글·입력 행 원문: `\| C45B \| NTOXN \| NOC \| ITXPARWC \| TOXPARWC \| CONPARWC \| ITXPARBC \| TOXPARBC \| CONPARBC \| \*CARBON\* \|` (46); `\|  \| 1 \| 1 \| 1 \| 0.00291 \| 1 \| 0 \| 0.0218 \| 0 \|  \|` (47); `\|  \| 1 \| 2 \| 1 \| 0.00291 \| 1 \| 0 \| 0.0218 \| 0 \|  \|` (48); `\|  \| 2 \| 1 \| 0 \| 0.316 \| 1 \| 0 \| 0.0218 \| 0 \|  \|` (49); `\|  \| 2 \| 2 \| 0 \| 0.000983 \| 0 \| 0 \| 0.00737 \| 0 \|  \|` (50); `\|  \| 3 \| 1 \| 0 \| 0 \| 1 \| 0 \| 0.0218 \| 0 \|  \|` (51); `\|  \| 3 \| 2 \| 0 \| 0 \| 1 \| 0 \| 0.0218 \| 0 \|  \|` (52). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·46: 본문 오염물질 번호의 이름은 `NTOXC`이다(16). 표 머리글은 `NTOXN`이다(46). 두 표기의 대응 설명은 이 파일에 없다.
- 24: 정상 수주 분배의 옵션 값은 문자 `O`로 적혀 있다.
- 24·28·32: 정의된 옵션 이름은 `ITXPARWC`이다(24). `TOXPARWC`와 `CONPARWC`의 적용 조건에는 `ITXPARW=1`이 있다(28·32). `ITXPARW`의 별도 정의는 이 파일에 없다.
- 32: 정의 이름은 `CONPARWC`이다. 같은 줄의 지수식은 `CONPARW`를 사용한다. `CONPARW`의 별도 정의는 이 파일에 없다.
- 34·36: `ITXPARBC`는 `Not Used`로 적혀 있다(34). `TOXPARBC` 설명은 `(ITXPARB=1)`을 사용한다(36). `ITXPARB`의 별도 정의는 이 파일에 없다.
- 10·30·38: 제목은 `NON-SEDIMENT BASED ORGANIC CARBON (OC)`이다(10). 두 계수 설명은 `ASSOCIATED SEDIMENT PHASES`라고 적는다(30·38).
- 26·32: 식에는 `TOXPAR`, `CSED`, `CONPAR`가 있다. 이 파일에는 이 기호들의 별도 정의가 없다.
- 42: 주석 줄에 `1`, `0.8770`, `-0.943`, `0.025`가 있다. 이 줄의 값에 연결되는 열 이름이나 설명은 없다.

