---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_82.md
lines: 28
sha256: faf48637e9437f1ac846abf776587bfb0eb9837cae50d470db361365d617e37c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_82.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–24 | C82 INPLACE HARMONIC ANALYSIS PARAMETERS — 실행 중 최소제곱 조화 분석(in place least squares harmonic analysis)의 활성화 조건·분석 위치 수·기준 시간 기간(reference time period)의 정수 배수로 표현한 분석 길이를 적는다(10·14–18). 추세 제거(trend removal)와 단일 `TREF` 기간 수면 표고(surface elevation) 분석 옵션을 제시한다(20–22). 설명 없이 남은 주석 값과 주석 표식·빈 줄을 포함한다(11–24). 원문: `C82 INPLACE HARMONIC ANALYSIS PARAMETERS` (10); `\* ISLSHA: 1 FOR IN PLACE LEAST SQUARES HARMONIC ANALYSIS` (14); `\* MLLSHA: NUMBER OF LOCATIONS FOR LSHA` (16); `\* NTCLSHA: LENGTH OF LSHA IN INTEGER NUMBER OF REFERENCE TIME PERIODS` (18); `\* ISLSTR: 1 FOR TREND REMOVAL` (20); `\* ISHTA : 1 FOR SINGLE TREF PERIOD SURFACE ELEV ANALYSIS` (22); `\*                           90` (24). |
| 25–28 | C82 입력 예시 — 입력 열 제목과 수치 값 행을 제시한다(26·28). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(25·27). 원문: `C82 ISLSHA MLLSHA NTCLSHA ISLSTR ISHTA` (26); `             0          0            32              0          0` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22행: 단일 `TREF` 기간을 언급하지만 이 파일에는 `TREF`의 정의가 없다.
- 24행: 이름이나 설명이 없는 주석 값 `90`이 있다.

