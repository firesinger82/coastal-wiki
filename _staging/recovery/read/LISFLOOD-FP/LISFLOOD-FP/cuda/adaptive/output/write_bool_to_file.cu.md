---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_bool_to_file.cu
lines: 48
sha256: f128163378c40d93e9d8866487b509b0d8dd92c85741faf70f7cbc6626889ec2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_bool_to_file.cu — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–31 | 헤더 포함과 CUDA 호스트 함수(host function) `write_bool_to_file` 정의이다(1–11). 파일명·디렉터리 접두부·장치 진리값(boolean) 배열·길이를 받는다(6–9). 호스트 배열을 할당하고 바이트 수를 계산하여 `copy_cuda`로 복사한다(12–22). 255문자 경로 버퍼를 널 문자로 초기화하고 `sprintf`로 dirroot·filename·`.csv`를 붙여 w 모드로 연다(24–30). 전처리 조건 분기는 없다. 원문: `__host__` (3); `size_t bytes = array_length * sizeof(bool);` (15). |
| 32–48 | 시작 시 3–11행 `write_bool_to_file` 안. 파일 열기 실패이면 오류 출력 후 `exit(-1)`을 호출한다(32–35). `results` 머리글과 개행을 출력한다(38). 배열 전체를 순회하며 각 진리값을 `%d`로 한 줄씩 출력한다(40–43). 파일과 호스트 배열을 해제하고 함수를 닫는다(45–48). 원문: `if (NULL == fp)` (32); `for (int i = 0; i < array_length; i++)` (40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–28: 경로 버퍼 크기는 255이다. 경로 구성에는 길이 인수가 없는 `sprintf`를 사용한다.
