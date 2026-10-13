---
file: models/ROMS/raw/manuals/wiki/wikitext/WET_DRY.wiki
lines: 17
sha256: 7a794ff47d6a5864cdaaff2e7c30f7e480bfbc0a8f54888769c86710abba5fc4
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# WET_DRY.wiki — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | WET_DRY / 도입 — 제목, Options 페이지의 설명 가져오기 지시문, 줄 바꿈과 구분선을 포함한다(1–6). 원문: `{{#lst:Options\|WET_DRY}}` (3). |
| 7–11 | WET_DRY / 마스크 — 격자 NetCDF에 육지·해양 마스크(land/sea mask)가 필요하다고 적는다(7). mask_rho 값에 따라 영구 건조 셀과 습윤 또는 건조 셀을 구분한다(8–10). 습윤·건조 마스크 배열(wet/dry mask array)의 저장 이름을 제시한다(11). 원문: `* The Land/Sea [[MASKING\|masking]] arrays ([[Variables#mask_rho\|mask_rho]], [[Variables#mask_u\|mask_u]], [[Variables#mask_v\|mask_v]]) are required in the grid NetCDF file. Recall that the Land/Sea masking is set in some of the [[Test Cases\|test cases]] with an analytical routine by activating [[ANA_MASKING]].` (7); `** Cells with a [[Variables#mask_rho\|mask_rho]] '''= 0''' will always be '''dry'''. ` (8); `** Cells with a [[Variables#mask_rho\|mask_rho]] '''= 1''' can be '''wet''' (active) or '''dry''' (inactive) depending on the depth of water computed on that cell.` (9); `: Cells that are permanently dry (''i.e.'' cells with a [[Variables#mask_rho\|mask_rho]] '''= 0''') have a water depth equal to [[Variables#Dcrit\|Dcrit]].` (10); `* In the model, the wet/dry masks are stored in the [[Variables#rmask_wet\|rmask_wet]], [[Variables#umask_wet\|umask_wet]], and [[Variables#vmask_wet\|vmask_wet]] arrays.` (11). |
| 12–17 | WET_DRY / 초기화·플럭스·출력 — 초기 수심이 최소 수심보다 작으면 수위를 올리고 기본 최소 수심을 제시한다(12). 계산 중 수위가 임계값보다 작으면 유출 플럭스(flux)를 허용하지 않으며 유입은 항상 허용한다고 적는다(13). rho점 마스크의 시간 기록과 아래쪽이 양인 수심 부호를 설명한다(14–15). 활성 지시문을 제시한다(16–17). 원문: `* In the present formulation for wetting/drying, at initialization, the model computes for each cell the total depth of water as:<div class="box">D(i,j)=[[Variables#h\|h(i,j)]]+[[Variables#zeta\|zeta(i,j,1)]]</div> If the total depth is less than a user specified minimum depth ([[Variables#Dcrit\|Dcrit]]), then the water level is increased to<div class="box">[[Variables#zeta\|zeta(i,j,1)]] = [[Variables#Dcrit\|Dcrit]] - [[Variables#h\|h(i,j)]]</div> This ''drapes'' the water level over all the land cells. The default value for [[Variables#Dcrit\|Dcrit]] is 0.10 m.` (12); `* During computation, the water level in each cell is compared to [[Variables#Dcrit\|Dcrit]]. If the water level is less than [[Variables#Dcrit\|Dcrit]], then no flux is allowed out of that cell. Water can always flow into a cell.` (13); `* For output, a variable [[Variables#rmask_wet\|wet_dry_masking]] provides the time history of the wet/dry masking at &rho;-points.` (14); `* The bathymetry [[Variables#h\|h]] is measured positive downwards, with a typical refernce to mean sea level (MSL). Therefore value of [[Variables#h\|h]] below MSL are positive, and values of [[Variables#h\|h]] above MSL are negative. ROMS internally deals with the positive and negative values of [[Variables#h\|h]].` (15); `* To activate this feature you need to use:` (16); `:<div class="box">   #define WET_DRY</div>` (17). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12–13: 초기화의 비교 대상은 total depth of water이다. 계산 중 비교 대상은 water level이라고 적는다. 두 문장의 대상을 동일하게 바꾸지 않고 옮겼다.
