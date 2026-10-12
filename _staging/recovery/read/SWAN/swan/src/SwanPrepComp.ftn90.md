---
file: models/SWAN/raw/source_code/swan/src/SwanPrepComp.ftn90
lines: 94
sha256: 2a8130a697dcfeb0522c64c53130ea6e82e06ebbab5e942bf3156eb8b8250b84
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanPrepComp.ftn90 — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | SwanPrepComp(cross)를 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 추가 이력과 계산 시작 전 준비 목적을 적는다(3–40). ocpcomm4·swcomm3·m_obsta·SwanGriddata·SwanGridobjects를 사용한다(44–48). m_obsta에서는 `use m_obsta, only: OBSTDONE`으로 OBSTDONE만 가져온다(46). [10-13 전수 검증 정정] |
| 51–69 | 시작 시 1행 SwanPrepComp 루틴 안. 출력 cross(nfaces)는 면을 가로지르는 장애물 순서 번호이며 없으면 0이라는 주석을 갖는다(54–55). 추적 변수·정점 루프 변수·정점 객체 포인터(pointer)를 선언한다(59–62). 구조·소스 구분 주석을 포함한다. 원문(행 순서): `integer, save                         :: ient = 0 ! number of entries in this subroutine` (59). |
| 70–94 | 시작 시 1행 SwanPrepComp 루틴 안. strace를 조건부 호출하고 정점 객체를 연결한다(70–74). 할당된 kvertc·kvertf를 해제한다(78–79). vmark>=excmark인 정점에 경계 조건(boundary condition) VBC=1을 설정한다(83–85). 장애물이 있고 아직 처리하지 않았으면 SwanFindObstacles(cross)를 호출한 뒤 OBSTDONE을 참으로 설정한다(89–92). 루틴 종료를 포함한다(94). 원문(행 순서): `if (ltrace) call strace (ient,'SwanPrepComp')` (70); `vert => gridobject%vert_grid` (74); `if (allocated(kvertc)) deallocate(kvertc)` (78); `if (allocated(kvertf)) deallocate(kvertf)` (79); `do ivert = 1, nverts` (83); `if ( vmark(ivert) >= excmark ) vert(ivert)%atti(VBC) = 1` (84); `if ( NUMOBS > 0 .and. .not.OBSTDONE ) then` (89); `call SwanFindObstacles ( cross )` (90); `OBSTDONE = .true.` (91). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54–55·89–92: cross는 intent(out)이다. cross 값을 채우는 호출은 NUMOBS>0과 .not.OBSTDONE 분기 안에만 있으며 이 루틴에 무조건적인 cross=0 대입은 없다.

