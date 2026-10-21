---
title: LISFLOOD-FP CUDA GPU 노트 대조 반영 기록
model: LISFLOOD-FP
citation_status: verified
last_source_check: "2026-10-21 (recovery 대조 반영)"
verification_method: "2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
---

# LISFLOOD-FP CUDA GPU 노트 대조 반영 기록

배정 근거는 [LISFLOOD-FP-note-job-3.tsv](../assign/LISFLOOD-FP-note-job-3.tsv)다.
최종 분류는 [LISFLOOD-FP-final-conclusions.tsv](../assign/LISFLOOD-FP-final-conclusions.tsv)를 따른다.
결론 문장과 원문 인용은 배정표에 지정된 최종 근거 파일의 같은 행 ID를 따른다.

대상 파일은 [lisflood-fp-cuda-gpu.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md)다.
현재 상태는 CUDA 노트 반영 완료다.

배정표의 대상 행은 120개다.
기존 CUDA 노트에는 배정 행 표가 없다.
본문 수정안의 대상은 각 보고서의 CUDA 노트 인용 행과 callflow의 CUDA 노트 수정 문단이다.
노트 자기 인용은 반영 전 커밋 `bf804e23`의 줄 번호로 고정한다.

## CUDA 노트 완료 기록 (2026-10-21)

대상 파일은 `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md`다.
차이 표에 넣은 행 수는 배정표의 120개와 같다.
차이 표의 데이터 행은 `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:343–462`다.
기존 `citation_status: verified`를 유지했다.
`last_source_check`는 `2026-10-21 (recovery 대조 반영)`이다.
`verification_method`에 `2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영`을 덧붙였다.

| 추가·수정 줄 범위 | 반영 내용 |
|---|---|
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:7–35` | frontmatter, 상대 링크, CUDA 해법 목록, 별도 Metal 백엔드 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:111–130` | FV1 비분리 갱신, 운동량 식의 괄호, 8.3 reader 동기화 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:158–162` | ACC dt_field 할당과 최초값 결함 후보 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:181–215` | 수위형 점 원천, 경계의 내부·외부 상태, ACC 지역 유출 보정, NoData 판 구분 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:223–236` | RK 질량 장부, 시간 분모, 초기 체적, 침수 면적, 강우·점 원천 집계 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:249–258` | 8.2 MaxField 결함, 8.3 device 배열과 host 복사, 잔존 정밀도 인수 후보 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:270–289` | 실제 종료 writer, 실행기별 입력·출력 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:293–313` | acc_nugrid 초기 격자, MW 필터, adaptive 재구성, 출력 정의 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:319–326` | 비분리 FV1과 해법별 HLL·관성식 구분 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:328–462` | 문서·코드 판, 최종 근거 링크, 배정 행 차이 표 |

### 보고서별 반영 행 수

아래 행 수는 배정표와 CUDA 노트의 행 ID 열에서 각각 셌다.

| 보고서 약칭 | 배정 행 수 | 넣은 행 수 | CUDA 노트의 줄 범위 |
|---|---:|---:|---|
| bridge-docx | 9 | 9 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:343–351` |
| build-83 | 10 | 10 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:352–361` |
| callflow | 6 | 6 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:362–367` |
| cpu-gpu-acc-adaptive | 36 | 36 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:368–403` |
| cpu-gpu-swe | 34 | 34 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:404–437` |
| docx-manual | 5 | 5 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:438–442` |
| files-output | 10 | 10 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:443–452` |
| par | 9 | 9 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:453–461` |
| theory | 1 | 1 | `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:462` |

합계는 배정 120행과 반영 120행이다.
배정표의 분류별 행 수는 A 7행, B 6행, C 63행, E 38행, F 6행이다.

### 반영한 본문 수정안

아래 행 ID는 보고서의 노트 수정안에서 CUDA 노트를 가리키는 행을 식별한다.
차이 표의 행 배정은 앞 절의 120행만 따른다.

| 보고서 | 반영한 수정안 행 ID | CUDA 노트의 반영 위치 |
|---|---|---|
| theory §4 | LT1-419 | 18–35행, 319–326행 |
| par §4 | LI1-369 | 207–215행, 249–258행 |
| files-output §4 | LI2-318, LI2-331–342, LI2-352 | 249–289행, 305–313행, 해당 배정 행 표 |
| docx-manual §4.2 | LV1-286–289·295 | 111–130행, 249–289행, 해당 배정 행 표 |
| bridge-docx §4 | LB1-404·405 | 7–35행, 249–258행 |
| build-83 §4 | LN1-242·243·244 | 18–35행, 119–126행, 249–258행 |
| cpu-gpu-swe §4 | LG1-011의 두 수정안, LG1-024, LG1-021–023, LG1-058·127–129·134·142·145–146, LG1-100–108·137–141, LG1-155의 본문 수정안 | 18–35행, 111–130행, 181–215행, 223–289행, 319–326행, 해당 배정 행 표 |
| cpu-gpu-acc-adaptive §4.2·출력 추가안 | LG2-023·046·048·092, LG2-008·055, LG2-060, LG2-029–035·037, LG2-046–048·057·062–068·081–089, LG2-028 | 18–35행, 158–162행, 207–215행, 276–313행, 322–326행, 해당 배정 행 표 |
| callflow §6 | RF-014·016·018, CUDA 노트 수정 문단의 RF-023·024 | 18–35행, 119–126행, 249–258행, 293–313행, 319–326행 |

callflow의 8.3 동기화 설명은 방향 커널 내부의 barrier로 반영했다.
Metal FV1은 CUDA 분기의 자식이 아닌 별도 백엔드로 반영했다.
adaptive의 출력 설명은 leaf 평균과 위치별 모드 평가값을 구분한다.

### 대조 결과와 미반영 행

배정표의 행 ID와 노트 표의 행 ID가 모두 일치한다.
배정표의 최종 분류와 노트 표의 결론 열이 모두 일치한다.
최종 근거 파일의 결론 문장 120개를 노트 표와 대조했다.
차이 표의 결론 문장에 보탠 문구는 요청한 E 강도와 `8.2 결함, 8.3에서 고침` 표기이다.
E 38행의 결론 문장에 강도가 있다.
8.3에서 고친 E 11행에 `8.2 결함, 8.3에서 고침`을 적었다.
Markdown 파서는 차이 표를 머리행과 데이터 120행으로 읽는다.
Markdown 파서가 읽은 각 행의 열 수는 6개다.
코드 원문과 최종 확인 원문을 포함한 표 행 120개가 준비한 반영 문구와 일치한다.
넣지 않은 배정 행은 없다.
중복 행은 없다.
추가 배정 밖 차이 표 행은 없다.
노트와 이 기록의 상대 링크 대상은 모두 존재한다.
노트 자기 인용은 모두 `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md:N` 형식이다.
기록한 보고서별 행 수와 줄 범위는 현재 노트와 일치한다.
대상 노트의 `git diff --check`는 통과했다.
