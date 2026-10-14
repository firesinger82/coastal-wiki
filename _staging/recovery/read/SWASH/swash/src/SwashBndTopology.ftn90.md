---
file: models/SWASH/raw/source_code/swash/src/SwashBndTopology.ftn90
lines: 144
sha256: 379d8f8d48767596dabd51cbf81dd2ee1c6e8661a0f8a61af61caeea958e55b8
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashBndTopology.ftn90 — 판독 구간 기록

구간은 1행부터 144행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `SwashBndTopology` 시작(1). 저작권·GPL 3 이상·무보증, 작성자와 2022년 신규 이력·빈 줄·주석(2–36). 경계 위상(boundary topology)을 구성한다는 목적(38–40). |
| 42–80 | 시작 시 1행 루틴 안. 통신·격자 자료·격자 객체·계산 자료 모듈(44–49). 셀(cell)·면(face)·경계 인덱스와 추적 횟수 ient=0 선언(53–56). celltype·facetype 포인터(58–59). 경계 셀용 bcpt와 경계 면용 bfpt 연결 목록(linked list)의 정수 jb·다음 노드 포인터, 첫 노드와 현재/임시 포인터 선언(61–73). 구조·소스 머리말 주석(75–80). 원문 조건·계산식·호출: `integer, save                         :: ient = 0 ! number of entries in this subroutine` (54). |
| 81–115 | 시작 시 1행 루틴 안. 추적 호출 후 cell·face를 gridobject에 연결한다(81–86). 경계 셀 수와 첫 노드를 초기화한다(90–93). 모든 셀에서 CMARKER/=0이면 경계 셀 수를 늘리고 셀 번호 노드를 연결한다(94–103). jbcell이 미할당이면 ncellsb 크기로 만든다(105). ncellsb>0이면 목록을 순회하여 jbcell에 번호를 복사하고 tmpbc를 해제한다(107–114). 원문 조건·계산식·호출: `if (ltrace) call strace (ient,'SwashBndTopology')` (81); `cell => gridobject%cell_grid` (85); `face => gridobject%face_grid` (86); `ncellsb   = 0` (90); `frstbc%jb = 0` (91); `currbc => frstbc` (93); `do icell = 1, ncells` (94); `if ( cell(icell)%atti(CMARKER) /= 0 ) then   ! boundary cell` (95); `ncellsb = ncellsb + 1` (96); `allocate(tmpbc)` (97); `tmpbc%jb = icell` (98); `currbc%nextbc => tmpbc` (100); `currbc => tmpbc` (101); `if (.not.allocated(jbcell)) allocate(jbcell(ncellsb))` (105); `if ( ncellsb > 0 ) then` (107); `currbc => frstbc%nextbc` (108); `do jb = 1, ncellsb` (109); `jbcell(jb) = currbc%jb` (110); `currbc => currbc%nextbc` (111); `deallocate(tmpbc)` (113). |
| 116–144 | 시작 시 1행 루틴 안. 경계 면 수와 첫 노드를 초기화한다(118–121). 모든 면에서 FMARKER/=0이면 면 수를 늘리고 면 번호 노드를 연결한다(122–131). jbface가 미할당이면 nfacesb 크기로 만든다(133). nfacesb>0이면 목록을 순회해 번호를 복사하고 tmpbf를 해제한다(135–142). 빈 주석·루틴 종료(143–144). 원문 조건·계산식·호출: `nfacesb   = 0` (118); `frstbf%jb = 0` (119); `currbf => frstbf` (121); `do iface = 1, nfaces` (122); `if ( face(iface)%atti(FMARKER) /= 0 ) then   ! boundary face` (123); `nfacesb = nfacesb + 1` (124); `allocate(tmpbf)` (125); `tmpbf%jb = iface` (126); `currbf%nextbf => tmpbf` (128); `currbf => tmpbf` (129); `if (.not.allocated(jbface)) allocate(jbface(nfacesb))` (133); `if ( nfacesb > 0 ) then` (135); `currbf => frstbf%nextbf` (136); `do jb = 1, nfacesb` (137); `jbface(jb) = currbf%jb` (138); `currbf => currbf%nextbf` (139); `deallocate(tmpbf)` (141). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 97–113·125–141: 경계 셀/면마다 노드를 할당한다. 명시적 노드 해제는 마지막 tmpbc·tmpbf에 대한 각각 한 문장이다. 이 파일에는 목록 전체를 순회하며 노드를 해제하는 루프가 없다.
- 105·133: jbcell·jbface는 미할당일 때만 할당한다. 이미 할당된 배열 크기와 새 ncellsb·nfacesb를 비교하거나 재할당하는 문장은 이 루틴에 없다.
