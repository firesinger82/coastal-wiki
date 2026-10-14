---
title: ROMS 대조 결론 노트 반영 — 배정 18
citation_status: verified
last_source_check: "2026-10-14 (recovery 대조 반영)"
verification_method: "2026-10-14 ROMS recovery 대조 보고서 반영"
---

# ROMS 대조 결론 노트 반영 — 배정 18

배정 기준은 [note-job-18.tsv](../assign/note-job-18.tsv)다.
배정표의 `roms_wec.md` 행 수는 116개다.
배정표의 `roms_nesting.md` 행 수는 50개다.
배정표의 `roms_equation_of_state.md` 행 수는 7개다.
`roms-coawst-applications-review.md`에는 배정된 차이 행이 없다.

파일별 반영 결과는 작업을 마친 순서대로 아래에 기록한다.

## roms_wec.md

대상 파일: [models/ROMS/source-analysis/roms_wec.md](../../../models/ROMS/source-analysis/roms_wec.md).

- frontmatter 추가·수정: `models/ROMS/source-analysis/roms_wec.md:6–7`.
- SHOREFACE 판 차이 추가: `models/ROMS/source-analysis/roms_wec.md:46–49`.
- SWAN 결합 주기 수정: `models/ROMS/source-analysis/roms_wec.md:149–156`.
- 수신 변환·송신 속도 설명 추가·수정: `models/ROMS/source-analysis/roms_wec.md:171–185`.
- 차이 절 추가: `models/ROMS/source-analysis/roms_wec.md:237–361`.
- 넣은 차이 행 수는 116개다.
- 배정표의 이 파일 행 수는 116개다.
- 반영한 수정안 행 ID: `build-options-history:RBH-3508`, `testcases:RT1-1527`, `coupling-nesting-parallel:RCN-1973`, `coupling-nesting-parallel:RCN-1974`, `coupling-nesting-parallel:RCN-1975`, `coupling-nesting-parallel:RCN-1976`.
- RBH-3508의 WEC·WAV_COUPLING 파생 조건은 유지했다.
- RT1-1527의 현재 사례 CPP 옵션은 유지했다.
- RCN-1974의 수신 변수 이름은 유지했다.
- RCN-1976의 현재 HEAD에 관한 WW3·WAM 설명은 유지했다.
- 넣지 않은 배정 행은 없다.
- 반영하지 않은 수정안 행은 없다.
- 배정표와 차이 표를 대조한 누락·초과·중복 행은 없다.

## roms_nesting.md

대상 파일: [models/ROMS/source-analysis/roms_nesting.md](../../../models/ROMS/source-analysis/roms_nesting.md).

- frontmatter 추가·수정: `models/ROMS/source-analysis/roms_nesting.md:6–7`.
- 접촉 파일 검사·초기화 설명 수정: `models/ROMS/source-analysis/roms_nesting.md:33–37`.
- 접촉 파일 가중치·도구 이름 설명 수정: `models/ROMS/source-analysis/roms_nesting.md:52–56`.
- tracer flux 보정 조건·계산 설명 수정: `models/ROMS/source-analysis/roms_nesting.md:69–72`.
- 시간 비율 계산 추가: `models/ROMS/source-analysis/roms_nesting.md:88–89`.
- 단일 격자 입력 예와 중첩 구성 조건 수정: `models/ROMS/source-analysis/roms_nesting.md:110–137`.
- 도구 함수 이름 수정: `models/ROMS/source-analysis/roms_nesting.md:141`.
- 차이 절 추가: `models/ROMS/source-analysis/roms_nesting.md:155–213`.
- 넣은 차이 행 수는 50개다.
- 배정표의 이 파일 행 수는 50개다.
- 반영한 수정안 행 ID: `coupling-nesting-parallel:RCN-1963`, `coupling-nesting-parallel:RCN-1964`, `coupling-nesting-parallel:RCN-1965`, `coupling-nesting-parallel:RCN-1966`, `coupling-nesting-parallel:RCN-1967`, `coupling-nesting-parallel:RCN-1968`, `coupling-nesting-parallel:RCN-1969`, `coupling-nesting-parallel:RCN-1970`, `coupling-nesting-parallel:RCN-1971`, `coupling-nesting-parallel:RCN-1972`, `testcases:RT1-1528`, `tools-guides:RTG-1988`.
- RCN-1963의 중첩 옵션 역할은 유지했다.
- RCN-1966의 가중치 개수 표는 유지했다.
- RT1-1528의 두 시험 입력이 단일 격자라는 설명은 유지했다.
- RTG-1988의 도구 이름 정정은 본문에 반영했다.
- H 차이 행은 표에 추가하지 않았다.
- 넣지 않은 배정 행은 없다.
- 반영하지 않은 수정안 행은 없다.
- 배정표와 차이 표를 대조한 누락·초과·중복 행은 없다.

