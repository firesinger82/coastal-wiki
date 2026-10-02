import json,sys
b=json.load(open('xb-batches.json'))[int(sys.argv[1])-1]
files='\n'.join(f'- models/XBeach/raw/source_code/{p}  ({n}행)' for n,p in b)
outs='\n'.join(f'- _staging/recovery/read/XBeach/{p}.md' for n,p in b)
print(f"""OBJECTIVE
아래 XBeach 소스 파일을 각각 1행부터 마지막 행까지 직접 읽고, 파일마다 판독 구간 기록 1개를 작성한다.

대상 파일 (저장소 루트 = /home/firesinger/coastal-wiki):
{files}

출력 파일 (이 경로에만 새로 쓴다):
{outs}

형식 견본 (반드시 먼저 읽고 똑같은 형식으로 쓴다):
- _staging/recovery/read/XBeach/trunk/src/xbeachlibrary/vegetation.F90.md

읽는 방법 (필수)
- `nl -ba <파일> | sed -n 'A,Bp'` 로 한 번에 최대 200행씩 순서대로 읽는다. 1행부터 마지막 행까지 빠짐없이.
- 출력에 "tokens truncated" 또는 잘림 표시가 보이면 그 범위를 더 작게 나눠 다시 읽는다. 보지 못한 행을 기록에 넣지 않는다.
- 다른 노트·기존 판독 기록(_staging/total-read, models/XBeach/source-analysis 등)은 읽지 않는다. 원문만 보고 쓴다.

기록 형식
- frontmatter: file(저장소 상대경로), lines(`nl -ba <파일> | tail -1` 의 마지막 행 번호 — 마지막 줄에 개행이 없으면 wc -l 보다 1 크다), sha256(`sha256sum` 값), reader: codex gpt-6.1-sol, read_date: 2026-10-02
- 본문 표 `| 구간 | 내용 |`: 구간은 `A–B`(en dash) 형식. 첫 구간은 1에서 시작, 각 구간은 앞 구간 끝+1에서 시작, 마지막 구간은 lines에서 끝난다. 빈 줄·주석·선언도 구간에 포함한다.
- 내용 칸: 그 구간이 하는 일, 식(코드 그대로 또는 수식), 기본값·범위, 조건 분기, 호출하는 루틴을 원문 행 번호와 함께 한국어로 쓴다. 의미 있는 단위(루틴·블록)로 나누되 한 구간이 너무 길면(대략 80행 이상의 실질 코드) 더 나눈다.
- 끝에 `## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)` 절: 불일치·미사용 변수·초기화 누락 의심·하드코딩 등 눈에 띈 것을 행 번호와 함께. 없으면 "없음". "결함이다"라고 판정하지 않는다.
- 빈 파일(0행)은 frontmatter와 "빈 파일" 한 줄만 쓴다.

SCOPE
- 쓰기 허용: 위 출력 파일 경로만. 그 외 어떤 파일도 만들거나 수정·삭제하지 않는다(소스, models/, 다른 _staging 파일, git 포함). git 명령으로 커밋하지 않는다.

STOP CONDITION
- 위 파일을 모두 기록하면 끝낸다. 어떤 파일을 끝까지 읽지 못했으면 그 파일 기록을 쓰지 말고 이유를 보고한다. 범위 밖 판단이 필요하면 멈추고 보고한다.

DELIVERABLE
- 파일별: 출력 경로, lines, 구간 수, 판독 중 확인된 코드 사실 개수. 끝까지 못 읽은 파일이 있으면 명시.
""")
