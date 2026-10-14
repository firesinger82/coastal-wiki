---
file: models/SWASH/raw/source_code/swash/src/SwanGriddata.ftn90
lines: 86
sha256: 6dd1ea15a54d3fa1afd71ef11781f1c9dcf57640863dc8a93559b41a3b83d7d7
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanGriddata.ftn90 — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | SwanGriddata 모듈 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). 비구조 격자(unstructured grid) 자료를 보유하며 격자 생성기(grid generator)가 채운다는 목적·방법(38–44). 사용 모듈 없음 주석(46–48), implicit none(50), 매개변수 표제(52–53). |
| 54–69 | 시작 시 1행 SwanGriddata 모듈 안. 생성기 식별 상수는 `integer, parameter :: meth_adcirc   = 1 !` (54), `integer, parameter :: meth_triangle = 2 !` (55), `integer, parameter :: meth_easy     = 3 !` (56)이다. grid_generator(60), 부분영역(subdomain) 셀 수 ncells·경계 셀 수 ncellsb·전역(global) 셀 수 ncellsg(62–64), 면(face) 수 nfaces·경계 면 수 nfacesb(65–66), 부분영역·전역 꼭짓점(vertex) 수 nverts·nvertsg(67–68)를 선언한다. |
| 70–86 | 시작 시 1행 SwanGriddata 모듈 안. kvertc·kvertf는 save allocatable 2차원 정수 배열(70–71). ivertg는 전역 꼭짓점 인덱스, vmark는 경계 마커(marker)의 save allocatable 1차원 배열(73–74). maxgsiz·mingsiz는 최대·최소 격자 크기(76–77). xcugrd·ycugrd와 전역 좌표 xcugrdgl·ycugrdgl은 save allocatable 실수 배열(79–82). 실행부 표제와 모듈 종료(83–86). 실행 루틴은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60–68·76–77: 격자 생성기·개수·격자 크기 변수의 선언에는 초기값 대입이 없다.
