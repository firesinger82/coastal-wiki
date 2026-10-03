# Codex PDF page re-read prompt (usage: python3 codexreread.py N IMGDIR)  N = pdfjobs.json job number
import json, os, sys
j = json.load(open('_staging/recovery/scripts/pdfjobs.json'))[int(sys.argv[1]) - 1]
imgdir = sys.argv[2]
base = os.path.splitext(os.path.basename(j['path']))[0]
key = {'XBeach_manual_kingsday': ('kingsday', 3), 'XBeach_manual_master': ('master', 3), 'Parallellization_report': ('parallel', 2),
       'curvilinear grid properties': ('curvilinear', 2), 'adapted_front_0': ('adapted', 1)}[base]
imgs = '\n'.join(f'- {j["a"] + k}쪽: {imgdir}/{key[0]}-{j["a"] + k:0{key[1]}d}.png' for k in range(j['b'] - j['a'] + 1))
mk = f'_staging/recovery/extract/XBeach/marker/{base}/{base}.md'
print(f"""OBJECTIVE
PDF 판독 기록 1개를 쪽 이미지와 대조해 바로잡는다(재판독). 저장소 루트 = /home/firesinger/coastal-wiki.

원본 PDF: {j['path']} ({j['a']}–{j['b']}쪽, 전체 {j['total']}쪽)
고칠 기록: {j['out']}  (쪽마다 `| p.N ... | 내용 |` 한 행. 앞선 판독자가 썼다. 오류율이 높으니 모든 행을 의심하고 대조한다)
쪽 이미지(300 dpi PNG, 이미지 보기 도구로 직접 연다):
{imgs}
기계 판독 초안(Marker OCR): {mk} — 쪽 구분자 `{{N-1}}------` (PDF N쪽 = `{{N-1}}`). 참고용이며 정답이 아니다(괄호 구조 붕괴, p↔ρ 혼동이 잦다).

할 일 — 범위의 모든 쪽에 대해
1. 그 쪽 PNG를 연다. 작은 첨자는 확대해서 본다.
2. 기록 행을 이미지와 대조한다. 기록과 Marker가 다른 곳은 반드시 이미지로 판정한다.
3. 기록을 고친다.
   - 수식: 이미지에 인쇄된 그대로의 LaTeX(위·아래 첨자, 분자/분모, 부호, 상선, 식 번호). 원문이 틀려 보여도 고치지 않고 인쇄 그대로 옮긴다. 빠진 연산자를 채우지 않는다. 틀려 보이는 점은 끝 절 "판독 중 확인된 사실"에 적는다.
   - 매개변수 이름·기본값·범위·단위와 적용 조건은 원문 그대로.
   - 한국어 설명이 원문과 반대·과장·누락이면 고친다(예: non-erodible ↔ erodible).
   - 텍스트가 있는 쪽에 6단어 이상 원문 인용 `문장` (p.N)이 없으면 하나 추가한다(머리말·바닥글 제외).
   - 고친 행 끝에 `[10-03 codex 재판독]`, 맞는 행 끝에 `[10-03 codex 재판독: 일치]`를 붙인다. 이미지로도 판단할 수 없으면 `[원문 인쇄 판독 불가]`.
4. 표의 행 수와 기존 frontmatter는 유지하고, frontmatter에 `reread_by: codex gpt-6.1-sol (2026-10-03, 300dpi 이미지 + Marker 대조)` 한 줄만 추가한다.

SCOPE
- 쓰기 허용: 위 기록 파일 하나. 다른 파일은 만들거나 고치지 않는다. git 명령을 쓰지 않는다.

STOP CONDITION
- 범위의 모든 쪽을 대조하면 끝낸다. 어떤 쪽 이미지를 열 수 없으면 그 쪽은 고치지 말고 보고한다.

DELIVERABLE (한국어, 한 문장에 한 사실)
- 대조한 쪽 수, 고친 쪽 수와 주요 정정(무엇을 무엇으로), 기록과 Marker가 다를 때 어느 쪽이 맞았는지 대략 비율, 판독 불가 항목, 열지 못한 이미지.""")
