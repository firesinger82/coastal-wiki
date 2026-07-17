---
title: "CADMAS-AGENT 영문 매뉴얼 — 멀티에이전트 피난 모델(potential-field·signpost·mob·확률회피) (소스 cross-confirm, Tobler 식 소스전용 적발)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
verification_method: "CADMAS-AGENT_Manual_English.pdf(30p, 기계번역) pdftotext. 시스템(p.3)·potential 항법 eq7-1(p.26)·shelter potential -1/r eq7-3(p.27)·mob eq7-4(p.27)·signpost(p.28)·랜덤워크 eq7-5(p.28)·익사 deadline(p.7·18 Table6-2)·CADMAS online/offline data.ma(p.3·9-14)·입출력(p.5-12)·확률회피 §7.4-7.5(p.28-29). 소스 cross-confirm: get_direction.f90·recursive_search_shelter.f90·slope_function.f90:23·update_attribute.f90·random_normal.f90. 적발: Tobler 식 소스전용(매뉴얼 미인쇄)·익사=max_depth(peak)·underwater_function dead-code. printed page+file:line."
citation_status: verified
has_source_needed: false
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/cadmas-agent-evacuation-simulator.md
---

# CADMAS-AGENT 영문 매뉴얼 — 피난 모델

> 번들 `Simulators/AGENT/Manual/CADMAS-AGENT_Manual_English.pdf`(30p, 기계번역 JP→EN, TOC 북마크 깨짐). 격자기반 멀티에이전트 피난, CADMAS 침수결과 결합. [소스 AGENT 노트](../source-analysis/cadmas-agent-evacuation-simulator.md)와 cross-confirm.

## 1. 모델 개요 (p.3·26)

CADMAS-SURF 2D 수심·유속을 통신/파일로 받아 피난 시뮬. 이동은 8근방 셀 potential 최소방향(연속좌표, Δt≤dx/v_max eq2-1 p.4). potential 중첩 `U_k=a_{k,1}u_1+a_{k,2}u_2+...`(eq7-1 p.26). 상태(Table6-2 p.18): 0 피난완료·1 이동·2 수중이동·3 사망. → 소스 `get_direction.f90:27-143`(8근방 `pot_total` 최소, 대각 `/√2`).

## 2. 보행 모델

- **사면(hiking)**: 매뉴얼은 개념만, `n_slope` 토글(p.6)만 노출. **Tobler 식 `F=1.191246·exp(-3.5|S+0.05|)` 미인쇄** → 소스 `slope_function.f90:23`만 보유(주석 "sample 함수"=사용자 교체가능). ⚠ **소스전용**
- **수중감속**: 매뉴얼 정성적(status2). 소스 실제경로 `move_agent.f90:59` 선형 `vel·(1−depth/deadline)`. ⚠ 별도 `underwater_function.f90`(수심×유속 표 depth_limit0.7·flow_limit2.5)는 **미호출 dead-code**
- 기본속도 `agent.inp` Velocity 열(p.7, sample 3.0 m/s)

## 3. potential-field 항법 (p.26-28)

- **shelter potential** `u=−1/r`(eq7-3 p.27), r=**최단경로거리**(직선 아님). → 소스 `recursive_search_shelter.f90`(8방향 Dijkstra형 완화, 대각 √2, `move_boundary=-1` 차단)
- **signpost**(p.28): 영향반경 셀 진입 시 확률적으로 표지방향 추종. → `move_agent.f90:65-67`(`theta_signpost` override). `signpost.inp`=i,j,r,θ
- **mob(군중)** `u=−Σ1/d`(eq7-4 p.27, 반경 r_mob, 자기기여 제외). → `make_potential_mob.f90:54`+`_revise`. 음부호=군중 유인(낮은 potential로 이동)

## 4. 익사 판정 (p.7·18)

매뉴얼: `deadline`=에이전트 허용수심(초과 시 사망), `agent.inp` 5열(p.7, sample 1.0m). **순수 수심임계**(depth×velocity 아님). → 소스 `update_attribute.f90` `max_depth(i,j)>deadline(n)`(:35·56·65). ⚠ **핵심 뉘앙스**: 순간수심 아닌 **`max_depth`(누적 첨두수심, `remesh.f90:195`)** — 물 빠져도 첨두 초과 셀은 사망. 매뉴얼은 "above this depth"로만 기술(첨두 미공개).

## 5. CADMAS 결합 (p.3·9-14)

- **online(MPMD/MPI)**: CADMAS·MA 별도 실행파일 통신(appfile, `mpirun -p4pg`, p.13)
- **offline(파일)**: CADMAS가 `data.ma`(binary, Fortran unformatted) 작성→독립 read(`&offline`, p.14). 포맷(Table3-2 p.10): 헤더(icmax,jcmax·xc/yc·height) + 시각별 depth_c·uu_c·vv_c(real4)
- → 소스 `read_cadmas.f90`(MPI path + `cadmas_rank=-1`이 online/offline 스위치)·`remesh.f90`(CADMAS격자→균일 에이전트격자)

## 6. 확률 요소

- **랜덤워크** θ=θ_pot+θ_rw, θ_rw~N(0,rw_sigma)(eq7-5 p.28, σ deg p.7). → `random_normal.f90:20-31`(**Box-Muller**), `move_agent.f90:70`
- 출발시각 `agent_start`(p.7) → `move_agent.f90:32`
- 쓰나미 회피: §7.4 도달시간 회피(`flag_danger`, danger.txt; Sakata et al. JSCE B2 76(2) 2020) / §7.5 도달확률 회피(`flag_prob`, ini_prob·relaxation_rate; Ishiyama et al. APAC2023)

## 7. 입출력 (p.5-12)

입력: `namelist.inp`(&time·agent·potential·output·offline·flag·danger·prob)·`agent.inp`(N,X0,Y0,Vel,Deadline,rw_sigma,W_signpost,W_shelter,W_mob,agent_start)·`shelter.inp`(N,i,j,z)·`signpost.inp`(N,i,j,r,θ)·`move_boundary.inp`(0=진입/-1=차단)·potential `NNN.txt`·`data.ma`(CADMAS). 출력: `agent.out`(binary 시계열)·`statistics_{i,r}.csv`(피난완료/이동/사망 수)·`debug.txt`. 시각화=CADMAS-VR(agent.out+.grp).

## 적발 요약

1. **Tobler hiking 식 소스전용**(`slope_function.f90:23`, 매뉴얼 미인쇄, "sample"=교체가능)
2. **익사=peak depth(`max_depth`)** depth-only(`update_attribute.f90`), 매뉴얼은 첨두 미공개
3. **underwater_function.f90 dead-code**(미호출), 수심×유속 표 미사용
4. **`vertical_evacuation_speed=0.479 m/s`**(`m_agent.f90:43`) 매뉴얼 부재 상수
