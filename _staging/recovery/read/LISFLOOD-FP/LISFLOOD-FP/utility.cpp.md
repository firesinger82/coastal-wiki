---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/utility.cpp
lines: 130
sha256: 0fd0fc3c45a283b8db057764a8f7339b076b1d40a6a2b7277bda054545df74e7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# utility.cpp — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 전처리 조건 없음. `#include "utility.h"` (1)로 선언을 포함한다. 파일 내부 할당량 계수기의 기본값은 `static long total_allocated = 0;` (3), `static long total_legacy_allocated = 0;` (4)이다. 빈 줄도 포함한다(2·5). |
| 6–18 | 전처리 조건 없음. `memory_allocate_zero_numeric_legacy(size_t size)`는 `NUMERIC_TYPE* memory = new NUMERIC_TYPE[size]();` (8)로 size개 원소를 값 초기화(value initialization)하여 할당한다. `if (memory == NULL)` (10)이면 두 계수기와 합계를 MB 단위로 출력하고 `exit(-1);` (13)을 호출한다. 실패 분기 밖에서 `total_legacy_allocated += size * sizeof(NUMERIC_TYPE);` (15)로 바이트 수를 누적하고 포인터(pointer)를 반환한다(16). 함수 종료와 빈 줄을 포함한다(17–18). |
| 19–31 | 전처리 조건 없음. `memory_allocate_numeric_legacy(size_t size)`는 `NUMERIC_TYPE* memory = new NUMERIC_TYPE[size];` (21)로 size개 원소를 할당하며 8행의 값 초기화 괄호가 없다. `if (memory == NULL)` (23)이면 할당량을 출력하고 `exit(-1);` (26)을 호출한다. 실패 분기 밖에서 `total_legacy_allocated += size * sizeof(NUMERIC_TYPE);` (28)로 바이트 수를 누적하고 포인터를 반환한다(29). 함수 종료와 빈 줄을 포함한다(30–31). |
| 32–42 | 전처리 조건 없음. `memory_free_legacy(int** memory)`의 `if (*memory != NULL)` (34) 참 분기는 `total_legacy_allocated -= sizeof *memory;` (36)를 실행한다. 이어서 `delete[] * memory;` (38)로 배열을 해제하고 호출자가 전달한 포인터를 NULL로 설정한다(39). 분기·함수 종료와 빈 줄을 포함한다(40–42). |
| 43–53 | 전처리 조건 없음. `memory_free_legacy(NUMERIC_TYPE** memory)`의 `if (*memory != NULL)` (45) 참 분기는 `total_legacy_allocated -= sizeof *memory;` (47)를 실행한다. 이어서 `delete[] * memory;` (49)로 배열을 해제하고 호출자가 전달한 포인터를 NULL로 설정한다(50). 분기·함수 종료와 빈 줄을 포함한다(51–53). |
| 54–70 | `memory_allocate(size_t size)`의 전처리 분기는 `#if defined(_MSC_VER) \|\| defined (__INTEL_COMPILER)` (56), `#else` (58), `#endif` (61)이다. `_MSC_VER` 또는 `__INTEL_COMPILER`가 정의된 조합에서는 `void* memory = _mm_malloc(size, 64);` (57)로 64바이트 정렬(alignment)을 요청한다. 두 매크로(macro)가 모두 미정의인 조합에서는 포인터를 NULL로 초기화하고(59) `posix_memalign(&memory, 64, size);` (60)를 호출한다. 62행 이후는 두 조합의 공통 코드다. `if (memory == NULL)` (62)이면 할당량 출력과 `exit(-1);` (65)을 실행한다. 실패 분기 밖에서 `total_allocated += size;` (67)를 실행하고 포인터를 반환한다(68). 함수 종료와 빈 줄을 포함한다(69–70). 이 파일에는 두 전처리 매크로의 정의값이 없다. |
| 71–80 | 전처리 조건 없음. `memory_free(int** memory)`는 `memory_free((void**)memory);` (73)를 호출한다. `memory_free(NUMERIC_TYPE** memory)`도 `memory_free((void**)memory);` (78)를 호출한다. 두 함수는 명시적 형 변환(cast)으로 void** 인수의 동명 함수에 위임한다. 각 함수의 종료와 빈 줄을 포함한다(74–75·79–80). |
| 81–90 | `memory_free(void** memory)`의 전처리 분기는 `#if defined(_MSC_VER) \|\| defined (__INTEL_COMPILER)` (83), `#else` (85), `#endif` (87)이다. `_MSC_VER` 또는 `__INTEL_COMPILER`가 정의된 조합은 `_mm_free(*memory);` (84)를 호출한다. 두 매크로가 모두 미정의인 조합은 `posix_memalign((void**)&memory, sizeof(float) * 100* 128, 64);` (86)를 호출한다. 이 호출은 지역 인수 memory의 주소를 void**로 변환하여 전달하며, 두 수치 인수는 `sizeof(float) * 100* 128`과 `64`이다. 두 조합의 공통 문장은 `*memory = NULL;` (88)이다. 함수 종료와 빈 줄을 포함한다(89–90). |
| 91–98 | 전처리 조건 없음. `memory_free(void** memory, size_t size)`는 `memory_free(memory);` (93)를 먼저 호출한다. 이후 `total_allocated += size;` (94)를 실행한다. 함수 종료와 뒤의 빈 줄을 포함한다(95–98). |
| 99–123 | 전처리 조건 없음. 머리말 주석은 `trimwhitespace`의 반환값이 원래 문자열의 부분 문자열을 가리키며 반환값을 별도로 해제해서는 안 된다고 적는다(99–103). `trimwhitespace(char *str)`는 끝 포인터 end를 선언한다(104–106). `while (isspace(*str)) str++;` (109)로 선행 공백을 건너뛴다. `if (*str == 0)` (111)이면 현재 str을 즉시 반환한다(112). 그 밖에는 `end = str + strlen(str) - 1;` (115)로 마지막 문자 위치를 구하고 `while (end > str && isspace(*end)) end--;` (116)로 후행 공백을 거슬러 간다. `*(end + 1) = 0;` (119)으로 원래 문자열에 널 종료 문자(null terminator)를 쓰고 str을 반환한다(121). 설명 주석·빈 줄·함수 종료를 포함한다. |
| 124–130 | 전처리 조건 없음. `SetArrayValue(int* arr, int value, int length)`는 `for (int j = 0; j < length; j++)` (126) 안에서 arr[j]에 value를 복사한다(128). 반복 범위는 0부터 length 미만이다. 루프(loop)와 함수의 종료를 포함한다(129–130). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15·28·36·47: 레거시(legacy) 할당 함수는 `size * sizeof(NUMERIC_TYPE)`를 계수기에 더한다. 레거시 해제 함수는 배열 길이를 받지 않고 `sizeof *memory`를 계수기에서 뺀다. 두 해제 함수의 *memory 형식은 각각 int*와 NUMERIC_TYPE*이다.
- 83–88: 두 전처리 매크로가 모두 미정의인 `memory_free(void**)` 분기는 `posix_memalign((void**)&memory, sizeof(float) * 100* 128, 64);` (86)를 호출한다. 이 분기에는 기존 *memory를 해제하는 호출이 없다. 호출 뒤에는 `*memory = NULL;` (88)이 있다.
- 91–95: size 인수가 있는 해제 함수는 `memory_free(memory);` (93) 뒤에 `total_allocated += size;` (94)를 실행한다. 계수기 변경 연산자는 +=이다.
- 60·62·86: 두 posix_memalign 호출의 반환값을 저장하거나 검사하는 문장이 없다. 60행 호출 뒤에는 memory의 NULL 검사만 있다(62). 86행 호출 뒤에는 같은 NULL 검사도 없다(87–88).
