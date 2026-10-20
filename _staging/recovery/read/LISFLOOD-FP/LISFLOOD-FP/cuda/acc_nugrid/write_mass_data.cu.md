---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_mass_data.cu
lines: 72
sha256: f271d7ca0665ef405dac9c5727c41167169af1c051d211fd2cb0c5106675e012
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_mass_data.cu — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 관련 헤더 포함(1), write_mass_data는 결과 경로·GaugePoints·격자 차원·Solver·States·면적·체적·유입·Hds·유출·유량 오차·체적 오차·강우·침투·증발 손실 값을 받는다(3–21). AssembledSolution 인수는 주석이다(6). 관측점 수 검사·격자 크기 계산·바이트 수·h/qx/qy 할당·copy_cuda 호출은 모두 주석이다(23–35). 빈 줄까지 포함한다. 전처리 조건 분기는 없다. |
| 37–55 | 시작 시 3행 write_mass_data 함수 안. 길이 255 경로 배열과 sprintf로 respath에 .mass를 붙인다(37–39). `FILE* fp; // = (solver.t > 0) ? fopen(fullpath, "a") : fopen(fullpath, "w");` (41)의 삼항 연산자는 주석이다. 실제 분기는 `if (solver.t > 0) { //if this is a checkpointed job, we only need to amend the .mass file` (43)이며 참이면 append 모드(44), `else {` (46)이면 write 모드(47)로 연다. `if (NULL == fp)` (50)이면 오류 메시지와 exit(-1)을 실행한다(52–53). 빈 줄을 포함한다. |
| 56–72 | 시작 시 3행 write_mass_data 함수 안. `if (solver.t == C(0.0))` (56) 참이면 Time·Tstep·MinTstep·NumTsteps·Area·Vol·Qin·Hds·Qout·Qerror·Verror·Rain-(Inf+Evap) 머리말을 쓴다(58). `else` (60)에서는 수치 행을 출력한다. 강우와 두 손실의 차를 포함한 전체 원문은 `fprintf(fp, "%-12.3" NUM_FMT" %-10.4" NUM_FMT" %-10.4" NUM_FMT" %-10ld %12.4" NUM_FMT" %12.4" NUM_FMT"  %-11.3" NUM_FMT" %-10.3" NUM_FMT" %-11.3" NUM_FMT" %12.4" NUM_FMT" %12.4" NUM_FMT" %12.4" NUM_FMT"\n", solver.t, solver.Tstep, solver.MinTstep, solver.itCount, FArea, vol2, Qin, Hds, Qout, Qerror, Verror, RainTotalLoss - (InfilTotalLoss + EvapTotalLoss));` (63). 분기를 닫고 fclose한다(65–67). h·qx·qy 해제는 주석이며 함수 닫기·빈 줄을 포함한다(69–72). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–10·23·37–67: gauge_points·mesh_dim·states는 실행 본문에서 참조하지 않는다. 관측점 수가 0인 경우의 반환문도 주석이다.
- 56–65: solver.t가 C(0.0)이면 머리말만 쓰고 수치 행은 else 분기에서 쓴다.
