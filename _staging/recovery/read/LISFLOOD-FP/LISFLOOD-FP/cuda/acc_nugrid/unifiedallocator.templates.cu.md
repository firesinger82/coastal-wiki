---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/unifiedallocator.templates.cu
lines: 14
sha256: bfed77621cd1db951e9ece704f050a44299e79b90309c9aaba889255917258c9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# unifiedallocator.templates.cu — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | allocator·cuda_utils 헤더를 포함한다(1–2). `template<typename T>` (4)의 allocate 메서드(5–8)는 통합 메모리(unified memory)를 할당한다. 크기 계산과 형 변환을 포함한 반환식은 `return static_cast<T*>(lis::cuda::acc_nugrid::malloc_unified(sizeof(T) * n));` (7). 입력 n은 std::size_t이다. 빈 줄(3·9)을 포함한다. 전처리 조건 분기는 없다. |
| 10–14 | `template<typename T>` (10)의 deallocate 메서드는 T* ptr과 std::size_t unused를 받는다(11–12). `lis::cuda::acc_nugrid::free_unified(ptr);` (13)로 포인터를 해제하고 메서드를 닫는다(14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–13: deallocate의 unused 인수는 본문에서 참조하지 않는다.
