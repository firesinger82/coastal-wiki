---
title: Celeris 노트 대조 반영 9
citation_status: verified
last_source_check: 2026-11-04 (recovery 대조 반영)
verification_method: 2026-11-04 Celeris recovery 대조 보고서 반영
---

# Celeris 노트 대조 반영 9

배정 기준: [Celeris-note-job-9.tsv](../assign/Celeris-note-job-9.tsv).

## celeris-render.md

- 추가·수정: `models/Celeris/source-analysis/celeris-render.md:5–6`(frontmatter), `models/Celeris/source-analysis/celeris-render.md:13`(논문 그림의 범위), `models/Celeris/source-analysis/celeris-render.md:36–45`(높이 입력·판별 캐시), `models/Celeris/source-analysis/celeris-render.md:76–79`(f32·색상 배열·Base 타일 구분), `models/Celeris/source-analysis/celeris-render.md:120–139`(높이 입력 그림·설명), `models/Celeris/source-analysis/celeris-render.md:142–163`(차이 표).
- 표 행 수: 배정표 14행 중 14행을 넣었다.
- 반영한 수정안: docs-architecture:CD1-1351·CD1-1352(기존 캐시 생성·건조 셀 조건 유지), docs-source:CD2-475, tavakkol2017:CP1-157, tavakkol2020:CP2-179(최종 분류를 따라 표시 전용 사항으로 서술), lynett2026:CP3-081·076, transect:CT1-367·CT1-368, callflow:일치·렌더 위치(유지).
- 색상 배열 표시 문제를 E 후보로 새로 분류하지 않았다.
- 넣지 않은 배정 행: 없음.

## celeris-architecture-and-config.md

- 추가·수정: `models/Celeris/manual-notes/celeris-architecture-and-config.md:71–72`(직접 입력·파생값 구분), `models/Celeris/manual-notes/celeris-architecture-and-config.md:137`(퇴적물 단계 전달 구분), `models/Celeris/manual-notes/celeris-architecture-and-config.md:217–218`(Base 계승 범위), `models/Celeris/manual-notes/celeris-architecture-and-config.md:236–272`(차이 표).
- 표 행 수: 배정표 29행 중 29행을 넣었다.
- 반영한 수정안: docs-architecture:CD1-1310–CD1-1326, docs-source:CD2-476·CD2-477, tavakkol2017:CP1-140·CP1-159, tavakkol2020:CP2-165·CP2-174·CP2-175, lynett2026:CP3-112, transect:CT1-369, callflow:RF-001·RF-021.
- 이미 들어 있던 설정 로딩·키 이름·dt·오버레이 호출·CR/PCR·2019 문헌 정정은 확인 후 유지했다.
- frontmatter의 지정된 last_source_check와 verification_method 구절은 이미 들어 있어 유지했다.
- 넣지 않은 배정 행: 없음.

## celeris-pipeline-graph.md

- 추가·수정: `models/Celeris/source-analysis/celeris-pipeline-graph.md:5–6`(frontmatter), `models/Celeris/source-analysis/celeris-pipeline-graph.md:14–187`(본문·호출 위치 정정), `models/Celeris/source-analysis/celeris-pipeline-graph.md:197–318`(원본 Mermaid 세 그림), `models/Celeris/source-analysis/celeris-pipeline-graph.md:320–359`(차이 표).
- 표 행 수: 배정표 33행 중 33행을 넣었다.
- 반영한 수정안: docs-architecture:CD1-1334·CD1-1335(유지)·CD1-1336·CD1-1337(유지), docs-source:CD2-460·CD2-463·CD2-464·CD2-466(호출 순서 유지), tavakkol2017:CP1-156, tavakkol2020:CP2-167(조건 유지와 dt 구분), lynett2026:CP3-116·CP3-041·090·099·108의 호출 위치 수정, transect:CT1-357, callflow:RF-015·일치/pipeline 단계(유지)·state swap 용어 정리·Claude 렌더 확인 (11-04).
- 그림 위에 지정된 렌더 확인 문장을 넣었다.
- 넣지 않은 배정 행: 없음.

