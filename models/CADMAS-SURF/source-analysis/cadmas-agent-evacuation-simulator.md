---
title: "CADMAS AGENT 쓰나미 피난 시뮬레이터 — potential-field(Dijkstra) 항법·Tobler hiking·수심 익사판정·CADMAS 결합 (main·solver·move_agent·make_potential_*·update_attribute)"
model: CADMAS-SURF
component: src (AGENT evacuation simulator)
canonical_source: self
verification_method: "AGENT 소스 40 .f90 전수 read (raw/.../Simulators/AGENT/Source code/). main.f90:1-3·13(agent_ver3.5) + solver.f90:66-99 시간루프 + 에이전트 m_agent.f90:6-43(상태 0/1/2/3·deadline·weight) + move_agent.f90:48-132(이동·수중감속:59) + Tobler slope_function.f90:23(F=1.191246·exp(-3.5|S+0.05|)) + potential recursive_search_shelter.f90(8방향 Dijkstra)·make_n_potential.f90(flag0최단/1쓰나미회피/2확률) + get_direction.f90(8근방 최급강하) + CADMAS read_cadmas.f90·remesh.f90·익사 update_attribute.f90:54-82(max_depth>deadline) + 확률 random_normal.f90(Box-Muller). file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md
  - models/CADMAS-SURF/README.md
---

# CADMAS AGENT 쓰나미 피난 시뮬레이터

> 멀티스케일 사슬의 종착(STOC→SURF/3D→2F→STR3D→**AGENT**). 격자기반 **potential-field 멀티에이전트 피난 모델**(self-id `agent_ver3.5` `main.f90:13`), CADMAS 침수결과(수심·유속)에 결합. MPMD `l_mlt_agent`(`mod_comm.f90:26·41`). 경로 루트: `raw/.../Simulators/AGENT/Source code/`. 40 .f90 전수 커버.

## 1. 드라이버·시간루프 (main.f90 → solver.f90)

`main.f90`(헤더 `メインルーチン` :1-3): `init_mpmd`(:17)→`read_condition`(namelist.inp :31)→`read_agent`(agent.inp :36)→`allocate_potential`(:41)→`read_potential`(:46)→`read_cadmas(0)`(:51)→`solver`(:61).

실제 시간적분 `solver.f90` 루프 `do nstep=1,maxstep`(`:66-99`): ①`time+=dt` ②`read_cadmas(1)`(쓰나미 수심/유속 갱신 :70) ③`update_rw`(랜덤워크 :73) ④`make_potential_mob`(군중 :78) ⑤`move_agent`(:83) ⑥`update_attribute`(상태/사망 :86) ⑦`output(1)`(:89) — `time≥time_end` 종료(:97). 8 모듈: `m_agent·m_cadmas·m_danger·m_potential·m_prob·m_flag·m_timectl·m_output`.

## 2. 에이전트 모델 (m_agent·move_agent)

표현(`m_agent.f90:6-43`): 셀 `i/j_agent`·위치 `agent_x/y/z`·속도 `agent_u/v·vel`·**상태 `agent_status` 0=피난완료·1=이동·2=수중이동·3=사망**(`:17`)·`deadline`(허용 최대수심, 초과 시 사망 :21)·랜덤워크 `rw_sigma/theta/dt`·행동가중 `weight_signpost/shelter/mob/danger`·`agent_start`(출발시각). `vertical_evacuation_speed=0.479 m/s`(피난소 등반 :43). `age/height`는 선언만·계산 미사용.

이동(`move_agent.f90`, `do n=1,n_agent` :28): `time≤agent_start` skip(:32)·피난완료/사망 skip(:43). 피난소 내 연직피난 `agent_z+=0.479·dt`(:48-55). 상태1 `velocity=vel`·**상태2 수중감속 `velocity=vel·(1-depth/deadline)`**(:59). 방향=`get_direction`(:61)→signpost override(:65-68)→랜덤워크 `theta+=rw_theta`(:70). `u=velocity·cosθ`·`xnext=xnow+u·dt`(:106-107), 영역밖 차단(:119-126).

**Tobler hiking 함수**(`n_slope==1`): 사면 `S=(h_next-h_now)/dxy`→`slope_function`→`u=velocity·xn·F`. `slope_function.f90:23`:
```
F = 1.191246·exp(-3.5·|S+0.05|)          ! Tobler hiking, 최대속도 내리막 S≈-0.05
```

