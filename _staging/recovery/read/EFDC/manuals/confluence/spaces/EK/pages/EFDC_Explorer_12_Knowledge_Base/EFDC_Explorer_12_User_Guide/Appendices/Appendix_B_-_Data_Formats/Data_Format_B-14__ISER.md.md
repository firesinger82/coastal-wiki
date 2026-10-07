---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-14__ISER.md
lines: 28
sha256: 5f38cc9be374ca36ac36febad5564b9b94fd6906be83a83954e726b30879a2e0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-14__ISER.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 문서 메타데이터 — 페이지 ID·제목·space·URL·판본·갱신 시각·문서 경로와 frontmatter 구분자를 포함한다(1–9). Data Format B-14 / ISER.INP 조건·헤더 — 외부 지정 얼음 피복(ice cover) 시계열(time series) 파일이다(10–13). 적용 조건 원문: `**Data Format B-14  ISER.INP for ISICE = 1**   ` (10). NISER 횟수만큼 제어값과 시계열 데이터를 반복하는 구조 원문: `C \*\* CONTROL AND TIME SERIES DATA REPEATING NISER TIMES.  ` (13). 헤더 이름·시간 환산 단위·가산 시간 조정 원문: `C \*\* HEADER: MISER(NISER), TCISER(NISER),TAISER(NISER),RMULADJC,RMULADJT  ` (14); `C \*\* MISER = NUMBER OF DATA, TCISER=TIME CONVERSION TO SEC, TAISER=ADDITIVE TIME ADJ  ` (15). 프로젝트·파일 용도 주석도 포함한다(11–12). 빈 주석을 포함한다(16). |
| 17–21 | Data Format B-14 / 첫 블록 예시 입력 — 첫 헤더는 자료 수 4와 환산값·조정값을 제시한다(17). 뒤에는 두 열의 자료 네 행이 있다(18–21). 행별 원문: `               4              86400          0          1            0  ` (17); `240.001 0.3500  ` (18); `240.010 0.5500  ` (19); `240.020 0.7500  ` (20); `240.030 0.6000  ` (21). 표시된 수치를 기본값으로 해석하지 않았다. |
| 22–28 | Data Format B-14 / 둘째 블록 예시 입력 — 둘째 헤더는 자료 수 6과 환산값·조정값을 제시한다(22). 뒤에는 두 열의 자료 여섯 행이 있다(23–28). 행별 원문: `              6                86400         0           1            0  ` (22); `20.000 0.0000  ` (23); `238.000 0.4000  ` (24); `252.000 0.5700  ` (25); `283.000 0.7200  ` (26); `290.000 0.5500  ` (27); `320.000 0.3400` (28). 표시된 수치를 기본값으로 해석하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14행의 `RMULADJC`, `RMULADJT`는 이 파일에서 의미를 정의하지 않는다.
- 18–21·23–28행의 시계열 두 열에는 이름·단위·물리적 의미를 설명하는 헤더가 없다. 얼음 피복 값의 표현 방식이나 허용 범위도 이 파일에 없다.