## celeris-sediment.md

- 추가·수정: `models/Celeris/source-analysis/celeris-sediment.md:5–6`(frontmatter), `models/Celeris/source-analysis/celeris-sediment.md:20–166`(본문 정정), `models/Celeris/source-analysis/celeris-sediment.md:182–232`(차이 표).
- 표 행 수: 배정표 43행 중 43행을 넣었다.
- 반영한 수정안: docs-architecture:CD1-1345·CD1-1346·CD1-1347·CD1-1348, docs-source:CD2-471·CD2-472·CD2-473(기존 설명 유지), tavakkol2017:CP1-155(기본 비활성·조건부 호출 유지와 출처 구분), tavakkol2020:CP2-172, lynett2026:CP3-091–096, transect:CT1-363·CT1-364·CT1-365, callflow:RF-012.
- 넣지 않은 배정 행: 없음.

## celeris-fv-reconstruction.md

- 추가·수정: `models/Celeris/source-analysis/celeris-fv-reconstruction.md:5–6`(frontmatter), `models/Celeris/source-analysis/celeris-fv-reconstruction.md:28–203`(본문 정정), `models/Celeris/source-analysis/celeris-fv-reconstruction.md:206–249`(차이 표).
- 표 행 수: 배정표 36행 중 36행을 넣었다.
- 반영한 수정안: docs-architecture:CD1-1339(유지)·CD1-1340·CD1-1341, docs-source:CD2-467(유지), tavakkol2017:CP1-144·CP1-145·CP1-149, tavakkol2020:CP2-169(기존 설명 유지와 상태 변수 구분), lynett2026:CP3-115, transect:CT1-359·CT1-360, callflow:일치·FV 연결(유지).
- 넣지 않은 배정 행: 없음.


## 최종 확인

| 파일 | 배정표 행 수 | 넣은 행 수 |
|---|---:|---:|
| [celeris-sediment.md](../../../models/Celeris/source-analysis/celeris-sediment.md) | 43 | 43 |
| [celeris-fv-reconstruction.md](../../../models/Celeris/source-analysis/celeris-fv-reconstruction.md) | 36 | 36 |
| [celeris-pipeline-graph.md](../../../models/Celeris/source-analysis/celeris-pipeline-graph.md) | 33 | 33 |
| [celeris-architecture-and-config.md](../../../models/Celeris/manual-notes/celeris-architecture-and-config.md) | 29 | 29 |
| [celeris-render.md](../../../models/Celeris/source-analysis/celeris-render.md) | 14 | 14 |
| 합계 | 155 | 155 |

배정표에서 센 155행의 ID와 대상 파일이 노트 표와 일치한다.
155행의 최종 분류는 Celeris-final-conclusions.tsv와 일치한다.
155행의 결론 문장과 확인한 원문 위치는 지정된 검증 파일의 같은 행과 일치한다.
인용 경로·논문 이름·백틱·표 안 세로선 표기는 요청된 형식으로 정규화했다.
A 행은 결론 칸에 문서 판 또는 근거 커밋을 적었다.
E 행은 결론 칸에 강도를 적었다.
비활성 경로의 E 행은 현재 호출되지 않는다는 사실을 적었다.
H·일치 분류는 차이 표에 추가하지 않았다.
기존 본문 정정과 유지 항목은 위 파일별 수정안 목록에 기록했다.
세 Mermaid 블록은 callflow §4의 원문과 글자 단위로 일치한다.
세 그림 위에는 지정된 렌더 확인 문장이 각각 있다.
각 표는 여섯 열이며 코드 블록 밖에 있다.
상대 링크의 대상 파일이 존재한다.
금지된 경로·문자열과 해결된 미완료 표시는 없다.
넣지 않은 배정 행은 없다.
