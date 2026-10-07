---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_2.md
lines: 64
sha256: b4135a48723c32d9a96812747fc9526bef5c38943819a3d1be48376ad50ff103
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_2.md — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C2 — 원문 frontmatter의 페이지 식별자·제목·space·URL·판본·갱신 시각·분류 경로를 읽었다(1–9). 재시작(restart), 일반 제어(general control), 진단(diagnostics) 스위치 제목을 제시한다(10). 빈 줄과 주석 표식을 포함한다(11–13). 원문: ` C2 RESTART, GENERAL CONTROL AND AND DIAGNOSTIC SWITCHES ` (10). |
| 14–35 | 재시작 제어 — 초기조건(initial conditions) 읽기, 하상 표고(bottom elevation) 변경 조정, 이전 형식 재시작 파일 읽기를 구분한다(14–18). 실행 종료 또는 참조 시간 주기(reference time period)마다 재시작 파일을 쓰는 조건을 제시한다(22–24). 잔여 수송(residual transport), 날짜가 붙은 재시작 파일, EE 연결 파일(EE linkage files)의 실행 연속(run continuation) 설정을 설명한다(26–34). 원문: ` \* ISRESTI: 1 FOR READING INITIAL CONDITIONS FROM FILE restart.inp ` (14); ` \*               -1 AS ABOVE BUT ADJUST FOR CHANGING BOTTOM ELEVATION ` (16); ` \*              10 FOR READING IC'S FROM restart.inp WRITTEN BEFORE 8 SEPT 92 ` (18); ` \* ISRESTO: -1 FOR WRITING RESTART FILE restart.out AT END OF RUN ` (22); ` \* N INTEGER.GE.0 FOR WRITING restart\*.out EVERY N REF TIME PERIODS ` (24); ` \* ISRESTR: 1 FOR WRITING RESIDUAL TRANSPORT FILE RESTRAN.OUT ` (26); ` \* ISGREGOR: 0/1 NOT USE/USE DATE STAMPED RESTART FILES ` (28); ` \* ICONTINUE: RUN CONTINUATION OPTION FOR EE LINKAGE FILES WHEN ISRESTI=1 ` (30); ` \*                    0 NO RUN CONTINUATION - EFDC WRITES EE\_\*.OUT FILES AS USUAL ` (32); ` \*                    1 ACTIVATE RUN CONTINUATION - EE LINKAGE OUTPUT WILL BE APPENDED TO THE EXISTING FILES ` (34). |
| 36–60 | 로그·진단·수지 — 로그 파일과 미사용 항목을 제시한다(36–38). 외부 모드(external mode) 발산(divergence), 음의 수심(negative depth), 추가 모델 결과 로그, 질량·운동량·에너지 수지(mass, momentum and energy balances), 실행 상태 표시의 활성화 조건과 파일명을 제시한다(44–58). 빈 줄과 주석 표식도 포함한다. 원문: ` \* ISLOG: 1 FOR WRITING LOG FILE EFDC.LOG ` (36); ` \* IDUM: NOT USED ` (38); ` \* ISDIVEX: 1 FOR WRITING EXTERNAL MODE DIVERGENCE TO SCREEN ` (44); ` \* ISNEGH: 1 FOR SEARCHING FOR NEGATIVE DEPTHS AND WRITING TO SCREEN ` (46); ` \* ISMMC: <0 FLAG TO GLOBALLY ACTIVATE WRITING EXTRA MODEL RESULTS LOG FILES ` (48); ` \* ISBAL: 1 FOR ACTIVATING MASS, MOMENTUM AND ENERGY BALANCES AND ` (52); ` \* WRITING RESULTS TO FILE bal.out ` (54); ` \* IDUM: NOT USED ` (56); ` \* ISHOW: >0 TO SHOW RUNTIME STATUS ON SCREEN, SEE INSTRUCTIONS FOR FILE SHOW.INP ` (58). |
| 61–64 | C2 입력 예시 — 매개변수 열 순서(62)와 대응 값(64)을 제시한다. 이 값들은 입력 예시이며 원문은 이 줄을 기본값 목록으로 표시하지 않는다. 원문: ` C2 ISRESTI     ISRESTO      ISRESTR      ISGREGOR     ISLOG     ISDIVEX     ISNEGH     ISMMC     ISBAL     ICONTINUE     ISHOW ` (62); `          0                1                   0                   0                   0               0                0               0              1               0                  1 ` (64). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
