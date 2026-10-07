# Codex first-pass PDF page reading from 300 dpi page images
# usage: python3 codexpdfread.py JOBFILE N IMGDIR   (jobs: path,total,a,b,out,ext[,marker])
import json, os, sys, hashlib, datetime
j = json.load(open(sys.argv[1]))[int(sys.argv[2]) - 1]
imgdir = sys.argv[3]
base = os.path.splitext(os.path.basename(j['path']))[0]
w = len(str(j['total']))
sha = hashlib.sha256(open(j['path'], 'rb').read()).hexdigest()
D = datetime.date.today().isoformat()
imgs = '\n'.join(f'- {p}쪽: {imgdir}/{base}-{p:0{w}d}.png' for p in range(j['a'], j['b'] + 1))
ext = f"_staging/recovery/extract/{j['model']}/pdf-md/{j['ext']}.md"
mk = j.get('marker')
mkline = (f"\n기계 판독 초안(Marker OCR): {mk} — 쪽 구분자 `{{N-1}}------` (PDF N쪽 = `{{N-1}}`). 수식 참고용이며 정답이 아니다(괄호 구조 붕괴, p↔ρ 혼동이 잦다). 이미지와 다르면 이미지를 따른다." if mk else "")
print(f"""OBJECTIVE
PDF의 지정 쪽을 쪽 이미지로 직접 보고 판독 기록 1개를 새로 쓴다. 저장소 루트 = /home/firesinger/coastal-wiki.

원본 PDF: {j['path']} ({j['a']}–{j['b']}쪽, 전체 {j['total']}쪽, sha256 {sha})
출력 파일(이 파일만 새로 만든다): {j['out']}
쪽 이미지(300 dpi PNG, 이미지 보기 도구로 직접 연다. 작은 첨자는 확대해서 본다):
{imgs}
텍스트 추출본(opendataloader, 쪽 구분 `<<<PAGE N>>>`): {ext} — 원문 인용 문장을 옮길 때 철자 확인용. 표·수식 구조는 이미지를 따른다.{mkline}

기록 형식 (한국어)
---
file: {j['path']}
pages_total: {j['total']}
range: {j['a']}–{j['b']}
sha256: {sha}
reader: codex gpt-6.1-sol
read_date: {D}
---
# {base} {j['a']}–{j['b']}쪽 — 판독 기록

| 쪽 | 내용 |
|---|---|
| p.{j['a']} | ... |
(범위의 모든 쪽마다 정확히 한 행. 빈 쪽이면 "빈 쪽".)

내용 칸에 쓸 것
- 인쇄된 쪽 번호(있으면), 절 번호·제목, 그 쪽이 설명하는 내용.
- ★수식은 요약하지 말고 이미지에 인쇄된 그대로 LaTeX로 옮기고(위·아래 첨자, 분자/분모, 부호, 상선) 인쇄된 식 번호를 붙인다. 원문이 틀려 보여도 고치지 않고, 빠진 연산자를 채우지 않는다. 기호 정의·단위도 적는다.
- 매개변수 이름·기본값·범위·권장값·단위와 적용 조건(어떤 옵션일 때)은 원문 그대로. 부정·조건·수량·의무·불확실성을 그대로 유지한다.
- 표는 핵심 행·값을 원문 그대로 옮기고, 그림·도표는 무엇을 보여 주는지(축, 비교 대상, 결론)를 적는다. 그림·표 번호와 캡션은 원문 그대로.
- 텍스트가 있는 쪽마다 그 쪽 본문 문장(6단어 이상)을 최소 1개 원문 그대로 백틱 안에 넣고 바로 뒤에 `(p.N)`을 붙인다. 이 인용은 추출 텍스트와 기계 대조된다. 머리말·바닥글은 인용하지 않는다.
- 용어: directional spreading = '방향 퍼짐', dispersion = '분산', variance = '분산(variance)'. 전문 용어는 처음 쓸 때 영어 원어를 괄호로.
- 이미지로도 판단할 수 없는 부분은 `[원문 인쇄 판독 불가]`.

끝에 `## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)` 절: 식 번호 누락·중복, 정의되지 않은 기호, 같은 문서 안의 모순, 판독이 어려웠던 부분을 쪽 번호와 함께. 없으면 "없음".

SCOPE
- 쓰기 허용: 위 출력 파일 하나. 다른 노트·기존 판독 기록(_staging/total-read, models/*/manual-notes 등)은 읽지 않는다. 다른 파일은 만들거나 고치지 않는다. git 명령을 쓰지 않는다.

STOP CONDITION
- 범위의 모든 쪽을 기록하면 끝낸다. 어떤 쪽 이미지를 열 수 없으면 그 쪽 행에 "이미지 열지 못함"이라 쓰고 보고한다.

DELIVERABLE (한국어, 한 문장에 한 사실)
- 출력 경로, 행 수(=쪽 수), 옮긴 수식 개수, 판독 불가 항목, 열지 못한 이미지.""")
