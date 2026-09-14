"""Build three review candidates; never write canonical targets."""
from pathlib import Path
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CANDIDATE = HERE / 'candidate'
CANDIDATE.mkdir(exist_ok=True)
BASE = 'models/ADCIRC/source-analysis/'
FILES = [BASE + 'tide/adcirc-tide-harmonic-prep.md',
         BASE + 'tide/adcirc-tide-forcing-implementation.md',
         BASE + 'adcirc-topic-map.md']

def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('replacement mismatch: ' + old[:100])
    return text.replace(old, new, 1)

def paragraph(text, start, new):
    begin = text.index(start)
    end = text.index('\n\n', begin)
    return text[:begin] + new + text[end:]

manifest, patches = [], []
for rel in FILES:
    old = (ROOT / rel).read_text()
    new = old
    extra = 'external_evidence_date: 2026-09-14\nexternal_evidence_review: "Claude Fable 5.1 — 외부 제품·변환 확인 방법·독립 관측/지표 원문 대조; 과학적 사람 승인 아님"\nexternal_evidence_human_approval: not-issued\nexternal_evidence_scope: "외부 조석 제품 정의·변환 확인 방법·관측 독립성·지표 근거와 관련 무근거 권고 정정. 실제 자료/실행/수치/물리 검증 아님."\n'
    new = once(new, 'canonical_source: self\n', 'canonical_source: self\n' + extra)
    if '/tide/' in rel:
        new = once(new, '다른 절과 외부 DB 규약은 이번 검증 범위에 포함하지 않는다.', '이 코드 대조는 다른 절과 외부 DB 규약을 포함하지 않는다. 외부 자료에 대한 별도 보강 범위는 harmonic-prep의 「외부 조석 자료」 절을 따른다.')
    if rel.endswith('adcirc-tide-harmonic-prep.md'):
        new = paragraph(new, '이 절은 **확인할 증거와 수행 순서**', '이 절은 **확인할 증거와 수행 순서**를 정한다. 실제 사용할 조석 DB·지형·관측자료와 허용오차는 아직 선정하지 않았으므로 **입력 품질·실행 확인·수치 검증·물리 검증은 미완**이다. 외부 DB 정의와 관측·오차 지표의 원문 대조는 아래 별도 절에 정리했다. 확인되지 않은 변환 세부·정량 권고는 `source-needed`로 남긴다.')
        new = once(new, 'ADCIRC 소비 형식만 확인. FES/NAO/TPXO의 판본별 정의는 `source-needed`', '[제품별 정의](#external-data-conventions)에 확인 범위 명시. TPXO 개별 파일 형식과 실제 자료는 미확인')
        new = once(new, '형식이 유효해도 품질 통과로 취급하지 않음; 제품별 원문 `source-needed`', 'FES mask/결측 정의와 NAO scale/결측 처리, UHSLC QC 원문 확보. 실제 사용할 자료의 품질 판정은 미수행')
        new = once(new, 'ADCIRC 시간/부호는 §D/F에서 한정 대조. 외부 규약은 `source-needed`', 'ADCIRC §D/F, FES/NAO 부호·예측 정의는 [외부 자료 절](#external-data-conventions). TPXO 규약과 실제 FF/FACE 변환은 미확인')
        new = once(new, '**관측자료·분석 세부 절차·목적별 허용오차는 `source-needed`**이며 관측 대조를 수행했다고 쓰지 않는다.', '[독립 관측·오차 지표](#independent-observation-and-errors)의 원문·정의는 확보했다. **선정 정점/기간·실제 분석·목적별 허용오차는 미확정**이며 관측 대조를 수행했다고 쓰지 않는다.')
        new = paragraph(new, '이 묶음의 다음 완료 조건은', '외부 자료의 일반 규약과 관측·지표 근거는 아래에 정리했다. 다음 실제 입력 단계에는 atlas 판본·경계 노드·시각과 관측 정점/기간을 지정하고 변환 결과를 대조해야 한다. 기준해·보존/민감도와 목적별 허용치도 별도로 필요하다. 개인 실행 결과는 [coastal-runs 채널](../../../../RUNS-CHANNEL.md)에 둔다.')
        new = once(new, '\n## Scope\n', '\n' + (HERE / 'external-section.md').read_text().rstrip() + '\n\n\n## Scope\n')
        new = paragraph(new, 'ADCIRC uses **lag-subtracted**', 'ADCIRC uses **lag-subtracted** phase (`cos(arg − phase)`; `src/gwce.F:1642–1649`). FES/PyFES와 이번 NAO 패키지에서 확인한 lag 합성은 [제품별 근거](#external-data-conventions)에 정리했다. 부호가 같아도 epoch·단위·천문식·노달보정까지 같다는 뜻은 아니다. TPXO의 특정 배포 형식은 아직 대조하지 않았다.')
        new = once(new, 'These come from astronomical theory; standard tools (T_TIDE, UTIDE, pyTMD) compute them per epoch.', 'FES의 천문 인수·노달보정 의미는 [PyFES nodal 식][pyfes-nodal]을 참조한다. 실제 FF/FACE 생성에서는 제품과 예측기의 판본·분조·epoch·보정 포함 여부를 맞춘다. T_TIDE/UTIDE/pyTMD의 출력을 동일한 ADCIRC 입력으로 사용할 수 있다는 일괄 호환 주장은 여기서 확정하지 않는다.')
        new = paragraph(new, '**This is the most common source of phase errors**', '`STATIM/REFTIM`은 이 코드에서 수치적인 일(day) 값이다. 시각대/달력 epoch를 자동으로 부여한다고 가정하지 않는다. 외부에서 구한 FACE/FACET의 기준시각과 같은 실제 시각을 나타내도록 연결한다(`src/timestep.F:257–258`; `src/gwce.F:1642–1649`).')
        start, end = new.index('## G. NAO99jb / FES2022b workflow'), new.index('## Working Rules')
        replacement = '''## G. 외부 atlas에서 fort.15로

1. [제품별 정의와 변환 대조](#external-data-conventions)를 따라 ocean/geocentric/radial 성분, 판본, 분조, 단위, 유효 영역을 고정한다.
2. 실제 시작시각과 STATIM/REFTIM을 대응시키고 분조별 AMIG(rad/s), FF, FACE(deg)의 epoch·천문/노달보정을 기록한다. 전체 공급기관 예측과 NBFR 일부 분조의 비교는 성분부터 맞춘다.
3. 경계 노드마다 동일 자료에서 추출한 진폭·lag를 EMO(m), EFA(deg)로 변환한다. 결측/외삽·보간 처리와 원자료 대응을 보존한다.
4. §A의 NBFR 레코드와 분조/노드 순서대로 작성하고 fort.16 echo 및 같은 성분의 재합성에 대조한다(`src/read_input.F:3431–3456,3485–3497`; `src/gwce.F:1638–1649`).

이 절차의 실제 변환 실행은 미수행이다. SAL은 위 [loading tide 구분](#external-data-conventions)의 별도 물리량 정의를 확보한 뒤 준비한다.

## H. Validation pitfalls

- **Epoch·시각대**: FACE/FACET의 기준과 TimeH의 기준을 대조한다. 오차를 임의의 90°/180° 증상으로 단정하지 않는다(§D/F 합성식).
- **Lead/lag**: 부호를 뒤집은 오차는 원래 위상에 의존한다. 순환 위상 차이와 복소 오차를 함께 본다([지표 정의](#independent-observation-and-errors)).
- **단위·결측**: cm 값을 m로 쓰면 진폭이 100배가 된다. 결측 sentinel에 단위 변환/보간을 적용하기 전에 제외한다([제품별 정의](#external-data-conventions)).
- **분조/노드 순서**: NBFR의 ELEVALPHA는 echo되지만 BOUNTAG와 대조되지 않는다. SAL의 TIPOTAG 매칭과 혼동하지 않는다(§A/C; `src/read_input.F:3485–3497`).
- **노달보정**: 이 NBFR 경로는 입력 FF/FACE를 합성에 사용한다. 시간에 따라 변하는 공급기관 예측과의 차이를 대상 기간에서 평가한다. 고정 1개월/분기별 갱신을 공통 정확도 기준으로 사용하지 않는다(`src/gwce.F:1642–1649`; [PyFES nodal 정의][pyfes-nodal]).
- **관측/atlas 혼동**: 원 DB와의 재합성 일치, 동화/보정에 사용한 관측 일치, 독립 관측 검증을 구분한다([독립성 기준](#independent-observation-and-errors)).

## Decision Guide

| Need | Setup |
|---|---|
| 주기 수위 경계 | NBFR와 EMO/EFA를 준비한다. NTIP/NTIF 퍼텐셜 선택은 별도다. 위 회귀 예제는 NTIP=0, NTIF=0, NBFR=1이다. |
| 퍼텐셜/SAL도 포함 | NTIP의 0/1/2 정의와 §A/F·forcing 노트를 대조한다. SAL 사용에는 성분·물리량·분조·파일의 추가 근거가 필요하며, 모든 해역에 일괄 권고하지 않는다. |
| FES2022b / NAO99Jb / TPXO | [제품별 정의](#external-data-conventions)에 따라 변환한다. 제품명·격자 간격·포함 분조 수만으로 특정 해역의 정확도 순위를 정하지 않는다. |
| 관측과 비교 | [독립성·분석창·지표](#independent-observation-and-errors)를 고정한다. 해역·목적별 허용치는 미선정이다. |
| 긴 실행 기간 | 고정 FF/FACE 합성과 선택한 공급기관 예측의 기간 내 차이를 확인한다. 보정 변경/재시작 방법과 허용오차는 별도 검증 대상이다. |
| Disable tidal potential and periodic elevation forcing | `NTIP=0`; keep the required `NBFR=0` line. Any non-periodic elevation boundary data are a separate input (`src/read_input.F:1705–1731,3410–3444`; [official NBFR definition](https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html)). |

'''
        new = new[:start] + replacement + new[end:]
        new = paragraph(new, '- For Korean coast, NAO99jb', '- 지역별 DB 선택은 해당 정점/기간의 독립 관측 대조로 판단한다. NAO99Jb도 N2/K2/P1을 포함하므로 이 분조들의 존재만으로 FES의 추가 정확도를 주장하지 않는다([NAO README §2][nao-readme]).\n- 기존 SAL의 일괄 5–10% 진폭 감소 권고는 `source-needed`다. 해당 조건·정량 근거를 확인하기 전 특정 과대예측의 원인 판정에 사용하지 않는다.')
        new = new.replace('- T_TIDE / pyTMD recipe for FF/FACE generation.', '- 판본·천문/노달보정이 명시된 FF/FACE 생성 및 공급기관 예측과의 대조.')
        new = new.replace('- SAL preparation from FES2022b loading-tide grids.', '- SAL 입력과 외부 제품의 물리량/퍼텐셜 정의 연결. FES radial loading의 직접 이전은 미입증.')
        new = once(new, '- FES2022b: Lyard et al. 2024.', '- FES2022b: [CNES dataset DOI](https://doi.org/10.24400/527896/A01-2024.004), [handbook Issue 2.0][fes-hdbk]. 이 handbook p. 1의 FES2022 논문은 in preparation으로 기재돼 있어, 기존의 불명확한 “Lyard et al. 2024” 출판 인용을 대체한다.\n- 외부 자료·검증 지표 출처는 해당 절의 제품 문서, NAO 입력/합성 코드, UHSLC와 Wang et al. (2022)에 명시했다.')
    elif rel.endswith('adcirc-tide-forcing-implementation.md'):
        new = once(new, '- **Using NAO99jb amplitudes with FES2022b phases** — common cross-mix mistake; phases are referenced to different conventions.', '- **서로 다른 DB의 진폭·위상 혼합** — 동일 제품·판본·공간 추출의 한 쌍을 사용한다. FES와 NAO의 위상 규약이 서로 다르다고 단정한 기존 문장은 철회한다. 확인한 부호·단위와 아직 미확인인 변환 조건은 [제품별 정의](adcirc-tide-harmonic-prep.md#external-data-conventions)에 있다. FES radial loading을 fort.24로 직접 이전할 근거도 이와 별도로 필요하다.')
    else:
        new = once(new, '외부 DB 규약과 실제 경계 자료의 품질·변환 확인; 아래 조석 진입점', 'FES/NAO 정의·변환 확인 방법 및 TPXO 확인 한계는 [제품별 근거](tide/adcirc-tide-harmonic-prep.md#external-data-conventions). 실제 경계 파일 품질·변환/합성 결과는 미확인')
        new = once(new, 'full-formula/SAL 전체 조건·파일·분조 정합, 정량 효과와 외부 SAL 제품 정의', 'full-formula/SAL 전체 조건·파일·분조 정합과 정량 효과. FES radial 변위를 fort.24로 직접 옮길 물리량 대응은 미입증([구분](tide/adcirc-tide-harmonic-prep.md#external-data-conventions))')
        new = once(new, '| 입력 품질·불확실성 | [조석 확인 방법](tide/adcirc-tide-harmonic-prep.md#input-quality-and-validation) |', '| 입력 품질·불확실성 | [조석 확인 방법](tide/adcirc-tide-harmonic-prep.md#input-quality-and-validation)과 [외부 제품 원문·관측/지표 정의](tide/adcirc-tide-harmonic-prep.md#external-data-conventions) |')
        new = paragraph(new, '4. **다음 근거 확보**', '4. **외부 자료·관측/오차 근거**: [제품별 정의·변환 대조](tide/adcirc-tide-harmonic-prep.md#external-data-conventions)와 [독립 관측·지표](tide/adcirc-tide-harmonic-prep.md#independent-observation-and-errors)를 확보했다. 다음은 사용할 DB 파일·경계·시각과 관측 정점/기간을 지정한 실제 품질·변환 확인 및 목적별 허용치다. TPXO 개별 배포 형식, SAL 물리량 대응, 기준해·보존/민감도도 미확인이다. 입력/물리 검증 준비 완료로 표시하지 않는다.')
    path = CANDIDATE / Path(rel).name
    path.write_text(new)
    manifest.append({'target': rel, 'source': str(path.relative_to(ROOT)),
                     'before_sha256': hashlib.sha256(old.encode()).hexdigest(),
                     'after_sha256': hashlib.sha256(new.encode()).hexdigest()})
    patches.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile='a/'+rel, tofile='b/'+rel))
(HERE / 'install-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(HERE / 'changes.patch').write_text(''.join(patches))
print('Prepared three candidates and review patch')
