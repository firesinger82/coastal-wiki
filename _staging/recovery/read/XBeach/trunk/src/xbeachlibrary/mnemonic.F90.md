---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/mnemonic.F90
lines: 76
sha256: 36aee2eaf8092cf5487efe00ecd754d65213eff2b6bf6b7069a7b79760ae3ab9
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# mnemonic.F90 — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `mnemmodule`: slen 사용, implicit none·private·save. numvars·arraytype·mnemonics·maxnamelen·maxrank·chartoindex·printvar 공개(6). `mnemonic.inc` 포함(8); 포함 파일 내용은 이 파일 본문에 없다. |
| 10–36 | `arraytype` 정의: type은 i/r, btype은 b/d, rank 주석 범위 0..4(12–14). 이름 maxnamelen, units·standardname·description은 slen, dimensions는 maxrank개의 slen 문자열(15–19). 실수·정수별 rank 0..4 포인터(21–31); 기본 null 초기화 문장 없음. contains 포함. |
| 37–50 | `chartoindex(line)`: -1로 초기화(43), `chartoindex.inc` 포함(45). 포함문 뒤에도 -1이면 `writelog`로 검색 실패 메시지(46–48). 원문 조건·식(행 순서): `chartoindex = -1` (43); `if (chartoindex == -1) then` (46); `end if` (48). |
| 51–76 | `printvar`: arraytype 인수의 trim(name)·type·btype·rank를 표준 출력 및 lid/eid/wid 네 목적지에 모두 기록(55–73). 조건·계산식 없음; 루틴 및 모듈 끝. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–31: arraytype의 포인터 컴포넌트 선언에는 기본 null 초기화가 없다.
- 55–73: printvar는 같은 네 메타데이터를 표준 출력·로그·오류·경고 unit에 무조건 모두 쓴다.
