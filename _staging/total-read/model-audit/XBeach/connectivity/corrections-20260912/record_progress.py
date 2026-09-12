"""Advance only the four installed correction IDs; retain frozen residual scope."""
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]

def binding(p):
    return {'path':str(p.relative_to(ROOT)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

def main():
    validation=json.loads((HERE/'validation.json').read_text())
    assert validation['stage']=='installed' and validation['status']=='PASS'
    assert validation['review_binding_checked'] is True
    manifest=json.loads((HERE/'install-manifest.json').read_text())
    for f in manifest['files']:
        assert binding(ROOT/f['target'])['sha256']==f['after_sha256'], f['target']
    corrections={
        'R3-C1':['source-analysis/xbeach_wave_boundary_generation.md','source-analysis/wave/xbeach_wave_boundary.md'],
        'R3-C2':['source-analysis/xbeach_wave_action_balance.md','source-analysis/xbeach_wave_stationary.md'],
        'R3-C3':['source-analysis/xbeach_intrawave_sediment_transport.md','source-analysis/xbeach_morphology.md'],
        'R3-C4':['manual-notes/xbeach-manual-equation-code-contracts.md','README.md'],
    }
    progress={'schema':'xbeach-fixed-remaining-progress/v1','date':'2026-09-12',
              'frozen_scope':binding(HERE.parent/'remaining-20260912/remaining.json'),
              'frozen_input_snapshots':'Preserved at their original hashes, not current-install validators',
              'status_by_id':{i:{'status':'installed_source_correction_not_new_HG',
                                  'canonical':[binding(ROOT/'models/XBeach'/p) for p in targets]}
                              for i,targets in corrections.items()},
              'evidence':[binding(HERE/x) for x in ['evidence.json','probe-results.json','review-response.json','install-manifest.json','validation.json']],
              'overall':{'R1':'open','R2':'open','R3':'open_pending_R1_R2_final_reconciliation','R4':'open_after_prerequisites'},
              'whole_model_complete':False,'human_approval_issued':False,
              'goal_control':'unchanged; last observed paused',
              'next':'R1 remaining routine/guard/state-consumer gaps using existing evidence; R2 equation-position disposition reuse. Do not repeat completed C1..C4 or enlarge scope.'}
    (HERE.parent/'remaining-20260912/progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')
    update='''## 2026-09-12 초기 정정 R3-C1~C4 반영 — 최신 재개 지점

[정정 네 건](corrections-20260912/README.md)을 기존 위키 문서 8개에 반영했다. `intrasedtr`의 명시 입력과 12개 입력→실제 공식 분기를 구분했고, 활성 파랑 경계·stationary 루틴의 귀속과 위상 처리를 고쳤으며, 기존 침투식 비교를 매뉴얼 노트에 넣었다. [후속 상태](remaining-20260912/progress.json)가 아래 동결 목록의 초기 네 정정 상태보다 우선한다. 과거 입력·검증 snapshot은 원래 해시를 보존한다.

다음은 고정 R1의 기존 루틴·호출 조건·핵심 상태 소비 근거에서 미연결 부분을 대조하고, R2의 기존 수식 판정과 위치를 결속하는 일이다. 처리한 네 정정을 다시 미완으로 세지 않는다. R3 전체는 R1/R2의 최종 결과에 의존하므로 아직 종결하지 않았다. 전체 모델 완료·새 사람 승인·GOAL 도구 상태는 변경하지 않았다.

'''
    for name in ['RESUME.md','GOAL-STATUS.md']:
        p=HERE.parent/name
        text=p.read_text()
        if update.splitlines()[0] not in text:
            first,rest=text.split('\n',1)
            p.write_text(first+'\n\n'+update+rest.lstrip('\n'))
    print('Recorded C1..C4 installed; R1..R4 and GOAL overall states unchanged')

if __name__=='__main__':
    main()
