---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_timestep_analysis.f90
lines: 247
sha256: 4abb49df1ba2edfd962df29dd1e30117a9d7bd8375974b83e16edbcbfdf03974
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_timestep_analysis.f90 — 판독 구간 기록

구간은 1행부터 247행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | sfincs_timestep_analysis 모듈은 sfincs_data·sfincs_log를 사용하고 implicit none을 적용한다(1–8). `initialize_timestep_analysis`는 npuv 크기의 평균 요구 시간간격 누적값·현재 요구 시간간격·제한 횟수·습윤 횟수 배열을 할당한다(10–15). 누적값·횟수를 0으로 초기화한다(17·19–20). 요구 시간간격 초기식은 `timestep_analysis_required_timestep = dtmax` (18)이다. 루틴 종료·빈 줄·구분 주석을 포함한다(22–25). |
| 26–76 | `timestep_analysis_update(min_dt)`는 real*4 min_dt를 입력으로 받는다(26–33). 주석은 compute_fluxes 직후 통계를 갱신하고 건조점의 dtmax를 건너뛴다고 적는다(28–30). OpenMP private ip 및 OpenACC present·gang vector 지시문을 둔다(35–39). ip=1..npuv 루프의 `if (kcuv(ip) == 1 .or. kcuv(ip) == 6) then` (43) 안에서 `if (kfuv(ip) == 1) then` (47)을 검사한다. 두 조건 안의 누적식은 `timestep_analysis_average_required_timestep(ip) = timestep_analysis_average_required_timestep(ip) + timestep_analysis_required_timestep(ip)` (51), `timestep_analysis_times_wet(ip) = timestep_analysis_times_wet(ip) + 1` (55)이다. 그 안 `if (timestep_analysis_required_timestep(ip) <= min_dt + 1.0e-6) then` (59)이면 `timestep_analysis_times_limiting(ip) = timestep_analysis_times_limiting(ip) + 1` (61)을 실행한다. 조건·루프·병렬 영역·루틴 종료와 빈 줄을 포함한다(63–76). |
| 77–103 | `timestep_analysis_finalize(nt)`는 종료 시 셀별 평균 시간간격과 제한 횟수를 계산한다는 주석을 둔다(77–79). sfincs_data 사용, integer nt 입력, dtm·여덟 이웃 인덱스·tmsl·maximum_times_limiting을 선언한다(81–88). np 크기 셀별 평균 요구 시간간격·제한 백분율 배열을 할당하고 0으로 초기화한다(92–96). 세 OpenACC update host 지시문은 누적 시간간격·습윤 횟수·제한 횟수를 CPU로 복사한다(98–102). |
| 104–121 | 시작 시 77행 timestep_analysis_finalize 루틴 안. nm=1..np 루프의 `if (kcs(nm) > 0) then` (106) 안에서 md1·md2·mu1·mu2·nd1·nd2·nu1·nu2의 속도점 인덱스를 가져온다(110–117). 주석은 4개 또는 최대 8개의 이웃 U/V점 평균 요구 시간간격을 설명한다(108). `dtm = 1.0e6` (119), tmsl=0(120)으로 탐색을 시작한다. |
| 122–149 | 시작 시 77행 timestep_analysis_finalize 루틴·104행 nm 루프·106행 kcs 참 분기 안. `if (nmd1 > 0) then` (122)·`if (kcuv(nmd1) == 1 .or. kcuv(nmd1) == 6) then` (123)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(nmd1) / max(timestep_analysis_times_wet(nmd1), 1))` (124), `tmsl = max(tmsl, timestep_analysis_times_limiting(nmd1))` (125)이다. 독립 `if (nmd2 > 0) then` (129)·`if (kcuv(nmd2) == 1 .or. kcuv(nmd2) == 6) then` (130)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(nmd2) / max(timestep_analysis_times_wet(nmd2), 1))` (131), `tmsl = max(tmsl, timestep_analysis_times_limiting(nmd2))` (132)이다. 독립 `if (nmu1 > 0) then` (136)·`if (kcuv(nmu1) == 1 .or. kcuv(nmu1) == 6) then` (137)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(nmu1) / max(timestep_analysis_times_wet(nmu1), 1))` (138), `tmsl = max(tmsl, timestep_analysis_times_limiting(nmu1))` (139)이다. 독립 `if (nmu2 > 0) then` (143)·`if (kcuv(nmu2) == 1 .or. kcuv(nmu2) == 6) then` (144)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(nmu2) / max(timestep_analysis_times_wet(nmu2), 1))` (145), `tmsl = max(tmsl, timestep_analysis_times_limiting(nmu2))` (146)이다. 각 분기 종료·구분 주석을 포함한다. |
| 150–177 | 시작 시 77행 timestep_analysis_finalize 루틴·104행 nm 루프·106행 kcs 참 분기 안. `if (ndm1 > 0) then` (150)·`if (kcuv(ndm1) == 1 .or. kcuv(ndm1) == 6) then` (151)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(ndm1) / max(timestep_analysis_times_wet(ndm1), 1))` (152), `tmsl = max(tmsl, timestep_analysis_times_limiting(ndm1))` (153)이다. 독립 `if (ndm2 > 0) then` (157)·`if (kcuv(ndm2) == 1 .or. kcuv(ndm2) == 6) then` (158)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(ndm2) / max(timestep_analysis_times_wet(ndm2), 1))` (159), `tmsl = max(tmsl, timestep_analysis_times_limiting(ndm2))` (160)이다. 독립 `if (num1 > 0) then` (164)·`if (kcuv(num1) == 1 .or. kcuv(num1) == 6) then` (165)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(num1) / max(timestep_analysis_times_wet(num1), 1))` (166), `tmsl = max(tmsl, timestep_analysis_times_limiting(num1))` (167)이다. 독립 `if (num2 > 0) then` (171)·`if (kcuv(num2) == 1 .or. kcuv(num2) == 6) then` (172)이면 `dtm = min(dtm, timestep_analysis_average_required_timestep(num2) / max(timestep_analysis_times_wet(num2), 1))` (173), `tmsl = max(tmsl, timestep_analysis_times_limiting(num2))` (174)이다. 각 분기 종료·구분 주석을 포함한다. |
| 178–200 | 시작 시 77행 timestep_analysis_finalize 루틴·104행 nm 루프·106행 kcs 참 분기 안. `if (dtm < 1.0e5) then` (178)이면 `timestep_analysis_average_required_timestep_per_cell(nm) = min(dtm * alfa, dtmax)` (182)이다. `else` (184)는 `timestep_analysis_average_required_timestep_per_cell(nm) = -1.0` (188)이다. 주석은 이 값을 습윤 이웃이 없거나 유효하지 않은 셀의 표시로 설명한다(186). 이 조건 밖에서 `timestep_analysis_percentage_limiting_per_cell(nm) = 100.0 * tmsl / nt` (192)를 계산한다. kcs 조건·nm 루프·루틴 종료와 빈 줄을 포함한다(194–200). |
| 201–223 | `timestep_analysis_write_log`는 인덱스·좌표·제한 백분율·최대 제한 및 습윤 횟수를 선언한다(201–204). `if (maxval(timestep_analysis_times_limiting) > 0.0) then` (206)이면 `ip = maxloc(timestep_analysis_times_limiting, dim=1)` (208), `max_times_limiting = maxval(timestep_analysis_times_limiting)` (210), `max_times_wet = maxval(timestep_analysis_times_wet)` (212), `percentage_limiting = max_times_limiting / max_times_wet * 100.0 ! percentage limiting` (214)이다. `else` (216)는 dtmax만 제한한다는 주석과 ip=0 대입을 둔다(218–220). 분기 종료·주석을 포함한다(222–223). |
| 224–247 | 시작 시 201행 timestep_analysis_write_log 루틴 안이며 206행 제한 횟수 분기 밖. ip를 사용하여 양쪽 수위점 nm·nmu를 가져온다(224–225). `xuv = 0.5 * (z_xz(nm) + z_xz(nmu))` (229), `yuv = 0.5 * (z_yz(nm) + z_yz(nmu))` (230)로 유량 연결점 좌표를 계산한다. write_log와 logstr 출력을 사용하여 제한점 인덱스·백분율·좌표를 기록한다(232–243). 루틴·모듈 종료와 구분 주석을 포함한다(245–247). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–30·43–61: update의 주석은 요구 시간간격이 dtmax인 건조점을 건너뛴다고 적는다. 실제 갱신 조건은 kcuv가 1 또는 6이고 kfuv가 1인 경우이다. 요구 시간간격이 dtmax보다 작은지 검사하는 조건은 이 루틴에 없다.
- 17·19·122–176·178–188: finalize는 이웃의 습윤 횟수가 0인지 제외하는 조건을 두지 않는다. 누적값과 습윤 횟수가 모두 0이면 평균식은 0/max(0,1)을 사용한다. dtm<1.0e5 분기는 이 0을 포함한다.
- 85·192: 셀별 제한 백분율 식은 nt로 나눈다. finalize에는 nt>0을 검사하는 조건이 없다.
- 204·216–236: 로그 루틴의 else는 ip=0만 설정한다. 분기 밖에서 uv_index_z_nm(ip)·uv_index_z_nmu(ip)를 읽는다. percentage_limiting은 참 분기에서만 대입하지만 로그 출력은 조건 밖에 있다. 배열의 하한과 다른 파일의 호출 조건은 이 판독 범위에서 확인하지 않았다.
- 208–214: 로그의 제한점 인덱스는 제한 횟수의 maxloc이다. 백분율 분모는 그 ip의 습윤 횟수가 아니라 전체 습윤 횟수 배열의 maxval이다.
- 88: maximum_times_limiting은 선언 이후 이 파일의 실행문에서 사용되지 않는다.
