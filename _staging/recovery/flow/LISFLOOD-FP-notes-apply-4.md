---
title: "LISFLOOD-FP 노트 반영 기록 4"
model: LISFLOOD-FP
canonical_source: self
citation_status: verified
verification_method: "2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-10-21
---

# LISFLOOD-FP 노트 반영 기록 4

작업 대상은 [배정표](../assign/LISFLOOD-FP-note-job-4.tsv)에 적힌 두 노트다.

## 반영 상태

| 파일 | 배정표 행 수 | 반영 행 수 | 상태 |
|---|---:|---:|---|
| [lisflood-fp-channel-sgc.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md) | 112 | 112 | 완료 |
| [lisflood-fp-mwdg2-adaptive-mra.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md) | 80 | 80 | 완료 |

파일별 추가·수정 줄 범위와 수정안 행 ID는 각 노트 반영을 마칠 때 덧붙인다.

## 하도·구조 노트 반영 결과

대상은 [lisflood-fp-channel-sgc.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md)다. 배정표에서 이 파일에 지정한 112개 행을 반영했다.

| 내용 | 추가·수정 위치 | 반영한 수정안 행 ID |
|---|---|---|
| frontmatter | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:7–12` | last_source_check 추가. verification_method에 recovery 대조 반영을 덧붙임. citation_status 유지. |
| 기본 SGC 경로·단면 빌드 조건 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:21`, `:35` | theory:LT1-408; files-output:LI2-062·312; docx-manual:LV1-248·270·277; cpu-gpu-acc-adaptive:LG2-013·017 |
| beta 초기값·SGCA_mode·pram | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:55`, `:68`, `:74` | theory:LT1-409; par:LI1-363; files-output:LI2-059–066·311–313; docx-manual:LV1-250; cpu-gpu-acc-adaptive:LG2-015 |
| 옛 SGC 결함 후보·hotstart | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:94`, `:114` | cpu-gpu-acc-adaptive:LG2-018·019·020 |
| 운동파 시간 갱신·확산파 반복 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:127–129`, `:137` | 최종 결론 bridge-docx:LB1-219; theory:LT1-320 |
| 공극률 입력·PBVAR | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:162–164` | files-output:LI2-046–048·307–308·347 |
| 고전 구조물·Fast 교량·문서식·방향 태그·crest | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:170`, `:179`, `:185`, `:193–195` | bridge-docx:LB1-395·396; theory:LT1-411; docx-manual:LV1-220·224; files-output:LI2-069–079·346 |
| 관련 링크 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:218` | 상대 링크로 변경. |
| 판·근거 안내와 대조 표 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md:220–343` | 배정표 112개 행. 표 데이터는 232–343행. |

LT1-410과 callflow §6.1이 유지하도록 한 RESULT_CHECK 설명은 원문을 보존했다. LT1-411이 유지하도록 한 자유·잠김월류 구현식도 원문을 보존했다. 파일·출력 보고서가 유지하도록 한 y방향 교량의 SGC 조건도 원문을 보존했다.

반영 행 수는 배정표의 이 파일 지정 행 수와 같다. 중복 행은 없다. 넣지 않은 배정 행과 미반영 수정안 행은 없다.

## 적응격자 노트 반영 결과

대상은 [lisflood-fp-mwdg2-adaptive-mra.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md)다. 배정표에서 이 파일에 지정한 80개 행을 반영했다.

| 내용 | 추가·수정 위치 | 반영한 수정안 행 ID |
|---|---|---|
| frontmatter | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:7–14` | last_source_check 추가. verification_method에 recovery 대조 반영을 덧붙임. citation_status 유지. |
| 분석 판·진입점·utility | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:20–21` | build-83:LN1-247; callflow §6.2의 adaptive 수정안; cpu-gpu-acc-adaptive:LG2-035 |
| 실제 노드 좌표·벽 preflag | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:25`, `:46` | cpu-gpu-acc-adaptive §4.3의 24·45행 수정안(LG2-037·038·093); par:LI1-275 |
| qy 정규화·분모 하한 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:49–50` | theory:LT1-420; bridge-docx:LB1-407; docx-manual:LV1-293; cpu-gpu-acc-adaptive:LG2-032·033 |
| 별도 기본값·파서·사례 번호 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:56–57` | par:LI1-364·365; bridge-docx:LB1-406; docx-manual:LV1-279–282; callflow:RF-029; cpu-gpu-acc-adaptive:LG2-056·092–094 |
| 조건부 결함 후보 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:59–66` | cpu-gpu-acc-adaptive:LG2-039·045·065·068·070·087 |
| 입력·출력 지원·stage와 raster | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:68–72` | files-output:LI2-318·331–342의 adaptive 범위(LI2-340); par:LI1-278; cpu-gpu-acc-adaptive:LG2-086 |
| 판 출처·관련 링크·acc_nugrid 설명 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:76–84` | build-83:LN1-247; cpu-gpu-acc-adaptive §4.3의 64행 수정안(LG2-029–031·035) |
| 판·근거 안내와 대조 표 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:86–177` | 배정표 80개 행. 표 데이터는 98–177행. |

par:LI1-365가 유지하도록 한 tol_h와 DepthThresh의 변수 구분을 원문으로 보존했다. callflow §6.1이 유지하도록 한 첫 시간 간격 0.001 s 설명도 원문으로 보존했다.

반영 행 수는 배정표의 이 파일 지정 행 수와 같다. 중복 행은 없다. 넣지 않은 배정 행과 미반영 수정안 행은 없다.

## 최종 확인

[배정표](../assign/LISFLOOD-FP-note-job-4.tsv)의 192개 행은 하도·구조 노트 112개 행과 적응격자 노트 80개 행으로 반영됐다. 두 노트의 행 ID와 최종 분류는 [최종 결론 배정표](../assign/LISFLOOD-FP-final-conclusions.tsv)와 일치한다. 각 표 행에는 최종 근거의 결론 문장과 확인한 원문이 들어 있다.

추가·수정 위치는 위 표에 기록했다. 두 노트의 상대 링크는 모두 대상 파일이나 디렉터리로 연결된다. 자기 노트 인용은 반영 전 커밋 bf804e23으로 고정했다. 유지 지정 문장은 반영 전 커밋의 원문과 일치한다. 대조 표는 모두 6열이다. 두 노트의 diff 공백 검사를 통과했다.

넣지 않은 배정 행은 0개다. 중복 행은 0개다. 미반영 수정안 행은 0개다.
