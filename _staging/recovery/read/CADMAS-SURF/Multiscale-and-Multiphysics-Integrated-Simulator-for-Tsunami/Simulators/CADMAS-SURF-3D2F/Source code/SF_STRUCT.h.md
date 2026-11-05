---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/SF_STRUCT.h
lines: 5
sha256: 0c1d6a669749d4639349302d661e8ca75de63c2de1bc518cdc1f7be65ede07a0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SF_STRUCT.h — 판독 구간 기록

구간은 1행부터 5행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 공유 저장 영역(COMMON block) /SF_STRUCT/의 변수 목록 전체가 1–5행의 한 연속 문장이다. 이 파일에는 자료형·초기값·실행문이 없다. 이 파일만으로 각 변수의 용도는 확인할 수 없다. 원문: `      COMMON /SF_STRUCT/ ICPL,IPART,IGEO,IOT,IENS,INT1,NELM,NELM0,NNOD` (1); `     &                  ,NNOD0,NPFC,NPFC0,TSTR1,TSTR2,IROOTS,ISTM` (2); `     &                  ,IROOTSTM,ICON,NICRG,NCTR,E_MEAN` (3); `     &                  ,INT2,IOR` (4); `     &                  ,PLOWER2,GMIN,FMIN,PORS` (5) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
