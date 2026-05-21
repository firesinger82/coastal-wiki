# concepts/tides — 조석

## 상태

`TBD` — 디렉토리 생성됨, 내용 미작성.

## 작성 우선순위 (사용자 우선 예시 토픽)

1. `01-concept.md` — 조석의 정의, 천체역학적 원인, 분조의 개념
2. 관련 textbook 노트 추출:
   - `134340780-Tides-and-Currents.pdf` → `textbook/notes/tides-tides-and-currents-chN.md`
   - `Manual_for_Tidal_Heights_Analysis_and_Pr.pdf` → 조위 분석 매뉴얼
3. `02-theory.md` — 평형조석 이론, Laplace 조석방정식, 분조
4. `03-analysis-methods.md` — 조화분해, t_tide, UTide, 비조화 분석
5. `04-code-and-tools.md` — t_tide(MATLAB), UTide(Python), pytides
6. `06-model-application.md` — EFDC tidal forcing (`models/EFDC/`), ADCIRC tidal db

## 작업 시작

```bash
cp -r ../_template/* .
rm README.md  # 또는 이 README는 자동 채워질 때까지 보존
```

세부 절차는 [../_template/README.md](../_template/README.md) 참조.
