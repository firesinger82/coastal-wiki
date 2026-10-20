---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_snapshot.templates.cu
lines: 112
sha256: cc4e1a69735ef62bef1b0d192b3ea964c22b79fb05eafc11741ecde71863433b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_snapshot.templates.cu — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | `template<typename F>` (1)의 Snapshot 생성자는 전달된 출력 설정·상태·기하 참조를 초기화 목록(initializer list)에 저장한다(2–26). 파일 내부 전처리 조건 분기는 없다. |
| 28–48 | `write_if_needed`의 `if (t >= next_save) {` (36) 안에서 wait, `F::copy(U, d_U, geometry)` (38), `if (verbose) printf("Writing snapshot at t=%f\n", t);` (39), write(call_gzip)를 순서대로 호출한다. 다음 시각은 `next_save += interval;` (43), 출력 번호는 `counter++;` (44)로 갱신한다. 조건 종료·함수 종료·빈 줄을 포함한다(45–48). |
| 49–63 | `write_max_files`는 `F::copy(U, d_U, geometry)` (56)를 호출한다. 조건은 `if (verbose) printf("Writing max files\n");` (57)이다. `write_maxes()` (59)를 호출하고 종료한다. |
| 64–85 | 수위·유량·유속 기록 활성화 함수는 각각 write_elevation·write_discharge·write_velocity를 true로 설정한다(65–82). 유속 함수는 전달된 DepthThresh도 저장한다(83). |
| 86–99 | F·T의 이중 템플릿인 `write_async`는 `return lis::Snapshot::write_async(field, geometry, pitch, offset,` (96), `resrootname, counter, suffix, verbose, outflag, call_gzip, precision);` (97)로 공통 기록 루틴에 위임한다. 반환형은 std::future<void>이다(88). |
| 100–112 | F·T의 이중 템플릿인 `write_max`는 `return lis::Snapshot::write_max(field, geometry, pitch, offset, resrootname, suffix,` (110), `verbose, outflag, precision);` (111)로 공통 최대값 기록 루틴에 위임한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–44: 저장 조건은 while이 아닌 if이다. 한 번의 호출은 next_save에 interval을 한 번만 더한다.
- 36–38·54–59: write_if_needed는 복사 전에 wait를 호출한다. write_max_files 본문에는 wait 호출이 없다.
