---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_gauge_point_data.cu
lines: 257
sha256: d6b39baf4c071484f97666bf1cc85947b733f674ed46773fff98fb04ba8702c5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_gauge_point_data.cu — 판독 구간 기록

구간은 1행부터 257행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 관련 헤더 포함(1), write_gauge_point_data는 결과 경로·조립 해(assembled solution) 참조·관측점(gauge point)·격자 차원·관측점 파일명·Pars·Solver·States를 받는다(3–13). `if (gauge_points.num_points == 0) return;` (15)로 관측점이 없으면 반환한다. 요소 수·전송 바이트 수는 `int num_finest_elems = mesh_dim * mesh_dim;` (17)과 `size_t bytes = sizeof(NUMERIC_TYPE) * num_finest_elems;` (19). h·z 배열을 할당해 copy_cuda로 h·z0를 복사한다(21–27). qx·qy 처리는 주석이다(23–24·28–29). 길이 255 경로 버퍼(31)에 sprintf로 respath와 .stage를 붙인다(33). `FILE* fp; // = (time_now > 0) ? fopen(fullpath, "a") : fopen(fullpath, "w");` (35)의 삼항 연산자는 주석이며 실행되지 않는다. 열기 조건은 `if (/*states.checkpoint == ON && */ solver.t > 0) { //if this is a checkpointed job, we only need to amend the .stage file` (37), 참이면 append 모드(38), `else {` (40)이면 write 모드(41). `if (NULL == fp)` (44)이면 stderr 출력과 exit(-1)을 실행한다(46–47). 전처리 조건 분기는 없다. |
| 50–77 | 시작 시 3행 write_gauge_point_data 함수 안. `if (solver.t == C(0.0) /* \|\| states.checkpoint == OFF*/)` (50) 참 분기는 설명 머리말만 쓴다. 대체 쉼표 형식 출력은 주석이다(52–56). 수심 단위 m·입력 파일명·관측점 정보 표제를 쓴다(58–59). `for (int i = 0; i < gauge_points.num_points; i++)` (60)에서 Morton 코드(Morton code)를 해독하고 중심 좌표·행 우선(row-major) 인덱스를 계산한다. 원문은 `int x = compact(gauge_points.codes[i]);` (62)<br>`int y = compact(gauge_points.codes[i] >> 1);` (63)<br>`NUMERIC_TYPE x_centre = pars.blx + x * pars.dx + pars.dx / C(2.0);` (65)<br>`NUMERIC_TYPE y_centre = pars.bly + y * pars.dx + pars.dx / C(2.0);` (66)<br>`index_1D idx = y * mesh_dim + x;` (68). 관측점 번호·x_centre·y_centre·z[idx]를 출력한다(70). 반복을 닫고 깊이 출력 설명·관측점 수를 쓴 뒤 참 분기를 닫는다(71–77). |
| 78–130 | 시작 시 3행 함수 안. `else {` (78)는 50행 solver.t==C(0.0) 거짓 분기이다. 쉼표 출력 대체 코드는 주석이다(80–92). solver.t를 출력하고(94) `for (int i = 0; i < gauge_points.num_points; i++)` (95)에서 `int x = compact(gauge_points.codes[i]);` (98)<br>`int y = compact(gauge_points.codes[i] >> 1);` (99)<br>`index_1D idx = y * mesh_dim + x;` (101)로 관측 위치를 구해 h[idx]를 출력한다(103). 줄바꿈(105). fflush 및 별도 속력 출력 코드는 주석이다(107–120). 분기를 닫고 fclose, delete[] h·z를 실행한다(122–126). qx·qy 해제는 주석이며 함수 닫기·빈 줄을 포함한다(127–130). |
| 131–177 | write_velocity_point_data는 앞 함수와 같은 종류의 인수를 받는다(131–141). `if (gauge_points.num_points == 0) return;` (143)로 관측점이 없으면 반환한다. 요소 수·바이트 수는 `int num_finest_elems = mesh_dim * mesh_dim;` (145)와 `size_t bytes = sizeof(NUMERIC_TYPE) * num_finest_elems;` (147). v·z를 할당하고 v·z0를 copy_cuda로 복사한다(149–155). qx·qy 처리는 주석이다(151–152·156–157). 길이 255 버퍼에 respath와 .velocity를 붙인다(159–161). `FILE* fp; // = (time_now > 0) ? fopen(fullpath, "a") : fopen(fullpath, "w");` (163)의 삼항 연산자는 주석이다. 실제 열기 조건은 `if (/*states.checkpoint == ON && */ solver.t > 0) { //if this is a checkpointed job, we only need to amend the .stage file` (165), 참이면 append(166), `else {` (168)이면 write(169). `if (NULL == fp)` (172)이면 오류 출력과 exit(-1)을 실행한다(174–175). 전처리 조건 분기는 없다. |
| 178–205 | 시작 시 131행 write_velocity_point_data 함수 안. `if (solver.t == C(0.0) /* \|\| states.checkpoint == OFF*/)` (178) 참 분기는 속력 단위 ms-1과 위치 파일명·관측점 정보 머리말을 쓴다(186–187). 대체 쉼표 형식은 주석이다(180–184). `for (int i = 0; i < gauge_points.num_points; i++)` (188)에서 `int x = compact(gauge_points.codes[i]);` (190)<br>`int y = compact(gauge_points.codes[i] >> 1);` (191)<br>`NUMERIC_TYPE x_centre = pars.blx + x * pars.dx + pars.dx / C(2.0);` (193)<br>`NUMERIC_TYPE y_centre = pars.bly + y * pars.dx + pars.dx / C(2.0);` (194)<br>`index_1D idx = y * mesh_dim + x;` (196)으로 좌표·인덱스를 계산하고 번호·좌표·z[idx]를 출력한다(198). 반복을 닫고(199), 원문 출력 `fprintf(fp, "\nOutput, depths:\n");` (201)와 `fprintf(fp, "Time; velocities 1 to %d\n", gauge_points.num_points);` (202)를 쓴다. 빈 줄과 참 분기 끝(200·203–205). |
| 206–257 | 시작 시 131행 write_velocity_point_data 함수 안. `else {` (206)는 178행 solver.t==C(0.0) 거짓 분기이다. 대체 쉼표 출력은 주석이다(208–220). solver.t를 출력하고(222), `for (int i = 0; i < gauge_points.num_points; i++)` (223)에서 `int x = compact(gauge_points.codes[i]);` (226)<br>`int y = compact(gauge_points.codes[i] >> 1);` (227)<br>`index_1D idx = y * mesh_dim + x;` (229)로 위치를 구해 v[idx]를 출력한다(231). 줄바꿈(233), 주석 처리된 fflush·속력 대체 코드와 빈 줄(235–249)을 포함한다. 분기를 닫고 fclose 및 delete[] v·z를 실행한다(250–254). qx·qy 해제는 주석이다(255–256). 함수 끝(257). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·37·50·140·165·178: 두 함수의 states 인수는 실행식에서 참조하지 않는다. checkpoint 조건은 행 안의 주석으로만 남아 있다.
- 50–77·94–105·178–205·222–233: solver.t가 C(0.0)이면 머리말과 위치 정보만 쓰고, 관측값 시계열 행은 else 분기에서 쓴다.
- 65–66·193–194: y_centre 계산은 y 방향에도 pars.dx를 사용한다. 이 계산식에는 pars.dy가 없다.
- 186·201–202: 속력 함수는 Velocity output·velocities 표제와 함께 Output, depths 표제도 출력한다.
- 62–70·98–103·190–198·226–231: Morton 코드에서 얻은 x·y로 배열 인덱스를 만든다. 각 배열 접근 앞에 x·y의 범위 검사는 없다.
