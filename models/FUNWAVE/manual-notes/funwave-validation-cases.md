---
title: "FUNWAVE-TVD 검증 케이스 카탈로그 (benchmarks/ + simple_cases/ 검증 plot)"
model: FUNWAVE
doc: "FUNWAVE-TVD 소스트리 benchmarks/·simple_cases/ 1페이지 검증 plot PDF (raw/source_code/FUNWAVE-TVD/), funwave_tvd_2.1_manual.pdf §5"
canonical_source: manual
citation_status: verified
verification_method: "raw/source_code/FUNWAVE-TVD 트리 35개 PDF를 find/ls 로 전수 열거 후, 대표 검증 plot 17개를 pdftotext 로 직접 추출해 plot 제목·축 라벨·범례(FUNWAVE/ANALYTICAL/EXPERIMENT/Measured data, NRMSD 값) 인용. 케이스 식별은 (a) plotter .m 파일명(BM5_A_Plotter.m, BM7_loader.m)과 (b) funwave_tvd_2.1_manual.pdf line-grep(§5.1~5.6 목차·본문 line 2813/3918/4083 등 Briggs·Synolakis·Berkhoff·Mase&Kirby 출처)로 교차확인. simple_cases morpho/rip 디렉토리는 ls 로 vessel*/ 입력 존재 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/FUNWAVE/README.md
---

# FUNWAVE-TVD 검증 케이스 카탈로그 (benchmarks/ + simple_cases/ 검증 plot)

> FUNWAVE-TVD 소스트리에 동봉된 35개 1페이지 PDF(`*.pdf`)는 대부분 **검증 plot**(모델 결과 vs 해석해/실험)이다. 본 노트는 이를 `find`/`ls`로 전수 열거하고, 대표 plot의 제목·범례를 `pdftotext`로 직접 추출해 **각 케이스가 무엇을 검증하는지(해석해 비교 / 실험실 비교 / 자기수렴)** 분류한 카탈로그다. `_v20` 접미사 = FUNWAVE-TVD **v2.0** 결과 재생산본(동일 케이스에 접미사 없는 구버전 plot 병존). 1페이지 PDF는 그림이라 추출 텍스트가 적을 수 있어, 파일명·plotter 스크립트·메뉴얼 §5 교차로 보강했다.

전체 PDF 위치 루트: `raw/source_code/FUNWAVE-TVD/{benchmarks,simple_cases,doc}/` (gitignore 로컬). 아래 경로는 이 루트 기준 상대.

## 1. 분류 요약

| 분류 | 비교 대상 | 케이스 |
|---|---|---|
| **해석해(analytical) 검증** | Carrier-Greenspan / Synolakis 해석 runup | `sph_sol_plane_ana`, `sph_conical_island`(부분) |
| **실험실(laboratory) 검증** | 수리모형 계측치 | `sph_comp_beach`(BM5), `sph_monai_valley`(BM7), `sph_sol_plane_mea`, `car_conical_island`/`sph_conical_island`(Briggs), `car_mase_kirby`, `car_berkhoff_2d`, `car_osu_runup` |
| **수치 자기검증** | 격자수렴(self-convergence) / nesting 일관성 | `sph_sol_plane_statis`(convergence), `sph_nesting` |
| **응용 데모(정식 검증 아님)** | 정답해 없음(시연용) | `single/multi_vessel_morphology`, `rip_tracking` |

## 2. 케이스별 카탈로그

### 2.1 solitary wave on a simple beach — 해석해 (`sph_sol_plane_ana/`)

해석적 평면사면(plane beach) solitary wave runup. plotter 산출 plot 2종:

| PDF | 추출된 제목/범례 | 검증 내용 |
|---|---|---|
| `sph_sol_ana_prof_v20.pdf` | `"-Analytical- Solitary Wave on a Simple Beach CASE H = 0.0185"`, 범례 `SLOPE / FUNWAVE / ANALYTICAL`, 시각 `t=35…55` 스냅샷 | 표면 프로파일 시계열(공간 형상) vs **해석해** |
| `sph_sol_ana_time_v20.pdf` | `"-Analytical- Runup on a Simple Beach"`, `x/h=9.95`·`x/h=0.25` 게이지, `FUNWAVE - NRMSD=2% - ERR Max Runup Amp =1%` | 게이지 시계열 + **정량 오차지표**(NRMSD, 최대runup진폭 오차) vs 해석해 |

