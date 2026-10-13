---
file: models/ROMS/raw/manuals/wiki/wikitext/LtracerSrc.wiki
lines: 12
sha256: bd1a84138d9b4f82ae304c5347710f7cee7a291bfcc6864c259627fd101083fa
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# LtracerSrc.wiki — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | LtracerSrc — 제목, Variables의 절 포함 지시문(section transclusion), 구분선과 빈 줄을 포함한다(1–5). 포함 지시문 자체를 원문대로 옮긴다(2). 원문: `{{#lst:Variables\|LtracerSrc}}` (2). |
| 6–11 | 하천 유출(river runoff) 추적자(tracer) 스위치 — 점 공급원(point source)으로 유출을 추가할 때 보통 활성화한다고 적는다(6). 모든 하천에 최소 수온과 염분을 지정해야 하고 다른 추적자는 선택사항이라고 적는다(6). 이 논리 스위치(logical switch)가 river_flag의 보유·읽기를 대체하여 제거한다고 설명한다(8). 기존 NetCDF 선언, 옵션별 의미와 무차원 단위 및 하위 호환(backward compatibility) 설명을 그대로 옮긴다(8–10). 원문: `Recall that switches are usually activated to add river runoff as a point source. At minimum, it is necessary to specify both temperature and salinity for all rivers.  The other tracers are optional.` (6); `This logical switch '''replaces''' and '''eliminates''' the need to have or read the variable <span class="forestGreen">river_flag(river)</span> from the input rivers forcing NetCDF file:<div class="box">  double river_flag(river)<br />          river_flag:long_name = "river runoff tracer flag"<br />          river_flag:option_0 = "all tracers are off"<br />          river_flag:option_1 = "only temperature"<br />          river_flag:option_2 = "only salinity"<br />          river_flag:option_3 = "both temperature and salinity"<br />          river_flag:units = "nondimensional"</div>` (8); `The above variable was too cumbersome and complicated when additional tracers are considered. However, this change is backward compatible.` (10). |
| 12–12 | 추적자 읽기와 하천별 값 — LtracerSrc는 SSFNAME 입력 하천 강제력(forcing) NetCDF에서 해당 추적자를 읽도록 활성화한다(12). 수온·염분 외 추적자를 특정 하천의 공급원으로 쓰려면 그 하천에 값을 주고, 해당 강제력이 불필요한 다른 하천에는 ZERO를 지정한다(12). 0인 경우도 모든 하천에 추적자 값을 지정해야 한다는 의무를 원문대로 옮긴다. 원문: `The [[Variables#LtracerSrc\|LtracerSrc]] switch will be used to activate the reading of respective tracer variables from the input river forcing NetCDF file ([[Variables#SSFNAME\|SSFNAME]]). If you want to add other tracer variables (other than temperature and salinity) as a source for a particular river(s), you just need to specify such values on those river(s). Then, set the values to ZERO on the other river(s) that do NOT require such river forcing for that tracer. Remember that you need to specify the tracer values for all rivers, even if their values are zero.` (12). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 2행: LtracerSrc의 Variables 절을 불러오는 `{{#lst:Variables|LtracerSrc}}`가 있으며, 불러올 정의 본문은 이 파일에 포함되어 있지 않다.
