---
file: models/ROMS/raw/manuals/wiki/wikitext/SHOREFACE_CASE.wiki
lines: 31
sha256: a95a9b2757952e4c48f1e1900e7e4c76aa44633c17e143d183f3cbf6adef65ea
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# SHOREFACE_CASE.wiki — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | Shore Face Planar Beach Test Case — 경사 해빈(planar beach)에 비스듬히 입사하는 스펙트럼 파랑(spectral waves) 시험과 Haas·Warner(2009) 문헌을 소개한다(1–5). 경사·파고·첨두 주기(peak period)·입사각·방향 및 주파수 구간 수·주파수 범위를 원문 그대로 적는다(7). SWAN을 먼저 단독 실행하여 강제력 파일을 만들며 흐름의 파랑 피드백과 roller 기여를 포함하지 않는다(9–12). 수심 평균 흐름으로 이차 저면 응력을 계산하고 정상 상태(steady state)의 결과를 제시한다고 적는다(12–14). 원문: `The case consists of spectral waves approaching a mild sloping (1/80) plane beach with an oblique angle of incidence. The wave forcing is obtained by first running SWAN separately by specifying a JONSWAP spectrum for 2 m offshore wave height with a peak period of 10 s at an angle of 10 degrees for the incoming wave field. SWAN was configured to use 90 directional bins and 30 frequency bins between 0.04 and 0.5 Hz.` (7); `Data/ROMS/Forcing/swan_shoreface_angle_forc.nc` (10); `The circulation model computes the radiation stress forcing based on the SWAN wave output. For this application there is not a feedback of the currents to the wave model. Also we neglect the contribution from the roller model. The circulation model uses a quadratic bottom stress formulation using the depth average currents.` (12). |
| 16–25 | Output Files / 그림 참조 — history 출력 파일 링크를 제시한다(16). shoreface_fig1.jpg의 캡션은 횡단 방향 파고·수심·수위 상승(wave setup)·수심 적분 횡단류·연안류와 실선·파선의 모델 구분을 적는다(20). shoreface_fig2.jpg의 캡션은 위쪽 횡단 유속과 아래쪽 연안 유속의 수직 분포를 비교한다(23). 두 그림 모두 그림 파일 없음. 원문: `'''Output Files:'''  [[media:SHOREFACE_hishis.nc \| history file (shoreface_ocean_his.nc) ]].` (16); `[[Image:shoreface_fig1.jpg\|thumb\|850px\|none\|<center><b>Figure 1:</b> Plane beach test case results showing cross-shore variation of: (a) significant wave height (dashed) and bathymetry (solid); (b) wave setup; (c) depth-integrated cross shore currents; and (d) depth-integrated longshore currents. SHORECIRC results are solid lines, ROMS results are dashed lines (for panels b, c, and d). </center>]]` (20); `[[Image:shoreface_fig2.jpg\|thumb\|850px\|none\|<center><b>Figure 1:</b> Plane beach test case results comparing cross-shore variations of the vertical profiles of currents of: (top) cross-shore velocities; and (bottom) longshore velocities. SHORECIRC results are solid lines, ROMS results are dashed lines.</center>]]` (23). |
| 26–31 | 결과 해설 — x=600 m 근처에서 쇄파 소산(wave breaking dissipation)으로 파고가 줄어든다고 적는다(26–27). 두 순환 모델의 수심 평균 강제력은 같고 수위 상승·평균 저층 복귀류(undertow)·연안류는 유사하나 해안 부근은 경계 처리 차이가 있다고 설명한다(27). 수심별 복사 응력(radiation stress)과 쇄파대 밖 복귀류 수직 구조는 다르다고 적는다(29). 추가 설명 문헌을 제시한다(31). 원문: `The waves begin to decrease near x = 600 m due to wave breaking dissipation. The wave fields computed from SWAN are used in each circulation model to compute the radiation stress forcing. The depth-averaged forcing as computed by each circulation model is identical and the resulting wave setup (Fig. 1b) is very similar for the two models. Similarly the depth averaged undertow and longshore currents (Fig. 1c and d) match for the two models, except near the shoreline due to different treatments of that lateral BC.` (27); `However, the depth varying radiation stress components computed in each circulation model are different. The vertical structure of the longshore and cross-shore currents is shown in Fig. 2. Both models produce the classical undertow profile inside the surf zone. Outside the surf zone (x < 600 m), SHORECICRC is producing undertow with fairly depth uniform or a slightly increased flow near the surface in accordance with Putrevu and Svendsen (1993), whereas, ROMS is producing undertow which is still stronger in the lower part of the water column, albeit with much less curvature than inside the surf zone.` (29). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 20행: `shoreface_fig1.jpg`와 결과 비교 캡션을 참조한다. 그림 파일 없음.
- 23행: `shoreface_fig2.jpg`와 유속 수직 분포 캡션을 참조한다. 그림 파일 없음.
- 20·23·29행: 두 그림 캡션은 모두 `Figure 1`로 표시되지만 뒤 본문은 수직 유속 구조를 `Fig. 2`로 참조한다.
