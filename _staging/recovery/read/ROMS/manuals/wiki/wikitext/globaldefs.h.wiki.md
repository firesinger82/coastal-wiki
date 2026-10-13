---
file: models/ROMS/raw/manuals/wiki/wikitext/globaldefs.h.wiki
lines: 10
sha256: 12cda1a5a1129e529147243a264dea947dafdf75702793dbd0bf0dec729c0475
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# globaldefs.h.wiki — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다. 한국어 문장은 판독 설명이며, 원문 인용은 행 번호와 함께 구분한다.

| 구간 | 내용 |
|---|---|
| 1–10 | globaldefs.h — 모든 응용에 사용하는 내부 CPP 정의를 담는 헤더(header)라고 설명한다(2). 개발자가 배열 동적 할당·선언·병렬화(parallelism)·라이브러리 인터페이스(library interface)·표준 알고리즘(standard algorithms)·옵션 검사를 제어하는 정의를 수정하며 일반 사용자에게는 수정하지 않기를 권한다(2). cppdefs.h 끝의 include 예제와 주석을 원문대로 옮긴다(4–10). 원문: `<div class="title">globaldefs.h</div>` (1); `ROMS header file containing internal '''cpp''' definitions that are used in all applications. This file is usually modified by the developers to define various internal options that controls array dynamic allocation, array declaration, parallelism, library interface, standard algorithms options, and internal option checking. It is recommended to the regular user to not modify this file.` (2); `This file is included at the bottom of [[cppdefs.h]]:` (4); ` <span class="red">` (5); `  /*` (6); `  **  Include internal CPP definitions.` (7); `  */<br>` (8); `  #include "globaldefs.h"` (9); ` </span>` (10). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