→ 무차원 진폭 `c/h`, 무차원 시간 `t(g/h)^{1/2}` 축. 비접미사 구버전 `sph_sol_ana_prof.pdf`/`sph_sol_ana_time.pdf` 병존.

### 2.2 solitary wave on a simple beach — 실험치 (`sph_sol_plane_mea/postprocessing/`)

동일 평면사면 케이스를 **실험 계측치**(Synolakis 계열 lab)와 비교. 두 입사진폭:

| PDF | 추출된 제목/범례 | 비고 |
|---|---|---|
| `sph_sol_mea_prof1_v20.pdf` | `"Solitary Wave on a Simple Beach CASE H = 0.0185"`, 범례 `SLOPE / FUNWAVE / EXPERIMENT`, `t=30 FUNWAVE - NRMSD=10% - ERR Max Wave Amp =3%` … `t=50 NRMSD=4%` | 비쇄파(소진폭) 케이스 |
| `sph_sol_mea_prof2_v20.pdf` | `"Solitary Wave on a Simple Beach CASE H = 0.30"`, `t=15 NRMSD=5% ERR=4%`, `t=20 NRMSD=6% ERR=15%` | 쇄파(대진폭) 케이스 |

§2.1(해석해)과 §2.2(실험)는 같은 simple-beach 물리, **검증 기준만 다름**.

### 2.3 격자수렴 (`sph_sol_plane_statis/`)

| PDF | 추출된 축 | 검증 내용 |
|---|---|---|
| `convergence_v20.pdf` | y축 `Difference in setup (m)`(log, ~10^{-1.2}…10^{-1.9}), x축 `dx (m)`(log) | 격자 간격 `dx`에 대한 setup 차이의 **자기수렴(self-convergence)** — 해석해/실험이 아닌 수치 수렴성 검증 |

### 2.4 composite beach — BM5 실험 (`sph_comp_beach/`)

NTHMP/Catalina 벤치마크 **BM5**(plotter `BM5_A_Plotter.m`, `BM5_tmp_Plotter.m` 확인). composite(다단) beach 위 입사파의 wall 게이지 시계열. 입사파고/수심비 `H/d` 별 3 케이스:

| PDF | 추출된 제목 |
|---|---|
| `case_A/comp_beach_A_v20.pdf` | `"Case B (H/d=0.0.0378)"` *(plot 제목 오타 그대로; A 디렉토리)* |
| `case_B/comp_beach_B_v20.pdf` | `"Case B (H/d=0.2578)"` |
| `case_C/comp_beach_C_v20.pdf` | `"Case C (H/d=0.6404)"` |

축: `cm`(표면변위) vs `sec`(~268–296s 윈도). 각 케이스 비접미사 구버전 plot 병존. ⚠ case_A plot 제목이 "Case B"로 표기됨(원 PDF 오타) — 디렉토리/파일명 기준 A로 분류.

### 2.5 Monai Valley / Okushiri — BM7 실험 (`sph_monai_valley/`)

NTHMP/Catalina 벤치마크 **BM7**(loader `BM7_loader.m` 확인) — Okushiri섬 Monai Valley 수리모형 tsunami runup.

| PDF | 추출된 제목/범례 |
|---|---|
| `postprocessing/monai_comp_v20.pdf` | `Gauge 5 / 7 / 9` 시계열, 범례 `Measured data` / `Numerical Simulation`, 축 `cm` vs `Time(sec)`(0–20s) |
| `fft/boundary.pdf` | (텍스트 미추출 — 입력 경계조건 시계열 그림으로 추정) |

비접미사 구버전 `monai_comp.pdf` 병존.

### 2.6 conical island — Briggs 실험 (`car_conical_island/`, `sph_conical_island/`)

Briggs et al. (1994/1995) 원추형 섬 solitary wave runup 실험. 메뉴얼 §5.4 본문: *"Laboratory experiments on the interaction between solitary waves and a conical island were conducted by Briggs et al (1995)… benchmark test is specified in Section 3.3 of Appendix A of Synolakis et al (2007)"* (funwave_tvd_2.1_manual.pdf line 2813–2817). 입사파고 3 케이스(A/B/C), Cartesian·spherical 좌표 양쪽 실행.

| 그룹 | PDF | 추출 내용 |
|---|---|---|
| Cartesian | `car_conical_island/work_case_{A,B,C}/case{A,B,C}.pdf` | `Gauge 6 / 9 / 16 / 22` 시계열, 축 `eta (m)`(±0.04) vs 시간(25–40s) |
| Spherical | `sph_conical_island/work_case_{A,B,C}/case{A,B,C}_sph.pdf`, `_sph_v20.pdf`, `_cart.pdf` | `Gauge 6 / 9 …`, 동일 `eta (m)` 축 — spherical 모드 동일 게이지 재현 |

