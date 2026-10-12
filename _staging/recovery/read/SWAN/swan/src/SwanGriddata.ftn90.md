---
file: models/SWAN/raw/source_code/swan/src/SwanGriddata.ftn90
lines: 89
sha256: 1943a1a73c3bf50671255ce7e9b656f76a65ee71d73c4b0cf78eaf2e4f7136a1
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanGriddata.ftn90 — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `module SwanGriddata` 시작(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 비정형 격자 데이터를 담으며 격자 생성기가 데이터를 채운다는 목적·방법(38–44). 사용 모듈은 없다는 주석(46–48). `implicit none`(50). |
| 52–76 | 시작 시 1행 모듈 안. 격자 생성 방법 상수는 `integer, parameter :: meth_adcirc   = 1 !` (54); `integer, parameter :: meth_triangle = 2 !` (55); `integer, parameter :: meth_easy     = 3 !` (56)이다. `grid_generator`와 부분영역·전역 셀 수, 면 수, 부분영역·전역 꼭짓점 수를 선언한다(60–66). `kvertc,kvertf`는 저장·할당 가능 2차원 정수 배열이다(68–69). 전역 꼭짓점 대응 `ivertg`, 경계 표지 `vmark`는 1차원 배열이다(71–72). 예외 경계 표지 `excmark`와 격자 순회(sweep) 수 `nsweep` 선언(74–75). [10-13 전수 검증 정정] |
| 77–89 | 시작 시 1행 모듈 안. 사용자·파랑·바람 방향 정렬 `asort`, 격자 크기 최댓값·최솟값 `maxgsiz,mingsiz`, 사용자 순회 방향 `usort` 선언(77–80). 지역 좌표 `xcugrd,ycugrd`와 전역 좌표 `xcugrdgl,ycugrdgl`는 저장·할당 가능 1차원 실수 배열이다(82–85). 소스 안내 주석·모듈 종료(86–89). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