## roms_equation_of_state.md

대상 파일: [models/ROMS/source-analysis/roms_equation_of_state.md](../../../models/ROMS/source-analysis/roms_equation_of_state.md).

- frontmatter 추가·수정: `models/ROMS/source-analysis/roms_equation_of_state.md:6–7`.
- 해결된 미커버 표현·노트 연결 수정: `models/ROMS/source-analysis/roms_equation_of_state.md:22`, `models/ROMS/source-analysis/roms_equation_of_state.md:66`.
- 선형식의 물리 밀도·저장 편차 설명 수정: `models/ROMS/source-analysis/roms_equation_of_state.md:28`, `models/ROMS/source-analysis/roms_equation_of_state.md:92–95`, `models/ROMS/source-analysis/roms_equation_of_state.md:105`.
- 상대 링크 수정: `models/ROMS/source-analysis/roms_equation_of_state.md:40`, `models/ROMS/source-analysis/roms_equation_of_state.md:77`, `models/ROMS/source-analysis/roms_equation_of_state.md:119–122`.
- 차이 절 추가: `models/ROMS/source-analysis/roms_equation_of_state.md:124–139`.
- 넣은 차이 행 수는 7개다.
- 배정표의 이 파일 행 수는 7개다.
- 반영한 수정안 행 ID: `theory-numerics:RTN-391`.
- 넣지 않은 배정 행은 없다.
- 반영하지 않은 수정안 행은 없다.
- 배정표와 차이 표를 대조한 누락·초과·중복 행은 없다.

## roms-coawst-applications-review.md

대상 파일: [models/ROMS/web-refs/roms-coawst-applications-review.md](../../../models/ROMS/web-refs/roms-coawst-applications-review.md).

- 추가·수정 줄 범위는 없다.
- 넣은 차이 행 수는 0개다.
- 배정표의 이 파일 행 수는 0개다.
- 이 파일을 직접 가리키는 수정안 행은 없다.
- 파일 내용은 작업 시작 시 내용과 같다.
- 차이 절을 만들지 않았다.
- 넣지 않은 배정 행은 없다.
- 반영하지 않은 수정안 행은 없다.

## 최종 대조 결과

- 배정표의 전체 행 수는 173개다.
- 세 노트의 차이 표 행 수 합계는 173개다.
- 파일별 행 수는 배정표의 116개·50개·7개와 같다.
- 보고서 수정안 절에서 담당 노트를 직접 가리키는 19행을 반영했다.
- 행 ID·배정 파일·분류·결론 문장을 보고서 최종본과 대조했다.
- A 행에는 git 판정의 커밋 HASH와 날짜를 넣었다.
- E 행에는 보고서의 근거 강도를 넣었다.
- 수정한 노트의 citation_status는 유지했다.
- 수정한 노트의 frontmatter 날짜와 verification_method를 갱신했다.
- 표 열 수·상대 링크·금지 문자열 검사에서 오류는 없다.
- 넣지 않은 배정 행은 없다.
- 반영하지 않은 수정안 행은 없다.
