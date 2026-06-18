# examples/

개념을 가로지르는 통합 실습. `concepts/<topic>/05-examples.md`가 단일 토픽 내 예제라면, 여기는 **여러 토픽·모델을 결합**한 시나리오.

## 구조

```
examples/
├── <scenario-name>/
│   ├── README.md         # 시나리오 설명, 다루는 개념·모델
│   ├── data/             # (선택) 입력 데이터
│   ├── code/             # 재현 코드
│   └── results/          # 결과·해석
```

## 작성 규칙

- **재현 가능**해야 함. 데이터 위치·환경·실행 순서 명시.
- 개인 결론 대신 **객관 비교** 위주. "내가 해보니" 화법 금지.
- 사용 모델·개념 명시: 상단에 `concepts/...`, `models/...` 링크.
- 사용 textbook 자료는 `textbook/notes/...`로 인용.

## 예제

| 시나리오 | 다루는 개념 | 사용 모델/도구 | 상태 |
|---|---|---|---|
| [swan-to-swash-nesting](swan-to-swash-nesting/) | waves · swash-zone | SWAN → SWASH | ✅ 절차 템플릿 (검수 메커닉 기반, 정량 run 미수록) |
| [khoa-surge-eva-pipeline](khoa-surge-eva-pipeline/) | storm-surge · tides | utide → EVA (experience 연계) | ✅ 재현 절차 (정량은 experience 귀속) |
| [adcirc-swan-surge-coupling](adcirc-swan-surge-coupling/) | storm-surge · waves · compound-flooding | ADCIRC + SWAN (tightly-coupled, radiation stress) | ✅ 절차 템플릿 (검수 메커닉 기반, 정량 run 미수록) |

## 후보 (다음)

| 시나리오 | 다루는 개념 | 사용 모델 |
|---|---|---|
| delft3d-flow-wave-morphology | sediment-transport · littoral-drift | Delft3D FLOW+WAVE+morphology |
