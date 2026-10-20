---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/dilate.cuh
lines: 50
sha256: 1f52d448fcd9067e46c080d1da857eefc1e0ac8a0567c3bcfb5c34a4fbbcc8ac
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# dilate.cuh — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1), CUDA 실행 환경과 `MortonCode.h` 포함(3·5). 전처리 조건 분기는 없다. 비트 연산(bitwise operation)과 16진수 표기·OR·AND·XOR·좌우 시프트 설명 주석(7–20). |
| 22–37 | `lis::cuda::acc_nugrid` 이름 공간(namespace)(22–27). 각 비트 사이에 0을 넣는다는 주석과 참고 블로그 주소(29–30). 함수 지정과 서명은 `__host__ __device__ __forceinline__ MortonCode dilate(int coord)` (31). 좌표를 먼저 16비트로 제한하여 두 좌표의 모턴 코드(Morton code)를 32비트로 만든다는 주석(34–36). |
| 38–50 | 시작 시 22–27행 이름 공간·31행 `dilate` 함수 안. `coord &= 0x0000ffff;                         // in binary: ---- ---- ---- ---- fedc ba98 7654 3210` (38)로 하위 16비트만 남긴다. 비트를 벌리는 연속 식은 `coord = (coord ^ (coord << 8)) & 0x00ff00ff; // in binary: ---- ---- fedc ba98 ---- ---- 7654 3210` (40), `coord = (coord ^ (coord << 4)) & 0x0f0f0f0f; // in binary: ---- fedc ---- ba98 ---- 7654 ---- 3210` (41), `coord = (coord ^ (coord << 2)) & 0x33333333; // in binary: --fe --dc --ba --98 --76 --54 --32 --10` (42), `coord = (coord ^ (coord << 1)) & 0x55555555; // in binary: -f-e -d-c -b-a -9-8 -7-6 -5-4 -3-2 -1-0` (43). `return coord;` (45). 함수와 이름 공간 종료(46–50). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 16진수 설명 주석은 `1 = 0000`이라고 적는다.
- 34–43: 입력 좌표는 하위 16비트로 제한한다. 마스크와 시프트 수는 식 안의 고정 리터럴이다.
