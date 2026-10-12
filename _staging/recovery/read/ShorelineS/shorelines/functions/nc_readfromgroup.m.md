---
file: models/ShorelineS/raw/source_code/shorelines/functions/nc_readfromgroup.m
lines: 20
sha256: c03813b375e26f58f5882d53bf1f75ff2c6af10730badeb25b991551bcea6ca7
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# nc_readfromgroup.m — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 함수 시그니처(1). 지정한 그룹(group)의 NetCDF4 변수를 전체 또는 start·count 부분 배열로 읽는 사용법·예시 주석(2–7)과 빈 줄(8). 원문: `function data = nc_readfromgroup(fname, group, varname, varargin)` (1). |
| 9–12 | 시작 시 1행 nc_readfromgroup 함수 안. netcdf.open의 NC_NOWRITE로 파일을 읽기 전용으로 연다(9). onCleanup에 netcdf.close를 등록한다(10). netcdf.inqNcid·inqVarID로 그룹·변수 식별자를 얻는다(11–12). 원문: `ncid  = netcdf.open(fname,'NC_NOWRITE');` (9), `cleanupObj = onCleanup(@() netcdf.close(ncid));` (10), `gid   = netcdf.inqNcid(ncid, group);` (11), `vid   = netcdf.inqVarID(gid, varname);` (12). |
| 13–20 | 시작 시 1행 nc_readfromgroup 함수 안. 입력이 3개면 netcdf.getVar로 전체 변수를 읽는다(13–14). 그 외에는 varargin의 첫 두 값을 start·count로 전달해 부분 배열을 읽는다(15–18). 분기·함수 종료(19–20). 원문: `if nargin==3` (13), `data = netcdf.getVar(gid, vid);` (14), `else` (15), `start = varargin{1};` (16), `count = varargin{2};` (17), `data  = netcdf.getVar(gid, vid, start, count);` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2–7: 사용법 주석은 readFromGroup 이름을 사용한다. 실제 함수 이름은 nc_readfromgroup이다(1).
- 13–18: 3인수 이외 경로는 varargin{1}·{2}를 직접 참조한다. 선택 인수가 둘인지 검사하는 조건은 없다.
