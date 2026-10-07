---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_84.md
lines: 42
sha256: 2453fd89bd57755bb422c52806116af13a36795688b7fea24e911ef8d584f82a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_84.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–30 | C84 CONTROLS FOR WRITING TO TIME SERIES FILES / 활성화·간격 — 시계열(time series) 파일에 수면 표고(surface elevation)·속도(velocity)·순 내부 및 외부 모드 체적 생성·소멸(net internal and external mode volume source-sink)·농도 변수를 출력하는 옵션과 기존 파일에 덧붙이는 옵션을 적는다(14–18). 수평 출력 위치 수를 정의한다(20–22). 출력 시작·종료 시간 단계(time step) 설정은 비활성이라고 적는다(24–26). 출력 사이에 건너뛸 시간 단계 수와 시작·종료 시나리오(start-stop scenario) 수의 조건을 제시한다(28–30). 주석 표식과 빈 줄을 포함한다(11–30). 원문: `C84 CONTROLS FOR WRITING TO TIME SERIES FILES` (10); `\* ISTMSR: 1 OR 2 TO WRITE TIME SERIES OF SURF ELEV, VELOCITY, NET` (14); `\*                INTERNAL AND EXTERNAL MODE VOLUME SOURCE-SINKS, AND` (16); `\*                CONCENTRATION VARIABLES, 2 APPENDS EXISTING TIME SERIES FILES` (18); `\* MLTMSR: NUMBER HORIZONTAL LOCATIONS TO WRITE TIME SERIES OF SURF ELEV,` (20); `\* VELOCITY, AND CONCENTRATION VARIABLES` (22); `\* NBTMSR: TIME STEP TO BEGIN WRITING TO TIME SERIES FILES (Inactive)` (24); `\* NSTMSR: TIME STEP TO STOP WRITING TO TIME SERIES FILES (Inactive)` (26); `\* NWTMSR: NUMBER OF TIME STEPS TO SKIP BETWEEN OUTPUT` (28); `\* NTSSTSP: NUMBER OF TIME SERIES START-STOP SCENARIOS, 1 OR GREATER` (30). |
| 31–38 | C84 CONTROLS FOR WRITING TO TIME SERIES FILES / 시간 단위 — 시계열 시각의 단위 변환(unit conversion) 인자를 정의한다(32–34). 초·분·시간·일과 각 변환 값의 대응을 원문 그대로 옮긴다(32–34). 반복 주석 표식과 빈 줄을 포함한다(31–38). 원문: `\* TCTMSR: UNIT CONVERSION FOR TIME SERIES TIME. FOR SECONDS, MINUTES,` (32); `\*                  HOURS,DAYS USE 1.0, 60.0, 3600.0, 86400.0 RESPECTIVELY` (34). |
| 39–42 | C84 입력 예시 — 입력 열 제목과 수치 값 행을 제시한다(40·42). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(39·41). 원문: `C84 ISTMSR MLTMSR NBTMSR NSTMSR NWTMSR NTSSTSP TCTMSR` (40); `           0             0              0             0               1             0            86400` (42). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 30·40·42행: `NTSSTSP` 설명은 `1 OR GREATER`로 적지만 예시 값 행의 해당 열은 `0`이다.

