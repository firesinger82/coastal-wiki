---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_advection_diffusion.f90
lines: 97
sha256: 3d637776e478c70d24a57e72e454be03344130f7e29c78ff051a4eb1a1519e58
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_advection_diffusion.f90 — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 모듈·contains(1–3), `compute_tracer_fluxes(dt, min_dt, tloop)` 입구(5). 서브그리드 u/v점 flux 계산 주석(7), sfincs_data 사용·implicit none(9–11). 시계 계수·tloop·real*4 dt·격자 및 tracer 인덱스 선언(13–27). `call system_clock(count0, count_rate, count_max)` (29), flux 갱신 주석·구분 주석·빈 줄(2–4·6–10·12·18·20·28·30–32 포함). |
| 33–66 | 시작 시 5행 compute_tracer_fluxes 안. OpenMP private 목록과 dynamic,256 스케줄(33–35), OpenACC present 목록과 independent 루프(36–37). `do ip = 1, npuv` (38), `if (kcuv(ip) == 1) then` (40) 안에서 nm/nmu를 uv_index_z_nm/nmu로 받는다(44–45). `do itracer = 1, ntracer` (47), `if (q(ip) > 0.0) then` (49)이면 `trflux(itracer, ip) = q(ip) * trconc(itracer, nm) + (trconc(itracer, nm) - trconc(itracer, nmu)) * dico` (51). `else` (53)는 `trflux(itracer, ip) = q(ip) * trconc(itracer, nmu) + (trconc(itracer, nm) - trconc(itracer, nmu)) * dico` (55). q 조건·tracer 루프·kcuv 조건·ip 루프 종료(57–62), 병렬 지시문 종료와 주석(63–66). |
| 67–91 | 시작 시 5행 compute_tracer_fluxes 안이며 앞 루프 밖. `if (ncuv > 0) then` (67). 결합 uv점 평균을 연속식과 netCDF 출력에 쓴다는 주석(69–70). OpenMP/OpenACC 지시문(72–76), `do icuv = 1, ncuv` (77), `do itracer = 1, ntracer` (78)에서 원문 대입 `trflux(itracer, cuv_index_uv(icuv))  = (itracer, trflux(cuv_index_uv1(icuv)) + trflux(itracer, cuv_index_uv2(icuv))) / 2` (82). 두 루프·병렬 지시문·조건 종료 및 구분 주석(84–91). |
| 92–97 | 시작 시 5행 compute_tracer_fluxes 안이며 앞 ncuv 조건 밖. `call system_clock(count1, count_rate, count_max)` (92), `tloop = tloop + 1.0*(count1 - count0)/count_rate` (93). 구분 주석·루틴 종료·모듈 종료(94–97). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·11–27·29–93: 인수 목록에 min_dt가 있지만 이 루틴의 지역 형식 선언과 실행문에는 min_dt가 없다. dt에는 형식 선언이 있으나 실행문 참조가 없다. sfincs_data 내부는 이 파일 판독의 근거로 사용하지 않았다.
- 40–61: kcuv=1 참 분기만 trflux에 값을 대입한다. kcuv 조건에는 else가 없다.
- 51·55: tracer 차이에 dico를 곱한 항을 q와 농도의 곱에 더한다. 이 두 대입식에는 dt나 격자 간격 변수가 없다.
- 82: 우변은 괄호 안의 itracer와 쉼표로 시작한다. 첫 trflux 참조는 cuv_index_uv1(icuv) 하나만 인수로 적고, 두 번째 trflux 참조는 itracer와 cuv_index_uv2(icuv)를 적는다. 이 기록은 원문 표현을 수정하지 않았다.
