---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readwind.F90
lines: 112
sha256: 6c3c76f1046245f82d786ddcba988287d53cbebaa81eef789c71a8f470c4f6b9
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# readwind.F90 — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | private `readwind_module`·공개 `readwind` 선언(1–7), 저작권·LGPL 머리말(8–33). |
| 34–59 | 모듈 의존성·인수(`par`는 intent(in))·지역 변수 및 3원소 temp 선언(34–47). `if(.not. xmaster) return` (51), io·nwind 0, 격자 바람 배열 할당·0 초기화(53–59). |
| 60–78 | `if (par%windfile==' ') then` (60)의 정상풍 분기: 길이 1의 시계열 할당(62–67), 시각=tstop, 풍속=windv(69–70). `s%winddirts=(270.d0-par%windth-s%alfa)*par%px/180.d0` (71); `s%windxts = dcos(s%winddirts)*s%windvelts` (73), `s%windyts = dsin(s%winddirts)*s%windvelts` (74). 격자 투영식 `s%windsu = s%windxts(1)*dcos(s%alfau) + s%windyts(1)*dsin(s%alfau)` (76), `s%windnv = s%windyts(1)*dcos(s%alfav-0.5d0*par%px) - s%windxts(1)*dsin(s%alfav-0.5d0*par%px)` (77). 78에서 파일 입력 `else` 시작. |
| 79–97 | 60의 파일명 조건의 else 안. `writelog`, unit 31 파일 열기(79–80). `do while (io==0)` (81), `nwind=nwind+1` (82)·3열 읽기(83), rewind 및 `s%windlen=nwind-1` (85–86). 다섯 시계열 할당(87–91), 행별 시각·속력·방향 읽기(92–93). `if (io .ne. 0) then` (94)이면 `report_file_read_error` (95). |
| 98–108 | 여전히 60의 else 안. 방향 변환 `s%winddirts=(270.d0-s%winddirts-s%alfa)*par%px/180.d0` (99), `s%windxts = dcos(s%winddirts)*s%windvelts` (100), `s%windyts = dsin(s%winddirts)*s%windvelts` (101), 파일 닫기(102). `if (par%morfacopt==1) s%windinpt = s%windinpt / max(par%morfac,1.d0)` (103). 별도 `if (s%windinpt(s%windlen)<par%tstop) then` (104)이면 로그·`halt_program` (105–106). 108에서 정상/비정상풍 분기 종료. |
| 109–112 | 빈 줄 및 `readwind`·모듈 종료. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38: `constants`에서 가져온 `pi`를 이 파일의 계산에는 사용하지 않고 `par%px`를 쓴다(71·77·99).
- 80·93·102: 파일 unit 31이 하드코딩되어 있다.
- 81–86·104: 읽기 실패 상태까지 세어 `windlen=nwind-1`로 정하며, 마지막 원소 검사 앞에 양수 길이 검사는 없다.
- 58–59·76–77·98–107: 격자 바람은 0으로 초기화한 뒤 정상풍 분기에서만 여기서 투영한다. 파일 분기는 시계열 x/y 성분까지만 계산한다.
