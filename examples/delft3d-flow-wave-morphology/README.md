# Delft3D FLOW + WAVE + online morphology (해빈·하구 형태변화 결합)

> **Delft3D-FLOW**(수리)·**Delft3D-WAVE**(SWAN 파)·**online morphology**(표사→bed 갱신)를 한 시뮬레이션으로 양방향 결합하는 **형태동역학(morphodynamic) 워크플로**. 파(radiation stress)→흐름→표사 수송→해저 변화→(다시 파/흐름)의 피드백을 **MORFAC** 가속으로 장기 모의. 해빈 침식·하구 사주·연안표사 등.

## 다루는 개념·모델

- 개념: [`concepts/sediment-transport`](../../concepts/sediment-transport/)(표사 수송 공식)·[`concepts/littoral-drift`](../../concepts/littoral-drift/)(연안표사)·[`concepts/waves`](../../concepts/waves/)(radiation stress)
- 모델: [`models/Delft3D`](../../models/Delft3D/) (FLOW + WAVE + morphology)
- 결합 메커닉(검수 근거):
  - online morphology: [`delft3d_sediment_morphology`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md) — `erosed.f90`(erosion/deposition source/sink)·**`bott3d.f90` bed update(BODSED 변화=Exner)**·**`updmorfac`**(형태가속계수, `bott3d.f90:554`). canonical = Lesser et al. 2004.
  - 수송 공식: [`delft3d_sediment_transport_formulae`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md) (van Rijn·Bijker·Soulsby, `iform`)
  - FLOW↔WAVE 결합: [`wave/delft3d_flow_wave_coupling`](../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling.md) — **COM 파일** 교환, `WaveOL` flag, radiation stress `wsu/wsv/fxw/fyw`, 결합주기 `itcomi`/`Flpp`(≠TWAVE), roller
  - WAVE 설정: [`delft3d-wave-user-manual`](../../models/Delft3D/manual-notes/delft3d-wave-user-manual.md)
  - 오케스트레이션: [`delft3d_dimr_coupling`](../../models/Delft3D/source-analysis/delft3d_dimr_coupling.md) (DIMR)

## 워크플로 (실행 순서)

```
DIMR (dimr_config.xml) 가 FLOW·WAVE 를 교대 구동:
1. WAVE(SWAN) run → 파장(Hs·Tp·dir) + radiation stress 를 COM 파일에 기록
2. FLOW run (itcomi 간격으로 COM 읽음) → 파력(wsu/wsv/fxw/fyw)으로 흐름·setup 계산
   + online morphology: erosed(표사 source/sink) → bott3d(BODSED bed 갱신=Exner)
3. bed 변화 → (MORFAC 가속) → 다음 WAVE/FLOW 스텝에 갱신된 지형 반영
→ 반복 (양방향 morphodynamic feedback)
```

## 입력 파일 (code/)

| 파일 | 역할 |
|---|---|
| [`code/dimr_config.xml`](code/dimr_config.xml) | DIMR 결합 제어 (FLOW↔WAVE 순서·주기) |
| [`code/flow.mdf`](code/flow.mdf) | FLOW: 격자·수심·경계·sediment 참조·morphology on |
| [`code/wave.mdw`](code/wave.mdw) | WAVE(SWAN): 파 경계·물리·FLOW 격자 nesting |
| [`code/sediment.sed`](code/sediment.sed) | 표사 물성(입경·밀도·sand/mud) |
| [`code/morphology.mor`](code/morphology.mor) | **MORFAC**·bed update·transport formula(`iform`)·spin-up |

## 재현 조건

- Delft3D 4 (structured flow2d3d) — FLOW+WAVE+MOR 라이선스. DIMR 실행기.
- WAVE 격자가 FLOW 격자를 포함(nesting). COM 파일 경로 일치.
- **MORFAC** 선택이 핵심 trade-off: 클수록 장기 morphodynamic 가속이나 안정성·정확도 저하([`delft3d_sediment_morphology §후속`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md)). spin-up(morphology 지연 시작)으로 초기 transient 회피.
- ⚠ **본 예제는 검수 메커닉·매뉴얼 기반 절차 템플릿**(값은 placeholder, 정량 run 미수록).

## 본 위키 연계

연안표사([`littoral-drift/06`](../../concepts/littoral-drift/06-model-application.md))의 process-based 모델 적용 = 본 워크플로. 특정 한국 사례 적용은 본 위키 범위 밖(실 적용은 데이터·검증 확보 후 `experience/`). full-physics 형태동역학의 대표 예 — reduced-complexity([`SFINCS`](../../models/SFINCS/))는 형태변화 미포함.
