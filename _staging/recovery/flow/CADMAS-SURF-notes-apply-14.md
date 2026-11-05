---
title: "CADMAS-SURF 노트 반영 기록 14"
canonical_source: self
citation_status: verified
note_author: Codex
note_date: 2026-11-04
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "배정표·최종 근거·보고서 수정안 대조. 2026-11-04 CADMAS-SURF recovery 대조 보고서 반영"
---

# CADMAS-SURF 노트 반영 기록 14

대상은 [배정표](../assign/CADMAS-SURF-note-job-14.tsv)의 134행이다.
최종 결론은 각 `CADMAS-SURF-conclusion-verify-*.md`의 같은 행 ID를 따른다.
세 노트의 반영 결과를 아래에 기록했다.

## cadmas-agent-evacuation-simulator.md

- 파일: `models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md`.
- frontmatter 수정: `models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md:2`, `models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md:6–7`.
- 본문 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md:19–65`.
- 대조 절 추가: `models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md:68–125`.
- 표 행 범위: `models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md:76–125`.
- 표 행 수: 배정표 50행과 반영 50행이 같다.
- 반영한 수정안 행 ID: agent:KA1-500·501·502·503·505·506·507·508·509·510·511·512·513·514·518, tutorials-build:KU1-818·907, callflow:RF-013·021.
- agent:KA1-504의 수중 감속식은 유지했다.
- 넣지 않은 배정 행: 없음.

## cadmas-surf3d-turbulence-and-porous-resistance.md

- 파일: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md`.
- frontmatter 수정: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:6–7`.
- 본문 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:72–87`.
- 대조 절 추가: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:92–142`.
- 표 행 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:100–142`.
- 표 행 수: 배정표 43행과 반영 43행이 같다.
- 반영한 수정안 행 ID: 3d-input:KS3-401, 3d-program:KS2-810·814·815, 3d-theory:KS1-715·716.
- 2f-theory:KF1-044에 연결된 GT 비활성 서술은 유지했다.
- 3d-theory:KS1-723의 GT 비활성 서술은 유지했다.
- 넣지 않은 배정 행: 없음.

## cadmas-surf3d-wave-generation-and-boundaries.md

- 파일: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md`.
- frontmatter 수정: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md:6–7`.
- 본문 수정: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md:51`.
- 대조 절 추가: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md:78–126`.
- 표 행 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md:86–126`.
- 표 행 수: 배정표 41행과 반영 41행이 같다.
- 반영한 수정안 행 ID: 3d-theory:KS1-717.
- 3d-theory:KS1-718은 최종 근거에서 일치이다. 기존 내장 고립파 selector 설명과 외부 행렬 설명을 유지했다.
- 넣지 않은 배정 행: 없음.

## 최종 확인

- 배정표의 고유 행 ID 134개와 세 표의 행 ID 134개가 일치한다.
- 배정 파일을 벗어난 행은 없다.
- 표는 각각 50행·43행·41행이다.
- 각 표 행은 지정한 6열이다.
- 최종 분류와 결론 문장은 각 근거 파일의 같은 행과 대조했다.
- A 행의 결론 문장에는 사본 diff 또는 수정자 표지 근거를 붙였다.
- E 행에는 최종 근거의 강도를 적었다.
- 코드 원문 인용 1,070개는 표기한 파일의 줄 범위 안에서 공백을 제외한 문자열이 일치한다.
- 세 노트의 상대 링크 대상은 모두 존재한다.
- 금지 경로·위키링크 문자열은 없다.
- 세 노트의 `git diff --check`는 오류가 없다.
- 넣지 않은 배정 행은 없다.
