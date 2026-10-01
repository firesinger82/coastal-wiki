# XBeach R2 수식 위치별 근거 결속 결과 (2026-10-01)

계획 [PLAN.md](PLAN.md) v2. 범위: 동결 캡션 위치 443곳(Kingsday 174 · Master 179 · 비정수압 보고서 90). 최종 처분표 `R2-final.jsonl`([압축](R2-final.jsonl.gz), sha256 `f14f32e1021c071fac97662a1cb0185a8ad8d07e6afba8f847e3c55ebd065505`). 결정적 검사 `check_r2.py` 오류 0.

## 1. 공정과 모델

| 단계 | 대상 | 모델 | 결과 |
|---|---|---|---|
| 계획 적대 검토 | PLAN v1 | gpt-6-astra | blocker 2·major 6 → v2 |
| 근거 꾸러미 | 443 | gpt-6.1-sol 구현·Claude 검증 | 440 unique·3 none, 재실행 바이트 동일 |
| 파일럿 판정·검증 | 30 | gpt-6.1-sol / gpt-6-astra | 21 유지·9 NARROWED → 규칙 보강 |
| 본 판정 | 413 (12배치) | gpt-6.1-sol | check 오류 0. 이미지 실제 열람(롤아웃 대조) |
| 정리 | 99 | gpt-6.1-sol | 종결 규칙 재분류(표준 기호 정의 부재 ≠ 미해결) |
| 적대 검증 1 | 405 (전건 391 + 층별 20% 14, seed 20261001) | **gpt-6-astra** | 유지 174·NARROWED 201·**REFUTED 30** |
| 정정 2 | 431 (verdict 231 + 스윕 S1 기호·S2 충실 전사·S3 지하수 K·S4 바닥경사 부호) | gpt-6.1-sol | 판정 이견 0 |
| 적대 검증 2 | 431 | gpt-6-astra | 유지 373·NARROWED 51·REFUTED 7 |
| 정정 3·확인 | 7 (전사) | gpt-6.1-sol / gpt-6-astra | 7/7 유지 → 확정 (멈춤 규칙) |

판정(gpt-6.1-sol)과 검증(gpt-6-astra)은 다른 계열이다. 1차 검증에서 REFUTED 가 R1(같은 모델 검증) 보다 훨씬 많이 나왔다 — 대부분 이산화 식의 첨자·시간 수준·막대를 인쇄와 다르게 "정돈"한 전사였다. 시각 판독은 AI 판독이며 수학적 검증이 아니다.

검증 운영 기록: V-10 판정어 오타 1건(`NARED`→`NARROWED`, 원본 `verify/V-10.verify.orig.txt` 보존).

## 2. 최종 분포

| 축 | 분포 |
|---|---|
| body_status | readable 437 · absent_at_caption 3 · present_unreadable 3 |
| document_role | model_relation 328 · derivation_or_validation 64 · definition_or_assumption 48 · unknown 3 |
| implementation_relation | mapped_with_differences 271 · not_applicable 70 · unresolved 77 · mapped 21 · document_only 4 |
| closure_status | documented_limit 206 · resolved 96 · **unresolved 141** |

(인벤토리이며 결함 수·진행률이 아니다.) 남은 NARROWED 51건(적대 검증 2)은 [verify2/all-verdicts.json](verify2/all-verdicts.json) 에 기록 — 멈춤 규칙에 따라 정정하지 않고 확정.

## 3. 미해결 141 ([unresolved-classified.json](unresolved-classified.json))

| 영역 \ 원인 | 문서 오기 후보 | 문서–구현 충돌 | 의미 불명(문서) | 구현 경로 미확정 | 본체 없음 | 계 |
|---|---:|---:|---:|---:|---:|---:|
| 비정수압 압력·해법 | 22 | 12 | 13 | 3 | 0 | 50 |
| 지하수 | 11 | 9 | 3 | 2 | 0 | 25 |
| 흐름·이산화 | 8 | 5 | 6 | 5 | 1 | 25 |
| 표사·지형 | 3 | 1 | 18 | 1 | 0 | 23 |
| 파랑·롤러·쇄파 | 2 | 0 | 8 | 4 | 4 | 18 |
| **계** | **46** | **27** | **48** | **15** | **5** | **141** |

분류는 레코드의 기존 필드만 읽어 한 원인으로 묶은 것(gpt-6.1-sol)이다.

## 4. 모델 쪽 발견 (Claude 원문 확인)

| 발견 | 근거 | 성격 |
|---|---|---|
| 식생 v 방향 항력이 u점 속력을 곱함 | `vegetation.F90:516,520` `Fvgtv = …*(s%vev(i,j)*s%vmageu(i,j))`, `(s%vv(i,j)*s%vmagu(i,j))` — x 방향은 u점끼리 | 엇갈린 격자 위치 불일치 **결함 후보** |
| 지하수 속도가 Poisson 투수계수 추정치를 쓰지 않음 | 주석 `groundwater.F90:387-397` 은 비정수압에서 속도가 해법의 추정치를 쓰도록 "강제"한다고 적지만, `gw_calculate_velocities` 는 `Kxupd = Kx`(intent(out)) 후 `Kin=Kx` 로 속도 계산 | 주석–코드 불일치, 난류 방식에서 압력·속도 투수계수 불일치 **결함 후보** |
| 비정수압 바닥경사 압력항 부호 | 보고서 인쇄식 `−(∂x(H p̄)+p∂x d)/H` vs 소스(`nonh.F90:1193-1195,1234-1238`, p̄=p/2, zb=−d) `−(∂x(H p̄)−p∂x d)/H`. 소스가 수심 적분 Leibniz 규칙과 일치 | 문서 오기 후보 — 보고서의 d 정의로 확정 필요 |

판정 모델이 추가로 지목한 결함 후보(미확인, 레코드 note 참조): 하상 속도 대체 경로의 수면경사(`kingsday:xml:23355`, `104221`), 지하수 투수계수 재사용 방향(`kingsday:xml:96136`, `96665`, `master:xml:91067`), `cats` sentinel 적용 조건(`kingsday:xml:27792`). 주요 문서 오기 후보: 표사 확산 부호(`kingsday:xml:26946`, `master:xml:31157`), 공극률 상한(`master:xml:90719`, `kingsday:xml:96318`), 응력 항등식(`nonhydro:word:45061`, `45539`), 분산관계 유도(`nonhydro:word:184203`, `184944`, `185208`).

## 5. 상태 (PLAN §4)

- **기록 완료**: 443건 처분 + 결정적 검사 + 적대 검증 2회 + 멈춤 규칙 적용.
- **의미·구현 공백**: 미해결 141 (위 §3). 동결 조건상 공백이 남으면 R2 는 **미완**이다.
- **사용자 결정**: 공백을 수용할지 — 수용만으로 동결 완료 조건을 충족했다고 기록하지 않는다.
- `models/` 반영은 R2 단위 SCOPED EDIT 1회(Codex diff → Claude 검증 → 사용자 sudo). R3 전체·R4 자동 착수 안 함. 사람 승인 발급 없음.
