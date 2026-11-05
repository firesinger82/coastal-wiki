# CADMAS-SURF code-1 전수 검증

검증일: 2026-11-04.
대상은 사용자 지정 AGENT 40개 기록과 CADMAS-SURF-3D 헤더 10개 기록이다.
완료 기록 표에서 집계한 대조 범위는 50개 기록의 171개 구간 행이다.
해당 frontmatter가 가리키는 원문의 행 수 합계는 5,161행이다.
최종 검사에서 4,969개 비공백 원문 행의 인용 문자열과 행 번호가 모두 일치했다.
구간의 누락·중복은 없었다.
원문 SHA-256은 각 기록의 frontmatter 값과 모두 일치했다.
frontmatter와 구간 경계는 수정하지 않았다.
각 구간마다 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
각 호출은 최대 200행이다.
원문 인용의 문자열·행 번호는 기계 대조했다.
요약·조건·식·바깥 블록·주석의 뜻은 원문을 읽어 대조했다.
원문과 git은 변경하지 않았다.
모델은 실행하지 않았다.
원문 행 수는 빈 행을 포함한다.
정정·보완은 아래 수정 항목 수다.
이상 없음은 완료 기록의 구간 행 중 수정하지 않은 구간 행 수다.
표 밖의 코드 사실 수정은 별도 항목으로 센다.
기록 경로의 접두사는 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/`이다.

## 완료 기록

| 기록 | 대조한 원문 행 수 | 대조한 구간 행 수 | 상태 |
|---|---:|---:|---|
| AGENT/Source code/allocate_cadmas.f90.md | 29 | 2 | 완료 |
| AGENT/Source code/allocate_potential.f90.md | 69 | 3 | 완료 |
| AGENT/Source code/errmsg.f90.md | 26 | 2 | 완료 |
| AGENT/Source code/errstop.f90.md | 19 | 1 | 완료 |
| AGENT/Source code/get_direction.f90.md | 153 | 4 | 완료 |
| AGENT/Source code/initialize.f90.md | 42 | 2 | 완료 |
| AGENT/Source code/m_agent.f90.md | 154 | 4 | 완료 |
| AGENT/Source code/m_cadmas.f90.md | 105 | 3 | 완료 |
| AGENT/Source code/m_danger.f90.md | 7 | 1 | 완료 |
| AGENT/Source code/m_flag.f90.md | 6 | 1 | 완료 |
| AGENT/Source code/m_output.f90.md | 59 | 2 | 완료 |
| AGENT/Source code/m_potential.f90.md | 254 | 8 | 완료 |
| AGENT/Source code/m_prob.f90.md | 12 | 1 | 완료 |
| AGENT/Source code/m_timectl.f90.md | 17 | 1 | 완료 |
| AGENT/Source code/main.f90.md | 74 | 3 | 완료 |
| AGENT/Source code/make_n_potential.f90.md | 918 | 19 | 완료 |
| AGENT/Source code/make_potential_mob.f90.md | 62 | 2 | 완료 |
| AGENT/Source code/make_potential_mob_revise.f90.md | 50 | 2 | 완료 |
| AGENT/Source code/make_potential_shelter.f90.md | 149 | 5 | 완료 |
| AGENT/Source code/make_signpost.f90.md | 72 | 3 | 완료 |
| AGENT/Source code/mod_comm.f90.md | 330 | 8 | 완료 |
| AGENT/Source code/move_agent.f90.md | 140 | 4 | 완료 |
| AGENT/Source code/open_file.f90.md | 45 | 3 | 완료 |
| AGENT/Source code/output.f90.md | 156 | 4 | 완료 |
| AGENT/Source code/pot_total.f90.md | 35 | 2 | 완료 |
| AGENT/Source code/random_normal.f90.md | 35 | 2 | 완료 |
| AGENT/Source code/read_agent.f90.md | 126 | 3 | 완료 |
| AGENT/Source code/read_cadmas.f90.md | 278 | 8 | 완료 |
| AGENT/Source code/read_condition.f90.md | 131 | 4 | 완료 |
| AGENT/Source code/read_move_boundary.f90.md | 54 | 2 | 완료 |
| AGENT/Source code/read_potential.f90.md | 39 | 2 | 완료 |
| AGENT/Source code/read_shelter.f90.md | 56 | 2 | 완료 |
| AGENT/Source code/read_signpost.f90.md | 58 | 2 | 완료 |
| AGENT/Source code/recursive_search_shelter.f90.md | 239 | 6 | 완료 |
| AGENT/Source code/remesh.f90.md | 238 | 6 | 완료 |
| AGENT/Source code/slope_function.f90.md | 26 | 2 | 완료 |
| AGENT/Source code/solver.f90.md | 115 | 4 | 완료 |
| AGENT/Source code/underwater_function.f90.md | 96 | 3 | 완료 |
| AGENT/Source code/update_attribute.f90.md | 110 | 4 | 완료 |
| AGENT/Source code/update_rw.f90.md | 26 | 2 | 완료 |
| CADMAS-SURF-3D/Source code/VF_A0PRM.h.md | 70 | 3 | 완료 |
| CADMAS-SURF-3D/Source code/VF_A0PRM_mpversion.h.md | 56 | 3 | 완료 |
| CADMAS-SURF-3D/Source code/VF_ACOMPI.h.md | 33 | 2 | 완료 |
| CADMAS-SURF-3D/Source code/VF_ACOMPR.h.md | 35 | 3 | 완료 |
| CADMAS-SURF-3D/Source code/VF_ACPUTR.h.md | 46 | 2 | 완료 |
| CADMAS-SURF-3D/Source code/VF_ADBGI.h.md | 23 | 2 | 완료 |
| CADMAS-SURF-3D/Source code/VF_ADBGR.h.md | 14 | 2 | 완료 |
| CADMAS-SURF-3D/Source code/VF_AFILEI.h.md | 204 | 7 | 완료 |
| CADMAS-SURF-3D/Source code/VF_AFILER.h.md | 44 | 3 | 완료 |
| CADMAS-SURF-3D/Source code/VF_ANUMBI.h.md | 26 | 2 | 완료 |

## 정정·보완 목록

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 | 종류 |
|---|---|---|---|---|
| get_direction.f90.md:74–115 | 대각 방향은 현 셀 대비 포텐셜 차를 root2로 나눈 값을 비교한다(95·109). | 대각 방향은 현 셀 대비 포텐셜 차를 root2로 나눈 뒤 potnow를 더한 값을 potmin과 비교한다(95–96·109–110). | get_direction.f90:95–96,109–110 | 정정 |
| get_direction.f90.md:116–153 | 음수 ierr를 검사한다(145). 이동 방향 계산이라는 주석(147) 아래 목표 셀 중심과 실제 에이전트 좌표 차를 dxy로 계산하고 atan2로 theta를 구한다(148–150). | `if(ierr<0) call errstop(rout,ierr)`로 음수 ierr를 처리한다(145). 이동 방향 계산이라는 주석(147) 아래 `target_dx=dxy*(dble(i_target)-0.5d0)-agent_x(n)`과 `target_dy=dxy*(dble(j_target)-0.5d0)-agent_y(n)`을 계산한다(148–149). `theta=atan2(target_dy,target_dx)`를 계산한다(150). 해석: dxy와 목표 인덱스로 만든 좌표를 목표 셀 중심으로 볼 수 있다. | get_direction.f90:145–150 | 정정 |
| get_direction.f90.md:note | - 29–31·148–150: 더 낮은 이웃이 없으면 초기 목표는 현재 셀이고 theta는 현재 셀 중심까지의 좌표 차로 계산된다. | - 29–31·148–150: 더 낮은 이웃이 없으면 초기 목표 인덱스는 현재 셀 인덱스다. theta는 148–149행의 target_dx·target_dy를 인수로 계산된다. | get_direction.f90:29–31,148–150 | 정정 |
| make_n_potential.f90.md:401–464 | 피난 시간 계산(406)은 dr의 대각 여부 판단·경사 보정·PT와 EPT 누적·음수 EPT의 0 설정·시작 시각 합산을 수행한다. | 피난 시간 계산에서 `if(i_now /= i_next .and. j_now /= i_next) then`이면 `dr = root2`를 설정한다(407–408). 그 외에는 `dr = 1.0d0`을 설정한다(409–411). 두 번째 비교는 j_next가 아니라 i_next를 사용한다. 이후 경사 보정·PT와 EPT 누적·음수 EPT의 0 설정·시작 시각 합산을 수행한다. | make_n_potential.f90:407–424 | 정정 |
| make_n_potential.f90.md:465–495 | 아니면 피난 불가이므로 최단 경로를 넣는다는 주석(478)대로 가장 가까운 피난소 장을 복사한다. | 아니면 피난 불가이므로 최단 경로를 넣는다는 주석(478) 아래 초기 위치의 포텐셜 값이 가장 작은 피난소인 sort_index(1)의 장을 복사한다(44–62·478). | make_n_potential.f90:44–62,478 | 정정 |
| make_n_potential.f90.md:113–161 | 시작 시 81행 flag==1 분기 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. | make_n_potential.f90:69,81,915 | 보완 |
| make_n_potential.f90.md:162–229 | 시작 시 81행 flag==1 분기·113행 shelter_loop·156행 search_loop 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. 바깥 반복문 `shelter_loop: do mm=1,n_shelter`(113)는 464행에서 닫힌다. 바깥 반복문 `search_loop: do`(156)는 463행에서 닫힌다. | make_n_potential.f90:69,81,113,156,373,460–464,915 | 보완 |
| make_n_potential.f90.md:230–298 | 시작 시 81행 flag==1 분기·113행 shelter_loop·156행 search_loop 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. 바깥 반복문 `shelter_loop: do mm=1,n_shelter`(113)는 464행에서 닫힌다. 바깥 반복문 `search_loop: do`(156)는 463행에서 닫힌다. | make_n_potential.f90:69,81,113,156,373,460–464,915 | 보완 |
| make_n_potential.f90.md:299–347 | 시작 시 81행 flag==1 분기·113행 shelter_loop·156행 search_loop 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. 바깥 반복문 `shelter_loop: do mm=1,n_shelter`(113)는 464행에서 닫힌다. 바깥 반복문 `search_loop: do`(156)는 463행에서 닫힌다. | make_n_potential.f90:69,81,113,156,373,460–464,915 | 보완 |
| make_n_potential.f90.md:348–371 | 시작 시 81행 flag==1 분기·113행 shelter_loop·156행 search_loop 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. 바깥 반복문 `shelter_loop: do mm=1,n_shelter`(113)는 464행에서 닫힌다. 바깥 반복문 `search_loop: do`(156)는 463행에서 닫힌다. `go to 1000`(368)의 대상은 461행 `1000 continue`다. | make_n_potential.f90:69,81,113,156,373,460–464,915 | 보완 |
| make_n_potential.f90.md:372–400 | 시작 시 81행 flag==1 분기·113행 shelter_loop·156행 search_loop 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. 바깥 반복문 `shelter_loop: do mm=1,n_shelter`(113)는 464행에서 닫힌다. 바깥 반복문 `search_loop: do`(156)는 463행에서 닫힌다. `if(nskip == 8) then`(373)은 460행에서 닫힌다. | make_n_potential.f90:69,81,113,156,373,460–464,915 | 보완 |
| make_n_potential.f90.md:401–464 | 시작 시 81행 flag==1 분기·113행 shelter_loop·156행 search_loop·373행 nskip==8 조건 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. 바깥 반복문 `shelter_loop: do mm=1,n_shelter`(113)는 464행에서 닫힌다. 바깥 반복문 `search_loop: do`(156)는 463행에서 닫힌다. 시작 시 `if(nskip == 8) then`(373) 안이며 402행 `else`를 거쳐 460행 `endif`에서 닫힌다. | make_n_potential.f90:69,81,113,156,373,402,460–464,915 | 보완 |
| make_n_potential.f90.md:465–495 | 시작 시 81행 flag==1 분기 안. | 바깥 조건은 `if(flag==0)then`(69)의 `else if(flag==1)then` 분기(81)이며 915행 `endif`에서 닫힌다. | make_n_potential.f90:69,81,915 | 보완 |
| make_n_potential.f90.md:496–558 | 시작 시 1행 make_n_potential 루틴 안. | 496행 `elseif(flag==2)then`은 69행 `if(flag==0)then`에서 시작한 분기 사슬에 속한다. 이 조건문은 913행 `else`를 거쳐 915행 `endif`에서 닫힌다. | make_n_potential.f90:69,496,913–915 | 보완 |
| make_n_potential.f90.md:559–625 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. | make_n_potential.f90:69,496,517,524,553,764,769–802,875–879,901,915 | 보완 |
| make_n_potential.f90.md:626–691 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. | make_n_potential.f90:69,496,517,524,553,764,769–802,875–879,901,915 | 보완 |
| make_n_potential.f90.md:692–738 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. | make_n_potential.f90:69,496,517,524,553,764,769–802,875–879,901,915 | 보완 |
| make_n_potential.f90.md:739–767 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. `go to 1002`(764)의 대상은 876행 `1002 continue`다. | make_n_potential.f90:69,496,517,524,553,764,769–802,875–879,901,915 | 보완 |
| make_n_potential.f90.md:768–800 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. `if(nskip == 8) then`(769)은 875행에서 닫힌다. 내부 `if((i_now==i_agent(n) .and. j_now==j_agent(n)) .or. cellstep == 1) then`(771)의 782행 `else`는 802행 `endif`까지 이어진다. | make_n_potential.f90:69,496,517,524,553,764,769–802,875–879,901,915 | 보완 |
| make_n_potential.f90.md:801–838 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2·769행 nskip==8 조건·771행 조건의 782행 else 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. 시작 시 `if(nskip == 8) then`(769) 안이다. 내부 `if((i_now==i_agent(n) .and. j_now==j_agent(n)) .or. cellstep == 1) then`(771)의 782행 `else` 안에서 시작하며 이 내부 조건문은 802행에서 닫힌다. 769행 조건문은 805행 `else`를 거쳐 875행에서 닫힌다. | make_n_potential.f90:69,496,517,524,553,769–805,875–879,901,915 | 보완 |
| make_n_potential.f90.md:839–880 | 시작 시 496행 flag==2 분기·517행 do while·524행 shelter_loop2·553행 search_loop2·769행 조건의 805행 else 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. `shelter_loop2: do mm=1,n_shelter`(524)는 879행에서 닫힌다. `search_loop2: do`(553)는 878행에서 닫힌다. 시작 시 `if(nskip == 8) then`(769)의 805행 `else` 안이며 이 조건문은 875행에서 닫힌다. | make_n_potential.f90:69,496,517,524,553,769,805,875–879,901,915 | 보완 |
| make_n_potential.f90.md:881–918 | 시작 시 496행 flag==2 분기·517행 do while 안. | 바깥 조건은 `if(flag==0)then`(69)의 `elseif(flag==2)then` 분기(496)이며 915행에서 닫힌다. 바깥 반복문 `do while (set_prob <= 100)`(517)은 901행에서 닫힌다. | make_n_potential.f90:69,496,517,901,915 | 보완 |
| make_potential_mob_revise.f90.md:25–50 | 원 안 셀에서 동일 셀 거리는 dxy, 그 외는 실제 거리로 계산하고 pot_mob에 +1/rr을 더한다(35–44). | `if(ir2<=irmob2)then` 안에서 `if(ir2==0)then`이면 `rr=dxy`를 설정한다(38–40). 그 외에는 `rr=sqrt(dble(ir2))*dxy`를 계산한다(41–43). `pot_mob_revise(i,j)=pot_mob(i,j)+1.0d0/rr`로 보정 배열을 갱신한다(44). | make_potential_mob_revise.f90:35–44 | 정정 |
| make_potential_shelter.f90.md:87–129 | 쓰나미 도달 확률 고려 주석(95)의 flag_prob==1에서는 | 쓰나미 도달 확률 고려 주석(95)의 `elseif(flag_prob==1)then`은 앞선 `if(flag_danger==1)then`이 거짓일 때 검사한다(88·96). 이 분기에서는 | make_potential_shelter.f90:88,96 | 보완 |
| make_potential_shelter.f90.md:130–149 | 시작 시 87–96행 위험도·확률 조건 체인 안이며 131행 else는 두 조건 모두 불성립한 경우다. | 시작 시 `if(flag_danger==1)then`(88)의 `elseif(flag_prob==1)then` 분기(96) 안이다. 131행 `else`는 두 조건이 모두 거짓인 경우다. 이 조건문은 138행 `endif`에서 닫힌다. | make_potential_shelter.f90:88,96,131,138 | 보완 |
| mod_comm.f90.md:126–180 | 각 if·elseif와 MPI 인수를 보존한다. | 127행 `if( imodel==l_cadmas_2fc ) then`과 130행 `elseif( imodel==l_stoc_ic.or.imodel==l_stoc_ds ) then`의 사슬에는 ELSE가 없다. 두 조건이 거짓이면 126행의 `imodel=my_model` 값이 유지된다. 각 MPI 인수와 연속 행을 보존한다. | mod_comm.f90:126–135 | 보완 |
| mod_comm.f90.md:222–249 | 시작 디렉터리 취득(232), 디렉터리 이동(244), 실행 디렉터리 취득(246)은 주석 처리된 코드다. | 시작 디렉터리 취득(232), 디렉터리 이동(244), 실행 디렉터리 취득(246)은 주석 처리된 코드다. `if( m==1.and.my_group==l_stoc ) then`(238)과 `else if( m==1.and.my_group==l_cadmas ) then`(240)의 사슬에는 ELSE가 없다. 이 내부 조건문은 242행에서 닫힌다. | mod_comm.f90:232–246 | 보완 |
| move_agent.f90.md:27–63 | 상태 1의 수직 피난(47)은 피난소 셀에 있을 때라는 주석(49)의 조건 아래 z를 증가시키고 10으로 간다. | 상태 1의 수직 피난(47)은 `if(inow==i_shelter(m).and.jnow==j_shelter(m))then`(49) 안에서 `if(agent_z(n)<shelter_height(m))then`(50)이 참일 때 z를 증가시킨다(51). 이후 `go to 10`(52)은 134행 `10 continue`로 이동한다. 상태 분기 사슬(43·45·58)은 ELSE 없이 60행에서 닫힌다. | move_agent.f90:43–60,134 | 보완 |
| move_agent.f90.md:64–105 | 시작 시 1행 move_agent 루틴·28행 n 루프 안. | 시작 시 `do n=1,n_agent`(28) 안이며 이 반복문은 136행 `enddo`에서 닫힌다. | move_agent.f90:28,136 | 보완 |
| move_agent.f90.md:106–140 | 시작 시 1행 move_agent 루틴·28행 n 루프 안. | 시작 시 `do n=1,n_agent`(28) 안이며 이 반복문은 136행 `enddo`에서 닫힌다. | move_agent.f90:28,136 | 보완 |
| open_file.f90.md:16–35 | 장치 90의 open·close 및 로그 출력은 주석 처리되었다. | 장치 90의 open·close 및 로그 출력은 주석 처리되었다. `if( iflag==0 )then`(19)과 `elseif( iflag==1 )then`(27)의 사슬에는 ELSE가 없다. 다른 iflag 값에서는 파일 조작 없이 34행에서 반환한다. | open_file.f90:19–34 | 보완 |
| output.f90.md:26–71 | 정수·실수 통계 CSV도 status=new로 열고 헤더(header)를 출력한다. | 정수·실수 통계 CSV도 status=new로 연다(62·65). 정수 통계 헤더는 장치 15에 쓴다(64). 실수 통계 헤더는 statistics_r.csv의 장치 16이 아니라 장치 100에 쓴다(67). | output.f90:62–67 | 정정 |
| output.f90.md:72–115 | 시간·스텝·통계·개인 상태와 절대 좌표·속도를 바이너리에 쓴다. | 시간·스텝·통계·개인 상태를 바이너리에 쓴다. 좌표 출력값은 `agent_x(n)+xpin`·`agent_y(n)+ypin`·`agent_z(n)+margin`이다(93–95). 속도 출력값은 `agent_u(n)`·`agent_v(n)`이다(96–97). | output.f90:80–98 | 정정 |
| output.f90.md:116–156 | 오류 처리 주석(136)의 91·92·93 레이블은 각각 파일명과 함께 ierr=-10·errmsg를 출력하고 반환한다. | 오류 처리 주석(136)의 레이블 91·92·93은 각각 138·144·150행에 있다. 각 처리부는 `ierr=-10`을 대입한다. 이어 `call errmsg(rout,ierr)`를 호출한다. 해당 파일명을 포함한 오류 문구를 쓴 뒤 반환한다. | output.f90:138–154 | 정정 |
| pot_total.f90.md:22–35 | 군중 포텐셜 주석(27)의 n_mob==1이면 make_potential_mob_revise로 자기 영향을 제거하고 weight_mob를 곱해 더한다. | 군중 포텐셜 주석(27)의 n_mob==1이면 make_potential_mob_revise를 호출하고 weight_mob를 곱해 더한다. 자기 영향 제거의 근거는 `make_potential_mob_revise.f90:3,25–44`의 주석과 보정식이다. | pot_total.f90:27–31; make_potential_mob_revise.f90:3,25–44 | 보완 |
| read_agent.f90.md:70–126 | 시작 시 1행 read_agent 루틴·53행 입력 반복문 안. | 시작 시 53행 `do` 안이며 이 반복문은 114행 `enddo`에서 닫힌다. 54행 `end=10`의 대상은 116행 `10 continue`다. 인덱스 제한의 IF/ELSEIF 사슬(97–101·103–107)에는 ELSE가 없다. 각 인덱스가 범위 안이면 96·102행에서 계산한 값이 유지된다. | read_agent.f90:53–54,96–107,114–116 | 보완 |
| read_cadmas.f90.md:61–97 | 시작 시 33행 iflag==0 분기 안. | 시작 시 `if(iflag==0) then`(33) 안이다. 이 조건문은 188·267행 ELSEIF를 거쳐 269행에서 닫힌다. | read_cadmas.f90:33,188,267–269 | 보완 |
| read_cadmas.f90.md:154–184 | 시작 시 33행 iflag==0 분기 안. | 시작 시 `if(iflag==0) then`(33) 안이다. 이 조건문은 188·267행 ELSEIF를 거쳐 269행에서 닫힌다. | read_cadmas.f90:33,188,267–269 | 보완 |
| read_cadmas.f90.md:98–153 | 시작 시 33행 iflag==0 분기·61행 조건 안. | 시작 시 `if(iflag==0) then`(33)과 `if( region(1)%cadmas_rank>=0 ) then`(61) 안이다. 61행 조건문은 99행 `else`를 거쳐 151행에서 닫힌다. 33행 조건문은 269행에서 닫힌다. | read_cadmas.f90:33,61,99,151,269 | 보완 |
| read_cadmas.f90.md:214–252 | 시작 시 188행 iflag==1 분기·190행 m 루프·191행 do while·193행 rank 조건 안. | 바깥 분기는 `if(iflag==0) then`(33)의 `elseif(iflag==1) then`(188)이며 조건문은 269행에서 닫힌다. `do m=1,n_cadmas`(190)는 261행에서 닫힌다. `do while(time>=region(m)%cadmas_tnext)`(191)는 260행에서 닫힌다. 시작 시 `if(region(m)%cadmas_rank>=0) then`(193) 안이며 214행 `else`를 거쳐 251행에서 닫힌다. | read_cadmas.f90:33,188–193,214,251,260–269 | 보완 |
| read_cadmas.f90.md:253–278 | 시작 시 188행 iflag==1 분기·190행 m 루프·191행 do while 안이며 rank 조건 밖. | 시작 시 `if(iflag==0) then`(33)의 `elseif(iflag==1) then` 분기(188) 안이다. `do m=1,n_cadmas`(190)는 261행에서 닫힌다. `do while(time>=region(m)%cadmas_tnext)`(191)는 260행에서 닫힌다. 193행 rank 조건문은 251행에서 이미 닫혔다. 바깥 iflag 분기 사슬에는 ELSE가 없으며 269행에서 닫힌다. | read_cadmas.f90:33,188–193,251,260–269 | 보완 |
| read_cadmas.f90.md:253–278 | open 실패 99는 -99·errmsg를 출력한다. | open 실패 대상은 273행 `99 continue`다. 이 처리부는 `ierr=-99`를 대입하고 `call errmsg(rout,ierr)`를 호출한다. 이어 오류 문구를 쓰고 반환한다(274–277). | read_cadmas.f90:273–277 | 정정 |
| read_cadmas.f90.md:note | - 41–42: n_cadmas는 isize-1>0일 때만 통신 크기에서 갱신한 뒤 allocate_cadmas_0으로 전달된다. | - 41–42: `if( isize-1>0 ) n_cadmas=isize-1` 다음에 `call allocate_cadmas_0(ierr)`를 호출한다. 이 호출의 명시적 인수는 ierr뿐이다. allocate_cadmas_0은 모듈의 n_cadmas를 참조한다(`m_cadmas.f90:54–59`). | read_cadmas.f90:41–42; m_cadmas.f90:54–59 | 정정 |
| recursive_search_shelter.f90.md:30–81 | 시작 시 1행 recursive_search_shelter 루틴 안. | 시작 시 1행 recursive_search_shelter 루틴 안. 주석은 더 짧은 경로를 설명하지만 실제 `pot_shelter(inext,jnext)<=dnext` 비교는 같은 값도 포함한다(45–47,71–73). | recursive_search_shelter.f90:45–47,71–73 | 보완 |
| recursive_search_shelter.f90.md:82–132 | 시작 시 1행 recursive_search_shelter 루틴 안. | 시작 시 1행 recursive_search_shelter 루틴 안. 주석은 더 짧은 경로를 설명하지만 실제 `pot_shelter(inext,jnext)<=dnext` 비교는 같은 값도 포함한다(97–99,122–124). | recursive_search_shelter.f90:97–99,122–124 | 보완 |
| recursive_search_shelter.f90.md:133–182 | 시작 시 1행 recursive_search_shelter 루틴 안. | 시작 시 1행 recursive_search_shelter 루틴 안. 주석은 더 짧은 경로를 설명하지만 실제 `pot_shelter(inext,jnext)<=dnext` 비교는 같은 값도 포함한다(147–149,172–174). | recursive_search_shelter.f90:147–149,172–174 | 보완 |
| recursive_search_shelter.f90.md:183–232 | 시작 시 1행 recursive_search_shelter 루틴 안. | 시작 시 1행 recursive_search_shelter 루틴 안. 주석은 더 짧은 경로를 설명하지만 실제 `pot_shelter(inext,jnext)<=dnext` 비교는 같은 값도 포함한다(197–199,222–224). | recursive_search_shelter.f90:197–199,222–224 | 보완 |
| remesh.f90.md:31–74 | iflag==0에서는 재격자화용 변수를 미리 계산한다는 주석(49)대로 셀 중심 xp/yp를 구한다. x 격자 0..icmax에서 끝점·중심 좌표를 구성하고 xp가 포함된 구간의 ii와 coef1을 구한다. | iflag==0에서는 재격자화용 변수를 미리 계산한다는 주석(49) 아래 `yp=dxy*(dble(jp)-0.5d0)`와 `xp=dxy*(dble(ip)-0.5d0)`를 계산한다(52–53). 해석: 이 두 좌표를 목적 셀 중심으로 볼 수 있다. `do i=0,region(m)%icmax`(56)에서 x1·x2를 끝점의 xc 또는 인접 xc 두 값의 평균으로 설정한다(57–66). `if(x1<=xp.and.xp<=x2) then`이면 `ii=i`와 `coef1=(xp-x1)/(x2-x1)`을 설정하고 루프를 벗어난다(68–72). | remesh.f90:48–73 | 정정 |
| remesh.f90.md:75–128 | 시작 시 48행 iflag==0 분기·50행 jp 루프·51행 ip 루프 안. | 시작 시 `if(iflag==-1) then`(34)의 `elseif(iflag==0) then` 분기(48) 안이다. 이 조건문은 235행에서 닫힌다. 바깥 `do jp=1,jpmax`(50)는 127행에서 닫힌다. `do ip=1,ipmax`(51)는 126행에서 닫힌다. | remesh.f90:34,48,50–51,126–127,235 | 보완 |
| remesh.f90.md:129–178 | 시작 시 48행 iflag==0 분기 안. | 시작 시 `if(iflag==-1) then`(34)의 `elseif(iflag==0) then` 분기(48) 안이다. 145행은 같은 사슬의 `elseif(iflag==1) then`이다. 이 조건문은 235행에서 닫힌다. | remesh.f90:34,48,145,235 | 보완 |
| remesh.f90.md:179–201 | 시작 시 1행 remesh 루틴 안. | 시작 시 `if(iflag==-1) then`(34)의 `elseif(iflag==1) then` 분기(145) 안이다. 182행은 같은 사슬의 `elseif(iflag==2) then`이다. 이 조건문은 235행에서 닫힌다. | remesh.f90:34,145,182,235 | 보완 |
| remesh.f90.md:202–238 | 시작 시 1행 루틴, 34행 조건문의 182행 분기 안. | 시작 시 `if(iflag==-1) then`(34)의 `elseif(iflag==2) then` 분기(182) 안이다. 205행 `elseif(iflag==3) then` 뒤 ELSE 없이 235행 `endif`에서 닫힌다. | remesh.f90:34,182,205,235 | 보완 |
| underwater_function.f90.md:76–96 | 시작 시 1행 루틴·40행에서 열린 수심 등급 조건 체인 안. | 시작 시 `if(depth_rank <0.2)then`(40)의 `elseif(depth_rank <0.6)then` 분기(66) 안이다. 76·84행 ELSEIF와 90행 ELSE를 거쳐 92행 `endif`에서 닫힌다. | underwater_function.f90:40,66,76–92 | 보완 |
| update_attribute.f90.md:26–53 | 피난소 셀 주석(30)의 좌표 일치에서 수직 피난 주석(33)의 높이 미달이면 최대 수심과 에이전트 z의 차가 deadline을 넘을 때 사망(36), 속도 0·통계 갱신(39–40) 후 10으로 간다. | 피난소 셀 주석(30)의 좌표 일치에서 `if(agent_z(n)<shelter_height(m)) then`(34)이 참이면 35행의 최대 수심과 z 차이 조건을 검사한다. `if(max_depth(i_agent(n),j_agent(n))-agent_z(n)>deadline(n)) then`(35)이 참이면 사망 상태·속도 0·통계를 설정한다(36–40). 34행 조건이 참이면 35행 조건의 결과와 관계없이 `goto 10`(42)을 실행한다. 이 대상은 96행 `10 continue`다. | update_attribute.f90:31–42,96 | 정정 |
| update_attribute.f90.md:54–82 | 시작 시 1행 루틴·26행 n 루프·28행 이동 상태 분기 안이며 피난소 루프 밖. | 시작 시 `do n=1,n_agent`(26)와 `if(agent_status(n)==1 .or. agent_status(n)==2)then`(28) 안이다. 피난소 루프는 53행에서 닫혔다. 28행 조건문은 95행에서 닫힌다. 26행 반복문은 97행에서 닫힌다. | update_attribute.f90:26,28,53,95–97 | 보완 |
| update_attribute.f90.md:83–110 | 시작 시 1행 루틴·26행 n 루프·28행 상태 조건 체인 안. | 시작 시 `do n=1,n_agent`(26)와 `if(agent_status(n)==1 .or. agent_status(n)==2)then`(28) 안이다. 83행 `elseif(agent_status(n)==0)then`과 89행 `elseif(agent_status(n)==5)then`은 같은 분기 사슬이다. ELSE 없이 95행에서 닫힌다. 반복문은 97행에서 닫힌다. | update_attribute.f90:26,28,83–97 | 보완 |
| read_cadmas.f90.md:185–213 | 시작 시 1행 read_cadmas 루틴 안. | 시작 시 `if(iflag==0) then`(33) 안이다. 188행 `elseif(iflag==1) then`은 같은 분기 사슬이다. 이 조건문은 269행에서 닫힌다. | read_cadmas.f90:33,188,269 | 보완 |

정정 13, 보완 44, 이상 없음 119
