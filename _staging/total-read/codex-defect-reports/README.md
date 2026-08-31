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

## B tier-2 (ADCIRC 코어 확대, 2026-08-30, task-mtef53zl) — 18파일
결과: HIGH 8 · MED 4. ★단일 pass·미검증(HIGH 는 적대검증 예정).

- **HIGH·OOB** read_input.F L5141-5172;5178-5182;5213-5221 — NFEN=0 passes, and NFEN=1 is also permitted even though generated grids raise it to 2 only after NFEN-sized arrays have been allocated; IGC=0 writes S
- **HIGH·OOB** transport.F L1443-1475 — With the default cubic scheme and accepted NFEN=2 or 3, the top branch sets k1 to -1 or 0, while the bottom branch sets k4=4, before indexing Sigma an
- **HIGH·OOB** ephemerides.F90 L109-126;164-170;173-216 — For a first external-table request outside file coverage, recache_data returns IERR=2 before allocating self%times, but this routine continues into ra
- **HIGH·UBA** wind.F L860-879;957-991;2088-2108;2223-2291 — The NWS=3 branches assign wind stress and wind output but never PR2; the hot-start branch also leaves the wind-output dummies unset. Because these are
- **HIGH·UBA** owiwind.F L270-310;338-358 — NWS=-14 calls this routine to overlay OWI values only where data exist, but INTENT(OUT) makes all three actual arrays undefined before the no-data bra
- **HIGH·UBA** owiwind_netcdf.F L687-737;815-865 — When a wind or pressure corner is converted from _FillValue to NaN, the self-equality guard skips assignment of UU/VV/Wind or PP, yet these uninitiali
- **HIGH·sign/geometry** nws08.F90 L606;1201;1582-1596 — The Holland and CLE15 active-storm calls pass different swapped argument orders, but both cause the helper to store latitude in EyeLon and longitude i
- **MED·sign/geometry** nws08.F90 L650-670 — At a mesh node exactly at the storm eye, sphericalDistance returns zero, so alpha divides by zero and the velocity radical evaluates an infinity-times
- **MED·dead-guard** nws08.F90 L1494-1511 — The vector expression divides its first element by r(1)=0 and only overwrites res(1) afterward. That post-assignment cannot neutralize an IEEE divide 
- **HIGH·time-mixing** subdomain.F L398-451;513-551 — The hot-start opener never references TimeLoc after accepting it; it zeros the old field and reads the first fort.019 record instead of seeking the ho
- **MED·logic** harm.F L401-479 — Under NFOVER=1, all four invalid harmonic-output selectors are announced as reset to zero, but none is actually assigned. No later normalization occur
- **MED·sign/geometry** rs2.F L619-628;663-672 — A repeated or collinear STWAVE triangle has totalarea=0; for a collinear target the inclusion test accepts 0<=0 and immediately divides by zero to for

## B tier-2 적대검증 (2026-08-30, task a223508844) — HIGH 8/8 CONFIRM
독립 skeptic REFUTE 시도 → 전건 CONFIRM(`B2-verify.json`): read_input NFEN OOB·transport NFEN OOB·
ephemerides IERR=2 후 미정의 참조·wind NWS=3 PR2 미대입·owiwind no-data INTENT(OUT) 미정의·
owiwind_netcdf NaN-skip 미정의 read·nws08 Holland/CLE15 위경도 스왑·subdomain hotstart time-mixing.

## ADCIRC 누적 (게이트 밖, 적대검증 완료)
1차 7(HIGH 4 검증·MED 3) + tier-2 12(HIGH 8 검증·MED 4) = **19 결함(HIGH 12 전건 적대검증 CONFIRM·MED 7)**.
30파일 감사(전체 837 중). ROMS/Delft3D 미착수.

## C — ROMS 코어 1차 결함감사 (무감사 2.8M줄, 2026-08-30, task-mtfcgj94) — 16~20파일
★로그 검증: 실제 sed/nl/rg 로 step3d_uv/step3d_t/step2d/prsgrd/omega/mp_exchange 등 판독 확인, 중립화로
halo-init·HSIMT 의심 등 기각. **4건(HIGH 2·MED 2)** 생존:
- HIGH step3d_uv.F L235-1736 — Huon/Hvom INTENT(OUT) 이나 첫 대입이 set_massflux 산출 incoming 값을 읽음(INOUT 이어야). UBA.
- HIGH main3d.F L681-683 — STEP2D_FB_AB3_AM4 서 knew 가 4까지 순환하나 zeta/ubar/vbar 는 3 시간슬롯만 할당(mod_ocean L407) → OOB. checkdefs 통과.
- MED step3d_t.F L1080-1088 — 수직 Courant=1 서 KaZ=0, 무조건 1/KaZ → Inf/NaN(HSIMT 수평경로엔 가드 있음).
- MED wvelocity.F L222-227 — N=1 서 level 2 참조(수직 extent N 초과). read_phypar 는 N<0 만 거부.
- HIGH 2 적대검증 예정. ROMS 나머지·Delft3D 후속.

