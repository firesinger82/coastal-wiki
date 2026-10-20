---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/windows_ext.h
lines: 14
sha256: 7b076269c311c80dffbb823ef3fe5df9d9f091267507a96e675631c1bd5d8b08
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# windows_ext.h — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | LIS_WINDOWS_EXT_H_가 정의되지 않은 경우에만 헤더를 처리하고 같은 이름의 포함 방지 매크로(include guard)를 정의한다(1–2·14). 그 조건 안에서 windows.h를 포함한다(4). timezone 구조체는 그리니치 서쪽 분·일광절약시간(daylight saving time) 보정 종류의 int 필드 두 개를 선언한다(6–10). gettimeofday는 timeval·timezone 포인터를 받고 int를 반환하는 원형만 선언한다(12). 기본값·계산식·실행 분기는 없다. 원문 조건·식·지시: `#ifndef LIS_WINDOWS_EXT_H_` (1), `#define LIS_WINDOWS_EXT_H_` (2), `#endif` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
