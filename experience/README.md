# experience/

## 현재 항목 (verified)

| 파일 | 주제 | 검증일 |
|---|---|---|
| `khoa-multi-station-tide-validation-2026.md` | UTide 15정점 1년 조화분해 검증 (median 0.057%, max 0.30%) | 2026-05-21 |
| `khoa-annual-climate-trend.md` | KHOA 14년 백서 → 한국 연안 SLR 2007-2025 (한국 평균 3.94 mm/yr, 서귀포 5.42 max) | 2026-05-23 |
| `khoa-sst-warming-trend.md` | KHOA 9년 SST trend 2017-2025 (한국 평균 1.39 °C/decade, 서귀포·제주 max) + SLR 정합성 + 1968-2012 KHOA 공식 reference (11× 가속) | 2026-05-23 |
| `khoa-sst-global-crosscheck.md` | OISST v2.1 + HadISST + COBE-SST2 + NIFS KODC raw vs KHOA — 5-source cross-check. 2017-2025 ~1.25 °C/dec 일치, 1968-2022 HadISST 0.27 ≈ NIFS raw 0.19, 1850-2025 baseline 0.064 | 2026-05-23 |
| `nifs-vertical-sst-trends.md` | NIFS 다층 수온 trend 1968-2025 (surface +0.30, 100m +0.13, 200m -0.59 °C/dec) + 동해 100m cooling 신호 + thermosteric SLR ~10% | 2026-05-23 |

## 들어가는 것

모델링·실무에서 얻은 통찰 중 **3조건 모두 만족하는 것만**:

1. **반복 관찰** — 같은 패턴이 최소 2번 이상 독립적으로 관측됨
2. **객관 데이터 근거** — 단지 직관이 아닌 측정·수치 결과 첨부
3. **재현 가능** — 다른 사람이 같은 조건으로 결과를 얻을 수 있음

세 조건 중 하나라도 불충족 시 여기 들어갈 자격 없음.

## 들어가지 않는 것

- 한 번 본 케이스
- "기분상" 추정
- 검증 없는 직관
- 특정 프로젝트의 사적 산출 (해당 프로젝트 폴더에 두기)

## 구조 (도입 시)

```
experience/
├── failure-patterns/    # 반복 관찰된 실패 패턴
├── heuristics/          # 검증된 운영 휴리스틱
└── playbooks/           # 재현 가능한 작업 절차
```

(기존 `D:\modeling-wiki/`에 이미 비슷한 구조가 있음. 객관 레이어 정착 후 통합 여부 결정.)

## 객관 레이어로 승급

`experience/` 항목이 한 번 더 검증되어 "도메인 일반 지식"으로 강화되면 `concepts/<topic>/`로 이동.
