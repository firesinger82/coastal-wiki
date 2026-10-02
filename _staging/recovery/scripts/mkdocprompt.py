import json,sys
R='models/XBeach/raw/manuals/readthedocs/en/latest/_sources/'
O='_staging/recovery/extract/XBeach/office/'
B=[[R+'xbeach_manual.rst.txt'],[R+'matlab_toolbox.rst.txt'],
   [R+f for f in ['numerical_implementation.rst.txt','matlab_tutorials.rst.txt','cheatsheet.rst.txt','examples.rst.txt','index.rst.txt','compile.rst.txt','advanced_techniques.rst.txt','gallery.rst.txt','python_tools.rst.txt','input_parameters.rst.txt','output_variables.rst.txt']],
   ['models/XBeach/raw/manuals/readthedocs_markdown/en/latest/input_parameters.md','models/XBeach/raw/manuals/readthedocs_markdown/en/latest/output_variables.md',O+'DecisionTreeXBeach.txt',O+'members.txt',O+'namespaces.tsv','models/XBeach/raw/source_code/trunk/doc/reports/libxbeach.tex']]
json.dump(B,open('_staging/recovery/scripts/docbatches.json','w'))
def out(p):
    if '/raw/' in p: return '_staging/recovery/read/XBeach/'+p.split('/raw/')[1]+'.md'
    return '_staging/recovery/read/XBeach/office-converted/'+p.split('/')[-1]+'.md'
orig={'DecisionTreeXBeach.txt':'source_code/trunk/doc/misc/DecisionTreeXBeach.docx','members.txt':'source_code/trunk/doc/misc/members.doc','namespaces.tsv':'source_code/trunk/doc/misc/namespaces.xls'}
i=int(sys.argv[1]); b=B[i-1]
files='\n'.join(f'- {p}' for p in b); outs='\n'.join(f'- {out(p)}' for p in b)
conv=[p for p in b if '/office/' in p]
convnote=('\n변환본 주의: '+', '.join(f"{p.split('/')[-1]}은 models/XBeach/raw/{orig[p.split('/')[-1]]}을 LibreOffice/xlrd로 변환한 텍스트다. frontmatter에 `original: models/XBeach/raw/{orig[p.split('/')[-1]]}` 줄을 추가한다." for p in conv)) if conv else ''
print(f"""OBJECTIVE
아래 XBeach 문서 파일을 각각 1행부터 마지막 행까지 직접 읽고, 파일마다 판독 구간 기록 1개를 작성한다.

대상 파일 (저장소 루트 = /home/firesinger/coastal-wiki):
{files}

출력 파일 (이 경로에만 새로 쓴다):
{outs}
{convnote}

형식 견본 (반드시 먼저 읽고 같은 형식으로 쓴다. 견본은 소스코드용이니 '코드' 대신 문서 내용을 적는다):
- _staging/recovery/read/XBeach/trunk/src/xbeachlibrary/groundwater.F90.md

읽는 방법 (필수)
- `nl -ba <파일> | sed -n 'A,Bp'` 로 한 번에 최대 200행씩 순서대로 읽는다. 1행부터 마지막 행까지 빠짐없이.
- 출력에 "tokens truncated" 또는 잘림 표시가 보이면 그 범위를 더 작게 나눠 다시 읽는다. 보지 못한 행을 기록에 넣지 않는다.
- 다른 노트·기존 판독 기록(_staging/total-read, models/XBeach/manual-notes 등)은 읽지 않는다. 원문만 보고 쓴다.

기록 형식
- frontmatter: file(저장소 상대경로), lines(`nl -ba <파일> | tail -1` 의 마지막 행 번호), sha256(`sha256sum` 값), reader: codex gpt-6.1-sol, read_date: 2026-10-02
- 본문 표 `| 구간 | 내용 |`: 구간은 `A–B`(en dash). 첫 구간은 1에서 시작, 각 구간은 앞 구간 끝+1에서 시작, 마지막 구간은 lines에서 끝난다. 빈 줄·마크업·지시문도 구간에 포함한다. 절·소절 단위로 나누되 실질 내용이 대략 80행을 넘으면 더 나눈다.
- 내용 칸: 절 제목, 그 구간이 설명하는 내용을 행 번호와 함께 한국어로.
- ★수식(math 지시문, LaTeX), 매개변수 이름·기본값·범위·단위, 적용 조건(어떤 옵션일 때)은 요약·의역하지 말고 백틱 안에 원문 그대로 행 번호와 함께 적는다(예: `:math:\\`H_{{rms}} = \\sqrt{{8E/\\rho g}}\\`` (120)). 긴 표는 행마다 이름·기본값·범위를 원문 그대로 옮긴다.
- 요약 문장이 옆의 원문 인용과 다른 뜻이 되지 않게 한다(합↔평균, 상한/하한↔조건 같은 의역 금지).
- 끝에 `## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)` 절: 문서 내부 모순, 정의 없는 기호, 깨진 참조·수식, 다른 판(kingsday/master) 언급 등을 행 번호와 함께. 없으면 "없음".
- 빈 파일(0행)은 frontmatter와 "빈 파일" 한 줄만.

SCOPE
- 쓰기 허용: 위 출력 파일 경로만. 그 외 어떤 파일도 만들거나 수정·삭제하지 않는다. git 명령을 쓰지 않는다.

STOP CONDITION
- 위 파일을 모두 기록하면 끝낸다. 끝까지 읽지 못한 파일은 기록을 쓰지 말고 이유를 보고한다.

DELIVERABLE
- 파일별: 출력 경로, lines, 구간 수, 옮긴 수식·매개변수 수, 확인된 사실 개수.""")
