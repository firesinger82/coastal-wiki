# usage: python3 mkdocprompt_model.py MODEL BATCHFILE N   — doc reading prompt (rst/md/txt), figures opened as images
import json,sys,datetime,os
M,BF,N=sys.argv[1],sys.argv[2],int(sys.argv[3])
D=datetime.date.today().isoformat()
b=json.load(open(BF))[N-1]
out=lambda p:'_staging/recovery/read/'+M+'/'+p.split('/raw/')[1]+'.md'
files='\n'.join(f'- {p}' for p in b); outs='\n'.join(f'- {out(p)}' for p in b)
print(f"""OBJECTIVE
아래 {M} 문서 파일을 각각 1행부터 마지막 행까지 직접 읽고, 파일마다 판독 구간 기록 1개를 작성한다.

대상 파일 (저장소 루트 = /home/firesinger/coastal-wiki):
{files}

출력 파일 (이 경로에만 새로 쓴다):
{outs}

형식 견본 (먼저 읽고 같은 형식으로 쓴다. 다른 모델의 문서 기록이다. 형식만 따른다):
- _staging/recovery/read/XBeach/manuals/readthedocs/en/latest/_sources/numerical_implementation.rst.txt.md

읽는 방법 (필수)
- `nl -ba <파일> | sed -n 'A,Bp'` 로 한 번에 최대 200행씩 순서대로 읽는다. 1행부터 마지막 행까지 빠짐없이.
- 출력에 "tokens truncated" 또는 잘림 표시가 보이면 그 범위를 더 작게 나눠 다시 읽는다. 보지 못한 행을 기록에 넣지 않는다.
- `.. figure::`·`.. image::`가 가리키는 그림 파일(같은 docs 폴더 기준 상대 경로)은 이미지 보기 도구로 직접 열어 본다. 그림이 수식·도식·격자·흐름을 담고 있으면 그 내용을 기록에 적는다(축, 기호, 화살표 방향, 식). 열지 못하면 그렇다고 적는다.
- 다른 노트·기존 판독 기록(_staging/total-read, models/{M}/manual-notes, models/{M}/source-analysis 등)은 읽지 않는다. 원문만 보고 쓴다.

기록 형식
- frontmatter: file(저장소 상대경로), lines(`nl -ba <파일> | tail -1` 의 마지막 행 번호 — 마지막 줄에 개행이 없으면 wc -l 보다 1 크다), sha256(`sha256sum` 값), reader: codex gpt-6.1-sol, read_date: {D}
- 본문 표 `| 구간 | 내용 |`: 구간은 `A–B`(en dash). 첫 구간은 1에서 시작, 각 구간은 앞 구간 끝+1에서 시작, 마지막 구간은 lines에서 끝난다. 빈 줄·마크업·지시문도 구간에 포함한다. 절·소절 단위로 나누되 실질 내용이 대략 80행을 넘으면 더 나눈다.
- 내용 칸: 절 제목, 그 구간이 설명하는 내용을 행 번호와 함께 한국어로.
- ★수식(math 지시문, LaTeX), 매개변수 이름·기본값·범위·단위, 적용 조건(어떤 옵션일 때), 입력 파일 형식 예시 줄은 요약·의역하지 말고 백틱 안에 원문 그대로 행 번호와 함께 적는다(예: `tref = 20180101 000000` (42)). 긴 표는 행마다 이름·기본값·범위를 원문 그대로 옮긴다.
- 요약 문장이 옆의 원문 인용과 다른 뜻이 되지 않게 한다(합↔평균, 상한/하한↔조건 같은 의역 금지). 부정·조건·수량·의무·불확실성을 그대로 유지한다.
- 끝에 `## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)` 절: 문서 내부 모순, 정의 없는 기호, 깨진 참조·수식, 없는 그림 파일 등을 행 번호와 함께. 없으면 "없음".
- 빈 파일(0행)은 frontmatter와 "빈 파일" 한 줄만.

SCOPE
- 쓰기 허용: 위 출력 파일 경로만. 그 외 어떤 파일도 만들거나 수정·삭제하지 않는다. git 명령을 쓰지 않는다.

STOP CONDITION
- 위 파일을 모두 기록하면 끝낸다. 끝까지 읽지 못한 파일은 기록을 쓰지 말고 이유를 보고한다.

DELIVERABLE
- 파일별: 출력 경로, lines, 구간 수, 옮긴 수식·매개변수 수, 연 그림 수, 확인된 사실 개수.""")
