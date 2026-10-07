---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_45.md
lines: 55
sha256: c3f02301c04c4f2072ed1a590a11b5706a06f493b4c0930a34f68ad2f2cae51a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_45.md — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31817751(2), 제목 Card Image 45(3), space ECIG(4), 원문 URL(5), 버전 2(6), 수정 시각 2018-01-11T08:23:13.002Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–22 | C45 TOXIC CONTAMINANT SEDIMENT INTERACTION PARAMETERS — 독성 오염물질(toxic contaminant)과 퇴적물(sediment)의 상호작용을 다룬다(10). 오염물질 번호, 오염물질마다 반복하는 데이터 행수, 점착성(cohesive)·비점착성(non-cohesive) 퇴적물 행 순서를 설명한다(16–22). 이름·행수·기본값 문구 원문: `\* NTOXC: TOXIC CONTAMINANT NUMBER ID. NSEDC+NSEDN LINES OF DATA` (16); `\*               FOR EACH TOXIC CONTAMINANT (DEFAULT = 2)` (18); `\* NSEDN/NSNDN: FIRST NSED LINES COHESIVE, NEXT NSND LINES NON-COHESIVE.` (20); `\*                           REPEATED FOR EACH CONTAMINANT` (22). |
| 23–42 | 수주·퇴적층 분배 매개변수 — 수주(water column) 분배(partitioning)의 정상 옵션과 고형물 의존 옵션 및 계수·지수식을 제시한다(24–32). 퇴적층(sediment bed)의 ITXPARB와 CONPARB를 Not Used로 적고 TOXPARB의 조건·단위를 설명한다(34–40). 이름·적용 조건·단위·식과 별도 수치 주석 원문: `\* ITXPARW: O FOR NORMAL WC PARTITIONING` (24); `\*                   1 FOR SOLIDS DEPENDENT WC PARTITIONING TOXPAR=PARO\*(CSED\*\*CONPAR)` (26); `\* TOXPARW: WATER COLUMN PARO (ITXPARW=1) OR EQUIL TOX CON PART COEFF BETWEEN` (28); `\*                    EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (LITERS/MG)` (30); `\* CONPARW: EXPONENT IN TOXPAR=PARO\*(CSED\*\*CONPARW) IF ITXPARW=1` (32); `\* ITXPARB: Not Used` (34); `\* TOXPARB: SEDIMENT BED PARO (ITXPARB=1) OR EQUIL TOX CON PART COEFF BETWEEN` (36); `\*                   EACH TOXIC IN WATER AND ASSOCIATED SEDIMENT PHASES (LITERS/MG)` (38); `\* CONPARB: Not Used` (40); `\*                                                 1                   0.8770            -0.943                                   0.025` (42). |
| 43–55 | C45 입력 표 — 빈 줄·표 마크업과 아홉 입력 행을 포함한다(43–55). 세 오염물질 번호마다 세 퇴적물 번호 행을 제시한다(47–55). 이 표의 수치를 기본값으로 표시하지 않는다. 머리글·입력 행 원문: `\| C45 \| NTOXN \| NSEDN \| ITXPARW \| TOXPARW \| CONPARW \| ITXPARB \| TOXPARB \| CONPARB \|` (46); `\|  \| 1 \| 1 \| 1 \| 0.00291 \| 1 \| 0 \| 0.0218 \| 0 \|` (47); `\|  \| 1 \| 2 \| 1 \| 0.00291 \| 1 \| 0 \| 0.0218 \| 0 \|` (48); `\|  \| 1 \| 3 \| 1 \| 0.00291 \| 1 \| 0 \| 0.0218 \| 0 \|` (49); `\|  \| 2 \| 1 \| 0 \| 0.000983 \| 0 \| 0 \| 0.00737 \| 0 \|` (50); `\|  \| 2 \| 2 \| 0 \| 0.000983 \| 0 \| 0 \| 0.00737 \| 0 \|` (51); `\|  \| 2 \| 3 \| 0 \| 0.000983 \| 0 \| 0 \| 0.00737 \| 0 \|` (52); `\|  \| 3 \| 1 \| 1 \| 0.000062 \| 1 \| 0 \| 0.00007 \| 0 \|` (53); `\|  \| 3 \| 2 \| 1 \| 0.000062 \| 1 \| 0 \| 0.00007 \| 0 \|` (54); `\|  \| 3 \| 3 \| 1 \| 0.000062 \| 1 \| 0 \| 0.00007 \| 0 \|` (55). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·46: 본문 오염물질 번호의 이름은 `NTOXC`이다(16). 표 머리글은 `NTOXN`이다(46). 두 표기의 대응 설명은 이 파일에 없다.
- 16·20: 데이터 행수 문구는 `NSEDC+NSEDN LINES OF DATA`이다(16). 행 순서 문구에는 `NSED`와 `NSND`가 있다(20). `NSEDC`의 별도 정의는 이 파일에 없다.
- 24: 정상 수주 분배의 옵션 값은 문자 `O`로 적혀 있다.
- 34·36: `ITXPARB`는 `Not Used`로 적혀 있다(34). `TOXPARB` 설명에는 `(ITXPARB=1)` 조건이 있다(36).
- 26·32: 식에는 `TOXPAR`, `CSED`, `CONPAR`가 있다. 이 파일에는 이 기호들의 별도 정의가 없다.
- 42: 주석 줄에 `1`, `0.8770`, `-0.943`, `0.025`가 있다. 이 줄의 값에 연결되는 열 이름이나 설명은 없다.

