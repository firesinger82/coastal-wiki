---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_wave_enhanced_roughness.f90
lines: 76
sha256: 9529e9e9eee1a44941edcfc642671db8e9e733ffa203d3382102c71e9e05ffa7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_wave_enhanced_roughness.f90 — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | sfincs_wave_enhanced_roughness 모듈·contains 뒤 `update_wave_enhanced_roughness`가 시작한다(1–5). sfincs_data 사용, implicit none, 점 인덱스와 파랑·흐름 속도·수위·수심·Manning 조도·항력 변수 선언을 포함한다(7–12). `if (.not. wave_enhanced_roughness) return` (14)이면 복귀한다. OpenMP parallel·private 목록과 `!$omp do schedule ( dynamic, 256 )` (18)을 둔다(16–18). |
| 19–45 | 시작 시 5행 update_wave_enhanced_roughness 루틴·16행 OpenMP parallel 영역 안. ip=1..npuv 루프의 `if (kcuv(ip) == 1 .or. kcuv(ip) == 6) then` (21)은 일반 속도점 또는 해안 측방 경계라는 주석을 둔다(23). 이웃 nm·nmu를 가져온다(27–28). gnapp2(ip)에 이미 g·n²로 변환된 subgrid_uv_navg_w(ip)를 복사한다(30). `Uw = 0.5 * (uorb(nm) + uorb(nmu))` (32), uu=uv(ip)(34), `vu = (uv(uv_index_v_ndm(ip)) + uv(uv_index_v_ndmu(ip)) + uv(uv_index_v_nm(ip)) + uv(uv_index_v_nmu(ip))) / 4` (35), `Uc = max(sqrt(uu*2 + vu**2) , 0.25)` (37)을 계산한다. `if (Uw < 0.1) cycle` (39)이면 건너뛴다. `zsu = max(zs(nm), zs(nmu))` (41), `hu = subgrid_uv_havg_zmax(ip) + zsu` (42)을 계산한다. `if (hu < 0.1) cycle` (44)이면 건너뛴다. |
| 46–63 | 시작 시 5행 update_wave_enhanced_roughness 루틴·16행 OpenMP parallel 영역·19행 ip 루프·21행 kcuv 참 분기 안. `n_base = sqrt(subgrid_uv_navg_w(ip) / g)` (48), `cd = g * n_base**2 / hu**(1.0 / 3.0)` (50)로 기본 Manning 조도에서 마찰계수를 구한다. Ruessink (2001)이라는 주석 아래 `cdeff = cd * sqrt((1.16 * Uw)**2 + Uc**2) / Uc` (54)를 계산한다. Grant & Madsen (1979) 또는 Soulsby (1997)라는 대체식 주석과 `! cdeff = cd * (1.4 * Uw + Uc) / Uc` (58)은 실행되지 않는다(56–58). `n_app = sqrt(cdeff * hu**(1.0/3.0) / g)` (60), `gnapp2(ip) = g * n_app**2` (62)로 파랑 효과를 적용한 조도 값을 저장한다. |
| 64–76 | 시작 시 5행 update_wave_enhanced_roughness 루틴·16행 OpenMP parallel 영역·19행 ip 루프·21행 kcuv 참 분기 안. 조건·루프·OpenMP 영역을 닫는다(64–68). 주석은 CPU에서만 계산한 gnapp2를 GPU로 갱신해야 한다고 적는다(70). `!$acc update device(gnapp2)` (72)를 실행한다. 루틴·모듈 종료와 빈 줄·구분 주석을 포함한다(74–76). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37: Uc 계산의 제곱근 안 첫 항은 uu*2이고 두 번째 항은 vu**2이다. 원문은 uu**2를 사용하지 않는다. max(...,0.25)는 sqrt 바깥에 있다.
- 30·39·44·62: gnapp2의 기본값 복사는 Uw·hu의 cycle 검사보다 앞에 있다. 두 cycle 경로는 파랑 조도 갱신식에 도달하지 않는다.
- 21·35: 교차 속도 평균은 네 uv_index_v_* 인덱스를 직접 사용한다. 이 접근 블록에는 네 인덱스의 범위를 검사하는 조건이나 kfuv 검사가 없다. 인덱스 배열의 생성·하한은 이 판독 범위에서 확인하지 않았다.
- 37·39·44·54·58: 흐름 속도 하한 0.25, 파랑 속도·수심 기준 0.1, 실행식 계수 1.16은 고정값이다. 계수 1.4를 사용하는 대체식은 주석 처리되어 있다.