`sph_conical_island`는 케이스당 `_cart`(직교 비교)·`_sph`·`_sph_v20` 3종 plot 보유.

### 2.7 nesting 일관성 (`sph_nesting/`)

| PDF | 추출 내용 | 검증 내용 |
|---|---|---|
| `postprocessing/solitary_nesting_v20.pdf` | `Grid A` / `Grid B`, `nesting boundary`, 시각 `t=100/200/300/400s`, x ~1000–5500 | 큰 격자(Grid A) ↔ nested 작은 격자(Grid B) 간 solitary wave **일관성**(one-way nesting 검증). 메뉴얼 §5.6 nesting case 대응 |

비접미사 `solitary_nesting.pdf` 병존.

### 2.8 메뉴얼 §5 추가 벤치마크 (plot PDF 미동봉 / 다른 형식)

메뉴얼 §5 목차에 있으나 위 1페이지 PDF로는 직접 안 잡힌 케이스(디렉토리만 존재, postprocessing 별도):

| 디렉토리 | 메뉴얼 §5 항목 | 비교 대상 |
|---|---|---|
| `car_mase_kirby/` | §5.2 Random wave shoaling/breaking on a slope | **Mase & Kirby (1992)** 실험 (manual line 102/152–156) |
| `car_berkhoff_2d/` | §5.3 Wave propagation over a shoal | **Berkhoff et al. (1982)** 초점 실험 (manual line 103/157) |
| `car_osu_runup/` | (OSU 수조 runup) | 실험 — postprocess/ 보유 |
| `car_sediment_lab_c2/` | (sediment 실험) | 실험 — gauges.txt·depth_dune_6cm.txt 보유 |
| `car_Nwave_statis/`, `sph_Nwave_statis/` | N-wave 통계 스윕 | 다수 input_s*_h*_a*.txt 파라미터 스윕(readme_results.txt) |

## 3. 응용 데모 (정식 검증 아님 — vessel wake / rip)

`simple_cases/` 하위의 아래 plot은 해석해·실험 비교가 아닌 **기능 시연**(vessel-induced wave & 형상변화·tracer 추적). 디렉토리에 `vessel*/`, `bathy_param.txt`, `mk_depth.F` 입력만 존재(정답해 없음).

| PDF | 추출 내용 | 성격 |
|---|---|---|
| `single_vessel_morphology/single_morpho.pdf` | (텍스트 미추출) | 단일 선박 wake 형상변화 데모 |
| `single_vessel_morphology/single_wave_conc.pdf` | (텍스트 미추출) | 단일 선박 파/농도(sediment conc) |
| `multi_vessel_morphology/multi_wave_morpho.pdf` | (텍스트 미추출) | 다중 선박 wake morphology |
| `multi_vessel_morphology/profile.pdf` | `Averaged Bed Change (m)` (×10^{-3}) vs `y (m)` | 평균 bed change 단면 |
| `rip_tracking/postprocessing/bathy_tracer.pdf` | `TRACER` | rip current tracer 추적 시연 |

## 4. 메모 / 미확인

- ⚠ 1페이지 PDF 다수는 그림 위주라 `pdftotext` 추출량이 0이거나 단편적(`single_morpho.pdf`, `multi_wave_morpho.pdf`, `boundary.pdf` 등) — 이들은 **파일명·plotter·디렉토리 입력 기반**으로만 분류했고 plot 내부 라벨은 미확인.
- ⚠ `comp_beach_A_v20.pdf` 제목 "Case B" 표기는 원 PDF 오타로 판단(디렉토리는 case_A). 실제 게이지/`H/d`는 plotter 미실행으로 미확인.
- `doc/` 4개 PDF(`Intro-to-FUNWAVE-CHL-TN.pdf`, `funwave_code_analysis.pdf`, `funwave_tvd_2.1_manual.pdf`, `funwave_tvd_3.0.pdf`)는 검증 plot이 아닌 **문서**라 본 카탈로그에서 제외(메뉴얼은 §5 교차확인 출처로만 사용).
- NTHMP 벤치마크 번호(BM5 composite beach, BM7 Monai)는 plotter 파일명(`BM5_*`, `BM7_loader.m`)으로 확인. 공식 BP/BM 번호 체계 전체 매핑은 ⚠ source-needed(Synolakis et al. 2007 원문 미열람).
