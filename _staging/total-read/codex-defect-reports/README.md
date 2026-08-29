# Codex 결함 리포트 (게이트 밖 — standalone)

> 2026-08-29. supplement 게이트(1차↔감사 crosswalk)는 **두 판독자가 낸 findings 만** 승격 가능.
> 아래는 그 밖의 Codex 독립 감사 결과 — **supplement 아님**, canonical 미반영. 모델 코드 자체의 버그 목록.

## A — FUNWAVE/EFDC 3차 독립 판독 (in-scope 코어, task-mtece00a)
두 판독자가 이미 본 코어 솔버 ~30파일을 Codex 가 3차로 독립 판독, 둘 다 놓친 신규 material 결함 탐색.
- **결과: 신규 HIGH 0 · MED 3** → 2-판독자 커버리지가 강했음을 재확인(중대 누락 없음).
- MED 3(전부 logic, `A-new-deltas.json`): etauv_solver.F L425-431 · mod_time_spectra.F L325-373 · mod_sediment.F L1385-1400.
  (per-finding 상세는 task 가 파일 미기록 — 필요 시 재요청.)

## B — ADCIRC 코어 1차 결함감사 (무감사 모델, task-mtecge90)
ADCIRC(base/감사 없음, ~305k줄) 코어 12파일 first-pass. `B-adcirc-deltas.json`.
- **결과: 7 material (HIGH 4 · MED 3)**:
  - HIGH itpackv.F L470,551-581 — JCG q1 saved-local use-before-assign(반복솔버 all-reduce 카운트 상이)
  - HIGH momentum.F L864-901 — type-41 경계서 NOFF(0) OOB(NEle 가드가 참조 뒤)
  - HIGH normal_flow_boundary.F90 L78-99 — 수직 경계세그먼트서 NY_R=0 → 0-나눗셈
  - HIGH weir_boundary.F90 L2477-2579 — FLUX INTENT(OUT) 특정 head 조합서 미대입
  - MED gwce.F L1325-1334 — CfacS0 가 DPavgS0 대신 현재 DPavg 로 Ma2 재계산(시간레벨 혼합)
  - MED wetdry.F L172,841-845 — IT(타임스텝) vs BTIME_END(초) 단위 불일치
  - MED wetdry.F L867-1056 — 신규 wet 노드(NM1)에 salinity/temp 를 NM3 에 기록(노드 오지정)
- ★base/감사 없어 supplement 게이트 진입 불가. 정식화하려면 별도 감사 채널 필요.
- ROMS(2.8M)·Delft3D(1.6M)·ADCIRC 잔여는 후속(메가프로젝트).

## B 적대검증 (2026-08-29, task-mtedvg99)
ADCIRC HIGH 4건을 독립 skeptic 이 REFUTE 시도 → **전건 CONFIRM**(교차파일 추적, `B-adcirc-verify.json`):
- H0 itpackv.F: bare SAVE q1, DATA/init 없음, in=0 후 첫 itjcg 가 pstop_nrms 대입 전 q1 read(L551) — messenger MP 카운트 상이 확인.
- H1 momentum.F: type-41 wrap slot(NNeigh-1)=0, NOFF(MNE) 하한 1 → NOFF(0) OOB(L900, mesh/global 추적).
- H2 normal_flow_boundary.F90: NY_R←SIII_OLD=(XGK-XGJ)/XL(mesh L2433), 상수-x chord 시 TAUX_R=0, epsilon 가드 없음.
- H3 weir_boundary.F90: 전 분기+호출부 무-default, PIPE_FLUX INTENT(OUT) 진입 시 미정의, RBARWL=ETA2-PIPEHT 특정값 전분기 우회.
→ ADCIRC HIGH 4 = supplement 수준(원문 span + 적대검증) 신뢰도. 단 base/감사 부재로 게이트엔 미진입(별도 채널 필요).
