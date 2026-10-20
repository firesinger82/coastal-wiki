---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/dilate.cuh
lines: 41
sha256: 74c5709423ce85b7914164dcd554d923734c8350f1cff4e6988550f57b8b9cbb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# dilate.cuh — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`를 포함한다(3). 빈 줄(4) 뒤 `MortonCode.h`·`Coordinate.h`를 포함한다(5–6). 빈 줄(7) 뒤 주석은 16진수(hexadecimal) 접두사 `0x`, 16진수와 이진수의 대응, `0x0000ffff`의 비트 배치 및 OR·AND·XOR·왼쪽/오른쪽 시프트(shift) 연산자를 설명한다(8–21). 마지막은 빈 줄(22)이다. 전처리 조건 분기는 없다. |
| 23–41 | 각 비트 사이에 0을 삽입한다는 주석과 참고 블로그 주소가 있다(23–24). `__host__ __device__ __forceinline__` (25) 함수 `MortonCode dilate(Coordinate coord)`를 정의한다(26–27). 빈 줄(28) 뒤 주석은 좌표마다 먼저 16비트로 잘라 두 좌표의 모턴 코드(Morton code)가 32비트가 되게 한다고 적는다(29–31). 빈 줄(32) 뒤 첫 식은 `coord &= 0x0000ffff;` (33)이다. 빈 줄(34) 뒤 `coord = (coord ^ (coord << 8)) & 0x00ff00ff;` (35), `coord = (coord ^ (coord << 4)) & 0x0f0f0f0f;` (36), `coord = (coord ^ (coord << 2)) & 0x33333333;` (37), `coord = (coord ^ (coord << 1)) & 0x55555555;` (38)를 차례로 수행한다. 각 식 뒤 주석은 비트가 벌어지는 배치를 보인다(33·35–38). 빈 줄(39) 뒤 `return coord;` (40)로 결과를 반환한다. 함수 종료(41)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12: 16진수 설명 주석은 이진수 대응의 첫 항을 `1 = 0000`이라고 적는다.
- 29–38: 설명 주석은 좌표당 16비트와 모턴 코드 32비트를 전제한다. 실행식은 입력에 고정 마스크 `0x0000ffff`를 적용하며 시프트 횟수와 후속 마스크도 상수이다.
