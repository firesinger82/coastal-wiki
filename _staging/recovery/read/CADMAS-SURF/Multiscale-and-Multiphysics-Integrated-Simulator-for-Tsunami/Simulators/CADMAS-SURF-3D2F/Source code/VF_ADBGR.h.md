---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ADBGR.h
lines: 13
sha256: db2298d120a83672734e946e769f32242db8fec3604f8d23d16f7c782d973193
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ADBGR.h — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | /VF_ADBGR/는 RDBGF·RDBGTD(3)를 공유한다. 주석은 실수 디버그 값이라고 소개하고 F값·TD용 x·y·z 속도의 의미를 설명한다. 실제 자료형 선언과 초기값은 이 파일에 없다. 원문: `      COMMON /VF_ADBGR/ RDBGF,RDBGTD(3)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ADBGR.h:デバッグ関連:実数` (5) (디버그 관련 실수); `C==== 内容 ===========================================================` (7) (내용); `CD    RDBGF     : CNS : I*4 : 矩形ボックスへのF値指定データ(F値)` (9) (직육면체 영역의 F값 지정 데이터(F값)); `CD    RDBGTD(3) : CNS : I*4 : 矩形ボックスへのTD用速度指定データ(V値)` (10) (직육면체 영역의 TD용 속도 지정 데이터(V값)); `CD                            (1):x方向速度` (11) ((1): x방향 속도); `CD                            (2):y方向速度` (12) ((2): y방향 속도); `CD                            (3):z方向速度` (13) ((3): z방향 속도) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·9–10: 개요 주석은 실수라고 적지만 RDBGF·RDBGTD의 개별 주석은 I*4라고 적는다. 이 파일에는 명시적 자료형 선언이 없다.
