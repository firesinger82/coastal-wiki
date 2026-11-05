---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/mk_dir.c
lines: 22
sha256: 565d2691402fe3a12703d0d0258c8e390112fdbcedabef14578c4770e967d925
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mk_dir.c — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | C 함수 mk_dir는 stdio.h·sys/stat.h를 포함한다(1–2). str[len]에 널 문자(null terminator)를 쓰고 mkdir(str,0777)을 호출한다(4–8). 10–11행 printf 두 줄은 /* ... */로 주석 처리된 코드다. MK_DIR와 mk_dir_는 각각 같은 인수로 mk_dir를 호출하는 이름 호환 함수다(14–22). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `#include <stdio.h>` (1) <br> `#include <sys/stat.h>` (2) <br> `void mk_dir(char *str, int len)` (4) <br> `{` (5) <br> `	str[len] = 0;` (6) <br> `    mkdir(str,0777);` (8) <br> `/*	printf("%s\n", str);` (10) <br> `	printf("%d\n", len); */` (11) <br> `}` (12) <br> `void MK_DIR(char *str, int len)` (14) <br> `{` (15) <br> `	mk_dir(str, len);` (16) <br> `}` (17) <br> `void mk_dir_(char *str, int len)` (19) <br> `{` (20) <br> `	mk_dir(str, len);` (21) <br> `}` (22) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·8: 함수는 전달받은 문자열의 str[len]을 직접 변경한다. mkdir의 반환값을 검사하거나 저장하는 문장은 없다.
