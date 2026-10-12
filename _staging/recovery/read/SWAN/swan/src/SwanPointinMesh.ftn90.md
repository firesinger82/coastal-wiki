---
file: models/SWAN/raw/source_code/swan/src/SwanPointinMesh.ftn90
lines: 127
sha256: 4d5e83468843adb9e14a627746ff9659101b0793264e2dc013b7ca8207e106e8
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanPointinMesh.ftn90 — 판독 구간 기록

구간은 1행부터 127행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | 논리 함수(logical function) SwanPointinMesh(x,y)를 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 추가 이력과 점의 격자 내부 여부 검사 목적을 적는다(3–40). 점에서 수직선을 그어 경계 면(boundary face) 교차 횟수가 홀수이면 내부라는 방법 주석과 모듈 사용을 포함한다(44–53). |
| 55–81 | 시작 시 1행 SwanPointinMesh 함수 안. 입력 좌표 x·y, 교차 횟수·면 정점 번호·면 양 끝 좌표·교차 y좌표, 면 객체 포인터(pointer)를 선언한다(57–74). 구조·소스 구분 주석과 빈 줄을 포함한다(75–81). 원문(행 순서): `integer, save                         :: ient = 0 ! number of entries in this subroutine` (62). |
| 82–117 | 시작 시 1행 SwanPointinMesh 함수 안. 조건부 strace 호출 후 면 객체를 연결하고 numcrs=0으로 시작한다(82–88). 전체 면 중 FMARKER=1인 경계 면을 선택한다(92–94). 끝점 좌표를 읽고 x를 가로지르는 반개구간(half-open interval) 조건과 y조건을 적용한다(96–106). 선형 교차 좌표 yc가 y보다 크면 교차 수를 더한다(108–109). 모든 루프·분기를 닫는다(111–117). 원문(행 순서): `if (ltrace) call strace (ient,'SwanPointinMesh')` (82); `face => gridobject%face_grid` (86); `numcrs = 0` (88); `do iface = 1, nfaces` (92); `if ( face(iface)%atti(FMARKER) == 1 ) then   ! boundary face` (94); `v1 = face(iface)%atti(FACEV1)` (96); `v2 = face(iface)%atti(FACEV2)` (97); `x1 = xcugrd(v1)` (99); `y1 = ycugrd(v1)` (100); `x2 = xcugrd(v2)` (101); `y2 = ycugrd(v2)` (102); `if ( ( (x1 > x) .and. (x2 <= x) ) .or. ( (x2 > x) .and. (x1 <= x) ) ) then` (104); `if ( y1 > y .or. y2 > y ) then` (106); `yc = y1 + (x-x1) * (y2-y1) / (x2-x1)` (108); `if ( yc > y ) numcrs = numcrs + 1` (109). |
| 118–127 | 시작 시 1행 SwanPointinMesh 함수 안. 교차 수의 2에 대한 나머지가 1이면 참, 아니면 거짓을 반환한다(121–125). 함수 종료를 포함한다(127). 원문(행 순서): `if ( mod(numcrs,2) == 1 ) then` (121); `SwanPointinMesh = .true.` (122); `else` (123); `SwanPointinMesh = .false.` (124). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 104–109·121–125: 교차 조건은 x에 대해 >와 <=를 함께 사용하고 yc>y를 사용한다. 경계점 자체를 별도 반환하는 분기는 이 함수에 없다.

