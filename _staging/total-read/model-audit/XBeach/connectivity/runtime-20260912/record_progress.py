"""Advance only this installed batch; preserve the frozen scope and old receipts."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
def dump(p, x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bind(p): return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}

validation = read(HERE/'validation.json')
assert validation['status']=='PASS' and validation['stage']=='installed' and validation['review_binding_checked']
manifest = read(HERE/'install-manifest.json')
for x in manifest['files']: assert sha(ROOT/x['target'])==x['after_sha256']
protection = read(HERE/'protection-before.json')
after = []
for x in protection:
    p=ROOT/x['path'];st=p.stat()
    actual={'mode':oct(st.st_mode&0o777),'uid':st.st_uid,'gid':st.st_gid}
    assert all(actual[k]==x[k] for k in actual), ('protection changed',p)
    after.append({'path':x['path'],'after_sha256':sha(p),**actual})
dump(HERE/'protection-after.json',after)

progress_path=HERE.parent/'remaining-20260912/progress.json'
progress=read(progress_path)
progress['status_by_id']['R1-runtime-20260912']={
    'status':'partial_source_contracts_and_candidate_index; R1_remains_open',
    'contracts':['R1-RT'+str(i).zfill(2) for i in range(1,10)],
    'evidence':bind(HERE/'evidence.json'),
    'remaining_gaps':bind(HERE/'remaining-gaps.json')}
progress['status_by_id']['R3-runtime-20260912']={
    'status':'installed_source_corrections_not_new_HG',
    'canonical':[{'path':x['target'],'sha256':x['after_sha256']} for x in manifest['files']],
    'correction_scope':'Ship/nonh pressure attribution, residual sign and active corrections, vegetation/rainfall timing, roughness linkage, output provider/writer guard'}
new=[bind(HERE/x) for x in ['evidence.json','install-manifest.json','review-response.json','validation.json','regeneration-check.json','protection-after.json']]
new_paths={x['path'] for x in new}
progress['evidence']=[x for x in progress['evidence'] if x['path'] not in new_paths]+new
progress['canonical_hash_semantics']='Each batch records installed-at-that-time bytes. Later reviewed batches may supersede shared paths such as README; older receipts are historical, not current-install validators.'
assert progress['overall']['R1']=='open' and progress['overall']['R2']=='open'
progress['next']='Continue fixed R1-G1/G2/G3 from runtime-20260912/remaining-gaps.json; then fixed R2 equation-position correspondence. Reuse completed C1-C4 and RT01-RT09, no scope expansion.'
dump(progress_path,progress)

heading='## 2026-09-12 R1 실행 연결 보강·7개 문서 정정 — 최신 재개 지점'
body='''
[실행 연결 보강](runtime-20260912/README.md)에서 선박 `ph`/nonh `pres·dp`, 운동량 잔차 부호·2차 보정 호출, 식생·강우·조도 갱신 시점, 출력 공급자/rank, 생성 로그·콜백을 소스에 결속했다. 기존 문서 7개를 [정확한 manifest](runtime-20260912/install-manifest.json)대로 반영했다. 독립 검토의 선박 소비 OR 조건 누락 P2를 수정하고 [후속 검토](runtime-20260912/codex-followup.txt)를 완료했다. 원문 48구간·생성 출력 27개·문서 링크·설치 바이트·기존 불변 기록 292개와 소유자/권한을 확인했다.

**R1 전체는 아직 미완이다.** 호출 후보 인덱스는 전체 의미 도달성 증명이 아니다. 다음 대조는 [R1-G1/G2/G3](runtime-20260912/remaining-gaps.json)의 generic/가시성/실행 조건, 미분류 정의, 동적 wrapper·생성 interface 연결이다. R2 수식별 대응 및 R3/R4 전체도 미완이며 입력 집합은 늘리지 않았다. [후속 상태](remaining-20260912/progress.json)가 현재 반영 상태다. 과거 C1~C4와 이번 정정을 다시 미완으로 세지 않는다.

Codex 하위 검토 프로세스의 읽기 전용 파일시스템 시작 실패와 승인 실행 경로는 [실행 메모](runtime-20260912/EXECUTION-NOTES.md)에 기록했다. 같은 유형을 기본 sandbox에서 반복 실패시키지 않는다. 전체 모델 완료·새 사람 승인·GOAL 도구 상태는 변경하지 않았다.

'''
for name in ['RESUME.md','GOAL-STATUS.md']:
    p=HERE.parent/name;s=p.read_text()
    if heading not in s:
        first,rest=s.split('\n',1)
        rest=rest.replace('초기 정정 R3-C1~C4 반영 — 최신 재개 지점','초기 정정 R3-C1~C4 반영 — 이전 재개 기록',1)
        p.write_text(first+'\n\n'+heading+'\n'+body+rest.lstrip('\n'))

print('Recorded installed seven-document batch; fixed R1/R2/R3/R4 remain open; owner/mode preserved')