## C ROMS 적대검증 (2026-08-30) — HIGH 2/2 CONFIRM
독립 skeptic REFUTE 시도(ROMS 3-time-level·tile 관례 주의) → 전건 CONFIRM(`C-roms-verify.json`):
step3d_uv Huon/Hvom intent(out) read-before-write·main3d knew=4 vs 3슬롯 OOB.

## D — Delft3D 코어 1차 결함감사 (무감사 1.6M줄, 2026-08-30, task-mtfv18ed) — FLOW ADI
★로그 검증: engines_gpl/flow2d3d 엔진 소스 실제 판독. Codex sandbox read-only 로 JSON 미기록 → 로그 복구.
**6건(HIGH 4·MED 2)** (★HIGH 4 는 전부 sparse INTENT(OUT) UBA 계열 — 라인은 적대검증서 확정):
- HIGH drychk.f90 — sparse INTENT(OUT) 가 전체 qxk/qyk flux 배열 무효화.
- HIGH bccorr.f90 — sparse INTENT(OUT) 가 SUD 전 비경계 flux 무효화.
- HIGH secrhs.f90 — 다구성 sour/sink 전체 무효화, secondary-flow 항목만 복원.
- HIGH secbou.f90 — 전체 r1 농도배열 무효화, 경계 끝점만 복원.
- MED tratur.f90 — V-wall 난류가 속도엔 GVV, 길이척도엔 GUU 사용(불일치).
- MED tritra.f90 — SNELLI 가 longshore flux 0 으로 풀고 질량/morphology flux 는 원 discharge 로 재구성.
- HIGH 4 적대검증 예정.

## D Delft3D 적대검증 (2026-08-31) — HIGH 4/4 CONFIRM
독립 skeptic 이 실제 INTENT 키워드 확정 → 전건 INTENT(OUT), CONFIRM:
drychk.f90 qxk/qyk · bccorr.f90 qxk · secrhs.f90 sour/sink · secbou.f90 r1 (모두 sparse-assign UBA).

## ★대형 3모델 코어 감사 누적 (게이트 밖, 로그 real-read 검증, HIGH 전건 적대검증 CONFIRM)
| 모델 | 감사파일 | 결함 | HIGH(검증) | MED |
|---|---|---|---|---|
| ADCIRC | 30/837 | 19 | 12 ✅ | 7 |
| ROMS | ~20/3870 | 4 | 2 ✅ | 2 |
| Delft3D | ~18/7256 | 6 | 4 ✅ | 2 |
| **계** | **~68** | **29** | **18 전건 검증** | **11** |
반복 최다 클래스: INTENT(OUT) sparse-assignment UBA(ADCIRC wind/owiwind·ROMS Huon/Hvom·Delft3D 4건).
전부 base/감사 없어 supplement 게이트 밖 — 정식화엔 별도 감사채널 필요. 각 모델 잔여 대부분 미감사.

## A MED 3 상세 (2026-08-31, 상세화+중립화 검사) — 전건 CONFIRM(MED)
→ 3건 모두 default 설정선 중립화되나 지원되는 비default 경로에선 실결함(MED). FUNWAVE 3차 독립판독 신규 HIGH 0 재확인.

(A MED 3 상세 항목):
- **etauv_solver.F** L425-431 — west test owns the whole outer branch, east is an ELSEIF; if both x-coupling flags true on one domain, I=Iend stays in the west arm, fails its I=Ibeg  [중립화: gated by COUPLING compile + DISPERSION runtime, but both-sides-active case not n]
- **mod_time_spectra.F** L325-333,365-373 — single IF advances the spectrum pair by only one record even if TIME crossed several record times → interpolation weights extrapolate until later step [중립화: small timesteps / EOF-hold avoid it but neither is an enforced bracket guard; no]
- **mod_sediment.F** L1385-1400 — SEDIMENT_ADVECTION_DIFFUSION runs once per each of 3 RK stages but adds full physical DT to the averaging clock and sums each call → non-default Morph [중립화: default Morph_interval=SMALL resets every stage (neutralized); explicitly-config]

