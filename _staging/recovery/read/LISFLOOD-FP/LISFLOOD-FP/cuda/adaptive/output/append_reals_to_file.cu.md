---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/append_reals_to_file.cu
lines: 49
sha256: 5d8c0cd362644f36bfb840a5f23ac35cd3b6dc057e4b9934ee91b2dedf27e9a2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# append_reals_to_file.cu — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–30 | 헤더 포함과 CUDA 호스트 함수(host function) `append_reals_to_file` 정의이다(1–12). 파일명·디렉터리 접두부·장치 결과 배열·길이·첫 시간 단계 표시를 받는다(6–10). 호스트 배열을 할당하고 바이트 수를 계산하여 `copy_cuda`로 복사한다(13–23). 255문자 경로 버퍼를 널 문자로 초기화하고 `sprintf`로 dirroot·filename·`.csv`를 붙인다(25–29). 전처리 조건 분기는 없다. 원문: `__host__` (3); `size_t bytes = array_length * sizeof(real);` (16). |
| 31–49 | 시작 시 3–12행 `append_reals_to_file` 안. 첫 시간 단계에는 w, 그 뒤에는 a 모드로 파일을 연다(31). 실패 시 오류를 출력하고 `exit(-1)`을 호출한다(33–36). 배열 전체를 순회하여 `NUM_FIG`·`NUM_FRMT` 형식과 뒤따르는 쉼표로 출력한다(39–42). 개행을 쓰고 파일과 호스트 배열을 해제한다(44–49). 두 출력 형식 매크로의 값은 이 파일에서 정의하지 않는다. 원문: `fp = (first_t_step) ? fopen(fullpath, "w") : fopen(fullpath, "a");` (31); `if (NULL == fp)` (33); `for (int i = 0; i < array_length; i++)` (39); `fprintf(fp, "%" NUM_FIG NUM_FRMT ",", h_results[i]);` (41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–29: 경로 버퍼 크기는 255이다. 경로 구성에는 길이 인수가 없는 `sprintf`를 사용한다.
- 39–44: 모든 원소 뒤에 쉼표를 쓰므로 행의 마지막 원소 뒤에도 쉼표가 남는다.
