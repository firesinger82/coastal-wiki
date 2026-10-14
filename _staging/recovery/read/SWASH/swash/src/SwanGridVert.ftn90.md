---
file: models/SWASH/raw/source_code/swash/src/SwanGridVert.ftn90
lines: 108
sha256: 5ad5728774009b73e5f1747ec167988d5fd5169c5b5d80bd78f2ed23903cfd2f
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanGridVert.ftn90 — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | SwanGridVert 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). 비구조 격자(unstructured grid)의 꼭짓점(vertex) 자료구조(data structure)를 채우는 목적·방법(38–44). ocpcomm4·SwanGridobjects 사용(48–49), implicit none(51). nverts·vmark(nverts)·xcugrd(nverts)·ycugrd(nverts)는 intent(in)(55–60). |
| 62–80 | 시작 시 1행 SwanGridVert 루틴 안. `ient = 0` (64)과 ivert(65), vert 포인터(pointer)(67), 구조·실행부 표제(69–74). `if (ltrace) call strace (ient,'SwanGridVert')` (75), gridobject%vert_grid에 연결한다(79). [10-15 전수 검증 보완] |
| 81–108 | 시작 시 1행 SwanGridVert 루틴 안. `do ivert = 1, nverts` (83)은 `vert(ivert)%atti(VERTID) = ivert` (87), `vert(ivert)%atti(VMARKER) = min(1,vmark(ivert))` (91)이다. `vert(ivert)%atti(VBC) = 0` (95)은 아직 경계조건 점이 아니라는 초기값이다(93). `vert(ivert)%active = .true.` (99)로 활성 상태를 설정한다. 좌표 저장식은 `vert(ivert)%attr(VERTX) = xcugrd(ivert)` (103)과 `vert(ivert)%attr(VERTY) = ycugrd(ivert)` (104)이다. 루프·루틴 종료(106–108). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91: VMARKER는 min(1,vmark(ivert))로 설정한다. 음수 입력을 0으로 제한하는 max 연산은 없다.
