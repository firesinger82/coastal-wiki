import json,sys,os
j=json.load(open('_staging/recovery/scripts/pdfjobs.json'))[int(sys.argv[1])-1]
base=os.path.splitext(os.path.basename(j['path']))[0]
mk=f"_staging/recovery/extract/XBeach/marker/{base}/{base}.md"
print(f"""너는 PDF 판독 기록의 재판독자다(작업 디렉터리 /home/firesinger/coastal-wiki). 아래 기록 파일 1개만 고칠 수 있다. 다른 파일은 만들거나 고치지 않는다(단, 확대 이미지는 _staging/recovery/scripts/fable/ 아래에만 임시로 만들 수 있다). git을 쓰지 않는다.

원본 PDF: {j['path']} ({j['a']}–{j['b']}쪽, 전체 {j['total']}쪽)
고칠 기록: {j['out']}  (쪽마다 `| p.N ... | 내용 |` 한 행. 앞선 판독자가 썼고 일부는 이미 검증 정정됨)
기계 판독 초안(Marker OCR, 수식 LaTeX 포함): {mk}  — 쪽 구분자 `{{N-1}}------` 로 나뉜 markdown(PDF N쪽 = `{{N-1}}`, 0부터 셈). 이 초안은 참고일 뿐 정답이 아니다(괄호·분수 구조가 가끔 틀림).

할 일 — 범위의 모든 쪽에 대해:
1. Read 도구(pages 인자, 한 번에 1~3쪽)로 쪽 이미지를 직접 본다. 수식·작은 첨자가 있으면 `pdftoppm -r 300 -f N -l N -png <PDF> <scratchpad/fable/이름>`으로 렌더해 Read로 확대해 본다.
2. 그 쪽의 기록 행을 이미지와 대조한다. Marker 초안의 같은 쪽과도 비교해, 기록과 Marker가 다른 곳은 반드시 이미지로 판정한다.
3. 기록을 고친다:
   - 수식: 이미지에 인쇄된 그대로의 LaTeX(위·아래 첨자, 분자/분모, 부호, 상선, 식 번호). ★원문 인쇄가 틀려 보여도 고치지 않고 인쇄 그대로 옮기고, 틀려 보인다는 점은 끝 절 "판독 중 확인된 사실"에 적는다. 빠진 연산자를 채우지 않는다.
   - 매개변수 이름·기본값·범위·단위, 적용 조건은 원문 그대로.
   - 한국어 설명이 원문과 반대·과장·누락이면 고친다(예: non-erodible ↔ erodible).
   - 인용 `원문 문장` (p.N)이 없는 쪽(텍스트가 있는 쪽)은 6단어 이상 본문 문장 하나를 추가한다(머리말·바닥글 제외).
   - 고친 행 끝에 `[10-02 fable 재판독]`을 붙인다. 이미 맞는 행은 `[10-02 fable 재판독: 일치]`만 붙인다.
   - 이미지로도 판단할 수 없으면 추측하지 말고 `[원문 인쇄 판독 불가]`로 적는다.
4. 표의 행 수(쪽 수)와 frontmatter는 바꾸지 않는다. frontmatter에 `reread_by: claude-fable (2026-10-02, Marker 대조)` 한 줄만 추가한다.

보고(한국어, 250단어 이내): 쪽 수, 고친 쪽 수와 주요 정정(무엇을 무엇으로), Marker와 기록이 달랐을 때 어느 쪽이 맞았는지 대략 비율, 판독 불가 항목.""")
