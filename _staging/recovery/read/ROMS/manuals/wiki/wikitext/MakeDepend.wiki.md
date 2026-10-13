---
file: models/ROMS/raw/manuals/wiki/wikitext/MakeDepend.wiki
lines: 4
sha256: 9b21fec020c41416e5c737847b6b1d9ff7914153a61b6b12a1904dee12454730
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# MakeDepend.wiki — 판독 구간 기록

구간은 1행부터 4행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | MakeDepend — 최상위 디렉터리에서 make depend를 실행하면 Compilers/MakeDepend를 자동 생성한다(2). 최상위 makefile이 이를 포함하며 소스 변경 뒤 올바른 재컴파일 순서를 위한 의존성(dependency) 정보를 담는다(2). CPP include, Fortran include, module 의존성의 세 종류를 포함한다고 적는다(2). Bin의 Perl 스크립트 sfmakedepend와 매뉴얼 페이지(man page) 명령을 안내한다(4). 제목과 빈 줄을 포함하며 명령을 그대로 옮긴다. 원문: `The file '''Compilers/MakeDepend''' is generated automatically by executing "'''make depend'''" from the top-level directory. It is included by the top-level '''makefile''' and contains [[Make#Dependencies\|dependency]] information to make sure that everything gets recompiled in the correct order after source files are edited. Fortran 90 with use of the [[C Preprocessor]] has include dependencies of both the '''cpp''' and '''Fortran''' flavor, plus '''module''' dependencies; all three types are placed into the '''MakeDepend''' file.` (2); `The dependency checking program is a [http://www.perl.org/ Perl][http://www.perl.com] script called '''sfmakedepend'''. This is in the '''Bin''' directory and typing "'''Bin/sfmakedepend --man'''" will present you with a man page.` (4). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
