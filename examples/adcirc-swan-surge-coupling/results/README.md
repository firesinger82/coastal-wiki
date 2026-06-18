---
title: "ADCIRC+SWAN 결합 — 검증 포인트 (정량 run 미수록)"
canonical_source: self
citation_status: verified
verification_method: >
  검증 절차의 메커닉 단언(수위 분해·RS 흡수·로그 메시지·NWS 인코딩)은 상위
  example README 및 adcirc-swan-coupling.md(couple2swan.F/read_input.F file:line)
  에 위임. 본 노트는 그 검수 메커닉으로부터 도출된 점검 항목 목록이며 새 정량
  단언을 만들지 않음. 정량 비교 run 은 미수록(source-needed).
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - examples/adcirc-swan-surge-coupling/README.md
  - models/ADCIRC/source-analysis/adcirc-swan-coupling.md
---

# 검증 포인트

> 본 예제는 절차 템플릿이므로 정량 결과 run을 싣지 않는다(`source-needed`).
> 대신, 결합이 **실제로 동작**하는지와 **wave setup이 surge에 더해졌는지**를
> 확인하는 점검 항목을 제시한다. 모든 메커닉 전거는
> [상위 README](../README.md) 및
> [`adcirc-swan-coupling`](../../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md).

## 1. 결합이 켜졌는지 (로그)

- ADCIRC 로그에 **"WAVES WILL BE COUPLED TO SWAN"** 출력 → `NRS=3` 파싱 성공
  (`read_input.F:2255-2261`).
- 실행 바이너리가 `padcswan`인지 확인. `padcirc`면 NWS=3xx여도 파 결합 없이 조용히 실행
  (`makefile:195-233`).

## 2. 메시 단일성

- ADCIRC `fort.14`와 SWAN이 읽은 메시의 노드 수 `np`·요소 수 `ne`가 동일한지.
  SWAN은 자신의 copy를 read하므로 두 파일이 다르면 경계에서 결과가 조용히 어긋남
  ([swan-adcirc-coupling-implementation Pitfalls](../../../models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md)).

## 3. 결합 주기 정합

- `SWAN_DT(=fort.26 COMPUTE DELTC) / DT(fort.15)`가 정수인지 확인.
  비정수면 간격 반올림으로 출력 빈도 이상 발생(`couple2swan.F:1079-1081`).

## 4. wave setup 기여 분해 (핵심 검증)

coupled run의 수위 `η`(fort.63)는 **surge + tide + wave setup**의 합이다. wave setup은
SWAN `SETUP`이 아니라 **ADCIRC가 radiation-stress gradient를 흡수**해 생성된다
(unstructured SWAN의 `SETUP`은 내부 비활성, `swanpre1.ftn:2089-2092`). 분해 절차:

| 비교 run | 설정 | 차이가 보여주는 것 |
|---|---|---|
| (A) 결합 run | `NWS=3xx` (padcswan) | surge + tide + **wave setup** |
| (B) surge-only run | `NWS=20/12/8...` (NRS=0) | surge + tide (파 없음) |
| η(A) − η(B) | 동일 메시·기상·시각 | **wave setup 기여분** (해안 근처에서 양(+)) |

- 기대: 천해·쇄파대 인근에서 η(A) > η(B) (radiation stress 수렴으로 set-up).
  외해 깊은 곳에서는 set-down 가능.
- 정성 sanity: storm-surge 이론의 wave setup 규모(서해 예시 +~1 m 자리)와 부호 일치
  ([storm-surge 02-theory §3.2 / 본문 wave setup 언급](../../../concepts/storm-surge/02-theory.md)).
  정확한 정량값은 도메인·파 입력 의존 → `source-needed`.

## 5. radiation stress 전달 확인

- SWAN 출력의 `Hs`·`Dir`가 합리적이면, ADCIRC `RSNX2/RSNY2`(파-유도 force)가
  momentum에 가산됨(`timestep.F:721-725`). max 수위(maxele.63)가 surge-only 대비
  해안에서 증가하면 RS 전달이 동작한 정황.

## 6. (선택) SWAN 시간창 제한 검증 (PR #498)

- `&SWANTimeControl` 사용 시: 시간창 밖 구간에서 SWAN 출력이 sentinel(`-99999`)이고
  RS가 0인지 → 그 구간은 ADCIRC-only 효과.
- 전체-시간 SWAN run과 비교해 peak surge/Hs 차이를 정량화(PR body: 최신 소스에서 default
  전체 시간 프레임이면 차이 없음)
  ([adcirc-swan-coupling — Temporal Controls](../../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md)).

## 미수록 (source-needed)

- 실제 도메인 정량 비교(η 분해 절댓값, RMSE vs 관측 조위·파고).
- hot-start NetCDF `NRS=3` 재시작 정합성(잠재 이슈 `netcdfio.F90:8017-8085` 보고).
