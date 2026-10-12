---
file: models/SWAN/raw/source_code/swan/src/SwanFindObstacles.ftn90
lines: 143
sha256: 9bbe6b907b3e0dd2dc568e7683775decc420b09ffb685ae1e9b0b71af842f639
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanFindObstacles.ftn90 — 판독 구간 기록

구간은 1행부터 143행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | `SwanFindObstacles` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 계산 격자 장애물(obstacle)을 찾아 저장한다는 목적과 면-장애물 교차 방법(38–44). 통신·장애물·격자 모듈과 `implicit none`(48–54). |
| 56–87 | 시작 시 1행 루틴 안. 출력 `cross(nfaces)`는 교차 장애물의 순서 번호이며 비교차 값은 0이라는 선언 주석(58–59). 순회·면 끝점 번호·장애물 선분 및 면 좌표·논리 함수 `SwanCrossObstacle`·장애물 연결 목록(linked list) 포인터·면 및 꼭짓점 포인터 선언(63–80). `ient = 0` 초기값(63). 구조·소스 안내 주석(82–87). [10-13 전수 검증 보완] |
| 88–112 | 시작 시 1행 루틴 안. 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanFindObstacles')` (88)이다. 꼭짓점·면 객체를 연결한다(92–93). `cross = 0`(97)으로 초기화한다. `cobst`를 첫 장애물 `FOBSTAC`에 연결한다(101). `do j = 1, NUMOBS`(103)에서 첫 모서리점(corner point)을 읽고(105–106), `do k = 2, cobst%NCRPTS    ! number of corner points of considered obstacle` (108)에서 선분의 다음 끝점을 읽는다(110–111). 첫 모서리점 대입은 `xobs(1) = cobst%XCRP(1)`(105), `yobs(1) = cobst%YCRP(1)`(106)이다. 다음 끝점 대입은 `xobs(2) = cobst%XCRP(k)`(110), `yobs(2) = cobst%YCRP(k)`(111)이다. [10-13 전수 검증 보완] |
| 113–143 | 시작 시 1행 루틴·103행 장애물 루프·108행 모서리점 루프 안. `faceloop : do iface = 1, nfaces`(115)의 경계 면 제외 조건은 `if ( face(iface)%atti(FMARKER) == 1 ) cycle faceloop    ! boundary face` (117)이다. 두 면 끝점 번호와 좌표를 읽는다(119–125). 교차 검사·저장 조건은 `if ( SwanCrossObstacle( xv, yv, xobs, yobs ) ) cross(iface) = j` (127)이며 `SwanCrossObstacle`을 호출한다. 면 루프 종료 후 다음 선분의 시작점을 현재 끝점으로 복사한다(129–134). 모서리점 루프 밖에서 다음 장애물 존재 검사·종료 조건은 `if (.not.associated(cobst%NEXTOBST)) exit` (138)이다. 다음 장애물 포인터를 연결하고 루프·루틴을 끝낸다(139–143). 면 끝점 번호는 `vb = face(iface)%atti(FACEV1)`(119), `ve = face(iface)%atti(FACEV2)`(120)이다. 좌표 대입은 `xv(1) = vert(vb)%attr(VERTX)`(122), `yv(1) = vert(vb)%attr(VERTY)`(123), `xv(2) = vert(ve)%attr(VERTX)`(124), `yv(2) = vert(ve)%attr(VERTY)`(125)이다. 면 루프는 129행에서 닫힌다. 다음 선분의 시작점 대입은 `xobs(1) = xobs(2)`(131), `yobs(1) = yobs(2)`(132)이다. 모서리점 루프는 134행에서 닫힌다. 장애물 루프는 141행에서 닫힌다. [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 97·103–129: `cross`는 면마다 장애물 번호 하나만 저장한다. 여러 장애물이 같은 면을 교차하면 나중 장애물 반복의 대입이 이전 번호를 덮어쓴다.
- 101–106·138–139: 첫 `FOBSTAC` 포인터를 연결한 뒤 첫 좌표 접근 전에는 `associated(cobst)` 검사가 없다. 다음 장애물로 이동할 때는 `associated(cobst%NEXTOBST)`를 검사한다.
