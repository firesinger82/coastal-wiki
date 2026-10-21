# LISFLOOD-FP 노트 반영 기록 1

배정표: [LISFLOOD-FP-note-job-1.tsv](../assign/LISFLOOD-FP-note-job-1.tsv).
최종 결론: [LISFLOOD-FP-final-conclusions.tsv](../assign/LISFLOOD-FP-final-conclusions.tsv).

대상은 `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md`와 `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md`이다.
파일별 반영 결과는 각 파일을 마친 뒤 아래에 기록한다.

## 차이 노트 반영 완료

- 파일: [lisflood-fp-io-boundary-differences.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md).
- 추가 범위: `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md:1–304`.
- 차이 표 범위: `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md:61–304`.
- 넣은 행 수: 배정표의 244행 중 244행이다.
- 보고서별 행 수: bridge-docx 68행, build-83 7행, callflow 7행, cpu-gpu-acc-adaptive 9행, cpu-gpu-swe 3행, docx-manual 45행, files-output 38행, par 50행, theory 17행이다.
- 각 행의 결론 칸은 배정표가 지정한 재검증 파일에 연결했다.
- 각 행의 코드 원문 칸에 재검증 행의 “확인한 원문”을 함께 옮겼다.
- 기존 IO 노트 수정안 중 배정된 행도 표에 포함했다.
- 담당 본문 수정안의 반영 위치는 다음 파일 완료 기록에 적는다.
- 넣지 않은 배정 행: 없다.
- 배정표와 대조한 중복 행: 없다.
- 배정표 밖에서 추가한 표 행: 없다.

## IO 본문 반영 완료

파일: [lisflood-fp-io-boundary.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md).
이 파일에 넣은 차이 표 행은 0행이다.

추가·수정 범위는 다음과 같다.

- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:7–8`, `:12`, `:18–20`: frontmatter와 상대 링크 및 기준 판을 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:25–107`: 구성 읽기 순서, 파서 길이, Qfile, 해법 플래그, 출력 키워드, verbose 검사, GPU 빌드 조건을 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:143–153`: bdy 누락 이름과 NULL 보간 후보 및 시계열 범위 밖 처리를 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:186–225`: 체크포인트 판 검사와 저장 배열 및 driver별 호출을 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:233–274`: 증발 손실 재사용, CPU·GPU 강우, routing 조건과 수면차 제한을 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:286–301`: ASCII 대체 헤더와 binary 자료 길이 및 Windows 시작 파일 후보를 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:317–320`: 표시용 DEM의 기본 출력과 SGCz를 반영했다.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:331–333`, `:337`, `:339–340`: 체크포인트 요약과 차이 표 링크 및 주의 문장을 고쳤다.

반영한 노트 수정안 행은 다음과 같다.

- theory: LT1-417.
- par: LI1-356, LI1-357, LI1-358, LI1-359, LI1-360, LI1-361.
- files-output: LI2-039–040, LI2-301–303, LI2-100–101, LI2-343–345, LI2-127, LI2-145–155, LI2-348–349, LI2-210–213.
- docx-manual: LV1-264, LV1-265, LV1-191–194, LV1-266, LV1-014, LV1-023, LV1-268.
- bridge-docx: LB1-400, LB1-401, LB1-402.
- build-83: LN1-241.
- cpu-gpu-acc-adaptive: §4.4의 IO 수정안을 반영했다. 근거 행은 LG2-073–078과 LG2-096이다.
- callflow: RF-019, RF-020, RF-021과 §6.2의 IO 수정안을 반영했다.

LI1-362의 기본 체크포인트 우선 설명은 유지했다.
이 설명에 dirroot 경로를 추가했다.
LI2-102–103이 코드와 맞다고 한 startelev 설명은 유지했다.
LI2-210–213이 맞다고 한 debug 마스크 설명은 유지했다.
고친 본문 문장에는 `[10-21 대조 정정]`을 붙였다.
고친 기존 표 행에는 마지막 칸에 정정 표시를 붙였다.
넣지 않은 담당 노트 수정안 행은 없다.

## 최종 확인

배정표의 244행과 새 차이 표의 244행은 행 ID와 순서가 같다.
최종 분류와 지정 근거 파일은 244행 모두 일치한다.
재검증 파일의 결론 문장은 244행 모두 대응한다.
재검증 파일의 “확인한 원문”은 244행 모두 대응한다.
LI1-316의 결론에서 작업 한계 문장만 제외했다.
LN1-128·129에는 사용자 지시의 “8.2 결함, 8.3에서 고침”을 덧붙였다.
LV1-023·024의 PDF 대조 쪽수는 재검증 기록에 따라 p.13으로 고쳤다.
LT1-306·316·318의 문서 대조 문구는 재검증 기록이 정한 누락 범위로 좁혔다.
새 차이 표는 모든 행이 6열이다.
상대 링크의 파일 경로 오류는 0건이다.
허용된 두 노트와 이 기록 파일만 작성했다.
`git diff --check`는 통과했다.
넣지 않은 배정 행과 담당 수정안 행은 없다.