## E — EFDC+ 코어 1차 결함감사 (cal* 솔버, 2026-08-31, task-mtgpwmvp) — 19파일
★로그 검증: calexp2t/congrad 등 실제 판독. (기읽은 6 EFDC-000 IO/setup 파일 제외.) **7건(HIGH 2·MED 5)**:
- HIGH calpuv9c.f90 L693-698 — MPI+MDCHH>=1(subgrid channel) 분기서 MPI/channel 압력solver 모두 미호출 후 P를 해결된 듯 exchange·사용. 질량 비보존.
- HIGH calpuv2c.f90 L659-664 — 2TL MPI 경로도 subgrid channel 시 압력/자유표면 solve 없이 downstream flux·depth 소비.
- MED calexp2t L1128-1132(SGZ 를 미대입 L 로 인덱스)·L1201-1205(Y-source 가 X성분을 Y face 에 주입)·caltran_ad L161-166(FWUU/FWVV 하면 zero)·calavb L356-360(bottom AQ 차원 불일치)·caluvw L1139-1143(SUB vs SVB mask).
- HIGH 2 적대검증 예정. (calpuv 는 DETTMP 파일 계열 — EFDC-000 감사쌍 있으나 calpuv 자체는 미판독.)

## E EFDC 적대검증 (2026-08-31) — H0 REFUTE · H1 CONFIRM
- **calpuv2c.f90 H1 → CONFIRM**: cold-start MPI 가 restart-only 가드 우회, rank0 positive MDCHH 가 전 압력solver skip, 미해결 P 가 face-discharge/channel-flow 서 소비→HP 갱신. 실 질량비보존.
- **calpuv9c.f90 H0 → REFUTE**: rank0 는 solver skip 하나 worker rank(MDCHH=0)는 Congrad_MPI 진입, rank0 가 MPI barrier 서 block — 조용한 비보존이 아닌 다른 거동. 특정 주장 미성립(→ 잠재 MPI 데드락 별건).
→ EFDC 확정 HIGH 1(calpuv2c)·MED 5, 기각 HIGH 1. span-gate 가 false positive 1건 적발.

## C ROMS tier-2 (2026-08-31, task-mtgtxawc) — 18파일
★로그 real-read: t3dmix/my25/bvf_mix/lmd_vmix/lmd_bkpp/conv_3d/wetdry 등 실제 판독(step3d_t 인라인 tracer-adv 확인). **5건(HIGH 2·MED 3)**:
- HIGH lmd_bkpp.F L252-530 — Ustar 는 중첩 sqrt 라 음수 불가 → 안정성 가드 항상 참(dead guard).
- HIGH wetdry.F L300-315 — 양 분기가 umask_full=1 동일 대입, vmask_full 도 동일 → 복붙 mask 가드 무력.
- MED my25_corstep.F L786-791 — 동쪽 halo 를 Iend+1 대신 Iend-1 로 copy(타 방향은 정상).
- MED lmd_vmix.F L225-336 — shear 재구성 부정확(부분 중립화).
- MED conv_3d.F L327-404 — GEOPOTENTIAL_HCONV xi-flux 가 Kh(i-1,j) 를 자기자신에 더해 Kh(i,j) 무영향(face 스텐실).
- HIGH 2 적대검증 예정.

## E EFDC tier-2 (2026-08-31, task-mtgtxw31) — 18파일
★로그 real-read. **11건(HIGH 2·MED 9)** — index/방향 버그 다수:
- HIGH calebi.f90 L437-445 — 북면 LS 적분(B(LS,K)·ZZN(K,LS))을 잘못된 목적지 index L 의 BI1N/BI2N/BEN 에 저장.
- HIGH setopenbc.f90 L580-596 — 북 radiation 분기가 CST 유도·사용하나 tidal-offset 복원엔 남쪽계수 CNT 사용.
- MED: hdmt LN 미대입 stale(+OMP private 누락)·PEAKFLOW 0-나눗셈·hdmt2t LN·calstepd L stale·caltbxy NAL vs class1 하드코딩·caltsxy 풍향투영 덮어씀·setopenbc stale boundary·subchan LCHNV 계산/LCHNU 검사·wavesxy veg 무조건대입.
- HIGH 2 적대검증 예정.

## E EFDC tier-2 적대검증 (2026-08-31) — HIGH 2/2 CONFIRM
- calebi.f90 H0 CONFIRM: V블록이 "NORTH FACE INTEGRAL OF LS"(B(LS,K)·ZZN(K,LS))를 LS 아닌 L 의 BI1N/BI2N/BEN 에 저장. consumer calpuv2c.f90 L521-522 는 BI*N(LS) 소비 → 목적지 index 오류 확정.
- setopenbc.f90 H1 CONFIRM: 남/서/동 branch 는 각자 계수(CNT/CET/CWT)로 offset 복원하나, 북 branch 는 전부 CST 쓰다 L596서만 미할당 CNT 사용(그 CNT L609 할당은 excess-flow용, tidal 아님).
