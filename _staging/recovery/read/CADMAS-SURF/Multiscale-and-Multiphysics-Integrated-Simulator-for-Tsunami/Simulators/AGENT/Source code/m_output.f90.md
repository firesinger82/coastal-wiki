---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/m_output.f90
lines: 59
sha256: c6bf61c4885d1c3d9a4fe8a3e919618931c7297cafce6f0b930c8605d9f535b2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# m_output.f90 — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 파일 출력 제어 데이터 주석(4). 출력 시각 항목은 목록 출력 시작·종료·간격·다음 출력 시각이며 단위는 s다(5–9). 출력 계열 수(10)는 정수·실수 통계값과 정수·실수 고정·변동 속성값(11–16)을 구분한다. 같은 여섯 계열의 라벨(17–23)과 출력 데이터(24–30)를 설명한다. 원문: `module m_output` (1); `  implicit none` (2); `!----------------------------------------` (3); `! ファイル出力制御データ` (4); `!--出力時刻--` (5); `! out_start              リスト出力の開始時刻(s)` (6); `! out_end                リスト出力の終了時刻(s)` (7); `! out_interval           リスト出力の出力間隔(s)` (8); `! out_time               次回リスト出力時刻(s)` (9); `!--出力の系列数--` (10); `! N_I_statistics         統計値(整数型)の系列数` (11); `! N_R_statistics         統計値(実数型)の系列数` (12); `! N_I_attribute_F        固定属性値(整数型)の系列数` (13); `! N_R_attribute_F        固定属性値(実数型)の系列数` (14); `! N_I_attribute_V        変動属性値(整数型)の系列数` (15); `! N_R_attribute_V        変動属性値(実数型)の系列数` (16); `!--出力データのラベル--` (17); `! String_I_statistics    統計値(整数型)のラベル` (18); `! String_R_statistics    統計値(実数型)のラベル` (19); `! String_I_attribute_F   固定属性値(整数型)のラベル` (20); `! String_R_attribute_F   固定属性値(実数型)のラベル` (21); `! String_I_attribute_V   変動属性値(整数型)のラベル` (22); `! String_R_attribute_V   変動属性値(実数型)のラベル` (23); `!--出力データ--` (24); `! I_statistics           統計値(整数型)` (25); `! R_statistics           統計値(実数型)` (26); `! I_attribute_F          固定属性値(整数型)` (27); `! R_attribute_F          固定属性値(実数型)` (28); `! I_attribute_V          変動属性値(整数型)` (29); `! R_attribute_V          変動属性値(実数型)` (30); `!----------------------------------------` (31); `!` (32) |
| 33–59 | 시작 시 1행 모듈 안. 시작 시 1행 m_output 모듈 안. 계열 수는 정수 통계 3·실수 통계 1·정수 고정 1·실수 고정 1·정수 변동 1·실수 변동 5다. 라벨은 피난 완료·이동 중·사망 인원, (Null), Age, Height, 상태값 설명, X/Y/Z/Velocity.X/Velocity.Y로 설정한다(40–51). 해당 크기의 정수 및 real(4) 출력 배열을 선언한다. 원문: `  real(8):: out_start,out_end,out_interval,out_time` (33); `  integer,parameter:: N_I_statistics=3` (34); `  integer,parameter:: N_R_statistics=1` (35); `  integer,parameter:: N_I_attribute_F=1` (36); `  integer,parameter:: N_R_attribute_F=1` (37); `  integer,parameter:: N_I_attribute_V=1` (38); `  integer,parameter:: N_R_attribute_V=5` (39); `  character(32):: String_I_statistics(N_I_statistics) &` (40); `                & =(/'Number of escaped ','Number of moving  ','Number of dead    '/)` (41); `  character(32):: String_R_statistics(N_R_statistics) &` (42); `                & ='(Null)'` (43); `  character(32):: String_I_attribute_F(N_I_attribute_F) &` (44); `                & ='Age'` (45); `  character(32):: String_R_attribute_F(N_R_attribute_F) &` (46); `                & ='Height'` (47); `  character(32):: String_I_attribute_V(N_I_attribute_V) &` (48); `                & ='0:escaped/1or2:moving/3:dead'` (49); `  character(32):: String_R_attribute_V(N_R_attribute_V) &` (50); `                & =(/'X         ','Y         ','Z         ','Velocity.X','Velocity.Y'/)` (51); `  integer:: I_statistics(N_I_statistics)` (52); `  integer:: I_attribute_F(N_I_attribute_F)` (53); `  integer:: I_attribute_V(N_I_attribute_V)` (54); `  real(4):: R_statistics(N_R_statistics)` (55); `  real(4):: R_attribute_F(N_R_attribute_F)` (56); `  real(4):: R_attribute_V(N_R_attribute_V)` (57); `end module m_output` (59) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
