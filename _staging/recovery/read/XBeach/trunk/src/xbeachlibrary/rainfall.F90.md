---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/rainfall.F90
lines: 104
sha256: 449f0024b36fc7235bcf96d45639de046e2e2eb9a2e6083d5acc04f4486d06d1
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# rainfall.F90 — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `rainfall_module` 및 저장되는 private 논리값 `constantRainfall` 선언(1–5). `rainfall_init`의 모듈 의존성·상태/매개변수·지역 변수 선언(9–20). |
| 22–33 | `if(.not. xmaster) return` (22) 뒤 master에서 격자 강우율 할당(25). `if (par%rainfall==1) then` (27), 그 안의 `if (par%rainfallratefile==' ') then` (29)이면 상수 강우, 입력 배열은 크기 0(30–32). 단위 변환식 `s%rainfallrate = par%rainfallrate/1000.d0/3600.d0` (33), mm/hr → m/s. |
| 34–63 | 27의 활성 강우 조건 안에서 29의 파일명 조건의 `else` (34): 비상수 강우, `(nx+1,ny+1,nrainfallrate)` 입력·시간 배열 할당(35–37), `create_new_fid()` 호출·파일 열기(39–41). 시간별·j별 입력에서 `if (ier .ne. 0) then` (44,49)이면 `report_file_read_error` (45,50). 읽기 뒤 `s%rainfallinput = s%rainfallinput/1000.d0/3600.d0` (55). 셀별 `LINEAR_INTERP`에 시간 `0.d0`를 전달해 초기 강우율 산출(57–62); 63은 파일명 분기의 끝. |
| 64–72 | 27의 강우 활성 조건의 `else` (64): MPI broadcast 주소용 크기 0 입력 배열, 상수 강우 표시와 강우율 0 설정(66–69). 활성 조건·초기화 루틴 끝(70–71). |
| 73–91 | `rainfall_update` 선언(73–84). `#ifdef USEMPI` (86)에서 `if (par%t<=par%dt) then` (87)일 때만 `xmpi_bcast(constantRainfall)` (88). |
| 92–104 | `if (.not. constantRainfall) then` (92)이면 모든 셀에서 `LINEAR_INTERP(s%trainfallinput,s%rainfallinput(i,j,:),par%nrainfallrate, &` / `par%t,s%rainfallrate(i,j),dummy)` (96–97) 호출. 조건 종료·루틴 및 모듈 끝(100–104). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·22·86–90: `constantRainfall` 선언에 초기값이 없고, 초기화 루틴은 비master에서 바로 반환한다. 이 파일에서 비master에 값을 전달하는 코드는 `USEMPI`의 `par%t<=par%dt` 분기에 있다.
- 60·97: 보간 호출이 돌려주는 `dummy` 값은 호출 후 검사하지 않는다.
