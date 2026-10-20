---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/sample.cpp
lines: 269
sha256: 284394beb8476915194f0ad11a9eaa3a16ab6c707d58152b73280df4f7ee3283
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sample.cpp — 판독 구간 기록

구간은 1행부터 269행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 헤더 포함(1–2). Sample::initialise는 fopen_or_die로 "rb" 파일을 열고(14) count를 fscanf로 읽은 뒤 fgetc로 한 문자를 건너뛴다(16–17). count 크기로 x·y·idx·idx_Qx1·idx_Qx2·idx_Qy1·idx_Qy2·inside_domain 배열을 값 초기화해 할당한다(19–26). 조건부 전처리 지시는 없다. |
| 28–56 | 시작 시 4행 initialise 안. `for (int p=0; p<sample_points.count; p++)` (28)에서 좌표를 fscanf로 읽는다(33–34). `sample_points.inside_domain[p] = (x >= geometry.blx &&` (36), `x <= geometry.blx + geometry.xsz*geometry.dx &&` (37), `y >= geometry.bly && y <= geometry.tly);` (38). `int i = static_cast<int>(floor((x - geometry.blx) / geometry.dx));` (40), `int j = geometry.ysz - 1 - static_cast<int>(` (41), `floor((y - geometry.bly) / geometry.dy));` (42), `i = FMIN(i, geometry.xsz-1);` (44), `j = FMAX(j, 0);` (45). `sample_points.idx[p] = j*pitch + i + offset;` (47), `sample_points.idx_Qx1[p] = j * (pitch + 1) + i + offset;` (48), `sample_points.idx_Qx2[p] = j * (pitch + 1) + i + offset + 1;` (49), `sample_points.idx_Qy1[p] = j * (pitch + 1) + i + offset;` (50), `sample_points.idx_Qy2[p] = j * (pitch + 1) + i + offset + (pitch + 1);` (51). 루프 뒤 fclose(54), 함수 종료(55). |
| 57–79 | Sample::free는 initialise에서 할당한 여덟 배열을 delete[]로 해제한다(62–69). StageFile 생성자는 SamplePoints 참조를 멤버 참조에 묶으며 본문은 비어 있다(72–78). |
| 80–100 | StageFile::open은 filename[800]에 .stage 경로를 만든다(87–88). `if (checkpoint == ON && t > 0) {` (90)이면 "a"로 연다(91). else(93)는 "w"로 연다(94). "wb"로 여는 문장은 주석이다(98). |
| 101–138 | StageFile::write_header의 `if (t == C(0.0) \|\| checkpoint == OFF) {` (110)이면 수심 단위 m·지점 파일 경로·좌표와 지형 정보 헤더를 출력한다(111–113). `for (int i = 0; i < sample_points.count; i++)` (115), `if (sample_points.inside_domain[i])` (117)이면 DEM[sample_points.idx[i]]를 출력한다(119–122). else(124)는 지형값을 n/a로 쓴다(126–127). 지점 루프 뒤 수심 출력 헤더를 쓴다(130–131). 110행의 else(133)는 재시작(checkpoint restart) 표시·fflush만 실행한다(134–135). |
| 139–172 | StageFile::write는 `for (int i=0; i<sample_buf_idx; i++)` (145)에서 시간을 출력하고 `int offset = i * sample_points.count;` (149)를 계산한다. `for (int p=0; p < sample_points.count; p++)` (151), `if (sample_points.inside_domain[p])` (153)이면 sample_buf.H[offset+p]를 출력한다(155–156). else(158)는 "-\\t"를 출력한다(160). 행별 개행·fflush(163–165). 소멸자는 `if (file != nullptr) fclose(file);` (170). |
| 173–200 | GaugeFile 생성자는 SamplePoints 참조를 보관한다(173–179). open은 .velocity 이름을 만든다(188–189). `if (checkpoint == ON && t > 0) {` (191)이면 "a"(192), else(194)는 "w"(195)로 연다. "wb" 문장은 주석이다(198). |
| 201–236 | GaugeFile::write_header의 `if (t == 0) {` (208)은 유속 단위 ms-1·지점 경로 헤더를 쓴다(209–210). `for (int i = 0; i < sample_points.count; i++)` (212), `if (sample_points.inside_domain[i])` (214)이면 지형을 출력한다(216–219). else(221)는 n/a(223–224). 이어 "Output, depths:"와 "Time; velocities 1 to %d"를 출력한다(228–229). 208행의 else(231)는 재시작 표시·fflush(232–233). |
| 237–269 | GaugeFile::write는 `for (int i=0; i<sample_buf_idx; i++)` (243), `int offset = i * sample_points.count;` (247), `for (int p=0; p < sample_points.count; p++)` (249), `if (sample_points.inside_domain[p])` (251)에서 sample_buf.speed[offset+p]를 출력한다(253–254). else(256)는 "-\\t"를 출력한다(258). 개행·fflush(261–263). 소멸자는 `if (file != nullptr) fclose(file);` (268). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–26·33–34: count와 좌표의 fscanf 반환값을 검사하는 조건이 없다. 배열 할당 전에 count의 범위를 검사하는 조건도 이 함수에 없다.
- 36–51: 영역 판정은 경계 좌표를 포함한다. i는 상한만, j는 하한만 제한한다. 인덱스 계산은 inside_domain 값과 관계없이 수행한다.
- 110·208: StageFile 헤더 생성 조건은 시간 0 또는 checkpoint OFF이다. GaugeFile 헤더 생성 조건은 시간 0이다.
- 209·228–229: GaugeFile은 velocity와 velocities 헤더를 쓰면서 중간에 "Output, depths:" 문구도 출력한다.