> disclosed: `underwater_function.f90`(수심×유속 2D 감속표, depth_limit 0.7m·flow_limit 2.5m/s)은 구현돼 있으나 **move_agent 에서 미호출(dead code)** — 실제 감속은 :59 수심비례식. `weight_danger`도 선언만(danger 는 n_potential 에 folding).

## 3. potential-field 항법 (Dijkstra형)

피난소별 **비용/시간 potential field**(8방향 재귀 flood-fill = Dijkstra형 최단경로) + 군중 potential + signpost. 에이전트는 **총 potential 8근방 최급강하**.

- **`make_potential_shelter.f90`**: 피난소별 `pot_shelter=9999` 초기화(:42)·소스셀 미소(:45)→`recursive_search_shelter`(:46)→시간환산(×dxy + 연직피난시간 :71-84)→`n_potential=-1/n_potential`(역시간 최대화 :140-146)
- **`recursive_search_shelter.f90`**: 8방향 Dijkstra 완화(직진 `dr=1`·대각 `dr=√2` :35·137), `pot(next)>dnext & move_boundary≠-1`일 때만 완화(:45-46). `n_slope==1`이면 `dr=dr/F`(사면)
- **`make_n_potential.f90`**(flag별 :18): **flag0 최단**=최근접 피난소(`m_pot_shelter(sort_index(1))` :69-76) / **flag1 쓰나미회피**=도달시간맵(`danger_path`) 대비 통과시간 `EPT2≥arrival_time`이면 셀차단(:429-433) / **flag2 확률회피**=완화 임계 `set_prob=ini_prob+rate·counter`(:516-518), 확률맵 `arrival_prob≥set_prob` 차단(:841-845)
- **`get_direction.f90`**: 현셀+8근방 `pot_total` 최소 선택(대각 `(pot-potnow)/√2+potnow` :95)→`theta=atan2(dy,dx)`(:148-150)
- **`pot_total.f90`**: `n_potential·weight_shelter + pot_mob_revise·weight_mob`(:20-32)
- **signpost**(`make_signpost.f90`): 에이전트별 확률준수 `rand≤weight_signpost→iflag=1`(:33-38), 영향반경 `r_signpost`. 활성 시 move_agent 가 `theta` override
- **군중**(`make_potential_mob.f90`): 셀별 생존 에이전트수 `nsum_agent`(:26-30)→`pot_mob-=nsum/rr`(반경 `r_mob` :33-59). `_revise`는 자기기여 제거(:44)

## 4. CADMAS 결합 + 익사판정

- 수입데이터(`m_cadmas.f90:10-34`): 지형 `height_c`·수심 `depth_c`·유속 `uu_c/vv_c`·갱신시각 → remesh 후 `height/depth/uu/vv/max_depth`. `read_cadmas.f90`: **MPI 온라인**(`cadmas_rank≥0` :61-96/193-211) 또는 **오프라인 비정형파일 `data.ma`**(:101-149/216-249), `time≥cadmas_tnext` 트리거(:191)
- `remesh.f90`: CADMAS 비정형격자→균일 에이전트격자 쌍선형보간(지형/수심/유속), `max_depth=max(max_depth,depth)`(:195-197)
- **익사판정**(`update_attribute.f90:26-97`): **`max_depth(i,j) > deadline(n)`**(첨두 침수수심 vs 에이전트 허용치) — depth×velocity 곱 아님. `depth≤0`→상태1(but max_depth>deadline 사망 :54-62)·`0<depth<deadline`→상태2(:63-73)·`depth≥deadline`→상태3 즉시사망(:74-82). 피난소 도달→상태0 피난완료(:44-51)

## 5. 확률·통계

- 방향 불확실성: `random_normal.f90`(Box-Muller N(0,σ) :20-31)·`rw_sigma`(deg→rad)→`rw_theta` 매 `rw_dt`
- signpost 준수: Bernoulli(`random_number` vs `weight_signpost` :33-34)
- 출발시각 `agent_start`(에이전트별 입력)·확률 쓰나미회피(`m_prob` flag2)

## 6. 잔여 (1줄 역할)

`mod_comm.f90`(MPMD)·`initialize.f90`(전루프 리셋)·`read_condition/agent/potential/move_boundary/shelter/signpost.f90`(입력)·`allocate_cadmas/potential.f90`·`output.f90`(binary agent.out+statistics csv)·`open_file.f90`(debug.txt)·`errmsg/errstop.f90`(mpi_abort).

> 멀티스케일 사슬 종착: 쓰나미 유체(STOC/CADMAS)→인명피해·피난행동. 익사판정·Tobler hiking·Dijkstra 피난항법이 코어.
