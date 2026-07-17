---
title: "ShorelineS coastline_change.m — one-line 이산화(staggered FTCS)·Bruun SLR·groyne 부착/자동연장·사구/mud 결합"
model: ShorelineS
component: functions/coastline_change.m
canonical_source: self
citation_status: verified
verification_method: "sha 7bf4481ab — coastline_change.m 440줄 전문 직접 read. 이산식·결합항 라인 인용, Roelvink et al. 2020 Eq.1·Eq.5 와 대조(manual-notes 참조)."
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/source-analysis/shorelines-transport-formulations.md
  - models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md
---

# coastline_change.m — 해안선 갱신 코어

> PHASE 2 의 본체(440줄). 논문 Eq.1(질량보존)·Eq.5(staggered explicit)의 코드 실체.

## 1. one-line 이산화 (`:301-318`, `:356-391`)

- **staggered**: QS 는 transport 점(nq), 해안선은 점(n). `ds(i)=hypot(x(i+1)−x(i−1),y(i+1)−y(i−1))/2`(:314), `dSds(i)=(QS(i+1q)−QS(iq))/ds(i)`(:316), `dndt(i)=−dSds/h0(i)`(:317) — **능동높이 h0 = Dc**(논문 Eq.1). forward-time central-space explicit(논문 Eq.5).
- **위치 갱신**: `dn=(dndt+dndtnour−SLRo/tanbeta)·dt`(:365) — 양빈(육상 rate_density + shoreface FNOUR.q_tot, :319) 가산·**SLR 은 Bruun형 후퇴항 `−SLR/tanβ`**. 이동은 국소 법선 방향(접선 회전 :380-381), 옵션 `preserveorientation` 은 초기 방위 고정(:367-372), 단부는 PHIcxy0 방위(:373-378). cyclic 섹션은 끝점 평균 봉합(:392-399).
- 수치 보호: ds 하한 eps=1e-3(:315), 빈 섹션 sentinel −1e10(:412-417).

## 2. groyne 경계 처리 (`:141-296`)

- **우회(bypass) 방향 판정**(:142-156): 양측 QS 발산→0 / 동부호→최대측 채택 / 수렴→합산.
- **차폐구간 분배**(:179-217): bypass 량을 그림자 구간에 **삼각분포^pwr**(`bypassdistpwr`)로 가산 — pwr>1 이면 구조물 인접 퇴적 집중.
- **해안선-구조물 부착**(:220-295): 해안선 끝점을 groyne 둘레 경로 shard 위 보간점으로 핀(:289-290). 끝점 침식 dn 은 국소 수지+양빈+SLR 로 산출(:244-249, mud 는 가산 :246-248).
- ★**구조물 자동 연장**(:255-286): 침식이 groyne 육측 끝을 넘으면 **구조물 다리를 육지쪽으로 연장**(epsgroyne=1 m 여유)하고 STRUC 좌표를 갱신 — 사용자 통보는 모델단 없음(런 후 구조물 길이가 입력과 다를 수 있음, 검수 관찰). 인접 배치 오류 시 ds0 대체 + 경고(:235).

## 3. 프로세스 결합 (`:321-354`)

- **사구**(DUNE.used, :322-337): `dndt += (qss−qw)/h0`(:325 — 사구침식 모래분 qss 는 해빈 공급, 바람 되돌림 qw 차감), berm 폭 wberm 별도 부기(:327-332, 하한 1 m)·사구 기저/정상고 _mc 동기.
- **mud 해안**(MUD.used): 일반 구간은 `dndt = dndt_mud` 로 **대체**(:342), groyne 인접점은 **가산**(:247) — 두 경로 처리 상이(관찰: mud 모드에선 모래 QS 경사항이 일반 구간에서 무시됨; transport_mud 가 파랑·조석·바람 유량 기반 농도수지로 dndt_mud 를 산출하므로 설계 의도로 보이나 groyne 점과의 비대칭은 disclosed). 갯벌 Bf·맹그로브 Bm·개척 맹그로브 Bfm 폭 상태를 [Bmmin,Bmmax] 클램프로 갱신(:344-353).

## 4. 논문 대조 (Roelvink et al. 2020)

| 논문 | 코드 |
|---|---|
| Eq.1 `∂n/∂t=−(1/Dc)∂Qs/∂s−RSLR/tanβ+(1/Dc)Σqi` (p.4) | :317 + :365 (RSLR·qi=양빈/사구/fnour) |
| Eq.5 staggered FTCS, Li 중심차 (p.5) | :314-317 |
| 고각도 upwind(임계각 고정) (p.5) | transport.m:125-137 (각도 클램프판) |
