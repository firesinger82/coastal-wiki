---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_reals_to_file.cu
lines: 53
sha256: be43ded761cf76e5b10af612bd88036be6319735e164e00ab7344f9b49131492
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_reals_to_file.cu — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 헤더 포함(1), `__host__ void lis::cuda::acc_nugrid::write_reals_to_file` (3) 인수와 본문 시작(4–10). 전처리 조건 분기는 없다. d_results 복사용 호스트 배열을 array_length 길이로 할당한다(11–12). 바이트 수 `size_t bytes = array_length * sizeof(NUMERIC_TYPE);` (14), copy_cuda 호출 전체 `copy_cuda`<br>`(`<br>`h_results,`<br>`d_results,`<br>`bytes`<br>`);` (16–21). |
| 23–38 | 시작 시 3–10행 write_reals_to_file 함수 안. 255자 fullpath에 respath·filename·.csv를 연결한다(25–27). fopen의 모드는 w(29). `if (NULL == fp)` (31)이면 오류 출력 후 exit(-1)(33–34). 파일 첫 행에 results를 쓴다(37). |
| 39–53 | 시작 시 3–10행 write_reals_to_file 함수 안. sum=0으로 초기화한다(39). `for (int i = 0; i < array_length; i++)` (41)에서 NUM_FMT·소수 정밀도 15로 값을 한 행씩 쓰고(43), `sum += h_results[i];` (45)로 합을 누적한다. 평균 출력식 `printf("%s: %.15f\n", filename, sum / array_length);` (48). fclose·호스트 배열 해제·함수 종료(50–53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–48: 평균 출력은 sum / array_length이다. 이 함수에는 array_length가 0인지 확인하는 분기가 없다.
- 25–27: fullpath 크기는 255자이다. 경로 조립은 길이 제한 인수가 없는 sprintf로 수행한다.
