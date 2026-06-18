# 기대 I/O · 검증 포인트

> 절차 템플릿 — 정량 run 미수록. 실행 시 산출물·검증 항목.

## 산출물

| 파일 | 내용 |
|---|---|
| `trim-<runid>.dat/.def` | FLOW map: 수위·유속·**bed level 변화(DPS)**·sediment 농도·transport |
| `trih-<runid>.dat/.def` | FLOW history(관측점 시계열) |
| `com-<runid>.dat` | FLOW↔WAVE 교환 필드(Hs/Tp/dir·wsu/wsv/fxw/fyw) |
| `wavm-<runid>.dat` | WAVE map(파장) |

## 검증 포인트

1. **결합 작동**: COM 파일에 radiation stress(`wsu/wsv/fxw/fyw`)가 매 itcomi 갱신되는지. FLOW 가 파력으로 wave setup·longshore current 생성하는지([[../../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling]] WaveOL).
2. **bed 갱신**: bed level(DPS) 변화가 transport 발산과 정합(Exner)인지([[../../../models/Delft3D/source-analysis/delft3d_sediment_morphology]] bott3d).
3. **MorFac 영향**: MorFac 변경 시 형태변화율 선형 비례 + 안정성 — 과대 MorFac 시 진동/비물리 bed. spin-up(MorStt) 후 morphology 시작 확인.
4. **질량 보존**: sediment budget(유입−유출−bed 변화) 폐합.

## 관련 검수 노트

- online morphology: [[../../../models/Delft3D/source-analysis/delft3d_sediment_morphology]] (erosed·bott3d·MORFAC)
- transport 공식: [[../../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae]]
- FLOW-WAVE 결합: [[../../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling]]
- 개념: [[../../../concepts/littoral-drift/06-model-application]] (연안표사 모델 적용)
