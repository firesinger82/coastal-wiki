---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readtide.F90
lines: 94
sha256: 693cfec8a9c0587fe388e7c1c8c00bb6c25e9604029cbf970cb88cf2184af196
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# readtide.F90 — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | private `readtide_module`·공개 `readtide` 선언(1–7), 저작권·LGPL 머리말(8–33). |
| 34–59 | 의존 모듈·인수 및 `temp(par%tideloc+1)` 선언(34–48). `if(.not. xmaster) return` (51). `if(.true.) then` (52) 안의 `if (par%tideloc .eq. 0) then` (53)이면 `s%tidelen = 2` (54), 시간 배열 2개와 위치 차원 0 수위 배열을 할당하고 반환(55–57). |
| 60–75 | 52의 항상 참 블록 안에서 실행(53의 조건은 이미 닫힘). io·ntide를 0으로 설정, `writelog`, unit 31 열기(60–64). `do while (io==0)` (65), `ntide=ntide+1` (66)과 읽기로 종료 상태까지 세고 rewind(67–69). `s%tidelen=ntide-1` (71), 시계열 배열 할당·수위 0 초기화(73–75). |
| 76–90 | 52의 블록 안에서 각 행 읽기(76–77), `if (io .ne. 0) then` (78)이면 `report_file_read_error` (79), 파일 닫기(82). `if (par%morfacopt==1) s%tideinpt = s%tideinpt / max(par%morfac,1.d0)` (84). 이어 독립적으로 `if (s%tideinpt(s%tidelen)<par%tstop) then` (85)이면 로그와 `halt_program` (86–87). 90은 52의 블록 끝. |
| 91–94 | 빈 줄 및 `readtide`·모듈 종료. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52: 전체 읽기 본체를 `if(.true.) then`으로 감싼다.
- 53–57: `tideloc==0` 반환 경로는 `tideinpt`를 할당한 뒤 값을 넣지 않는다.
- 64·77·82: 파일 unit 31이 하드코딩되어 있다.
- 65–71·85: 첫 읽기 실패도 행 수 세기를 종료시키며 `tidelen=ntide-1`로 정한다. 85의 마지막 원소 접근 앞에 `tidelen>0` 검사는 없다.
