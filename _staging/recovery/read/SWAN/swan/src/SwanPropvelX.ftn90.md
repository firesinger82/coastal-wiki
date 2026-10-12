---
file: models/SWAN/raw/source_code/swan/src/SwanPropvelX.ftn90
lines: 116
sha256: 3397227a42d75fb90c9d5efc0b4607c1e79b3964c47d0536002a8d51cc3eb341
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanPropvelX.ftn90 — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | SwanPropvelX 루틴을 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 신규 및 2009년 회절(diffraction) 보정 이력을 적는다(3–38). 지리 공간(geographical space)의 에너지 수송 속도 계산 목적과 모듈 사용을 포함한다(42–52). |
| 54–80 | 시작 시 1행 SwanPropvelX 루틴 안. cax·cay 출력은 (MDC,MSC,ICMAX)이며 군속도(group velocity)·방향 코사인/사인·현재 주변 흐름을 입력으로 받는다(56–62). 스텐실(stencil)·방향·주파수·정점 번호와 추적 변수를 선언하고 strace를 조건부 호출한다(66–79). 원문(행 순서): `integer, save :: ient = 0 ! number of entries in this subroutine` (68); `if (ltrace) call strace (ient,'SwanPropvelX')` (79). |
| 81–102 | 시작 시 1행 SwanPropvelX 루틴 안. 계산 스텐실 ic 루프를 연다(81). vs(ic)의 정점마다 군속도와 방향 코사인/사인의 곱으로 x/y 수송 속도를 구한다(83–90). IDIFFR와 PDIFFR(3)가 모두 0이 아니면 각 성분에 DIFPARAM(ivert)를 곱한다(94–101). 원문(행 순서): `do ic = 1, ICMAX` (81); `ivert  = vs(ic)      ! points in computational stencil` (83); `do is = 1, MSC` (85); `do id = 1, MDC` (86); `cax(id,is,ic) = cgo(is,ic) * ecos(id)` (87); `cay(id,is,ic) = cgo(is,ic) * esin(id)` (88); `if ( IDIFFR /= 0 .and. PDIFFR(3) /= 0. ) then` (94); `do is = 1, MSC` (95); `do id = 1 ,MDC` (96); `cax(id,is,ic) = cax(id,is,ic)*DIFPARAM(ivert)` (97); `cay(id,is,ic) = cay(id,is,ic)*DIFPARAM(ivert)` (98). |
| 103–116 | 시작 시 1행 SwanPropvelX 루틴·81행 스텐실 ic 루프 안. ICUR가 0이 아니면 모든 방향·주파수의 cax·cay에 현재 정점 ux2·uy2를 더한다(105–112). ic 루프와 루틴 종료를 포함한다(114–116). 원문(행 순서): `if ( ICUR /= 0 )  then` (105); `do is = 1, MSC` (106); `do id = 1, MDC` (107); `cax(id,is,ic) = cax(id,is,ic) + ux2(ivert)` (108); `cay(id,is,ic) = cay(id,is,ic) + uy2(ivert)` (109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 94–109: 회절 인자를 곱하는 조건은 IDIFFR/=0과 PDIFFR(3)/=0이다. 흐름 가산은 회절 분기 뒤에 있으며 회절 인자는 가산되는 흐름 속도에 곱하지 않는다.

