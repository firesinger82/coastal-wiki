---
file: models/ADCIRC/raw/manuals/wiki/markdown/Hstime.md
lines: 11
sha256: d49c52f8bd62f57158a9882d81a688db7a4f6e3b8a3aa2be014f161f53b563c5
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Hstime.md — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Hstime — 제목·판본·빈 줄을 포함한다(1–6). hstime은 ADCIRC의 핫스타트(hot start) 파일 안 시간 정보를 보는 유틸리티(utility)이다(5). 표준 배포의 소스 경로는 `util/hstime.F`이다(5). 원문: `hstime is a utility that comes with ADCIRC that allows you to see the time information inside an ADCIRC [hot start file](/index.php?title=Hot_start_file&action=edit&redlink=1).  In standard ADCIRC distributions, its source code is located in util/hstime.F.  The code can be run with the following options:  ` (5). |
| 7–11 | Options / Compilation — netCDF 입력과 파일명 지정 옵션을 제시한다(7·9). `work/` 디렉터리에서 컴파일 명령을 실행하며 보통 컴파일러 등 추가 옵션이 필요하다고 적는다(11). 원문: ``- `-n` specifies a netCDF file`` (7); ``- `-f filename` specifies the file name`` (9); ``The code can be compiled by entering into the work/ directory and executing `make hstime`.  Though typically the user will need to specify additional options with this command, such as the compiler.`` (11). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5행: `hot start file` 링크에 `action=edit&redlink=1`이 있다.
