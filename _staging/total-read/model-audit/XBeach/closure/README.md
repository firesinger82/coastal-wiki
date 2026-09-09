# XBeach 이월 및 canonical 반영 원장

2026-09-09 사용자 요청에 따른 후속 정리다. 승인된 감사 기록의 의미를 바꾸지 않고 후속 판정·문서 인용·canonical 대응을 추가했다. 이 원장은 사용자를 대신한 새 승인 영수증이 아니다.

## 범위와 원장

| 대상 | 정확한 분모 | 결과와 증거 |
|---|---:|---|
| P0 v3 파일 | 456 | 281 독립 2회 판독·22 문서/도해 단독·153 바이너리 메타데이터. [기존 HG 승인](../HG-APPROVAL-20260909.json) |
| 승인 소스 보충 | 103 | [기존60 대응](source-canonical/mapping-ledger.json) + [신규43 대응](build-canonical-mapping.json), 각 canonical 앵커로 연결 |
| 이월 충돌 | 3 | seed 타입·0 초기화/flux·README 문맥을 원문으로 재판정. [고난도5](hard-resolutions/hard-resolutions.json) 중 첫3 |
| 반증 인용 미검증 | 10 | [로컬8](local-refutations/resolution-ledger.json) + [MPICH2 최종 식별·판정](local-refutations/mpich-identity/identity-ledger.json). 초기 hard04는 DLL 오인으로 교정했으며 최종 override가 우선한다. 경고 유지/기각의 범위를 명시 |
| 문서 정량·조건·모순 후보 | 207 | [동결 입력](document-inventory/exact-207.jsonl), [전량 판정](document-inventory/all-207-disposition.jsonl), [207 canonical 앵커](document-inventory/document-canonical-mapping.json), [문서 출처·판본](document-inventory/source-map.json). 같은 문서의 두 표현을 독립 출처로 세지 않음 |
| 구성요소 귀속 | 456파일 / 1,472처분 | [귀속 원장](attribution.json): 파일 origin·component·role과 authored/generated/binary를 분리. project-integration은 저작권 귀속이나 솔버 결함 판정이 아님 |
| 기존 감사 증거 | 292파일 | [불변 기준](immutable-baseline.json)의 SHA-256 보존 |

[13건 최종 canonical 대응](deferred-canonical-mapping.json)은 동결 입력의 정확한 ID를 사용한다. 소스 판정 완료는 경고나 소스 결함을 수정했다는 뜻이 아니다. README·INDEX·AUDIT-LEDGER는 구 코어118 감사와 이번456 전량 조사 분모를 구별한다.

## 문서 판정 원칙

2015 Kingsday·2015 master·2010 비정수압 초안은 세 개의 별도 판본이다. PDF와 DOC/DOCX는 표현물로만 대응한다. 문서 자체가 충돌하면 양쪽 문장을 해당 판본에 귀속시키고 단일 권장값을 만들지 않는다. 변환 손상은 수치의 근거로 채택하지 않는다. 미완 초안이 설명하지 않은 내용은 문서의 범위 한계로 명시한다. 현재 소스에 대한 판단은 [8개 코드 대조](manual-code-adjudications.json)에 원문·파일 해시와 함께 분리했다.

PDF 물리페이지와 문서 인쇄페이지를 구별한다. DOC→PDF token alignment는 검색 위치 힌트이며 자동으로 동일 문장/같은 사실의 증명이 되지 않는다. 전량 변환물은 재생성 가능한 로컬 중간물로 git에서 제외하고, 짧은 인용·해시·위치·명령으로 출처를 추적한다.

## 검토와 재현

- [계획 검토와 반영](PLAN-REVIEW.md): exact13/exact207·불변 증거·배포 절차 고정.
- [Claude 적대적 검토 1](reviews/claude-round1.md): hard5·build43·귀속 분류. 원문과 바이너리 식별, fallback 귀속을 구별하도록 보강.
- 후속 검토 결과와 조치, 최종 무결성 검사 결과는 이 디렉토리의 `reviews/`, `validation-results.json`에서 확인한다.
- `validate_closure.py`: 동결 ID 집합·원문 해시·LF 인용·canonical 대응 검사. `--installed`는 설치 해시까지 검사.
- `install_canonical.py --check`: 검토본과 대상의 전후 SHA, 불변292 검사. `--apply`: exact manifest 대상만 원자적으로 교체, 실패 시 복원. raw와 기존 게이트를 수정하거나 models 전체 잠금을 해제하지 않는다.

역사적 V 실행 보고의 571건과 crosswalk에 실제 첨부된 적대판정 579건은 다른 집계다. 현재 첨부값은 STANDS308·NARROWED183·REFUTED78·REFUTED_UNVERIFIED10으로 579이며, 전체1,472처분 또는 고유결함 수와 같지 않다. 과거 보고를 소급해서 고치지 않고 [현재 집계](attribution.json)의 분모를 명시한다.
