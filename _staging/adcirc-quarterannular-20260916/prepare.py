"""Prepare the two scoped documentation candidates; never edit canonical files."""
from pathlib import Path
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TARGETS = [
    'models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md',
    'models/ADCIRC/source-analysis/adcirc-topic-map.md',
]


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected one occurrence: {old[:100]}')
    return text.replace(old, new, 1)


def main():
    baseline = json.loads((HERE / 'preservation-before.json').read_text())
    (HERE / 'before').mkdir(exist_ok=True)
    (HERE / 'candidate').mkdir(exist_ok=True)
    model_receipt = HERE / 'claude-model-check.json'
    model = json.loads(model_receipt.read_text())['primary_model'] if model_receipt.exists() else 'pending'
    metadata = (
        'reference_contract_date: 2026-09-16\n'
        f'reference_contract_evidence_by: "Claude Opus ({model}) — 선정 원문·코드 사실 추출"\n'
        'reference_contract_by: "Codex — 근거 판정·회귀/해석해 구분·문서 보강"\n'
        'reference_contract_human_approval: not-issued\n'
        'reference_contract_scope: "quarter-annular 입력·출력 비교 계약과 해석해 적용 경계의 한정 대조. 실제 모델 실행·수치/물리 검증·기존 전체 노트 재검증 아님."\n'
    )
    manifest, patch = [], []
    for rel in TARGETS:
        target = ROOT / rel
        data = target.read_bytes()
        if hashlib.sha256(data).hexdigest() != baseline['targets'][rel]['sha256']:
            raise ValueError(f'Canonical target changed: {rel}')
        old = data.decode()
        (HERE / 'before' / target.name).write_bytes(data)
        new = once(old, 'canonical_source: self\n', 'canonical_source: self\n' + metadata)
        if rel.endswith('adcirc-tide-harmonic-prep.md'):
            marker = '<a id="external-data-conventions"></a>'
            section = (HERE / 'quarterannular-section.md').read_text().rstrip() + '\n\n'
            new = once(new, marker, section + marker)
            start = new.index('- **회귀 예제**:')
            end = new.index('\n- **수치 검증**:', start)
            new = new[:start] + '- **회귀 예제**: 공식 testsuite의 `adcirc_quarterannular-2d-netcdf`에 대해 [입력·control·자동 비교 계약](#quarterannular-reference-contract)을 한정 대조했다. 비선형 입력과 선형 해석해의 조건을 구분하며 실제 회귀 실행·해석해 검증은 미수행이다.' + new[end:]
        else:
            new = once(new,
                '| 수치 검증 | T의 회귀검사 위치와 [예제 색인](../manual-notes/07-examples-index.md) | **이번 미수행**. 회귀 일치와 별도로 해석해/기준해·보존량·격자/시간 민감도 근거 |',
                '| 수치 검증 | [quarter-annular 입력·control·출력 비교 계약](tide/adcirc-tide-harmonic-prep.md#quarterannular-reference-contract)과 [예제 색인](../manual-notes/07-examples-index.md) | **실제 검증 미수행**. 비선형 회귀 입력과 선형 해석해의 조건을 구분. 동일 조건의 기준해·보존량·격자/시간 민감도 근거 필요 |')
            start = new.index('2. **실행 확인 후보**:')
            end = new.index('\n', start)
            new = new[:start] + '2. **공개 회귀 예제**: [quarter-annular의 고정 입력과 출력 비교 계약](tide/adcirc-tide-harmonic-prep.md#quarterannular-reference-contract)을 확보했다. T의 자동 비교는 저장된 control에 대한 여섯 NetCDF 출력이며, 조화출력 `fort.51`–`fort.54`는 해당 YAML 목록 밖이다. 회귀 실행·해석해 대조·독립 관측검증은 미수행이다. testsuite tolerance를 해역의 물리 허용오차로 복사하지 않는다.' + new[end:]
        candidate = HERE / 'candidate' / target.name
        candidate.write_text(new)
        manifest.append({
            'target': rel, 'source': str(candidate.relative_to(ROOT)),
            'before_sha256': hashlib.sha256(data).hexdigest(),
            'after_sha256': hashlib.sha256(new.encode()).hexdigest(),
        })
        patch.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile='a/' + rel, tofile='b/' + rel))
    (HERE / 'install-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (HERE / 'changes.patch').write_text(''.join(patch))
    print('Prepared two candidates and review patch; canonical files unchanged')


if __name__ == '__main__':
    main()
