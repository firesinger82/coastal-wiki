---
file: models/SWASH/raw/source_code/swash/src/SwashFlowUDP.ftn90
lines: 172
sha256: 49a2dfc8ad4ed2c284a9700b5af300e414d2d94be93bc11595a6d333348de57e
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashFlowUDP.ftn90 — 판독 구간 기록

구간은 1행부터 172행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | `SwashFlowUDP` 입구(1). 기관·저작권·GPL 3 이상·무보증 주석(2–29). Marcel Zijlema와 2017년 신설 이력(30–37). 도심(centroid)과 면(face)의 바닥 값을 결정한다는 목적 주석(38–41). ocpcomm4·SwashCommdata3·m_genarr·SwashFlowdata·SwanGriddata·SwanGridobjects를 사용한다(44–49). |
| 51–80 | 시작 시 1행 SwashFlowUDP 루틴 안. implicit none(51). 셀·면 반복자, 인접 셀 번호, 길이 3의 정점(vertex) 배열 v, 수심 dep, celltype·facetype 포인터를 선언한다(55–66). 진입 횟수 `integer, save                         :: ient = 0  ! number of entries in this subroutine` (59). 구조·소스 머리말 주석(68–73). `if (ltrace) call strace (ient,'SwashFlowUDP')` (74). cell·face 포인터를 gridobject의 격자 객체에 연결한다(78–79). |
| 81–95 | 시작 시 1행 루틴 안. `if ( dpsopt == 1 ) then` (81)은 최소값 선택이다. `do iface = 1, nfaces` (85)에서 면의 FACEV1·FACEV2 정점을 가져온다(89–90). `dpu(iface) = min( depf(v(1)), depf(v(2)) )` (92). 면 루프 종료(94). |
| 96–123 | 시작 시 1행 루틴과 81행 `if ( dpsopt == 1 ) then`의 참 분기 (124행 `else if`, 170행 `endif`) 안. 타일 방식(tiled approach)의 도심 바닥 계산 주석(96). `do icell = 1, ncells` (98)에서 `dep = 99999999.` (102). `do jf = 1, cell(icell)%nof` (104)에서 FACEID를 가져오고(108), `dep = min( dep, dpu(iface) )` (110)로 면 최소값을 누적한다. 면 루프 종료(112) 뒤 `dps(icell) = dep` (114)로 복사한다. `if ( s1(icell) < epsdry - dps(icell) ) then` (116)이면 `s1(icell) = 0.99*epsdry - dps(icell)` (118). 셀 루프 종료(122). [10-15 전수 검증 보완] |
| 124–146 | 시작 시 1행 루틴과 81행 `if ( dpsopt == 1 ) then`으로 시작한 분기 사슬 (170행 `endif`) 안. `else if ( dpsopt == 2 ) then` (124)은 평균값 선택이며 셀 내부 바닥 값은 일정하다는 주석(126–127). `do icell = 1, ncells` (129)에서 CELLV1·CELLV2·CELLV3 정점을 가져온다(133–135). `dps(icell) = ( depf(v(1)) + depf(v(2)) + depf(v(3)) )/ 3.` (137). `if ( s1(icell) < epsdry - dps(icell) ) then` (139)이면 `s1(icell) = 0.99*epsdry - dps(icell)` (141). 셀 루프 종료(145). [10-15 전수 검증 보완] |
| 147–172 | 시작 시 1행 루틴과 81행 `if ( dpsopt == 1 ) then`의 124행 `else if ( dpsopt == 2 ) then` 분기 (166행 `else`, 170행 `endif`) 안. `do iface = 1, nfaces` (149)에서 FACEC1·FACEC2의 인접 셀 번호를 가져온다(151–152). `if ( icell2 /= 0 ) then` (154)이면 `dpu(iface) = min( dps(icell1), dps(icell2) )` (156). `else` (158)는 `dpu(iface) = dps(icell1)` (160)로 복사한다. 조건·면 루프 종료(162–164). 바깥 dpsopt 분기의 `else` (166)는 `call msgerr(2, 'option BOTCEL = MAX and SHIFT not supported')` (168)를 호출한다. 바깥 조건·루틴 종료와 주석(170–172). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 102·110: 최소값 누적의 시작 값은 99999999.로 고정되어 있다.
- 104·133–137: 최소값 경로는 cell(icell)%nof개 면을 순회한다. 평균값 경로는 CELLV1·CELLV2·CELLV3의 세 정점을 합산하고 3.으로 나눈다.
