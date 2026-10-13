---
file: models/ROMS/raw/manuals/wiki/wikitext/UPWELLING_CASE.wiki
lines: 57
sha256: d11705b390368079bdaf014057cabcc504c923f50df9ac677f22c94ec99a6eaa
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# UPWELLING_CASE.wiki — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Wind-Driven Upwelling/Downwelling over a Periodic Channel Test Case — 양측 대륙붕(shelf)의 주기 수로(periodic channel)에서 수로 방향 바람과 Coriolis 항으로 한쪽은 용승(upwelling), 반대쪽은 침강(downwelling)이 생긴다고 적는다(1–3). 수직 혼합 없이 여러 날 실행하면 밀도가 큰 물이 작은 물 위에 놓인다고 설명한다(3). ROMS_APPLICATION을 UPWELLING으로 설정하는 적용 조건을 적는다(5). 원문: `The upwelling/downwelling example was contributed by Anthony Macks and Jason Middleton (Macks, 1993) and consists of a periodic channel with shelves on each side. There is along-channel wind forcing and the Coriolis term leads to upwelling on one side and downwelling on the other side. If you run it for several days without vertical mixing, you end up with dense water over light water.` (3); `If you wish to run the upwelling test case, set <span class="blue">ROMS_APPLICATION</span> to '''[[Options#UPWELLING\|UPWELLING]]''' in your [[build Script\|build script]] or [[makefile]].` (5). |
| 9–15 | Domain — 동서 주기와 동쪽에서 서쪽으로 부는 공간적으로 균일한 바람의 0.1 Pascals 값을 적는다(9–11). upwelling_domain.png의 캡션은 Upwelling Domain이다(13). 그림 파일 없음. 레이아웃 마크업을 포함한다(14). 원문: `The plot below shows the domain of the Upwelling test case. This test case is East-West periodic and has spatially uniform winds blowing from east to west at <span class="forestGreen">0.1</span> Pascals.` (11); `[[Image:upwelling_domain.png\|center\|frame\|<center>Upwelling Domain</center>]]` (13). |
| 16–31 | Results / Day 0 — csec의 남북 단면과 표면 깊이를 0으로 보이게 하는 LZEROZN=T 그림 설정을 설명한다(16–17). 표의 첫 행은 Day 0 initial conditions이며 t_his_0.png·uvel_his_0.png·vvel_his_0.png·wvel_his_0.png·omega_his_0.png를 참조한다(18–31). 캡션은 Temperature (Celsius), U/V-velocity (cm/s), W-velocity·Omega (m/day)이다. 다섯 그림 모두 그림 파일 없음. 표의 행·열 마크업·캡션·단위를 원문 그대로 옮긴다. 원문: `The results below were plotted with the [[Plotting Package Installation\|ROMS Plotting Package]] using <span class="red">csec</span> for the South-North cross-sections. For cosmetic purposes, the surface depth is set to zero (parameter '''LZEROZN=T''' in [[Internal_Plotting_Parameters\|default.cnt]]) and not the value at the middle of the surface grid cell which varies with the [[Variables#zeta\|free-surface]].` (17); `{\|width="99%"` (18); `\|style="width:20%"\|` (19); `'''Day 0'''<br>initial conditions` (20); `\|style="width:20%"\|` (21); `[[Image:t_his_0.png\|none\|thumb\|180px\|<center>Temperature (Celsius)</center>]]` (22); `\|style="width:20%"\|` (23); `[[Image:uvel_his_0.png\|none\|thumb\|180px\|<center>U-velocity (cm/s)</center>]]` (24); `\|style="width:20%"\|` (25); `[[Image:vvel_his_0.png\|none\|thumb\|180px\|<center>V-velocity (cm/s)</center>]]` (26); `\|style="width:20%"\|` (27); `[[Image:wvel_his_0.png\|none\|thumb\|180px\|<center>W-velocity (m/day)</center>]]` (28); `\|style="width:20%"\|` (29); `[[Image:omega_his_0.png\|none\|thumb\|180px\|<center>Omega (m/day)</center>]]` (30); `\|-` (31). |
| 32–44 | Results / Day 2 — instantaneous 표 행에서 t_his_2.png·uvel_his_2.png·vvel_his_2.png·wvel_his_2.png·omega_his_2.png를 참조한다(32–44). 캡션은 Temperature (Celsius), U/V-velocity (cm/s), W-velocity·Omega (m/day)이다. 다섯 그림 모두 그림 파일 없음. 표의 행·열 마크업·캡션·단위를 원문 그대로 옮긴다. 원문: `\|style="width:20%"\|` (32); `'''Day 2'''<br>instantaneous` (33); `\|style="width:20%"\|` (34); `[[Image:t_his_2.png\|none\|thumb\|180px\|<center>Temperature (Celsius)</center>]]` (35); `\|style="width:20%"\|` (36); `[[Image:uvel_his_2.png\|none\|thumb\|180px\|<center>U-velocity (cm/s)</center>]]` (37); `\|style="width:20%"\|` (38); `[[Image:vvel_his_2.png\|none\|thumb\|180px\|<center>V-velocity (cm/s)</center>]]` (39); `\|style="width:20%"\|` (40); `[[Image:wvel_his_2.png\|none\|thumb\|180px\|<center>W-velocity (m/day)</center>]]` (41); `\|style="width:20%"\|` (42); `[[Image:omega_his_2.png\|none\|thumb\|180px\|<center>Omega (m/day)</center>]]` (43); `\|-` (44). |
| 45–57 | Results / Day 1.5 — Day 1과 Day 2 사이 평균인 표 행에서 t_avg_1.5.png·uvel_avg_1.5.png·vvel_avg_1.5.png·wvel_avg_1.5.png·omega_avg_1.5.png를 참조한다(45–57). 캡션은 Temperature (Celsius), U/V-velocity (cm/s), W-velocity·Omega (m/day)이다. 다섯 그림 모두 그림 파일 없음. 표의 행·열 마크업·캡션·단위를 원문 그대로 옮긴다. 원문: `\|style="width:20%"\|` (45); `'''Day 1.5'''<br>average between Day&nbsp;1 and Day&nbsp;2` (46); `\|style="width:20%"\|` (47); `[[Image:t_avg_1.5.png\|none\|thumb\|180px\|<center>Temperature (Celsius)</center>]]` (48); `\|style="width:20%"\|` (49); `[[Image:uvel_avg_1.5.png\|none\|thumb\|180px\|<center>U-velocity (cm/s)</center>]]` (50); `\|style="width:20%"\|` (51); `[[Image:vvel_avg_1.5.png\|none\|thumb\|180px\|<center>V-velocity (cm/s)</center>]]` (52); `\|style="width:20%"\|` (53); `[[Image:wvel_avg_1.5.png\|none\|thumb\|180px\|<center>W-velocity (m/day)</center>]]` (54); `\|style="width:20%"\|` (55); `[[Image:omega_avg_1.5.png\|none\|thumb\|180px\|<center>Omega (m/day)</center>]]` (56); `\|}` (57). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13행: `upwelling_domain.png`와 Upwelling Domain 캡션을 참조한다. 그림 파일 없음.
- 22행: `t_his_0.png`와 Temperature (Celsius) 캡션을 참조한다. 그림 파일 없음.
- 24행: `uvel_his_0.png`와 U-velocity (cm/s) 캡션을 참조한다. 그림 파일 없음.
- 26행: `vvel_his_0.png`와 V-velocity (cm/s) 캡션을 참조한다. 그림 파일 없음.
- 28행: `wvel_his_0.png`와 W-velocity (m/day) 캡션을 참조한다. 그림 파일 없음.
- 30행: `omega_his_0.png`와 Omega (m/day) 캡션을 참조한다. 그림 파일 없음.
- 35행: `t_his_2.png`와 Temperature (Celsius) 캡션을 참조한다. 그림 파일 없음.
- 37행: `uvel_his_2.png`와 U-velocity (cm/s) 캡션을 참조한다. 그림 파일 없음.
- 39행: `vvel_his_2.png`와 V-velocity (cm/s) 캡션을 참조한다. 그림 파일 없음.
- 41행: `wvel_his_2.png`와 W-velocity (m/day) 캡션을 참조한다. 그림 파일 없음.
- 43행: `omega_his_2.png`와 Omega (m/day) 캡션을 참조한다. 그림 파일 없음.
- 48행: `t_avg_1.5.png`와 Temperature (Celsius) 캡션을 참조한다. 그림 파일 없음.
- 50행: `uvel_avg_1.5.png`와 U-velocity (cm/s) 캡션을 참조한다. 그림 파일 없음.
- 52행: `vvel_avg_1.5.png`와 V-velocity (cm/s) 캡션을 참조한다. 그림 파일 없음.
- 54행: `wvel_avg_1.5.png`와 W-velocity (m/day) 캡션을 참조한다. 그림 파일 없음.
- 56행: `omega_avg_1.5.png`와 Omega (m/day) 캡션을 참조한다. 그림 파일 없음.
