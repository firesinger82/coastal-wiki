---
file: models/ADCIRC/raw/source_code/adcirc/prep/mkdir.c
lines: 52
sha256: cfcd1d04f64cc473d2c8fad59418b8f1b3072e3bed85e4353af17ddbf797b96f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# mkdir.c — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | cfi.h·sys/stat.h·sys/types.h·stdlib.h·string.h를 포함한다(1–5). `#ifdef _WIN32` (7)이면 windows.h를 포함하고 조건을 닫는다(8–9). 빈 줄도 포함한다(6·10). cfi.h 내부는 이 대상 파일에서 판독하지 않았다. |
| 11–19 | `f_makedir(char* path, size_t len)` 함수 및 dirnm 선언(11–13). `dirnm = (char *) malloc(len+1);` (15)로 끝 문자 공간을 더해 할당한다. `memcpy(dirnm, path, len);` (16)로 len바이트를 복사한다. `dirnm[len] = '\0';` (18)으로 널 종료한다. 빈 줄도 포함한다. |
| 20–29 | 시작 시 11행 f_makedir 함수 안. `#ifdef _WIN32` (20)이면 `CreateDirectory(dirnm,NULL);` (21), `#else` (22)이면 `mkdir(dirnm, 0755);` (23)로 디렉터리를 만든다. 유닉스 권한 인수는 원문 0755이다. `#endif` (24) 후 `free(dirnm);` (27)로 메모리를 해제하고 함수를 끝낸다(28). 빈 줄도 포함한다. |
| 30–37 | `MAKEDIR(protoFSTRING(fpath) protoLenFSTRING(fpath))` 래퍼(wrapper) 선언(30–31). `char   *path = FCD2CP(fpath);` (32), `size_t  len  = FCDLEN(fpath);` (33)으로 Fortran 문자열 포인터와 길이를 얻는다. `f_makedir(path, len);` (35)을 호출하고 종료·빈 줄(36–37). |
| 38–45 | `makedir(protoFSTRING(fpath) protoLenFSTRING(fpath))` 래퍼 선언(38–39). `char   *path = FCD2CP(fpath);` (40), `size_t  len  = FCDLEN(fpath);` (41), `f_makedir(path, len);` (43)로 소문자 심벌 경로도 같은 함수를 호출한다. 종료·빈 줄(44–45). |
| 46–52 | `makedir_(protoFSTRING(fpath) protoLenFSTRING(fpath))` 래퍼 선언(46–47). `char   *path = FCD2CP(fpath);` (48), `size_t  len  = FCDLEN(fpath);` (49), `f_makedir(path, len);` (51)로 밑줄 심벌 경로도 같은 함수를 호출한다. 파일 마지막 닫는 중괄호(52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–18: malloc 반환 포인터를 검사하는 조건 없이 memcpy와 끝 문자 대입을 실행한다.
- 16–18·32–35·40–43·48–51: 전달된 길이만큼 그대로 복사한다. 이 파일에는 Fortran 문자열 끝 공백을 제거하는 처리가 없다.
- 21–23: CreateDirectory와 mkdir의 반환값을 저장하거나 검사하지 않는다. 세 래퍼와 f_makedir의 반환형은 void이다(11·30·38·46).
