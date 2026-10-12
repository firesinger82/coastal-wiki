---
file: models/SWAN/raw/source_code/swan/src/SwanGridVert.ftn90
lines: 108
sha256: 77fcd8639a1f0166b622a193133b4fcd1267a0bfaac094192bba13ffcf403949
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanGridVert.ftn90 — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | `SwanGridVert` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 비정형 격자의 꼭짓점 자료구조를 채우는 목적·방법(38–44). 통신·격자 객체 모듈과 `implicit none`(48–51). |
| 53–74 | 시작 시 1행 루틴 안. 꼭짓점 수, 경계 표지 `vmark(nverts)`, 좌표 배열 입력(55–60). 저장 추적 계수 `ient = 0`, 꼭짓점 순회 변수·객체 포인터 선언(64–67). 구조·소스 안내 주석(69–74). [10-13 전수 검증 정정] |
| 75–108 | 시작 시 1행 루틴 안. 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanGridVert')` (75)이다. 꼭짓점 객체 연결(79). `do ivert = 1, nverts`(83)에서 `vert(ivert)%atti(VERTID) = ivert`(87)로 ID를 인덱스로 설정한다. 경계 표지 식은 `vert(ivert)%atti(VMARKER) = min(1,vmark(ivert))` (91)이다. 경계조건점(boundary condition point) 표지 초기값은 `vert(ivert)%atti(VBC) = 0`(95)이다. 활성 초기값은 `vert(ivert)%active = .true.`(99)이다. 좌표 저장식은 `vert(ivert)%attr(VERTX) = xcugrd(ivert)`(103), `vert(ivert)%attr(VERTY) = ycugrd(ivert)`(104)이다. 루프·루틴 종료와 빈 줄(106–108). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91: 경계 표지는 `min(1,vmark(ivert))`로 계산한다. 이 식에는 0을 하한으로 제한하는 연산이 없다.
- 87–104: 이 루틴은 ID·경계 표지·경계조건 표지·활성 상태·좌표를 설정한다. 그 외 꼭짓점 객체 필드를 설정하는 대입은 이 파일에 없다.
